#!/usr/bin/env python3
"""
Ralph Improver Agent — picks worst pages, improves them via writer-reviewer pipeline.
Writer: ollama/kimi-k2.6 (local, fast)
Reviewer: zai/glm-5.1 (cloud, different training)

Runs N pages in parallel through pi subshells.
"""
import os
import sys
import re
import json
import datetime
import time
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    RAW_PAPERS_DIR, SCHEMA_PATH, append_log, git_commit,
    get_all_pages, read_page, save_page, load_frontmatter,
    word_count, has_placeholder, get_sources,
    run_pi, WRITER_MODEL, REVIEWER_MODEL,
    PARALLEL_WRITERS, PARALLEL_REVIEWERS,
)

log = get_logger("Improver")


# ── Page scoring ───────────────────────────────────────────────────────

def score_page(filepath: str) -> tuple[float, dict]:
    """
    Score a page by quality. Lower = needs more work.
    Returns (score, info_dict).
    """
    try:
        metadata, content = read_page(filepath)
    except Exception as e:
        return 0.0, {'error': str(e), 'path': filepath}

    info = {
        'path': filepath,
        'words': word_count(content),
        'has_placeholder': has_placeholder(content),
        'sources': len(get_sources(metadata)),
        'wikilinks': len(re.findall(r'\[\[([^\]]+)\]\]', content)),
        'updated': metadata.get('updated', ''),
        'type': metadata.get('type', ''),
        'title': metadata.get('title', os.path.basename(filepath)[:-3]),
    }

    score = 100.0

    # Placeholder text = critical
    if info['has_placeholder']:
        score -= 60

    # Too short
    if info['words'] < 200:
        score -= 30
    elif info['words'] < 500:
        score -= 10

    # No sources/refs
    if info['sources'] == 0:
        score -= 20
    elif info['sources'] < 2:
        score -= 5

    # No wikilinks
    if info['wikilinks'] == 0:
        score -= 15
    elif info['wikilinks'] < 3:
        score -= 5

    # Stale (not updated in 30+ days)
    try:
        updated = datetime.datetime.strptime(info['updated'], '%Y-%m-%d')
        days_old = (datetime.datetime.now() - updated).days
        if days_old > 60:
            score -= 15
        elif days_old > 30:
            score -= 5
    except (ValueError, TypeError):
        score -= 5  # No date = unknown = slight penalty

    info['score'] = max(0, score)
    return info['score'], info


def build_priority_queue(n: int = None) -> list[dict]:
    """Build priority queue of pages needing improvement, worst first."""
    pages = get_all_pages()
    scored = []

    for slug, filepath in pages.items():
        score, info = score_page(filepath)
        if score < 80:  # Only include pages that need work
            info['slug'] = slug
            scored.append(info)

    scored.sort(key=lambda x: x['score'])

    if n:
        return scored[:n]
    return scored


# ── Writer ─────────────────────────────────────────────────────────────

def build_writer_prompt(filepath: str) -> str:
    """Build the prompt for the writer to improve a page."""
    slug = os.path.basename(filepath)[:-3]

    # Read current page
    try:
        metadata, content = read_page(filepath)
    except Exception:
        metadata, content = {}, ""

    # Read relevant raw papers
    sources = get_sources(metadata)
    source_texts = []
    for source in sources[:3]:  # Limit to 3 most relevant
        source_path = os.path.join(WIKI_ROOT, source) if not os.path.isabs(source) else source
        if os.path.exists(source_path):
            try:
                with open(source_path, 'r', encoding='utf-8') as f:
                    src_content = f.read()[:2000]  # Truncate long papers
                source_texts.append(f"--- SOURCE: {source} ---\n{src_content}")
            except Exception:
                pass

    sources_block = '\n\n'.join(source_texts) if source_texts else "(No source papers available — use general knowledge)"

    # Read schema
    schema = ""
    if os.path.exists(SCHEMA_PATH):
        with open(SCHEMA_PATH, 'r') as f:
            schema = f.read()

    prompt = f"""You are the Ralph Writer agent improving a TVB Wiki page. Follow the schema strictly.

## SCHEMA
{schema}

## YOUR TASK
Improve the wiki page: {slug}

## CURRENT PAGE CONTENT
{content}

## AVAILABLE SOURCE PAPERS
{sources_block}

## INSTRUCTIONS
1. Replace ALL placeholder text (*Placeholder*) with real, sourced content
2. Add wikilinks [[like-this]] to related pages (minimum 3)
3. Add factual claims ONLY if you can cite a source
4. Keep the YAML frontmatter, but update the `updated:` date to today ({datetime.date.today().isoformat()})
5. Add any new sources used to the `sources:` frontmatter list
6. Aim for 400-800 words for a full page
7. Use clear section headings (##)
8. For concept pages: include a definition, role in modeling, related concepts
9. For entity pages: include overview, key features, related software/people

Write the COMPLETE updated page (including frontmatter). Output ONLY the markdown file content, no commentary."""
    return prompt


def build_reviewer_prompt(filepath: str, original_content: str, edited_content: str) -> str:
    """Build the prompt for the reviewer to check an edit."""
    prompt = f"""You are the Ralph Reviewer agent checking a wiki edit for quality.

## TASK
Review the proposed edit to: {os.path.basename(filepath)}

## ORIGINAL
{original_content[:3000]}

## PROPOSED EDIT
{edited_content[:5000]}

## REVIEW CHECKLIST
Answer each of these:
1. Are all new factual claims supported by cited sources? (PASS/FAIL)
2. Are there any factual errors or dubious claims? (PASS/FAIL)
3. Is the writing quality sufficient for a Scholarpedia-level wiki? (PASS/FAIL)
4. Do all wikilinks [[like-this]] look plausible for a TVB/whole-brain wiki? (PASS/FAIL)
5. Was placeholder text fully replaced? (PASS/FAIL)
6. Is there anything important missing that should be added? (NOTE or OK)

## OUTPUT FORMAT
Reply with ONLY:
VERDICT: PASS or VERDICT: NEEDS_REVISION
If NEEDS_REVISION, explain what needs to be fixed."""
    return prompt


# ── Validation ─────────────────────────────────────────────────────────

def validate_edit(filepath: str, new_content: str, original_content: str) -> tuple[bool, list[str]]:
    """
    Validate an edit. Returns (is_valid, list_of_issues).
    """
    issues = []

    # Check it has frontmatter
    if not new_content.strip().startswith('---'):
        issues.append("Missing YAML frontmatter")

    # Check no new placeholders introduced
    if has_placeholder(new_content) and not has_placeholder(original_content):
        issues.append("New placeholder text introduced")

    # Count wikilinks
    old_links = set(re.findall(r'\[\[([^\]]+)\]\]', original_content))
    new_links = set(re.findall(r'\[\[([^\]]+)\]\]', new_content))

    # Check wikilinks point to existing pages
    all_pages = get_all_pages()
    for link in new_links:
        target = link.split('|')[0].strip().lower().replace(' ', '-')
        if target not in all_pages and target not in {'tvb', 'nest', 'neuron', 'brian'}:
            # Allow common ones that might exist under slightly different names
            pass  # We'll let the LLM's judgment stand for now

    # Check word count isn't drastically lower
    old_wc = word_count(original_content)
    new_wc = word_count(new_content)
    if old_wc > 100 and new_wc < old_wc * 0.5:
        issues.append(f"Word count dropped significantly: {old_wc} → {new_wc}")

    # Check updated date is recent
    updated_match = re.search(r'updated:\s*(\d{4}-\d{2}-\d{2})', new_content)
    if updated_match:
        try:
            updated = datetime.datetime.strptime(updated_match.group(1), '%Y-%m-%d')
            if (datetime.datetime.now() - updated).days > 1:
                issues.append("Updated date not set to today")
        except ValueError:
            issues.append("Invalid updated date format")

    return len(issues) == 0, issues


# ── Improve a single page ─────────────────────────────────────────────

def improve_page(filepath: str) -> tuple[bool, str]:
    """
    Improve one page through writer → reviewer pipeline.
    Returns (success, description).
    """
    slug = os.path.basename(filepath)[:-3]

    # Read original
    try:
        metadata, original = read_page(filepath)
    except Exception as e:
        return False, f"Could not read {slug}: {e}"

    info_str = f"{word_count(original)} words, {len(get_sources(metadata))} refs"
    if has_placeholder(original):
        info_str += ", HAS PLACEHOLDER"

    log.info("Improving %s (%s)", slug, info_str)

    # Step 1: Writer improves the page
    writer_prompt = build_writer_prompt(filepath)
    success, output = run_pi(writer_prompt, model=WRITER_MODEL)

    if not success:
        return False, f"Writer failed for {slug}: {output[:100]}"

    # Extract the markdown content from pi output
    # pi may wrap in code blocks or add commentary
    new_content = output
    # Strip code fences if present
    if new_content.startswith('```'):
        lines = new_content.split('\n')
        # Remove first and last lines if they're code fences
        if lines[0].startswith('```'):
            lines = lines[1:]
        if lines and lines[-1].strip() == '```':
            lines = lines[:-1]
        new_content = '\n'.join(lines)

    # Step 2: Reviewer checks the edit
    reviewer_prompt = build_reviewer_prompt(filepath, original, new_content)
    review_success, review_output = run_pi(
        reviewer_prompt, model=REVIEWER_MODEL, tools="read"
    )

    needs_revision = False
    if review_success:
        verdict = review_output.strip().lower()
        if 'needs_revision' in verdict or 'fail' in verdict:
            needs_revision = True
            log.info("Reviewer flagged issues for %s: %s", slug, review_output[:100])
        else:
            log.info("Reviewer approved %s", slug)
    else:
        log.warn("Reviewer failed for %s, accepting writer output", slug)

    # Step 3: Revise if needed
    if needs_revision:
        revision_prompt = f"""You are the Ralph Writer. Your edit to {slug} was flagged for issues.
Fix these issues and return the complete updated page (including frontmatter).

ISSUES FLAGGED BY REVIEWER:
{review_output}

YOUR PREVIOUS EDIT (which needs fixes):
{new_content}

Fix the issues and output ONLY the corrected markdown file."""
        rev_success, rev_output = run_pi(revision_prompt, model=WRITER_MODEL)
        if rev_success:
            new_content = rev_output
            # Strip code fences again
            if new_content.startswith('```'):
                lines = new_content.split('\n')
                if lines[0].startswith('```'):
                    lines = lines[1:]
                if lines and lines[-1].strip() == '```':
                    lines = lines[:-1]
                new_content = '\n'.join(lines)
            log.info("Revised %s after reviewer feedback", slug)

    # Step 4: Validate
    valid, issues = validate_edit(filepath, new_content, original)
    if not valid:
        log.warn("Validation failed for %s: %s", slug, '; '.join(issues))
        return False, f"Validation failed for {slug}: {'; '.join(issues)}"

    # Step 5: Write the improved page
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, f"Improved {slug} ({word_count(new_content)} words)"


# ── Main improver cycle ───────────────────────────────────────────────

def run_improver_cycle(n_pages: int = None):
    """
    Run one improver cycle. Improves N pages in parallel.
    Returns (pages_improved, pages_failed).
    """
    n_pages = n_pages or PARALLEL_WRITERS
    log.info("Starting hourly cycle")

    # Build priority queue
    queue = build_priority_queue()
    log.info("Scoring %d pages, %d need improvement (score < 80)",
             len(get_all_pages()), len(queue))

    if not queue:
        log.info("Cycle complete. All pages look good!")
        return 0, 0

    # Pick worst N pages
    targets = queue[:n_pages]
    for t in targets:
        log.info("  %s (score=%.0f, %d words, %d refs%s)",
                 t['slug'], t['score'], t['words'], t['sources'],
                 ', PLACEHOLDER' if t['has_placeholder'] else '')

    # Improve pages in parallel
    improved = 0
    failed = 0
    results = []

    with ThreadPoolExecutor(max_workers=n_pages) as pool:
        futures = {
            pool.submit(improve_page, t['path']): t
            for t in targets
        }
        for future in as_completed(futures):
            target = futures[future]
            try:
                success, desc = future.result()
                results.append((target['slug'], success, desc))
                if success:
                    improved += 1
                else:
                    failed += 1
            except Exception as e:
                log.error("Exception improving %s: %s", target['slug'], e)
                failed += 1

    # Git commit improved pages
    if improved > 0:
        slugs = [r[0] for r in results if r[1]]
        msg = f"Improve: {', '.join(slugs)} (Writer:{WRITER_MODEL} Reviewer:{REVIEWER_MODEL}) (Improver)"
        git_commit(msg)
        append_log(f"Improve: {improved} pages improved ({', '.join(slugs)})")
        log.info("Committed: \"%s\"", msg)

    log.info("Cycle complete. %d improved, %d failed.", improved, failed)
    return improved, failed


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Ralph Improver Agent")
    parser.add_argument("-n", type=int, default=PARALLEL_WRITERS,
                        help=f"Number of pages to improve in parallel (default: {PARALLEL_WRITERS})")
    args = parser.parse_args()
    run_improver_cycle(args.n)
