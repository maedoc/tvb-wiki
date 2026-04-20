#!/usr/bin/env python3
"""
Daily lint script for TVB Wiki.
Checks for orphan pages, broken internal links, and logs issues.
"""
import os, re, sys, json, datetime, collections, pathlib, warnings, typing, textwrap, itertools, math, random, string, hashlib, subprocess, time, html

# Set environment for Obsidian skill
os.environ['OBSIDIAN_VAULT_PATH'] = os.path.expanduser('~/tvb-wiki')

wiki_path = os.path.expanduser('~/tvb-wiki')
entities_dir = os.path.join(wiki_path, 'entities')
concepts_dir = os.path.join(wiki_path, 'concepts')
raw_papers_dir = os.path.join(wiki_path, 'raw', 'papers')
raw_articles_dir = os.path.join(wiki_path, 'raw', 'articles')

def scan_wiki():
    pages = []
    for root, dirs, files in os.walk(wiki_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, f), wiki_path)
                pages.append(rel_path)
    return pages

def find_internal_links(content):
    # wikilinks [[page]] or [[page|alias]]
    links = re.findall(r'\[\[([^\]]+)\]\]', content)
    clean_links = []
    for link in links:
        if '|' in link:
            link = link.split('|')[0]
        clean_links.append(link.strip())
    return clean_links

def lint():
    print("Starting lint of TVB wiki...")
    # 1. Orphan pages (pages not linked from index.md)
    index_path = os.path.join(wiki_path, 'index.md')
    with open(index_path, 'r') as f:
        index_content = f.read()
    index_links = find_internal_links(index_content)
    # convert to page names without extension
    index_page_names = {link.lower().replace(' ', '-') for link in index_links}
    
    orphan_pages = []
    for root, dirs, files in os.walk(entities_dir):
        for f in files:
            if f.endswith('.md'):
                page_name = f[:-3]
                if page_name not in index_page_names:
                    orphan_pages.append(os.path.join(root, f))
    for root, dirs, files in os.walk(concepts_dir):
        for f in files:
            if f.endswith('.md'):
                page_name = f[:-3]
                if page_name not in index_page_names:
                    orphan_pages.append(os.path.join(root, f))
    
    # 2. Broken internal links across all pages
    broken_links = []
    all_pages = []
    for root, dirs, files in os.walk(wiki_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                full = os.path.join(root, f)
                all_pages.append(full)
    # Build map from page name (lowercase hyphenated) to path
    page_name_map = {}
    for path in all_pages:
        rel = os.path.relpath(path, wiki_path)
        # convert to page name
        name = os.path.splitext(rel)[0].replace('/', '-').lower()
        page_name_map[name] = path
        # also map without subdirectory prefix?
        basename = os.path.basename(path)[:-3].lower()
        if basename not in page_name_map:
            page_name_map[basename] = path
    
    for path in all_pages:
        with open(path, 'r') as f:
            content = f.read()
        links = find_internal_links(content)
        for link in links:
            # normalize link: replace non-breaking hyphen, spaces, etc.
            norm = link.lower().replace(' ', '-').replace('‑', '-')
            if norm not in page_name_map:
                broken_links.append((path, link))
    
    # Output report
    print(f"\n=== Lint Report {datetime.date.today().isoformat()} ===")
    print(f"Total pages scanned: {len(all_pages)}")
    print(f"Orphan pages (not in index.md): {len(orphan_pages)}")
    for p in orphan_pages[:5]:
        print(f"  - {os.path.relpath(p, wiki_path)}")
    if len(orphan_pages) > 5:
        print(f"  ... and {len(orphan_pages)-5} more")
    print(f"Broken internal links: {len(broken_links)}")
    for path, link in broken_links[:5]:
        print(f"  - {os.path.relpath(path, wiki_path)} -> [[{link}]]")
    if len(broken_links) > 5:
        print(f"  ... and {len(broken_links)-5} more")
    
    # Write report to meta/lint.log
    meta_dir = os.path.join(wiki_path, 'meta')
    os.makedirs(meta_dir, exist_ok=True)
    log_path = os.path.join(meta_dir, 'lint.log')
    with open(log_path, 'a') as f:
        f.write(f"\n## Lint {datetime.datetime.now().isoformat()}\n")
        f.write(f"- Orphan pages: {len(orphan_pages)}\n")
        f.write(f"- Broken links: {len(broken_links)}\n")
        if orphan_pages:
            f.write("  Orphan list:\n")
            for p in orphan_pages:
                f.write(f"    - {os.path.relpath(p, wiki_path)}\n")
        if broken_links:
            f.write("  Broken links:\n")
            for path, link in broken_links:
                f.write(f"    - {os.path.relpath(path, wiki_path)} -> [[{link}]]\n")
    
    # Append summary to log.md
    log_md_path = os.path.join(wiki_path, 'log.md')
    with open(log_md_path, 'a') as f:
        f.write(f"\n## [{datetime.date.today().isoformat()}] lint | {len(orphan_pages)} orphan pages, {len(broken_links)} broken links\n")
    
    print("\nLint complete. Report saved to meta/lint.log and appended to log.md.")

if __name__ == '__main__':
    lint()