# Skills for TVB Research Wiki

This directory contains **Hermes/Pi‑format skills** that enable AI agents to maintain, update, and deploy the TVB research wiki.

## Overview

The TVB wiki is a self‑growing knowledge base for connectome‑based whole‑brain modeling, with:

- **Hourly arXiv ingestion** – fetches new papers, extracts entities/concepts
- **Static site generation** – built with MkDocs + Material theme
- **GitHub Pages deployment** – automated via GitHub Actions
- **Daily linting** – health‑checks, broken‑link detection

These skills provide step‑by‑step instructions for agents (Hermes, Pi, Codex, etc.) to perform each part of the pipeline.

## Skill List

| Skill | Path | Description |
|-------|------|-------------|
| **tvb‑wiki‑maintenance** | `tvb‑wiki‑maintenance/SKILL.md` | Full pipeline: hourly ingestion → sync → convert → build → deploy |
| **tvb‑wiki‑ingestion** | `tvb‑wiki‑ingestion/SKILL.md` | arXiv paper fetching and entity extraction |
| **tvb‑wiki‑static‑site** | `tvb‑wiki‑static‑site/SKILL.md` | Build and deploy static site with MkDocs & GitHub Pages |

A machine‑readable manifest is available at [`../skill‑manifest.json`](../skill‑manifest.json).

## For Hermes Agent

Load a skill directly from this directory (if the repo is cloned locally):

```bash
skill_view('tvb‑wiki‑maintenance')
```

Or copy the skills to Hermes’ global skill directory:

```bash
cp -r tvb‑wiki-* ~/.hermes/skills/
```

Then load as usual:

```bash
skill_view('tvb‑wiki‑maintenance')
```

## For Pi / Feynman

Pi expects skills in a `skills/` directory with `SKILL.md` files. This repo follows that format.

If Pi is configured to look for skills in the current directory, it will discover these automatically.

Slash‑command mappings are defined in each skill’s YAML frontmatter under `metadata.pi.slash_commands`.

## For Codex / Other Agents

Agents that can read markdown files can parse the SKILL.md files and execute the described steps.

The `skill‑manifest.json` provides a programmatic index of available skills, their entry points, and dependencies.

## Skill Format

Each skill consists of:

- **YAML frontmatter** – name, description, version, tags, compatibility metadata
- **Markdown body** – step‑by‑step instructions, commands, pitfalls, verification
- **Related skills** – cross‑references to other skills in the bundle

Skills are designed to be **self‑contained** and **actionable** – an agent with the required dependencies can follow the steps to achieve the skill’s goal.

## Adding a New Skill

1. Create a new directory under `skills/` (e.g., `skills/tvb‑wiki‑new‑skill/`)
2. Write `SKILL.md` with YAML frontmatter and detailed instructions
3. Update `skill‑manifest.json` to include the new skill
4. Optionally add supporting files (scripts, templates, references) in the skill directory

Follow the existing skills as templates.

## Dependencies

All skills assume the TVB wiki repository is cloned at `~/tvb‑wiki` (or the `WIKI_PATH` environment variable is set). Required system dependencies:

- Python 3.11+
- Git
- MkDocs (`pip install mkdocs mkdocs‑material`)
- GitHub CLI (optional)

See individual skills for specific dependencies.

## License

These skills are released under the MIT License (same as the TVB wiki repository).