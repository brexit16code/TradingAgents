"""Daily report: python -m ibex.run [--with-agents]."""

import argparse
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from ibex.data import collect, history_for, rss_news
from ibex.metrics import add_peer_valuations, screen
from ibex.render import save_report
from ibex.universe import load_universe, verify_universe


def main():
    parser = argparse.ArgumentParser(description="IBEX 35, informes sin operaciones reales")
    parser.add_argument("--output", type=Path, default=Path("ibex-output/latest"))
    parser.add_argument("--with-agents", action="store_true")
    parser.add_argument("--state-root", type=Path, default=Path(".ibex-state"))
    parser.add_argument("--resume-baseline", action="store_true")
    args = parser.parse_args()
    now = datetime.now(ZoneInfo("Europe/Madrid"))
    if args.resume_baseline:
        import json

        report = json.loads((args.output / "datos.json").read_text(encoding="utf-8"))
        if report["date"] != now.date().isoformat():
            raise ValueError("No se reutilizan fundamentales ni noticias de otra fecha para la IA.")
    else:
        config = load_universe()
        report = {"date": now.date().isoformat(), "generated_at": now.isoformat(),
                  "timezone": "Europe/Madrid", "mode": "read_only_research",
                  "universe": verify_universe(config, now), "companies": [], "macro_news": []}
        try:
            benchmark = history_for("^IBEX", now)
        except Exception:
            benchmark = None
            report["benchmark_note"] = "Índice no disponible: fuerza relativa sin calcular."
        try:
            report["macro_news"] = rss_news('BCE España eurozona inflación tipos interés bolsa', now, limit=8)
        except Exception:
            report["macro_news"] = []
        for i, company in enumerate(config["companies"], 1):
            print(f"[{i}/35] {company['ticker']}", flush=True)
            report["companies"].append(collect(company, benchmark, now))
        add_peer_valuations(report["companies"])
        for row in report["companies"]:
            row["screen"] = screen(row, report["universe"]["verified"])
        save_report(report, args.output)
    if args.with_agents:
        from ibex.agents import run_agents

        try:
            run_agents(report, args.output, args.state_root)
        except Exception as exc:
            report["llm_note"] = f"IA no ejecutada ({type(exc).__name__}); revisar configuración/cuota."
            for row in report["companies"]:
                row.setdefault("agents", {"status": "disabled", "note": report["llm_note"]})
        save_report(report, args.output)
    if summary_path := os.environ.get("GITHUB_STEP_SUMMARY"):
        summary = Path(summary_path)
        with summary.open("a", encoding="utf-8") as stream:
            content = (args.output / "Informe.md").read_text(encoding="utf-8")
            # GitHub job summaries are limited to 1 MiB per step.
            stream.write(content[:800_000])
    print(f"Informe guardado: {args.output / 'Informe.md'}", flush=True)
    if not any(row.get("status") == "ok" for row in report["companies"]):
        raise SystemExit("Ningún valor tiene precios; se conserva el informe de error sin señales.")


if __name__ == "__main__":
    main()
