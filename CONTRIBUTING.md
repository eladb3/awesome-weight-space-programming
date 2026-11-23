# Contributing

Thanks for helping improve **Awesome Weight-Space Programming**! The paper list lives in [`papers.yaml`](papers.yaml). `README.md` is generated from that file, so **do not edit the paper list in `README.md` by hand**: CI fails if the two are out of sync.

## Is the paper in scope?

The core of the list is **weight-space programming**: LLMs or agents that read, edit, or write a network's weights directly (the `wsp-*` categories). It also covers the foundations this builds on, which treat a trained network's weights as something to directly compute, compose, learn from, or read. These are model and knowledge editing, task vectors and model merging, weight-space learning, weight generation, and weight-based interpretability. Benchmarks, datasets, tools, model zoos, and surveys for any of these are in scope too.

Out of scope: ordinary fine-tuning, PEFT methods that are only a training recipe, activation steering with no weight change, and pruning or quantization unless the paper is about weight-space structure. For borderline papers, ask: would someone interested in directly manipulating weights want to read this?

## Adding a paper

1. Install the one dependency: `pip install -r requirements.txt`.
2. Get a verified stub from arXiv (title, authors, year, date and URL come from the arXiv API):

   ```bash
   python scripts/arxiv_lookup.py --known 2202.05262
   ```

   For papers that are not on arXiv, copy the title, authors and year from the publisher page.
3. Paste the stub under `papers:` in `papers.yaml` and fill in the rest:

   ```yaml
   - title: "Locating and Editing Factual Associations in GPT"
     authors: "Kevin Meng et al."
     year: 2022
     date: '2022-02-10'
     venue: "NeurIPS 2022"          # optional; omit for preprints
     url: https://arxiv.org/abs/2202.05262
     code: https://github.com/kmeng01/rome   # optional
     category: model-editing
     note: "Locates factual recall in mid-layer MLPs and rewrites a fact with a closed-form rank-one weight update (ROME)."
   ```

4. Optionally fill in the date and citation count automatically with `python scripts/refresh_metadata.py`.
5. Regenerate the README and run the check:

   ```bash
   python scripts/build_readme.py
   ```

   ```bash
   python scripts/build_readme.py --check
   ```

6. Commit `papers.yaml` and `README.md` together and open a pull request.

## Field rules

| Field | Required | Format |
|---|---|---|
| `title` | yes | Exactly as on the arXiv or publisher page. |
| `authors` | yes | `First Author et al.` for three or more authors; both names for two. |
| `year` | yes | Year of the first public version (arXiv v1). |
| `date` | yes | Date of the first public version, quoted: `'YYYY-MM-DD'` (arXiv v1 date; `scripts/refresh_metadata.py` fills it in for arXiv papers). |
| `url` | yes | `https://arxiv.org/abs/XXXX.XXXXX` (no version suffix, no PDF link), or the publisher page. |
| `category` | yes | One of the `id`s under `categories:` in `papers.yaml`. |
| `note` | yes | One sentence in your own words on why the paper matters for weight-space programming, ending with a period, at most 300 characters. Do not copy the abstract. |
| `venue` | no | Short venue and year, such as `ICLR 2024`, `EMNLP 2023` or `TMLR`. Omit for preprints. |
| `code` | no | Official code repository URL. |
| `citations` | no | Semantic Scholar citation count. Don't edit it by hand: `scripts/refresh_metadata.py` sets it, and the daily maintenance run refreshes it. |

Entries are sorted automatically (newest first), so the position of an entry in `papers.yaml` does not matter. Never add a paper you have not checked on its arXiv or publisher page.

## Adding a category

Add an item under `categories:` with an `id`, a `group` (one of the `groups:` ids), a `title`, and a one-sentence `description`. Groups become top-level README sections and categories become their subsections, both in the order they are listed.
