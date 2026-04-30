#!/usr/bin/env python3
"""
Create Paper Stub — Auto-generate raw/papers/*.md stubs from verified metadata.

Usage:
    from create_paper_stub import create_stub_from_metadata
    create_stub_from_metadata("raw/papers", {"title":"X", "authors":["A"], "year":2020, ...})

Or standalone:
    python scripts/create_paper_stub.py "Stochastic Methods" "C. W. Gardiner" 2009
"""
import os
import re
import json
from pathlib import Path

# Import our shared verifier
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from citation_verify import verify_title, verify_doi, _http_json


def slugify(s: str) -> str:
    """Create a filesystem-safe slug from a title string."""
    s = s.lower()
    s = re.sub(r"[^\w\s]+", " ", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    s = re.sub(r"-+", "-", s)
    return s[:80]


def build_bibtex(meta: dict) -> str:
    """Generate a clean BibTeX entry from metadata dict."""
    authors = meta.get("authors", [])
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(",")]
    year = str(meta.get("year", ""))
    title = meta.get("title", "Untitled")
    venue = meta.get("venue", "")
    doi = meta.get("doi", "")

    first_author_surname = (authors[0].split()[-1] if authors else "unknown").lower()
    key = f"{first_author_surname}{year}{title.split()[0].lower()}"
    key = re.sub(r"[^a-z0-9]", "", key)[:20]

    # Determine entry type
    venue_lower = venue.lower()
    if any(k in venue_lower for k in ["journal", "neuro", "physics", "proceedings", "transactions", "review"]):
        entry_type = "article"
    else:
        entry_type = "misc"

    lines = [f"@{entry_type}{{{key},"]
    lines.append(f'  title = {{{title}}},')
    if authors:
        lines.append(f'  author = {{"{" and ".join(authors)}"}},')
    if year:
        lines.append(f'  year = {{{year}}},')
    if entry_type == "article":
        lines.append(f'  journal = {{{venue}}},')
    else:
        lines.append(f'  howpublished = {{{venue}}},')
    if doi:
        lines.append(f'  doi = {{{doi}}},')
    lines.append('}')
    return "\n".join(lines)


def format_frontmatter(meta: dict) -> str:
    """Generate YAML frontmatter string."""
    authors = meta.get("authors", [])
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(",")]

    # Clean author strings for YAML
    yaml_authors = []
    for a in authors:
        if ':' in a or '#' in a or '\n' in a or '"' in a:
            yaml_authors.append(json.dumps(a))
        else:
            yaml_authors.append(a)

    # Clean title for YAML
    title = meta.get("title", "")
    if ':' in title or '\n' in title:
        title = json.dumps(title)

    lines = ["---"]
    lines.append(f"title: {title}")
    lines.append(f"created: {meta.get('created', '')}")
    lines.append(f"updated: {meta.get('updated', '')}")
    lines.append("type: source")
    lines.append("tags: []")
    if yaml_authors:
        lines.append("authors:")
        for a in yaml_authors:
            lines.append(f"  - {a}")
    else:
        lines.append("authors: []")
    if meta.get("year"):
        lines.append(f"year: {meta['year']}")
    if meta.get("venue"):
        v = meta["venue"]
        if ':' in v or '\n' in v:
            v = json.dumps(v)
        lines.append(f"venue: {v}")
    if meta.get("doi"):
        lines.append(f"doi: {meta['doi']}")
    bibtex = meta.get("bibtex", "") or build_bibtex(meta)
    lines.append("bibtex: |")
    for line in bibtex.split("\n"):
        lines.append(f"  {line}")
    lines.append("---")
    return "\n".join(lines)


def create_stub_from_metadata(raw_dir: str, meta: dict) -> str | None:
    """
    Create a raw paper stub from metadata dict.
    Returns the filepath of the created stub, or None.
    """
    doi = meta.get("doi", "")
    title = meta.get("title", "")
    authors = meta.get("authors", [])
    year = str(meta.get("year", ""))

    # Determine filename
    if doi:
        # Preferred: use DOI-based slug
        doi_slug = doi.replace("https://doi.org/", "").replace("http://doi.org/", "").replace("/", "-").replace(".", "-")
        filename = f"doi-{doi_slug}.md"
    else:
        # Fallback: author+year based slug
        surname = authors[0].split()[-1].lower() if authors else "unknown"
        filename = f"{surname}-{year}.md"

    filepath = os.path.join(raw_dir, filename)
    if os.path.exists(filepath):
        return filepath  # Already exists

    # Ensure date fields
    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")
    meta.setdefault("created", today)
    meta.setdefault("updated", today)
    meta.setdefault("bibtex", "")

    content = format_frontmatter(meta)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        f.write("\n\n## Summary\n")
        f.write("## Key Concepts\n")
        f.write("## Relevance to TVB\n")
        f.write("## Citation\n")
        f.write(f"```bibtex\n{build_bibtex(meta)}\n```\n")

    return filepath


def create_stub_from_citation(citation: dict, raw_dir: str = "raw/papers") -> str | None:
    """
    Auto-create a stub given a parsed inline citation dict.
    Looks up the paper in OpenAlex/CrossRef, then writes the stub.
    Returns filepath or None.
    """
    if citation.get("type") == "doi":
        meta = verify_doi(citation.get("doi", ""))
    elif citation.get("type") == "author_year":
        search_title = f"{citation.get('author', '')} {citation.get('year', '')}"
        meta = verify_title(search_title)
    else:
        return None

    if not meta:
        return None

    filepath = create_stub_from_metadata(raw_dir, meta)
    return filepath


# ── CLI ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Create a raw paper stub")
    parser.add_argument("title", help="Paper title")
    parser.add_argument("--authors", nargs="+", default=[], help="Author names")
    parser.add_argument("--year", default="", help="Publication year")
    parser.add_argument("--venue", default="", help="Venue or journal")
    parser.add_argument("--doi", default="", help="DOI")
    parser.add_argument("--raw-dir", default="raw/papers", help="Output directory")
    args = parser.parse_args()

    meta = {
        "title": args.title,
        "authors": args.authors,
        "year": args.year,
        "venue": args.venue,
        "doi": args.doi,
    }
    fp = create_stub_from_metadata(args.raw_dir, meta)
    if fp:
        print(f"Created stub: {fp}")
    else:
        print("Stub already exists.")
