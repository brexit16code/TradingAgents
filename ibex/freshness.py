"""Avoid duplicate daily AI runs and visibly flag stale published research."""

import argparse
import html
import json
import os
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

MADRID = ZoneInfo("Europe/Madrid")


def completed_today(report, now):
    """Only a full, same-day AFTER-CLOSE report can replace a scheduled run."""
    try:
        local = now.astimezone(MADRID)
        captured = datetime.fromisoformat(report["generated_at"])
        if not captured.tzinfo or captured > now:
            return False
        captured = captured.astimezone(MADRID)
        rows = report["companies"]
        return (
            report["date"] == local.date().isoformat()
            and captured.date() == local.date()
            and captured.hour >= 18
            and report["universe"]["verified"] is True
            and len(rows) == 35
            and len({row["ticker"] for row in rows}) == 35
            and all(row.get("status") == "ok" and not row.get("stale")
                    and row.get("agents", {}).get("status") == "completed"
                    and row.get("fundamentals", {}).get("currency") == "EUR"
                    and bool(row.get("technical", {}).get("price_date"))
                    and row["technical"]["price_date"] <= report["date"]
                    for row in rows)
        )
    except (KeyError, ValueError, TypeError):
        return False


def recommendation_gaps(sources):
    """Report absent dates; never invent the missing recommendations or reset money."""
    dates = sorted({date.fromisoformat(source["report_date"]) for source in sources})
    result = []
    for before, after in zip(dates, dates[1:], strict=False):
        missing = (after - before).days - 1
        if missing > 0:
            result.append({"from": (before + timedelta(days=1)).isoformat(),
                           "to": (after - timedelta(days=1)).isoformat(), "days": missing})
    return result


def stale_notice(report_date):
    return (f'<div id="freshness-notice" class="notice" role="status" hidden '
            f'data-date="{html.escape(str(report_date), quote=True)}"></div>')


FRESHNESS_SCRIPT = """<script>(()=>{
const notice=document.getElementById('freshness-notice');if(!notice)return;
const value=notice.dataset.date;if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(value))return;
const parts=Object.fromEntries(new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Madrid',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',hourCycle:'h23'}).formatToParts(new Date()).map(p=>[p.type,p.value]));
const today=parts.year+'-'+parts.month+'-'+parts.day;
const age=Math.round((Date.parse(today+'T12:00:00Z')-Date.parse(value+'T12:00:00Z'))/86400000);
if(age>1||(age===1&&Number(parts.hour)>=23)){
notice.textContent='Datos desactualizados: el último análisis registrado es del '+value.slice(8,10)+'/'+value.slice(5,7)+'/'+value.slice(0,4)+'. Comprueba la actualización antes de utilizar estas recomendaciones.';notice.hidden=false;
}
})();</script>"""


def main():
    parser = argparse.ArgumentParser(description="Comprobar si ya hay un informe diario completo")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = json.loads(args.report.read_text(encoding="utf-8"))
        skip = completed_today(report, datetime.now(MADRID))
        if skip:
            skip = all((args.report.parent / row.get("agents", {}).get("report", "")).is_file()
                       for row in report["companies"])
    except (OSError, ValueError, TypeError):
        skip = False
    if output := os.environ.get("GITHUB_OUTPUT"):
        with Path(output).open("a", encoding="utf-8") as stream:
            stream.write(f"skip={'true' if skip else 'false'}\n")
    print("Informe completo de hoy ya disponible: se evitan llamadas duplicadas." if skip
          else "Se necesita actualizar el informe diario.")


if __name__ == "__main__":
    main()
