#!/usr/bin/env python3
"""
Ralph Deep Research Agent — periodic gap-driven research sprints.

Runs less frequently than the Ingestor (every 4-6 hours) but goes deeper:
- Reads audit report to find weakest wiki areas
- Uses pi to plan targeted research queries
- Follows citation chains from high-value papers
- Profiles prolific TVB researchers
- Feeds findings into raw/papers/ and creates stubs

Uses pi with kimi-k2.6 for reasoning about what to research,
then uses the same API fetchers as the Ingestor for actual paper retrieval.
"""
import os
import sys
import re
import json
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, RAW_PAPERS_DIR, META_DIR, AUDIT_REPORT_FILE,
    SCHEMA_PATH, ENTITIES_DIR, CONCEPTS_DIR,
    append_log, git_commit, get_all_pages, load_frontmatter, get_sources,
    run_pi, WRITER_MODEL,
    KEYWORD_MAP,
)
from ingestor import (
    save_raw_paper, paper_slug, is_already_ingested, extract_mentions,
    create_stubs_for_mentions, load_entity_counts, save_entity_counts,
    fetch_semantic_scholar, fetch_arxiv,
    _urlopen_with_backoff,
)
import urllib.request
import urllib.parse

log = get_logger("DeepResearch")


# ── Identify gaps ─────────────────────────────────────────────────────

def find_gaps() -> dict:
    """
    Analyze wiki state to identify research gaps.
    Returns a structured gap report for the LLM to plan research.
    """
    pages = get_all_pages()
    gaps = {
        'zero_source_pages': [],    # pages with no references at all
        'thin_pages': [],           # pages with < 200 words
        'missing_topics': [],       # topics in KEYWORD_MAP with no page
        'weak_areas': [],           # tag areas with few pages
        'high_value_authors': [],   # authors cited often but no person page
    }

    # Pages with zero sources
    for slug, filepath in pages.items():
        try:
            metadata = load_frontmatter(filepath)
            sources = get_sources(metadata)
            if len(sources) == 0:
                gaps['zero_source_pages'].append({
                    'slug': slug,
                    'type': metadata.get('type', ''),
                    'title': metadata.get('title', slug),
                })
        except Exception:
            pass

    # Check keyword map coverage
    for category, items in KEYWORD_MAP.items():
        for (keyword, slug, tag) in items:
            if slug not in pages:
                gaps['missing_topics'].append({
                    'keyword': keyword,
                    'slug': slug,
                    'category': category,
                })

    # Load audit report if available
    if os.path.exists(AUDIT_REPORT_FILE):
        with open(AUDIT_REPORT_FILE, 'r') as f:
            report = json.load(f)

        # Stale pages as candidates for refresh
        for item in report.get('stale_pages', [])[:10]:
            gaps['thin_pages'].append({
                'slug': item.get('slug', ''),
                'days_old': item.get('days_old', 0),
            })

    return gaps


def build_research_planning_prompt(gaps: dict) -> str:
    """Ask the LLM to plan a focused research sprint based on gaps."""
    gap_summary = json.dumps(gaps, indent=2)[:4000]  # Truncate if huge

    prompt = f"""You are the Ralph Deep Research agent planning a focused research sprint for a TVB Wiki.

## CURRENT GAPS IN THE WIKI
{gap_summary}

## YOUR TASK
Identify the 3 most impactful research targets to fill these gaps. For each target:
1. What to search for (specific search queries)
2. Why this matters (which gaps it fills)
3. What sources to use (arxiv, semantic_scholar, pubmed, citation_chasing)

Think about:
- Which gaps would improve the most pages if filled?
- Are there citation chains to follow from existing high-value papers?
- Are there key authors whose full body of work should be profiled?

Output as JSON:
[
  {{
    "focus": "short name for this research target",
    "rationale": "why this matters",
    "queries": ["search query 1", "search query 2"],
    "sources": ["semantic_scholar", "arxiv"],
    "gaps_addressed": ["zero_source_pages:slug1", "missing_topics:slug2"]
  }}
]

Output ONLY valid JSON, no other text."""
    return prompt


def plan_research() -> list[dict]:
    """Use LLM to plan a research sprint, fall back to heuristic if LLM fails."""
    gaps = find_gaps()
    log.info("Found gaps: %d zero-source pages, %d missing topics, %d thin pages",
             len(gaps['zero_source_pages']),
             len(gaps['missing_topics']),
             len(gaps['thin_pages']))

    # Try LLM-based planning
    prompt = build_research_planning_prompt(gaps)
    success, output = run_pi(prompt, model=WRITER_MODEL)

    if success:
        try:
            json_match = re.search(r'\[.*\]', output, re.DOTALL)
            if json_match:
                plans = json.loads(json_match.group())
                log.info("LLM planned %d research targets", len(plans))
                return plans
        except json.JSONDecodeError:
            log.warn("Could not parse LLM research plan, using heuristics")

    # Fallback: heuristic planning based on gaps
    plans = []

    # Plan 1: fill zero-source pages
    if gaps['zero_source_pages']:
        targets = [p['title'] for p in gaps['zero_source_pages'][:5]]
        plans.append({
            'focus': 'Fill zero-source pages',
            'rationale': f'{len(gaps["zero_source_pages"])} pages have no references',
            'queries': [f'"{t}" brain model' for t in targets[:3]],
            'sources': ['semantic_scholar'],
            'gaps_addressed': [f"zero_source_pages:{p['slug']}" for p in gaps['zero_source_pages'][:5]],
        })

    # Plan 2: find papers for missing topics
    if gaps['missing_topics']:
        topics = [t['keyword'] for t in gaps['missing_topics'][:5]]
        plans.append({
            'focus': 'Cover missing topics',
            'rationale': f'{len(gaps["missing_topics"])} topics have no page',
            'queries': topics[:3],
            'sources': ['semantic_scholar', 'arxiv'],
            'gaps_addressed': [f"missing_topics:{t['slug']}" for t in gaps['missing_topics'][:5]],
        })

    # Plan 3: citation chain from most-cited existing papers
    plans.append({
        'focus': 'Citation chain from TVB papers',
        'rationale': 'Follow citations from seminal TVB papers to find related work',
        'queries': ['The Virtual Brain connectome simulation', 'Jirsa virtual brain epilepsy'],
        'sources': ['semantic_scholar'],
        'gaps_addressed': [],
    })

    log.info("Heuristic planned %d research targets", len(plans))
    return plans


# ── Citation chaining ─────────────────────────────────────────────────

def fetch_citations(paper_id: str, direction: str = 'citations', limit: int = 20) -> list[dict]:
    """
    Follow citation chains from a Semantic Scholar paper.
    direction: 'citations' (papers that cite this) or 'references' (papers this cites)
    """
    url = f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}/{direction}'
    params = urllib.parse.urlencode({
        'limit': limit,
        'fields': 'title,authors,year,abstract,externalIds,venue,citationCount',
    })
    req = urllib.request.Request(f"{url}?{params}",
                                 headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
    raw = _urlopen_with_backoff(req, 'Semantic Scholar', f'citations/{paper_id}')
    if not raw:
        return []
    data = json.loads(raw)

    papers = []
    for item in data.get('data', []):
        paper = item.get('citingPaper' if direction == 'citations' else 'citedPaper', item)
        if not paper:
            continue

        ext_ids = paper.get('externalIds', {})
        authors = [a.get('name', '') for a in paper.get('authors', []) if a.get('name')]

        papers.append({
            'source': 'semantic-scholar-citations',
            'source_id': paper.get('paperId', ''),
            'title': paper.get('title', ''),
            'authors': authors,
            'year': str(paper.get('year', '')),
            'date': '',
            'abstract': paper.get('abstract', '') or '',
            'categories': [],
            'url': f"https://www.semanticscholar.org/paper/{paper.get('paperId', '')}",
            'doi': ext_ids.get('DOI', ''),
            'arxiv_id': ext_ids.get('ArXiv', ''),
            'venue': paper.get('venue', '') or '',
            'citation_count': paper.get('citationCount'),
        })

    return papers


def find_seminal_papers() -> list[str]:
    """
    Find Semantic Scholar paper IDs for the most-cited papers already in raw/papers/.
    These are good starting points for citation chaining.
    """
    if not os.path.isdir(RAW_PAPERS_DIR):
        return []

    seminal = []
    for fn in os.listdir(RAW_PAPERS_DIR)[:50]:  # Check recent papers
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(RAW_PAPERS_DIR, fn)
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read(500)
            # Look for high citation count
            cit_match = re.search(r'\*\*Citations\*\*:\s*(\d+)', content)
            if cit_match and int(cit_match.group(1)) > 20:
                # Try to find a Semantic Scholar ID
                s2_match = re.search(r'semanticscholar[-/]([a-f0-9]+)', fn)
                if s2_match:
                    seminal.append(s2_match.group(1))
        except Exception:
            pass

    return seminal[:5]


# ── Execute research plan ─────────────────────────────────────────────

def execute_research_plan(plan: dict) -> int:
    """Execute one research target. Returns number of papers added."""
    log.info("Research target: %s", plan.get('focus', 'unnamed'))
    log.info("Rationale: %s", plan.get('rationale', ''))

    papers_added = 0
    queries = plan.get('queries', [])
    sources = plan.get('sources', ['semantic_scholar'])
    since = datetime.datetime.now() - datetime.timedelta(days=365)  # Broader window

    for query in queries:
        for source in sources:
            if source == 'semantic_scholar':
                # Custom Semantic Scholar search with this specific query
                params = urllib.parse.urlencode({
                    'query': query,
                    'limit': 20,
                    'fields': 'title,authors,year,abstract,externalIds,url,venue,citationCount,publicationDate',
                    'year': f'{since.year}-',
                })
                url = f'https://api.semanticscholar.org/graph/v1/paper/search?{params}'
                req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki-Ralph/2.0'})
                raw = _urlopen_with_backoff(req, 'Semantic Scholar', query)
                if raw:
                    data = json.loads(raw)
                    for item in data.get('data', []):
                        ext_ids = item.get('externalIds', {})
                        authors = [a.get('name', '') for a in item.get('authors', [])
                                   if a.get('name')]
                        paper = {
                            'source': 'semantic-scholar',
                            'source_id': item.get('paperId', ''),
                            'title': item.get('title', ''),
                            'authors': authors,
                            'year': str(item.get('year', '')),
                            'date': item.get('publicationDate', '') or '',
                            'abstract': item.get('abstract', '') or '',
                            'categories': [],
                            'url': item.get('url', ''),
                            'doi': ext_ids.get('DOI', ''),
                            'arxiv_id': ext_ids.get('ArXiv', ''),
                            'venue': item.get('venue', '') or '',
                            'citation_count': item.get('citationCount'),
                        }
                        # Relevance filter: skip papers with no TVB-related terms
                        text = (paper['title'] + ' ' + paper['abstract']).lower()
                        tvb_terms = ['brain', 'neural', 'connectiv', 'epilep', 'whole-brain',
                                     'mass model', 'cortical', 'fmri', 'eeg', 'dti',
                                     'connectome', 'neuroimag', 'simulation', 'modeling',
                                     'spiking', 'bifurcation', 'seizure', 'tractograph']
                        if not any(t in text for t in tvb_terms):
                            continue
                        slug = paper_slug(paper)
                        if not is_already_ingested(slug):
                            if save_raw_paper(paper):
                                papers_added += 1
                                log.info("Found: %s", paper['title'][:60])

            elif source == 'arxiv':
                # Use the ingestor's arxiv fetcher with ONLY the specific query
                # Wrap in arXiv-compatible format (arXiv uses same search syntax)
                arxiv_papers = fetch_arxiv(since_date=since, max_per_query=10, queries=[query])
                # Filter: only keep papers matching the query intent
                query_terms = [t.lower().strip('"') for t in query.split() if len(t) > 3]
                for paper in arxiv_papers:
                    text = (paper['title'] + ' ' + paper.get('abstract', '')).lower()
                    if sum(1 for t in query_terms if t in text) >= 2:
                        slug = paper_slug(paper)
                        if not is_already_ingested(slug):
                            if save_raw_paper(paper):
                                papers_added += 1
                                log.info("Found: %s", paper['title'][:60])

            import time
            time.sleep(2)  # Rate limit

    # Citation chaining: follow citations from any high-value papers found
    if papers_added > 0 and 'semantic_scholar' in sources:
        log.info("Following citation chains...")
        # Find any newly-added papers with S2 IDs
        for fn in sorted(os.listdir(RAW_PAPERS_DIR)):
            if not fn.endswith('.md') or 'semanticscholar' not in fn:
                continue
            fp = os.path.join(RAW_PAPERS_DIR, fn)
            # Only chain from recent papers (added in last hour)
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(fp))
            if (datetime.datetime.now() - mtime).seconds > 3600:
                continue

            s2_id_match = re.search(r'semanticscholar[-]([a-f0-9]+)', fn)
            if not s2_id_match:
                continue
            s2_id = s2_id_match.group(1)

            # Follow forward citations (who cited this paper?)
            cited_by = fetch_citations(s2_id, direction='citations', limit=10)
            for paper in cited_by:
                slug = paper_slug(paper)
                if not is_already_ingested(slug):
                    # Only add if it mentions TVB-related keywords
                    text = (paper.get('title', '') + ' ' + paper.get('abstract', '')).lower()
                    tvb_terms = ['brain', 'neural', 'connectiv', 'epilep', 'whole-brain',
                                 'mass model', 'cortical', 'fmri', 'eeg', 'dti']
                    if sum(1 for t in tvb_terms if t in text) >= 2:
                        if save_raw_paper(paper):
                            papers_added += 1
                            log.info("Citation chain: %s", paper['title'][:60])
            break  # Only chain from one paper per cycle

    return papers_added


# ── Main deep research cycle ──────────────────────────────────────────

def run_deep_research_cycle():
    """Run one deep research cycle. Returns papers added."""
    log.info("Starting deep research cycle")

    # 1. Plan research targets
    plans = plan_research()

    if not plans:
        log.info("No research targets identified. Nothing to do.")
        return 0

    # 2. Execute each plan
    total_added = 0
    for i, plan in enumerate(plans):
        log.info("── Target %d/%d ──", i + 1, len(plans))
        added = execute_research_plan(plan)
        total_added += added
        log.info("Target '%s': %d papers added", plan.get('focus', ''), added)

    # 3. Create stubs for newly-mentioned entities
    # (Re-scan recent papers for mentions)
    counts = load_entity_counts()
    for fn in sorted(os.listdir(RAW_PAPERS_DIR)):
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(RAW_PAPERS_DIR, fn)
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(fp))
        if (datetime.datetime.now() - mtime).seconds > 3600:
            continue
        try:
            with open(fp, 'r') as f:
                content = f.read()
            # Quick mock paper for mention extraction
            mock_paper = {'title': '', 'abstract': content[:2000]}
            mentions = extract_mentions(mock_paper)
            for cat in ['software', 'concepts']:
                for (keyword, slug, tag) in mentions.get(cat, set()):
                    if keyword not in counts[cat]:
                        counts[cat][keyword] = 0
                    counts[cat][keyword] += 1
        except Exception:
            pass

    save_entity_counts(counts)

    # 4. Git commit
    if total_added > 0:
        msg = f"DeepResearch: {total_added} papers via gap analysis + citation chaining (DeepResearch)"
        git_commit(msg)
        append_log(f"DeepResearch: {total_added} papers added via focused research")
        log.info("Committed: \"%s\"", msg)

    log.info("Cycle complete. %d papers added.", total_added)
    return total_added


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    run_deep_research_cycle()
