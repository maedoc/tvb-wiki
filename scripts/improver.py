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
    get_fulltext,
    PARALLEL_WRITERS, PARALLEL_REVIEWERS,
)
from combined_relevance import load_graph, load_embeddings, bfs_distances, CORE_LINKS as RELEVANCE_CORE, get_emb_scores
import citation_verify
import create_paper_stub

log = get_logger("Improver")

# ── Citation guard cooldown state ──────────────────────────────────────

GUARD_COOLDOWN_FILE = os.path.join(WIKI_ROOT, "meta", "guard_cooldown.json")
GUARD_COOLDOWN_HOURS = 24
GUARD_REJECTION_THRESHOLD = 3


def _load_cooldown() -> dict:
    """Load per-page rejection timestamps."""
    if not os.path.exists(GUARD_COOLDOWN_FILE):
        return {}
    try:
        with open(GUARD_COOLDOWN_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def _save_cooldown(state: dict) -> None:
    """Save cooldown state."""
    try:
        os.makedirs(os.path.dirname(GUARD_COOLDOWN_FILE), exist_ok=True)
        with open(GUARD_COOLDOWN_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)
    except OSError:
        pass


def _record_rejection(slug: str) -> None:
    """Bump rejection count and set cooldown if threshold reached."""
    state = _load_cooldown()
    now = datetime.datetime.now().isoformat()
    entry = state.get(slug, {"count": 0, "last": None, "until": None})
    entry["count"] += 1
    entry["last"] = now
    if entry["count"] >= GUARD_REJECTION_THRESHOLD:
        entry["until"] = (datetime.datetime.now() + datetime.timedelta(hours=GUARD_COOLDOWN_HOURS)).isoformat()
        log.info("[Cooldown] %s enters 24h cooldown after %d rejections", slug, entry["count"])
    state[slug] = entry
    _save_cooldown(state)


def _is_in_cooldown(slug: str) -> bool:
    """Check if a page is currently in cooldown."""
    state = _load_cooldown()
    entry = state.get(slug)
    if not entry or not entry.get("until"):
        return False
    until = datetime.datetime.fromisoformat(entry["until"])
    if datetime.datetime.now() < until:
        log.info("[Cooldown] Skipping %s (cooldown until %s)", slug, entry["until"])
        return True
    return False


def _clear_expired_cooldowns() -> None:
    """Remove expired cooldown entries."""
    state = _load_cooldown()
    now = datetime.datetime.now()
    expired = [slug for slug, entry in state.items()
               if entry.get("until") and now >= datetime.datetime.fromisoformat(entry["until"])]
    if expired:
        for slug in expired:
            del state[slug]
        _save_cooldown(state)
        log.info("[Cooldown] Cleared %d expired entries", len(expired))


# ── Page scoring ───────────────────────────────────────────────────────

def score_page(filepath: str) -> tuple[float, dict]:
    """
    Score a page by quality. Lower = needs more work.
    Returns (score, info_dict).
    """
    try:
        metadata, content = read_page(filepath)
    except Exception as e:
        return 0.0, {'error': str(e), 'path': filepath, 'has_placeholder': False, 'sources': 0}

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
    structural_issues = []

    # ── Structural quality checks ──────────────────────────────────────
    # 1) Leaked frontmatter in body (content starts with title: or ---)
    content_start = content.strip()[:20].lower()
    if content_start.startswith('title:') or content_start.startswith('---'):
        score -= 50
        structural_issues.append('leaked_frontmatter')
        log.debug("%s: leaked frontmatter detected", filepath)

    # 2) No body content (just frontmatter or empty)
    body_words = word_count(content.strip())
    if body_words < 20:
        score -= 40
        structural_issues.append('empty_body')

    # 3) Duplicate hardcoded References section (should be hook-generated)
    if re.search(r'^##\s*References\s*$', content, re.MULTILINE) and info['sources'] > 0:
        score -= 20
        structural_issues.append('dup_references')

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

    info['structural_issues'] = structural_issues
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
    """Apply mechanical fixes without LLM: frontmatter, dates, orphan wikilinks, strip body refs, strip leaked frontmatter."""
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

    # ── Strip leaked frontmatter from body ──
    # If content has multiple --- blocks, keep only the first
    if content.startswith('---'):
        first_end = content.find('\n---', 3)
        if first_end != -1:
            after_first = content[first_end + 4:]
            # Check for second frontmatter block starting with \ntitle: or \ncreated:
            second_fm = re.search(r'\n(?:title:|created:|sources:|tags:)\s*', after_first)
            if second_fm:
                # Strip everything from second frontmatter onward
                content = content[:first_end + 4] + after_first[:second_fm.start()]

    # ── Strip code fences ──
    stripped = content.strip()
    if stripped.startswith('```markdown') or stripped.startswith('```yaml'):
        lines = stripped.split('\n')
        if lines[0].startswith('```'):
            lines = lines[1:]
        if lines and lines[-1].strip() == '```':
            lines = lines[:-1]
        content = '\n'.join(lines)
    if stripped.startswith('```'):
        lines = stripped.split('\n')
        if lines[0].startswith('```'):
            lines = lines[1:]
        if lines and lines[-1].strip() == '```':
            lines = lines[:-1]
        content = '\n'.join(lines)

    # ── Strip body ## References section ──
    # Find ## References in body (not in frontmatter)
    if content.startswith('---'):
        fm_end = content.find('\n---', 3)
        if fm_end != -1:
            body = content[fm_end + 4:]
            # Remove ## References to end of content or next ## heading
            refs_match = re.search(r'\n##\s*References\s*\n', body)
            if refs_match:
                refs_start = refs_match.start()
                refs_end = len(body)
                # Check if there's another ## heading after References
                next_heading = re.search(r'\n##\s+', body[refs_match.end():])
                if next_heading:
                    refs_end = refs_match.end() + next_heading.start()
                body = body[:refs_start] + body[refs_end:]
                content = content[:fm_end + 4] + body

    # Remove duplicate blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Remove trailing whitespace
    content = re.sub(r' +\n', '\n', content)
    # Ensure content ends with single newline
    content = content.rstrip() + '\n'

    return content


# ── Cached relevance data (lazy load) ─────────────────────────────────
_relevance_data = None

def _get_relevance_data():
    global _relevance_data
    if _relevance_data is not None:
        return _relevance_data
    try:
        outlinks, indegree, all_slugs = load_graph(WIKI_ROOT)
        page_embs, slugs_emb, centroid, core_i, sim, mat_n = load_embeddings(WIKI_ROOT)
        g_dist = bfs_distances(outlinks, all_slugs, RELEVANCE_CORE)
        _relevance_data = (page_embs, slugs_emb, mat_n, centroid, core_i, sim, g_dist)
    except Exception as e:
        log.warn("Could not load relevance data: %s", e)
        _relevance_data = (None, None, None, None, None, None, {})
    return _relevance_data


def build_priority_queue(n: int = None) -> list[dict]:
    """Build priority queue of pages needing improvement, worst first.
    Prioritizes stubs with sources AND graph-connected stubs.
    """
    pages = get_all_pages()
    scored = []
    
    # Load relevance data once
    rel_data = _get_relevance_data()
    _, _, _, _, _, _, g_dist = rel_data

    for slug, filepath in pages.items():
        score, info = score_page(filepath)
        if score < 80 and 'error' not in info:
            info['slug'] = slug
            info['score'] = info.get('score', score)
            has_ph = info.get('has_placeholder', False)
            srcs = info.get('sources', 0)
            
            # #2: Boost stubs that have sources (from Matcher)
            if has_ph and srcs > 0:
                info['score'] = max(0, info['score'] - 15)
            
            # #2: Boost graph-connected pages (likely TVB-relevant)
            dist = g_dist.get(slug, 999)
            if dist <= 3:
                info['score'] = max(0, info['score'] - 10)
            elif dist == 999:
                info['score'] += 5  # Slight penalty for orphans
            
            # Boost very thin pages (high priority for expansion)
            wc = info.get('word_count', 0)
            if wc < 20:
                info['score'] = max(0, info['score'] - 20)
            elif wc < 100:
                info['score'] = max(0, info['score'] - 10)
            
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
    for source in sources[:5]:  # Limit to 5 most relevant
        source_path = os.path.join(WIKI_ROOT, source) if not os.path.isabs(source) else source
        if os.path.exists(source_path):
            try:
                with open(source_path, 'r', encoding='utf-8') as f:
                    src_content = f.read()[:2000]  # Truncate long papers
                # Append full-text excerpt if available
                src_slug = os.path.basename(source_path)[:-3]
                ft = get_fulltext(src_slug, max_chars=2000)  # reduced from 6000 to keep prompts under 3000 tokens
                if ft:
                    src_content += f"\n\n--- FULL TEXT EXCERPT ({src_slug}) ---\n{ft}"
                source_texts.append(f"--- SOURCE: {source} ---\n{src_content}")
            except Exception:
                pass

    sources_block = '\n\n'.join(source_texts) if source_texts else "(No source papers available — use general knowledge)"

    # Read schema
    schema = ""
    if os.path.exists(SCHEMA_PATH):
        with open(SCHEMA_PATH, 'r') as f:
            schema = f.read()

    # Build page inventory for accurate wikilinks (capped to prevent prompt bloat)
    all_pages = get_all_pages()
    page_list = sorted(all_pages.keys())
    # Limit to 50 most relevant pages to keep prompts under 2500 tokens
    page_inventory = '\n'.join(f'  - {s}' for s in page_list[:50])
    if len(page_list) > 50:
        page_inventory += f"\n  ... and {len(page_list) - 50} more pages"

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
{"5. **Biological grounding**: For model pages, explain what biological phenomena the model captures and how parameters map to neural mechanisms" if is_concept else "5. **Key features**: For entity pages, explain what makes this notable and how it's used in practice, with a mandatory Relationship to TVB section"}

## SCOPE RULES — DO NOT VIOLATE
- This wiki covers whole-brain modeling via TVB and related computational neuroscience
- Do NOT write biographical content about individual researchers or lab PIs
- Do NOT write about generic neuroimaging preprocessing pipelines (SPM, FSL, fmriprep) unless specifically discussing TVB connectivity pipeline integration
- Do NOT write about generic data viewers, atlases, or segmentation tools unless discussing how TVB uses their outputs
- Do NOT write about generic Python data science libraries
- For entity pages, ALWAYS include a "Relationship to TVB" section explaining how this tool/concept connects to TVB workflows

## CITATION REQUIREMENTS
- Every factual claim MUST be supported by an inline citation to a source paper using the format `[[raw/papers/SLUG.md]]` or `[[raw/papers/SLUG.md|Author et al. (Year)]]`.
- If the provided source papers do not support a claim, do not include that claim.
- Before writing, review the source papers in the prompt. Synthesize their content, don't write from general knowledge.
- Aim for at least 3 inline citations per paragraph of factual content.

## FORMATTING RULES
1. Replace ALL placeholder text (*Placeholder*) with real, sourced content
2. Add wikilinks [[like-this]] to related pages from the inventory above (minimum 8)
3. Add factual claims ONLY if you can cite a source or are confident from domain knowledge
4. Keep the YAML frontmatter, but update the `updated:` date to today ({datetime.date.today().isoformat()})
5. Add any new sources used to the `sources:` frontmatter list
6. Aim for {word_target} words for a full page
7. Use clear section headings (##)
8. Do NOT add a `## References` section in the body — add sources to YAML `sources:` frontmatter only
9. Do NOT write meta-commentary like "Here is the corrected file", "I have fixed", or "Below is the updated version"
10. Do NOT wrap your output in ```markdown or ```yaml code fences — output raw markdown only
11. Do NOT leak frontmatter into the body — the frontmatter block ends at the second `---` and the body starts immediately after
12. Do NOT write in first person ("I think", "I recommend") or address the reader directly ("you should", "let me explain")

Write the COMPLETE updated page (including frontmatter). Output ONLY the markdown file content, no commentary."""
    return prompt


def build_reviewer_prompt(filepath: str, original_content: str, edited_content: str) -> str:
    """Build the prompt for the reviewer to check an edit."""
    # #5 Count inline citations [[ref-name]] and footnote-style [^n]
    inline_cites = len(re.findall(r'\[\[[^\]]+\]\]', edited_content))
    footnote_cites = len(re.findall(r'\[?\^[^\]]+\]?', edited_content))
    word_count_val = len(edited_content.split())
    
    # Flag low citation density
    cite_note = ""
    if word_count_val > 300:
        density = (inline_cites + footnote_cites) / (word_count_val / 500)
        if density < 3:
            cite_note = f"\nNOTE: Citation density is low ({density:.1f} per 500 words). A dense wiki article should have ≥3 inline citations per 500 words."

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
2. Check that EVERY factual claim has an inline citation to `raw/papers/*.md`. (PASS/FAIL)
3. Flag any paragraph with zero citations as FAIL. (PASS/FAIL)
4. Verify that cited papers actually support the claims made about them. (PASS/FAIL)
5. Are there any factual errors or dubious claims? (PASS/FAIL)
6. Is the writing quality sufficient for a Scholarpedia-level wiki? Dense prose, not bullet points or cheat-sheet style? (PASS/FAIL)
7. Does the page open with a clear, plain-English explanation before any equations? (PASS/FAIL)
8. Do all wikilinks [[like-this]] correspond to pages that plausibly exist in a TVB/whole-brain wiki? (PASS/FAIL)
9. Was placeholder text fully replaced? (PASS/FAIL)
10. Is there sufficient narrative context — motivation, history, comparisons — not just equations and tables? (PASS/FAIL)
11. Are there enough inline citations (≥3 per 500 words for dense articles, and ≥3 per paragraph of factual content)? (PASS/FAIL)
12. If citations are missing or inadequate, demand revision. (PASS/FAIL)
13. Anything important missing that should be added? (NOTE or OK)
{cite_note}

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

    # ── Post-write structural guards ──
    # Check body starts with meta-commentary
    body_lower = new_content.lower()
    meta_phrases = [
        'here is the corrected', 'here is the revised', 'here is the updated',
        'here is the fixed', 'i\'ll fix', 'i will fix', 'all issues fixed',
        'i have fixed', 'i have corrected', 'i have addressed',
        'i have updated', 'i have added', 'i have removed', 'i have modified',
        'i have rewritten', 'i have revised', 'i have successfully',
        'below is the corrected', 'below is the revised', 'below is the updated',
        'the corrected file', 'corrected file has been written',
        'revision complete', 'update complete', 'changes applied',
    ]
    for phrase in meta_phrases:
        if phrase in body_lower[:2000]:
            issues.append(f"Meta-commentary detected: '{phrase}'")
            break

    # Check for leaked frontmatter in body
    # Find end of frontmatter
    body = new_content
    if body.startswith('---'):
        fm_end = body.find('\n---', 3)
        if fm_end != -1:
            actual_body = body[fm_end+4:].strip()
            if actual_body.startswith('title:') or actual_body.startswith('created:') or actual_body.startswith('---'):
                issues.append("Leaked frontmatter in body")

    # Check for body ## References (should not exist anymore)
    if '\n## References' in body or body.strip().startswith('## References'):
        issues.append("Body contains ## References section — use YAML sources: instead")

    # Check for code fences still present
    if '```markdown' in body or '```yaml' in body:
        issues.append("Output wrapped in code fences — output raw markdown only")

    return len(issues) == 0, issues


# ── Improve a single page ─────────────────────────────────────────────

def _strip_code_fences(text: str) -> str:
    """Remove surrounding code fences from LLM output."""
    stripped = text.strip()
    if stripped.startswith('```markdown') or stripped.startswith('```yaml'):
        lines = stripped.split('\n')
        if lines[0].startswith('```'):
            lines = lines[1:]
        if lines and lines[-1].strip() == '```':
            lines = lines[:-1]
        text = '\n'.join(lines)
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
        for source in sources[:5]:
            source_path = os.path.join(WIKI_ROOT, source) if not os.path.isabs(source) else source
            if os.path.exists(source_path):
                try:
                    with open(source_path, 'r', encoding='utf-8') as f:
                        src_content = f.read()[:2000]
                    src_slug = os.path.basename(source_path)[:-3]
                    ft = get_fulltext(src_slug, max_chars=2000)  # reduced from 6000 to keep prompts under 3000 tokens
                    if ft:
                        src_content += f"\n\n--- FULL TEXT EXCERPT ({src_slug}) ---\n{ft}"
                    source_texts.append(f"--- SOURCE: {source} ---\n{src_content}")
                except Exception:
                    pass
        sources_block = '\n\n'.join(source_texts) if source_texts else "(No source papers available)"

        # Load schema
        schema = ""
        if os.path.exists(SCHEMA_PATH):
            with open(SCHEMA_PATH, 'r') as f:
                schema = f.read()

        # Build page inventory for accurate wikilinks (capped to prevent prompt bloat)
        all_pages = get_all_pages()
        page_list = sorted(all_pages.keys())
        # Limit to 50 most relevant pages to keep prompts under 2500 tokens
        page_inventory = '\n'.join(f'  - {s}' for s in page_list[:50])
        if len(page_list) > 50:
            page_inventory += f"\n  ... and {len(page_list) - 50} more pages"

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
4. Cite sources where appropriate — every factual claim needs an inline citation `[[raw/papers/SLUG.md]]` or `[[raw/papers/SLUG.md|Author et al. (Year)]]`
5. If the provided source papers do not support a claim, do not include that claim
6. Review the source papers and synthesize their content; do not write from general knowledge
7. Aim for at least 3 inline citations per paragraph of factual content
8. Aim for 100-300 words for this section, with full paragraphs of prose
6. Output ONLY the new section content (no headings, no frontmatter, no commentary)
9. Do NOT include the ## heading line itself — just the section body
10. Do NOT add a ## References section"""

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
    is_major = False
    if review_success:
        verdict = review_output.strip().lower()
        if 'needs_revision' in verdict or 'fail' in verdict:
            # #1: Classify issue severity
            issues_lower = review_output.lower()
            is_major = any(kw in issues_lower for kw in [
                'factual error', 'thin narrative', 'poor structure',
                'incorrect', 'hallucination', 'not dense', 'not scholarly',
                'missing context', 'insufficient context', 'low quality',
                'dubious claim',
            ])
            if is_major:
                needs_revision = True
                log.info("Reviewer flagged MAJOR issues for %s: %s", slug, review_output[:100])
            else:
                needs_revision = True
                log.info("Reviewer flagged minor issues for %s — trying quick revision", slug)
        else:
            log.info("Reviewer approved %s", slug)
    else:
        log.warn("Reviewer failed for %s, accepting writer output", slug)

    # #1: Conditional revise — major issues get full revision, minor get quick fix
    if needs_revision:
        if is_major:
            # Full revision (current behavior)
            if target_section:
                revision_prompt = f"""Fix the issues flagged for the \"{section_heading}\" section of {slug}.
Return ONLY the corrected section body (no heading, no frontmatter).
Do NOT explain your changes, summarize what you did, add meta-commentary, or say \"here's the corrected section\".

ISSUES: {review_output}

YOUR PREVIOUS SECTION:
{last_section_text}

Corrected section:"""
            else:
                revision_prompt = f"""You are the Ralph Writer. Your edit to {slug} was flagged for issues.
Fix these issues and return the complete updated page (including frontmatter).

**CRITICAL:** Output ONLY the final markdown content. Do NOT explain your changes, summarize what you did, add numbered lists of corrections, or include any meta-commentary like \"Here's a summary of fixes\" or \"The corrected page\".

ISSUES FLAGGED BY REVIEWER:
{review_output}

YOUR PREVIOUS EDIT (which needs fixes):
{new_content}

Fixed page:"""
            rev_success, rev_output = run_pi(revision_prompt, model=WRITER_MODEL)
        else:
            # Quick revision for minor issues: same model, lighter prompt
            quick_prompt = f"""You are editing the markdown page for {slug}. 
The reviewer flagged only MINOR style issues (citations, wikilinks, formatting). 
Fix them IN-PLACE and return the COMPLETE UPDATED PAGE — every section intact.

**CRITICAL:** Output ONLY the final markdown page. Do NOT list what you changed. 
Do NOT write "Done" or "Fixed issues" or summaries. 
Do NOT add meta-commentary. Just return the page content.

ISSUES: {review_output}

CURRENT CONTENT:
{new_content}

Updated content:"""
            rev_success, rev_output = run_pi(quick_prompt, model=WRITER_MODEL, timeout=120)
            if rev_success:
                revised = _strip_code_fences(rev_output)
                # Safety guard: reject pure meta-commentary
                first_line = revised.strip().split('\n')[0].strip().lower() if revised.strip() else ""
                if first_line.startswith(('done.', 'fixed', 'here is', 'okay.', 'ok.', 'summary', 'changes made', 'the corrected', 'polished', 'i fixed')):
                    log.warn("Quick revision for %s produced meta-commentary — keeping original", slug)
                    rev_success = False  # Skip outer revision block; keep original
            else:
                rev_success = False  # Ensure outer block is skipped

        if rev_success:
            revised = _strip_code_fences(rev_output)
            if target_section and is_major:
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


# ── Citation Guard ────────────────────────────────────────────────────

CITATION_GUARD_BLOCKING = False  # Set True after 48h log-only burn-in


def _citation_guard(page_path: str, stub_index: dict[str, str]) -> tuple[bool, list[str]]:
    """
    Verify all inline citations in a page are backed by real stubs or databases.
    Auto-creates missing stubs when OpenAlex/CrossRef finds a match.
    Returns (pass, issues).

    Non-blocking if CITATION_GUARD_BLOCKING is False (logs only).
    """
    import re
    metadata, content = read_page(page_path)
    slug = os.path.splitext(os.path.basename(page_path))[0]
    sources = get_sources(metadata)
    n_sources = len(sources) if sources else 0

    citations = citation_verify.parse_inline_citations(content)
    if not citations:
        return True, []

    issues = []
    verified_count = 0
    not_found_count = 0
    new_stubs = []

    for cite in citations:
        # Skip bracket / superscript refs if within bounds of YAML sources
        if cite.get("type") in ("superscript", "bracket_num"):
            num = cite.get("num", 0)
            if num <= n_sources:
                verified_count += 1
                continue
            # If out of bounds, still flag it
            issues.append(f"citation '{cite['text']}' out of bounds (page has {n_sources} sources)")
            not_found_count += 1
            continue

        # Also skip bare DOIs that are already in the page's sources list
        if cite.get("type") == "doi":
            raw_doi = cite.get("doi", "")
            # Check if this DOI appears in any source stub
            source_match = False
            for src in (sources or []):
                if isinstance(src, str) and raw_doi in src:
                    source_match = True
                    break
                if isinstance(src, dict) and raw_doi in str(src.get("doi", "")):
                    source_match = True
                    break
            if source_match:
                verified_count += 1
                continue

        result = citation_verify.verify_citation(cite, stub_index)
        if result["status"] == "VERIFIED":
            verified_count += 1
            if result["source"] == "stub_cache":
                log.info("[Guard] %s → VERIFIED via stub %s", cite['text'], result["raw_stub_path"])
            else:
                log.info("[Guard] %s → VERIFIED via %s", cite['text'], result["source"])
                # Auto-create stub if it doesn't exist
                if not result.get("raw_stub_path") and result.get("metadata"):
                    stub_path = create_paper_stub.create_stub_from_citation(cite, RAW_PAPERS_DIR)
                    if stub_path:
                        new_stubs.append(stub_path)
                        log.info("[Guard] Auto-created stub: %s", stub_path)
                        # Also add to stub_index for this cycle
                        stub_slug = os.path.splitext(os.path.basename(stub_path))[0]
                        stub_index[stub_slug] = stub_path
                    else:
                        log.warn("[Guard] VERIFIED but stub creation failed for %s", cite['text'])
        elif result["status"] == "METADATA_MISMATCH":
            log.warn("[Guard] %s → METADATA_MISMATCH (stub=%s ext=%s)", cite['text'], result["raw_stub_path"], result["metadata"])
        elif result["status"] == "NOT_FOUND":
            log.warn("[Guard] %s → NOT_FOUND in any database", cite['text'])
            not_found_count += 1
            issues.append(f"citation '{cite['text']}' not found")

    # If we created new stubs, add them to page YAML sources
    if new_stubs:
        try:
            sources = get_sources(metadata)
            for stub_path in new_stubs:
                rel_path = os.path.relpath(stub_path, WIKI_ROOT)
                if rel_path not in sources:
                    sources.append(rel_path)
            # Rebuild YAML frontmatter with new sources
            metadata['sources'] = sources
            metadata['updated'] = datetime.datetime.now().strftime('%Y-%m-%d')
            new_page = frontmatter.dumps(frontmatter.Post(content, **metadata))
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(new_page)
            log.info("[Guard] Updated %s sources: %s", slug, new_stubs)
        except Exception as e:
            log.error("[Guard] Failed to update %s sources: %s", slug, e)

    if not_found_count > 0:
        log.warn("[Guard] %s: %d/%d citations NOT_FOUND", slug, not_found_count, len(citations))
        _record_rejection(slug)
        return False, issues
    return True, []


# ── Main improver cycle ───────────────────────────────────────────────

def run_improver_cycle(n_pages: int = None):
    """
    Run one improver cycle. Improves N pages in parallel.
    Returns (pages_improved, pages_failed).
    """
    n_pages = n_pages or PARALLEL_WRITERS
    log.info("Starting hourly cycle")

    # Clear expired cooldowns
    _clear_expired_cooldowns()

    # Build priority queue
    queue = build_priority_queue()
    log.info("Scoring %d pages, %d need improvement (score < 80)",
             len(get_all_pages()), len(queue))

    # Filter out pages in cooldown
    queue = [t for t in queue if not _is_in_cooldown(t['slug'])]
    if len(queue) < len(get_all_pages()):
        log.info("  %d pages after cooldown filter", len(queue))

    if not queue:
        log.info("Cycle complete. All pages look good (or in cooldown)!")
        return 0, 0

    # Pick worst N pages
    targets = queue[:n_pages]
    for t in targets:
        issues = t.get('structural_issues', [])
        issue_flag = f', STRUCTURAL:{",".join(issues)}' if issues else ''
        log.info("  %s (score=%.0f, %d words, %d refs%s%s)",
                 t['slug'], t['score'], t['words'], t['sources'],
                 ', PLACEHOLDER' if t.get('has_placeholder') else '',
                 issue_flag)

    # Improve pages in parallel
    improved = 0
    failed = 0
    results = []

    # Build stub index once for citation guard
    stub_index = citation_verify.build_stub_index(RAW_PAPERS_DIR)

    with ThreadPoolExecutor(max_workers=n_pages) as pool:
        futures = {
            pool.submit(improve_page, t['path']): t
            for t in targets
        }
        for future in as_completed(futures):
            target = futures[future]
            try:
                success, desc = future.result()
                results.append((target['slug'], success, desc, target['path']))
                if success:
                    improved += 1
                else:
                    failed += 1
            except Exception as e:
                log.error("Exception improving %s: %s", target['slug'], e)
                failed += 1

    # ── Citation Guard — post-write, pre-commit ──
    guarded_results = []
    for slug, success, desc, filepath in results:
        if not success:
            guarded_results.append((slug, False, desc))
            continue
        try:
            guard_pass, guard_issues = _citation_guard(filepath, stub_index)
            if guard_pass:
                guarded_results.append((slug, True, desc))
            else:
                log.warn("Guard rejected %s: %s", slug, '; '.join(guard_issues))
                # Revert the written file
                try:
                    subprocess.run(['git', 'checkout', '--', filepath], check=True, cwd=WIKI_ROOT)
                    log.info("Reverted %s to last committed version", filepath)
                except Exception:
                    log.error("Failed to revert %s", filepath)
                if CITATION_GUARD_BLOCKING:
                    improved -= 1
                    failed += 1
                    guarded_results.append((slug, False, f"Citation guard rejected: {'; '.join(guard_issues)}"))
                else:
                    # Log-only mode: still count as improved but log the issue
                    guarded_results.append((slug, True, desc + f" [GUARD_WARN: {' | '.join(guard_issues)}]"))
        except Exception as e:
            log.error("Citation guard exception on %s: %s", slug, e)
            guarded_results.append((slug, True, desc))  # allow through on guard error

    # Git commit improved pages that passed the guard
    improved_slugs = [r[0] for r in guarded_results if r[1]]
    if improved_slugs:
        msg = f"Improve: {', '.join(improved_slugs)} (Writer:{WRITER_MODEL} Reviewer:{REVIEWER_MODEL}) (Improver)"
        git_commit(msg)
        append_log(f"Improve: {len(improved_slugs)} pages improved ({', '.join(improved_slugs)})")
        log.info("Committed: \"%s\"", msg)

    log.info("Cycle complete. %d improved, %d failed.", len(improved_slugs), failed)
    return len(improved_slugs), failed


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Ralph Improver Agent")
    parser.add_argument("-n", type=int, default=PARALLEL_WRITERS,
                        help=f"Number of pages to improve in parallel (default: {PARALLEL_WRITERS})")
    args = parser.parse_args()
    run_improver_cycle(args.n)
