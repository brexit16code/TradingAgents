"""Financial accounting, chronology and persistence of the fictional forward experiment."""

import copy
import json
import sys
from datetime import datetime

import pandas as pd
import pytest

from ibex.paper import (
    MADRID,
    POLICY,
    advance,
    bars_from_history,
    load_market,
    main,
    summary,
    validate_account,
)
from ibex.paper_render import write_portfolio, write_signal_archive

SUNDAY = datetime(2026, 11, 1, 20, 0, tzinfo=MADRID)
MONDAY = SUNDAY.replace(day=2)
TUESDAY = SUNDAY.replace(day=3)
WEDNESDAY = SUNDAY.replace(day=4)


def report(now=SUNDAY, rating="Buy", ticker="AAA.MC"):
    return {"date": now.date().isoformat(), "generated_at": now.isoformat(),
            "timezone": "Europe/Madrid", "universe": {"verified": True, "note": "BME verificado", "revision_date": "2026-09-21", "source": "https://example.org"},
            "companies": [{"ticker": ticker, "name": "Empresa A", "status": "ok", "stale": False,
                           "retrieved_at": now.isoformat(), "technical": {"price_date": "2026-10-30", "close": 10},
                           "fundamentals": {"currency": "EUR"}, "screen": {"label": "Vigilar favorable", "reasons": [], "risks": []},
                           "sources": {"quote": "https://example.org", "financials": "https://example.org"},
                           "agents": {"status": "completed", "rating": rating, "decision": "Justificación de la señal", "model": "free", "report": f"agents/{ticker}/complete_report.html"}}]}


def bar(day, opened=10, close=10, dividend=0, split=0):
    return {"date": day, "open": opened, "close": close, "dividend": dividend, "split": split}


def market(*extra):
    result = {"AAA.MC": [bar("2026-10-30"), *extra],
              "^IBEX": [bar("2026-10-30", 100, 100)]}
    result["^IBEX"] += [bar(b["date"], 100, 100) for b in extra]
    return result


def started(rating="Buy"):
    return advance(None, report(rating=rating), market(), SUNDAY)[0]


def test_sunday_registers_a_signal_but_does_not_trade_fridays_close_or_future_bars():
    state, archive = advance(None, report(), market(bar("2026-11-02", 30, 31)), SUNDAY)
    assert state["cash"] == 10000
    assert state["trades"] == []
    assert state["positions"] == {}
    assert state["status"] == "pending_market"
    assert state["orders"][0]["after"] == "2026-11-01"
    assert archive["companies"][0]["decision"] == "Justificación de la señal"
    assert summary(state)["profit"] == 0


def test_same_day_report_never_buys_at_an_open_that_precedes_its_registration():
    state, _ = advance(None, report(MONDAY), market(bar("2026-11-02", 10, 20)), MONDAY)
    assert not state["trades"]
    assert state["orders"][0]["after"] == "2026-11-02"


@pytest.mark.parametrize("exit_price,expected", [(11, 92.92), (9, -104.88)])
def test_buy_hold_sell_uses_later_opens_slippage_both_fees_and_exact_cash(exit_price, expected):
    first = started()
    second, _ = advance(first, report(MONDAY, "Sell"), market(bar("2026-11-02", 10, 10)), MONDAY)
    assert len(second["trades"]) == 1
    assert second["positions"]["AAA.MC"]["quantity"] == 99
    assert second["positions"]["AAA.MC"]["basis"] == 992.99
    assert second["cash"] == 9007.01
    assert second["orders"][-1]["side"] == "SELL"
    third, _ = advance(second, report(TUESDAY, "Hold"), market(bar("2026-11-02"), bar("2026-11-03", exit_price, exit_price)), TUESDAY)
    assert not third["positions"]
    assert summary(third)["realized"] == expected
    assert summary(third)["profit"] == expected
    assert third["cash"] == 10000 + expected
    assert summary(third)["fees"] == 4
    assert len(third["trades"]) == 2
    validate_account(third)
    assert not first["trades"]  # The input experiment is never mutated.


@pytest.mark.parametrize("rating", ["Hold", "Mantener", "Sell", "Vigilar favorable", "Unknown"])
def test_hold_sell_without_a_position_and_rule_filter_never_open_a_buy(rating):
    assert not started(rating)["orders"]


def test_a_later_hold_cancels_a_pending_buy_without_rewriting_the_original_signal():
    state = started()
    updated, archive = advance(state, report(SUNDAY.replace(hour=21), "Hold"), market(), SUNDAY.replace(hour=21))
    assert updated["orders"][0]["status"] == "cancelled"
    assert state["orders"][0]["status"] == "pending"
    assert len(updated["sources"]) == 2
    assert archive["companies"][0]["rating"] == "Hold"


def test_repeating_the_same_report_does_not_duplicate_signals_or_orders():
    state = started()
    repeated, archive = advance(state, report(), market(), SUNDAY.replace(hour=22))
    assert archive is None
    assert len(repeated["sources"]) == 1
    assert len(repeated["orders"]) == 1


def test_ten_positions_maximum_whole_shares_no_borrowing_and_deterministic_selection():
    data = report()
    data["companies"] = []
    prices = market(bar("2026-11-02"))
    for i in reversed(range(12)):
        ticker = f"T{i:02d}.MC"
        row = report(ticker=ticker)["companies"][0]
        data["companies"].append(row)
        prices[ticker] = [bar("2026-10-30"), bar("2026-11-02")]
    state, _ = advance(None, data, prices, SUNDAY)
    after, _ = advance(state, {**data, "date": "2026-11-02"}, prices, MONDAY)
    assert set(after["positions"]) == {f"T{i:02d}.MC" for i in range(10)}
    assert after["cash"] == 70.10
    assert len([o for o in after["orders"] if o["status"] == "rejected"]) == 2
    assert all(t["quantity"].is_integer() for t in after["trades"])


def test_missing_open_pauses_without_fabricating_a_fill_and_recovery_replays_once():
    state = started()
    prices = market(bar("2026-11-02"))
    prices["AAA.MC"] = [bar("2026-10-30")]
    blocked, archive = advance(state, report(MONDAY, "Sell"), prices, MONDAY)
    assert blocked["status"] == "paused"
    assert blocked["cursor"] == "2026-11-01"
    assert not blocked["trades"]
    assert archive is None
    fixed, _ = advance(blocked, report(MONDAY, "Sell"), market(bar("2026-11-02")), MONDAY)
    assert len(fixed["trades"]) == 1
    assert len(fixed["valuations"]) == 1
    repeated, _ = advance(fixed, report(MONDAY, "Sell"), market(bar("2026-11-02")), MONDAY)
    assert repeated["trades"] == fixed["trades"]


def test_intraday_data_and_future_prices_cannot_be_settled_early():
    state, _ = advance(started(), report(MONDAY.replace(hour=11), "Hold"), market(bar("2026-11-02", 10, 90)), MONDAY.replace(hour=11))
    assert not state["trades"]
    assert not state["valuations"]


@pytest.mark.parametrize("problem", ["future", "old", "unverified", "currency", "stale", "missing_ai", "future_price"])
def test_unusable_evidence_does_not_create_orders(problem):
    data = report()
    row = data["companies"][0]
    if problem == "future":
        data["generated_at"] = SUNDAY.replace(hour=23).isoformat()
    elif problem == "old":
        data["date"] = "2026-10-30"
    elif problem == "unverified":
        data["universe"]["verified"] = False
    elif problem == "currency":
        row["fundamentals"]["currency"] = "USD"
    elif problem == "stale":
        row["stale"] = True
    elif problem == "missing_ai":
        row["agents"]["status"] = "failed"
    else:
        row["technical"]["price_date"] = "2026-11-02"
    state, _ = advance(None, data, market(), SUNDAY)
    assert not state["orders"]
    assert state["warnings"]


def test_split_preserves_value_and_dividend_is_owed_only_to_previous_holders():
    prices = market(bar("2026-11-02", 10, 10, dividend=1), bar("2026-11-03", 5, 5, dividend=.25, split=2))
    state, _ = advance(started(), report(MONDAY, "Hold"), prices, MONDAY)
    assert not state["dividends"]  # Buying on ex-date is too late for that dividend.
    after, _ = advance(state, report(TUESDAY, "Sell"), prices, TUESDAY)
    assert after["positions"]["AAA.MC"]["quantity"] == 198
    assert after["positions"]["AAA.MC"]["basis"] == 992.99
    assert summary(after)["market_value"] == 990
    assert summary(after)["dividends"] == 49.50
    assert after["cash"] == 9007.01  # Accrued dividends cannot fund new purchases.
    assert summary(after)["profit"] == 46.51
    repeated, _ = advance(after, report(TUESDAY, "Sell"), prices, TUESDAY)
    assert len(repeated["dividends"]) == 1
    assert len(repeated["splits"]) == 1


def test_yahoo_split_adjusted_history_is_reconstructed_before_action_replay():
    frame = pd.DataFrame({"Open": [50, 50, 51], "Close": [50, 50, 51],
                          "Dividends": [.25, .5, 0], "Stock Splits": [0, 2, 0]},
                         index=pd.to_datetime(["2026-11-02", "2026-11-03", "2026-11-04"]))
    bars = bars_from_history(frame)
    assert bars[0] == bar("2026-11-02", 100, 100, .5)
    assert bars[1] == bar("2026-11-03", 50, 50, .5, 2)
    assert bars[2] == bar("2026-11-04", 51, 51)


def test_ex_date_entitlement_survives_a_sale_at_that_days_open():
    state, _ = advance(started(), report(MONDAY, "Sell"), market(bar("2026-11-02")), MONDAY)
    after, _ = advance(state, report(TUESDAY, "Hold"), market(bar("2026-11-02"), bar("2026-11-03", 10, 10, dividend=1)), TUESDAY)
    assert not after["positions"]
    assert summary(after)["dividends"] == 99
    assert summary(after)["profit"] == pytest.approx(summary(after)["realized"] + 99)


def test_invalid_balance_changed_policy_and_backdated_updates_never_reset_an_experiment():
    state = started()
    tampered = copy.deepcopy(state)
    tampered["cash"] = 20000
    with pytest.raises(ValueError, match="efectivo"):
        advance(tampered, report(), market(), SUNDAY)
    tampered = copy.deepcopy(state)
    tampered["policy"]["commission"] = 0
    with pytest.raises(ValueError, match="reglas"):
        advance(tampered, report(), market(), SUNDAY)
    with pytest.raises(ValueError, match="retroceder"):
        advance(state, report(), market(), SUNDAY.replace(hour=19))


def test_benchmark_is_a_price_index_and_cash_has_no_invented_stock_return():
    state = started("Hold")
    prices = market(bar("2026-11-02"))
    prices["^IBEX"][-1].update(open=100, close=110)
    after, _ = advance(state, report(MONDAY, "Hold"), prices, MONDAY)
    assert summary(after)["profit"] == 0
    assert after["valuations"][-1]["ibex_return_pct"] == 10


def test_missing_benchmark_or_missing_historical_coverage_pauses():
    state = started()
    after, _ = advance(state, report(MONDAY), {"AAA.MC": []}, MONDAY)
    assert after["status"] == "paused"
    prices = market(bar("2026-11-02"))
    prices["^IBEX"] = prices["^IBEX"][-1:]
    after, _ = advance(state, report(MONDAY), prices, MONDAY)
    assert after["status"] == "paused"
    assert not after["trades"]


def test_fictional_pages_escape_untrusted_text_and_link_the_frozen_source(tmp_path):
    data = report()
    data["companies"][0]["name"] = '<img src=x onerror=alert(1)>'
    data["companies"][0]["agents"]["decision"] = '<script>alert(1)</script>'
    state, archive = advance(None, data, market(), SUNDAY)
    (tmp_path / "paper-history").mkdir()
    write_signal_archive(archive, tmp_path)
    write_portfolio(state, tmp_path)
    page = (tmp_path / "cartera.html").read_text()
    snapshot = (tmp_path / archive["path"].replace(".json", ".html")).read_text()
    assert '<img src=x' not in page
    assert '<script>alert(1)</script>' not in snapshot
    assert '&lt;script&gt;' in snapshot
    assert archive["path"].replace(".json", ".html") in page
    assert "sin dividendos" in page and "sin impuestos" in page


def test_cli_preserves_corrupted_history_instead_of_resetting_cash(tmp_path, monkeypatch):
    previous = tmp_path / "previous"
    output = tmp_path / "output"
    previous.mkdir()
    (previous / "cartera.json").write_text('{"version": 99}')
    report_path = tmp_path / "datos.json"
    report_path.write_text(json.dumps(report()))
    monkeypatch.setattr(sys, "argv", ["paper", "--report", str(report_path), "--previous", str(previous / "cartera.json"), "--output", str(output)])
    with pytest.raises(ValueError, match="reinicia"):
        main()
    assert (output / "cartera.json").read_text() == '{"version": 99}'
    assert not (output / "cartera.html").exists()


def test_policy_budget_includes_entry_fee_and_exit_never_short_sells():
    assert POLICY["entry_budget"] * POLICY["max_positions"] == POLICY["initial_cash"]
    state, _ = advance(None, report(rating="Sell"), market(), SUNDAY)
    assert not state["orders"]
    assert state["cash"] == 10000


def test_complete_cli_saves_durable_evidence_links_and_resumes_without_reset(tmp_path, monkeypatch):
    import ibex.paper as paper_module

    class Clock(datetime):
        @classmethod
        def now(cls, tz=None):
            return SUNDAY

    monkeypatch.setattr(paper_module, "datetime", Clock)
    monkeypatch.setattr(paper_module, "load_market", lambda *_: market())
    report_path = tmp_path / "datos.json"
    report_path.write_text(json.dumps(report()))
    previous = tmp_path / "cartera.json"
    monkeypatch.setattr(sys, "argv", ["paper", "--report", str(report_path), "--previous", str(previous), "--output", str(tmp_path)])
    main()
    state = json.loads(previous.read_text())
    frozen_path = tmp_path / state["sources"][0]["path"]
    first_evidence = frozen_path.read_bytes()
    assert frozen_path.with_suffix(".html").is_file()
    assert 'href="cartera.html"' in (tmp_path / "index.html").read_text()
    assert len(state["orders"]) == 1
    main()
    updated = json.loads(previous.read_text())
    assert updated["started_at"] == state["started_at"]
    assert len(updated["orders"]) == len(updated["sources"]) == 1
    assert frozen_path.read_bytes() == first_evidence


def test_orphaned_archive_is_not_silently_reset(tmp_path, monkeypatch):
    (tmp_path / "paper-history").mkdir()
    path = tmp_path / "datos.json"
    path.write_text(json.dumps(report()))
    monkeypatch.setattr(sys, "argv", ["paper", "--report", str(path), "--previous", str(tmp_path / "cartera.json"), "--output", str(tmp_path)])
    with pytest.raises(ValueError, match="reiniciarla"):
        main()


def test_intraday_split_is_used_to_restore_old_prices_but_not_settled_early(monkeypatch):
    calls = []

    def history(ticker, now, *, include_open_session):
        calls.append(include_open_session)
        return pd.DataFrame({"Open": [5, 5, 5], "Close": [5, 5, 999],
                             "Dividends": [0, 0, 0], "Stock Splits": [0, 0, 2]},
                            index=pd.to_datetime(["2026-10-30", "2026-11-02", "2026-11-03"]))

    monkeypatch.setattr("ibex.data.history_for", history)
    state = started()
    now = TUESDAY.replace(hour=11)
    prices = load_market(state, report(now, "Hold"), now)
    updated, _ = advance(state, report(now, "Hold"), prices, now)
    assert all(calls)
    assert updated["trades"][0]["open"] == 10
    assert updated["positions"]["AAA.MC"]["quantity"] == 99
    assert updated["positions"]["AAA.MC"]["last_close"] == 10
    assert not updated["splits"]
