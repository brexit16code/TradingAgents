"""Data integrity and cost gates for the IBEX reporting integration."""

import copy
import io
import json
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import pytest

from ibex.agents import validate_llm_policy
from ibex.data import closed_history, company_headlines, rss_news, safe_url
from ibex.metrics import add_peer_valuations, fundamentals, relative_return, screen, technical
from ibex.render import save_report
from ibex.universe import load_universe, parse_revisions, verify_universe

NOW = datetime(2026, 10, 31, 20, 0, tzinfo=ZoneInfo("Europe/Madrid"))


def series(values, start="2025-01-01"):
    return pd.DataFrame({"Close": values, "Adj Close": values},
                        index=pd.bdate_range(start, periods=len(values), tz="Europe/Madrid"))


@pytest.mark.parametrize(("values", "expected"), [([5.0] * 250, 50),
                         (list(range(1, 251)), 100), (list(range(250, 0, -1)), 0)])
def test_rsi_constant_up_down_and_insufficient_history(values, expected):
    result = technical(series(values))
    assert result["rsi14"] == expected
    assert result["sma200"] is not None
    short = technical(series(values[:15]))
    assert short["sma200"] is None


def test_adjustment_avoids_a_false_signal_on_split():
    frame = series([10.0] * 250)
    frame.iloc[-2, frame.columns.get_loc("Close")] = 100
    result = technical(frame)
    assert result["close"] == 10
    assert result["change_pct"] == 0


def test_relative_return_aligns_dates_and_handles_short_series():
    benchmark = series(list(range(100, 200)))
    stock = benchmark * 2
    stock = stock.drop(stock.index[[3, 15, 28]])
    assert relative_return(stock, benchmark) == 0
    assert relative_return(stock.head(20), benchmark) is None


def test_intraday_bar_is_excluded_until_after_close():
    frame = series([100, 101], start="2026-10-29")
    early = datetime(2026, 10, 30, 17, 0, tzinfo=ZoneInfo("Europe/Madrid"))
    assert len(closed_history(frame, early)) == 1
    assert len(closed_history(frame, early.replace(hour=19))) == 2


def valid_row():
    company = {"ticker": "TEST.MC", "name": "Prueba", "kind": "corporate"}
    return {**company, "status": "ok", "stale": False, "warnings": [], "news": [],
            "retrieved_at": NOW.isoformat(), "technical": technical(series(range(1, 251))),
            "fundamentals": {"sector": "Utilities", "currency": "EUR", "revenueGrowth": .10},
            "valuation": {}, "sources": {"quote": "https://example.org", "financials": "https://example.org"}}


@pytest.mark.parametrize("mutation", ["unverified", "stale", "usd", "missing", "short"])
def test_uncertain_inputs_never_produce_a_favourable_signal(mutation):
    row = valid_row()
    if mutation == "stale":
        row["stale"] = True
    elif mutation == "usd":
        row["fundamentals"]["currency"] = "USD"
    elif mutation == "missing":
        row["status"] = "unavailable"
    elif mutation == "short":
        row["technical"]["sma200"] = None
    result = screen(row, mutation != "unverified")
    assert result["label"] == "Datos insuficientes"
    assert result["score"] is None


def test_bank_insurer_and_reit_do_not_receive_industrial_debt_rule():
    info = {"totalDebt": 1000, "totalCash": 0, "ebitda": 10,
            "dividendRate": 0.5, "currentPrice": 10, "dividendYield": 5}
    for kind in ("bank", "insurance", "reit"):
        assert fundamentals(info, {"kind": kind})["net_debt_ebitda"] is None
    values = fundamentals(info, {"kind": "corporate"})
    assert values["net_debt_ebitda"] == 100
    assert values["dividend_yield_pct"] == 5


def test_negative_pe_and_two_peers_are_not_usable_valuations():
    rows = [valid_row() for _ in range(3)]
    for row, pe in zip(rows, (10, 12, -3), strict=True):
        row["fundamentals"]["forwardPE"] = pe
    add_peer_valuations(rows)
    assert all("ratio" not in row["valuation"] for row in rows)
    rows[2]["fundamentals"]["forwardPE"] = 30
    add_peer_valuations(rows)
    assert rows[0]["valuation"]["peer_median_forward_pe"] == 12


def test_universe_has_35_madrid_symbols_and_current_redeia_symbol():
    companies = load_universe()["companies"]
    assert len(companies) == 35
    assert "RED.MC" in {c["ticker"] for c in companies}
    assert "REE.MC" not in {c["ticker"] for c in companies}


def test_bme_change_requires_revalidation_and_future_change_does_not(monkeypatch):
    import pypdf

    class Page:
        def extract_text(self):
            return "137 21/09/2026 - -\n138 20/12/2026 NUEVO VIEJO"

    monkeypatch.setattr(pypdf, "PdfReader", lambda _: type("PDF", (), {"pages": [Page()]})())
    monkeypatch.setattr("ibex.universe.urlopen", lambda *a, **kw: io.BytesIO(b"pdf"))
    assert verify_universe(load_universe(), NOW)["verified"]
    assert not verify_universe(load_universe(), NOW.replace(month=12, day=25))["verified"]
    revisions = parse_revisions("137 21/09/2026 — —\n138 20/12/2026 NUEVO VIEJO")
    assert revisions[0][2] == ""
    assert revisions[1][2] == "NUEVOVIEJO"


def test_missing_bme_response_is_not_a_verified_universe(monkeypatch):
    def fail(*a, **kw):
        raise OSError("offline")

    monkeypatch.setattr("ibex.universe.urlopen", fail)
    assert not verify_universe(load_universe(), NOW)["verified"]


def test_news_excludes_future_undated_and_old_articles(monkeypatch):
    xml = b'''<rss><channel>
    <item><title>Actual</title><link>https://example.org/current</link><pubDate>Fri, 30 Oct 2026 10:00:00 GMT</pubDate></item>
    <item><title>Futuro</title><link>https://example.org/future</link><pubDate>Sun, 01 Nov 2026 10:00:00 GMT</pubDate></item>
    <item><title>Sin fecha</title><link>https://example.org/undated</link></item>
    <item><title>Antiguo</title><link>https://example.org/old</link><pubDate>Fri, 01 Oct 2026 10:00:00 GMT</pubDate></item>
    </channel></rss>'''
    monkeypatch.setattr("ibex.data.urlopen", lambda *a, **kw: io.BytesIO(xml))
    assert [a["title"] for a in rss_news("Empresa", NOW)] == ["Actual"]
    assert safe_url("javascript:alert(1)") == ""
    assert safe_url("https://secret@example.org") == ""


def test_headline_relevance_excludes_publisher_matches_and_partial_names():
    articles = [{"title": "BBVA presenta resultados - Bankinter"},
                {"title": "Bankinter presenta resultados - Otro medio"},
                {"title": "Diageo sube - Otro medio"},
                {"title": "IAG presenta resultados - Otro medio"},
                {"title": "Red Eléctrica presenta resultados - Otro medio"}]
    assert company_headlines(articles, {"name": "Bankinter"}) == [articles[1]]
    assert company_headlines(articles, {"name": "IAG"}) == [articles[3]]
    assert company_headlines(articles, {"name": "Redeia"}) == [articles[4]]


def test_no_llm_calls_without_verified_free_tier_and_secret():
    with pytest.raises(ValueError):
        validate_llm_policy({})
    with pytest.raises(ValueError):
        validate_llm_policy({"GOOGLE_API_KEY": "dummy"})
    with pytest.raises(ValueError):
        validate_llm_policy({"IBEX_FREE_TIER_VERIFIED": "true"})
    validate_llm_policy({"IBEX_FREE_TIER_VERIFIED": "true", "GOOGLE_API_KEY": "dummy"})
    with pytest.raises(ValueError):
        validate_llm_policy({"IBEX_FREE_TIER_VERIFIED": "true", "GOOGLE_API_KEY": "dummy",
                             "IBEX_LLM_MODEL": "paid-model"})
    with pytest.raises(ValueError):
        validate_llm_policy({"IBEX_FREE_TIER_VERIFIED": "true", "GOOGLE_API_KEY": "dummy",
                             "IBEX_LLM_MODELS": "gemini-3.1-flash-lite,paid-model"})


@pytest.mark.parametrize("characters", [100, 80_000])
def test_free_tier_pacing_prevents_request_and_token_bursts(characters):
    from ibex.agents import FreeTierBudget

    now = [0.0]

    def advance(seconds):
        now[0] += max(seconds, 1e-8)

    budget = FreeTierBudget(clock=lambda: now[0], sleep=advance)
    starts = []
    for _ in range(30):
        budget.reserve(characters)
        starts.append(now[0])
    for started in starts:
        in_minute = [t for t in starts if started <= t < started + 60]
        assert len(in_minute) <= 12  # Below the account's 15 RPM.
        assert len(in_minute) * (characters + 10_000) <= 200_000
    assert budget.calls == 30


def test_free_tier_budget_rejects_calls_before_consuming_more_quota():
    from ibex.agents import BudgetExceeded, FreeTierBudget

    budget = FreeTierBudget(call_limit=1)
    budget.reserve(100)
    with pytest.raises(BudgetExceeded):
        budget.reserve(100)
    assert budget.calls == 1
    small = FreeTierBudget(token_limit=500)
    with pytest.raises(BudgetExceeded):
        small.reserve(100)
    with pytest.raises(BudgetExceeded):
        small.reserve(200_001)
    assert small.calls == 0


def test_completed_research_is_reused_only_with_same_date_and_evidence(tmp_path):
    from ibex.agents import cache_completed, reuse_completed

    row = {**copy.deepcopy(valid_row()), "ticker": "IBE.MC", "retrieved_at": "2026-11-01T00:01:00+01:00",
           "news": [{"title": "A"}, {"title": "B"}],
           "agents": {"status": "completed", "model": "gemini-3.1-flash-lite"}}
    report = {"date": "2026-11-01", "companies": [row], "macro_news": [{"title": "C"}, {"title": "D"}]}
    output = tmp_path / "original"
    saved = output / "agents" / "IBE.MC"
    saved.mkdir(parents=True)
    (saved / "complete_report.html").write_text("Research from verified evidence")
    cache_completed(report, row, output, tmp_path / "state")
    fresh = copy.deepcopy(row)
    fresh["retrieved_at"] = "2026-11-01T00:15:00+01:00"
    fresh["news"].reverse()
    reordered = {**report, "macro_news": list(reversed(report["macro_news"]))}
    assert reuse_completed(reordered, fresh, tmp_path / "reordered", tmp_path / "state")
    assert reuse_completed(report, fresh, tmp_path / "resumed", tmp_path / "state")
    assert (tmp_path / "resumed" / "agents" / "IBE.MC" / "complete_report.html").is_file()
    fresh["news"] = [{"title": "New results require a new analysis"}]
    assert not reuse_completed(report, fresh, tmp_path / "changed", tmp_path / "state")
    fresh = copy.deepcopy(row)
    fresh["statements"] = [{"statement": "income_stmt", "periods": [{"values": {"Net Income": 123}}]}]
    assert not reuse_completed(report, fresh, tmp_path / "new-accounts", tmp_path / "state")
    assert not reuse_completed({**report, "date": "2026-11-02"}, row, tmp_path / "tomorrow", tmp_path / "state")


@pytest.mark.parametrize("status", [500, 502, 503, 504])
def test_transient_google_server_errors_resume_with_bounded_backoff(status, capsys):
    from ibex.agents import propagate_with_retry

    class ProviderError(RuntimeError):
        code = status

    class Graph:
        calls = 0

        def propagate(self, ticker, date):
            self.calls += 1
            if self.calls < 3:
                raise ProviderError("dummy-private-api-key-must-not-leak")
            return {"final_trade_decision": "Neutral"}, "Neutral"

    graph, pauses = Graph(), []
    assert propagate_with_retry(graph, "IBE.MC", "2026-11-01", sleep=pauses.append)[1] == "Neutral"
    assert graph.calls == 3
    assert pauses == [20, 40]
    assert "dummy-private-api-key" not in capsys.readouterr().out


@pytest.mark.parametrize("status", [400, 401, 403, 404, 429, None, 503])
def test_retries_never_repeat_quota_auth_or_unclassified_errors_and_are_finite(status):
    from ibex.agents import propagate_with_retry

    class ProviderError(RuntimeError):
        code = status

    class Graph:
        calls = 0

        def propagate(self, ticker, date):
            self.calls += 1
            raise ProviderError("failure")

    graph, pauses = Graph(), []
    with pytest.raises(ProviderError):
        propagate_with_retry(graph, "IBE.MC", "2026-11-01", sleep=pauses.append)
    assert graph.calls == (3 if status == 503 else 1)
    assert pauses == ([20, 40] if status == 503 else [])


def test_35_company_report_escapes_provider_html_and_is_strict_json(tmp_path):
    rows = []
    for company in load_universe()["companies"]:
        row = {**copy.deepcopy(valid_row()), **company}
        row["news"] = [{"title": '<script>alert("bad")</script>', "url": "https://example.org",
                        "publisher": "Prueba", "published_at": NOW.isoformat()}]
        row["screen"] = screen(row, True)
        rows.append(row)
    report = {"date": "2026-10-31", "generated_at": NOW.isoformat(), "companies": rows,
              "universe": {"verified": True, "note": "Prueba", "revision_date": "2026-09-21",
                           "source": "https://example.org/bme"}}
    save_report(report, tmp_path)
    document = (tmp_path / "index.html").read_text()
    assert '<script>alert("bad")</script>' not in document
    assert "&lt;script&gt;" in document
    assert document.count("<article ") == 35
    assert len(json.loads((tmp_path / "datos.json").read_text())["companies"]) == 35
    assert (tmp_path / "Informe.md").read_text().count("## ") >= 35


def test_real_graph_adapter_keeps_completed_reports_and_stops_on_provider_failure(monkeypatch, tmp_path):
    from ibex.agents import run_agents
    from tradingagents.graph.trading_graph import TradingAgentsGraph

    monkeypatch.setenv("IBEX_FREE_TIER_VERIFIED", "true")
    monkeypatch.setenv("GOOGLE_API_KEY", "dummy-test-key")
    captured = {}

    def init(self, selected_analysts, config, callbacks):
        captured["analysts"] = selected_analysts
        captured["config"] = config
        captured["callbacks"] = callbacks
        captured.setdefault("calls", 0)
        captured.setdefault("models", set()).add(config["quick_think_llm"])

    def propagate(self, ticker, date):
        captured["calls"] += 1
        if captured["calls"] == 4:
            raise RuntimeError("dummy-test-key-must-not-leak")
        return {"final_trade_decision": "Evidence-backed test decision"}, "Hold"

    def save(self, state, ticker, save_path):
        save_path.mkdir(parents=True, exist_ok=True)
        (save_path / "complete_report.md").write_text("Test research only")
        (save_path / "complete_report.html").write_text("Test research only")

    monkeypatch.setattr(TradingAgentsGraph, "__init__", init)
    monkeypatch.setattr(TradingAgentsGraph, "propagate", propagate)
    monkeypatch.setattr(TradingAgentsGraph, "save_reports", save)
    rows = [{**copy.deepcopy(valid_row()), **company} for company in load_universe()["companies"]]
    for row in rows:
        row["screen"] = screen(row, True)
    report = {"date": "2026-10-31", "generated_at": NOW.isoformat(), "companies": rows,
              "universe": {"verified": True, "note": "Prueba", "revision_date": "2026-09-21",
                           "source": "https://example.org/bme"}}
    run_agents(report, tmp_path / "report", tmp_path / "state")
    assert captured["calls"] == 4
    assert report["llm_usage"]["completed"] == 3
    assert captured["analysts"] == ("market", "news", "fundamentals")
    assert captured["config"]["benchmark_ticker"] == "^IBEX"
    assert captured["config"]["llm_max_retries"] == 0
    assert captured["models"] == {"gemini-3.1-flash-lite", "gemini-3.5-flash-lite"}
    saved = (tmp_path / "report" / "datos.json").read_text()
    assert "dummy-test-key" not in saved
    assert report["companies"][4]["agents"]["status"] == "pending"
    run_agents(report, tmp_path / "report", tmp_path / "state")
    assert captured["calls"] == 36  # Four first attempts + 32 unfinished companies.
    assert report["llm_usage"]["completed"] == 35
    assert all(row["agents"].get("reused") for row in report["companies"][:3])
