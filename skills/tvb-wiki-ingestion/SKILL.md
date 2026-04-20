---
name: tvb-wiki-ingestion
description: "arXiv paper ingestion for the TVB research wiki: fetch new papers, extract entities/concepts, update raw/ and meta/."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wiki, ingestion, arxiv, research, entities]
    category: research
    related_skills: [arxiv, llm-wiki]
  pi:
    slash_commands: [/ingest-arxiv]
    agents: [researcher]
---

# TVB Wiki Ingestion

Skill for fetching new arXiv papers relevant to connectome‑based whole‑brain modeling, extracting software/concept/author mentions, and updating the wiki’s raw paper library and entity counts.

## When This Skill Activates

Use this skill when:
- You need to fetch the latest arXiv papers for the TVB wiki
- You want to update the raw paper library without running the full pipeline
- You are setting up a new ingestion source (bioRxiv, GitHub, etc.)
- The user asks “fetch new papers for the wiki” or “update the paper database”

## Prerequisites

- TVB wiki at `~/tvb‑wiki` (or `WIKI_PATH` environment variable)
- Python 3.11+ with `requests` and `xml.etree.ElementTree` (standard library)
- Network access to arXiv API (https://export.arxiv.org)

## Architecture

```
~/tvb‑wiki/
├── raw/papers/               # Raw paper markdown files (arxiv-*.md)
├── meta/entity_counts.json   # Counts of software/concept/author mentions
└── scripts/hourly_update.py  # Main ingestion script
```

The ingestion script (`hourly_update.py`) performs:

1. **Query arXiv** with domain‑specific search queries
2. **Filter duplicates** by arXiv ID
3. **Save new papers** as markdown in `raw/papers/`
4. **Extract entities** via keyword matching
5. **Update entity counts** in `meta/entity_counts.json`

## Step‑by‑Step Ingestion

### 1. Run the Ingestion Script

```bash
cd ~/tvb‑wiki
python3 scripts/hourly_update.py
```

**Output:** Prints number of new papers added, e.g., `Hourly update complete: 3 new papers`.

### 2. Inspect New Papers

List recently added raw papers:

```bash
ls -lt ~/tvb‑wiki/raw/papers/arxiv-*.md | head -5
```

View a raw paper:

```bash
cat ~/tvb‑wiki/raw/papers/arxiv-<ID>.md
```

### 3. Check Entity Counts

The script updates `meta/entity_counts.json` with mention counts. View current counts:

```bash
cat ~/tvb‑wiki/meta/entity_counts.json | jq .
```

Example structure:

```json
{
  "software": {
    "TVB": 42,
    "NEST": 18,
    "NEURON": 12
  },
  "concepts": {
    "neural mass model": 56,
    "fMRI": 89,
    "EEG": 67
  },
  "authors": {
    "John Doe": 5,
    "Jane Smith": 3
  }
}
```

### 4. Manual Ingestion with Custom Queries

If you need to ingest papers from other arXiv categories or with different keywords, you can modify the search queries inside `hourly_update.py` (function `fetch_arxiv_since`). Default queries:

```python
queries = [
    'cat:q-bio.NC+AND+all:connectome',
    'all:neural+mass+model',
    'all:dynamic+causal+modeling',
    'all:The+Virtual+Brain',
    'all:TVB',
    'all:whole+brain+model',
]
```

Add new queries, adjust `max_results`, or change the `since_date` threshold.

### 5. Add a New Ingestion Source (e.g., bioRxiv)

To extend beyond arXiv:

1. Create a new function `fetch_biorxiv_since()` that uses the bioRxiv RSS feed or API.
2. Merge results with arXiv papers.
3. Assign a `source: bioRxiv` field and save with filename prefix `biorxiv-`.
4. Update entity extraction accordingly.

See the `automated‑research‑wiki` skill for a multi‑source pattern.

## Entity Extraction Details

The current extraction uses simple keyword matching. Keywords are defined in `extract_entities`:

- **Software**: TVB, The Virtual Brain, NEST, NEURON, Brian, ANTs, SPM, FSL, FreeSurfer
- **Concepts**: neural mass model, dynamic causal modeling, Wilson‑Cowan, Jansen‑Rit, fMRI, EEG, MEG, DTI, functional connectivity, structural connectivity, effective connectivity, resting‑state, whole‑brain, connectomics, brain network

**Limitation:** Keyword matching may miss synonyms or paraphrases. For more robust extraction, consider using a lightweight NLP library (spaCy) or an LLM‑based extractor.

## Integration with Wiki Pages

Entity counts are used by the wiki’s page‑creation logic (in `hourly_full.py`). When a software/concept/author reaches a threshold (default: 2 mentions), a corresponding page is created in `entities/` or `concepts/`. This happens during the full pipeline, not during ingestion alone.

## For Other Agents (Codex, Pi)

Agents that discover this skill can:

1. **Locate the script** – `scripts/hourly_update.py`
2. **Run ingestion** – execute the Python script as described.
3. **Adapt to their environment** – set `WIKI_PATH` if the repo is elsewhere.
4. **Extend with new sources** – follow the pattern to add bioRxiv, GitHub, etc.

### Skill Metadata for Discovery

This skill is listed in the repo’s `skill‑manifest.json`:

```json
{
  "name": "tvb‑wiki‑ingestion",
  "path": "skills/tvb‑wiki‑ingestion/SKILL.md",
  "description": "arXiv paper ingestion and entity/concept extraction.",
  "entry_point": "scripts/hourly_update.py",
  "dependencies": ["python3"],
  "schedule": "hourly"
}
```

## Pitfalls

- **arXiv rate limits** – Polite usage: max 1 request per second. The script includes `time.sleep(1)` between queries.
- **Duplicate detection** – Based on arXiv ID (without version suffix). If a paper is revised (v2, v3), the new version will replace the old only if the filename matches exactly; currently, only the base ID is used, so revisions are ignored.
- **Network timeouts** – If arXiv API is unreachable, the script will fail silently (caught exception). Check network connectivity.
- **Keyword misses** – New software or concept terms may not be in the keyword list. Periodically review and update the keyword lists.

## Verification

After ingestion, verify:

- New `.md` files appear in `raw/papers/`
- `meta/entity_counts.json` has updated counts
- No errors in the script output

Run a quick count:

```bash
grep -c '^# ' ~/tvb‑wiki/raw/papers/arxiv-*.md
```

## Related Skills

- `arxiv` – General arXiv search and download skill
- `llm‑wiki` – Core wiki‑building skill
- `automated‑research‑wiki` – Full automation pattern

## References

- arXiv API user manual: https://arxiv.org/help/api/user‑manual
- TVB wiki repo: https://github.com/maedoc/tvb‑wiki