#!/usr/bin/env python3
"""
Hourly update for TVB Wiki.
- Fetch new papers from arXiv (and optionally Exa)
- Create/update raw paper files
- Update entity/concept pages with new mentions
- Run index update and lint
- Optionally use Pi/Hermes for enrichment tasks
"""
import os, sys, json, datetime, re, time, subprocess, argparse
import urllib.request, urllib.parse, xml.etree.ElementTree as ET

WIKI_ROOT = os.path.expanduser("~/tvb-wiki")
META_DIR = os.path.join(WIKI_ROOT, "meta")
RAW_PAPERS_DIR = os.path.join(WIKI_ROOT, "raw", "papers")
ENTITIES_DIR = os.path.join(WIKI_ROOT, "entities")
CONCEPTS_DIR = os.path.join(WIKI_ROOT, "concepts")

LAST_UPDATE_FILE = os.path.join(META_DIR, 'last_update.txt')
ENTITY_COUNTS_FILE = os.path.join(META_DIR, 'entity_counts.json')

# -------------------------------------------------------------------
# arXiv fetching
# -------------------------------------------------------------------
NS = {'a': 'http://www.w3.org/2005/Atom'}

ARXIV_QUERIES = [
    'cat:q-bio.NC+AND+all:connectome',
    'all:neural+mass+model',
    'all:dynamic+causal+modeling',
    'all:The+Virtual+Brain',
    'all:TVB',
    'all:whole+brain+model',
    'all:functional+connectivity',
    'all:resting+state+fMRI',
    'all:diffusion+MRI+tractography',
    'all:brain+network',
]

def fetch_arxiv_since(since_date, max_results=30):
    """Fetch papers from arXiv submitted after since_date."""
    papers = []
    seen = set()
    for query in ARXIV_QUERIES:
        params = {
            'search_query': query,
            'max_results': str(max_results),
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        url = 'https://export.arxiv.org/api/query?' + '&'.join(
            f'{k}={urllib.parse.quote(v)}' for k, v in params.items()
        )
        req = urllib.request.Request(url, headers={'User-Agent': 'TVBWiki/1.0'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
        except Exception as e:
            print(f"  arXiv error on '{query}': {e}")
            continue
        
        root = ET.fromstring(data)
        entries = root.findall('a:entry', NS)
        for entry in entries:
            title_elem = entry.find('a:title', NS)
            title = title_elem.text.strip().replace('\n', ' ') if title_elem is not None else ''
            raw_id = entry.find('a:id', NS).text.strip() if entry.find('a:id', NS) is not None else ''
            arxiv_id = raw_id.split('/abs/')[-1] if '/abs/' in raw_id else raw_id
            base_id = arxiv_id.split('v')[0]
            if base_id in seen:
                continue
            published = entry.find('a:published', NS).text[:10] if entry.find('a:published', NS) is not None else ''
            try:
                pub_date = datetime.datetime.strptime(published, '%Y-%m-%d')
                if pub_date < since_date:
                    continue
            except:
                pass
            seen.add(base_id)
            updated = entry.find('a:updated', NS).text[:10] if entry.find('a:updated', NS) is not None else ''
            authors = [a.find('a:name', NS).text for a in entry.findall('a:author', NS)]
            summary = entry.find('a:summary', NS).text.strip().replace('\n', ' ') if entry.find('a:summary', NS) is not None else ''
            categories = [c.get('term') for c in entry.findall('a:category', NS)]
            papers.append({
                'arxiv_id': base_id,
                'title': title,
                'published': published,
                'updated': updated,
                'authors': authors,
                'abstract': summary,
                'categories': categories,
                'url_abs': f'https://arxiv.org/abs/{base_id}',
                'url_pdf': f'https://arxiv.org/pdf/{base_id}',
                'source': 'arxiv',
                'query': query
            })
        time.sleep(1)  # be polite
    return papers

def save_raw_paper(paper):
    """Save paper as markdown in raw/papers/."""
    filename = f"arxiv-{paper['arxiv_id']}.md"
    filepath = os.path.join(RAW_PAPERS_DIR, filename)
    if os.path.exists(filepath):
        return False
    os.makedirs(RAW_PAPERS_DIR, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(f"# {paper['title']}\n\n")
        f.write(f"**arXiv ID**: {paper['arxiv_id']}\n")
        f.write(f"**Published**: {paper['published']}\n")
        f.write(f"**Updated**: {paper['updated']}\n")
        f.write(f"**Authors**: {', '.join(paper['authors'])}\n")
        f.write(f"**Categories**: {', '.join(paper['categories'])}\n")
        f.write(f"**URL**: {paper['url_abs']}\n")
        f.write(f"**PDF**: {paper['url_pdf']}\n")
        f.write(f"**Source**: arXiv\n\n")
        f.write("## Abstract\n\n")
        f.write(paper['abstract'] + "\n")
    return True

# -------------------------------------------------------------------
# Exa search (optional)
# -------------------------------------------------------------------
def exa_search(query, since_date=None, max_results=10):
    """
    Search Exa for recent papers.
    Requires EXA_API_KEY environment variable and `exa-py` installed.
    Returns list of dicts similar to arXiv format.
    """
    try:
        from exa_py import Exa
        api_key = os.environ.get('EXA_API_KEY')
        if not api_key:
            print("  EXA_API_KEY not set, skipping Exa search")
            return []
        exa = Exa(api_key)
        # Build search parameters
        params = {
            'query': query,
            'num_results': max_results,
            'use_autoprompt': True,
        }
        if since_date:
            params['start_published_date'] = since_date.strftime('%Y-%m-%d')
        response = exa.search(**params)
        results = []
        for r in response.results:
            results.append({
                'title': r.title,
                'url': r.url,
                'authors': r.author if hasattr(r, 'author') else [],
                'published': r.published_date[:10] if r.published_date else '',
                'abstract': r.text[:500] if r.text else '',
                'source': 'exa',
                'query': query
            })
        return results
    except ImportError:
        print("  exa-py not installed, skipping Exa search")
        return []
    except Exception as e:
        print(f"  Exa error: {e}")
        return []

# -------------------------------------------------------------------
# Entity extraction and page management
# -------------------------------------------------------------------
KEYWORD_MAP = {
    'software': [
        ('TVB', 'tvb', 'software-tvb'),
        ('The Virtual Brain', 'tvb', 'software-tvb'),
        ('NEST', 'nest', 'software-nest'),
        ('NEURON', 'neuron', 'software-neuron'),
        ('Brian', 'brian', 'software-brian'),
        ('ANTs', 'ants', 'software-ants'),
        ('SPM', 'spm', 'software-spm'),
        ('FSL', 'fsl', 'software-fsl'),
        ('FreeSurfer', 'freesurfer', 'software-freesurfer'),
        ('GraphVar', 'graphvar', 'software-graphvar'),
    ],
    'concepts': [
        ('neural mass model', 'neural-mass-model', 'neural-mass-models'),
        ('Wilson-Cowan', 'wilson-cowan', 'neural-mass-models'),
        ('Jansen-Rit', 'jansen-rit', 'neural-mass-models'),
        ('fMRI', 'fmri', 'neuroimaging-fmri'),
        ('EEG', 'eeg', 'neuroimaging-eeg'),
        ('MEG', 'meg', 'neuroimaging-meg'),
        ('DTI', 'dti', 'neuroimaging-dti'),
        ('functional connectivity', 'functional-connectivity', 'functional-connectivity'),
        ('structural connectivity', 'structural-connectivity', 'structural-connectivity'),
        ('effective connectivity', 'effective-connectivity', 'effective-connectivity'),
        ('resting-state', 'resting-state', 'resting-state'),
        ('whole-brain', 'whole-brain-modeling', 'whole-brain-modeling'),
        ('connectomics', 'connectomics', 'connectomics'),
        ('brain network', 'brain-network', 'network-dynamics'),
        ('dynamic causal modeling', 'dynamic-causal-modeling', 'dynamic-causal-modeling'),
        ('mean-field theory', 'mean-field-theory', 'mean-field-theory'),
        ('variational Bayes', 'variational-inference', 'variational-inference'),
        ('bifurcation analysis', 'bifurcation-analysis', 'bifurcation-analysis'),
    ]
}

# Reverse mapping: keyword -> (slug, tag, category)
REVERSE_MAP = {}
for category, items in KEYWORD_MAP.items():
    for (keyword, slug, tag) in items:
        REVERSE_MAP[keyword] = (slug, tag, category)

def extract_entities_from_paper(paper):
    """Extract software and concept mentions from a paper."""
    text = paper.get('title', '') + ' ' + paper.get('abstract', '')
    text_lower = text.lower()
    extracted = {'software': [], 'concepts': []}
    
    for category, items in KEYWORD_MAP.items():
        for (keyword, slug, tag) in items:
            if keyword.lower() in text_lower:
                extracted[category].append({
                    'keyword': keyword,
                    'slug': slug,
                    'tag': tag
                })
    # Authors as entities (simplified)
    authors = paper.get('authors', [])
    extracted['authors'] = authors[:3]  # top 3 authors
    
    return extracted

def update_entity_counts(counts, extracted):
    """Update entity mention counts."""
    for cat in ['software', 'concepts']:
        for item in extracted.get(cat, []):
            key = item['keyword']
            if key not in counts[cat]:
                counts[cat][key] = 0
            counts[cat][key] += 1
    for author in extracted.get('authors', []):
        if author not in counts['authors']:
            counts['authors'][author] = 0
        counts['authors'][author] += 1

def ensure_page_exists(slug, page_type, title, tag):
    """Create a page if it doesn't exist."""
    if page_type == 'entity':
        dir_path = ENTITIES_DIR
    else:
        dir_path = CONCEPTS_DIR
    os.makedirs(dir_path, exist_ok=True)
    filepath = os.path.join(dir_path, f"{slug}.md")
    if os.path.exists(filepath):
        return False
    
    today = datetime.date.today().isoformat()
    frontmatter = f"""---
title: {title}
created: {today}
updated: {today}
type: {page_type}
tags: [{tag}]
sources: []
---
"""
    if page_type == 'entity':
        content = f"""# {title}

Software tool used in connectome‑based whole‑brain modeling.

## Overview
*Placeholder for description.*

## Key Features
*Placeholder*

## Usage in Whole‑Brain Modeling
*Placeholder*

## Related Software
* [[TVB]]
* [[NEST]]
* [[NEURON]]

## References
*Links to relevant papers.*
"""
    else:
        content = f"""# {title}

Key concept in connectome‑based whole‑brain modeling.

## Definition
*Placeholder for formal definition.*

## Role in Whole‑Brain Modeling
*Placeholder for how this concept is used in modeling.*

## Related Concepts
* [[neural mass model]]
* [[functional connectivity]]
* [[whole‑brain]]

## References
*Links to relevant papers.*
"""
    
    with open(filepath, 'w') as f:
        f.write(frontmatter)
        f.write(content)
    return True

# -------------------------------------------------------------------
# Pi/Hermes enrichment
# -------------------------------------------------------------------
def run_pi_enrichment():
    """
    Use Pi CLI to enrich placeholder pages.
    Runs a Pi session that:
    1. Scans for pages with *Placeholder* content
    2. For each, generates a research prompt
    3. Updates page with real content
    """
    print("\n🤖 Running Pi enrichment session...")
    # First, find placeholder pages
    placeholder_pages = []
    for dir_path, dir_name in [(ENTITIES_DIR, 'entities'), (CONCEPTS_DIR, 'concepts')]:
        if not os.path.exists(dir_path):
            continue
        for filename in os.listdir(dir_path):
            if filename.endswith('.md'):
                filepath = os.path.join(dir_path, filename)
                with open(filepath, 'r') as f:
                    content = f.read()
                if '*Placeholder*' in content or 'needs summary' in content:
                    placeholder_pages.append((filepath, dir_name))
    
    if not placeholder_pages:
        print("  No placeholder pages found.")
        return
    
    print(f"  Found {len(placeholder_pages)} pages with placeholders")
    
    # For demonstration, we'll just create a script that the user can run.
    # In a real setup, you'd invoke Pi with a prompt.
    script_path = os.path.join(META_DIR, 'enrich_placeholder_pages.sh')
    with open(script_path, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Pi commands to enrich placeholder pages\n")
        f.write("# Run each command in a Pi session\n\n")
        for filepath, dir_name in placeholder_pages[:5]:  # limit to 5
            slug = os.path.basename(filepath)[:-3]
            title = slug.replace('-', ' ')
            f.write(f"# {title}\n")
            f.write(f'pi --model kimi-k2.5 -p "Read the file {filepath} and the wiki SCHEMA.md. '\
                    f'Research the topic \\"{title}\\" in whole‑brain modeling and neural mass models. '\
                    f'Update the page with real content, citations, and proper wikilinks. '\
                    f'Return the complete updated markdown." > {filepath}.updated\n')
            f.write(f"# Then: mv {filepath}.updated {filepath}\n\n")
    
    os.chmod(script_path, 0o755)
    print(f"  Generated enrichment script: {script_path}")
    print("  ⚠️  Review and run manually (requires Pi CLI setup)")

# -------------------------------------------------------------------
# Main workflow
# -------------------------------------------------------------------
def load_last_update():
    if os.path.exists(LAST_UPDATE_FILE):
        with open(LAST_UPDATE_FILE, 'r') as f:
            s = f.read().strip()
            try:
                return datetime.datetime.fromisoformat(s)
            except:
                pass
    return datetime.datetime.now() - datetime.timedelta(days=7)

def save_last_update():
    with open(LAST_UPDATE_FILE, 'w') as f:
        f.write(datetime.datetime.now().isoformat())

def load_entity_counts():
    if os.path.exists(ENTITY_COUNTS_FILE):
        with open(ENTITY_COUNTS_FILE, 'r') as f:
            return json.load(f)
    return {'software': {}, 'concepts': {}, 'authors': {}}

def save_entity_counts(counts):
    with open(ENTITY_COUNTS_FILE, 'w') as f:
        json.dump(counts, f, indent=2)

def run_hourly_update(args):
    """Main update workflow."""
    print(f"🔍 Hourly update started at {datetime.datetime.now().isoformat()}")
    os.makedirs(META_DIR, exist_ok=True)
    
    # 1. Fetch new papers
    last_update = load_last_update()
    print(f"  Last update: {last_update.isoformat()}")
    
    new_papers = []
    if not args.skip_arxiv:
        print("  Fetching arXiv papers...")
        arxiv_papers = fetch_arxiv_since(last_update, max_results=args.max_results)
        print(f"    Found {len(arxiv_papers)} new arXiv papers")
        new_papers.extend(arxiv_papers)
    
    if args.use_exa:
        print("  Searching Exa...")
        # Simple query for TVB/whole-brain modeling
        exa_results = exa_search("whole brain modeling The Virtual Brain", since_date=last_update)
        print(f"    Found {len(exa_results)} Exa results")
        new_papers.extend(exa_results)
    
    # 2. Save raw papers
    added = 0
    counts = load_entity_counts()
    for paper in new_papers:
        if save_raw_paper(paper):
            added += 1
            extracted = extract_entities_from_paper(paper)
            update_entity_counts(counts, extracted)
    
    print(f"  Added {added} new raw papers")
    
    # 3. Update entity counts and ensure pages for frequent mentions
    save_entity_counts(counts)
    if not args.skip_pages:
        print("  Ensuring pages for frequent entities...")
        threshold = 2
        for cat in ['software', 'concepts']:
            for key, cnt in counts[cat].items():
                if cnt >= threshold and key in REVERSE_MAP:
                    slug, tag, category = REVERSE_MAP[key]
                    page_type = 'entity' if cat == 'software' else 'concept'
                    if ensure_page_exists(slug, page_type, key, tag):
                        print(f"    Created {page_type}: {key}")
    
    # 4. Update index and lint
    if not args.skip_index:
        print("  Updating index and linting...")
        subprocess.run(
            [sys.executable, os.path.join(WIKI_ROOT, 'scripts', 'update_index.py')],
            cwd=WIKI_ROOT,
            capture_output=False
        )
    
    # 5. Pi enrichment (optional)
    if args.enrich:
        run_pi_enrichment()
    
    # 6. Save timestamp
    save_last_update()
    
    # 7. Log
    log_path = os.path.join(WIKI_ROOT, 'log.md')
    with open(log_path, 'a') as f:
        f.write(f"\n## [{datetime.date.today().isoformat()}] hourly | Added {added} new papers\n")
    
    print(f"\n✅ Hourly update completed. Added {added} new papers.")

def main():
    parser = argparse.ArgumentParser(description="TVB Wiki hourly update")
    parser.add_argument("--skip-arxiv", action="store_true", help="Skip arXiv fetching")
    parser.add_argument("--use-exa", action="store_true", help="Use Exa search (requires EXA_API_KEY)")
    parser.add_argument("--skip-pages", action="store_true", help="Skip creating/updating entity pages")
    parser.add_argument("--skip-index", action="store_true", help="Skip index update")
    parser.add_argument("--enrich", action="store_true", help="Run Pi enrichment on placeholder pages")
    parser.add_argument("--max-results", type=int, default=30, help="Max papers per arXiv query")
    args = parser.parse_args()
    
    run_hourly_update(args)

if __name__ == '__main__':
    main()