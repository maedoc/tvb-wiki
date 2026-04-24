#!/usr/bin/env python3
"""
Ralph Auditor Agent — daily structural integrity check.
Python-only, no LLM needed.

Checks: broken wikilinks, orphan pages, placeholders, missing refs,
        stale pages, broken source refs, inconsistent frontmatter,
        missing from index, cross-reference asymmetry.
"""
import os
import sys
import re
import json
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    RAW_PAPERS_DIR, CATALOG_PATH, META_DIR, AUDIT_REPORT_FILE,
    append_log, git_commit, get_all_pages, get_all_wikilinks,
    word_count, has_placeholder, get_sources, load_frontmatter,
    read_page,
)

log = get_logger("Auditor")


def find_broken_wikilinks(links, pages) -> list[dict]:
    """Find links pointing to non-existent pages."""
    broken = []
    for target, source in links:
        if target not in pages:
            broken.append({'target': target, 'source': source})
    return broken


def find_orphan_pages(links, pages) -> list[str]:
    """Find pages with no inbound links."""
    linked = {target for target, _ in links}
    return sorted(pages - linked)


def find_placeholder_pages() -> list[dict]:
    """Find pages still containing placeholder text."""
    results = []
    all_pages = get_all_pages()
    for slug, filepath in all_pages.items():
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if has_placeholder(content):
                count = content.count('*Placeholder')
                results.append({'slug': slug, 'placeholders': count, 'path': filepath})
        except Exception:
            pass
    return results


def find_pages_no_sources() -> list[dict]:
    """Find pages with no sources/references."""
    results = []
    all_pages = get_all_pages()
    for slug, filepath in all_pages.items():
        metadata = load_frontmatter(filepath)
        sources = get_sources(metadata)
        if not sources:
            results.append({'slug': slug, 'path': filepath})
    return results


def find_stale_pages(days: int = 60) -> list[dict]:
    """Find pages not updated in N+ days."""
    results = []
    all_pages = get_all_pages()
    cutoff = datetime.datetime.now() - datetime.timedelta(days=days)

    for slug, filepath in all_pages.items():
        metadata = load_frontmatter(filepath)
        updated = metadata.get('updated', '')
        try:
            updated_dt = datetime.datetime.strptime(updated, '%Y-%m-%d')
            if updated_dt < cutoff:
                days_old = (datetime.datetime.now() - updated_dt).days
                results.append({'slug': slug, 'days_old': days_old, 'path': filepath})
        except (ValueError, TypeError):
            results.append({'slug': slug, 'days_old': -1, 'path': filepath,
                            'note': 'missing or invalid date'})

    results.sort(key=lambda x: x['days_old'], reverse=True)
    return results


def find_broken_source_refs() -> list[dict]:
    """Find pages whose sources: point to non-existent raw papers."""
    results = []
    all_pages = get_all_pages()

    for slug, filepath in all_pages.items():
        metadata = load_frontmatter(filepath)
        sources = get_sources(metadata)

        for source in sources:
            if not isinstance(source, str):
                continue
            source_path = os.path.join(WIKI_ROOT, source) if not os.path.isabs(source) else source
            if not os.path.exists(source_path):
                results.append({
                    'slug': slug,
                    'broken_source': source,
                    'path': filepath
                })

    return results


def find_missing_frontmatter() -> list[dict]:
    """Find pages with missing or incomplete frontmatter."""
    required = ['title', 'created', 'updated', 'type', 'tags']
    results = []
    all_pages = get_all_pages()

    for slug, filepath in all_pages.items():
        metadata = load_frontmatter(filepath)
        missing = [f for f in required if f not in metadata or not metadata[f]]
        if missing:
            results.append({'slug': slug, 'missing_fields': missing, 'path': filepath})

    return results


def find_pages_missing_from_index() -> list[dict]:
    """Find pages not listed in catalog.md."""
    if not os.path.exists(CATALOG_PATH):
        return [{'note': 'catalog.md not found'}]

    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        index_content = f.read()

    index_links = set()
    for match in re.findall(r'\[\[([^\]]+)\]\]', index_content):
        target = match.split('|')[0].strip().lower().replace(' ', '-').replace('\u2011', '-')
        index_links.add(target)

    results = []
    all_pages = get_all_pages()
    for slug in all_pages:
        if slug not in index_links:
            results.append({'slug': slug, 'path': all_pages[slug]})

    return results


def find_cross_reference_asymmetry() -> list[dict]:
    """Find pages where A links to B but B doesn't mention A."""
    # Build forward link map
    forward = {}  # slug -> set of targets
    all_pages = get_all_pages()

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

    # Find asymmetric links
    asymmetric = []
    for slug, targets in forward.items():
        for target in targets:
            if target in forward and slug not in forward[target]:
                # Don't flag raw papers (they're immutable)
                if not target.startswith('arxiv-') and not target.startswith('pubmed-'):
                    asymmetric.append({
                        'from': slug,
                        'to': target,
                        'note': f'{slug} links to {target} but not vice versa'
                    })

    return asymmetric


# ── Quality checks (new) ───────────────────────────────────────────

def find_duplicate_references_sections() -> list[dict]:
    """Find pages with more than one ## References / ## Sources / ## Bibliography heading."""
    results = []
    ref_pattern = re.compile(r'^##\s+(References?|Sources?|Bibliography)\s*$', re.MULTILINE | re.IGNORECASE)
    all_pages = get_all_pages()

    for slug, filepath in all_pages.items():
        try:
            metadata, content = read_page(filepath)
            matches = ref_pattern.findall(content)
            if len(matches) > 1:
                results.append({
                    'slug': slug,
                    'count': len(matches),
                    'headings': matches,
                    'path': filepath,
                })
        except Exception:
            pass
    return results


def find_opaque_references() -> list[dict]:
    """Find pages whose body references contain raw slugs like arxiv-2509.02799."""
    opaque_pattern = re.compile(
        r'(?:^|\n)\s*[-*\d.)]+\s+(.*(?:arxiv-\d{4}\.\d{4,}|semanticscholar-[a-f0-9]+|pubmed-\d+|raw/papers/).*)',
        re.IGNORECASE
    )
    results = []
    all_pages = get_all_pages()

    for slug, filepath in all_pages.items():
        try:
            metadata, content = read_page(filepath)
            matches = opaque_pattern.findall(content)
            if matches:
                results.append({
                    'slug': slug,
                    'opaque_count': len(matches),
                    'samples': matches[:5],
                    'path': filepath,
                })
        except Exception:
            pass
    return results


def find_thin_narrative_pages() -> list[dict]:
    """Find pages where the first content section has very little prose."""
    results = []
    all_pages = get_all_pages()

    for slug, filepath in all_pages.items():
        try:
            metadata, content = read_page(filepath)

            # Find the first ## section and count its prose
            lines = content.split('\n')
            first_section_lines = []
            found_first = False
            for line in lines:
                if line.startswith('## ') and not line.startswith('### '):
                    if found_first:
                        break  # hit next section
                    found_first = True
                    continue
                if found_first:
                    first_section_lines.append(line)

            if not found_first:
                continue

            section_text = '\n'.join(first_section_lines).strip()
            # Strip tables and code
            section_text = re.sub(r'\|.*\|', '', section_text)
            section_text = re.sub(r'```[\s\S]*?```', '', section_text)
            section_text = re.sub(r'`[^`]+`', '', section_text)
            prose_words = len(section_text.split())

            page_type = metadata.get('type', '')
            # Concept pages should have substantial intro prose
            if page_type == 'concept' and prose_words < 50:
                results.append({
                    'slug': slug,
                    'first_section_words': prose_words,
                    'page_words': word_count(content),
                    'path': filepath,
                    'note': 'first section has <50 words of prose',
                })
        except Exception:
            pass
    return results


def find_missing_inline_crosslinks() -> list[dict]:
    """Find pages that mention existing page titles as plain text without [[wikilinks]]."""
    # Build set of searchable terms from page slugs/titles
    all_pages = get_all_pages()
    # Simple slug-based matching: look for slug-as-words (hyphens→spaces)
    # Only check a curated set of high-value terms to avoid noise
    key_terms = {
        'mean-field': 'mean-field-theory',
        'mean field': 'mean-field-theory',
        'integrate-and-fire': 'spiking-neural-networks',
        'integrate and fire': 'spiking-neural-networks',
        'neural mass': 'neural-mass-models',
        'Wilson-Cowan': 'wilson-cowan',
        'Jansen-Rit': 'jansen-rit',
        'Epileptor': 'epileptor',
        'Wong-Wang': 'wong-wang',
        'Larter-Breakspear': 'larter-breakspear',
        'Stefanescu-Jirsa': 'stefanescu-jirsa',
        'Zerlaut': 'zerlaut',
        'functional connectivity': 'functional-connectivity',
        'structural connectivity': 'structural-connectivity',
        'effective connectivity': 'effective-connectivity',
        'bifurcation': 'bifurcation-analysis',
        'resting-state': 'resting-state',
        'resting state': 'resting-state',
        'whole-brain': 'whole-brain-modeling',
        'connectome': 'connectome',
        'connectomics': 'connectomics',
        'BOLD': 'bold-signal',
        'dynamic causal modeling': 'dynamic-causal-modeling',
        'forward model': 'forward-model',
        'graph theory': 'network-dynamics',
        'tractography': 'tractography',
        'source localization': 'source-localization',
        'parcellation': 'parcellation',
    }

    results = []
    for slug, filepath in all_pages.items():
        try:
            metadata, content = read_page(filepath)
            # Strip frontmatter, code blocks, existing wikilinks
            check_text = re.sub(r'```[\s\S]*?```', '', content)
            check_text = re.sub(r'\[\[[^\]]+\]\]', '', check_text)

            missing = []
            for term, target in key_terms.items():
                if target == slug:
                    continue  # don't link to self
                if re.search(r'\b' + re.escape(term) + r'\b', check_text, re.IGNORECASE):
                    missing.append((term, target))

            if missing:
                results.append({
                    'slug': slug,
                    'missing_links': missing[:10],
                    'count': len(missing),
                    'path': filepath,
                })
        except Exception:
            pass
    return results


# ── Main audit cycle ──────────────────────────────────────────────────

def run_auditor_cycle():
    """Run one full audit cycle. Returns the report dict."""
    log.info("Starting daily cycle")

    # Gather data
    links, pages = get_all_wikilinks()
    log.info("Scanning %d pages with %d wikilinks", len(pages), len(links))

    # Run all checks
    report = {
        'timestamp': datetime.datetime.now().isoformat(),
        'total_pages': len(pages),
        'total_wikilinks': len(links),
        'broken_wikilinks': find_broken_wikilinks(links, pages),
        'orphan_pages': find_orphan_pages(links, pages),
        'placeholder_pages': find_placeholder_pages(),
        'pages_no_sources': find_pages_no_sources(),
        'stale_pages': find_stale_pages(),
        'broken_source_refs': find_broken_source_refs(),
        'missing_frontmatter': find_missing_frontmatter(),
        'missing_from_index': find_pages_missing_from_index(),
        'cross_ref_asymmetry': find_cross_reference_asymmetry(),
        'duplicate_references': find_duplicate_references_sections(),
        'opaque_references': find_opaque_references(),
        'thin_narrative': find_thin_narrative_pages(),
        'missing_inline_crosslinks': find_missing_inline_crosslinks(),
    }

    # Summary
    total_issues = (
        len(report['broken_wikilinks']) +
        len(report['orphan_pages']) +
        len(report['placeholder_pages']) +
        len(report['pages_no_sources']) +
        len(report['stale_pages']) +
        len(report['broken_source_refs']) +
        len(report['missing_frontmatter']) +
        len(report['missing_from_index']) +
        len(report['duplicate_references']) +
        len(report['opaque_references']) +
        len(report['thin_narrative']) +
        len(report['missing_inline_crosslinks'])
    )

    log.info("Broken wikilinks: %d", len(report['broken_wikilinks']))
    log.info("Orphan pages: %d", len(report['orphan_pages']))
    log.info("Placeholder pages: %d", len(report['placeholder_pages']))
    log.info("Pages with no sources: %d", len(report['pages_no_sources']))
    log.info("Stale pages (>60 days): %d", len(report['stale_pages']))
    log.info("Broken source refs: %d", len(report['broken_source_refs']))
    log.info("Missing frontmatter: %d", len(report['missing_frontmatter']))
    log.info("Missing from index: %d", len(report['missing_from_index']))
    log.info("Cross-ref asymmetries: %d", len(report['cross_ref_asymmetry']))
    log.info("Duplicate references sections: %d", len(report['duplicate_references']))
    log.info("Opaque references: %d", len(report['opaque_references']))
    log.info("Thin narrative pages: %d", len(report['thin_narrative']))
    log.info("Missing inline crosslinks: %d", len(report['missing_inline_crosslinks']))
    log.info("TOTAL ISSUES: %d", total_issues)

    # Save machine-readable report
    os.makedirs(META_DIR, exist_ok=True)
    with open(AUDIT_REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    log.info("Saved audit report to %s", AUDIT_REPORT_FILE)

    # Human-readable lint log
    lint_log_path = os.path.join(META_DIR, 'lint.log')
    with open(lint_log_path, 'a', encoding='utf-8') as f:
        f.write(f"\n## Audit {report['timestamp']}\n")
        f.write(f"Total pages: {report['total_pages']}\n")
        f.write(f"Broken wikilinks: {len(report['broken_wikilinks'])}\n")
        f.write(f"Orphan pages: {len(report['orphan_pages'])}\n")
        f.write(f"Placeholder pages: {len(report['placeholder_pages'])}\n")
        f.write(f"Pages no sources: {len(report['pages_no_sources'])}\n")
        f.write(f"Stale pages: {len(report['stale_pages'])}\n")
        f.write(f"Broken source refs: {len(report['broken_source_refs'])}\n")
        f.write(f"Missing frontmatter: {len(report['missing_frontmatter'])}\n")
        f.write(f"Missing from index: {len(report['missing_from_index'])}\n")
        f.write(f"Duplicate references sections: {len(report['duplicate_references'])}\n")
        f.write(f"Opaque references: {len(report['opaque_references'])}\n")
        f.write(f"Thin narrative pages: {len(report['thin_narrative'])}\n")
        f.write(f"Missing inline crosslinks: {len(report['missing_inline_crosslinks'])}\n")

        for item in report['broken_wikilinks'][:20]:
            f.write(f"  BROKEN: {item['source']} -> [[{item['target']}]]\n")
        for slug in report['orphan_pages'][:20]:
            f.write(f"  ORPHAN: [[{slug}]]\n")
        for item in report['placeholder_pages']:
            f.write(f"  PLACEHOLDER: {item['slug']} ({item['placeholders']} occurrences)\n")
        for item in report['duplicate_references']:
            f.write(f"  DUP_REFS: {item['slug']} ({item['count']} sections)\n")
        for item in report['opaque_references'][:20]:
            f.write(f"  OPAQUE_REF: {item['slug']} ({item['opaque_count']} opaque)\n")
        for item in report['thin_narrative'][:20]:
            f.write(f"  THIN: {item['slug']} ({item['first_section_words']} words intro prose)\n")
        for item in report['missing_inline_crosslinks'][:20]:
            f.write(f"  MISSING_LINKS: {item['slug']} ({item['count']} missed)\n")

    # Log to log.md
    append_log(f"Audit: {total_issues} issues ({len(report['broken_wikilinks'])} broken links, "
               f"{len(report['orphan_pages'])} orphans, {len(report['placeholder_pages'])} placeholders, "
               f"{len(report['duplicate_references'])} dup-refs, {len(report['opaque_references'])} opaque-refs, "
               f"{len(report['thin_narrative'])} thin, {len(report['missing_inline_crosslinks'])} missing-links)")

    # Git commit the report
    git_commit(f"Audit: {total_issues} issues — {len(report['broken_wikilinks'])} broken links, "
               f"{len(report['orphan_pages'])} orphans (Auditor)")

    log.info("Cycle complete.")
    return report


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    run_auditor_cycle()
