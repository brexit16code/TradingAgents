"""Explicit, reproducible screening rules; no portfolio or execution functions."""

import math
import statistics

import pandas as pd


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def technical(history):
    if history is None or history.empty or "Close" not in history:
        return {}
    raw = history["Close"].dropna()
    close = history.get("Adj Close", history["Close"]).dropna()
    close = close[close > 0]
    if len(raw) < 2 or len(close) < 2:
        return {}
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    rsi = 100 - 100 / (1 + gain / loss.replace(0, float("nan")))
    rsi = rsi.mask((gain > 0) & (loss == 0), 100)
    rsi = rsi.mask((gain == 0) & (loss > 0), 0)
    rsi = rsi.mask((gain == 0) & (loss == 0), 50)
    macd = (close.ewm(span=12, adjust=False, min_periods=12).mean()
            - close.ewm(span=26, adjust=False, min_periods=26).mean())
    signal = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    result = {
        "close": number(raw.iloc[-1]), "adjusted_close": number(close.iloc[-1]),
        "price_date": str(raw.index[-1].date()), "sessions": len(close),
        "change_pct": number((close.iloc[-1] / close.iloc[-2] - 1) * 100),
        "rsi14": number(rsi.iloc[-1]), "macd": number(macd.iloc[-1]),
        "macd_signal": number(signal.iloc[-1]),
        "volatility_pct": number(close.pct_change().tail(63).std() * math.sqrt(252) * 100),
        "drawdown_pct": number((close.iloc[-1] / close.tail(252).max() - 1) * 100),
        "chart": [{"date": str(index.date()), "value": number(value)}
                  for index, value in close.tail(252).items()],
    }
    for period in (20, 50, 200):
        result[f"sma{period}"] = number(close.rolling(period).mean().iloc[-1])
    for period in (21, 63, 252):
        result[f"return{period}_pct"] = (
            number((close.iloc[-1] / close.iloc[-period - 1] - 1) * 100)
            if len(close) > period else None
        )
    return result


def relative_return(history, benchmark, period=63):
    """Use the same trading dates for both legs, including suspended stocks."""
    if history is None or benchmark is None or history.empty or benchmark.empty:
        return None
    left = history.get("Adj Close", history["Close"]).copy()
    right = benchmark.get("Adj Close", benchmark["Close"]).copy()
    left.index = pd.to_datetime([i.date() for i in left.index])
    right.index = pd.to_datetime([i.date() for i in right.index])
    common = pd.concat([left.rename("stock"), right.rename("ibex")], axis=1).dropna()
    if len(common) <= period:
        return None
    returns = common.iloc[-1] / common.iloc[-period - 1] - 1
    return number((returns["stock"] - returns["ibex"]) * 100)


INFO_KEYS = (
    "marketCap", "trailingPE", "forwardPE", "priceToBook", "enterpriseToEbitda",
    "trailingEps", "forwardEps", "revenueGrowth", "earningsGrowth", "returnOnEquity",
    "profitMargins", "totalDebt", "totalCash", "ebitda", "operatingCashflow",
    "freeCashflow", "dividendYield", "dividendRate", "payoutRatio", "bookValue",
    "targetMeanPrice", "targetLowPrice", "targetHighPrice", "numberOfAnalystOpinions",
)


def fundamentals(info, company):
    values = {key: number(info.get(key)) for key in INFO_KEYS}
    values.update({"sector": info.get("sector"), "industry": info.get("industry"),
                   "currency": info.get("currency"), "financial_currency": info.get("financialCurrency"),
                   "fiscal_period_end": info.get("mostRecentQuarter")})
    # Derive yield to avoid vendors mixing percent and decimal units in dividendYield.
    price, dividend = number(info.get("currentPrice")), values["dividendRate"]
    values["dividend_yield_pct"] = dividend / price * 100 if dividend is not None and price and price > 0 else None
    debt, cash, ebitda = (values[k] for k in ("totalDebt", "totalCash", "ebitda"))
    values["net_debt_ebitda"] = ((debt - cash) / ebitda
                                if company["kind"] == "corporate"
                                and None not in (debt, cash, ebitda) and ebitda > 0 else None)
    # Do not turn an analyst target into an intrinsic valuation, or compare currencies.
    target = values["targetMeanPrice"]
    values["consensus_upside_pct"] = ((target / price - 1) * 100
                                       if target and target > 0 and price and price > 0 else None)
    return values


def add_peer_valuations(rows):
    """A descriptive sector multiple comparison, not an intrinsic value model."""
    for row in rows:
        f = row.get("fundamentals", {})
        sector, own = f.get("sector"), f.get("forwardPE")
        peers = [r for r in rows if r.get("status") == "ok" and r.get("kind") == row.get("kind")
                 and r.get("fundamentals", {}).get("sector") == sector and sector
                 and (r.get("fundamentals", {}).get("forwardPE") or 0) > 0
                 and (r.get("fundamentals", {}).get("forwardPE") or 0) < 150]
        if not own or own <= 0 or own >= 150 or len(peers) < 3:
            row["valuation"] = {"label": "Comparación sectorial no disponible"}
            continue
        median = statistics.median(r["fundamentals"]["forwardPE"] for r in peers)
        ratio = own / median
        label = "PER relativo inferior" if ratio < 0.8 else "PER relativo superior" if ratio > 1.2 else "PER relativo intermedio"
        row["valuation"] = {"label": label, "peer_median_forward_pe": median,
                            "ratio": ratio, "peers": [r["ticker"] for r in peers]}


def screen(row, universe_verified):
    """Missing, stale or unverified inputs must never become a positive signal."""
    t, f = row.get("technical", {}), row.get("fundamentals", {})
    reasons, risks = [], list(row.get("warnings", []))
    if (row.get("status") != "ok" or not universe_verified or row.get("stale")
            or t.get("sma200") is None or not f.get("sector")
            or f.get("currency") != "EUR"):
        return {"label": "Datos insuficientes", "score": None, "reasons": [],
                "risks": risks + ["Revisar cobertura, antigüedad, divisa y composición antes de valorar."]}
    score = 0
    if t["adjusted_close"] > t["sma50"] > t["sma200"]:
        score += 2
        reasons.append("El cierre ajustado está por encima de las medias de 50 y 200 sesiones.")
    elif t["adjusted_close"] < t["sma50"] < t["sma200"]:
        score -= 2
        risks.append("El cierre ajustado está por debajo de las medias de 50 y 200 sesiones.")
    relative = t.get("relative63_pp")
    if relative is not None:
        if relative > 3:
            score += 1
            reasons.append(f"Supera al IBEX en {relative:.1f} puntos en 63 sesiones comparables.")
        elif relative < -3:
            score -= 1
            risks.append(f"Queda {abs(relative):.1f} puntos por detrás del IBEX en 63 sesiones.")
    growth = f.get("revenueGrowth")
    if growth is not None:
        if growth > 0:
            score += 1
            reasons.append(f"Crecimiento de ingresos publicado por el proveedor: {growth * 100:.1f}%.")
        elif growth < -0.05:
            score -= 1
            risks.append(f"Ingresos en descenso: {growth * 100:.1f}% según el proveedor.")
    ratio = row.get("valuation", {}).get("ratio")
    if ratio is not None and ratio < 0.8:
        score += 1
        reasons.append("PER estimado inferior a la mediana de los comparables disponibles.")
    elif ratio is not None and ratio > 1.2:
        score -= 1
        risks.append("PER estimado superior a la mediana de los comparables disponibles.")
    if (f.get("net_debt_ebitda") or 0) > 4:
        score -= 1
        risks.append("Deuda neta/EBITDA superior a 4; revisar su sostenibilidad y el sector.")
    if (t.get("rsi14") or 0) > 70:
        risks.append("RSI superior a 70: posible extensión del movimiento.")
    if (t.get("volatility_pct") or 0) > 40:
        risks.append("Volatilidad anualizada de 63 sesiones superior al 40%.")
    if not row.get("news"):
        risks.append("Cobertura de noticias insuficiente; no equivale a ausencia de acontecimientos.")
    if row["kind"] in {"bank", "insurance", "reit"}:
        risks.append("Faltan métricas específicas del sector; no se aplican reglas de deuda industrial.")
    if not reasons:
        reasons.append("Las reglas no detectan una combinación favorable suficiente.")
    return {"label": "Vigilar favorable" if score >= 3 else "Precaución" if score <= -2 else "Neutral",
            "score": score, "reasons": reasons, "risks": risks,
            "method": "Filtro de reglas sin IA; noticias sin interpretación semántica."}
