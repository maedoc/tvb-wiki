#!/usr/bin/env python3
"""Audit raw/papers/*.md for uncited and off-mission papers."""

import glob
import json
import os
import re
import sys
from pathlib import Path

# Configuration
REPO_ROOT = Path("/home/duke/src/tvb-wiki")
RAW_PAPERS_DIR = REPO_ROOT / "raw" / "papers"
WIKI_DIRS = [
    REPO_ROOT / "entities",
    REPO_ROOT / "concepts",
    REPO_ROOT / "comparisons",
]
META_DIR = REPO_ROOT / "meta"
OUTPUT_JSON = META_DIR / "raw_paper_audit.json"

# TVB-relevant keywords (lowercased for case-insensitive matching)
KEYWORDS = [
    "connectivity", "network", "brain", "neuroimaging", "model", "simulation",
    "dynamics", "tvb", "neural mass", "whole-brain", "connectome", "tractography",
    "dti", "fmri", "eeg", "meg", "spiking", "oscillation", "bifurcation",
    "epilepsy", "stroke", "dementia", "alzheimer", "parkinson", "schizophrenia",
    "autism", "resting-state", "functional-connectivity", "structural-connectivity",
    "effective-connectivity", "graph-theory", "complexity", "entropy",
    "synchronization", "kuramoto", "jansen-rit", "wong-wang", "wilson-cowan",
    "hodgkin-huxley", "izhikevich", "mean-field", "neural field", "population dynamics",
    "brain simulation", "computational neuroscience", "theoretical neuroscience",
    "systems neuroscience",
]
KEYWORDS_SET = set(KEYWORDS)


def extract_frontmatter(text: str):
    """Extract YAML frontmatter and body from markdown text."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", text


def get_paper_slug(paper_path: Path) -> str:
    """Return the slug (filename without .md) for a paper."""
    return paper_path.stem


def get_paper_reference(slug: str) -> str:
    """Return the raw/papers/SLUG.md reference form used in citations."""
    return f"raw/papers/{slug}.md"


def extract_title_and_abstract(paper_path: Path):
    """Extract title from frontmatter and first 2000 chars of body."""
    text = paper_path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter(text)

    # Try to extract title from frontmatter
    title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # If no title in frontmatter, use first H1 from body
    if not title:
        h1_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        title = h1_match.group(1).strip() if h1_match else ""

    # Abstract = first 2000 chars of body
    abstract = body[:2000]

    return title, abstract


def build_citation_index():
    """Build a mapping from paper slug -> set of citing wiki page paths."""
    index = {}
    # Regex for inline citations: [[raw/papers/SLUG.md]] or [[raw/papers/SLUG.md|...]]
    inline_re = re.compile(r'\[\[raw/papers/([^\]|\s]+)\.md(?:\|[^\]]*)?\]\]')
    # Regex for frontmatter sources lines: - raw/papers/SLUG.md
    source_line_re = re.compile(r'^\s*-\s*raw/papers/([^\s]+)\.md\s*$', re.MULTILINE)

    for wiki_dir in WIKI_DIRS:
        if not wiki_dir.exists():
            continue
        for wiki_path in wiki_dir.glob("*.md"):
            text = wiki_path.read_text(encoding="utf-8")

            # Find frontmatter sources
            for m in source_line_re.finditer(text):
                slug = m.group(1)
                index.setdefault(slug, set()).add(str(wiki_path.relative_to(REPO_ROOT)))

            # Find inline citations
            for m in inline_re.finditer(text):
                slug = m.group(1)
                index.setdefault(slug, set()).add(str(wiki_path.relative_to(REPO_ROOT)))

    return index


def has_keyword_match(title: str, abstract: str) -> bool:
    """Check if title+abstract contains any TVB-relevant keyword."""
    combined = (title + " " + abstract).lower()
    for kw in KEYWORDS_SET:
        if kw in combined:
            return True
    return False


def main():
    papers = sorted(RAW_PAPERS_DIR.glob("*.md"))
    citation_index = build_citation_index()

    off_mission = []
    uncited = []
    cited = []

    for paper_path in papers:
        slug = get_paper_slug(paper_path)
        title, abstract = extract_title_and_abstract(paper_path)
        citing_pages = sorted(citation_index.get(slug, set()))
        is_cited = len(citing_pages) > 0
        is_on_mission = has_keyword_match(title, abstract)

        entry = {
            "slug": slug,
            "path": str(paper_path.relative_to(REPO_ROOT)),
            "title": title,
            "abstract_preview": abstract,
            "cited_by": citing_pages,
            "cited_count": len(citing_pages),
        }

        if not is_on_mission:
            off_mission.append(entry)
        elif not is_cited:
            uncited.append(entry)
        else:
            cited.append(entry)

    # --- stdout output ---
    def print_section(name, items):
        print(f"\n{name} ({len(items)})")
        print("=" * 60)
        for e in items:
            cite_info = f"  cited by {e['cited_count']} page(s)" if e['cited_count'] > 0 else "  not cited"
            print(f"  - {e['slug']}: {e['title']}{cite_info}")

    print_section("OFF-MISSION (delete candidates)", off_mission)
    print_section("UNCITED", uncited)
    print_section("CITED", cited)

    total = len(papers)
    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"  Total raw papers:    {total}")
    print(f"  Off-mission:         {len(off_mission)}")
    print(f"  Uncited:             {len(uncited)}")
    print(f"  Cited:               {len(cited)}")
    print(f"{'=' * 60}")

    # --- JSON report ---
    report = {
        "total_raw_papers": total,
        "off_mission_count": len(off_mission),
        "uncited_count": len(uncited),
        "cited_count": len(cited),
        "off_mission": off_mission,
        "uncited": uncited,
        "cited": cited,
    }

    META_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\nJSON report written to: {OUTPUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
