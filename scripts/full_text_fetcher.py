#!/usr/bin/env python3
"""
Ralph FullTextFetcher Agent — fetches and extracts full-text PDFs for raw papers.

Strategy:
  1. Scan raw/papers/ for papers lacking a fulltext companion file.
  2. Score papers by TVB relevance (foundational > application > general).
  3. Attempt PDF acquisition via (a) Unpaywall (DOI), (b) arXiv direct, (c) Semantic Scholar OA link.
  4. Extract plain text with pdftotext.
  5. Store in raw/papers/fulltext/{slug}.txt and record metadata in meta/fulltext_progress.json.

The extracted text is then consumed by Matcher/Improver/DeepResearch prompts
to enrich literature background and improve signal-to-noise.
"""
import os
import sys
import re
import json
import time
import hashlib
import subprocess
import datetime
import urllib.request
import urllib.parse
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, RAW_PAPERS_DIR, META_DIR,
    append_log, git_commit, run_pi, WRITER_MODEL,
)

log = get_logger("FullTextFetcher")

# ── Paths ──────────────────────────────────────────────────────────────
FULLTEXT_DIR = os.path.join(RAW_PAPERS_DIR, "fulltext")
PROGRESS_FILE = os.path.join(META_DIR, "fulltext_progress.json")
TEMP_PDF_DIR = os.path.join(META_DIR, "temp_pdfs")

# Unpaywall requires an email parameter (polite-use policy)
UNPAYWALL_EMAIL = os.environ.get("UNPAYWALL_EMAIL", "ralph@tvb-wiki.local")

# Rate-limiting
UNPAYWALL_DELAY = 1.0   # seconds between Unpaywall calls
SEMANTIC_SCHOLAR_DELAY = 0.5
ARXIV_DELAY = 3.0

# Per-cycle caps
MAX_FETCH_PER_CYCLE = 20
MAX_PDF_SIZE_MB = 50

# ── Progress tracking ──────────────────────────────────────────────────

def load_progress() -> dict:
    """Load or init progress tracker."""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "fetched": {},      # slug -> {"doi","source","pdf_url","fetched_at","bytes","words"}
        "failed": {},       # slug -> {"reason","attempted_at"}
        "skipped": {},      # slug -> {"reason","marked_at"}
    }


def save_progress(progress: dict):
    os.makedirs(META_DIR, exist_ok=True)
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, default=str)


# ── Relevance scoring ──────────────────────────────────────────────────

FOUNDATIONAL_TERMS = [
    "the virtual brain", "tvb", "whole-brain model", "whole brain model",
    "neural mass model", "connectome-based model", "brain network simulation",
    "mean-field", "jansen-rit", "wilson-cowan", "wong-wang", "epileptor",
    "stefanescu-jirsa", "larter-breakspear", "jirsa", "breakspear", " Deco ",
    "schirner", "woodman", "mcdonald", "knock", "proix", "gerstner",
]

APPLICATION_TERMS = [
    "epilepsy", "seizure", "stroke", "traumatic brain injury", "tbi",
    "alzheimer", "parkinson", "dementia", "aging", "development",
    "schizophrenia", "autism", "depression", "anxiety", "resting-state",
    "sleep", "consciousness", "coma", "anesthesia", "bci", "brain-computer",
    "neurofeedback", "personalized medicine", "precision medicine",
]

GENERIC_NEURO_TERMS = [
    "fmri", "eeg", "meg", "dti", "diffusion", "tractography",
    "functional connectivity", "structural connectivity", "effective connectivity",
    "graph theory", "network analysis", "dynamical system", "bifurcation",
    "oscillation", "synchronization", "neuroimaging", "computational neuroscience",
]


def score_paper_relevance(filepath: str) -> tuple[int, str]:
    """
    Score a paper's TVB relevance. Returns (score, tier).
    tier in {"foundational", "application", "generic", "low"}
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read().lower()
    except Exception:
        return (0, "low")

    # Remove markdown noise for cleaner matching
    text = re.sub(r'[#*\-\[\]\(\)\|]', ' ', text)

    fnd_count = sum(1 for t in FOUNDATIONAL_TERMS if t.lower() in text)
    app_count = sum(1 for t in APPLICATION_TERMS if t.lower() in text)
    gen_count = sum(1 for t in GENERIC_NEURO_TERMS if t.lower() in text)

    # Citation bonus
    cit_match = re.search(r'\*\*citations\*\*:\s*(\d+)', text)
    cit_bonus = int(cit_match.group(1)) // 10 if cit_match else 0

    # Year bonus (newer papers might be more relevant for applications)
    year_match = re.search(r'\*\*year\*\*:\s*(\d{4})', text)
    year = int(year_match.group(1)) if year_match else 2000
    year_bonus = max(0, (year - 2010) // 5)

    score = fnd_count * 10 + app_count * 5 + gen_count * 2 + cit_bonus + year_bonus

    if fnd_count >= 2:
        tier = "foundational"
    elif fnd_count >= 1 or app_count >= 2:
        tier = "application"
    elif gen_count >= 3 or app_count >= 1:
        tier = "generic"
    else:
        tier = "low"

    return (score, tier)


# ── PDF acquisition ────────────────────────────────────────────────────

def _urlopen_json(url: str, headers: dict = None, timeout: int = 30) -> dict:
    """Fetch URL and return parsed JSON."""
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        log.debug("JSON fetch failed for %s: %s", url[:80], e)
        return {}


def fetch_pdf_url_unpaywall(doi: str) -> str | None:
    """Query Unpaywall API for best OA PDF URL."""
    if not doi:
        return None
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={UNPAYWALL_EMAIL}"
    data = _urlopen_json(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
    best = data.get('best_oa_location')
    if best:
        pdf_url = best.get('url_for_pdf') or best.get('pdf_url')
        if pdf_url:
            return pdf_url
    # Fallback: any OA location with PDF
    for loc in data.get('oa_locations', []):
        pdf_url = loc.get('url_for_pdf') or loc.get('pdf_url')
        if pdf_url:
            return pdf_url
    return None


def fetch_pdf_url_semantic_scholar(s2_id: str) -> str | None:
    """Query S2 API for openAccessPdf url."""
    if not s2_id:
        return None
    url = (
        f"https://api.semanticscholar.org/graph/v1/paper/{s2_id}"
        f"?fields=openAccessPdf"
    )
    data = _urlopen_json(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
    oa = data.get('openAccessPdf')
    if oa:
        return oa.get('url')
    return None


def arxiv_pdf_url(arxiv_id: str) -> str | None:
    if not arxiv_id:
        return None
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"


# ── DOI lookup ─────────────────────────────────────────────────────────

def lookup_doi_crossref(title: str, authors: list[str]) -> str | None:
    """Query Crossref API for DOI by title + author. Returns DOI or None."""
    if not title:
        return None
    # Build query: title + first author surname if available
    query_parts = [title]
    if authors:
        first_author = authors[0].split()[-1]  # last name
        query_parts.append(first_author)
    query = ' '.join(query_parts)

    params = urllib.parse.urlencode({
        'query': query,
        'rows': 5,
        'select': 'DOI,title,author,score',
    })
    url = f"https://api.crossref.org/works?{params}"
    data = _urlopen_json(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})

    items = data.get('message', {}).get('items', [])
    if not items:
        return None

    # Score matches by title similarity
    best_doi = None
    best_score = 0.0
    title_lower = title.lower()
    for item in items:
        item_title = item.get('title', [''])[0].lower() if isinstance(item.get('title'), list) else str(item.get('title', '')).lower()
        # Simple matching: check if query title is substantially contained in result
        if title_lower in item_title or item_title in title_lower:
            score = item.get('score', 0)
            if score > best_score:
                best_score = score
                best_doi = item.get('DOI')

    return best_doi


def lookup_doi_semantic_scholar(title: str, authors: list[str]) -> str | None:
    """Query Semantic Scholar search API for DOI by title."""
    if not title:
        return None
    params = urllib.parse.urlencode({
        'query': title,
        'limit': 5,
        'fields': 'title,externalIds',
    })
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{params}"
    data = _urlopen_json(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})

    for item in data.get('data', []):
        item_title = item.get('title', '').lower()
        if title.lower() in item_title or item_title in title.lower():
            ext_ids = item.get('externalIds', {})
            doi = ext_ids.get('DOI', '')
            if doi:
                return doi
    return None


def lookup_doi_openalex(title: str, authors: list[str]) -> str | None:
    """Query OpenAlex API for DOI by title."""
    if not title:
        return None
    params = urllib.parse.urlencode({
        'search': title,
        'per-page': 5,
    })
    url = f"https://api.openalex.org/works?{params}"
    data = _urlopen_json(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})

    for item in data.get('results', []):
        item_title = item.get('display_name', '').lower()
        if title.lower() in item_title or item_title in title.lower():
            doi = item.get('doi', '')
            if doi:
                # OpenAlex returns full URL like https://doi.org/10.xxxx/yyyy
                if doi.startswith('https://doi.org/'):
                    doi = doi.replace('https://doi.org/', '')
                return doi
    return None


def update_paper_doi(filepath: str, doi: str) -> bool:
    """Update a raw paper markdown file to add the DOI. Returns True if modified."""
    if not doi or not os.path.exists(filepath):
        return False
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if DOI already present
        if '**DOI**' in content:
            return False

        # Insert DOI line after the ID line (early in the file)
        id_match = re.search(r'(\*\*ID\*\*:\s*.+\n)', content)
        if id_match:
            insert_pos = id_match.end()
            new_content = content[:insert_pos] + f"**DOI**: {doi}\n" + content[insert_pos:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            log.info("Annotated DOI %s in %s", doi, os.path.basename(filepath))
            return True

        # Fallback: insert after Source line
        src_match = re.search(r'(\*\*Source\*\*:\s*.+\n)', content)
        if src_match:
            insert_pos = src_match.end()
            new_content = content[:insert_pos] + f"**DOI**: {doi}\n" + content[insert_pos:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            log.info("Annotated DOI %s in %s", doi, os.path.basename(filepath))
            return True

        return False
    except Exception as e:
        log.warn("Failed to update DOI in %s: %s", filepath, e)
        return False


# ── PDF download ──────────────────────────────────────────────────────

def download_pdf(url: str, dest_path: str, max_bytes: int = MAX_PDF_SIZE_MB * 1024 * 1024) -> bool:
    """Download PDF from url to dest_path with size cap. Returns True on success."""
    log.info("Downloading PDF: %s", url[:100])
    req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read(max_bytes + 1)
            if len(data) > max_bytes:
                log.warn("PDF too large (> %d MB): %s", MAX_PDF_SIZE_MB, url[:80])
                return False
            with open(dest_path, 'wb') as f:
                f.write(data)
        return True
    except urllib.error.HTTPError as e:
        log.warn("PDF download HTTP %d: %s", e.code, url[:80])
        return False
    except Exception as e:
        log.warn("PDF download failed: %s — %s", url[:80], e)
        return False


# ── Main fetch logic for a single paper ────────────────────────────────
def extract_text_with_pdftotext(pdf_path: str, txt_path: str) -> bool:
    """Run pdftotext -layout on pdf_path. Returns True if text was extracted."""
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", pdf_path, txt_path],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            log.warn("pdftotext failed: %s", result.stderr.strip()[:200])
            return False
        # Verify non-empty
        if os.path.getsize(txt_path) < 100:
            log.warn("pdftotext produced almost empty output for %s", os.path.basename(pdf_path))
            return False
        return True
    except FileNotFoundError:
        log.error("pdftotext not found on system!")
        return False
    except Exception as e:
        log.warn("pdftotext exception: %s", e)
        return False


# ── Paper parsing helpers ──────────────────────────────────────────────

def parse_paper_markdown(filepath: str) -> dict:
    """Parse the raw paper markdown into a dict of metadata + abstract."""
    result = {
        'slug': os.path.basename(filepath)[:-3],
        'title': '',
        'doi': '',
        'arxiv_id': '',
        's2_id': '',
        'url': '',
        'year': '',
        'authors': '',
        'venue': '',
        'citations': 0,
        'abstract': '',
    }
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return result

    # Extract YAML frontmatter DOI first (manually curated papers)
    fm_text = ""
    if content.startswith('---'):
        fm_end = content.find('---', 3)
        if fm_end != -1:
            fm_text = content[3:fm_end]
            # Look for doi: in frontmatter
            fm_doi_match = re.search(r'^doi:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
            if fm_doi_match:
                result['doi'] = fm_doi_match.group(1).strip().strip('"\'')
                # Strip https://doi.org/ prefix if present
                if result['doi'].startswith('https://doi.org/'):
                    result['doi'] = result['doi'].replace('https://doi.org/', '')
            # Look for arxiv_id in frontmatter
            fm_arxiv_match = re.search(r'^arxiv_id?:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE | re.IGNORECASE)
            if fm_arxiv_match:
                result['arxiv_id'] = fm_arxiv_match.group(1).strip().strip('"\'')
            # Look for url in frontmatter
            fm_url_match = re.search(r'^url:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
            if fm_url_match:
                result['url'] = fm_url_match.group(1).strip().strip('"\'')
            # Look for authors in frontmatter (YAML list format: - Name)
            fm_authors = re.findall(r'^(?:-\s*(.+)|^authors?:\s*\n(?:\s+-\s*(.+)\n?)+)', fm_text, re.MULTILINE)
            if fm_authors:
                # Extract author names from YAML list
                yaml_list = re.findall(r'^\s+-\s*(.+)$', fm_text, re.MULTILINE)
                if yaml_list:
                    result['authors'] = [a.strip().strip('"\'') for a in yaml_list]
            # Look for title in frontmatter
            fm_title = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
            if fm_title:
                result['title'] = fm_title.group(1).strip().strip('"\'')
            # Look for year in frontmatter
            fm_year = re.search(r'^year:\s*(\d{4})\s*$', fm_text, re.MULTILINE)
            if fm_year:
                result['year'] = fm_year.group(1)
            # Look for venue in frontmatter
            fm_venue = re.search(r'^venue:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
            if fm_venue:
                result['venue'] = fm_venue.group(1).strip().strip('"\'')

    # Extract fields with regex from body (fallback)
    m = re.search(r'^# (.+)$', content, re.MULTILINE)
    if m:
        result['title'] = m.group(1).strip()

    for key in ['doi', 'url', 'year', 'authors', 'venue']:
        m = re.search(rf'\*\*{key.capitalize()}\*\*:\s*(.+)', content, re.IGNORECASE)
        if m:
            result[key] = m.group(1).strip()

    m = re.search(r'\*\*ID\*\*:\s*(.+)', content)
    if m:
        raw_id = m.group(1).strip()
        if raw_id.startswith('0') or len(raw_id) > 20:
            result['s2_id'] = raw_id

    m = re.search(r'\*\*Citations\*\*:\s*(\d+)', content)
    if m:
        result['citations'] = int(m.group(1))

    m = re.search(r'## Abstract\s*\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if m:
        result['abstract'] = m.group(1).strip()

    # Derive arxiv_id from slug if arxiv
    if result['slug'].startswith('arxiv-'):
        result['arxiv_id'] = result['slug'].replace('arxiv-', '')
    # Or from URL
    if not result['arxiv_id'] and 'arxiv.org' in result['url']:
        m = re.search(r'arxiv\.org/abs/(\d+\.\d+)', result['url'])
        if m:
            result['arxiv_id'] = m.group(1)

    return result


# ── Main fetch logic for a single paper ────────────────────────────────

def try_fetch_fulltext(filepath: str, progress: dict) -> dict:
    """
    Attempt to fetch full text for a single paper.
    Returns {"status": "success|failed|skipped", "details": {...}}
    """
    slug = os.path.basename(filepath)[:-3]
    meta = parse_paper_markdown(filepath)

    # Skip if already done
    if slug in progress.get("fetched", {}):
        return {"status": "skipped", "details": {"reason": "already fetched"}}
    if slug in progress.get("failed", {}):
        # Retry failed after 7 days
        fail_info = progress["failed"][slug]
        attempted = fail_info.get("attempted_at", "")
        try:
            dt = datetime.datetime.fromisoformat(attempted)
            if (datetime.datetime.now() - dt).days < 7:
                return {"status": "skipped", "details": {"reason": "recently failed"}}
        except Exception:
            pass

    # Try to look up missing DOI before giving up
    if not meta['doi'] and not meta['arxiv_id'] and not meta['s2_id']:
        log.info("[%s] No identifiers — attempting DOI lookup...", slug)
        found_doi = None
        # Try Crossref first
        found_doi = lookup_doi_crossref(meta['title'], meta['authors'])
        if found_doi:
            log.info("  Crossref found DOI: %s", found_doi)
        else:
            # Fallback to Semantic Scholar
            time.sleep(0.5)
            found_doi = lookup_doi_semantic_scholar(meta['title'], meta['authors'])
            if found_doi:
                log.info("  Semantic Scholar found DOI: %s", found_doi)
            else:
                # Fallback to OpenAlex
                time.sleep(0.5)
                found_doi = lookup_doi_openalex(meta['title'], meta['authors'])
                if found_doi:
                    log.info("  OpenAlex found DOI: %s", found_doi)
        if found_doi:
            meta['doi'] = found_doi
            update_paper_doi(filepath, found_doi)
        else:
            progress["skipped"][slug] = {"reason": "no identifiers and DOI lookup failed", "marked_at": datetime.datetime.now().isoformat()}
            return {"status": "skipped", "details": {"reason": "no doi/arxiv/s2_id and DOI lookup failed"}}

    os.makedirs(TEMP_PDF_DIR, exist_ok=True)
    os.makedirs(FULLTEXT_DIR, exist_ok=True)
    pdf_path = os.path.join(TEMP_PDF_DIR, f"{slug}.pdf")
    txt_path = os.path.join(FULLTEXT_DIR, f"{slug}.txt")

    pdf_url = None
    source_used = None

    # Strategy 1: arXiv direct (most reliable)
    if meta['arxiv_id']:
        pdf_url = arxiv_pdf_url(meta['arxiv_id'])
        if pdf_url:
            source_used = "arxiv"
            time.sleep(ARXIV_DELAY)
            if download_pdf(pdf_url, pdf_path):
                if extract_text_with_pdftotext(pdf_path, txt_path):
                    word_count = len(open(txt_path, 'r', encoding='utf-8', errors='ignore').read().split())
                    progress["fetched"][slug] = {
                        "doi": meta['doi'],
                        "source": source_used,
                        "pdf_url": pdf_url,
                        "fetched_at": datetime.datetime.now().isoformat(),
                        "bytes": os.path.getsize(pdf_path),
                        "words": word_count,
                    }
                    os.remove(pdf_path)
                    return {"status": "success", "details": {"words": word_count, "source": source_used}}

    # Strategy 2: Unpaywall (DOI-based OA discovery)
    if meta['doi'] and not pdf_url:
        time.sleep(UNPAYWALL_DELAY)
        pdf_url = fetch_pdf_url_unpaywall(meta['doi'])
        if pdf_url:
            source_used = "unpaywall"
            if download_pdf(pdf_url, pdf_path):
                if extract_text_with_pdftotext(pdf_path, txt_path):
                    word_count = len(open(txt_path, 'r', encoding='utf-8', errors='ignore').read().split())
                    progress["fetched"][slug] = {
                        "doi": meta['doi'],
                        "source": source_used,
                        "pdf_url": pdf_url,
                        "fetched_at": datetime.datetime.now().isoformat(),
                        "bytes": os.path.getsize(pdf_path),
                        "words": word_count,
                    }
                    os.remove(pdf_path)
                    return {"status": "success", "details": {"words": word_count, "source": source_used}}

    # Strategy 3: Semantic Scholar open access link
    if meta['s2_id'] and not pdf_url:
        time.sleep(SEMANTIC_SCHOLAR_DELAY)
        pdf_url = fetch_pdf_url_semantic_scholar(meta['s2_id'])
        if pdf_url:
            source_used = "semantic-scholar-oa"
            if download_pdf(pdf_url, pdf_path):
                if extract_text_with_pdftotext(pdf_path, txt_path):
                    word_count = len(open(txt_path, 'r', encoding='utf-8', errors='ignore').read().split())
                    progress["fetched"][slug] = {
                        "doi": meta['doi'],
                        "source": source_used,
                        "pdf_url": pdf_url,
                        "fetched_at": datetime.datetime.now().isoformat(),
                        "bytes": os.path.getsize(pdf_path),
                        "words": word_count,
                    }
                    os.remove(pdf_path)
                    return {"status": "success", "details": {"words": word_count, "source": source_used}}

    # All strategies exhausted
    progress["failed"][slug] = {
        "reason": "no open-access pdf found",
        "doi": meta['doi'],
        "arxiv_id": meta['arxiv_id'],
        "s2_id": meta['s2_id'],
        "attempted_at": datetime.datetime.now().isoformat(),
    }
    # Clean up temp PDF if it exists but failed extraction
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    return {"status": "failed", "details": {"reason": "no OA PDF available"}}


# ── Full text consumption helper (for other agents) ──────────────────────

def get_fulltext(slug: str, max_chars: int = 15000) -> str | None:
    """
    Read extracted full text for a paper slug, if available.
    Returns up to max_chars (default 15k ~ 4k tokens, fits comfortably in prompts).
    """
    txt_path = os.path.join(FULLTEXT_DIR, f"{slug}.txt")
    if not os.path.exists(txt_path):
        return None
    try:
        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read(max_chars + 1)
        if len(text) > max_chars:
            # Smart truncation: try to end at a paragraph boundary
            truncated = text[:max_chars]
            last_para = truncated.rfind('\n\n')
            if last_para > max_chars * 0.8:
                truncated = truncated[:last_para]
            text = truncated + "\n\n[... full text truncated ...]"
        return text
    except Exception:
        return None


def enrich_prompt_with_fulltext(slug: str, base_prompt: str, max_chars: int = 12000) -> str:
    """
    Append full text excerpt to a prompt if available.
    Used by Matcher/Improver/DeepResearch before calling run_pi.
    """
    ft = get_fulltext(slug, max_chars=max_chars)
    if not ft:
        return base_prompt
    return (
        base_prompt.rstrip()
        + "\n\n## FULL TEXT EXCERPT FROM SOURCE PAPER\n\n"
        + ft
        + "\n\n## END OF FULL TEXT EXCERPT\n"
    )


# ── Cycle runner ───────────────────────────────────────────────────────

def run_full_text_cycle():
    """Run one full-text fetch cycle. Returns number of new full texts fetched."""
    log.info("Starting FullTextFetcher cycle")

    progress = load_progress()
    os.makedirs(FULLTEXT_DIR, exist_ok=True)
    os.makedirs(TEMP_PDF_DIR, exist_ok=True)

    # Collect all paper files
    paper_files = []
    if os.path.isdir(RAW_PAPERS_DIR):
        for fn in os.listdir(RAW_PAPERS_DIR):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(RAW_PAPERS_DIR, fn)
            if not os.path.isfile(fp):
                continue
            paper_files.append(fp)

    log.info("Found %d total paper files", len(paper_files))

    # Score and filter
    scored = []
    for fp in paper_files:
        slug = os.path.basename(fp)[:-3]
        # Skip already fetched or recently failed
        if slug in progress.get("fetched", {}):
            continue
        fail_info = progress.get("failed", {}).get(slug)
        if fail_info:
            attempted = fail_info.get("attempted_at", "")
            try:
                dt = datetime.datetime.fromisoformat(attempted)
                if (datetime.datetime.now() - dt).days < 7:
                    continue
            except Exception:
                pass

        score, tier = score_paper_relevance(fp)
        scored.append((score, tier, fp, slug))

    # Sort: foundational first, then by score desc
    tier_order = {"foundational": 0, "application": 1, "generic": 2, "low": 3}
    scored.sort(key=lambda x: (tier_order.get(x[1], 99), -x[0]))

    log.info("%d papers need full text (%d foundational, %d application, %d generic, %d low)",
             len(scored),
             sum(1 for s in scored if s[1] == "foundational"),
             sum(1 for s in scored if s[1] == "application"),
             sum(1 for s in scored if s[1] == "generic"),
             sum(1 for s in scored if s[1] == "low"))

    fetched_count = 0
    for score, tier, fp, slug in scored[:MAX_FETCH_PER_CYCLE]:
        log.info("[%s | score=%d] Trying %s ...", tier, score, slug)
        result = try_fetch_fulltext(fp, progress)
        save_progress(progress)

        if result["status"] == "success":
            fetched_count += 1
            words = result["details"].get("words", 0)
            src = result["details"].get("source", "unknown")
            log.info("  ✅ Fetched %d words from %s (%s)", words, src, slug)
        elif result["status"] == "failed":
            log.info("  ❌ Failed: %s", result["details"].get("reason", ""))
        else:
            log.info("  ⏭ Skipped: %s", result["details"].get("reason", ""))

        # Brief pause between papers
        time.sleep(0.5)

    if fetched_count > 0:
        msg = f"FullTextFetcher: fetched {fetched_count} new full texts ({len(progress.get('fetched', {}))} total in corpus)"
        git_commit(msg)
        append_log(msg)
        log.info("Committed: %s", msg)
    else:
        log.info("No new full texts fetched this cycle.")

    log.info("Cycle complete. %d fetched this run. %d total in corpus. %d failed. %d skipped.",
             fetched_count,
             len(progress.get("fetched", {})),
             len(progress.get("failed", {})),
             len(progress.get("skipped", {})))
    return fetched_count


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    run_full_text_cycle()
