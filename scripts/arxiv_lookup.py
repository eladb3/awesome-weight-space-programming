#!/usr/bin/env python3
"""Fetch verified metadata for arXiv papers and print papers.yaml stubs.

Usage:
    python scripts/arxiv_lookup.py 2202.05262 2210.07229 ...
    python scripts/arxiv_lookup.py --abstract 2202.05262      # also print the abstract
    python scripts/arxiv_lookup.py --known 2202.05262         # report whether already in papers.yaml

Title, authors, year and URL in the stub come straight from the arXiv API,
so entries added this way are verified against arXiv. The 'category' and
'note' fields are left for a human (or the maintenance session) to fill in.
Year is the year of the first arXiv version.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

API = "https://export.arxiv.org/api/query?id_list={ids}&max_results={n}"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
ROOT = Path(__file__).resolve().parent.parent


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def format_authors(names: list[str]) -> str:
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{names[0]} et al."


def fetch(ids: list[str]) -> list[dict]:
    results = []
    for start in range(0, len(ids), 50):
        chunk = ids[start : start + 50]
        url = API.format(ids=",".join(chunk), n=len(chunk))
        req = urllib.request.Request(url, headers={"User-Agent": "awesome-wsp-lookup/1.0"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    xml = resp.read()
                break
            except Exception as exc:  # network hiccup or rate limit
                if attempt == 3:
                    raise
                print(f"retrying after error: {exc}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
        root = ET.fromstring(xml)
        for entry in root.findall("a:entry", NS):
            eid = clean(entry.findtext("a:id", default="", namespaces=NS))
            m = re.search(r"abs/([^v]+?)(v\d+)?$", eid)
            if not m or not entry.findtext("a:title", namespaces=NS):
                continue
            results.append(
                {
                    "id": m.group(1),
                    "title": clean(entry.findtext("a:title", namespaces=NS)),
                    "authors": [clean(a.findtext("a:name", namespaces=NS)) for a in entry.findall("a:author", NS)],
                    "published": clean(entry.findtext("a:published", namespaces=NS)),
                    "abstract": clean(entry.findtext("a:summary", namespaces=NS)),
                    "comment": clean(entry.findtext("arxiv:comment", default="", namespaces=NS)),
                    "journal_ref": clean(entry.findtext("arxiv:journal_ref", default="", namespaces=NS)),
                }
            )
        if start + 50 < len(ids):
            time.sleep(3)
    return results


def yq(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--abstract", action="store_true")
    ap.add_argument("--known", action="store_true", help="flag ids already present in papers.yaml")
    args = ap.parse_args()

    ids = [re.sub(r"v\d+$", "", i.strip().split("/")[-1]) for i in args.ids]
    known = (ROOT / "papers.yaml").read_text(encoding="utf-8") if args.known else ""
    found = {r["id"]: r for r in fetch(ids)}
    status = 0
    for i in ids:
        r = found.get(i)
        if not r:
            print(f"# NOT FOUND on arXiv: {i}")
            status = 1
            continue
        if args.known and f"arxiv.org/abs/{i}" in known:
            print(f"# already in papers.yaml: {i}")
        print(f"  - title: {yq(r['title'])}")
        print(f"    authors: {yq(format_authors(r['authors']))}")
        print(f"    year: {r['published'][:4]}")
        print(f"    url: https://arxiv.org/abs/{i}")
        extra = "; ".join(x for x in (r["comment"], r["journal_ref"]) if x)
        if extra:
            print(f"    # arXiv comment/journal-ref: {extra}")
        if args.abstract:
            print(f"    # abstract: {r['abstract']}")
        print()
    return status


if __name__ == "__main__":
    sys.exit(main())
