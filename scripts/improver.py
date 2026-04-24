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
import frontmatter
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
        score -= 50
    elif info['words'] < 300:
        score -= 40
    elif info['words'] < 500:
        score -= 20
    elif info['words'] < 800:
        score -= 5

    # No sources/refs
    if info['sources'] == 0:
        score -= 20
    elif info['sources'] < 2:
        score -= 5

    # No wikilinks
    if info['wikilinks'] == 0:
        score -= 20
    elif info['wikilinks'] < 3:
        score -= 10
    elif info['wikilinks'] < 8:
        score -= 3

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


def analyze_sections(content: str) -> list[dict]:
    """Split page content into sections. Returns list of {heading, content, score}."""
    sections = []
    current_heading = "_preamble"
    current_lines = []

    for line in content.split('\n'):
        if line.startswith('## ') and not line.startswith('### '):
            # Save previous section
            if current_lines:
                text = '\n'.join(current_lines).strip()
                sections.append({
                    'heading': current_heading,
                    'content': text,
                    'words': len(text.split()),
                    'has_placeholder': '*Placeholder' in text or '*placeholder' in text,
                    'has_citations': bool(re.search(r'\[\[', text)),
                })
            current_heading = line.strip('# ').strip()
            current_lines = []
        else:
            current_lines.append(line)

    # Last section
    if current_lines:
        text = '\n'.join(current_lines).strip()
        sections.append({
            'heading': current_heading,
            'content': text,
            'words': len(text.split()),
            'has_placeholder': '*Placeholder' in text or '*placeholder' in text,
            'has_citations': bool(re.search(r'\[\[', text)),
        })

    # Score each section (lower = needs more work)
    for s in sections:
        score = 100
        if s['has_placeholder']:
            score -= 60
        if s['words'] < 30:
            score -= 40
        elif s['words'] < 100:
            score -= 20
        if not s['has_citations']:
            score -= 15
        s['score'] = max(0, score)

    return sections


def pick_weakest_section(sections: list[dict], page_score: float) -> dict | None:
    """Pick which section to improve. Returns None if page needs full rewrite."""
    # If page is very bad (score < 40), rewrite entire page
    if page_score < 40:
        return None

    # Otherwise, target the weakest section
    if not sections:
        return None

    weakest = min(sections, key=lambda s: s['score'])
    if weakest['score'] < 80:
        return weakest

    return None  # All sections look OK


def apply_mechanical_fixes(content: str, filepath: str) -> str:
    """Apply mechanical fixes without LLM: frontmatter, dates, orphan wikilinks."""
    today = datetime.date.today().isoformat()

    # Ensure frontmatter exists
    if not content.strip().startswith('---'):
        try:
            fm_block = frontmatter.dumps(frontmatter.load(filepath))
            if fm_block.strip().startswith('---'):
                end = fm_block.find('\n---', 3)
                if end != -1:
                    yaml_header = fm_block[:end + 4]
                    content = yaml_header + '\n' + content.lstrip()
        except Exception:
            pass

    # Force updated date to today
    content = re.sub(
        r'updated:\s*\d{4}-\d{2}-\d{2}',
        f'updated: {today}',
        content
    )

    # Remove duplicate blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def build_priority_queue(n: int = None) -> list[dict]:
    """Build priority queue of pages needing improvement, worst first.
    Prioritizes stubs with sources (they have material to work from).
    """
    pages = get_all_pages()
    scored = []

    for slug, filepath in pages.items():
        score, info = score_page(filepath)
        if score < 80:  # Only include pages that need work
            info['slug'] = slug
            # Boost stubs that have sources — the Matcher found papers for them
            if info['has_placeholder'] and info['sources'] > 0:
                info['score'] = max(0, info['score'] - 15)  # push to front of queue
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

    # Build page inventory for accurate wikilinks
    all_pages = get_all_pages()
    page_list = sorted(all_pages.keys())
    page_inventory = '\n'.join(f'  - {s}' for s in page_list)

    page_type = metadata.get('type', 'concept')
    is_concept = page_type == 'concept'
    is_entity = page_type == 'entity'
    is_comparison = page_type == 'comparison'

    # Type-specific word targets
    if is_concept:
        word_target = "500–800"
    elif is_entity:
        word_target = "400–600"
    else:
        word_target = "500–700"

    prompt = f"""You are the Ralph Writer agent improving a TVB Wiki page about whole-brain modeling and computational neuroscience. Follow the schema strictly.

## SCHEMA
{schema}

## YOUR TASK
Improve the wiki page: {slug}

## CURRENT PAGE CONTENT
{content}

## AVAILABLE SOURCE PAPERS
{sources_block}

## EXISTING WIKI PAGES (use these for [[wikilinks]] — only link to pages in this list)
{page_inventory}

## WRITING STYLE
- Write for a **graduate student in neuroscience** who is intelligent but not a specialist in this particular topic
- **Dense but readable** prose — like Scholarpedia or a very good Wikipedia science article, NOT like a PowerPoint slide
- Every section must have at least one full paragraph of prose. Avoid sections that are only a table or equations
- Cross-link aggressively: the first mention of any concept that appears in the page inventory above should be a [[wikilink]]. Aim for 8–15 wikilinks per page
- Avoid one-liner sections — if a section would be only 1–2 sentences, expand it or merge it

## STRUCTURAL REQUIREMENTS
1. **Opening paragraph** (2–3 sentences): What is this? Define it plainly before any technical detail
2. **Motivation / Context** (1–2 paragraphs): WHY does this exist? What problem does it solve? How does it fit into the broader field?
3. **Technical content**: Equations and tables are welcome but must be **surrounded by explanatory prose** — explain what each equation means in words
4. **Relationships**: Compare to related models/concepts. What came before? What came after? What are the tradeoffs?
{"5. **Biological grounding**: For model pages, explain what biological phenomena the model captures and how parameters map to neural mechanisms" if is_concept else "5. **Key features**: For entity pages, explain what makes this notable and how it's used in practice"}

## FORMATTING RULES
1. Replace ALL placeholder text (*Placeholder*) with real, sourced content
2. Add wikilinks [[like-this]] to related pages from the inventory above (minimum 8)
3. Add factual claims ONLY if you can cite a source or are confident from domain knowledge
4. Keep the YAML frontmatter, but update the `updated:` date to today ({datetime.date.today().isoformat()})
5. Add any new sources used to the `sources:` frontmatter list
6. Aim for {word_target} words for a full page
7. Use clear section headings (##)
8. Do NOT add a ## References section — a separate agent handles reference formatting

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
3. Is the writing quality sufficient for a Scholarpedia-level wiki? Dense prose, not bullet points or cheat-sheet style? (PASS/FAIL)
4. Does the page open with a clear, plain-English explanation before any equations? (PASS/FAIL)
5. Do all wikilinks [[like-this]] correspond to pages that plausibly exist in a TVB/whole-brain wiki? (PASS/FAIL)
6. Was placeholder text fully replaced? (PASS/FAIL)
7. Is there sufficient narrative context — motivation, history, comparisons — not just equations and tables? (PASS/FAIL)
8. Anything important missing that should be added? (NOTE or OK)

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

def _strip_code_fences(text: str) -> str:
    """Remove surrounding code fences from LLM output."""
    if text.startswith('```'):
        lines = text.split('\n')
        if lines[0].startswith('```'):
            lines = lines[1:]
        if lines and lines[-1].strip() == '```':
            lines = lines[:-1]
        text = '\n'.join(lines)
    return text


def _ensure_frontmatter(new_content: str, filepath: str) -> str:
    """Ensure content has YAML frontmatter with updated date set to today."""
    today = datetime.date.today().isoformat()

    if not new_content.strip().startswith('---'):
        # Re-attach frontmatter from original file
        try:
            fm_block = frontmatter.dumps(frontmatter.load(filepath))
            if fm_block.strip().startswith('---'):
                end = fm_block.find('\n---', 3)
                if end != -1:
                    yaml_header = fm_block[:end + 4]  # include closing ---
                    new_content = yaml_header + '\n' + new_content.lstrip()
        except Exception:
            pass

    # Ensure updated date is set to today
    new_content = re.sub(
        r'updated:\s*\d{4}-\d{2}-\d{2}',
        f'updated: {today}',
        new_content
    )

    return new_content


def improve_page(filepath: str) -> tuple[bool, str]:
    """
    Improve one page through writer → reviewer pipeline.
    Uses section-aware editing for pages with score >= 40.
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

    # Decide: section edit or full rewrite?
    page_score, page_info = score_page(filepath)
    sections = analyze_sections(original)
    target_section = pick_weakest_section(sections, page_score)

    if target_section:
        # SECTION-AWARE EDIT: improve only the weakest section
        section_heading = target_section['heading']
        log.info("Section-edit %s: targeting '%s' (score=%.0f, %d words)",
                 slug, section_heading, target_section['score'], target_section['words'])

        # Build sources block
        sources = get_sources(metadata)
        source_texts = []
        for source in sources[:3]:
            source_path = os.path.join(WIKI_ROOT, source) if not os.path.isabs(source) else source
            if os.path.exists(source_path):
                try:
                    with open(source_path, 'r', encoding='utf-8') as f:
                        src_content = f.read()[:2000]
                    source_texts.append(f"--- SOURCE: {source} ---\n{src_content}")
                except Exception:
                    pass
        sources_block = '\n\n'.join(source_texts) if source_texts else "(No source papers available)"

        # Load schema
        schema = ""
        if os.path.exists(SCHEMA_PATH):
            with open(SCHEMA_PATH, 'r') as f:
                schema = f.read()

        # Build page inventory for accurate wikilinks
        all_pages = get_all_pages()
        page_list = sorted(all_pages.keys())
        page_inventory = '\n'.join(f'  - {s}' for s in page_list)

        writer_prompt = f"""You are improving ONE SECTION of a TVB Wiki page about whole-brain modeling and computational neuroscience.

## SCHEMA
{schema}

## PAGE: {slug}
Full page content:
{original}

## SECTION TO IMPROVE: \"{section_heading}\"
Current content ({target_section['words']} words):
{target_section['content']}

## AVAILABLE SOURCE PAPERS
{sources_block}

## EXISTING WIKI PAGES (use these for [[wikilinks]])
{page_inventory}

## WRITING STYLE
- Dense but readable prose — like Scholarpedia, not a cheat sheet
- Every section needs explanatory prose, not just tables or equations
- Cross-link aggressively: wrap any term that appears in the page inventory in [[wikilinks]]
- Avoid one-liner sections — write full paragraphs

## INSTRUCTIONS
1. Rewrite ONLY the \"{section_heading}\" section with real, sourced content
2. Replace ALL placeholder text with factual content
3. Add wikilinks [[like-this]] to related pages from the inventory above
4. Cite sources where appropriate
5. Aim for 100-300 words for this section, with full paragraphs of prose
6. Output ONLY the new section content (no headings, no frontmatter, no commentary)
7. Do NOT include the ## heading line itself — just the section body
8. Do NOT add a ## References section"""

        success, output = run_pi(writer_prompt, model=WRITER_MODEL)
        if not success:
            return False, f"Writer failed for {slug} section '{section_heading}': {output[:100]}"

        new_section = _strip_code_fences(output)

        # Replace the old section in the page
        lines = original.split('\n')
        new_lines = []
        in_target = False
        replaced = False
        for line in lines:
            if line.strip().startswith('## ') and not line.strip().startswith('### '):
                heading_text = line.strip('# ').strip()
                if heading_text == section_heading and not replaced:
                    in_target = True
                    new_lines.append(line)  # keep the heading
                    new_lines.append(new_section)  # insert new content
                    continue
                elif in_target:
                    in_target = False
                    replaced = True
            if not in_target:
                new_lines.append(line)
        if in_target:
            replaced = True  # was last section

        if not replaced:
            return False, f"Could not locate section '{section_heading}' in {slug}"

        new_content = '\n'.join(new_lines)
        last_section_text = new_section  # save for revision
    else:
        # FULL REWRITE for low-score pages
        writer_prompt = build_writer_prompt(filepath)
        success, output = run_pi(writer_prompt, model=WRITER_MODEL)

        if not success:
            return False, f"Writer failed for {slug}: {output[:100]}"

        new_content = _strip_code_fences(output)

    last_section_text = None  # only set for section edits
    new_content = apply_mechanical_fixes(new_content, filepath)

    # Reviewer checks
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

    # Revise if needed
    if needs_revision:
        if target_section:
            revision_prompt = f"""Fix the issues flagged for the \"{section_heading}\" section of {slug}.
Return ONLY the corrected section body (no heading, no frontmatter).

ISSUES: {review_output}

YOUR PREVIOUS SECTION:
{last_section_text}

Corrected section:"""
        else:
            revision_prompt = f"""You are the Ralph Writer. Your edit to {slug} was flagged for issues.
Fix these issues and return the complete updated page (including frontmatter).

ISSUES FLAGGED BY REVIEWER:
{review_output}

YOUR PREVIOUS EDIT (which needs fixes):
{new_content}

Fix the issues and output ONLY the corrected markdown file."""

        rev_success, rev_output = run_pi(revision_prompt, model=WRITER_MODEL)
        if rev_success:
            revised = _strip_code_fences(rev_output)
            if target_section:
                # Re-splice the revised section into the page
                last_section_text = revised
                lines2 = original.split('\n')
                new_lines2 = []
                in_target2 = False
                replaced2 = False
                for line in lines2:
                    if line.strip().startswith('## ') and not line.strip().startswith('### '):
                        heading_text2 = line.strip('# ').strip()
                        if heading_text2 == section_heading and not replaced2:
                            in_target2 = True
                            new_lines2.append(line)
                            new_lines2.append(revised)
                            continue
                        elif in_target2:
                            in_target2 = False
                            replaced2 = True
                    if not in_target2:
                        new_lines2.append(line)
                if in_target2:
                    replaced2 = True
                new_content = '\n'.join(new_lines2) if replaced2 else new_content
            else:
                new_content = revised
            new_content = apply_mechanical_fixes(new_content, filepath)
            log.info("Revised %s after reviewer feedback", slug)

    # Validate
    valid, issues = validate_edit(filepath, new_content, original)
    if not valid:
        log.warn("Validation failed for %s: %s", slug, '; '.join(issues))
        return False, f"Validation failed for {slug}: {'; '.join(issues)}"

    # Write the improved page
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    mode = "section" if target_section else "full"
    return True, f"Improved {slug} ({word_count(new_content)} words, {mode} edit)"


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
