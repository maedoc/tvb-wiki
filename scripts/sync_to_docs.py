#!/usr/bin/env python3
"""
Sync the wiki source (entities/, concepts/, etc.) to the docs/ directory,
convert wikilinks, and optionally build the static site.
"""
import os, sys, shutil, pathlib, re, subprocess, datetime, json, warnings, typing, collections, itertools, math, random, string, hashlib, html, urllib.parse, frontmatter

wiki_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
docs_dir = os.path.join(wiki_root, 'docs')
entities_src = os.path.join(wiki_root, 'entities')
concepts_src = os.path.join(wiki_root, 'concepts')
comparisons_src = os.path.join(wiki_root, 'comparisons')
queries_src = os.path.join(wiki_root, 'queries')
raw_papers_src = os.path.join(wiki_root, 'raw', 'papers')

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def clean_dir(path, keep=None):
    """Remove all .md files in directory, keep subdirectories."""
    if not os.path.exists(path):
        return
    for f in os.listdir(path):
        if f.endswith('.md'):
            os.remove(os.path.join(path, f))

def copy_md_files(src, dst):
    """Copy all .md files from src to dst, preserving structure."""
    if not os.path.exists(src):
        return 0
    count = 0
    for f in os.listdir(src):
        if f.endswith('.md'):
            shutil.copy2(os.path.join(src, f), os.path.join(dst, f))
            count += 1
    return count

def sync():
    print(f"Syncing wiki to docs at {datetime.datetime.now().isoformat()}")
    
    # Ensure directories
    for d in ['entities', 'concepts', 'comparisons', 'queries']:
        ensure_dir(os.path.join(docs_dir, d))
    
    # Clean existing .md files (except index.md and about.md)
    for d in ['entities', 'concepts', 'comparisons', 'queries']:
        clean_dir(os.path.join(docs_dir, d))
    
    # Copy source files
    ent_count = copy_md_files(entities_src, os.path.join(docs_dir, 'entities'))
    conc_count = copy_md_files(concepts_src, os.path.join(docs_dir, 'concepts'))
    # Copy index files if they exist
    for src, dst in [
        (os.path.join(wiki_root, 'index.md'), os.path.join(docs_dir, 'index.md')),
        (os.path.join(wiki_root, 'SCHEMA.md'), os.path.join(docs_dir, 'schema.md')),
        (os.path.join(wiki_root, 'about.md'), os.path.join(docs_dir, 'about.md')),
        (os.path.join(comparisons_src, 'index.md'), os.path.join(docs_dir, 'comparisons', 'index.md')),
        (os.path.join(queries_src, 'index.md'), os.path.join(docs_dir, 'queries', 'index.md')),
    ]:
        if os.path.exists(src):
            shutil.copy2(src, dst)
    
    print(f"Copied {ent_count} entity files, {conc_count} concept files.")
    
    # Run wikilink conversion
    conv_script = os.path.join(wiki_root, 'scripts', 'convert_wikilinks.py')
    if os.path.exists(conv_script):
        subprocess.run([sys.executable, conv_script], cwd=wiki_root, check=False)
        print("Ran wikilink conversion.")
    else:
        print("Warning: convert_wikilinks.py not found.")
    
    # Optionally build the site
    build_site = False
    if len(sys.argv) > 1 and sys.argv[1] == '--build':
        build_site = True
    
    if build_site:
        subprocess.run(['mkdocs', 'build'], cwd=wiki_root, check=True)
        print("Built static site.")
    
    print("Sync complete.")

if __name__ == '__main__':
    sync()