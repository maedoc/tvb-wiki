#!/usr/bin/env python3
"""
Ralph Ingestor Agent — fetches new papers from multiple sources.
Python-only, no LLM needed for fetching.

Sources: arXiv, Semantic Scholar, PubMed, OpenAlex, bioRxiv.
"""
import os
import sys
import json
import re
import time
import datetime
import hashlib
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed

# Allow running standalone or imported
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, RAW_PAPERS_DIR, META_DIR, ENTITIES_DIR, CONCEPTS_DIR,
    LAST_UPDATE_FILE, ENTITY_COUNTS_FILE, append_log, git_commit,
    SEARCH_QUERIES, KEYWORD_MAP, PARALLEL_INGESTORS
)

log = get_logger("Ingestor")

# ── arXiv ──────────────────────────────────────────────────────────────
NS = {'a': 'http://www.w3.org/2005/Atom'}

def fetch_arxiv(since_date, max_per_query=15):
    """Fetch papers from arXiv submitted after since_date."""
    papers = []
    seen_ids = set()

    for query in SEARCH_QUERIES:
        params = {
            'search_query': query,
            'max_results': str(max_per_query),
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        url = 'https://export.arxiv.org/api/query?' + '&'.join(
            f'{k}={urllib.parse.quote(v)}' for k, v in params.items()
        )
        req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
        except Exception as e:
            log.warn("arXiv error on '%s': %s", query[:40], e)
            continue

        root = ET.fromstring(data)
        for entry in root.findall('a:entry', NS):
            title_el = entry.find('a:title', NS)
            title = title_el.text.strip().replace('\n', ' ') if title_el is not None else ''
            raw_id = entry.find('a:id', NS).text.strip() if entry.find('a:id', NS) is not None else ''
            arxiv_id = raw_id.split('/abs/')[-1] if '/abs/' in raw_id else raw_id
            base_id = arxiv_id.split('v')[0]  # strip version

            if base_id in seen_ids:
                continue
            seen_ids.add(base_id)

            published = entry.find('a:published', NS)
            published_str = published.text[:10] if published is not None else ''
            try:
                pub_date = datetime.datetime.strptime(published_str, '%Y-%m-%d')
                if pub_date < since_date:
                    continue
            except (ValueError, TypeError):
                pass

            updated_el = entry.find('a:updated', NS)
            updated_str = updated_el.text[:10] if updated_el is not None else ''
            authors = [a.find('a:name', NS).text for a in entry.findall('a:author', NS)
                       if a.find('a:name', NS) is not None]
            summary_el = entry.find('a:summary', NS)
            summary = summary_el.text.strip().replace('\n', ' ') if summary_el is not None else ''
            categories = [c.get('term') for c in entry.findall('a:category', NS)]

            papers.append({
                'source': 'arxiv',
                'source_id': base_id,
                'title': title,
                'authors': authors,
                'year': published_str[:4] if published_str else '',
                'date': published_str,
                'abstract': summary,
                'categories': categories,
                'url': f'https://arxiv.org/abs/{base_id}',
                'doi': '',
                'venue': '',
                'citation_count': None,
            })
        time.sleep(1)

    return papers


# ── Semantic Scholar ───────────────────────────────────────────────────

def fetch_semantic_scholar(since_date, max_results=50):
    """Fetch papers from Semantic Scholar API."""
    papers = []
    queries = [
        "The Virtual Brain whole-brain modeling",
        "neural mass model connectome",
        "TVB epilepsy simulation",
        "whole-brain dynamics structural connectivity",
    ]

    for query in queries:
        params = urllib.parse.urlencode({
            'query': query,
            'limit': max_results,
            'fields': 'title,authors,year,abstract,externalIds,url,venue,citationCount,publicationDate',
            'year': f'{since_date.year}-',
        })
        url = f'https://api.semanticscholar.org/graph/v1/paper/search?{params}'
        req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
        except Exception as e:
            log.warn("Semantic Scholar error on '%s': %s", query[:40], e)
            continue

        for item in data.get('data', []):
            ext_ids = item.get('externalIds', {})
            arxiv_id = ext_ids.get('ArXiv', '')
            doi = ext_ids.get('DOI', '')
            s2_id = item.get('paperId', '')

            authors = [a.get('name', '') for a in item.get('authors', [])
                       if a.get('name')]
            pub_date = item.get('publicationDate', '') or ''

            papers.append({
                'source': 'semantic-scholar',
                'source_id': s2_id,
                'title': item.get('title', ''),
                'authors': authors,
                'year': str(item.get('year', '')),
                'date': pub_date[:10] if pub_date else '',
                'abstract': item.get('abstract', '') or '',
                'categories': [],
                'url': item.get('url', ''),
                'doi': doi,
                'arxiv_id': arxiv_id,
                'venue': item.get('venue', '') or '',
                'citation_count': item.get('citationCount'),
            })
        time.sleep(0.5)

    return papers


# ── PubMed ─────────────────────────────────────────────────────────────

def fetch_pubmed(since_date, max_results=20):
    """Fetch papers from PubMed (peer-reviewed biomedical)."""
    queries = [
        '"The Virtual Brain"',
        '"neural mass model" AND brain',
        '"whole-brain model" AND connectivity',
        'connectome AND modeling',
    ]

    all_ids = []
    for query in queries:
        params = urllib.parse.urlencode({
            'db': 'pubmed',
            'term': query,
            'retmax': max_results,
            'retmode': 'json',
            'datetype': 'pdat',
            'mindate': since_date.strftime('%Y/%m/%d'),
            'maxdate': '3000',
            'sort': 'date',
        })
        url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{params}'
        req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
            ids = data.get('esearchresult', {}).get('idlist', [])
            all_ids.extend(ids)
        except Exception as e:
            log.warn("PubMed search error on '%s': %s", query[:40], e)
            continue
        time.sleep(0.5)

    # Deduplicate
    all_ids = list(set(all_ids))
    if not all_ids:
        return []

    # Fetch details
    params = urllib.parse.urlencode({
        'db': 'pubmed',
        'id': ','.join(all_ids[:50]),
        'retmode': 'json',
        'rettype': 'abstract',
    })
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?{params}'
    req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})

    papers = []
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        for uid, info in data.get('result', {}).items():
            if uid == 'uids':
                continue
            authors = [a.get('name', '') for a in info.get('authors', [])]
            papers.append({
                'source': 'pubmed',
                'source_id': uid,
                'title': info.get('title', ''),
                'authors': authors,
                'year': info.get('pubdate', '')[:4],
                'date': info.get('pubdate', ''),
                'abstract': '',  # esummary doesn't include full abstracts
                'categories': [],
                'url': f'https://pubmed.ncbi.nlm.nih.gov/{uid}/',
                'doi': '',
                'venue': info.get('source', ''),
                'citation_count': None,
            })
    except Exception as e:
        log.warn("PubMed fetch error: %s", e)

    return papers


# ── OpenAlex ───────────────────────────────────────────────────────────

def fetch_openalex(since_date, max_results=20):
    """Fetch papers from OpenAlex."""
    queries = [
        "The Virtual Brain",
        "neural mass model whole brain",
        "connectome simulation",
    ]

    papers = []
    for query in queries:
        params = urllib.parse.urlencode({
            'search': query,
            'per_page': max_results,
            'filter': f'from_publication_date:{since_date.strftime("%Y-%m-%d")}',
            'sort': 'publication_date:desc',
            'select': 'id,doi,title,authorships,publication_year,abstract_inverted_index,primary_location',
        })
        url = f'https://api.openalex.org/works?{params}'
        req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0 mailto:ralph@tvb-wiki.org'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
        except Exception as e:
            log.warn("OpenAlex error on '%s': %s", query[:40], e)
            continue

        for item in data.get('results', []):
            # Reconstruct abstract from inverted index
            abstract = ''
            inv_idx = item.get('abstract_inverted_index')
            if inv_idx:
                words = [''] * max((pos for positions in inv_idx.values() for pos in positions), default=0)
                for word, positions in inv_idx.items():
                    for pos in positions:
                        if pos < len(words):
                            words[pos] = word
                abstract = ' '.join(words)

            authors = [a.get('author', {}).get('display_name', '')
                       for a in item.get('authorships', [])]

            venue = ''
            loc = item.get('primary_location', {})
            if loc:
                source = loc.get('source', {})
                if source:
                    venue = source.get('display_name', '')

            papers.append({
                'source': 'openalex',
                'source_id': item.get('id', ''),
                'title': item.get('title', '') or '',
                'authors': authors,
                'year': str(item.get('publication_year', '')),
                'date': '',
                'abstract': abstract,
                'categories': [],
                'url': f"https://doi.org/{item.get('doi', '').replace('https://doi.org/', '')}" if item.get('doi') else '',
                'doi': (item.get('doi') or '').replace('https://doi.org/', ''),
                'venue': venue,
                'citation_count': None,
            })
        time.sleep(0.5)

    return papers


# ── Deduplication ─────────────────────────────────────────────────────

def paper_slug(paper: dict) -> str:
    """Generate a unique slug for a paper."""
    source = paper.get('source', 'unknown')
    source_id = paper.get('source_id', '')

    if source == 'arxiv':
        return f"arxiv-{source_id}"
    elif source == 'pubmed':
        return f"pubmed-{source_id}"
    elif source == 'semantic-scholar':
        # Prefer arxiv ID if available
        arxiv_id = paper.get('arxiv_id', '')
        if arxiv_id:
            return f"arxiv-{arxiv_id}"
        return f"semanticscholar-{source_id[:12]}"
    elif source == 'openalex':
        doi = paper.get('doi', '')
        if doi:
            return f"doi-{doi.replace('/', '-')}"
        return f"openalex-{source_id.split('/')[-1]}"
    else:
        # Hash the title
        h = hashlib.md5(paper.get('title', '').encode()).hexdigest()[:8]
        return f"{source}-{h}"


def is_already_ingested(slug: str) -> bool:
    """Check if a paper slug already exists in raw/papers/."""
    return os.path.exists(os.path.join(RAW_PAPERS_DIR, f"{slug}.md"))


# ── Save raw paper ────────────────────────────────────────────────────

def save_raw_paper(paper: dict) -> bool:
    """Save a paper as markdown. Returns True if new paper was saved."""
    slug = paper_slug(paper)
    filepath = os.path.join(RAW_PAPERS_DIR, f"{slug}.md")

    if os.path.exists(filepath):
        return False

    os.makedirs(RAW_PAPERS_DIR, exist_ok=True)

    lines = [
        f"# {paper['title']}",
        "",
        f"**Source**: {paper['source']}",
        f"**ID**: {paper.get('source_id', '')}",
    ]
    if paper.get('doi'):
        lines.append(f"**DOI**: {paper['doi']}")
    if paper.get('url'):
        lines.append(f"**URL**: {paper['url']}")
    if paper.get('date'):
        lines.append(f"**Date**: {paper['date']}")
    if paper.get('year'):
        lines.append(f"**Year**: {paper['year']}")
    if paper.get('authors'):
        lines.append(f"**Authors**: {', '.join(paper['authors'])}")
    if paper.get('venue'):
        lines.append(f"**Venue**: {paper['venue']}")
    if paper.get('categories'):
        lines.append(f"**Categories**: {', '.join(paper['categories'])}")
    if paper.get('citation_count') is not None:
        lines.append(f"**Citations**: {paper['citation_count']}")

    lines.append("")
    lines.append("## Abstract")
    lines.append("")
    lines.append(paper.get('abstract', '(No abstract available)'))
    lines.append("")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return True


# ── Entity extraction ─────────────────────────────────────────────────

def extract_mentions(paper: dict) -> dict:
    """Extract software and concept mentions from a paper's title + abstract."""
    text = (paper.get('title', '') + ' ' + paper.get('abstract', '')).lower()
    mentions = {'software': set(), 'concepts': set()}

    for category, items in KEYWORD_MAP.items():
        for (keyword, slug, tag) in items:
            if keyword.lower() in text:
                mentions[category].add((keyword, slug, tag))

    return mentions


def update_entity_counts(counts: dict, mentions: dict):
    """Increment mention counts."""
    for cat in ['software', 'concepts']:
        for (keyword, slug, tag) in mentions.get(cat, set()):
            if keyword not in counts[cat]:
                counts[cat][keyword] = 0
            counts[cat][keyword] += 1


# ── Create stub pages for new entities ────────────────────────────────

def ensure_page_exists(slug: str, page_type: str, title: str, tag: str) -> bool:
    """Create a stub page if it doesn't exist. Returns True if created."""
    if page_type == 'entity':
        dir_path = ENTITIES_DIR
    else:
        dir_path = CONCEPTS_DIR

    os.makedirs(dir_path, exist_ok=True)
    filepath = os.path.join(dir_path, f"{slug}.md")
    if os.path.exists(filepath):
        return False

    today = datetime.date.today().isoformat()

    if page_type == 'entity':
        content = f"""# {title}

## Overview
*Placeholder — awaiting content from Ralph Improver.*

## Key Features
*Placeholder*

## Usage in Whole-Brain Modeling
*Placeholder*

## Related Software
* [[TVB]]

## References
"""
    else:
        content = f"""# {title}

## Definition
*Placeholder — awaiting content from Ralph Improver.*

## Role in Whole-Brain Modeling
*Placeholder*

## Related Concepts
* [[neural mass model]]
* [[functional connectivity]]

## References
"""

    frontmatter_text = f"""---
title: {title}
created: {today}
updated: {today}
type: {page_type}
tags: [{tag}]
sources: []
---

"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter_text + content)

    return True


def create_stubs_for_mentions(mentions: dict, threshold: int = 2):
    """Create stub pages for entities mentioned enough times."""
    counts = load_entity_counts()
    update_entity_counts(counts, mentions)
    save_entity_counts(counts)

    created = 0
    for cat in ['software', 'concepts']:
        for (keyword, slug, tag) in mentions.get(cat, set()):
            count = counts[cat].get(keyword, 0)
            if count >= threshold:
                page_type = 'entity' if cat == 'software' else 'concept'
                if ensure_page_exists(slug, page_type, keyword, tag):
                    log.info("Created stub: %s (%s, %d mentions)", slug, page_type, count)
                    created += 1
    return created


# ── Load/Save helpers ─────────────────────────────────────────────────

def load_last_update() -> datetime.datetime:
    if os.path.exists(LAST_UPDATE_FILE):
        with open(LAST_UPDATE_FILE, 'r') as f:
            try:
                return datetime.datetime.fromisoformat(f.read().strip())
            except (ValueError, TypeError):
                pass
    return datetime.datetime.now() - datetime.timedelta(days=7)


def save_last_update():
    with open(LAST_UPDATE_FILE, 'w') as f:
        f.write(datetime.datetime.now().isoformat())


def load_entity_counts() -> dict:
    if os.path.exists(ENTITY_COUNTS_FILE):
        with open(ENTITY_COUNTS_FILE, 'r') as f:
            return json.load(f)
    return {'software': {}, 'concepts': {}, 'authors': {}}


def save_entity_counts(counts: dict):
    os.makedirs(META_DIR, exist_ok=True)
    with open(ENTITY_COUNTS_FILE, 'w') as f:
        json.dump(counts, f, indent=2)


# ── Main ingestor cycle ───────────────────────────────────────────────

def run_ingestor_cycle():
    """Run one ingestor cycle. Returns (papers_added, pages_created)."""
    log.info("Starting hourly cycle")
    os.makedirs(META_DIR, exist_ok=True)

    since = load_last_update()
    log.info("Searching for papers since %s", since.strftime('%Y-%m-%d'))

    # Fetch from all sources in parallel
    all_papers = []
    source_counts = {}

    def fetch_source(name, func):
        try:
            papers = func(since)
            return name, papers
        except Exception as e:
            log.error("%s fetch failed: %s", name, e)
            return name, []

    with ThreadPoolExecutor(max_workers=PARALLEL_INGESTORS) as pool:
        futures = [
            pool.submit(fetch_source, "arXiv", fetch_arxiv),
            pool.submit(fetch_source, "Semantic Scholar", fetch_semantic_scholar),
            pool.submit(fetch_source, "PubMed", fetch_pubmed),
            pool.submit(fetch_source, "OpenAlex", fetch_openalex),
        ]
        for future in as_completed(futures):
            name, papers = future.result()
            source_counts[name] = len(papers)
            all_papers.extend(papers)
            log.info("%s: found %d papers", name, len(papers))

    # Deduplicate across sources
    seen_slugs = set()
    unique_papers = []
    for paper in all_papers:
        slug = paper_slug(paper)
        if slug not in seen_slugs:
            seen_slugs.add(slug)
            unique_papers.append(paper)

    # Filter already-ingested
    new_papers = [p for p in unique_papers if not is_already_ingested(paper_slug(p))]

    if not new_papers:
        log.info("No new papers found")
        log.info("Cycle complete. Nothing to do.")
        save_last_update()
        return 0, 0

    log.info("Found %d new papers (deduped from %d total)", len(new_papers), len(all_papers))

    # Save raw papers + extract mentions
    added = 0
    all_mentions = {'software': set(), 'concepts': set()}

    for paper in new_papers:
        if save_raw_paper(paper):
            slug = paper_slug(paper)
            added += 1
            log.info("Saved raw/%s.md — %s", slug, paper['title'][:60])

            mentions = extract_mentions(paper)
            for cat in ['software', 'concepts']:
                all_mentions[cat].update(mentions[cat])

    # Create stubs for frequently-mentioned entities
    pages_created = create_stubs_for_mentions(all_mentions, threshold=2)

    # Save timestamp
    save_last_update()

    # Git commit
    if added > 0:
        msg = f"Ingest: {added} papers ({', '.join(f'{v} {k}' for k, v in source_counts.items() if v > 0)}) (Ingestor)"
        git_commit(msg)
        append_log(f"Ingest: {added} new papers, {pages_created} stubs created")
        log.info("Committed: \"%s\"", msg)

    log.info("Cycle complete. %d papers added, %d stubs created.", added, pages_created)
    return added, pages_created


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    run_ingestor_cycle()
