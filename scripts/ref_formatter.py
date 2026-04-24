#!/usr/bin/env python3
"""
Ralph RefFormatter Agent — ensures every page has exactly one well-formatted
## References section with human-readable citations.

Runs daily, after the Matcher (so sources are fresh).
Fully mechanical — no LLM needed.

Logic:
  1. For each page, read sources: from frontmatter
  2. For each source, extract title, authors, year, DOI, URL from the raw paper
  3. Check body for duplicate or missing ## References sections
  4. Merge duplicates, replace opaque slug-lists with formatted citations
  5. Leave already-formatted citations alone
"""
import os
import re
import sys
import json
import datetime

import frontmatter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, RAW_PAPERS_DIR, META_DIR,
    append_log, git_commit, get_all_pages, read_page, get_sources,
)

log = get_logger("RefFormatter")

# ── Metadata extraction from raw papers ────────────────────────────────

# Patterns for the two known raw-paper formats:
#   Format A (ingestor-generated): lines like "**Key**: Value"
#   Format B (deep-research-generated): YAML frontmatter + "**Key**: Value" lines

META_PATTERNS = {
    'title':     re.compile(r'^#\s+(.+)$', re.MULTILINE),
    'authors':   re.compile(r'\*\*Authors?\*\*:\s*(.+)$', re.MULTILINE),
    'year':      re.compile(r'\*\*Year\*\*:\s*(\d{4})', re.MULTILINE),
    'date':      re.compile(r'\*\*Date\*\*:\s*(\d{4}-\d{2}-\d{2})', re.MULTILINE),
    'doi':       re.compile(r'\*\*DOI\*\*:\s*(.+)$', re.MULTILINE),
    'url':       re.compile(r'\*\*URL\*\*:\s*(.+)$', re.MULTILINE),
    'venue':     re.compile(r'\*\*Venue\*\*:\s*(.+)$', re.MULTILINE),
    'journal':   re.compile(r'\*\*Journal\*\*:\s*(.+)$', re.MULTILINE),
    'published': re.compile(r'\*\*Published\*\*:\s*(.+)$', re.MULTILINE),
    'source':    re.compile(r'\*\*Source\*\*:\s*(.+)$', re.MULTILINE),
    'source_id': re.compile(r'\*\*ID\*\*:\s*(.+)$', re.MULTILINE),
}


def extract_paper_metadata(raw_path: str) -> dict:
    """Extract citation metadata from a raw paper file."""
    if not os.path.exists(raw_path):
        return {}

    try:
        with open(raw_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        return {}

    meta = {}

    # Try YAML frontmatter first (deep-research format)
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            fm = text[3:end]
            # Extract title from frontmatter
            m = re.search(r'title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if m:
                meta['title'] = m.group(1).strip('"\'')
            text = text[end + 4:]  # rest of the file

    # Extract from body using patterns
    for key, pattern in META_PATTERNS.items():
        if key in meta:
            continue  # already got it from frontmatter
        m = pattern.search(text)
        if m:
            meta[key] = m.group(1).strip()

    # Derive URL from source type if not present
    if 'url' not in meta:
        source = meta.get('source', '')
        source_id = meta.get('source_id', '')
        if source == 'arxiv' and source_id:
            base_id = source_id.split('v')[0]
            meta['url'] = f'https://arxiv.org/abs/{base_id}'
        elif source == 'pubmed' and source_id:
            meta['url'] = f'https://pubmed.ncbi.nlm.nih.gov/{source_id}/'

    # Derive year from date if not present
    if 'year' not in meta and 'date' in meta:
        meta['year'] = meta['date'][:4]

    return meta


def format_citation(meta: dict, index: int) -> str:
    """Format a single citation entry as a readable reference."""
    parts = []

    # Authors
    authors = meta.get('authors', '')
    if authors:
        parts.append(authors)
        if not authors.endswith('.'):
            parts.append('.')
    else:
        parts.append('(authors unknown).')

    # Year
    year = meta.get('year', '')
    if year:
        parts.append(f' ({year}).')

    # Title
    title = meta.get('title', '')
    if title:
        parts.append(f' *{title}*.')

    # Venue/Journal
    venue = meta.get('venue', '') or meta.get('journal', '')
    if venue:
        parts.append(f' {venue}.')

    # DOI link
    doi = meta.get('doi', '')
    if doi:
        doi_url = doi if doi.startswith('http') else f'https://doi.org/{doi}'
        parts.append(f' [DOI]({doi_url})')

    # URL (if no DOI, or different from DOI)
    url = meta.get('url', '')
    if url and not doi:
        parts.append(f' [Link]({url})')
    elif url and doi and url not in doi:
        source = meta.get('source', '')
        if source == 'arxiv':
            parts.append(f' [arXiv]({url})')

    citation = ''.join(parts).strip()
    if not citation:
        return ''

    return f'{index}. {citation}'


# ── Body analysis ──────────────────────────────────────────────────────

def find_references_sections(content: str) -> list[tuple[int, str]]:
    """
    Find all ## References (or ## Sources, ## Bibliography) headings in body.
    Returns list of (line_index, heading_text).
    """
    sections = []
    lines = content.split('\n')
    ref_pattern = re.compile(r'^##\s+(References?|Sources?|Bibliography)\s*$', re.IGNORECASE)
    for i, line in enumerate(lines):
        m = ref_pattern.match(line.strip())
        if m:
            sections.append((i, line.strip()))
    return sections


def extract_references_block(content: str, section_start: int) -> tuple[str, int]:
    """
    Extract the content of a References section (from heading to next ## or end).
    Returns (section_text, end_line_index).
    """
    lines = content.split('\n')
    end = len(lines)
    for i in range(section_start + 1, len(lines)):
        if lines[i].startswith('## ') and not lines[i].startswith('### '):
            end = i
            break
    block = '\n'.join(lines[section_start:end])
    return block, end


def is_opaque_reference(line: str) -> bool:
    """Check if a line looks like an opaque raw slug reference."""
    stripped = line.strip().lstrip('- •*0123456789. ').strip()
    # Match patterns like "arxiv-2509.02799", "semanticscholar-abc123", "raw/papers/..."
    if re.match(r'^(arxiv|semanticscholar|pubmed|openalex|doi)-[\w.\-]+', stripped):
        return True
    if stripped.startswith('raw/papers/'):
        return True
    return False


def parse_existing_citations(block: str) -> list[dict]:
    """
    Parse existing citations from a References block.
    Returns list of {'raw': line_text, 'is_opaque': bool, 'is_formatted': bool}
    """
    citations = []
    for line in block.split('\n'):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        # Skip empty list items
        if stripped in ('-', '* ', ''):
            continue

        is_opaque = is_opaque_reference(stripped)

        # Check if it looks like a proper citation (has author-like text, year, or DOI)
        is_formatted = bool(
            re.search(r'\d{4}', stripped) and
            (re.search(r'[A-Z][a-z]+.*[A-Z]', stripped) or re.search(r'doi|https?://', stripped, re.IGNORECASE))
            and not is_opaque
        )

        if stripped.startswith('-') or stripped.startswith('*') or re.match(r'^\d+\.', stripped):
            citations.append({
                'raw': stripped,
                'is_opaque': is_opaque,
                'is_formatted': is_formatted,
            })
    return citations


# ── Main formatting logic ─────────────────────────────────────────────

def format_page_references(filepath: str) -> tuple[bool, str]:
    """
    Format references for a single page.
    Returns (changed, description).
    """
    slug = os.path.basename(filepath)[:-3]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()
    except Exception as e:
        return False, f"Could not read {slug}: {e}"

    post = frontmatter.loads(raw)
    content = post.content
    metadata = dict(post.metadata)
    sources = get_sources(metadata)

    if not sources:
        return False, ''  # No sources to format

    # ── Extract metadata for each source ──
    paper_metas = []
    for source in sources:
        source_path = os.path.join(WIKI_ROOT, source) if not os.path.isabs(source) else source
        meta = extract_paper_metadata(source_path)
        if meta:
            paper_metas.append(meta)

    if not paper_metas:
        return False, ''

    # ── Analyze existing body references ──
    ref_sections = find_references_sections(content)

    # Build the ideal formatted references block
    formatted_lines = ['## References', '']
    for i, meta in enumerate(paper_metas, 1):
        cite = format_citation(meta, i)
        if cite:
            formatted_lines.append(cite)
    formatted_lines.append('')
    ideal_block = '\n'.join(formatted_lines)

    needs_fix = False
    fix_reason = ''

    if len(ref_sections) == 0:
        # No references section at all — append one
        needs_fix = True
        fix_reason = 'missing'

    elif len(ref_sections) > 1:
        # Duplicate sections — merge into one
        needs_fix = True
        fix_reason = f'{len(ref_sections)} duplicate sections'

    else:
        # Exactly one section — check quality
        start_line = ref_sections[0][0]
        block, end_line = extract_references_block(content, start_line)
        citations = parse_existing_citations(block)

        opaque_count = sum(1 for c in citations if c['is_opaque'])
        if opaque_count > 0:
            needs_fix = True
            fix_reason = f'{opaque_count} opaque references'

    if not needs_fix:
        return False, ''

    # ── Apply fix ──
    lines = content.split('\n')

    if len(ref_sections) == 0:
        # Append at end of file
        # Ensure there's a blank line before
        if lines and lines[-1].strip():
            lines.append('')
        lines.append(ideal_block)
        new_content = '\n'.join(lines)

    elif len(ref_sections) > 1:
        # Remove all existing ref sections, then append one at the first position
        # Find the range: from first ref section heading to last ref section end
        first_start = ref_sections[0][0]
        last_start = ref_sections[-1][0]
        _, last_end = extract_references_block(content, last_start)

        # Remove everything from first_start to last_end
        new_lines = lines[:first_start] + lines[last_end:]
        # Append ideal block
        if new_lines and new_lines[-1].strip():
            new_lines.append('')
        new_lines.append(ideal_block)
        new_content = '\n'.join(new_lines)

    else:
        # Replace the single existing section
        start_line = ref_sections[0][0]
        _, end_line = extract_references_block(content, start_line)
        new_lines = lines[:start_line] + lines[end_line:]
        # Insert ideal block at start_line position
        if new_lines and new_lines[-1].strip():
            new_lines.append('')
        new_lines.append(ideal_block)
        new_content = '\n'.join(new_lines)

    # Update frontmatter date and write
    post.content = new_content
    post.metadata['updated'] = datetime.date.today().isoformat()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))

    return True, f'{slug}: {fix_reason}'


# ── Main cycle ─────────────────────────────────────────────────────────

def run_ref_formatter_cycle() -> dict:
    """Run one ref formatter cycle across all pages."""
    log.info("Starting reference formatting cycle")

    pages = get_all_pages()
    stats = {
        'timestamp': datetime.datetime.now().isoformat(),
        'total_pages': len(pages),
        'pages_fixed': 0,
        'fixes': [],
    }

    for slug, filepath in sorted(pages.items()):
        try:
            changed, desc = format_page_references(filepath)
            if changed:
                stats['pages_fixed'] += 1
                stats['fixes'].append(desc)
                log.info("  Fixed: %s", desc)
        except Exception as e:
            log.warn("  Error formatting %s: %s", slug, e)

    if stats['pages_fixed'] > 0:
        git_commit(
            f"RefFormat: fixed references on {stats['pages_fixed']} pages "
            f"(RefFormatter)"
        )
        append_log(
            f"RefFormatter: formatted references on {stats['pages_fixed']} pages"
        )
        log.info("Committed %d reference fixes", stats['pages_fixed'])
    else:
        log.info("All references already well-formatted")

    # Save stats
    stats_file = os.path.join(META_DIR, 'ref_format_stats.json')
    os.makedirs(META_DIR, exist_ok=True)
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    log.info("Cycle complete. %d pages fixed.", stats['pages_fixed'])
    return stats


if __name__ == '__main__':
    run_ref_formatter_cycle()
