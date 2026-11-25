# CLAUDE.md

This repository is a curated awesome-list of papers on **weight-space programming (WSP)**: treating a trained network's weights as something you directly read, edit, and write. The scope and its exclusions are defined at the top of `scripts/readme_header.md` (rendered into `README.md`) and in `CONTRIBUTING.md`. Read both before judging relevance.

## Layout

- `papers.yaml`: the single source of truth. It holds `groups` (top-level README sections), `categories` (subsections, each with a `group`), and `papers`.
- `scripts/build_readme.py`: validates `papers.yaml` and regenerates `README.md`. `--check` is the CI check.
- `scripts/readme_header.md`: the static README intro, which defines WSP.
- `scripts/refresh_metadata.py`: fills in missing `date` fields from arXiv and refreshes every `citations` count from Semantic Scholar, stamping `citations_updated`.
- `scripts/arxiv_lookup.py`: prints verified `papers.yaml` stubs (title, authors, year, date, url) from the arXiv API. Pass `--abstract` to include abstracts and `--known` to flag duplicates.
- `scripts/arxiv_recent.py`: runs the queries in `search_config.yaml` against the arXiv API for the last N days and lists candidates that are not yet in `papers.yaml`, with abstracts.
- `search_config.yaml`: keyword starting points for searches.
- `MAINTENANCE_LOG.md`: one line per maintenance run that changed something.
- `.github/workflows/check.yml`: CI that runs `python scripts/build_readme.py --check`.

## Rules for every change

- Never hand-edit the paper list in `README.md`. Edit `papers.yaml`, then run `python scripts/build_readme.py`.
- Never add a paper from memory. Title, authors, year and URL must come from the arXiv API or page (use `scripts/arxiv_lookup.py`) or from the publisher page. If you cannot verify a paper, leave it out.
- `note` is one sentence in your own words on why the paper matters for WSP. Do not paraphrase the abstract's first sentence.
- Use the year of arXiv v1. Venue is optional; set it only when the arXiv comment or journal-ref, the publisher page, or the venue's proceedings or OpenReview page confirms acceptance.
- Run `python scripts/build_readme.py --check` before every commit.

## Daily maintenance

A scheduled Claude session runs this routine once a day. It commits directly to `main`.

1. **Sync.** Check out `main` and pull, then run `pip install -r requirements.txt` if PyYAML is missing.
2. **Collect candidates from the last 7 days.** The 7-day window is deliberate: overlapping windows mean a missed run loses nothing. Run:

   ```bash
   python scripts/arxiv_recent.py --days 7 --out /tmp/wsp_candidates.md
   ```

   Then go beyond the keyword list. Run a few web searches for WSP work from the past week, such as new model-editing, model-merging, weight-generation, weight-space-learning and parameter-decomposition papers, and above all LLMs or agents that read or modify model weights ("weight-space programming"). Also run free-form arXiv API queries for phrasings the config misses. Add any good new phrasing to `search_config.yaml`. Much WSP work first appears as research blog posts or project pages, not arXiv papers. Search for those too, and add one only if you can read its title, authors and date from the page itself or from its source on GitHub (raw.githubusercontent.com). Set `venue` to `Blog post (<organization>)`, take `date` from the page, and leave `citations` out.
3. **Judge relevance by reading each abstract**, not by keyword match. Apply the scope and exclusions from `CONTRIBUTING.md`. For a borderline paper, ask whether a reader interested in directly manipulating weights would want it. Prefer leaving out a marginal incremental variant over cluttering the list. Search hardest for the core Weight-Space Programming group (the `wsp-*` categories): LLMs or agents reading, editing, or writing weights, including papers that use the phrase "weight-space programming".
4. **Skip duplicates.** Drop anything whose arXiv ID or title is already in `papers.yaml`. `arxiv_recent.py` already removes ID matches; also check titles for papers that are listed under a non-arXiv URL.
5. **Verify and add.** For each paper you keep, run:

   ```bash
   python scripts/arxiv_lookup.py --known <id> [<id> ...]
   ```

   Paste the stub into `papers.yaml`, then set `category`, a one-sentence `note` in your own words, and `venue` or `code` only if confirmed (see the rules above). Do not alter the title, authors, year, date or URL that the lookup printed.
6. **Backfill venue and code.** Look at existing entries that have no `venue` or no `code`. Start with the oldest-added and check about 15 per run. Run `scripts/arxiv_lookup.py` on their IDs to see the current arXiv comment and journal-ref, and check the publisher or OpenReview page or the paper's project page. Fill in a venue or official code link only when a primary source confirms it.
7. **Refresh citations.** On every run, whether or not papers were added, run:

   ```bash
   python scripts/refresh_metadata.py
   ```

   It refreshes all citation counts from Semantic Scholar and fills any missing dates. If Semantic Scholar is unreachable or rate-limited after retries, it leaves the counts unchanged; note that in the commit message and carry on.
8. **Regenerate and check.** Run:

   ```bash
   python scripts/build_readme.py
   ```

   ```bash
   python scripts/build_readme.py --check
   ```

   Both must succeed. If the check fails, fix `papers.yaml`. Do not edit the check to make it pass.
9. **Log.** If anything was added or backfilled, add one line at the top of the log table in `MAINTENANCE_LOG.md`:
   `| YYYY-MM-DD | added: <short titles (arXiv IDs)>; backfilled: <...> | skipped borderline: <short title (ID): reason>; ... |`
   Always list borderline papers you skipped, so the maintainer can overrule the call.
10. **Commit and push.** If anything changed, commit to `main` with a message like:

   ```
   Daily update YYYY-MM-DD: add N papers

   - <Title> (arXiv:<id>) [<category>]
   - Backfilled venue for <Title>
   - Refreshed citation counts
   ```

   Then push to `origin main`. If only citation counts changed, commit with the message `Daily update YYYY-MM-DD: refresh citation counts` and add no log line. **If nothing changed at all, make no commit.**
11. **Safety.** Do not change the scripts, CI or README template during a maintenance run unless one is broken. In that case, fix it in a separate commit and explain the fix in the commit message. Never rewrite history on `main`.
