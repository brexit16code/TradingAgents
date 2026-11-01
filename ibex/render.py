"""Self-contained mobile HTML and GitHub-readable Markdown reports."""

import html
import json
from pathlib import Path

from ibex.data import safe_url


def esc(value):
    return html.escape(str(value or ""), quote=True)


def fmt(value, suffix="", digits=2):
    if value is None:
        return "No disponible"
    return f"{value:,.{digits}f}{suffix}".replace(",", " ")


def chart(points):
    values = [point["value"] for point in points if point.get("value") is not None]
    if len(values) < 2:
        return "<p>Gráfico no disponible.</p>"
    low, high = min(values), max(values)
    span = high - low or 1
    coords = " ".join(f"{10 + i * 580 / (len(values) - 1):.2f},{120 - (v - low) * 105 / span:.2f}"
                      for i, v in enumerate(values))
    return (f'<svg viewBox="0 0 600 135" role="img" aria-label="Cierre ajustado, hasta 252 sesiones">'
            f'<polyline points="{coords}" fill="none" stroke="#27d9b0" stroke-width="2.5"/></svg>'
            f'<small>{esc(points[0]["date"])} → {esc(points[-1]["date"])} · Cierre ajustado; incluye ajustes del proveedor.</small>')


LABELS = {
    "trailingPE": "PER histórico", "forwardPE": "PER estimado", "priceToBook": "Precio/valor contable",
    "enterpriseToEbitda": "EV/EBITDA", "net_debt_ebitda": "Deuda neta/EBITDA (industrial)",
    "dividend_yield_pct": "Rentabilidad dividendo (%)", "consensus_upside_pct": "Potencial de consenso (%)",
    "targetMeanPrice": "Objetivo medio del consenso (€)", "numberOfAnalystOpinions": "Analistas en consenso",
}


def write_html(report, output):
    cards = []
    for row in report["companies"]:
        t, f, signal = row.get("technical", {}), row.get("fundamentals", {}), row["screen"]
        metrics = {"Cierre (€)": t.get("close"), "Cambio ajustado (%)": t.get("change_pct"),
                   "RSI 14": t.get("rsi14"), "SMA 50 ajustada": t.get("sma50"),
                   "SMA 200 ajustada": t.get("sma200"), "MACD": t.get("macd"),
                   "Señal MACD": t.get("macd_signal"), "Volatilidad (%)": t.get("volatility_pct"),
                   "Ventaja IBEX 63 sesiones (pp)": t.get("relative63_pp")}
        metrics.update({label: f.get(key) for key, label in LABELS.items()})
        dl = "".join(f"<div><dt>{esc(label)}</dt><dd>{fmt(value)}</dd></div>" for label, value in metrics.items())
        reasons = "".join(f"<li>{esc(item)}</li>" for item in signal["reasons"])
        risks = "".join(f"<li>{esc(item)}</li>" for item in signal["risks"])
        news = "".join(f'<li><a href="{esc(safe_url(a["url"]))}" target="_blank" rel="noopener noreferrer">'
                       f'{esc(a["title"])}</a><small>{esc(a["publisher"])} · {esc(a["published_at"][:10])}</small></li>'
                       for a in row.get("news", [])) or "<li>Cobertura insuficiente; revisar fuentes originales.</li>"
        agents = row.get("agents", {"status": "disabled", "note": "TradingAgents pendiente de activar con una cuota gratuita verificada."})
        if agents["status"] == "completed":
            ai = f'<p>TradingAgents: <strong>{esc(agents["rating"])}</strong></p><pre>{esc(agents["decision"])}</pre>'
            ai += f'<p><a href="{esc(agents["report"])}">Informe completo de los agentes</a></p>'
        else:
            ai = f'<p>{esc(agents.get("note", agents["status"]))}</p>'
        css = "good" if signal["label"] == "Vigilar favorable" else "bad" if signal["label"] == "Precaución" else "neutral"
        statements = esc(json.dumps(row.get("statements", []), ensure_ascii=False, indent=2))
        cards.append(f'''<article data-name="{esc(row['name'].casefold() + ' ' + row['ticker'].casefold())}" data-label="{esc(signal['label'])}">
<header><div><h2>{esc(row['name'])}</h2><small>{esc(row['ticker'])} · {esc(f.get('sector'))}</small></div><span class="badge {css}">{esc(signal['label'])}</span></header>
<div class="price">{fmt(t.get('close'), ' €')} <small>Cierre {esc(t.get('price_date', 'no disponible'))}</small></div>
{chart(t.get('chart', []))}
<p class="caption">Filtro de reglas sin IA · {esc(row.get('valuation', {}).get('label'))}</p>
<h3>Por qué</h3><ul>{reasons or '<li>No hay datos suficientes para emitir una señal.</li>'}</ul>
<h3>Riesgos y datos pendientes</h3><ul>{risks or '<li>Las reglas no cubren todos los riesgos de inversión.</li>'}</ul>
<details><summary>Indicadores y valoración</summary><dl>{dl}</dl><p>El consenso no es un valor intrínseco. El PER relativo usa como máximo los comparables del IBEX; muestra pequeña y negocios distintos.</p>
<p>Comparables: {esc(', '.join(row.get('valuation', {}).get('peers', [])) or 'No disponibles')}</p>
<p>{esc(row.get('fundamentals_note', ''))}</p><pre>{statements}</pre></details>
<details><summary>Noticias de los últimos siete días</summary><ul class="news">{news}</ul><p>Muestra de titulares; confirmar relevancia y contexto en el artículo. El filtro sin IA no interpreta estas noticias.</p></details>
<details><summary>Análisis de TradingAgents</summary>{ai}</details>
<footer><a href="{esc(row['sources']['quote'])}" target="_blank" rel="noopener noreferrer">Cotización y ratios</a> · <a href="{esc(row['sources']['financials'])}" target="_blank" rel="noopener noreferrer">Cuentas en Yahoo</a><small>Descargado {esc(row['retrieved_at'])}</small></footer></article>''')
    usage = report.get("llm_usage", {})
    done = usage.get("completed", 0)
    title = f"IBEX 35 · {report['date']}"
    css = """
:root{color-scheme:dark;font-family:system-ui,sans-serif;background:#0a1018;color:#ecf4fc;line-height:1.55}*{box-sizing:border-box}body{margin:0}main{max-width:1100px;margin:auto;padding:20px}a{color:#77cfef;text-underline-offset:3px}h1{font-size:clamp(29px,6vw,44px);margin:8px 0}h2{font-size:22px;margin:0}h3{font-size:16px;margin:18px 0 5px}p{margin:10px 0}small{display:block;color:#a9bacb;font-size:12px}nav{position:sticky;top:0;z-index:2;background:#0a1018ed;padding:12px 0;display:flex;gap:10px}input,select{font:inherit;background:#172437;color:#fff;border:1px solid #3e536f;border-radius:10px;padding:12px;min-width:0}input{flex:1}select{max-width:42%}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:18px}article{background:#111d2b;border:1px solid #293e56;border-radius:18px;padding:20px}article[hidden]{display:none}header{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}.badge{font-size:12px;font-weight:700;border-radius:20px;padding:6px 10px;flex-shrink:0}.good{background:#113e36;color:#79f3cf}.bad{background:#492538;color:#ffbbcb}.neutral{background:#2c374a;color:#d2def0}.price{font-size:32px;margin:16px 0 4px;font-variant-numeric:tabular-nums}svg{width:100%;display:block;max-height:170px}.caption{color:#b0c7d9;font-size:13px}ul{padding-left:20px}li{margin-bottom:8px}details{border-top:1px solid #293e56;padding:14px 0}summary{cursor:pointer;font-weight:650}dl{display:grid;grid-template-columns:1fr 1fr;gap:10px}dt{font-size:12px;color:#b0c7d9}dd{margin:0;font-size:18px;font-variant-numeric:tabular-nums}footer{border-top:1px solid #293e56;padding-top:14px;font-size:13px}.notice{border:1px solid #435674;background:#152235;border-radius:14px;padding:16px;margin:16px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;font-size:13px}.topline{color:#76dfc8;font-size:13px;font-weight:700;letter-spacing:1px}.news li{margin:14px 0}.method{color:#afbfce;font-size:13px}button{font:inherit} @media print{nav{display:none}article{break-inside:avoid}.grid{display:block}}
"""
    document = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><title>{esc(title)}</title><style>{css}</style></head><body><main>
<p class="topline">INVESTIGACIÓN · SIN OPERACIONES REALES</p><h1>{esc(title)}</h1>
<p>35 empresas · Cierre de mercado · España</p><small>Generado {esc(report['generated_at'])} · Zona Europe/Madrid</small>
<div class="notice"><strong>{sum(r.get('status') == 'ok' for r in report['companies'])}/35 con precios · {done}/35 con informe de TradingAgents</strong><p>{esc(report['universe']['note'])}</p>
<small>Última revisión BME contrastada: {esc(report['universe']['revision_date'])}. Los fines de semana y festivos se conserva la fecha del último cierre disponible.</small></div>
{'<div class="notice"><a href="cartera.html"><strong>Abrir la cartera virtual · 10.000 € ficticios</strong></a><p>Seguimiento de las recomendaciones, compras y ventas simuladas, ganancias y pérdidas.</p></div>' if (output / 'cartera.html').exists() else ''}
<nav aria-label="Filtrar empresas"><input id="search" type="search" aria-label="Buscar empresa" placeholder="Buscar empresa o símbolo"><select id="signal" aria-label="Filtrar señal"><option value="">Todas las señales</option><option>Vigilar favorable</option><option>Neutral</option><option>Precaución</option><option>Datos insuficientes</option></select></nav>
<div class="grid">{''.join(cards)}</div><div class="notice method"><strong>Cómo leerlo</strong><p>El filtro gratuito calcula tendencia, fuerza relativa, crecimiento de ingresos, múltiplos de valoración y deuda cuando es aplicable. Las reglas y umbrales no están validados como estrategia rentable. Las señales son hipótesis para investigar.</p>
<p>Fundamentales y consenso son instantáneas del proveedor. No se calcula un valor intrínseco universal, ni se deduce un resultado histórico con datos actuales. No hay cuenta de bróker conectada ni función de envío de órdenes.</p><p>Datos: Yahoo Finance y Google News. Composición: <a href="{esc(report['universe']['source'])}">BME</a>.</p></div></main>
<script>const search=document.getElementById('search'),signal=document.getElementById('signal');function filter(){{for(const card of document.querySelectorAll('article')){{card.hidden=!card.dataset.name.includes(search.value.toLocaleLowerCase('es'))||(signal.value&&card.dataset.label!==signal.value);}}}}search.addEventListener('input',filter);signal.addEventListener('change',filter);</script></body></html>'''
    (output / "index.html").write_text(document, encoding="utf-8")


def md(value):
    return esc(value).replace("[", "\\[").replace("]", "\\]").replace("|", "\\|").replace("\n", " ")


def write_markdown(report, output):
    lines = [f"# IBEX 35 · {report['date']}", "", "Investigación sin operaciones reales.", "",
             f"Generado: {report['generated_at']} (Europe/Madrid).", "", report["universe"]["note"], "",
             f"[Composición oficial BME]({report['universe']['source']}).", "",
             "El filtro de reglas sin IA y el análisis de TradingAgents se muestran por separado.", "",
             "| Empresa | Cierre EUR | Fecha precio | Filtro sin IA | TradingAgents |",
             "|---|---:|---|---|---|"]
    if (output / "cartera.html").exists():
        lines[4:4] = ["[Cartera virtual: operaciones y resultados ficticios](cartera.html)", ""]
    for row in report["companies"]:
        t, signal, ai = row.get("technical", {}), row["screen"], row.get("agents", {})
        lines.append(f"| {md(row['name'])} | {fmt(t.get('close'))} | {t.get('price_date', 'N/D')} | "
                     f"{signal['label']} | {md(ai.get('rating', ai.get('status', 'Desactivado')))} |")
    for row in report["companies"]:
        t, f, signal = row.get("technical", {}), row.get("fundamentals", {}), row["screen"]
        lines += ["", f"## {md(row['name'])} · {row['ticker']}", "", f"**{signal['label']}** (filtro de reglas sin IA).", "",
                  f"Cierre: {fmt(t.get('close'), ' EUR')}, fecha: {t.get('price_date', 'N/D')}. "
                  f"RSI: {fmt(t.get('rsi14'))}. MACD: {fmt(t.get('macd'))}. "
                  f"Ventaja IBEX a 63 sesiones: {fmt(t.get('relative63_pp'), ' pp')}.", ""]
        lines += [f"- {md(reason)}" for reason in signal["reasons"]]
        lines += [f"- Riesgo/dato pendiente: {md(risk)}" for risk in signal["risks"]]
        lines += ["", "| Ratio/estimación | Dato |", "|---|---:|"]
        lines += [f"| {label} | {fmt(f.get(key))} |" for key, label in LABELS.items()]
        lines += ["", md(row.get("valuation", {}).get("label")), "",
                  "El objetivo del consenso no es un valor intrínseco. "+md(row.get("fundamentals_note")), "", "### Noticias", ""]
        lines += [f"- [{md(a['title'])}]({safe_url(a['url'])}) · {md(a['publisher'])} · {md(a['published_at'][:10])}"
                  for a in row.get("news", [])] or ["- Cobertura insuficiente."]
        ai = row.get("agents", {})
        if ai.get("status") == "completed":
            lines += ["", "### TradingAgents", "", md(ai["decision"]), "",
                      f"[Informe completo de agentes](agents/{row['ticker']}/complete_report.md)"]
        else:
            lines += ["", "TradingAgents: " + md(ai.get("note", "pendiente de activar un proveedor gratuito verificado."))]
        lines += ["", f"[Precios y ratios]({row['sources']['quote']}) · [Cuentas]({row['sources']['financials']})", ""]
    lines += ["", "Las reglas no están validadas como estrategia rentable. Los datos gratuitos pueden tener "
              "retrasos y huecos. El filtro no interpreta el contenido de las noticias. "
              "No se han suministrado posiciones personales ni hay ejecución de órdenes."]
    (output / "Informe.md").write_text("\n".join(lines), encoding="utf-8")


def save_report(report, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "datos.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    write_html(report, output)
    write_markdown(report, output)
