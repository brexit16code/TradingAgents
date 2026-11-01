"""Forward-only, fully funded fictional portfolio. No broker or order API exists here."""

import argparse
import copy
import hashlib
import json
import re
import shutil
from datetime import datetime, timedelta
from decimal import ROUND_DOWN, ROUND_HALF_UP, Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

MADRID = ZoneInfo("Europe/Madrid")
POLICY = {
    "id": "ibex-forward-v1", "initial_cash": 10000, "entry_budget": 1000,
    "max_positions": 10, "commission": 2, "slippage_bps": 10,
    "order_expiry_days": 14,
    "execution": "Primera apertura de una sesión posterior al día de registro de la señal.",
    "dividends": "Brutos devengados en exfecha; separados del efectivo y sin reinversión.",
}
RATINGS = {
    "strong buy": "BUY", "buy": "BUY", "overweight": "BUY",
    "comprar": "BUY", "sobreponderar": "BUY", "hold": "HOLD", "mantener": "HOLD",
    "sell": "SELL", "strong sell": "SELL", "underweight": "SELL",
    "vender": "SELL", "infraponderar": "SELL",
}


def dec(value):
    result = Decimal(str(value))
    if not result.is_finite():
        raise ValueError("Importe no finito en la simulación.")
    return result


def money(value):
    return float(dec(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def digest(value):
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()
    return hashlib.sha256(encoded).hexdigest()[:24]


def new_account(now):
    return {
        "version": 1, "policy": copy.deepcopy(POLICY), "started_at": now.isoformat(),
        "updated_at": now.isoformat(), "cursor": now.date().isoformat(),
        "cash": 10000.0, "positions": {}, "orders": [], "trades": [],
        "dividends": [], "splits": [], "sources": [], "latest_signals": [],
        "valuations": [], "benchmark": {"symbol": "^IBEX", "units": None},
        "warnings": [], "status": "pending_market",
    }


def validate_account(state):
    if state.get("version") != 1 or state.get("policy") != POLICY:
        raise ValueError("Historial o reglas incompatibles: no se reinicia una cartera existente.")
    if dec(state["cash"]) < 0 or len(state["positions"]) > POLICY["max_positions"]:
        raise ValueError("Saldo o posiciones inválidos: se conserva el historial anterior.")
    for ticker, position in state["positions"].items():
        if not re.fullmatch(r"[A-Z0-9-]+\.MC", ticker):
            raise ValueError("Símbolo no válido en la cartera.")
        if dec(position["quantity"]) <= 0 or dec(position["basis"]) < 0:
            raise ValueError("Cantidad o coste no válido en el historial.")
    ids = [order["id"] for order in state["orders"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Órdenes duplicadas en el historial.")
    expected = dec(POLICY["initial_cash"])
    for trade in state["trades"]:
        change = dec(trade["notional"]) + dec(trade["fee"]) if trade["side"] == "BUY" else -dec(trade["notional"]) + dec(trade["fee"])
        expected -= change
    if money(expected) != money(state["cash"]):
        raise ValueError("El efectivo no coincide con las operaciones; no se borra el historial.")


def bars_from_history(frame):
    """Undo Yahoo's retrospective split adjustment before replaying corporate actions.

    Open/Close with auto_adjust=False still incorporate subsequent splits. Reconstruct
    the price and dividend per share that applied on EACH historical session. Never
    use Adj Close and also credit dividends: that would count them twice.
    """
    factor, result = Decimal(1), []
    for index, row in reversed(list(frame.iterrows())):
        split = dec(row.get("Stock Splits", 0))
        if split < 0:
            raise ValueError("Split no válido.")
        result.append({"date": index.date().isoformat(),
                       "open": float(dec(row["Open"]) * factor),
                       "close": float(dec(row["Close"]) * factor),
                       "dividend": float(dec(row.get("Dividends", 0)) * factor),
                       "split": float(split)})
        if split:
            factor *= split
    return list(reversed(result))


def signal_snapshot(report, now):
    rows = []
    cutoff = (now.date() if now.hour >= 18 else now.date() - timedelta(days=1)).isoformat()
    for row in report["companies"]:
        ai = row.get("agents", {})
        rating = str(ai.get("rating", ""))
        eligible = (ai.get("status") == "completed" and row.get("status") == "ok"
                    and not row.get("stale") and row.get("fundamentals", {}).get("currency") == "EUR"
                    and bool(row.get("technical", {}).get("price_date"))
                    and row["technical"]["price_date"] <= cutoff)
        rows.append({"ticker": row["ticker"], "name": row["name"], "rating": rating,
                     "action": RATINGS.get(rating.strip().casefold(), "REVIEW") if eligible else "REVIEW",
                     "model": ai.get("model"), "decision": ai.get("decision", ""),
                     "price_date": row.get("technical", {}).get("price_date"),
                     "close": row.get("technical", {}).get("close"),
                     "evidence_hash": digest(row)})
    source = {"report_date": report["date"], "generated_at": report["generated_at"],
              "universe_verified": bool(report.get("universe", {}).get("verified")),
              "companies": sorted(rows, key=lambda row: row["ticker"])}
    source["id"] = digest(source)
    source["observed_at"] = now.isoformat()
    source["path"] = f"paper-history/{report['date']}_{source['id']}.json"
    return source


def ingest_signals(state, report, now):
    generated = datetime.fromisoformat(report["generated_at"])
    if not generated.tzinfo or generated > now or report["date"] != now.date().isoformat() or not report.get("universe", {}).get("verified"):
        state["warnings"].append("No se incorporan señales de otra fecha o de una composición sin verificar.")
        return None
    source = signal_snapshot(report, now)
    if source["id"] in {s["id"] for s in state["sources"]}:
        return None
    state["sources"].append({k: v for k, v in source.items() if k != "companies"})
    state["latest_signals"] = [{k: v for k, v in row.items() if k not in {"decision", "evidence_hash"}}
                               for row in source["companies"]]
    review_count = sum(row["action"] == "REVIEW" for row in source["companies"])
    if review_count:
        state["warnings"].append(f"{review_count} empresas sin señal utilizable; no se inventan recomendaciones.")
    for row in source["companies"]:
        ticker, action = row["ticker"], row["action"]
        if not re.fullmatch(r"[A-Z0-9-]+\.MC", ticker) or action == "REVIEW":
            continue
        pending = [o for o in state["orders"] if o["ticker"] == ticker and o["status"] == "pending"]
        for order in pending:
            if action != order["side"]:
                order.update(status="cancelled", note="Una señal posterior sustituye la orden pendiente.")
        side = "BUY" if action == "BUY" and ticker not in state["positions"] else "SELL" if action == "SELL" and ticker in state["positions"] else None
        if side and not any(o["status"] == "pending" and o["side"] == side for o in pending):
            state["orders"].append({
                "id": digest([source["id"], ticker, side]), "ticker": ticker, "name": row["name"],
                "side": side, "rating": row["rating"], "requested_at": now.isoformat(),
                "after": now.date().isoformat(), "source": source["path"], "status": "pending",
            })
    return source


def fill_order(state, order, bar):
    ticker, side = order["ticker"], order["side"]
    opened = dec(bar["open"])
    impact = dec(POLICY["slippage_bps"]) / 10000
    price = opened * (1 + impact if side == "BUY" else 1 - impact)
    fee = dec(POLICY["commission"])
    if side == "BUY":
        if ticker in state["positions"] or len(state["positions"]) >= POLICY["max_positions"]:
            order.update(status="rejected", note="Ya existe posición o se ha alcanzado el máximo de diez.")
            return
        budget = min(dec(state["cash"]), dec(POLICY["entry_budget"]))
        quantity = ((budget - fee) / price).to_integral_value(rounding=ROUND_DOWN)
        if quantity <= 0 or quantity * price + fee > dec(state["cash"]):
            order.update(status="rejected", note="Saldo insuficiente para una acción entera y sus costes.")
            return
        notional = money(quantity * price)
        basis = money(dec(notional) + fee)
        state["cash"] = money(dec(state["cash"]) - dec(basis))
        state["positions"][ticker] = {"name": order["name"], "quantity": float(quantity),
                                      "basis": basis, "opened_on": bar["date"], "source": order["source"]}
        realized = None
    else:
        position = state["positions"].get(ticker)
        if not position:
            order.update(status="cancelled", note="No hay acciones; no se permiten ventas en corto.")
            return
        quantity = dec(position["quantity"])
        notional = money(quantity * price)
        if dec(state["cash"]) + dec(notional) < fee:
            order.update(status="rejected", note="Efectivo insuficiente para la comisión de salida.")
            return
        realized = money(dec(notional) - fee - dec(position["basis"]))
        state["cash"] = money(dec(state["cash"]) + dec(notional) - fee)
        del state["positions"][ticker]
    trade = {"order": order["id"], "ticker": ticker, "name": order["name"], "side": side,
             "date": bar["date"], "quantity": float(quantity), "open": float(opened),
             "price": float(price), "notional": notional, "fee": float(fee),
             "realized_pl": realized, "source": order["source"], "rating": order["rating"]}
    state["trades"].append(trade)
    order.update(status="filled", filled_on=bar["date"], quantity=float(quantity), price=float(price))


def summary(state):
    market = money(sum(dec(p["quantity"]) * dec(p.get("last_close", 0)) for p in state["positions"].values()))
    basis = sum(dec(p["basis"]) for p in state["positions"].values())
    dividends = money(sum(dec(d["amount"]) for d in state["dividends"]))
    equity = money(dec(state["cash"]) + dec(market) + dec(dividends))
    return {"cash": state["cash"], "market_value": market, "dividends": dividends,
            "equity": equity, "profit": money(dec(equity) - POLICY["initial_cash"]),
            "return_pct": float((dec(equity) / POLICY["initial_cash"] - 1) * 100),
            "realized": money(sum(dec(t["realized_pl"] or 0) for t in state["trades"])),
            "unrealized": money(dec(market) - basis),
            "fees": money(sum(dec(t["fee"]) for t in state["trades"]))}


def advance(previous, report, market, now):
    """Settle existing instructions first, then freeze NEW recommendations; no hindsight."""
    now = now.astimezone(MADRID)
    state = copy.deepcopy(previous) if previous is not None else new_account(now)
    validate_account(state)
    if datetime.fromisoformat(state["updated_at"]) > now:
        raise ValueError("No se permite retroceder la fecha del experimento.")
    state.update(updated_at=now.isoformat(), warnings=[], status="ok")
    cutoff = now.date() if now.hour >= 18 else now.date() - timedelta(days=1)
    calendars = {ticker: {bar["date"]: bar for bar in bars if bar["date"] <= cutoff.isoformat()}
                 for ticker, bars in market.items()}
    benchmark = calendars.get("^IBEX", {})
    if not benchmark:
        state["warnings"].append("IBEX no disponible; valoración y ejecuciones detenidas sin inventar precios.")
        state["status"] = "paused"
        return state, None
    if min(benchmark) > state["cursor"]:
        state["warnings"].append("La serie no cubre la última sesión guardada; se conserva el historial.")
        state["status"] = "paused"
        return state, None
    for day in sorted(d for d in benchmark if d > state["cursor"]):
        pending = [o for o in state["orders"] if o["status"] == "pending" and o["after"] < day]
        for order in pending:
            age = (datetime.fromisoformat(day) - datetime.fromisoformat(order["after"])).days
            if age > POLICY["order_expiry_days"]:
                order.update(status="expired", note="Más de catorce días sin poder simular su ejecución.")
        pending = [o for o in pending if o["status"] == "pending"]
        needed = set(state["positions"]) | {o["ticker"] for o in pending}
        missing = []
        for ticker in needed | {"^IBEX"}:
            bar = calendars.get(ticker, {}).get(day)
            if not bar or any(dec(bar.get(k, 0)) <= 0 for k in ("open", "close")) or dec(bar.get("dividend", 0)) < 0 or dec(bar.get("split", 0)) < 0:
                missing.append(ticker)
        if missing:
            state["warnings"].append(f"Sesión {day} incompleta para {', '.join(sorted(missing))}; liquidación en espera.")
            state["status"] = "paused"
            break
        for ticker, position in state["positions"].items():
            bar = calendars[ticker][day]
            if split := bar.get("split", 0):
                position["quantity"] = float(dec(position["quantity"]) * dec(split))
                state["splits"].append({"ticker": ticker, "date": day, "ratio": split})
            if dividend := bar.get("dividend", 0):
                state["dividends"].append({"ticker": ticker, "date": day, "per_share": dividend,
                                           "quantity": position["quantity"],
                                           "amount": money(dec(dividend) * dec(position["quantity"]))})
        # Free cash from exits before considering entries, deterministically by symbol.
        for order in sorted(pending, key=lambda o: (o["side"] == "BUY", o["requested_at"], o["ticker"])):
            fill_order(state, order, calendars[order["ticker"]][day])
        for ticker, position in state["positions"].items():
            position.update(last_close=calendars[ticker][day]["close"], price_date=day)
        reference = state["benchmark"]
        if reference["units"] is None:
            reference.update(units=float(dec(POLICY["initial_cash"]) / dec(benchmark[day]["open"])),
                             started_on=day, entry=benchmark[day]["open"])
        reference.update(last_close=benchmark[day]["close"], price_date=day)
        point = summary(state)
        point.update(date=day, ibex_return_pct=float((dec(reference["last_close"]) / dec(reference["entry"]) - 1) * 100))
        peak = max([POLICY["initial_cash"], point["equity"], *[p["equity"] for p in state["valuations"]]])
        point["drawdown_pct"] = float((dec(point["equity"]) / dec(peak) - 1) * 100)
        state["valuations"].append(point)
        state["cursor"] = day
    archive = None if state["status"] == "paused" else ingest_signals(state, report, now)
    if not state["valuations"] and state["status"] != "paused":
        state["status"] = "pending_market"
    state["summary"] = summary(state)
    validate_account(state)
    return state, archive


def load_market(state, report, now):
    from ibex.data import history_for

    tickers = set(state["positions"]) | {o["ticker"] for o in state["orders"] if o["status"] == "pending"}
    tickers |= {r["ticker"] for r in report["companies"] if RATINGS.get(str(r.get("agents", {}).get("rating", "")).casefold()) == "BUY" and re.fullmatch(r"[A-Z0-9-]+\.MC", r["ticker"])}
    result = {}
    for ticker in sorted(tickers | {"^IBEX"}):
        try:
            history = history_for(ticker, now, include_open_session=True)
            since = datetime.fromisoformat(state["cursor"]).date() - timedelta(days=7)
            history = history.loc[[i.date() >= since for i in history.index]]
            result[ticker] = bars_from_history(history)
        except Exception:
            result[ticker] = []
    return result


def main():
    parser = argparse.ArgumentParser(description="Cartera virtual IBEX; sin dinero real ni llamadas a IA")
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--previous", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    now = datetime.now(MADRID)
    args.output.mkdir(parents=True, exist_ok=True)
    report = json.loads(args.report.read_text(encoding="utf-8"))
    state = None
    if args.previous.exists():
        # Preserve the only durable history even if validation or data collection fails.
        for name in ("cartera.json", "cartera.html"):
            source, target = args.previous.parent / name, args.output / name
            if source.exists() and source.resolve() != target.resolve():
                shutil.copy2(source, target)
        history = args.previous.parent / "paper-history"
        target_history = args.output / "paper-history"
        if history.exists() and history.resolve() != target_history.resolve():
            shutil.copytree(history, target_history, dirs_exist_ok=True)
        state = json.loads(args.previous.read_text(encoding="utf-8"))
        validate_account(state)
    if state is None and (args.previous.parent / "paper-history").exists():
        raise ValueError("Falta el saldo de una cartera con historial; no se permite reiniciarla.")
    market = load_market(state or new_account(now), report, now)
    state, archive = advance(state, report, market, now)
    if archive:
        destination = args.output / archive["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            raise ValueError("La evidencia ya existe: no se sobrescribe una recomendación archivada.")
        destination.write_text(json.dumps(archive, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    from ibex.paper_render import write_portfolio, write_signal_archive
    from ibex.render import save_report

    if archive:
        write_signal_archive(archive, args.output)
    temporary = args.output / "cartera.json.tmp"
    temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    temporary.replace(args.output / "cartera.json")
    write_portfolio(state, args.output)
    save_report(report, args.output)
    print(f"Cartera ficticia: {len(state['positions'])} posiciones, {len(state['trades'])} operaciones; estado {state['status']}.")


if __name__ == "__main__":
    main()
