"""Validate the fixed universe against BME's official revision history."""

import io
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen

CONFIG = Path(__file__).with_name("universe.json")


def load_universe():
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    tickers = [c["ticker"] for c in config["companies"]]
    if len(tickers) != 35 or len(set(tickers)) != 35:
        raise ValueError("Se requieren 35 valores distintos")
    if not all(re.fullmatch(r"[A-Z0-9]+\.MC", t) for t in tickers):
        raise ValueError("El universo debe usar símbolos de Madrid (.MC)")
    return config


def parse_revisions(text):
    """Only no-change revisions can extend a verified universe automatically."""
    revisions = []
    for line in text.splitlines():
        match = re.match(r"\s*(\d+)\s+(\d{2}/\d{2}/\d{4})\s+(.*)$", line)
        if not match:
            continue
        number, date, changes = match.groups()
        symbols = re.sub(r"[\s—–-]", "", changes)
        revisions.append((int(number), datetime.strptime(date, "%d/%m/%Y").date(), symbols))
    if not revisions:
        raise ValueError("BME no devolvió una tabla de revisiones reconocible")
    return revisions


def verify_universe(config, now):
    """Do not silently label an old list as the current index after a change."""
    try:
        from pypdf import PdfReader

        request = Request(config["source"], headers={"User-Agent": "IBEX35-research/1.0"})
        with urlopen(request, timeout=20) as response:
            document = response.read(3_000_000)
        reader = PdfReader(io.BytesIO(document))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        revisions = parse_revisions(text)
        known = config["last_bme_revision"]
        if not any(n == known for n, _, _ in revisions):
            raise ValueError("La revisión de referencia no aparece en BME")
        latest = max((d for _, d, _ in revisions if d <= now.date()), default=None)
        changes = [(n, d) for n, d, symbols in revisions
                   if n > known and d <= now.date() and symbols]
        if changes:
            return {"verified": False, "source": config["source"],
                    "revision_date": str(latest), "checked_at": now.isoformat(),
                    "note": "BME registra cambios: revisar universe.json antes de recomendar."}
        return {"verified": True, "source": config["source"],
                "revision_date": str(latest), "checked_at": now.isoformat(),
                "note": "Lista contrastada con el histórico de revisiones de BME."}
    except Exception as exc:
        return {"verified": False, "source": config["source"],
                "revision_date": config["effective_date"], "checked_at": now.isoformat(),
                "note": f"Composición sin verificar en esta ejecución ({type(exc).__name__})."}
