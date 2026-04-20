---
name: tvb-wiki-maintenance
description: "Full pipeline for maintaining the TVB research wiki: hourly arXiv ingestion, static site build, git commit, and GitHub Pages deployment."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wiki, automation, research, arxiv, static-site, github-pages]
    category: research
    related_skills: [automated-research-wiki, llm-wiki, cronjob]
  pi:
    slash_commands: [/update-wiki, /hourly-pipeline]
    agents: [researcher, engineer]
---

# TVB Wiki Maintenance

Complete guide to updating the TVB research wiki (`~/tvb‑wiki`) and deploying the static site. This skill describes the hourly pipeline that fetches new arXiv papers, syncs the wiki to MkDocs, builds the static site, commits changes, and pushes to GitHub for automatic deployment via GitHub Pages.

## When This Skill Activates

Use this skill when:
- You need to run the hourly update pipeline for the TVB wiki
- You want to manually trigger a full wiki refresh (fetch, sync, build, deploy)
- You are setting up a new agent to maintain this wiki
- The user asks "update the wiki" or "run the hourly pipeline"

## Prerequisites

- The TVB wiki repo cloned at `~/tvb‑wiki` (or set `WIKI_PATH` environment variable)
- Python 3.11+ with dependencies installed (`pip install -r requirements.txt`)
- Git configured with SSH key for pushing to GitHub
- GitHub repository remote set (`origin` points to `git@github.com:maedoc/tvb‑wiki`)
- GitHub Actions workflow enabled (deploys to `gh‑pages` branch)

## Architecture

```
~/tvb‑wiki/
├── scripts/
│   ├── hourly_update.py      # Fetches arXiv papers, ingests into raw/
│   ├── sync_to_docs.py       # Syncs entities/concepts to docs/
│   ├── convert_wikilinks.py  # Converts Obsidian [[links]] to relative Markdown
│   ├── hourly_full.py        # Full pipeline: update → sync → convert → build → git
│   └── daily_lint.py         # Lint script (run at 3 AM UTC)
├── docs/                     # MkDocs source (auto‑synced)
├── site/                     # Built static site (MkDocs output)
├── .github/workflows/deploy.yml # GitHub Actions deploy to Pages
└── mkdocs.yml               # MkDocs configuration
```

Two cron jobs are already active:
- **Hourly pipeline** (`0 * * * *`) – runs `scripts/hourly_full.py`
- **Daily lint** (`0 3 * * *`) – runs `scripts/daily_lint.py`

## Step‑by‑Step Pipeline

### 1. Run the Hourly Full Pipeline

The main script `hourly_full.py` orchestrates everything:

```bash
cd ~/tvb‑wiki
python3 scripts/hourly_full.py
```

What it does:
1. **Fetch new arXiv papers** – queries arXiv for connectome‑based whole‑brain modeling, neural mass models, TVB, etc. (see `hourly_update.py`).
2. **Save raw papers** – writes new papers to `raw/papers/arxiv-*.md`.
3. **Update entity/concept counts** – updates `meta/entity_counts.json`.
4. **Sync to docs/** – copies `entities/*.md`, `concepts/*.md`, `index.md`, etc. to `docs/`.
5. **Convert wikilinks** – transforms Obsidian‑style `[[page]]` links to standard Markdown relative links, normalizing hyphens.
6. **Build static site** – runs `mkdocs build`, output to `site/`.
7. **Commit changes** – if there are modifications, commits with message “Hourly update YYYY‑MM‑DD HH:MM”.
8. **Push to GitHub** – pushes the `main` branch to `origin`. This triggers the GitHub Actions workflow that rebuilds and deploys to `gh‑pages`.

### 2. Manual Trigger (One‑off Update)

If you need to run the pipeline manually (outside the cron schedule), use the same command. You can also run individual steps:

```bash
# Just fetch new papers
python3 scripts/hourly_update.py

# Sync and convert wikilinks
python3 scripts/sync_to_docs.py
python3 scripts/convert_wikilinks.py

# Build the site
mkdocs build

# Commit and push (if there are changes)
git add .
git commit -m "Manual update $(date '+%Y‑%m‑%d %H:%M')"
git push origin main
```

### 3. Verify Deployment

After pushing, check that GitHub Actions runs successfully:

```bash
# List recent workflow runs
curl -s -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/maedoc/tvb‑wiki/actions/runs" | jq '.workflow_runs[0] | {status, conclusion, created_at}'
```

The site is live at **https://maedoc.github.io/tvb‑wiki/**.

### 4. Daily Lint

The lint script runs automatically at 3 AM UTC. To run it manually:

```bash
cd ~/tvb‑wiki
python3 scripts/daily_lint.py
```

It checks:
- Broken internal links
- Orphan pages (no inbound links)
- Missing frontmatter
- Stale content (papers older than 2 years)
- Hyphen normalization mismatches

Results are logged to `meta/lint.log`.

## For Other Agents (Codex, Pi)

Agents that discover this skill in the git repo can:

1. **Locate skills** – look in `skills/` directory for `SKILL.md` files.
2. **Read the skill** – parse YAML frontmatter and markdown instructions.
3. **Execute the pipeline** – run the commands listed above.
4. **Adapt to their environment** – adjust paths if the repo is cloned elsewhere.

### Skill Discovery Pattern

This repo includes a `skill‑manifest.json` at the root that lists available skills:

```json
{
  "skills": [
    {
      "name": "tvb‑wiki‑maintenance",
      "path": "skills/tvb‑wiki‑maintenance/SKILL.md",
      "description": "Full pipeline for maintaining the TVB research wiki.",
      "entry_point": "scripts/hourly_full.py",
      "dependencies": ["python3", "git", "mkdocs"]
    },
    {
      "name": "tvb‑wiki‑ingestion",
      "path": "skills/tvb‑wiki‑ingestion/SKILL.md",
      "description": "arXiv paper ingestion and entity/concept extraction.",
      "entry_point": "scripts/hourly_update.py"
    },
    {
      "name": "tvb‑wiki‑static‑site",
      "path": "skills/tvb‑wiki‑static‑site/SKILL.md",
      "description": "Build and deploy static site with MkDocs and GitHub Pages.",
      "entry_point": "mkdocs build"
    }
  ]
}
```

Agents can read this manifest to know which skills are available and how to invoke them.

## Pitfalls

- **GitHub Pages 404 after first deploy** – can take 5‑10 minutes for the site to become live.
- **Hyphen normalization** – Obsidian inserts non‑breaking hyphens (`U+2011`); the conversion script normalizes them, but mismatches can cause broken links. Check `meta/lint.log`.
- **SSH host key verification** – if `known_hosts` is missing, use `GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no" git push`.
- **MkDocs 2.0 incompatibility** – currently using MkDocs 1.6.x; future upgrades may break plugins.
- **Rate limiting** – arXiv API allows only 1 request per second; the script includes delays.

## Verification

After running the pipeline, verify:

- New papers appear in `raw/papers/`
- `docs/` directory is updated
- `site/` contains fresh HTML
- GitHub Actions run succeeds (green checkmark)
- Live site returns HTTP 200 (not 404)

## Related Skills

- `automated‑research‑wiki` – generic pattern for self‑updating research wikis
- `llm‑wiki` – core wiki‑building skill
- `cronjob` – scheduling recurring tasks in Hermes

## References

- TVB wiki repo: https://github.com/maedoc/tvb‑wiki
- Live site: https://maedoc.github.io/tvb‑wiki/
- arXiv API: https://arxiv.org/help/api/user‑manual
- MkDocs documentation: https://www.mkdocs.org