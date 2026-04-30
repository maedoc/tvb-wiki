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
"""
import urllib.request
import urllib.parse
import urllib.error
import re
import time
import json
from typing import Any

_USER_AGENT = "tvb-wiki-citation-verify (mailto:agent@local)"
_POLITE_SLEEP = 0.15  # seconds between API calls


# ── API lookup helpers ─────────────────────────────────────────────────

def _http_json(url: str, headers: dict | None = None, timeout: int = 20) -> dict | None:
    """GET JSON and return parsed dict, or None on failure."""
    h = {"User-Agent": _USER_AGENT}
    if headers:
        h.update(headers)
    try:
        req = urllib.request.Request(url, headers=h)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except Exception:
        return None


def _normalize_text(s: str | None) -> str:
    if not s:
        return ""
    s = s.lower()
    s = re.sub(r"[^\w\s]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _title_similarity(a: str | None, b: str | None) -> float:
    """Simple token overlap similarity."""
    a = _normalize_text(a)
    b = _normalize_text(b)
    if not a or not b:
        return 0.0
    a_tokens = set(a.split())
    b_tokens = set(b.split())
    return len(a_tokens & b_tokens) / max(len(a_tokens), 1)


# ── CrossRef DOI lookup ────────────────────────────────────────────────

def verify_doi(doi: str) -> dict | None:
    """Look up a paper by DOI via CrossRef. Returns normalized metadata or None."""
    if not doi or not isinstance(doi, str):
        return None
    doi = doi.strip().replace("https://doi.org/", "").replace("http://doi.org/", "").replace("dx.doi.org/", "")
    if not doi:
        return None

    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    data = _http_json(url, headers={"User-Agent": _USER_AGENT})
    if not data or "message" not in data:
        return None

    m = data["message"]
    authors = []
    for a in m.get("author", []):
        parts = []
        if a.get("given"):
            parts.append(a["given"].strip())
        if a.get("family"):
            parts.append(a["family"].strip())
        if parts:
            authors.append(" ".join(parts))

    year = str(
        m.get("published-print", {}).get("date-parts", [[""]])[0][0]
        or m.get("published-online", {}).get("date-parts", [[""]])[0][0]
        or m.get("created", {}).get("date-parts", [[""]])[0][0]
        or ""
    )

    venue = ""
    container = m.get("container-title")
    if isinstance(container, list) and container:
        venue = container[0]
    elif isinstance(container, str):
        venue = container

    return {
        "title": m.get("title", [""])[0] if isinstance(m.get("title"), list) else m.get("title", ""),
        "authors": authors,
        "year": year,
        "venue": venue,
        "doi": doi,
    }


# ── OpenAlex title search ──────────────────────────────────────────────

def verify_title(title: str) -> dict | None:
    """Search OpenAlex by title. Returns best match or None."""
    if not title or not isinstance(title, str):
        return None

    q = urllib.parse.quote(title)
    url = f"https://api.openalex.org/works?search={q}&per-page=5"
    data = _http_json(url)
    if not data or not data.get("results"):
        return None

    best = None
    best_score = 0.0
    for r in data["results"]:
        score = _title_similarity(title, r.get("title", ""))
        if score > best_score:
            best_score = score
            best = r

    if not best or best_score < 0.3:
        return None

    # Extract authors
    authors = []
    for a in best.get("authorships", []):
        author = a.get("author", {})
        name = author.get("display_name", "")
        if name:
            authors.append(name)

    # Extract venue safely
    loc = best.get("primary_location") or {}
    venue = (loc.get("source") or {}).get("display_name", "")
    if not venue and best.get("locations"):
        venue = " ".join(
            (l.get("source") or {}).get("display_name", "")
            for l in best["locations"] if (l.get("source") or {}).get("display_name")
        )[:100]

    doi = str(best.get("doi", "")).replace("https://doi.org/", "")

    return {
        "title": best.get("title", ""),
        "authors": authors,
        "year": str(best.get("publication_year", "")),
        "venue": venue,
        "doi": doi,
    }


# ── Citation extraction ───────────────────────────────────────────────

def parse_inline_citations(text: str) -> list[dict]:
    """
    Extract inline citation mentions from markdown text.
    Returns list of dicts: [{"text": "Gardiner (2009)", "type": "author_year"}, ...]
    """
    results = []
    if not text:
        return results

    # Pattern 1: Author (Year) — e.g., "Deco (2008)", "Tuckwell (1988)"
    for m in re.finditer(r"\b([A-Z][a-zA-Z\-\']+(?:\s+[A-Z][a-zA-Z\-\']+)*?)\s*\((\d{4})[a-z]?\)", text):
        results.append({
            "text": m.group(0),
            "type": "author_year",
            "author": m.group(1).strip(),
            "year": m.group(2),
        })

    # Pattern 2: bare [^N] reference numbers (already linked via YAML sources)
    for m in re.finditer(r"\[\^(\d+)\]", text):
        results.append({
            "text": m.group(0),
            "type": "superscript",
            "num": int(m.group(1)),
        })

    # Pattern 3: bare [N] reference numbers
    for m in re.finditer(r"(?<!\[)\[(\d+)\](?!\()", text):
        results.append({
            "text": m.group(0),
            "type": "bracket_num",
            "num": int(m.group(1)),
        })

    # Pattern 4: DOI inline
    for m in re.finditer(r"(?:https?://doi\.org/|DOI:?\s*)?(10\.\d{4,9}/[^\s\]]+)", text, re.IGNORECASE):
        results.append({
            "text": m.group(0),
            "type": "doi",
            "doi": m.group(1),
        })

    # Deduplicate by text span
    seen = set()
    deduped = []
    for r in results:
        key = r["text"]
        if key not in seen:
            seen.add(key)
            deduped.append(r)
    return deduped


# ── Stub matching ─────────────────────────────────────────────────────

def find_stub_for_citation(citation: dict, stub_index: dict[str, str]) -> str | None:
    """
    Try to find a raw/papers/*.md slug that matches a citation mention.
    stub_index: {slug: filepath}
    Returns filepath or None.
    """
    if citation["type"] == "doi":
        doi = citation["doi"]
        # Check stubs with DOI field
        for slug, path in stub_index.items():
            if doi.replace("https://doi.org/","").replace("http://doi.org/","") in slug:
                return path
            # Also check inside file (lightweight: don't parse YAML, just grep)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    stub_text = f.read()
                if doi in stub_text:
                    return path
            except Exception:
                pass
        return None

    if citation["type"] == "author_year":
        author = citation.get("author", "").split()[-1].lower()  # last name
        year = citation.get("year", "")
        # Look for slug containing author + year
        for slug, path in stub_index.items():
            if author in slug and year in slug:
                return path
            # Try just author
            if author in slug:
                return path
    return None


# ── Main verification function ───────────────────────────────────────

def verify_citation(citation: dict, stub_index: dict[str, str] | None = None) -> dict:
    """
    Main verification entry point.

    Returns a verdict dict:
      {
        "status": "VERIFIED" | "NOT_FOUND" | "METADATA_MISMATCH" | "TIMEOUT",
        "source": "crossref_doi" | "openalex_title" | "stub_cache" | "none",
        "metadata": {...} | None,
        "raw_stub_path": str | None,
      }
    """
    result = {
        "status": "NOT_FOUND",
        "source": "none",
        "metadata": None,
        "raw_stub_path": None,
    }

    # Step 1: check if stub exists
    if stub_index:
        stub_path = find_stub_for_citation(citation, stub_index)
        if stub_path:
            result["raw_stub_path"] = stub_path
            # Read stub metadata
            try:
                with open(stub_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                # Quick regex for authors/year/venue in frontmatter
                authors = re.findall(r'^authors:\s*$\n(?:^\s+[-*]\s*(.+)\n)+', text, re.M)
                if not authors:
                    authors = re.findall(r'^authors:\s*\[(.*?)\]', text, re.M)
                    if authors:
                        authors = [a.strip().strip('"\'') for a in authors[0].split(',')]
                year_match = re.search(r'^year:\s*(\d{4})', text, re.M)
                venue_match = re.search(r'^venue:\s*(.+)$', text, re.M)
                title_match = re.search(r'^title:\s*(.+)$', text, re.M)
                doi_match = re.search(r'^doi:\s*(.+)$', text, re.M)

                stub_authors = authors if authors else []
                stub_year = year_match.group(1) if year_match else ""
                stub_venue = venue_match.group(1).strip().strip('"\'') if venue_match else ""

                if stub_authors and stub_year and stub_venue and not any('unknown' in str(a).lower() for a in stub_authors):
                    result["status"] = "VERIFIED"
                    result["source"] = "stub_cache"
                    result["metadata"] = {
                        "title": title_match.group(1).strip().strip('"\'') if title_match else "",
                        "authors": stub_authors,
                        "year": stub_year,
                        "venue": stub_venue,
                        "doi": doi_match.group(1).strip().strip('"\'') if doi_match else "",
                    }
                    return result
            except Exception:
                pass

    # Step 2: if stub missing or stub has bad metadata, query databases
    if citation["type"] == "doi":
        time.sleep(_POLITE_SLEEP)
        meta = verify_doi(citation.get("doi", ""))
        if meta:
            result["status"] = "VERIFIED"
            result["source"] = "crossref_doi"
            result["metadata"] = meta
            return result

    elif citation["type"] == "author_year":
        # Construct a synthetic title for searching
        # We don't have the actual title from inline citation, just author + year
        # Search OpenAlex with "author year" as a broad query
        author = citation.get("author", "")
        year = citation.get("year", "")
        if author and year:
            search_title = f"{author} {year}"
            time.sleep(_POLITE_SLEEP)
            meta = verify_title(search_title)
            if meta:
                # Check author overlap to avoid false matches
                stub_last = author.split()[-1].lower()
                found_last_names = [
                    a.split()[-1].lower() for a in meta.get("authors", [])
                    if a.split()
                ]
                if stub_last in found_last_names:
                    result["status"] = "VERIFIED"
                    result["source"] = "openalex_title"
                    result["metadata"] = meta
                    return result
                # If title is very similar but authors diverge, it's a mismatch
                sim = _title_similarity(search_title, meta.get("title", ""))
                if sim > 0.5:
                    result["status"] = "METADATA_MISMATCH"
                    result["source"] = "openalex_title"
                    result["metadata"] = meta
                    return result

    # Fallback: nothing found
    return result


# ── Batch verification for Auditor ────────────────────────────────────

def build_stub_index(raw_papers_dir: str = "raw/papers") -> dict[str, str]:
    """Build {slug: filepath} index for all raw stubs."""
    import os
    import glob
    index = {}
    for path in glob.glob(os.path.join(raw_papers_dir, "*.md")):
        slug = os.path.splitext(os.path.basename(path))[0]
        index[slug] = path
    return index


def verify_all_stubs(raw_papers_dir: str = "raw/papers") -> list[dict]:
    """
    Batch-verify every raw stub. Returns list of verdict dicts.
    Useful for Auditor daily check.
    """
    import os
    import glob
    results = []
    for path in sorted(glob.glob(os.path.join(raw_papers_dir, "*.md"))):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception:
            continue

        # Extract DOI from frontmatter
        doi_match = re.search(r'^doi:\s*(.+)$', text, re.M)
        doi = doi_match.group(1).strip().strip('"\'') if doi_match else ""

        title_match = re.search(r'^title:\s*(.+)$', text, re.M)
        title = title_match.group(1).strip().strip('"\'') if title_match else ""

        authors = re.findall(r'^\s+[-*]\s*(.+)$', text, re.M)
        if not authors:
            authors = re.findall(r'^authors:\s*\[(.*?)\]', text, re.M)
            if authors:
                authors = [a.strip().strip('"\'') for a in authors[0].split(',')]
        year_match = re.search(r'^year:\s*(\d{4})', text, re.M)
        venue_match = re.search(r'^venue:\s*(.+)$', text, re.M)

        if doi:
            v = verify_doi(doi)
        elif title:
            v = verify_title(title)
        else:
            v = None

        if v:
            # Compare stub metadata with external metadata
            issues = []
            if v.get("year") != (year_match.group(1) if year_match else ""):
                issues.append(f"year mismatch: stub={year_match.group(1) if year_match else ''}, ext={v['year']}")
            # Author overlap check
            ext_last = [a.split()[-1].lower() for a in v.get("authors", []) if a.split()]
            stub_last = [a.split()[-1].lower() for a in authors if a.split()]
            overlap = set(ext_last) & set(stub_last)
            if not overlap and ext_last and stub_last:
                issues.append(f"authors mismatch: stub={stub_last}, ext={ext_last}")
            if issues:
                status = "METADATA_MISMATCH"
            else:
                status = "VERIFIED"
        else:
            status = "NOT_FOUND"
            issues = []

        results.append({
            "file": os.path.basename(path),
            "title": title,
            "status": status,
            "source": "crossref_doi" if doi else ("openalex_title" if title else "none"),
            "issues": issues,
        })

        time.sleep(_POLITE_SLEEP)
    return results
