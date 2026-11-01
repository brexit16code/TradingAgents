"""Readable, self-contained portfolio pages for Android; all money is fictional."""

from datetime import datetime

from ibex.paper import MADRID, summary
from ibex.render import esc

CSS = """
:root{color-scheme:dark;font:17px/1.6 system-ui,sans-serif;color:#ecf4fc;background:#0a1018}*{box-sizing:border-box}body{margin:0}main{max-width:1050px;margin:auto;padding:22px}a{color:#8edcf5;text-underline-offset:4px}h1{font-size:clamp(32px,7vw,50px);line-height:1.15;margin:12px 0}h2{font-size:25px;margin-top:32px}h3{font-size:19px;margin:0 0 8px}p{margin:10px 0}small,.muted{color:#b4c7da}small{font-size:14px}.eyebrow{color:#7ae3c7;font-size:13px;letter-spacing:1px;font-weight:750}.links{display:flex;flex-wrap:wrap;gap:12px;margin:22px 0}.button{display:inline-block;border:1px solid #3b5973;padding:12px 16px;border-radius:12px;background:#162a3c;font-weight:650}.hero,.panel{background:#122031;border:1px solid #30465f;border-radius:18px;padding:22px;margin:18px 0}.hero .amount{font-size:clamp(35px,8vw,54px);font-weight:750;line-height:1.25;margin:10px 0;font-variant-numeric:tabular-nums}.notice{border-left:4px solid #e8bb71;background:#262938;padding:16px 20px;border-radius:10px;margin:18px 0}.positive{color:#7df0c8}.negative{color:#ffb3c4}.metrics,.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:14px}.metric,.card{background:#101d2b;border:1px solid #2b4058;border-radius:14px;padding:18px}.metric strong{display:block;font-size:25px;font-variant-numeric:tabular-nums;margin:6px 0}.metric small{display:block}dl{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:12px 0}dt{color:#b4c7da;font-size:14px}dd{margin:0;font-variant-numeric:tabular-nums}summary{cursor:pointer;font-weight:700;padding:12px 0}details{border-top:1px solid #2b4058;margin-top:14px}ul{padding-left:23px}li{margin:10px 0}.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:15px;white-space:nowrap}td,th{text-align:left;padding:13px 10px;border-bottom:1px solid #2b4058}th{color:#b4c7da}svg{width:100%;height:auto;display:block}.legend{display:flex;flex-wrap:wrap;gap:22px;font-size:15px}.legend .portfolio{color:#7df0c8}.legend .index{color:#8dc8ff}.fields{display:grid;grid-template-columns:1fr 1fr;gap:14px}label{font-size:15px}input{width:100%;padding:12px;margin-top:6px;font:inherit;background:#0b1622;color:#fff;border:1px solid #476079;border-radius:10px}output{display:block;font-size:28px;font-weight:750;margin:20px 0 6px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;font-size:16px}.footer{font-size:14px;color:#b4c7da;margin:30px 0}a:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid #7df0c8;outline-offset:4px}@media(max-width:440px){main{padding:16px}.hero,.panel{padding:18px}.fields{grid-template-columns:1fr}h2{font-size:23px}}@media print{.links,#ensayo{display:none}.panel,.card{break-inside:avoid}}
"""


def amount(value, suffix=" €"):
    if value is None:
        return "Pendiente"
    return f"{value:,.2f}".replace(",", " ").replace(".", ",") + suffix


def date_label(value, include_time=False):
    stamp = datetime.fromisoformat(value)
    if stamp.tzinfo:
        stamp = stamp.astimezone(MADRID)
    return stamp.strftime("%d/%m/%Y · %H:%M" if include_time else "%d/%m/%Y")


def source_link(path, ticker):
    return f'{esc(path.removesuffix(".json"))}.html#{esc(ticker)}'


def document(title, body):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="referrer" content="no-referrer"><title>{esc(title)}</title>'
            f'<style>{CSS}</style></head><body><main>{body}</main></body></html>')


def performance_chart(state):
    points = [{"return_pct": 0, "ibex_return_pct": 0}, *state["valuations"]]
    if len(points) < 2:
        return '<p class="muted">La evolución aparecerá al completar la primera sesión del experimento.</p>'
    values = [p[k] for p in points for k in ("return_pct", "ibex_return_pct")]
    low, high = min(values) - 0.2, max(values) + 0.2
    lines = []
    for key, color in (("return_pct", "#7df0c8"), ("ibex_return_pct", "#8dc8ff")):
        coords = " ".join(f"{65 + i * 680 / (len(points) - 1):.2f},{230 - (p[key] - low) * 195 / (high - low):.2f}"
                          for i, p in enumerate(points))
        lines.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="3"/>')
    ticks = "".join(f'<text x="2" y="{230 - i * 195 / 4:.0f}" fill="#b4c7da" font-size="14">{low + i * (high - low) / 4:.1f}%</text>' for i in range(5))
    return (f'<svg viewBox="0 0 770 265" role="img" aria-label="Evolución porcentual de la cartera ficticia y del IBEX de precio">'
            f'{ticks}{"".join(lines)}</svg><div class="legend"><span class="portfolio">● Cartera con dividendos devengados y costes</span>'
            '<span class="index">● IBEX 35 de precio, sin dividendos ni costes</span></div>'
            '<p><small>El IBEX es una referencia de mercado. Las bases son distintas; esta diferencia no mide por sí sola el mérito de las recomendaciones.</small></p>')


def write_signal_archive(source, output):
    cards = []
    for row in source["companies"]:
        action = {"BUY": "Entrada virtual", "SELL": "Salida virtual", "HOLD": "Mantener", "REVIEW": "Sin señal utilizable"}[row["action"]]
        cards.append(f'<section class="panel" id="{esc(row["ticker"])}"><h2>{esc(row["name"])}</h2>'
                     f'<p>{esc(row["ticker"])} · {esc(row["rating"])} · {action}</p>'
                     f'<small>Cierre de referencia: {amount(row["close"])} · {esc(row["price_date"])}</small>'
                     f'<pre>{esc(row["decision"]) or "No hay decisión completa disponible."}</pre></section>')
    body = (f'<p class="eyebrow">RECOMENDACIONES GUARDADAS · EXPERIMENTO FICTICIO</p>'
            f'<h1>Señales del {date_label(source["report_date"])}</h1>'
            f'<p>Registradas el {date_label(source["observed_at"], True)} (hora peninsular). Este registro conserva lo que se sabía al emitir la señal.</p>'
            '<p><a href="../cartera.html">Volver a la cartera virtual</a></p>' + "".join(cards))
    (output / source["path"].replace(".json", ".html")).write_text(document("Recomendaciones registradas", body), encoding="utf-8")


def write_portfolio(state, output):
    totals = summary(state)
    profit_css = "positive" if totals["profit"] >= 0 else "negative"
    pending = [o for o in state["orders"] if o["status"] == "pending"]
    warning = "".join(f'<p>{esc(w)}</p>' for w in state["warnings"])
    if state["status"] == "pending_market":
        warning += '<p><strong>Esperando la primera sesión.</strong> Las órdenes virtuales pendientes usarán una apertura posterior a su registro. No se han simulado compras a precios anteriores.</p>'
    if state["status"] == "paused":
        warning += '<p><strong>Actualización en espera.</strong> La fecha de valoración indica la última sesión completa; las cifras no se presentan como actuales.</p>'
    notice = f'<div class="notice" role="status">{warning}</div>' if warning else ""
    metrics = [("Efectivo disponible", amount(totals["cash"]), "Dinero ficticio sin invertir"),
               ("Acciones en cartera", amount(totals["market_value"]), f'{len(state["positions"])} posiciones abiertas'),
               ("Resultado de ventas", amount(totals["realized"]), "Ganancia o pérdida cerrada, con costes"),
               ("Resultado pendiente", amount(totals["unrealized"]), "De las posiciones abiertas, con coste de entrada"),
               ("Dividendos devengados", amount(totals["dividends"]), "Brutos; separados del efectivo y sin reinversión"),
               ("Comisiones simuladas", amount(totals["fees"]), "Ya descontadas; no se vuelven a restar")]
    metrics_html = "".join(f'<div class="metric"><span>{label}</span><strong>{value}</strong><small>{note}</small></div>' for label, value, note in metrics)
    positions = []
    for ticker, pos in sorted(state["positions"].items()):
        value = pos["quantity"] * pos.get("last_close", 0)
        positions.append(f'<article class="card"><h3>{esc(pos["name"])}</h3><small>{esc(ticker)}</small><dl>'
                         f'<div><dt>Acciones</dt><dd>{pos["quantity"]:g}</dd></div><div><dt>Valor actual</dt><dd>{amount(value)}</dd></div>'
                         f'<div><dt>Coste con comisión</dt><dd>{amount(pos["basis"])}</dd></div><div><dt>Resultado pendiente</dt><dd>{amount(value - pos["basis"])}</dd></div>'
                         f'<div><dt>Último cierre</dt><dd>{amount(pos.get("last_close"))}</dd></div><div><dt>Fecha del precio</dt><dd>{date_label(pos["price_date"])}</dd></div></dl>'
                         f'<a href="{source_link(pos["source"], ticker)}">Recomendación original</a></article>')
    positions_html = "".join(positions) or '<p class="muted">Todavía no hay acciones en la cartera. «Mantener» no abre una compra si no existe una posición.</p>'
    orders_html = "".join(f'<article class="card"><h3>{"Comprar" if o["side"] == "BUY" else "Vender"} · {esc(o["name"])}</h3>'
                          f'<p>{esc(o["rating"])} · registrada el {date_label(o["requested_at"], True)}</p>'
                          f'<p>{"Hasta 1.000 € con costes incluidos" if o["side"] == "BUY" else "Cerrar toda la posición existente"}. Apertura de una sesión posterior al {date_label(o["after"])}.</p>'
                          f'<a href="{source_link(o["source"], o["ticker"])}">Ver la recomendación guardada</a></article>' for o in pending)
    orders_html = orders_html or '<p class="muted">No hay órdenes virtuales pendientes.</p>'
    trades = []
    for trade in reversed(state["trades"][-50:]):
        result = amount(trade["realized_pl"]) if trade["side"] == "SELL" else "Posición abierta"
        trades.append(f'<tr><td>{date_label(trade["date"])}</td><td><a href="{source_link(trade["source"], trade["ticker"])}">{esc(trade["name"])}</a></td>'
                      f'<td>{"Compra" if trade["side"] == "BUY" else "Venta"}</td><td>{trade["quantity"]:g}</td><td>{amount(trade["price"])}</td>'
                      f'<td>{amount(trade["fee"])}</td><td>{result}</td></tr>')
    trade_table = ('<div class="table-wrap"><table><thead><tr><th>Fecha</th><th>Empresa y señal</th><th>Operación</th><th>Acciones</th><th>Precio ejecutado</th><th>Comisión</th><th>Resultado cerrado</th></tr></thead><tbody>' + "".join(trades) + '</tbody></table></div>') if trades else '<p class="muted">El historial se llenará cuando se ejecuten compras o ventas ficticias.</p>'
    signals = "".join(f'<tr><td>{esc(r["name"])}</td><td>{esc(r["rating"]) or "Sin informe"}</td><td>{ {"BUY":"Entrada", "SELL":"Salida", "HOLD":"Mantener", "REVIEW":"Revisar datos"}[r["action"]] }</td></tr>' for r in state["latest_signals"])
    cancelled = [o for o in state["orders"] if o["status"] in {"cancelled", "rejected", "expired"}]
    cancelled_html = "".join(f'<li>{esc(o["name"])} · {esc(o["note"])}</li>' for o in cancelled[-30:])
    asof = date_label(state["valuations"][-1]["date"]) if state["valuations"] else "Esperando la primera sesión"
    max_drop = min([0, *[p["drawdown_pct"] for p in state["valuations"]]])
    body = f'''
<p class="eyebrow">SIMULACIÓN AUTOMÁTICA · DINERO FICTICIO</p><h1>Cartera virtual del IBEX</h1>
<p>Una prueba para observar qué ocurre al seguir las recomendaciones de TradingAgents.</p>
<div class="links"><a class="button" href="index.html">Ver los informes</a><a class="button" href="#ensayo">Ensayar compra y venta</a><a class="button" href="cartera.json" download="historial-cartera-virtual.json">Descargar historial</a></div>
<div class="hero"><span>Valor total de la cartera</span><div class="amount">{amount(totals['equity'])}</div><p class="{profit_css}"><strong>Resultado total: {amount(totals['profit'])} · {amount(totals['return_pct'], ' %')}</strong></p>
<small>Capital inicial: 10.000 € ficticios · Inicio: {date_label(state['started_at'])}<br>Valoración: {asof}<br>Actualizado: {date_label(state['updated_at'], True)} · Hora peninsular</small></div>
{notice}<div class="metrics">{metrics_html}</div>
<p><small>Valor total = efectivo + acciones + dividendos brutos devengados. Resultado total = valor total − 10.000 €. Se actualiza tras el análisis diario; los precios no son en tiempo real.</small></p>
<h2>Evolución del experimento</h2><div class="panel">{performance_chart(state)}<p><small>Mayor caída desde un máximo de cierre: {amount(max_drop, ' %') if state['valuations'] else 'Aún sin historial de sesiones'}.</small></p></div>
<h2>Órdenes virtuales pendientes · {len(pending)}</h2><div class="cards">{orders_html}</div>
<h2>Acciones que mantiene la cartera</h2><div class="cards">{positions_html}</div>
<h2>Compras y ventas registradas</h2>{trade_table}<p><small>Se muestran las últimas 50 operaciones. El archivo descargable conserva el historial completo.</small></p>
<details><summary>Últimas recomendaciones procesadas · {len(state['latest_signals'])}</summary><div class="table-wrap"><table><thead><tr><th>Empresa</th><th>TradingAgents</th><th>Regla de simulación</th></tr></thead><tbody>{signals}</tbody></table></div></details>
{'<details><summary>Órdenes sin ejecutar</summary><ul>' + cancelled_html + '</ul></details>' if cancelled_html else ''}
<section class="panel" id="ensayo"><h2>Ensaya una compra y una venta</h2><p>Introduce precios hipotéticos de ejecución para ver el resultado de una operación. La cartera automática conserva su propio historial de recomendaciones.</p>
<div class="fields"><label>Acciones<input id="calc-quantity" type="number" min="1" step="1" value="100" inputmode="numeric"></label>
<label>Precio de compra por acción (€)<input id="calc-buy" type="number" min="0.0001" step="any" value="10" inputmode="decimal"></label>
<label>Precio de venta por acción (€)<input id="calc-sell" type="number" min="0.0001" step="any" value="11" inputmode="decimal"></label>
<label>Comisión por operación (€)<input id="calc-fee" type="number" min="0" step="any" value="2" inputmode="decimal"></label></div>
<output id="calc-result" aria-live="polite"></output><p id="calc-detail" class="muted"></p><small>Se descuentan las comisiones de compra y venta. Ensayo antes de impuestos y sin dividendos.</small></section>
<details><summary>Reglas y límites de esta prueba</summary><ul>
<li>Saldo inicial fijo de 10.000 €. Hasta 1.000 € por entrada, con sus costes, y diez posiciones como máximo. Acciones enteras en las compras. Solo se vende lo que ya está en cartera.</li>
<li>Comprar / Buy / Overweight: abrir una posición si no existe. Mantener / Hold: conservarla, sin abrir ni ampliar. Vender / Sell / Underweight: cerrar toda la posición. Son reglas de este experimento, no una asignación personal de inversión.</li>
<li>Se usa la calificación final de TradingAgents. El filtro de reglas «Vigilar favorable» de la página principal no origina operaciones en esta cartera.</li>
<li>Las señales quedan registradas con su fecha y justificación. La ejecución ficticia usa la primera apertura de una sesión posterior al día de registro, con 0,1 % de ajuste desfavorable al comprar y vender, más 2 € por operación.</li>
<li>Las ventas liberan efectivo antes de las compras. A igual fecha se sigue el orden alfabético del símbolo; no se seleccionan retrospectivamente los mejores resultados. Una señal posterior puede cancelar una orden pendiente; caduca tras catorce días sin ejecución.</li>
<li>Los dividendos se reconocen en la exfecha para quienes tenían las acciones al cierre anterior. Se mantienen como importe devengado, sin reinversión ni supuesto de cobro inmediato. Importes brutos, sin impuestos.</li>
<li>Se contemplan splits y contrasplits según los datos del proveedor; las fracciones resultantes se conservan en la simulación. Otros eventos corporativos, derechos o exclusiones requieren revisión. Los precios y eventos gratuitos pueden contener errores.</li>
<li>Si falta la apertura o el cierre necesario, se pausa la liquidación en esa sesión. Se conserva el historial, sin reiniciar el saldo ni inventar operaciones o rentabilidades.</li>
<li>El índice de referencia es el IBEX 35 de precio: excluye dividendos y costes. La cartera sí incluye sus costes y los dividendos devengados. No se presenta su diferencia como una prueba de superioridad.</li>
<li>Es un seguimiento desde el inicio del experimento, sin reconstruir un historial de supuestos aciertos anteriores. Los resultados simulados no garantizan resultados futuros.</li></ul></details>
<p class="footer">Experimento público con datos de mercado de Yahoo Finance. Sin cuenta de bróker, dinero real ni envío de órdenes. No utiliza llamadas adicionales a IA ni servicios de pago.</p>
<script>
const quantity=document.getElementById('calc-quantity'),buy=document.getElementById('calc-buy'),sell=document.getElementById('calc-sell'),fee=document.getElementById('calc-fee'),result=document.getElementById('calc-result'),detail=document.getElementById('calc-detail');
const euro=new Intl.NumberFormat('es-ES',{{style:'currency',currency:'EUR'}});
function calculate(){{const q=Number(quantity.value),b=Number(buy.value),s=Number(sell.value),f=Number(fee.value);if(![q,b,s,f].every(Number.isFinite)||!Number.isInteger(q)||q<=0||b<=0||s<=0||f<0||[quantity,buy,sell,fee].some(e=>e.value.trim()==='')){{result.textContent='Introduce cantidades y precios válidos.';detail.textContent='';result.className='';return;}}const cost=q*b+f,received=q*s-f,pnl=received-cost;if(![cost,received,pnl].every(Number.isFinite)){{result.textContent='Importe fuera de rango.';detail.textContent='';return;}}result.textContent=(pnl>=0?'Ganancia: ':'Pérdida: ')+euro.format(pnl);result.className=pnl>=0?'positive':'negative';detail.textContent='Coste de compra: '+euro.format(cost)+' · Importe de venta tras comisión: '+euro.format(received);}}
for(const field of [quantity,buy,sell,fee])field.addEventListener('input',calculate);calculate();
</script>'''
    (output / "cartera.html").write_text(document("Cartera virtual IBEX · Sin dinero real", body), encoding="utf-8")
