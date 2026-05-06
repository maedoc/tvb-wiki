#!/usr/bin/env python3
"""
Citation Verify — Shared library for verifying academic citations.

Pure stdlib Python, no external dependencies.

Usage:
    from citation_verify import verify_doi, verify_title, parse_inline_citations

Design choices:
  - 150ms sleep between requests (polite pool)
  - Falls back from CrossRef (DOI) → OpenAlex (title search) → None
  - Returns normalized dicts for easy comparison
  - Persistent JSON cache for OpenAlex lookups (~week TTL)
"""
import urllib.request
import urllib.parse
import urllib.error
import re
import time
import json
import os
from typing import Any

_USER_AGENT = "tvb-wiki-citation-verify (mailto:agent@local)"
_POLITE_SLEEP = 0.15  # seconds between API calls

# ── Persistent cache ───────────────────────────────────────────────────

_CACHE_DIR = os.path.expanduser("~/.cache/tvb-wiki")
_CACHE_FILE = os.path.join(_CACHE_DIR, "citation_cache.json")
_CACHE_TTL_DAYS = 7


def _load_cache() -> dict:
    """Load cached OpenAlex/CrossRef responses."""
    if not os.path.exists(_CACHE_FILE):
        return {}
    try:
        with open(_CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)
        # Purge stale entries
        now = time.time()
        stale = [
            k
            for k, v in cache.items()
            if not isinstance(v, dict) or now - v.get("_ts", 0) > _CACHE_TTL_DAYS * 86400
        ]
        for k in stale:
            del cache[k]
        return cache
    except (json.JSONDecodeError, OSError):
        return {}


def _save_cache(cache: dict) -> None:
    """Write cache to disk."""
    try:
        os.makedirs(_CACHE_DIR, exist_ok=True)
        with open(_CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
    except OSError:
        pass


def _cache_key(query_type: str, query: str) -> str:
    """Build a deterministic cache key."""
    return f"{query_type}:{query.lower().strip()}"


def _cached_call(query_type: str, query: str, fn: Any) -> dict | None:
    """Return cached result or call fn, cache, and return."""
    cache = _load_cache()
    key = _cache_key(query_type, query)
    if key in cache:
        return cache[key]
    result = fn()
    if result is not None:
        result["_ts"] = time.time()
        cache[key] = result
        _save_cache(cache)
    return result


# ── API lookup helpers ─────────────────────────────────────────────────

def _http_json(url: str, headers: dict | None = None, timeout: int = 20) -> dict | None:
    """GET JSON and return parsed dict, or None on failure."""
    if headers is None:
        headers = {}
    headers.setdefault("User-Agent", _USER_AGENT)
    headers.setdefault("Accept", "application/json")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            return json.loads(data)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None


def verify_doi(doi: str) -> dict | None:
    """
    Lookup a DOI via CrossRef and return normalized metadata.
    Returns None if not found or malformed.
    Cache backed.
    """
    doi = _clean_doi(doi.strip())
    if not doi or not doi.startswith("10."):
        return None

    def _lookup():
        cfr = _http_json(
            f"https://api.crossref.org/works/{urllib.parse.quote(doi)}",
            timeout=10,
        )
        if not cfr:
            return None
        msg = cfr.get("message", {})
        return {
            "title": " ".join(msg.get("title", []) or msg.get("container-title", []) or [""]),
            "authors": [
                f"{a.get('given', '')} {a.get('family', '')}".strip()
                for a in msg.get("author", [])
                if a.get("family")
            ][:10],
            "year": str(msg.get("published-print", {}).get("date-parts", [[""]])[0][0]
            or msg.get("published-online", {}).get("date-parts", [[""]])[0][0]
            or ""
            ),
            "venue": ", ".join(
                msg.get("container-title", []) or msg.get("short-container-title", []) or []
            ),
            "doi": doi,
        }

    result = _cached_call("doi", doi, _lookup)
    return dict(result) if result else None


def verify_title(title: str, extra_wait: float = _POLITE_SLEEP) -> dict | None:
    """
    Search OpenAlex by title and return normalized metadata for the top result.
    Cache backed.
    """
    title = title.strip()
    if not title or len(title) < 10:
        return None
    q = urllib.parse.quote(title)

    def _lookup():
        time.sleep(extra_wait)  # politeness
        ol = _http_json(
            f"https://api.openalex.org/works?search={q}&per-page=1",
            timeout=25,
        )
        if not ol or not ol.get("results"):
            return None
        r = ol["results"][0]
        return {
            "title": r.get("title", ""),
            "authors": [
                f"{a.get('raw_author_name', a.get('author', {}).get('display_name', ''))}".strip()
                for a in r.get("authorships", [])
            ][:10],
            "year": str(r.get("publication_year", "")),
            "venue": r.get("primary_location", {}).get("source", {}).get("display_name", "")
            if r.get("primary_location")
            else "",
            "doi": (r.get("doi") or "").replace("https://doi.org/", ""),
        }

    result = _cached_call("title", title, _lookup)
    return dict(result) if result else None


def verify_citation(citation: dict, stub_index: dict) -> dict:
    """
    Cross-check a single parsed citation against local stubs + external DB.

    Returns {"status": "VERIFIED" | "NOT_FOUND", "metadata": ..., "source": ...}
    """
    result = {"status": "NOT_FOUND", "metadata": None, "source": None, "raw_stub_path": None}

    # 1) DOI path
    if citation.get("type") == "doi":
        doi = citation.get("doi", "").strip()
        stub = stub_index.get(doi, stub_index.get(f"doi:{doi}"))
        if stub:
            # stub present
            result["raw_stub_path"] = stub
            stub_doi = _extract_doi_from_stub(stub)
            if stub_doi:
                ext = verify_doi(stub_doi)
            else:
                ext = verify_title(_extract_title_from_stub(stub))
            if ext:
                if _title_similarity(_extract_title_from_stub(stub), ext.get("title", "")) > 0.5:
                    result["status"] = "VERIFIED"
                    result["metadata"] = ext
                    result["source"] = "crossref_doi"
                else:
                    result["metadata"] = ext
                    result["source"] = "crossref_doi"
            else:
                result["source"] = "stub_no_ext"
        else:
            ext = verify_doi(doi)
            if ext:
                result["status"] = "VERIFIED"
                result["metadata"] = ext
                result["source"] = "crossref_doi"
            else:
                result["status"] = "NOT_FOUND"
                result["source"] = None
            return result

    # 2) Author-year path
    if citation.get("type") == "author_year":
        author = citation.get("author", "").strip()
        year = citation.get("year", "").strip()
        key = f"{author.split()[-1].lower()}-{year}"
        stub = stub_index.get(key)
        if stub:
            result["raw_stub_path"] = stub
            stub_doi = _extract_doi_from_stub(stub)
            if stub_doi:
                ext = verify_doi(stub_doi)
            else:
                ext = verify_title(_extract_title_from_stub(stub))
            if ext and _title_similarity(_extract_title_from_stub(stub), ext.get("title", "")) > 0.5:
                result["status"] = "VERIFIED"
                result["metadata"] = ext
            elif ext:
                result["metadata"] = ext
        else:
            # No stub — could search by author+year but that's noisy
            result["source"] = "no_stub"
        return result

    return result


def _extract_title_from_stub(path: str) -> str:
    """Extract title from raw stub (YAML frontmatter or body-text fallback)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read(2048)
    except OSError:
        return ""
    # YAML frontmatter
    m = re.search(r"^title:\s*['\"]?(.*?)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip("'\"")
    # Body-text format: # Title at first heading
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return ""


def _extract_doi_from_stub(path: str) -> str | None:
    """Extract DOI from raw stub (YAML frontmatter or body-text fallback)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read(2048)
    except OSError:
        return None
    # YAML frontmatter
    m = re.search(r"^doi:\s*(\S+)", text, re.MULTILINE)
    if m:
        d = m.group(1).strip().strip("'\"")
        if d.startswith("10."):
            return d
    # Body-text format: **DOI**: 10.xxxx
    m = re.search(r"\*\*DOI\*\*:\s*10\.\S+", text)
    if m:
        d = m.group(0).split(":", 1)[1].strip()
        return d if d.startswith("10.") else None
    return None


def _extract_authors_from_stub(path: str) -> list[str]:
    """Extract author list from raw stub (YAML frontmatter or body-text fallback)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read(2048)
    except OSError:
        return []
    # YAML frontmatter (list format: - Author Name)
    authors = re.findall(r"^-\s*(.+)$", text, re.MULTILINE)
    if authors:
        return [a.strip().strip("'\"") for a in authors]
    # Body-text format: **Authors**: Author1, Author2, ...
    m = re.search(r"\*\*Authors\*\*:\s*(.+)", text, re.MULTILINE)
    if m:
        raw = m.group(1).strip()
        return [a.strip() for a in raw.split(",") if a.strip()]
    return []


def _title_similarity(a: str, b: str) -> float:
    """Simple token-overlap similarity [0, 1]."""
    sa = set(re.sub(r"[^a-zA-Z0-9]", " ", a.lower()).split())
    sb = set(re.sub(r"[^a-zA-Z0-9]", " ", b.lower()).split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def build_stub_index(raw_papers_dir: str) -> dict:
    """
    Build a lookup dict for raw stubs indexed by DOI, author_year, or title.
    """
    index = {}
    for fname in os.listdir(raw_papers_dir):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(raw_papers_dir, fname)
        title = _extract_title_from_stub(fpath)
        doi = _extract_doi_from_stub(fpath)
        authors = _extract_authors_from_stub(fpath)

        # Index by DOI
        if doi:
            index[doi] = fpath
            index[f"doi:{doi}"] = fpath

        # Index by author_year (from filename slug like "schirner-2018")
        author_year = None
        slug = os.path.splitext(fname)[0]
        parts = slug.rsplit("-", 1)
        if len(parts) == 2 and parts[1].isdigit():
            author_year = slug
        if author_year:
            index[author_year] = fpath

        # Index by first author + year from extracted authors
        if authors:
            first_last = authors[0].split()[-1].lower()
            # Try to get year from title or filename
            year_match = re.search(r'\b(19\d{2}|20\d{2})\b', title)
            if year_match:
                key = f"{first_last}-{year_match.group(1)}"
                index[key] = fpath
            # Also try year from filename
            parts = slug.rsplit("-", 1)
            if len(parts) == 2 and parts[1].isdigit():
                key = f"{first_last}-{parts[1]}"
                index[key] = fpath

        # Index by lowercased title keywords for fuzzy matching
        if title:
            key = re.sub(r"[^a-z0-9]", "", title.lower())[:40]
            if key:
                index[key] = fpath

    return index


def parse_inline_citations(text: str) -> list[dict]:
    """
    Extract inline citation mentions from markdown text.
    Handles wikilink-citations like [[gustavo-deco|Deco]] (2008).
    Returns list of dicts: [{"text": "Gardiner (2009)", "type": "author_year"}, ...]
    """
    results = []
    if not text:
        return results

    # Preprocess: strip wikilink notation [[link|Display]] → Display
    # so that "[[gustavo-deco|Deco]] (2008)" becomes "Deco (2008)"
    clean_text = re.sub(r"\[\[[^\]]+\|([^\]]+)\]\]", r"\1", text)
    # Also strip plain wikilinks [[Display]] → Display
    clean_text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", clean_text)

    # Pattern 1: Author (Year) — e.g., "Deco (2008)", "Tuckwell (1988)", "Breakspear et al. (2003)"
    for m in re.finditer(
        r"\b([A-Z][a-zA-Z\-'']+(?:\s+[A-Z][a-zA-Z\-'']+)*?(?:\s+et\s+al\.?)?)\s*\((\d{4})[a-z]?\)",
        clean_text,
    ):
        results.append({
            "text": m.group(0),
            "type": "author_year",
            "author": m.group(1).strip(),
            "year": m.group(2),
        })

    # Pattern 2: bare [^N] reference numbers (already linked via YAML sources)
    for m in re.finditer(r"\[\^(\d+)\]", clean_text):
        results.append({
            "text": m.group(0),
            "type": "superscript",
            "num": int(m.group(1)),
        })

    # Pattern 3: bare [N] reference numbers
    for m in re.finditer(r"(?<!\[)\[(\d+)\](?!\()", clean_text):
        results.append({
            "text": m.group(0),
            "type": "bracket_num",
            "num": int(m.group(1)),
        })

    # Pattern 4: DOI inline (case-insensitive for prefix, strips trailing punctuation)
    for m in re.finditer(
        r"(?:https?://doi\.org/|doi:?\s*|DOI:?\s*)?(10\.\d{4,9}/[^\s\]]+)",
        clean_text,
        re.IGNORECASE,
    ):
        doi = _clean_doi(m.group(1))
        if doi:
            results.append({
                "text": m.group(0),
                "type": "doi",
                "doi": doi,
            })

    return results


def _clean_doi(doi: str) -> str | None:
    """Strip trailing punctuation and validate a DOI string."""
    if not doi:
        return None
    # Strip common trailing punctuation added by writers
    doi = doi.rstrip("\"'.,;:!?)}/")
    # Strip page-mode suffixes (Frontiers/PLOS/Elsevier URLs append these)
    for suffix in ['/full', '/abstract', '/pdf', '/abs', '/htm', '/epub', '/xml']:
        if doi.lower().endswith(suffix):
            doi = doi[:-len(suffix)]
    if not doi.startswith("10."):
        return None
    return doi


# ── Batch operations ───────────────────────────────────────────────────


def verify_all_stubs_fast(raw_papers_dir: str) -> list[dict]:
    """
    FAST daily path: verify only stubs with DOIs (CrossRef ~1s each).
    Skips stubs without DOIs — those are checked by the weekly full pass.
    """
    results = []
    for fname in os.listdir(raw_papers_dir):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(raw_papers_dir, fname)
        doi = _extract_doi_from_stub(fpath)
        fm = _read_stub_frontmatter(fpath)
        if not fm or not doi:
            continue

        ext = verify_doi(doi)
        if ext and _title_similarity(fm.get("title", ""), ext.get("title", "")) > 0.5:
            results.append({"file": fpath, "status": "VERIFIED", "issues": []})
        elif ext:
            results.append({
                "file": fpath,
                "status": "METADATA_MISMATCH",
                "issues": ["DOI resolves to different title"],
            })
        else:
            results.append({"file": fpath, "status": "NOT_FOUND", "issues": ["DOI not found in CrossRef"]})
    return results


def verify_all_stubs_full(raw_papers_dir: str, max_stubs: int = 0) -> list[dict]:
    """
    SLOW weekly path: verify ALL stubs via OpenAlex title search.
    Use max_stubs to cap for dry runs.
    Recommended: run weekly, not daily.
    """
    results = []
    stub_index = build_stub_index(raw_papers_dir)
    for i, (slug, fpath) in enumerate(sorted(stub_index.items())):
        if not isinstance(fpath, str) or not fpath.endswith(".md"):
            continue
        fm = _read_stub_frontmatter(fpath)
        title = fm.get("title", "")
        if not title:
            continue

        ext = verify_title(title)
        if ext and _title_similarity(title, ext.get("title", "")) > 0.5:
            results.append({"file": fpath, "status": "VERIFIED", "issues": []})
        elif ext:
            results.append({
                "file": fpath,
                "status": "METADATA_MISMATCH",
                "issues": ["Title resolves to different paper"],
            })
        else:
            results.append({
                "file": fpath,
                "status": "NOT_FOUND",
                "issues": ["Title not found in OpenAlex"],
            })

        if max_stubs and i + 1 >= max_stubs:
            break

    return results


def verify_all_stubs(raw_papers_dir: str) -> list[dict]:
    """Backward-compatible: alias for fast (daily) path."""
    return verify_all_stubs_fast(raw_papers_dir)


def _read_stub_frontmatter(path: str) -> dict:
    """Minimal frontmatter parser (safe even on broken YAML)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read(4096)
    except OSError:
        return {}
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        import yaml

        return yaml.safe_load(parts[1]) or {}
    except Exception:
        return {}


# ── CLI (lightweight tests) ──────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1].startswith("10."):
        print(json.dumps(verify_doi(sys.argv[1]), indent=2))
    else:
        # Quick sanity checks
        text = "[[gustavo-deco|Deco]] (2008) established that. [[author|Smith]] (2021) confirmed it."
        cites = parse_inline_citations(text)
        print(f"Parsed {len(cites)} citations from sample text:")
        for c in cites:
            print(f"  {c}")
