"""Regression checks for the November 2026 scheduling interruption and duplicate usage."""

import copy
import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from ibex.freshness import MADRID, completed_today, main, recommendation_gaps

NOW = datetime(2026, 11, 12, 20, 0, tzinfo=MADRID)


def full_report():
    return {"date": "2026-11-12", "generated_at": "2026-11-12T18:24:00+01:00",
            "universe": {"verified": True},
            "companies": [{"ticker": f"T{i:02d}.MC", "status": "ok", "stale": False,
                           "fundamentals": {"currency": "EUR"},
                           "technical": {"price_date": "2026-11-12"},
                           "agents": {"status": "completed", "report": f"agents/T{i:02d}.MC/complete_report.html"}}
                          for i in range(35)]}


def test_manual_after_close_completion_prevents_duplicate_scheduled_ai_run():
    assert completed_today(full_report(), NOW)
    assert completed_today(full_report(), NOW.astimezone(ZoneInfo("America/New_York")))


@pytest.mark.parametrize("problem", ["old", "morning", "future", "missing", "duplicate", "partial", "stale", "currency", "unverified", "price", "corrupt"])
def test_incomplete_or_stale_reports_never_prevent_the_daily_refresh(problem):
    data = full_report()
    if problem == "old":
        data["date"] = "2026-11-01"
    elif problem == "morning":
        data["generated_at"] = "2026-11-12T08:00:00+01:00"
    elif problem == "future":
        data["generated_at"] = "2026-11-12T23:00:00+01:00"
    elif problem == "missing":
        data["companies"].pop()
    elif problem == "duplicate":
        data["companies"][0] = copy.deepcopy(data["companies"][1])
    elif problem == "partial":
        data["companies"][0]["agents"]["status"] = "failed"
    elif problem == "stale":
        data["companies"][0]["stale"] = True
    elif problem == "currency":
        data["companies"][0]["fundamentals"]["currency"] = "USD"
    elif problem == "unverified":
        data["universe"]["verified"] = False
    elif problem == "price":
        data["companies"][0]["technical"]["price_date"] = None
    else:
        data = {}
    assert not completed_today(data, NOW)


def test_weekend_uses_report_date_without_requiring_a_nonexistent_weekend_close():
    data = full_report()
    data.update(date="2026-11-15", generated_at="2026-11-15T18:30:00+01:00")
    for row in data["companies"]:
        row["technical"]["price_date"] = "2026-11-13"
    assert completed_today(data, NOW.replace(day=15))


def test_interrupted_dates_are_disclosed_without_creating_hypothetical_recommendations():
    sources = [{"report_date": "2026-11-12"}, {"report_date": "2026-11-01"},
               {"report_date": "2026-11-01"}, {"report_date": "2026-11-13"}]
    assert recommendation_gaps(sources) == [{"from": "2026-11-02", "to": "2026-11-11", "days": 10}]
    assert len(sources) == 4
    assert recommendation_gaps([]) == []


def test_cli_requires_the_actual_individual_report_files_before_skipping(tmp_path, monkeypatch):
    import ibex.freshness as module

    class Clock(datetime):
        @classmethod
        def now(cls, tz=None):
            return NOW

    monkeypatch.setattr(module, "datetime", Clock)
    data = full_report()
    report_path = tmp_path / "datos.json"
    output = tmp_path / "output.txt"
    report_path.write_text(json.dumps(data))
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.setattr(sys, "argv", ["freshness", "--report", str(report_path)])
    main()
    assert output.read_text() == "skip=false\n"
    for row in data["companies"]:
        path = tmp_path / row["agents"]["report"]
        path.parent.mkdir(parents=True)
        path.write_text("<html>Informe</html>")
    output.write_text("")
    main()
    assert output.read_text() == "skip=true\n"
    report_path.unlink()
    output.write_text("")
    main()
    assert output.read_text() == "skip=false\n"
