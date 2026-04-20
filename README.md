# TVB Wiki – Connectome‑Based Whole‑Brain Modeling

A growing knowledge base for computational neuroscience, focusing on connectome‑based whole‑brain modeling, neural mass models, neuroimaging modalities, and related software.

## Structure

- `raw/papers/` – arXiv papers as markdown (metadata + abstract)
- `raw/articles/` – other sources (bioRxiv, medRxiv, GitHub READMEs)
- `entities/` – pages for software, authors, labs, datasets
- `concepts/` – pages for methods, modalities, topics
- `comparisons/` – comparative analyses
- `queries/` – saved queries and search patterns
- `meta/` – internal state (entity counts, timestamps, lint logs)
- `scripts/` – Python scripts for automated updates and linting

## Automated Updates

The wiki is updated automatically via two cron jobs:

1. **Hourly research** (`scripts/hourly_update.py`) – fetches new papers from arXiv, updates entity/concept pages, rebuilds the index.
2. **Daily lint** (`scripts/daily_lint.py`) – checks for orphan pages and broken internal links.

Cron logs are saved to `~/.hermes/cron/output/`. The wiki's own log is at `log.md`.

## Usage

Open this directory as an Obsidian vault (set `OBSIDIAN_VAULT_PATH` to this path).

Browse `index.md` for a categorized list of all pages.

## Schema

The `SCHEMA.md` file defines the tag taxonomy used for categorizing pages.

## Adding Content Manually

1. Drop a new paper in `raw/papers/` as markdown.
2. Run the ingest script to update entity/concept pages.
3. Or just edit pages directly.

## Development

To extend the automation:

- Edit `scripts/hourly_update.py` to add new sources (bioRxiv, medRxiv, GitHub).
- Adjust entity extraction logic in the same script.
- Modify `SCHEMA.md` to refine the tag taxonomy.

## Credits

Built with Hermes Agent's `llm‑wiki` and `obsidian` skills.

## Static Site

This wiki is also a static site built with MkDocs + Material theme. The `site/` directory contains the generated HTML. A GitHub Actions workflow automatically deploys the site to GitHub Pages on every push to `main`.

Last seeded: 2026‑04‑20 with 122 arXiv papers.