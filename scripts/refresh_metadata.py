#!/usr/bin/env python3
"""Fill in publication dates and refresh citation counts in papers.yaml.

Usage:
    python scripts/refresh_metadata.py              # dates for entries missing one, and all citation counts
    python scripts/refresh_metadata.py --no-citations

- `date` is the date of the first arXiv version (v1), from the arXiv API.
  Existing dates are never changed. Non-arXiv entries need a date by hand.
- `citations` is Semantic Scholar's citationCount, looked up by arXiv ID.
  When Semantic Scholar has no record of a paper, its previous count is kept.
- The top-level `citations_updated` date is set when the citation refresh succeeds.

The script rewrites the `papers:` part of papers.yaml in canonical field order
and keeps everything above it, including comments, unchanged.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arxiv_lookup  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "papers.yaml"
FIELD_ORDER = ("title", "authors", "year", "date", "venue", "url", "code", "category", "citations", "note")
S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount"


def arxiv_id(url: str) -> str | None:
    m = re.match(r"^https://arxiv\.org/abs/(\d{4}\.\d{4,5})$", url)
    return m.group(1) if m else None


def s2_citations(ids: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for start in range(0, len(ids), 400):
        chunk = ids[start : start + 400]
        body = json.dumps({"ids": [f"ARXIV:{i}" for i in chunk]}).encode()
        req = urllib.request.Request(S2_BATCH, data=body, headers={"Content-Type": "application/json"})
        for attempt in range(6):
            try:
                with urllib.request.urlopen(req, timeout=90) as resp:
                    res = json.load(resp)
                break
            except Exception as exc:  # 429 rate limit or network hiccup
                if attempt == 5:
                    raise RuntimeError(f"Semantic Scholar request failed: {exc}") from exc
                wait = 10 * (attempt + 1)
                print(f"Semantic Scholar: {exc}; retrying in {wait}s", file=sys.stderr)
                time.sleep(wait)
        for i, rec in zip(chunk, res):
            if rec and isinstance(rec.get("citationCount"), int):
                counts[i] = rec["citationCount"]
        time.sleep(2)
    return counts


def dump_papers(papers: list[dict]) -> str:
    ordered = [{k: p[k] for k in FIELD_ORDER if k in p} | {k: v for k, v in p.items() if k not in FIELD_ORDER} for p in papers]
    body = yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True, width=1000)
    return "\n".join("  " + line if line else line for line in body.splitlines()) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-citations", action="store_true", help="only fill in missing dates")
    args = ap.parse_args()

    text = DATA.read_text(encoding="utf-8")
    head, sep, _ = text.partition("\npapers:\n")
    if not sep:
        print("papers.yaml: could not find the 'papers:' key", file=sys.stderr)
        return 1
    papers = yaml.safe_load(text)["papers"]

    # Dates: only for entries that lack one.
    missing = [arxiv_id(p["url"]) for p in papers if "date" not in p and arxiv_id(p["url"])]
    if missing:
        published = {r["id"]: r["published"][:10] for r in arxiv_lookup.fetch(missing)}
        for p in papers:
            aid = arxiv_id(p["url"])
            if "date" not in p and aid in published:
                p["date"] = published[aid]
        print(f"dates: filled {sum(1 for i in missing if i in published)} of {len(missing)} missing")
    no_date = [p["title"] for p in papers if "date" not in p]
    for t in no_date:
        print(f"dates: no date for {t!r}; add it by hand from the publisher page", file=sys.stderr)

    # Citations: refresh all.
    if not args.no_citations:
        ids = [a for a in (arxiv_id(p["url"]) for p in papers) if a]
        try:
            counts = s2_citations(ids)
        except RuntimeError as exc:
            print(f"citations: {exc}; counts left unchanged", file=sys.stderr)
            counts = None
        if counts is not None:
            changed = 0
            for p in papers:
                aid = arxiv_id(p["url"])
                if aid in counts and p.get("citations") != counts[aid]:
                    p["citations"] = counts[aid]
                    changed += 1
            print(f"citations: {len(counts)} of {len(ids)} found on Semantic Scholar, {changed} changed")
            stamp = f"citations_updated: '{date.today().isoformat()}'"
            if re.search(r"^citations_updated:.*$", head, flags=re.M):
                head = re.sub(r"^citations_updated:.*$", stamp, head, flags=re.M)
            else:
                head = head.rstrip("\n") + "\n\n# Date of the last citation-count refresh (scripts/refresh_metadata.py).\n" + stamp + "\n"

    DATA.write_text(head + "\npapers:\n" + dump_papers(papers), encoding="utf-8")
    return 1 if no_date else 0


if __name__ == "__main__":
    sys.exit(main())
