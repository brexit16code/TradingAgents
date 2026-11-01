"""Public market data and dated headline samples; never brokerage APIs."""

import json
import re
import time
import unicodedata
import xml.etree.ElementTree as ET
from datetime import UTC, datetime, time as datetime_time, timedelta
from email.utils import parsedate_to_datetime
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from ibex.metrics import fundamentals, relative_return, technical

MADRID = ZoneInfo("Europe/Madrid")

NEWS_ALIASES = {
    "Banco Santander": ("santander",), "Banco Sabadell": ("sabadell",),
    "ArcelorMittal": ("arcelormittal", "arcelor mittal"),
    "IAG": ("iag", "iberia", "british airways", "vueling"),
    "Inmobiliaria Colonial": ("colonial",), "Laboratorios Rovi": ("rovi",),
    "Merlin Properties": ("merlin",), "Redeia": ("redeia", "red electrica"),
}


def company_headlines(articles, company):
    """Require the company's name in the headline, excluding the publisher suffix.

    Search matches may occur only in a site's sidebar or publisher name. Such
    matches must not be presented to the agents as verified company events.
    """
    def normalize(value):
        return "".join(ch for ch in unicodedata.normalize("NFKD", value.casefold())
                       if not unicodedata.combining(ch))

    aliases = NEWS_ALIASES.get(company["name"], (company["name"],))
    patterns = [re.compile(r"(?<!\w)" + re.escape(normalize(alias)) + r"(?!\w)")
                for alias in aliases]
    return [article for article in articles if any(
        pattern.search(normalize(article["title"].rsplit(" - ", 1)[0]))
        for pattern in patterns)]


def safe_url(url):
    if not isinstance(url, str):
        return ""
    try:
        parsed = urlparse(url)
        return url if parsed.scheme == "https" and parsed.hostname and not parsed.username else ""
    except ValueError:
        return ""


def closed_history(history, now):
    if history is None or history.empty:
        return history
    local = now.astimezone(MADRID)
    cutoff = local.date()
    # Buffer after the closing auction; a manual run must not use an unfinished bar.
    if local.time() < datetime_time(18, 0):
        cutoff -= timedelta(days=1)
    return history.loc[[i.date() <= cutoff for i in history.index]]


def history_for(ticker, now):
    import yfinance as yf

    error = None
    for attempt in range(2):
        try:
            history = yf.Ticker(ticker).history(period="2y", auto_adjust=False, timeout=20)
            if history is not None and not history.empty:
                return closed_history(history, now)
        except Exception as exc:
            error = type(exc).__name__
        if attempt == 0:
            time.sleep(1)
    raise ValueError(f"Serie no disponible: {ticker} ({error or 'respuesta vacía'})")


def rss_news(query, now, limit=6):
    url = "https://news.google.com/rss/search?" + urlencode({
        "q": f'{query} when:7d', "hl": "es", "gl": "ES", "ceid": "ES:es",
    })
    request = Request(url, headers={"User-Agent": "IBEX35-research/1.0"})
    with urlopen(request, timeout=15) as response:
        root = ET.fromstring(response.read(2_000_000))
    articles, seen = [], set()
    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "").strip()
        link = safe_url(item.findtext("link"))
        try:
            published = parsedate_to_datetime(item.findtext("pubDate") or "")
            if published.tzinfo is None:
                published = published.replace(tzinfo=UTC)
        except (ValueError, TypeError, OverflowError):
            continue
        if not (now - timedelta(days=7) <= published <= now) or not link or not title:
            continue
        if title.casefold() in seen:
            continue
        seen.add(title.casefold())
        articles.append({"title": title, "url": link,
                         "publisher": item.findtext("source") or "Google News (agregador)",
                         "published_at": published.isoformat()})
    return sorted(articles, key=lambda a: a["published_at"], reverse=True)[:limit]


def statement_summary(ticker):
    """Period-end dates are NOT publication dates; never used for backtests."""
    result = []
    specifications = (
        ("income_stmt", ("Total Revenue", "Net Income", "EBITDA")),
        ("balance_sheet", ("Total Assets", "Total Debt", "Stockholders Equity")),
        ("cashflow", ("Operating Cash Flow", "Capital Expenditure", "Free Cash Flow")),
    )
    for attr, fields in specifications:
        frame = getattr(ticker, attr)
        if frame is None or frame.empty:
            continue
        periods = []
        for column in list(frame.columns)[:3]:
            values = {}
            for field in fields:
                if field in frame.index:
                    from ibex.metrics import number

                    values[field] = number(frame.loc[field, column])
            periods.append({"period_end": str(column.date()), "values": values})
        result.append({"statement": attr, "periods": periods})
    return result


def collect(company, benchmark, now):
    import yfinance as yf

    row = {**company, "status": "unavailable", "warnings": [], "news": [],
           "retrieved_at": now.isoformat(), "technical": {}, "fundamentals": {},
           "sources": {"quote": f"https://finance.yahoo.com/quote/{company['ticker']}/",
                       "financials": f"https://finance.yahoo.com/quote/{company['ticker']}/financials/"}}
    try:
        history = history_for(company["ticker"], now)
        row["technical"] = technical(history)
        if not row["technical"]:
            raise ValueError("Precios insuficientes")
        row["technical"]["relative63_pp"] = relative_return(history, benchmark)
        reference_date = (benchmark.index[-1].date() if benchmark is not None and not benchmark.empty
                          else now.astimezone(MADRID).date())
        price_date = datetime.fromisoformat(row["technical"]["price_date"]).date()
        row["stale"] = (reference_date - price_date).days > 0 or (now.date() - price_date).days > 5
        if row["stale"]:
            row["warnings"].append("Cotización atrasada respecto al índice o más de cinco días sin datos.")
        ticker = yf.Ticker(company["ticker"])
        try:
            info = ticker.get_info() or {}
            row["fundamentals"] = fundamentals(info, company)
            row["vendor_name"] = info.get("longName") or info.get("shortName")
            if row["fundamentals"].get("currency") != "EUR":
                row["warnings"].append("Divisa no verificada como EUR: se bloquea la señal.")
        except Exception as exc:
            row["warnings"].append(f"Ratios no disponibles ({type(exc).__name__}).")
        try:
            row["statements"] = statement_summary(ticker)
            if not row["statements"]:
                row["warnings"].append("Estados financieros no disponibles en la fuente gratuita.")
        except Exception as exc:
            row["warnings"].append(f"Estados financieros incompletos ({type(exc).__name__}).")
        row["status"] = "ok"
    except Exception as exc:
        row["warnings"].append(f"Precios no disponibles ({type(exc).__name__}).")
    try:
        candidates = rss_news(f'"{company["name"]}" bolsa resultados', now, limit=20)
        row["news"] = company_headlines(candidates, company)[:6]
        if not row["news"]:
            row["warnings"].append("La muestra de titulares no cubre esta empresa en los últimos siete días.")
    except Exception as exc:
        row["warnings"].append(f"Fuente de noticias no disponible ({type(exc).__name__}).")
    row["fundamentals_note"] = ("Instantánea de Yahoo al descargar; los períodos contables no "
                                "certifican cuándo se publicaron las cifras. No apta para backtesting.")
    return row


def compact_evidence(row):
    keep = {k: row.get(k) for k in ("ticker", "name", "kind", "retrieved_at", "technical",
                                   "fundamentals", "statements", "valuation", "news", "warnings", "sources")}
    keep["technical"] = {k: v for k, v in (keep["technical"] or {}).items() if k != "chart"}
    return json.dumps(keep, ensure_ascii=False, allow_nan=False)
