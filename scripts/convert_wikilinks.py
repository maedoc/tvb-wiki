#!/usr/bin/env python3
"""
Convert Obsidian‑style wikilinks [[page]] to standard Markdown links.
Maps link text to page title or filename.
"""
import os, re, sys, frontmatter, pathlib, warnings, typing, collections, itertools, json, hashlib, math, random, string, datetime, html, urllib.parse, shutil, subprocess, unicodedata

def normalize(text):
    """Convert any dash‑like characters and spaces to hyphens, lower case."""
    # replace non‑breaking hyphen (U+2011), en dash, em dash, hyphen‑minus, etc.
    # also replace spaces
    text = re.sub(r'[\s\u2010-\u2015\u002d\u00ad\u2011\u2212]+', '-', text)
    # collapse multiple hyphens
    text = re.sub(r'-+', '-', text)
    # strip leading/trailing hyphens
    text = text.strip('-')
    return text.lower()

def find_markdown_files(root):
    """Yield all .md files under root."""
    for dirpath, dirnames, filenames in os.walk(root):
        # skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for f in filenames:
            if f.lower().endswith('.md'):
                yield os.path.join(dirpath, f)

def build_title_map(docs_root):
    """Return dict mapping normalized page title to relative path (without extension)."""
    title_to_path = {}
    for path in find_markdown_files(docs_root):
        rel = os.path.relpath(path, docs_root)
        # skip raw papers
        if rel.startswith('raw/'):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            try:
                post = frontmatter.load(f)
                title = post.get('title')
                if title:
                    norm = normalize(title)
                    title_to_path[norm] = os.path.splitext(rel)[0]
                # also map filename without extension
                base = os.path.splitext(os.path.basename(path))[0]
                norm_base = normalize(base)
                title_to_path[norm_base] = os.path.splitext(rel)[0]
            except Exception as e:
                print(f"Warning: could not parse frontmatter in {path}: {e}")
                # fallback to filename
                base = os.path.splitext(os.path.basename(path))[0]
                norm_base = normalize(base)
                title_to_path[norm_base] = os.path.splitext(rel)[0]
    return title_to_path

def convert_wikilinks_in_file(path, title_map):
    """Replace wikilinks in the file with markdown links."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # pattern: [[page]] or [[page|alias]]
    pattern = re.compile(r'\[\[([^\]]+)\]\]')
    def replace(match):
        inner = match.group(1)
        # split by pipe
        if '|' in inner:
            target, alias = inner.split('|', 1)
            target = target.strip()
            alias = alias.strip()
        else:
            target = inner.strip()
            alias = target
        # normalize target for lookup
        norm = normalize(target)
        if norm in title_map:
            rel_path = title_map[norm]
            # ensure .md extension
            if not rel_path.endswith('.md'):
                rel_path += '.md'
            # relative link from current file to target
            current_dir = os.path.dirname(path)
            target_full = os.path.join(os.path.dirname(docs_root), 'docs', rel_path)
            # compute relative path from current file to target full
            rel_link = os.path.relpath(target_full, current_dir)
            return f'[{alias}]({rel_link})'
        else:
            # keep original wikilink (will be broken)
            # skip known placeholder targets
            if target in ['wikilinks']:
                return match.group(0)
            print(f"Warning: unknown link target '{target}' (normalized '{norm}') in {path}")
            # optionally keep as wikilink
            return match.group(0)
    
    new_content = pattern.sub(replace, content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == '__main__':
    docs_root = os.path.join(os.path.dirname(__file__), '..', 'docs')
    docs_root = os.path.abspath(docs_root)
    print(f"Building title map from {docs_root}...")
    title_map = build_title_map(docs_root)
    print(f"Found {len(title_map)} title mappings.")
    # Debug: print mapping
    for norm, rel in sorted(title_map.items()):
        print(f"  {norm} -> {rel}")
    
    converted = 0
    for path in find_markdown_files(docs_root):
        if convert_wikilinks_in_file(path, title_map):
            converted += 1
    print(f"Converted wikilinks in {converted} files.")