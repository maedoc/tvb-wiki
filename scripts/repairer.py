#!/usr/bin/env python3
"""
Ralph Repairer Agent — fixes structural issues found by the Auditor.
Uses cheap model (gpt-oss-120b) for text-level fixes;
pure Python for mechanical ones.

Repairable categories:
  Layer 0 (no LLM):  missing_from_index, broken_source_refs, missing_frontmatter,
                      duplicate_references (delegated to RefFormatter),
                      opaque_references (delegated to RefFormatter),
                      missing_inline_crosslinks (delegated to CrosslinkApplier)
  Layer 1 (LLM):     broken_wikilinks
  Layer 2 (stretch): orphan_pages (add backlinks from related pages)

Skipped (not repairable without domain knowledge):
  placeholder_pages    → Improver handles these
  pages_no_sources     → needs real research
  stale_pages          → stale ≠ broken
  cross_ref_asymmetry  → too noisy, false positives
"""
import os
import sys
import re
import json
import datetime
import copy
from collections import defaultdict

import frontmatter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    RAW_PAPERS_DIR, CATALOG_PATH, META_DIR, AUDIT_REPORT_FILE, SCHEMA_PATH,
    REPAIRER_MODEL, append_log, git_commit, run_pi,
    get_all_pages, read_page, save_page, load_frontmatter,
    word_count, has_placeholder, get_sources,
)

log = get_logger("Repairer")


# ── Constants ──────────────────────────────────────────────────────────

REQUIRED_FRONTMATTER = ['title', 'created', 'updated', 'type', 'tags']

# Wikilinks that are too generic to add backlinks for (in orphan repair)
SKIP_ORPHAN_SLUGS = {'root', 'index'}

# Maximum LLM calls per cycle (safety cap)
MAX_LLM_CALLS = 50


# ── Helpers ────────────────────────────────────────────────────────────

def _load_report() -> dict | None:
    """Load the latest audit report, or None if missing/empty."""
    if not os.path.exists(AUDIT_REPORT_FILE):
        log.warn("No audit report found at %s", AUDIT_REPORT_FILE)
        return None
    try:
        with open(AUDIT_REPORT_FILE, 'r', encoding='utf-8') as f:
            report = json.load(f)
        if not report:
            log.warn("Audit report is empty")
            return None
        return report
    except Exception as e:
        log.error("Failed to load audit report: %s", e)
        return None


def _slug_from_path(filepath: str) -> str:
    return os.path.basename(filepath).replace('.md', '')


def _read_raw(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def _write_raw(filepath: str, content: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def _validate_repair(filepath: str, original: str, edited: str) -> tuple[bool, list[str]]:
    """
    Lightweight validation for repairs.
    Returns (is_valid, list_of_issues).
    """
    issues = []

    # Must still have frontmatter
    if not edited.strip().startswith('---'):
        issues.append("Lost frontmatter")

    # Must not introduce placeholders
    if has_placeholder(edited) and not has_placeholder(original):
        issues.append("Introduced placeholders")

    # Word count must not drop >40%
    old_wc = word_count(original)
    new_wc = word_count(edited)
    if old_wc > 50 and new_wc < old_wc * 0.6:
        issues.append(f"Word count dropped too much: {old_wc} -> {new_wc}")

    # Must still have at least as many wikilinks (unless we intentionally removed broken ones)
    old_links = re.findall(r'\[\[([^\]]+)\]\]', original)
    new_links = re.findall(r'\[\[([^\]]+)\]\]', edited)
    if len(new_links) < len(old_links) - 10:  # allow removal of up to 10 broken links
        issues.append(f"Too many wikilinks removed: {len(old_links)} -> {len(new_links)}")

    return len(issues) == 0, issues


# ── Layer 0: Pure Python fixes (no LLM) ───────────────────────────────

def fix_broken_source_refs(report: dict) -> int:
    """Remove source paths that point to non-existent files."""
    items = report.get('broken_source_refs', [])
    if not items:
        return 0

    log.info("Layer 0: fixing %d broken source refs", len(items))

    # Group by filepath so we fix each file once
    by_file = defaultdict(list)
    for item in items:
        by_file[item['path']].append(item['broken_source'])

    fixed = 0
    for filepath, broken_sources in by_file.items():
        try:
            raw = _read_raw(filepath)
            post = frontmatter.loads(raw)
            sources = post.metadata.get('sources', [])

            if isinstance(sources, str):
                sources = [s.strip() for s in sources.split(',') if s.strip()]

            original_len = len(sources)
            # Remove broken entries
            new_sources = [
                s for s in sources
                if (s if isinstance(s, str) else str(s)) not in broken_sources
            ]

            if len(new_sources) < original_len:
                post.metadata['sources'] = new_sources
                _write_raw(filepath, frontmatter.dumps(post))
                removed = original_len - len(new_sources)
                fixed += removed
                log.info("  Removed %d broken source ref(s) from %s", removed, _slug_from_path(filepath))
        except Exception as e:
            log.warn("  Failed to fix sources in %s: %s", filepath, e)

    return fixed


def fix_missing_from_index(report: dict) -> int:
    """Append pages not listed in catalog.md under the correct section."""
    items = report.get('missing_from_index', [])
    if not items:
        return 0

    log.info("Layer 0: adding %d pages to catalog.md", len(items))

    if not os.path.exists(CATALOG_PATH):
        log.warn("catalog.md not found at %s", CATALOG_PATH)
        return 0

    # Determine section for each page based on directory
    entities = set()
    concepts = set()
    comparisons = set()

    for item in items:
        slug = item['slug']
        filepath = item.get('path', '')
        if ENTITIES_DIR in filepath:
            entities.add(slug)
        elif CONCEPTS_DIR in filepath:
            concepts.add(slug)
        elif COMPARISONS_DIR in filepath:
            comparisons.add(slug)
        else:
            # Default to entities
            entities.add(slug)

    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        index_content = f.read()

    added = 0

    # Add each section's missing pages
    for section_label, slugs in [
        ("## Entities", entities),
        ("## Concepts", concepts),
        ("## Comparisons", comparisons),
    ]:
        if not slugs:
            continue

        # Find the section in index.md
        # Look for common section header patterns
        patterns = [
            re.compile(rf'^{re.escape(section_label)}', re.MULTILINE | re.IGNORECASE),
            re.compile(rf'^###?\s+{re.escape(section_label.lstrip("# "))}', re.MULTILINE | re.IGNORECASE),
        ]

        section_match = None
        for pattern in patterns:
            section_match = pattern.search(index_content)
            if section_match:
                break

        if not section_match:
            log.warn("  Could not find section '%s' in catalog.md, skipping %d pages",
                     section_label, len(slugs))
            continue

        # Find the next section header after this one
        rest = index_content[section_match.end():]
        next_section = re.search(r'^##\s', rest, re.MULTILINE)
        if next_section:
            insert_pos = section_match.end() + next_section.start()
        else:
            insert_pos = len(index_content)

        # Build lines to insert
        lines = ""
        for slug in sorted(slugs):
            # Check it's not already there somehow
            if f'[[{slug}' in index_content:
                continue
            # Determine the page type for the link text
            title = slug.replace('-', ' ').title()
            lines += f"- [[{slug}|{title}]]\n"
            added += 1

        if lines:
            index_content = index_content[:insert_pos].rstrip('\n') + '\n' + lines + index_content[insert_pos:]

    if added > 0:
        with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
            f.write(index_content)
        log.info("  Added %d pages to catalog.md", added)

    return added


def fix_missing_frontmatter(report: dict) -> int:
    """Inject missing required frontmatter fields with sensible defaults."""
    items = report.get('missing_frontmatter', [])
    if not items:
        return 0

    log.info("Layer 0: fixing frontmatter for %d pages", len(items))

    fixed = 0
    today = datetime.date.today().isoformat()

    for item in items:
        filepath = item['path']
        missing = item.get('missing_fields', [])
        slug = _slug_from_path(filepath)

        try:
            raw = _read_raw(filepath)
            post = frontmatter.loads(raw)

            for field in missing:
                if field == 'title':
                    post.metadata['title'] = slug.replace('-', ' ').title()
                elif field == 'created':
                    post.metadata['created'] = today
                elif field == 'updated':
                    post.metadata['updated'] = today
                elif field == 'type':
                    if ENTITIES_DIR in filepath:
                        post.metadata['type'] = 'entity'
                    elif CONCEPTS_DIR in filepath:
                        post.metadata['type'] = 'concept'
                    elif COMPARISONS_DIR in filepath:
                        post.metadata['type'] = 'comparison'
                    else:
                        post.metadata['type'] = 'entity'
                elif field == 'tags':
                    post.metadata['tags'] = []

            _write_raw(filepath, frontmatter.dumps(post))
            fixed += 1
            log.info("  Fixed frontmatter for %s (added: %s)", slug, ', '.join(missing))
        except Exception as e:
            log.warn("  Failed to fix frontmatter for %s: %s", slug, e)

    return fixed


# ── Layer 1: LLM-assisted fixes ───────────────────────────────────────

def _find_closest_page(target: str, all_pages: dict, max_results: int = 3) -> list[str]:
    """Find pages with similar slugs to a broken link target."""
    candidates = []
    target_lower = target.lower().replace('-', ' ')

    for slug in all_pages:
        slug_lower = slug.lower().replace('-', ' ')
        # Exact prefix/suffix match
        if slug_lower.startswith(target_lower[:5]) or slug_lower.endswith(target_lower[-5:]):
            candidates.append((slug, 1))
        # Substring match
        elif target_lower in slug_lower or slug_lower in target_lower:
            candidates.append((slug, 2))
        # Shared words
        elif len(set(target_lower.split()) & set(slug_lower.split())) > 0:
            candidates.append((slug, 3))

    candidates.sort(key=lambda x: x[1])
    return [c[0] for c in candidates[:max_results]]


def fix_broken_wikilinks(report: dict, all_pages: dict) -> int:
    """
    LLM-assisted: fix typos in wikilinks or remove broken ones.
    Batches all broken links per source page into a single LLM call.
    """
    items = report.get('broken_wikilinks', [])
    if not items:
        return 0

    log.info("Layer 1: fixing %d broken wikilinks across pages", len(items))

    # Group by source page
    by_source = defaultdict(list)
    for item in items:
        by_source[item['source']].append(item['target'])

    fixed = 0
    llm_calls = 0

    for source_slug, broken_targets in by_source.items():
        if llm_calls >= MAX_LLM_CALLS:
            log.warn("Hit max LLM call limit (%d), stopping", MAX_LLM_CALLS)
            break

        filepath = all_pages.get(source_slug)
        if not filepath or not os.path.exists(filepath):
            log.warn("  Source page not found: %s", source_slug)
            continue

        # Find candidate matches for each broken target
        target_hints = {}
        for target in broken_targets:
            closest = _find_closest_page(target, all_pages)
            target_hints[target] = closest

        # Build the prompt
        raw = _read_raw(filepath)

        broken_list = '\n'.join(
            f"  - [[{t}]]" + (f"  → possible fix: [[{target_hints[t][0]}]]" if target_hints[t] else "  → no close match, should be removed")
            for t in broken_targets
        )

        prompt = f"""You are a wiki repair bot. Fix the broken wikilinks in this page.

## FILE: {source_slug}

## BROKEN LINKS (these targets do not exist as pages):
{broken_list}

## RULES
- If a broken link has a clear typo (e.g., "epileptorrs" → "epileptor"), fix it using the suggested replacement
- If there is no close match, REMOVE the wikilink syntax but keep the surrounding text (replace [[bad-link]] with just the display text)
- If the link used display text like [[target|Display Text]], keep "Display Text" as plain text when removing
- Do NOT change anything else in the page — only fix the broken links listed above
- Keep ALL frontmatter exactly as-is, except bump the `updated:` date to {datetime.date.today().isoformat()}
- Output the COMPLETE corrected page including frontmatter

Output ONLY the corrected markdown file content, no commentary."""

        success, output = run_pi(prompt, model=REPAIRER_MODEL)

        if not success:
            log.warn("  LLM failed for %s: %s", source_slug, output[:100])
            continue

        llm_calls += 1

        # Strip code fences if present
        new_content = output
        if new_content.strip().startswith('```'):
            lines = new_content.split('\n')
            if lines[0].strip().startswith('```'):
                lines = lines[1:]
            if lines and lines[-1].strip() == '```':
                lines = lines[:-1]
            new_content = '\n'.join(lines)

        # Validate
        valid, issues = _validate_repair(filepath, raw, new_content)
        if not valid:
            log.warn("  Validation failed for %s: %s", source_slug, '; '.join(issues))
            continue

        # Apply
        _write_raw(filepath, new_content)
        fixed += len(broken_targets)
        log.info("  Fixed %d broken link(s) in %s", len(broken_targets), source_slug)

    log.info("  LLM calls used: %d", llm_calls)
    return fixed


# ── Layer 2: Stretch goal — orphan pages ──────────────────────────────

def fix_orphan_pages(report: dict, all_pages: dict) -> int:
    """
    LLM-assisted: find a natural place to add a backlink to orphan pages.
    Only attempts a small batch per cycle (max 10) to limit cost.
    """
    orphans = report.get('orphan_pages', [])
    if not orphans:
        return 0

    # Filter out trivial pages and limit batch size
    orphans = [s for s in orphans if s not in SKIP_ORPHAN_SLUGS and s in all_pages]
    batch = orphans[:10]

    log.info("Layer 2: attempting backlinks for %d orphan pages (of %d total)",
             len(batch), len(orphans))

    # Build a page -> outbound links map for context
    link_map = {}
    for slug, filepath in all_pages.items():
        try:
            content = _read_raw(filepath)
            targets = set(re.findall(r'\[\[([^\]]+)\]\]', content))
            # Normalize
            targets = {t.split('|')[0].strip().lower().replace(' ', '-') for t in targets}
            link_map[slug] = targets
        except Exception:
            link_map[slug] = set()

    fixed = 0
    llm_calls = 0

    for orphan_slug in batch:
        if llm_calls >= MAX_LLM_CALLS:
            break

        orphan_path = all_pages[orphan_slug]
        if not os.path.exists(orphan_path):
            continue

        # Read orphan page to understand its topic
        try:
            orphan_raw = _read_raw(orphan_path)
        except Exception:
            continue

        # Find pages that this orphan links to — those are candidates for adding a backlink
        orphan_targets = link_map.get(orphan_slug, set())

        # Find the best candidate: a page that the orphan links to but doesn't link back
        candidates = []
        for target in orphan_targets:
            if target in all_pages and target != orphan_slug:
                target_links = link_map.get(target, set())
                if orphan_slug not in target_links:
                    candidates.append(target)

        if not candidates:
            continue

        # Pick the first candidate (most natural — the orphan already references it)
        candidate_slug = candidates[0]
        candidate_path = all_pages[candidate_slug]
        candidate_raw = _read_raw(candidate_path)

        prompt = f"""You are a wiki repair bot. Add a natural backlink to [[{orphan_slug}]] in the page below.

## CONTEXT
The page [[{orphan_slug}]] links to [[{candidate_slug}]] but [[{candidate_slug}]] does not link back.
This makes [[{orphan_slug}]] an "orphan" page with no inbound links.

## YOUR TASK
Add ONE natural wikilink [[{orphan_slug}]] somewhere in the page content below.
Place it where it makes contextual sense — in a relevant paragraph or "See also" section.
If the page doesn't naturally relate to [[{orphan_slug}]], output the page UNCHANGED.

## RULES
- Add ONLY the wikilink [[{orphan_slug}]], do not add other content
- If it doesn't fit naturally, leave the page unchanged
- Keep ALL frontmatter exactly as-is, except bump `updated:` to {datetime.date.today().isoformat()}
- Output the COMPLETE page including frontmatter
- If you made no changes, output the page exactly as provided

Output ONLY the markdown file content, no commentary."""

        # Include the candidate page content + a snippet of the orphan for context
        orphan_snippet = orphan_raw[:500]
        full_prompt = prompt + f"\n\n## PAGE TO EDIT ({candidate_slug})\n{candidate_raw}\n\n## ORPHAN PAGE CONTEXT ({orphan_slug})\n{orphan_snippet}"

        success, output = run_pi(full_prompt, model=REPAIRER_MODEL)

        if not success:
            continue

        llm_calls += 1

        new_content = output
        if new_content.strip().startswith('```'):
            lines = new_content.split('\n')
            if lines[0].strip().startswith('```'):
                lines = lines[1:]
            if lines and lines[-1].strip() == '```':
                lines = lines[:-1]
            new_content = '\n'.join(lines)

        # Validate
        valid, issues = _validate_repair(candidate_path, candidate_raw, new_content)
        if not valid:
            log.warn("  Validation failed adding backlink to %s from %s: %s",
                     orphan_slug, candidate_slug, '; '.join(issues))
            continue

        # Check that the backlink was actually added
        if f'[[{orphan_slug}' not in new_content:
            log.info("  LLM chose not to add backlink to %s from %s (no natural fit)", orphan_slug, candidate_slug)
            continue

        _write_raw(candidate_path, new_content)
        fixed += 1
        log.info("  Added backlink to %s from %s", orphan_slug, candidate_slug)

    log.info("  LLM calls used: %d", llm_calls)
    return fixed


# ── Main repair cycle ─────────────────────────────────────────────────

def run_repairer_cycle() -> dict:
    """
    Main entry point. Reads audit report, runs all fixers.
    Returns a stats dict.
    """
    log.info("Starting repair cycle")

    report = _load_report()
    if report is None:
        log.warn("No audit report available — skipping repair cycle")
        return {'error': 'no audit report'}

    all_pages = get_all_pages()
    stats = {
        'timestamp': datetime.datetime.now().isoformat(),
        'audit_timestamp': report.get('timestamp', 'unknown'),
        'total_issues_in_report': (
            len(report.get('broken_wikilinks', [])) +
            len(report.get('orphan_pages', [])) +
            len(report.get('placeholder_pages', [])) +
            len(report.get('pages_no_sources', [])) +
            len(report.get('stale_pages', [])) +
            len(report.get('broken_source_refs', [])) +
            len(report.get('missing_frontmatter', [])) +
            len(report.get('missing_from_index', []))
        ),
    }

    log.info("Audit report: %s — %d total issues",
             stats['audit_timestamp'], stats['total_issues_in_report'])

    # ── Layer 0: Pure Python fixes ─────────────────────────────────────
    log.info("── Layer 0: Mechanical fixes (no LLM) ──")

    stats['fixed_broken_source_refs'] = fix_broken_source_refs(report)
    log.info("  broken_source_refs fixed: %d", stats['fixed_broken_source_refs'])

    stats['fixed_missing_from_index'] = fix_missing_from_index(report)
    log.info("  missing_from_index fixed: %d", stats['fixed_missing_from_index'])

    stats['fixed_missing_frontmatter'] = fix_missing_frontmatter(report)
    log.info("  missing_frontmatter fixed: %d", stats['fixed_missing_frontmatter'])

    # ── Layer 1: LLM-assisted broken wikilink fixes ────────────────────
    log.info("── Layer 1: LLM-assisted fixes ──")

    stats['fixed_broken_wikilinks'] = fix_broken_wikilinks(report, all_pages)
    log.info("  broken_wikilinks fixed: %d", stats['fixed_broken_wikilinks'])

    # ── Layer 2: Stretch — orphan pages ────────────────────────────────
    log.info("── Layer 2: Stretch fixes ──")

    stats['fixed_orphan_pages'] = fix_orphan_pages(report, all_pages)
    log.info("  orphan_pages fixed: %d", stats['fixed_orphan_pages'])

    # ── Layer 3: Quality fixes via specialist agents ────────────────────
    log.info("── Layer 3: Quality fixes (delegated to RefFormatter / CrosslinkApplier) ──")

    stats['fixed_duplicate_refs'] = 0
    stats['fixed_opaque_refs'] = 0
    stats['fixed_missing_crosslinks'] = 0

    # Delegate reference formatting to RefFormatter for flagged pages
    dup_refs = report.get('duplicate_references', [])
    opaque_refs = report.get('opaque_references', [])
    if dup_refs or opaque_refs:
        try:
            from ref_formatter import format_page_references
            slugs_to_fix = set()
            for item in dup_refs:
                slugs_to_fix.add(item['slug'])
            for item in opaque_refs:
                slugs_to_fix.add(item['slug'])
            for fix_slug in slugs_to_fix:
                if fix_slug in all_pages:
                    changed, desc = format_page_references(all_pages[fix_slug])
                    if changed:
                        if any(d['slug'] == fix_slug for d in dup_refs):
                            stats['fixed_duplicate_refs'] += 1
                        if any(o['slug'] == fix_slug for o in opaque_refs):
                            stats['fixed_opaque_refs'] += 1
                        log.info("  Fixed refs: %s", desc)
        except Exception as e:
            log.warn("  RefFormatter delegation failed: %s", e)

    # Delegate inline crosslinking to CrosslinkApplier for flagged pages
    missing_links = report.get('missing_inline_crosslinks', [])
    if missing_links:
        try:
            from crosslink_applier import build_term_map, apply_inline_crosslinks
            term_map = build_term_map(all_pages)
            all_slugs = set(all_pages.keys())
            for item in missing_links[:20]:  # cap at 20 per cycle
                fix_slug = item['slug']
                if fix_slug in all_pages:
                    changed, count = apply_inline_crosslinks(
                        all_pages[fix_slug], term_map, all_slugs
                    )
                    if changed:
                        stats['fixed_missing_crosslinks'] += count
                        log.info("  Fixed crosslinks: %s (+%d)", fix_slug, count)
        except Exception as e:
            log.warn("  CrosslinkApplier delegation failed: %s", e)

    log.info("  duplicate_refs fixed: %d", stats['fixed_duplicate_refs'])
    log.info("  opaque_refs fixed: %d", stats['fixed_opaque_refs'])
    log.info("  missing_crosslinks fixed: %d", stats['fixed_missing_crosslinks'])

    # ── Summary & commit ───────────────────────────────────────────────
    total_fixed = (
        stats.get('fixed_broken_source_refs', 0) +
        stats.get('fixed_missing_from_index', 0) +
        stats.get('fixed_missing_frontmatter', 0) +
        stats.get('fixed_broken_wikilinks', 0) +
        stats.get('fixed_orphan_pages', 0) +
        stats.get('fixed_duplicate_refs', 0) +
        stats.get('fixed_opaque_refs', 0) +
        stats.get('fixed_missing_crosslinks', 0)
    )
    stats['total_fixed'] = total_fixed

    if total_fixed > 0:
        git_commit(
            f"Repair: {total_fixed} issues fixed — "
            f"{stats.get('fixed_broken_source_refs', 0)} source refs, "
            f"{stats.get('fixed_missing_from_index', 0)} index entries, "
            f"{stats.get('fixed_missing_frontmatter', 0)} frontmatter, "
            f"{stats.get('fixed_broken_wikilinks', 0)} wikilinks, "
            f"{stats.get('fixed_orphan_pages', 0)} orphans, "
            f"{stats.get('fixed_duplicate_refs', 0)} dup-refs, "
            f"{stats.get('fixed_opaque_refs', 0)} opaque-refs, "
            f"{stats.get('fixed_missing_crosslinks', 0)} crosslinks "
            f"(Repairer)"
        )
        append_log(
            f"Repair: {total_fixed} issues fixed "
            f"({stats.get('fixed_broken_source_refs', 0)} source refs, "
            f"{stats.get('fixed_missing_from_index', 0)} index, "
            f"{stats.get('fixed_missing_frontmatter', 0)} frontmatter, "
            f"{stats.get('fixed_broken_wikilinks', 0)} wikilinks, "
            f"{stats.get('fixed_orphan_pages', 0)} orphans, "
            f"{stats.get('fixed_duplicate_refs', 0)} dup-refs, "
            f"{stats.get('fixed_opaque_refs', 0)} opaque-refs, "
            f"{stats.get('fixed_missing_crosslinks', 0)} crosslinks)"
        )
        log.info("Committed %d fixes", total_fixed)
    else:
        log.info("No fixes applied — nothing to commit")

    log.info("Cycle complete. Fixed %d of %d total issues.", total_fixed, stats['total_issues_in_report'])

    # Save repair stats
    stats_file = os.path.join(META_DIR, 'repair_stats.json')
    os.makedirs(META_DIR, exist_ok=True)
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    return stats


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Ralph Repairer Agent")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be fixed without making changes")
    parser.add_argument("--layer", type=int, choices=[0, 1, 2],
                        help="Only run a specific layer (0=mechanical, 1=LLM wikilinks, 2=LLM orphans)")
    args = parser.parse_args()

    if args.dry_run:
        report = _load_report()
        if report:
            all_pages = get_all_pages()
            print(f"Audit report: {report.get('timestamp')}")
            print(f"  broken_source_refs: {len(report.get('broken_source_refs', []))}")
            print(f"  missing_from_index: {len(report.get('missing_from_index', []))}")
            print(f"  missing_frontmatter: {len(report.get('missing_frontmatter', []))}")
            print(f"  broken_wikilinks: {len(report.get('broken_wikilinks', []))}")
            print(f"  orphan_pages: {len(report.get('orphan_pages', []))}")
        else:
            print("No audit report found.")
    else:
        run_repairer_cycle()
