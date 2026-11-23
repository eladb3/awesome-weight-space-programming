#!/usr/bin/env python3
"""List recent arXiv papers matching search_config.yaml that are not yet in papers.yaml.

Usage:
    python scripts/arxiv_recent.py                 # last `lookback_days` days (default 7)
    python scripts/arxiv_recent.py --days 14
    python scripts/arxiv_recent.py --out candidates.md

This is a recall aid for the daily maintenance session. It prints every
candidate with its abstract; relevance is decided by reading the abstract,
not by the fact that a keyword matched.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NS = {"a": "http://www.w3.org/2005/Atom"}
API = "https://export.arxiv.org/api/query?"


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def to_query(phrase: str, cats: list[str]) -> str:
    # A config phrase is either "some phrase" or '"a" AND "b"'.
    parts = [p.strip().strip('"') for p in phrase.split(" AND ")] if " AND " in phrase else [phrase.strip('"')]
    terms = " AND ".join(f'(abs:"{p}" OR ti:"{p}")' for p in parts)
    cat = " OR ".join(f"cat:{c}" for c in cats)
    return f"({terms}) AND ({cat})"


def run(query: str, since: datetime) -> list[dict]:
    out, start = [], 0
    while True:
        params = {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "start": start,
            "max_results": 100,
        }
        req = urllib.request.Request(API + urllib.parse.urlencode(params), headers={"User-Agent": "awesome-wsp-recent/1.0"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    root = ET.fromstring(r.read())
                break
            except Exception as exc:
                if attempt == 3:
                    print(f"query failed: {query}: {exc}", file=sys.stderr)
                    return out
                time.sleep(5 * (attempt + 1))
        entries = root.findall("a:entry", NS)
        if not entries:
            return out
        for e in entries:
            published = datetime.fromisoformat(clean(e.findtext("a:published", namespaces=NS)).replace("Z", "+00:00"))
            if published < since:
                return out
            m = re.search(r"abs/(.+?)(v\d+)?$", clean(e.findtext("a:id", namespaces=NS)))
            out.append(
                {
                    "id": m.group(1),
                    "title": clean(e.findtext("a:title", namespaces=NS)),
                    "published": published.date().isoformat(),
                    "abstract": clean(e.findtext("a:summary", namespaces=NS)),
                }
            )
        start += 100
        time.sleep(3)


def main() -> int:
    cfg = yaml.safe_load((ROOT / "search_config.yaml").read_text(encoding="utf-8"))
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=cfg.get("lookback_days", 7))
    ap.add_argument("--out", help="write the candidate list to this file instead of stdout")
    args = ap.parse_args()

    since = datetime.now(timezone.utc) - timedelta(days=args.days)
    known = (ROOT / "papers.yaml").read_text(encoding="utf-8")
    found: dict[str, dict] = {}
    for cat, phrases in cfg["queries"].items():
        for phrase in phrases:
            for p in run(to_query(phrase, cfg["arxiv_categories"]), since):
                rec = found.setdefault(p["id"], {**p, "hits": set()})
                rec["hits"].add(f"{cat}: {phrase}")
            time.sleep(3)

    new = [p for pid, p in found.items() if f"arxiv.org/abs/{pid}" not in known]
    new.sort(key=lambda p: p["published"], reverse=True)
    lines = [f"# {len(new)} candidates not in papers.yaml (submitted in the last {args.days} days)\n"]
    for p in new:
        lines.append(f"## {p['id']} | {p['published']} | {p['title']}")
        lines.append(f"matched: {'; '.join(sorted(p['hits']))}")
        lines.append(p["abstract"] + "\n")
    text = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {len(new)} candidates to {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
