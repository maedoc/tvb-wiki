---
name: tvb-wiki-static-site
description: "Build and deploy the TVB research wiki as a static site using MkDocs and GitHub Pages."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [static-site, mkdocs, github-pages, deployment]
    category: devops
    related_skills: [automated-research-wiki, cronjob]
  pi:
    slash_commands: [/build-site, /deploy-wiki]
    agents: [engineer]
---

# TVB Wiki Static Site

Skill for building the TVB research wiki into a static website with MkDocs, deploying to GitHub Pages, and managing the deployment pipeline.

## When This Skill Activates

Use this skill when:
- You need to build the static site from the wiki source
- You want to deploy the site to GitHub Pages (or another hosting service)
- You are setting up a new static‑site generator for the wiki
- The user asks “build the wiki site” or “deploy the wiki”

## Prerequisites

- TVB wiki at `~/tvb‑wiki` (or `WIKI_PATH` environment variable)
- Python 3.11+ with MkDocs and Material theme installed (`pip install -r requirements.txt`)
- Git configured with SSH key for pushing to GitHub
- GitHub repository remote set (`origin` points to `git@github.com:maedoc/tvb‑wiki`)
- GitHub Pages enabled (Settings → Pages → Source: `gh‑pages` branch)

## Architecture

```
~/tvb‑wiki/
├── docs/                     # MkDocs source (synced from wiki)
├── site/                     # Built static site (output of `mkdocs build`)
├── mkdocs.yml               # MkDocs configuration
├── .github/workflows/deploy.yml # GitHub Actions workflow
└── scripts/
    ├── sync_to_docs.py      # Sync entities/concepts → docs/
    └── convert_wikilinks.py # Convert Obsidian [[links]] → relative links
```

The static‑site pipeline consists of three phases:

1. **Sync** – copy wiki source (`entities/`, `concepts/`, `index.md`) to `docs/`
2. **Convert** – transform wikilinks to standard Markdown links
3. **Build** – run `mkdocs build` to generate HTML in `site/`
4. **Deploy** – commit and push to GitHub, triggering GitHub Actions that deploys to `gh‑pages`

## Step‑by‑Step Build & Deploy

### 1. Sync Wiki to Docs

The sync script copies wiki pages to the MkDocs source directory, preserving directory structure:

```bash
cd ~/tvb‑wiki
python3 scripts/sync_to_docs.py
```

**What it does:**
- Copies `entities/*.md` → `docs/entities/`
- Copies `concepts/*.md` → `docs/concepts/`
- Copies `index.md`, `SCHEMA.md`, `about.md` → `docs/`
- Preserves frontmatter and content

### 2. Convert Wikilinks

Obsidian‑style `[[page]]` links are not understood by MkDocs. The conversion script transforms them to standard relative Markdown links:

```bash
python3 scripts/convert_wikilinks.py
```

**Conversion rules:**
- `[[page]]` → `[page](page.md)` (if target exists in same directory)
- `[[page|display]]` → `[display](page.md)`
- Normalizes dash‑like characters (`‑`, `–`, `—`, `U+2011`) to regular hyphens
- Converts spaces to hyphens, lowercases filenames
- Logs unknown link targets to `meta/lint.log`

### 3. Build Static Site

Build the site with MkDocs:

```bash
mkdocs build
```

Output is written to `site/`. Verify the build succeeded:

```bash
ls -la site/
cat site/index.html | head -5
```

### 4. Deploy via GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automatically rebuilds and deploys the site on every push to `main`. To trigger a deployment:

```bash
git add .
git commit -m "Build static site $(date '+%Y‑%m‑%d %H:%M')"
git push origin main
```

**Workflow steps:**
1. Checks out the repository
2. Installs Python dependencies
3. Runs `mkdocs build`
4. Deploys the `site/` directory to the `gh‑pages` branch using `peaceiris/actions‑gh‑pages`

**Manual deployment (without push):**
You can also run the workflow manually from the GitHub UI (Actions → “Deploy to GitHub Pages” → Run workflow).

### 5. Verify Deployment

Check the live site:

```bash
curl -I https://maedoc.github.io/tvb‑wiki/
```

Expected response: `HTTP/2 200`. If `404`, wait a few minutes for GitHub Pages propagation.

Check the GitHub Actions run status:

```bash
curl -s -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/maedoc/tvb‑wiki/actions/runs" | \
  jq '.workflow_runs[0] | {status, conclusion, html_url}'
```

## Configuration

### MkDocs Configuration (`mkdocs.yml`)

```yaml
site_name: TVB Research Wiki
site_description: A growing knowledge base for connectome‑based whole‑brain modeling.
theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
    - search.highlight
    - content.tabs.link
    - content.code.copy
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed
  - attr_list
  - def_list
  - footnotes
plugins:
  - search

nav:
  - Home: index.md
  - Entities: entities/index.md
  - Concepts: concepts/index.md
  - Comparisons: comparisons/index.md
  - Queries: queries/index.md
  - About: about.md
```

### GitHub Actions Workflow (`deploy.yml`)

See `.github/workflows/deploy.yml` in the repo for the exact steps.

## For Other Agents (Codex, Pi)

Agents that discover this skill can:

1. **Locate the scripts** – `sync_to_docs.py`, `convert_wikilinks.py`
2. **Run the build steps** – execute the commands above.
3. **Deploy** – commit and push to GitHub, or run the GitHub Actions workflow manually.
4. **Customize configuration** – modify `mkdocs.yml` or the workflow as needed.

### Skill Metadata for Discovery

This skill is listed in the repo’s `skill‑manifest.json`:

```json
{
  "name": "tvb‑wiki‑static‑site",
  "path": "skills/tvb‑wiki‑static‑site/SKILL.md",
  "description": "Build and deploy static site with MkDocs and GitHub Pages.",
  "entry_point": "mkdocs build",
  "dependencies": ["python3", "mkdocs", "git"],
  "schedule": "hourly (via full pipeline)"
}
```

## Pitfalls

- **Hyphen normalization mismatches** – Obsidian uses non‑breaking hyphens; the conversion script handles most, but manual pages may need adjustment. Check `meta/lint.log`.
- **GitHub Pages 404 after first deploy** – Wait 5‑10 minutes. Ensure the `gh‑pages` branch contains `index.html` and the Pages source is set correctly.
- **MkDocs 2.0 incompatibility** – Currently using MkDocs 1.6.x. Future upgrades may break plugins. Pin versions in `requirements.txt`.
- **Broken internal links** – After conversion, some `[[wikilinks]]` may remain as placeholders (e.g., in `SCHEMA.md`). These are flagged by the daily lint.
- **SSH key permissions** – Ensure the SSH key is added to GitHub account and the agent has permission to push to the repository.

## Verification

After building and deploying:

1. **Local build** – `site/index.html` exists and contains expected content.
2. **GitHub Actions run** – shows green checkmark.
3. `gh‑pages` **branch** – updated with latest `site/` contents.
4. **Live site** – returns HTTP 200 and displays the wiki.

Run a quick link check:

```bash
cd ~/tvb‑wiki
python3 -m mkdocs build --strict 2>&1 | grep -i error
```

## Related Skills

- `automated‑research‑wiki` – includes static‑site deployment as part of the full pipeline
- `cronjob` – scheduling regular builds
- `github‑pr‑workflow` – alternative deployment via pull request

## References

- MkDocs documentation: https://www.mkdocs.org
- Material for MkDocs: https://squidfunk.github.io/mkdocs-material/
- GitHub Pages action: https://github.com/peaceiris/actions‑gh‑pages
- TVB wiki live site: https://maedoc.github.io/tvb‑wiki/