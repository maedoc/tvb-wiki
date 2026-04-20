#!/usr/bin/env python3
"""
Hourly update script for TVB Wiki.
Fetches new arXiv papers, updates entity/concept pages, rebuilds index.
"""
import os, sys, json, datetime, urllib.request, urllib.parse, xml.etree.ElementTree as ET, re, time, pathlib, collections, textwrap, itertools, math, random, string, subprocess, warnings, typing, pprint, html

# Set environment for Obsidian skill
os.environ['OBSIDIAN_VAULT_PATH'] = os.path.expanduser('~/tvb-wiki')

wiki_path = os.path.expanduser('~/tvb-wiki')
meta_dir = os.path.join(wiki_path, 'meta')
raw_papers_dir = os.path.join(wiki_path, 'raw', 'papers')
raw_articles_dir = os.path.join(wiki_path, 'raw', 'articles')
scripts_dir = os.path.join(wiki_path, 'scripts')
entities_dir = os.path.join(wiki_path, 'entities')
concepts_dir = os.path.join(wiki_path, 'concepts')
os.makedirs(meta_dir, exist_ok=True)
os.makedirs(raw_papers_dir, exist_ok=True)
os.makedirs(raw_articles_dir, exist_ok=True)
os.makedirs(scripts_dir, exist_ok=True)
os.makedirs(entities_dir, exist_ok=True)
os.makedirs(concepts_dir, exist_ok=True)

# Paths
last_update_file = os.path.join(meta_dir, 'last_update.txt')
entity_counts_file = os.path.join(meta_dir, 'entity_counts.json')

# Load last update time
def load_last_update():
    if os.path.exists(last_update_file):
        with open(last_update_file, 'r') as f:
            s = f.read().strip()
            try:
                return datetime.datetime.fromisoformat(s)
            except:
                pass
    # default: 7 days ago
    return datetime.datetime.now() - datetime.timedelta(days=7)

def save_last_update():
    with open(last_update_file, 'w') as f:
        f.write(datetime.datetime.now().isoformat())

# Load entity counts
def load_entity_counts():
    if os.path.exists(entity_counts_file):
        with open(entity_counts_file, 'r') as f:
            return json.load(f)
    return {'software': {}, 'concepts': {}, 'authors': {}}

def save_entity_counts(counts):
    with open(entity_counts_file, 'w') as f:
        json.dump(counts, f, indent=2)

# arXiv search
NS = {'a': 'http://www.w3.org/2005/Atom'}

def fetch_arxiv_since(since_date, max_results=30):
    """Fetch papers from arXiv submitted after since_date."""
    since_str = since_date.strftime('%Y%m%d')
    queries = [
        'cat:q-bio.NC+AND+all:connectome',
        'all:neural+mass+model',
        'all:dynamic+causal+modeling',
        'all:The+Virtual+Brain',
        'all:TVB',
        'all:whole+brain+model',
    ]
    papers = []
    seen = set()
    for query in queries:
        params = {
            'search_query': query,
            'max_results': str(max_results),
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        url = 'https://export.arxiv.org/api/query?' + '&'.join(f'{k}={urllib.parse.quote(v)}' for k, v in params.items())
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesAgent/1.0'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
        except Exception as e:
            print(f"arXiv error: {e}")
            continue
        root = ET.fromstring(data)
        entries = root.findall('a:entry', NS)
        for entry in entries:
            title = entry.find('a:title', NS).text.strip().replace('\n', ' ') if entry.find('a:title', NS) is not None else ''
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
        time.sleep(1)
    return papers

# Save raw paper
def save_raw_paper(paper):
    filename = f"arxiv-{paper['arxiv_id']}.md"
    filepath = os.path.join(raw_papers_dir, filename)
    if os.path.exists(filepath):
        return False  # already exists
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

# Extract entities/concepts from paper (simplified)
def extract_entities(paper):
    text = paper['title'] + ' ' + paper['abstract']
    text_lower = text.lower()
    software = []
    for kw in ['TVB', 'The Virtual Brain', 'NEST', 'NEURON', 'Brian', 'ANTs', 'SPM', 'FSL', 'FreeSurfer']:
        if kw.lower() in text_lower:
            software.append(kw)
    concepts = []
    for kw in ['neural mass model', 'dynamic causal modeling', 'Wilson-Cowan', 'Jansen-Rit', 'fMRI', 'EEG', 'MEG', 'DTI', 'functional connectivity', 'structural connectivity', 'effective connectivity', 'resting-state', 'whole-brain', 'connectomics', 'brain network', 'epilepsy', 'schizophrenia', 'aging', 'neurodevelopment']:
        if kw.lower() in text_lower:
            concepts.append(kw)
    authors = paper['authors']
    return {'software': software, 'concepts': concepts, 'authors': authors}

# Update entity counts
def update_counts(counts, extracted):
    for cat in ['software', 'concepts', 'authors']:
        for item in extracted[cat]:
            if item not in counts[cat]:
                counts[cat][item] = 0
            counts[cat][item] += 1

# Ensure entity/concept pages exist (threshold >= 2)
def ensure_pages(counts, threshold=2):
    # Software
    for name, cnt in counts['software'].items():
        if cnt >= threshold:
            filename = name.lower().replace(' ', '-').replace('.', '') + '.md'
            filepath = os.path.join(entities_dir, filename)
            if not os.path.exists(filepath):
                create_software_page(name, filepath)
    # Authors (maybe threshold 3)
    for name, cnt in counts['authors'].items():
        if cnt >= 3:
            filename = name.lower().replace(' ', '-') + '.md'
            filepath = os.path.join(entities_dir, filename)
            if not os.path.exists(filepath):
                create_author_page(name, filepath)
    # Concepts
    for name, cnt in counts['concepts'].items():
        if cnt >= threshold:
            filename = name.lower().replace(' ', '-').replace('‑', '-') + '.md'
            filepath = os.path.join(concepts_dir, filename)
            if not os.path.exists(filepath):
                create_concept_page(name, filepath)

def create_software_page(name, path):
    today = datetime.date.today().isoformat()
    tags = ['software']
    if name in ['TVB', 'The Virtual Brain']:
        tags.append('software-tvb')
    elif name == 'NEST':
        tags.append('software-nest')
    elif name == 'NEURON':
        tags.append('software-neuron')
    content = f"""# {name}

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
    frontmatter = f"""---
title: {name}
created: {today}
updated: {today}
type: entity
tags: [{', '.join(tags)}]
sources: []
---
"""
    with open(path, 'w') as f:
        f.write(frontmatter)
        f.write(content)
    print(f"Created software page: {name}")

def create_author_page(name, path):
    today = datetime.date.today().isoformat()
    content = f"""# {name}

Researcher in connectome‑based whole‑brain modeling.

## Affiliations
*Placeholder*

## Key Publications
*Placeholder*

## Research Focus
*Placeholder*

## Links
* [[TVB]]
* [[neural mass model]]
"""
    frontmatter = f"""---
title: {name}
created: {today}
updated: {today}
type: entity
tags: [people‑researcher]
sources: []
---
"""
    with open(path, 'w') as f:
        f.write(frontmatter)
        f.write(content)
    print(f"Created author page: {name}")

def create_concept_page(name, path):
    today = datetime.date.today().isoformat()
    # Map to tag
    tag_map = {
        'neural mass model': 'neural-mass-models',
        'dynamic causal modeling': 'dynamic-causal-modeling',
        'Wilson-Cowan': 'neural-mass-models',
        'Jansen-Rit': 'neural-mass-models',
        'fMRI': 'neuroimaging-fmri',
        'EEG': 'neuroimaging-eeg',
        'MEG': 'neuroimaging-meg',
        'DTI': 'neuroimaging-dti',
        'functional connectivity': 'functional-connectivity',
        'structural connectivity': 'structural-connectivity',
        'effective connectivity': 'effective-connectivity',
        'resting-state': 'resting-state',
        'whole-brain': 'whole-brain-modeling',
        'connectomics': 'connectomics',
        'brain network': 'network-dynamics',
        'epilepsy': 'epilepsy-modeling',
        'schizophrenia': 'schizophrenia-models',
        'aging': 'aging-brain',
        'neurodevelopment': 'neurodevelopment',
    }
    tag = tag_map.get(name, 'concept')
    content = f"""# {name}

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
    frontmatter = f"""---
title: {name}
created: {today}
updated: {today}
type: concept
tags: [{tag}]
sources: []
---
"""
    with open(path, 'w') as f:
        f.write(frontmatter)
        f.write(content)
    print(f"Created concept page: {name}")

# Rebuild index.md from existing pages
def rebuild_index():
    entity_files = []
    for f in os.listdir(entities_dir):
        if f.endswith('.md'):
            name = f[:-3].replace('-', ' ')
            entity_files.append(name)
    concept_files = []
    for f in os.listdir(concepts_dir):
        if f.endswith('.md'):
            name = f[:-3].replace('-', ' ')
            concept_files.append(name)
    today = datetime.date.today().isoformat()
    total = len(entity_files) + len(concept_files)
    with open(os.path.join(wiki_path, 'index.md'), 'w') as f:
        f.write(f"""# Wiki Index

> Content catalog. Every wiki page listed under its type with a one‑line summary.
> Read this first to find relevant pages for any query.
> Last updated: {today} | Total pages: {total}

## Entities
<!-- Alphabetical within section -->
""")
        for name in sorted(entity_files):
            f.write(f"- [[{name}]] – *placeholder summary*\n")
        f.write("\n## Concepts\n")
        for name in sorted(concept_files):
            f.write(f"- [[{name}]] – *placeholder summary*\n")
        f.write("\n## Comparisons\n\n## Queries\n")
    print(f"Rebuilt index.md with {total} pages.")

# Main update function
def run_hourly_update():
    print(f"Starting hourly update at {datetime.datetime.now().isoformat()}")
    last_update = load_last_update()
    print(f"Last update: {last_update.isoformat()}")
    
    # Fetch new arXiv papers
    new_papers = fetch_arxiv_since(last_update, max_results=20)
    print(f"Found {len(new_papers)} new arXiv papers.")
    
    # Load existing entity counts
    counts = load_entity_counts()
    
    added = 0
    for paper in new_papers:
        if save_raw_paper(paper):
            added += 1
            extracted = extract_entities(paper)
            update_counts(counts, extracted)
    
    print(f"Added {added} new raw papers.")
    
    # Save updated counts
    save_entity_counts(counts)
    
    # Ensure pages for entities/concepts that meet threshold
    ensure_pages(counts, threshold=2)
    
    # Rebuild index
    rebuild_index()
    
    # Append to log
    log_path = os.path.join(wiki_path, 'log.md')
    with open(log_path, 'a') as f:
        f.write(f"\n## [{datetime.date.today().isoformat()}] hourly | Added {added} new papers, updated pages\n")
    
    # Save last update timestamp
    save_last_update()
    
    print(f"Hourly update completed.")

if __name__ == '__main__':
    run_hourly_update()