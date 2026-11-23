#!/usr/bin/env python3
"""Generate README.md from papers.yaml, or check that they are in sync.

Usage:
    python scripts/build_readme.py           # validate papers.yaml and rewrite README.md
    python scripts/build_readme.py --check   # validate and fail if README.md is stale (used in CI)

papers.yaml is the single source of truth. README.md is generated; never edit
the paper list in README.md by hand.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "papers.yaml"
README = ROOT / "README.md"
TEMPLATE = ROOT / "scripts" / "readme_header.md"

REQUIRED = ("title", "authors", "year", "date", "url", "category", "note")
OPTIONAL = ("venue", "code")
ALLOWED = set(REQUIRED) | set(OPTIONAL) | {"citations"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ARXIV_RE = re.compile(r"^https://arxiv\.org/abs/(\d{4}\.\d{4,5})$")
URL_RE = re.compile(r"^https://[^\s]+$")
MAX_NOTE = 300


def slugify(text: str) -> str:
    """GitHub-style heading anchor."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def arxiv_id(url: str) -> str | None:
    m = ARXIV_RE.match(url)
    return m.group(1) if m else None


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or not all(k in data for k in ("groups", "categories", "papers")):
        return ["papers.yaml must have top-level keys 'groups', 'categories' and 'papers'"]

    group_ids = []
    for i, grp in enumerate(data["groups"]):
        for key in ("id", "title", "description"):
            if not isinstance(grp.get(key), str) or not grp[key].strip():
                errors.append(f"group #{i + 1}: missing or empty '{key}'")
        group_ids.append(grp.get("id"))
    if len(group_ids) != len(set(group_ids)):
        errors.append("duplicate group ids")

    cat_ids = []
    for i, cat in enumerate(data["categories"]):
        for key in ("id", "group", "title", "description"):
            if not isinstance(cat.get(key), str) or not cat[key].strip():
                errors.append(f"category #{i + 1}: missing or empty '{key}'")
        if cat.get("group") not in group_ids:
            errors.append(f"category {cat.get('id')!r}: unknown group {cat.get('group')!r}")
        cat_ids.append(cat.get("id"))
    titles = [g.get("title") for g in data["groups"]] + [c.get("title") for c in data["categories"]]
    if len(titles) != len(set(titles)):
        errors.append("group and category titles must all be distinct (they become README anchors)")
    if len(cat_ids) != len(set(cat_ids)):
        errors.append("duplicate category ids")

    seen_urls: dict[str, str] = {}
    seen_titles: dict[str, str] = {}
    this_year = date.today().year
    for i, p in enumerate(data["papers"]):
        label = f"paper #{i + 1} ({p.get('title', '<no title>')!r})"
        if not isinstance(p, dict):
            errors.append(f"paper #{i + 1}: not a mapping")
            continue
        for key in REQUIRED:
            val = p.get(key)
            if val is None or (isinstance(val, str) and not val.strip()):
                errors.append(f"{label}: missing required field '{key}'")
        for key in p:
            if key not in ALLOWED:
                errors.append(f"{label}: unknown field '{key}'")
        for key in OPTIONAL:
            if key in p and (not isinstance(p[key], str) or not p[key].strip()):
                errors.append(f"{label}: optional field '{key}' is present but empty; omit it instead")
        year = p.get("year")
        if year is not None and (not isinstance(year, int) or not 1980 <= year <= this_year + 1):
            errors.append(f"{label}: year must be an integer between 1980 and {this_year + 1}")
        d = p.get("date")
        if d is not None:
            if not isinstance(d, str) or not DATE_RE.match(d):
                errors.append(f"{label}: date must be a quoted string 'YYYY-MM-DD'")
            elif isinstance(year, int) and int(d[:4]) != year:
                errors.append(f"{label}: date {d} does not match year {year}")
        if "citations" in p and (not isinstance(p["citations"], int) or p["citations"] < 0):
            errors.append(f"{label}: citations must be a non-negative integer")
        for key in ("url", "code"):
            val = p.get(key)
            if isinstance(val, str) and val and not URL_RE.match(val):
                errors.append(f"{label}: '{key}' must be an https URL")
        url = p.get("url")
        if isinstance(url, str) and "arxiv.org" in url and not ARXIV_RE.match(url):
            errors.append(f"{label}: arXiv URLs must look like https://arxiv.org/abs/XXXX.XXXXX (no version, no pdf)")
        if p.get("category") is not None and p.get("category") not in cat_ids:
            errors.append(f"{label}: unknown category {p.get('category')!r}")
        note = p.get("note")
        if isinstance(note, str):
            if len(note) > MAX_NOTE:
                errors.append(f"{label}: note is longer than {MAX_NOTE} characters")
            if not note.rstrip().endswith("."):
                errors.append(f"{label}: note should be one sentence ending with a period")
            if "\n" in note.strip():
                errors.append(f"{label}: note must be a single line")
        if isinstance(url, str):
            if url in seen_urls:
                errors.append(f"{label}: duplicate url (also used by {seen_urls[url]!r})")
            seen_urls[url] = p.get("title", "")
        if isinstance(p.get("title"), str):
            t = re.sub(r"\W+", " ", p["title"].lower()).strip()
            if t in seen_titles:
                errors.append(f"{label}: duplicate title")
            seen_titles[t] = p["title"]
        for key in ("title", "authors", "venue"):
            if isinstance(p.get(key), str) and ("|" in p[key] or "\n" in p[key].strip()):
                errors.append(f"{label}: '{key}' must be a single line without '|'")
    return errors


def sort_key(p: dict):
    # Newest first by publication date, then arXiv id, then title.
    aid = arxiv_id(p["url"]) or "0000.00000"
    yymm, num = aid.split(".")
    return (-int(p["date"].replace("-", "")), -int(yymm), -int(num), p["title"].lower())


def render_entry(p: dict) -> str:
    venue = p.get("venue", "arXiv preprint")
    authors = p["authors"]
    meta = f"{authors}, {venue}. Published {p['date']}"
    if "citations" in p:
        n = p["citations"]
        meta += f", {n:,} citation{'s' if n != 1 else ''}"
    line = f"- [{p['title']}]({p['url']}) - *{meta}.* {p['note']}"
    if p.get("code"):
        line += f" [[Code]({p['code']})]"
    return line


def render(data: dict) -> str:
    header = TEMPLATE.read_text(encoding="utf-8").rstrip() + "\n"
    cats = data["categories"]
    papers = data["papers"]
    by_cat = {c["id"]: [] for c in cats}
    for p in papers:
        by_cat[p["category"]].append(p)

    groups = data["groups"]
    cats_in = {g["id"]: [c for c in cats if c["group"] == g["id"]] for g in groups}

    out = [header]
    when = data.get("citations_updated")
    out.append(
        "Publication dates are those of the first public version, usually arXiv v1."
        + (f" Citation counts are from [Semantic Scholar](https://www.semanticscholar.org/), updated {when}." if when else "")
        + "\n"
    )
    out.append("## Contents\n")
    for g in groups:
        n = sum(len(by_cat[c["id"]]) for c in cats_in[g["id"]])
        out.append(f"- [{g['title']}](#{slugify(g['title'])}) ({n})")
        for c in cats_in[g["id"]]:
            out.append(f"  - [{c['title']}](#{slugify(c['title'])}) ({len(by_cat[c['id']])})")
    out.append("- [Contributing](#contributing)")
    out.append("- [License](#license)\n")

    for g in groups:
        out.append(f"## {g['title']}\n")
        out.append(f"{g['description'].strip()}\n")
        for c in cats_in[g["id"]]:
            out.append(f"### {c['title']}\n")
            out.append(f"{c['description'].strip()}\n")
            for p in sorted(by_cat[c["id"]], key=sort_key):
                out.append(render_entry(p))
            out.append("")
            out.append("**[⬆ back to top](#contents)**\n")

    out.append("## Contributing\n")
    out.append(
        "Contributions are welcome! The list is generated from [`papers.yaml`](papers.yaml): "
        "add an entry there, run `python scripts/build_readme.py`, and open a pull request. "
        "See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and the entry format.\n"
    )
    out.append("## License\n")
    out.append(
        "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)\n\n"
        "To the extent possible under law, the contributors have waived all copyright and related "
        "or neighboring rights to this work. See [LICENSE](LICENSE).\n"
    )
    out.append(
        f"<sub>{len(papers)} papers. This file is generated from `papers.yaml` by "
        "`scripts/build_readme.py`; do not edit it by hand.</sub>"
    )
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if README.md is out of date")
    args = ap.parse_args()

    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("papers.yaml is invalid:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    text = render(data)
    if args.check:
        current = README.read_text(encoding="utf-8") if README.exists() else ""
        if current != text:
            print("README.md is out of sync with papers.yaml. Run: python scripts/build_readme.py", file=sys.stderr)
            diff = difflib.unified_diff(
                current.splitlines(), text.splitlines(), "README.md (committed)", "README.md (generated)", lineterm="", n=1
            )
            for line in list(diff)[:40]:
                print(line, file=sys.stderr)
            return 1
        print(f"OK: {len(data['papers'])} papers valid, README.md in sync.")
        return 0

    README.write_text(text, encoding="utf-8")
    print(f"Wrote README.md with {len(data['papers'])} papers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
