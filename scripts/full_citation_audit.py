#!/usr/bin/env python3
"""
Full Citation Audit — One-off scan checking every page's YAML sources: against
CrossRef/OpenAlex to find missing stubs and bad metadata.

For each page:
  1. Read YAML sources: list
  2. For each source path:
     a. Check file exists
     b. Check stub has real metadata
     c. Verify DOI/title in CrossRef/OpenAlex
  3. Report: VERIFIED / MISSING_STUB / BAD_METADATA / NOT_FOUND

Usage:
    python scripts/full_citation_audit.py
    cat meta/full_citation_audit.json | jq '.not_found'
"""
import os
import sys
import json
import re
import glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    WIKI_ROOT, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    RAW_PAPERS_DIR, META_DIR, load_frontmatter, get_sources, read_page,
)
import citation_verify


def get_stub_info(stub_path: str) -> dict:
    """Read stub file and return key metadata."""
    fm = load_frontmatter(stub_path)
    if not fm:
        return {'exists': False}
    authors = fm.get('authors', [])
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(',') if a.strip()]
    has_real_authors = bool(authors) and not any('unknown' in str(a).lower() for a in authors)
    year = str(fm.get('year', '')).strip()
    venue = str(fm.get('venue', '')).strip()
    doi = str(fm.get('doi', '')).strip()
    return {
        'exists': True,
        'title': fm.get('title', ''),
        'authors': authors,
        'has_real_authors': has_real_authors,
        'year': year,
        'venue': venue,
        'doi': doi,
    }


def verify_stub(stub_path: str) -> dict:
    """Verify a stub's metadata against external databases."""
    info = get_stub_info(stub_path)
    if not info['exists']:
        return {'status': 'MISSING_STUB', 'reason': 'File does not exist'}

    # If already looks complete, verify against external source
    if info['has_real_authors'] and info['year'] and info['venue']:
        if info['doi']:
            ext = citation_verify.verify_doi(info['doi'])
            if ext:
                # Check title similarity
                sim = citation_verify._title_similarity(info['title'], ext.get('title', ''))
                if sim > 0.5:
                    return {'status': 'VERIFIED', 'source': 'crossref_doi', 'ext': ext}
                else:
                    return {'status': 'METADATA_MISMATCH', 'reason': 'DOI resolves to different title', 'ext': ext}
            else:
                return {'status': 'NOT_FOUND', 'reason': 'DOI not found in CrossRef'}
        else:
            ext = citation_verify.verify_title(info['title'])
            if ext:
                return {'status': 'VERIFIED', 'source': 'openalex_title', 'ext': ext}
            else:
                return {'status': 'NOT_FOUND', 'reason': 'Title not found in OpenAlex'}
    else:
        # Try external lookup even with bad local metadata
        if info['doi']:
            ext = citation_verify.verify_doi(info['doi'])
        elif info['title']:
            ext = citation_verify.verify_title(info['title'])
        else:
            return {'status': 'BAD_METADATA', 'reason': 'Missing title, DOI, authors, year, or venue'}

        if ext:
            return {'status': 'VERIFIED', 'source': 'openalex_crossref', 'ext': ext}
        else:
            return {'status': 'NOT_FOUND', 'reason': 'No external record found'}


def main():
    print("Scanning all pages for source verification...")
    page_paths = []
    for d in [CONCEPTS_DIR, ENTITIES_DIR, COMPARISONS_DIR]:
        page_paths.extend(glob.glob(os.path.join(d, '*.md')))
    print(f"  {len(page_paths)} pages")

    results = {
        'timestamp': __import__('datetime').datetime.now().isoformat(),
        'pages': {},
        'summary': {
            'total_pages': len(page_paths),
            'total_sources_checked': 0,
            'verified': 0,
            'missing_stub': 0,
            'bad_metadata': 0,
            'not_found': 0,
            'metadata_mismatch': 0,
        }
    }

    all_verdicts = []  # flat list for top-level analysis

    for page_path in page_paths:
        slug = os.path.splitext(os.path.basename(page_path))[0]
        try:
            metadata, _ = read_page(page_path)
        except Exception as e:
            print(f"  WARN: Could not parse {page_path}: {e}")
            continue
        sources = get_sources(metadata)
        if not sources:
            continue

        page_results = []
        for source in sources:
            if isinstance(source, dict):
                source = source.get('url', '') or source.get('title', '')
            source = str(source).strip()
            if not source:
                continue

            # Resolve to absolute path
            stub_path = os.path.join(WIKI_ROOT, source) if not os.path.isabs(source) else source
            results['summary']['total_sources_checked'] += 1

            verdict = verify_stub(stub_path)
            page_results.append({
                'source': source,
                'stub_path': stub_path,
                'status': verdict['status'],
                'reason': verdict.get('reason', ''),
            })
            all_verdicts.append({
                'page': slug,
                'source': source,
                **verdict,
            })

            if verdict['status'] == 'VERIFIED':
                results['summary']['verified'] += 1
            elif verdict['status'] == 'MISSING_STUB':
                results['summary']['missing_stub'] += 1
            elif verdict['status'] == 'BAD_METADATA':
                results['summary']['bad_metadata'] += 1
            elif verdict['status'] == 'NOT_FOUND':
                results['summary']['not_found'] += 1
            elif verdict['status'] == 'METADATA_MISMATCH':
                results['summary']['metadata_mismatch'] += 1

        if page_results:
            results['pages'][slug] = page_results

        if len(results['pages']) % 50 == 0:
            print(f"  Checked {len(results['pages'])} pages...")

    # Write JSON report
    os.makedirs(META_DIR, exist_ok=True)
    report_path = os.path.join(META_DIR, 'full_citation_audit.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Write human-readable markdown summary
    summary_path = os.path.join(META_DIR, 'full_citation_audit.md')
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# Full Citation Audit\n\n")
        s = results['summary']
        f.write(f"| Metric | Count |\n|--------|-------|\n")
        f.write(f"| Pages scanned | {s['total_pages']} |\n")
        f.write(f"| Sources checked | {s['total_sources_checked']} |\n")
        f.write(f"| VERIFIED | {s['verified']} |\n")
        f.write(f"| METADATA_MISMATCH | {s['metadata_mismatch']} |\n")
        f.write(f"| NOT_FOUND | {s['not_found']} |\n")
        f.write(f"| MISSING_STUB | {s['missing_stub']} |\n")
        f.write(f"| BAD_METADATA | {s['bad_metadata']} |\n")

        # Priority sections
        f.write("\n## 🔴 NOT_FOUND (Potential Fabrications)\n\n")
        for v in all_verdicts:
            if v['status'] == 'NOT_FOUND':
                f.write(f"- **{v['page']}**: `{v['source']}`\n")

        f.write("\n## 🟡 METADATA_MISMATCH\n\n")
        for v in all_verdicts:
            if v['status'] == 'METADATA_MISMATCH':
                f.write(f"- **{v['page']}**: `{v['source']}` — {v.get('reason','')}\n")

        f.write("\n## 🟠 MISSING_STUB\n\n")
        for v in all_verdicts:
            if v['status'] == 'MISSING_STUB':
                f.write(f"- **{v['page']}**: `{v['source']}`\n")

    print(f"\n{'='*60}")
    print(f"FULL CITATION AUDIT COMPLETE")
    print(f"{'='*60}")
    s = results['summary']
    print(f"Sources checked:     {s['total_sources_checked']}")
    print(f"VERIFIED:            {s['verified']}")
    print(f"METADATA_MISMATCH:   {s['metadata_mismatch']}")
    print(f"NOT_FOUND:           {s['not_found']} ⚠️")
    print(f"MISSING_STUB:        {s['missing_stub']}")
    print(f"BAD_METADATA:        {s['bad_metadata']}")
    print(f"\nReports:")
    print(f"  JSON:  {report_path}")
    print(f"  MD:    {summary_path}")


if __name__ == '__main__':
    main()
