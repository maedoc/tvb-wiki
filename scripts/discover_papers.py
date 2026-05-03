#!/usr/bin/env python3
"""Paper discovery cycle — Semantic Scholar → raw/papers stubs."""
import os, sys, json, time, urllib.request, urllib.parse
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from create_paper_stub import create_stub_from_metadata

RAW_DIR = "/home/duke/src/tvb-wiki/raw/papers"
LOG_PATH = "/home/duke/src/tvb-wiki/SPRINT_LOG_SUBAGENT.md"
QUERIES = [
    "connectomics resting-state whole-brain modeling",
    "epilepsy whole-brain computational modeling",
]

def doi_to_filename(doi):
    bare = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return f"doi-{bare.replace('/', '-').replace('.', '-')}.md"

def doi_to_filename_existing(doi):
    bare = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return f"doi-{bare.replace('/', '-')}.md"

def already_exists(doi, existing):
    return doi_to_filename(doi) in existing or doi_to_filename_existing(doi) in existing

def search(query, limit=30):
    params = urllib.parse.urlencode({
        'query': query,
        'limit': limit,
        'fields': 'title,authors,year,abstract,externalIds,url,venue,citationCount,publicationDate',
    })
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?{params}'
    req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read()).get('data', [])

def main():
    existing = set(os.listdir(RAW_DIR))
    candidates = []
    for q in QUERIES:
        print(f"Searching: {q}...")
        try:
            for p in search(q, limit=30):
                ext = p.get('externalIds') or {}
                doi = ext.get('DOI', '')
                if not doi or already_exists(doi, existing):
                    continue
                candidates.append({
                    'query': q,
                    'title': p.get('title', ''),
                    'authors': [a.get('name', '') for a in p.get('authors', []) if a.get('name')],
                    'year': str(p.get('year', '')),
                    'venue': p.get('venue', '') or '',
                    'doi': doi,
                    'citation_count': p.get('citationCount') or 0,
                })
        except Exception as e:
            print(f"  Error searching {q}: {e}")
        time.sleep(1)

    # dedupe by DOI and take top 15 by citation count
    seen = set()
    uniq = []
    for c in sorted(candidates, key=lambda x: x['citation_count'], reverse=True):
        if c['doi'] not in seen:
            seen.add(c['doi']); uniq.append(c)
    top = uniq[:15]

    created = []
    for c in top:
        try:
            fp = create_stub_from_metadata(RAW_DIR, c)
            if fp:
                created.append((fp, c['title'], c['doi']))
                existing.add(os.path.basename(fp))
        except Exception as e:
            print(f"  Error creating stub for {c['title']}: {e}")

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write(f"# Sprint Subagent Log — Paper Discovery\n\n")
        f.write(f"**Date:** {datetime.now().isoformat()}\n\n")
        f.write(f"## Queries\n")
        for q in QUERIES:
            f.write(f"- `{q}`\n")
        f.write(f"\n## Results\n")
        f.write(f"- **Created:** {len(created)}\n")
        f.write(f"- **Candidates found:** {len(candidates)}\n")
        f.write(f"- **Unique with DOI:** {len(uniq)}\n")
        f.write(f"\n## Created Stubs\n")
        for fp, title, doi in created:
            f.write(f"- `{fp}` — {title} (DOI: {doi})\n")
        f.write("\n")

    print(f"Created {len(created)} stubs. Log: {LOG_PATH}")

if __name__ == '__main__':
    main()
