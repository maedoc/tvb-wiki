#!/usr/bin/env python3
"""
Enrich raw/papers/*.md stubs by querying OpenAlex and CrossRef for real metadata.

Input:  raw/papers/*.md files with frontmatter (title, authors, year, venue, doi)
Output: Updates those files in-place with verified metadata + BibTeX.

Strategy per paper:
  1. If DOI present  → query CrossRef via DOI (authoritative)
  2. Else if title   → query OpenAlex by title search
  3. If hits found   → update authors[], year, venue, doi, and regenerate BibTeX
  4. If not found    → leave untouched (no degradation)

Uses:
  - OpenAlex REST API (free, 100k credits/day with key)
  - CrossRef REST API (free, polite pool with email)

Requires: requests (stdlib JSON)
"""
import glob
import json
import re
import time
import urllib.request
import urllib.parse
import urllib.error
from typing import Any

RAW_DIR = 'raw/papers'
# Use email for CrossRef polite pool and optional OpenAlex
_CONTACT_EMAIL = "marmaduke.woodman@univ-amu.fr"
_OPENALEX_KEY = None  # set from env if needed


def _http_json(url: str, headers: dict | None = None) -> dict | None:
    """GET JSON and return parsed dict, or None on failure."""
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception:
        return None


def openalex_search(title: str) -> dict | None:
    """Search OpenAlex works by title. Returns normalized hit or None."""
    q = urllib.parse.quote(title)
    url = f"https://api.openalex.org/works?search={q}&per-page=5&mailto={_CONTACT_EMAIL}"
    if _OPENALEX_KEY:
        url += f"&api_key={_OPENALEX_KEY}"
    data = _http_json(url)
    if not data or not data.get('results'):
        return None
    # Pick the best match by title similarity
    best = None
    best_score = 0
    t_lower = title.lower()
    for r in data['results']:
        cand = (r.get('title') or '').lower()
        score = len(set(t_lower.split()) & set(cand.split())) / max(len(t_lower.split()), 1)
        if score > best_score:
            best_score = score
            best = r
    if not best or best_score < 0.3:
        return None
    # Normalize OpenAlex result to same format as CrossRef
    authors = []
    for a in best.get('authorships', []):
        author = a.get('author', {})
        name = author.get('display_name', '')
        if name:
            authors.append(name)
    venue_obj = best.get('primary_location', {}) or {}
    venue = (venue_obj.get('source') or {}).get('display_name', '')
    if not venue:
        locs = best.get('locations', []) or []
        venue = ', '.join([(s.get('source') or {}).get('display_name', '') for s in locs if (s.get('source') or {}).get('display_name')])[:100]
    return {
        'title': best.get('title', ''),
        'authors': authors,
        'year': str(best.get('publication_year', '')),
        'venue': venue,
        'doi': best.get('doi', ''),
    }


def crossref_by_doi(doi: str) -> dict | None:
    """Fetch CrossRef metadata for a DOI. Returns simplified dict."""
    # Strip https://doi.org/ or dx.doi.org/ prefix if present
    doi = doi.strip().replace('https://doi.org/', '').replace('http://doi.org/', '').replace('dx.doi.org/', '')
    if not doi:
        return None
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    data = _http_json(url, headers={"User-Agent": f"tvb-wiki-enricher (mailto:{_CONTACT_EMAIL})"})
    if not data or 'message' not in data:
        return None
    m = data['message']
    authors = []
    for a in m.get('author', []):
        parts = []
        if a.get('given'):
            parts.append(a['given'].strip())
        if a.get('family'):
            parts.append(a['family'].strip())
        if parts:
            authors.append(' '.join(parts))
    return {
        'title': m.get('title', [''])[0] if isinstance(m.get('title'), list) else m.get('title', ''),
        'authors': authors,
        'year': str(m.get('published-print', {}).get('date-parts', [['']])[0][0] or
                     m.get('published-online', {}).get('date-parts', [['']])[0][0] or
                     m.get('created', {}).get('date-parts', [['']])[0][0] or ''),
        'venue': (m.get('container-title', ['']) or [''])[0] if isinstance(m.get('container-title'), list) else m.get('container-title', ''),
        'doi': m.get('DOI', ''),
    }


def crossref_search(title: str) -> dict | None:
    """Search CrossRef by title string. Returns best match or None."""
    q = urllib.parse.quote(title)
    url = f"https://api.crossref.org/works?query.title={q}&rows=5&select=title,author,DOI,published-print,published-online,created,container-title&mailto={_CONTACT_EMAIL}"
    data = _http_json(url, headers={"User-Agent": f"tvb-wiki-enricher (mailto:{_CONTACT_EMAIL})"})
    if not data or 'message' not in data:
        return None
    items = data['message'].get('items', [])
    if not items:
        return None
    best = None
    best_score = 0
    t_lower = title.lower()
    for item in items:
        cand = (item.get('title', [''])[0] if isinstance(item.get('title'), list) else item.get('title', '')).lower()
        score = len(set(t_lower.split()) & set(cand.split())) / max(len(t_lower.split()), 1)
        if score > best_score:
            best_score = score
            best = item
    if not best or best_score < 0.3:
        return None
    authors = []
    for a in best.get('author', []):
        parts = []
        if a.get('given'): parts.append(a['given'].strip())
        if a.get('family'): parts.append(a['family'].strip())
        if parts:
            authors.append(' '.join(parts))
    return {
        'title': best.get('title', [''])[0] if isinstance(best.get('title'), list) else best.get('title', ''),
        'authors': authors,
        'year': str(best.get('published-print', {}).get('date-parts', [['']])[0][0] or
                     best.get('published-online', {}).get('date-parts', [['']])[0][0] or
                     best.get('created', {}).get('date-parts', [['']])[0][0] or ''),
        'venue': best.get('container-title', [''])[0] if isinstance(best.get('container-title'), list) else best.get('container-title', ''),
        'doi': best.get('DOI', ''),
    }


def parse_paper_frontmatter(path: str) -> tuple[dict, str]:
    """Extract frontmatter dict and body from a raw/papers/*.md file."""
    with open(path) as f:
        text = f.read()
    if not text.startswith('---'):
        return {}, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    try:
        import yaml
        fm = yaml.safe_load(parts[1])
    except Exception:
        fm = {}
    return fm if fm else {}, parts[2]


def build_bibtex(fm: dict) -> str:
    """Generate a BibTeX entry string from frontmatter dict."""
    authors = fm.get('authors', [])
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(',')]
    year = str(fm.get('year', ''))
    title = fm.get('title', 'Untitled')
    venue = fm.get('venue', '')
    doi = fm.get('doi', '')
    # Prefer venue as journal, but fallback to generic book
    first_author_surname = authors[0].split()[-1].lower() if authors else 'unknown'
    key = f"{first_author_surname}{year}{title.split()[0].lower()}"
    key = re.sub(r'[^a-z0-9]', '', key)[:20]

    if doi and 'journal' in venue.lower() or 'neuro' in venue.lower() or 'physics' in venue.lower():
        lines = [
            f"@article{{{key},",
            f'  title={{{title}}},',
        ]
        if authors:
            author_str = ' and '.join(authors)
            lines.append(f'  author={{"{author_str}"}},')
        if year:
            lines.append(f'  year={{{year}}},')
        if venue:
            lines.append(f'  journal={{{venue}}},')
        if doi:
            lines.append(f'  doi={{{doi}}},')
        lines.append('}')
    else:
        lines = [
            f"@book{{{key},",
            f'  title={{{title}}},',
        ]
        if authors:
            author_str = ' and '.join(authors)
            lines.append(f'  author={{"{author_str}"}},')
        if year:
            lines.append(f'  year={{{year}}},')
        if venue:
            lines.append(f'  publisher={{{venue}}},')
        if doi:
            lines.append(f'  doi={{{doi}}},')
        lines.append('}')
    return '\n'.join(lines)


def clean_yaml_string(s) -> str:
    """Quote a YAML string value if it contains colons or special chars."""
    # Coerce datetime / int / any non-string to string
    s = str(s) if s not in (None, '') else ''
    if not s or s in ('None', 'null', 'Null'):
        return '""'
    if ':' in s or '#' in s or s.strip().startswith('-') or '\n' in s or '"' in s or "," in s or "'" in s:
        return json.dumps(s)
    return s


def serialize_frontmatter(fm: dict) -> str:
    """Minimal YAML-like serialization (no external dep)."""
    lines = ['---']
    authors = fm.get('authors', [])
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(',')]
    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',')]
    for k, v in [('title', fm.get('title', '')),
                 ('created', str(fm.get('created', ''))),
                 ('updated', str(fm.get('updated', ''))),
                 ('type', fm.get('type', 'source')),
                 ('tags', tags),
                 ('authors', authors),
                 ('year', str(fm.get('year', ''))),
                 ('venue', str(fm.get('venue', ''))),
                 ('doi', str(fm.get('doi', ''))),
                 ('bibtex', fm.get('bibtex', ''))]:
        if k == 'tags' and v:
            lines.append(f'tags: [{" ,".join(v)}]')
        elif k == 'authors' and v:
            lines.append('authors:')
            for a in v:
                lines.append(f'  - {clean_yaml_string(a)}')
        elif k == 'bibtex' and v:
            lines.append('bibtex: |')
            for line in v.split('\n'):
                lines.append(f'  {line}')
        elif v:
            lines.append(f'{k}: {clean_yaml_string(v)}')
    lines.append('---')
    return '\n'.join(lines)


def enrich_file(path: str) -> bool:
    """Attempt to enrich one paper file. Returns True if updated."""
    fm, body = parse_paper_frontmatter(path)
    if not fm:
        return False

    title = fm.get('title', '')
    doi = fm.get('doi', '')

    # If already well-populated, skip
    authors = fm.get('authors', [])
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(',')]
    has_real_authors = bool(authors) and not any('unknown' in a.lower() or 'author' in a.lower() for a in authors)
    has_year = bool(fm.get('year'))
    has_venue = bool(fm.get('venue'))
    if has_real_authors and has_year and has_venue and doi:
        return False  # Already looks good

    found = None
    # Strategy 1: DOI via CrossRef (most reliable)
    if doi and doi.startswith('10.'):
        found = crossref_by_doi(doi)
        if found:
            print(f'  {path}: DOI CrossRef hit')
            time.sleep(0.5)

    # Strategy 2: Title via OpenAlex
    if not found and title:
        found = openalex_search(title)
        if found:
            print(f'  {path}: OpenAlex title hit')
            time.sleep(0.5)

    # Strategy 3: Title via CrossRef
    if not found and title:
        found = crossref_search(title)
        if found:
            print(f'  {path}: CrossRef title hit')
            time.sleep(0.5)

    if not found:
        return False

    # Merge in the found metadata where missing
    if found.get('title') and not title:
        fm['title'] = found['title']
    if found.get('authors'):
        fm['authors'] = found['authors']
    if found.get('year') and not has_year:
        fm['year'] = found['year']
    if found.get('venue') and not has_venue:
        fm['venue'] = found['venue']
    if found.get('doi') and not doi:
        fm['doi'] = found['doi']

    # Regenerate BibTeX
    fm['bibtex'] = build_bibtex(fm)

    # Write back
    full = serialize_frontmatter(fm) + '\n' + body
    with open(path, 'w') as f:
        f.write(full)
    return True


def main():
    paths = sorted(glob.glob(f'{RAW_DIR}/*.md'))
    updated = 0
    skipped = 0
    failed = 0
    for path in paths:
        try:
            if enrich_file(path):
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f'  ERROR on {path}: {e}')
            failed += 1
    print(f'\nSummary: {updated} enriched, {skipped} skipped/already-good, {failed} errors')


if __name__ == '__main__':
    main()
