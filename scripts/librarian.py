#!/usr/bin/env python3
"""
Ralph Librarian Agent — daily metadata and cross-reference maintenance.
Python-only, no LLM needed.

Tasks: regenerate index, rebuild link graph, score authority,
       ensure cross-link symmetry, tag consistency.
"""
import os
import sys
import re
import json
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    CATALOG_PATH, META_DIR, append_log, git_commit, get_all_pages,
    get_all_wikilinks, load_frontmatter, get_sources,
)

log = get_logger("Librarian")


# ── Index regeneration ────────────────────────────────────────────────

def extract_summary(filepath: str) -> str:
    """Extract a one-line summary from a page."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return "*needs summary*"

    # Skip frontmatter
    in_frontmatter = False
    body_lines = []
    for line in content.split('\n'):
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '*Placeholder*' in line or line.startswith('* [['):
            continue
        if line.startswith('Software tool') or line.startswith('Key concept'):
            continue
        if len(line) > 20:
            return line[:120] + ('...' if len(line) > 120 else '')

    return "*needs summary*"


def regenerate_catalog():
    """Regenerate catalog.md with current summaries."""
    log.info("Regenerating catalog.md")

    sections = {
        'Entities': ENTITIES_DIR,
        'Concepts': CONCEPTS_DIR,
        'Comparisons': COMPARISONS_DIR,
    }

    lines = [
        "# Complete Wiki Catalog",
        "",
        "> **For power users:** This is the complete alphabetical listing of all wiki pages.",
        "",
    ]

    today = datetime.date.today().isoformat()
    total = 0

    for section_name, directory in sections.items():
        if not os.path.isdir(directory):
            continue

        pages = []
        for fn in sorted(os.listdir(directory)):
            if fn.endswith('.md'):
                filepath = os.path.join(directory, fn)
                slug = fn[:-3]
                name = slug.replace('-', ' ').title()
                summary = extract_summary(filepath)
                pages.append((name, slug, summary))
                total += 1

        if pages:
            lines.append(f"\n## {section_name}")
            lines.append(f"<!-- {section_name.lower()} -->")
            for name, slug, summary in pages:
                lines.append(f"- [[{name}]] – {summary}")

    # Add header with count
    lines.insert(3, f"> Last updated: {today} | Total pages: {total}")
    lines.insert(4, "")

    content = '\n'.join(lines)
    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    log.info("Catalog updated: %d pages", total)
    return total


# ── Authority scoring ─────────────────────────────────────────────────

def compute_authority_scores() -> dict:
    """
    Score pages by authority = number of inbound links.
    Returns {slug: {'inbound': n, 'authority': float}}
    """
    links, pages = get_all_wikilinks()

    inbound_count = {slug: 0 for slug in pages}
    for target, source in links:
        if target in inbound_count:
            inbound_count[target] += 1

    max_inbound = max(inbound_count.values()) if inbound_count else 1

    authority = {}
    for slug, count in inbound_count.items():
        authority[slug] = {
            'inbound': count,
            'authority': round(count / max_inbound, 3) if max_inbound > 0 else 0.0
        }

    return authority


def save_authority_scores(authority: dict):
    """Save authority scores to meta/page_authority.json"""
    path = os.path.join(META_DIR, 'page_authority.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(authority, f, indent=2, sort_keys=True)

    # Log top 10
    top = sorted(authority.items(), key=lambda x: x[1]['inbound'], reverse=True)[:10]
    for slug, info in top:
        log.info("  Authority: %s = %.2f (%d inbound links)",
                 slug, info['authority'], info['inbound'])


# ── Cross-link symmetry check ────────────────────────────────────────

def check_symmetry() -> list[dict]:
    """
    Find asymmetric links: A links to B but B doesn't mention A.
    Returns list of suggestions (not auto-applied).
    """
    all_pages = get_all_pages()
    forward = {}  # slug -> set of targets

    for slug, filepath in all_pages.items():
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            targets = set()
            for match in re.findall(r'\[\[([^\]]+)\]\]', content):
                target = match.split('|')[0].strip().lower().replace(' ', '-')
                targets.add(target)
            forward[slug] = targets
        except Exception:
            forward[slug] = set()

    asymmetric = []
    for slug, targets in forward.items():
        for target in targets:
            if target in forward and slug not in forward[target]:
                # Skip raw papers (immutable) and pages with <2 inbound links
                if not target.startswith('arxiv-') and not target.startswith('pubmed-'):
                    asymmetric.append({
                        'from': slug,
                        'to': target,
                    })

    log.info("Cross-link asymmetries: %d (logged, not auto-fixed)", len(asymmetric))
    return asymmetric


# ── Main librarian cycle ──────────────────────────────────────────────

def run_librarian_cycle():
    """Run one librarian cycle."""
    log.info("Starting daily cycle")

    # 1. Regenerate catalog
    total_pages = regenerate_catalog()

    # 2. Compute authority scores
    log.info("Computing page authority scores...")
    authority = compute_authority_scores()
    save_authority_scores(authority)

    # 3. Check cross-link symmetry
    asymmetric = check_symmetry()

    # 4. Summary stats
    links, pages = get_all_wikilinks()
    log.info("Stats: %d pages, %d wikilinks, %d asymmetric links",
             len(pages), len(links), len(asymmetric))

    # 5. Git commit
    msg = f"Librarian: rebuilt catalog ({total_pages} pages), authority scores updated (Librarian)"
    git_commit(msg)
    append_log(f"Librarian: catalog rebuilt, {len(asymmetric)} asymmetric links noted")

    log.info("Cycle complete.")
    return {
        'total_pages': total_pages,
        'total_links': len(links),
        'asymmetric_links': len(asymmetric),
    }


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    run_librarian_cycle()
