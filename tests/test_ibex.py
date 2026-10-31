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
        captured["calls"] = 0

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
    saved = (tmp_path / "report" / "datos.json").read_text()
    assert "dummy-test-key" not in saved
    assert report["companies"][4]["agents"]["status"] == "pending"
