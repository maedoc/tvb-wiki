#!/usr/bin/env python3
"""
Repair malformed markdown links in wiki pages.

Fixes:
  1. Wikilinks inside URLs: `https://www.[[nitrc]].org/...` -> `https://www.nitrc.org/...`
  2. Absolute file paths in links: `[text](/home/duke/src/tvb-wiki/eeg.md)` -> `[text](eeg.md)`
  3. Wikilinks inside link text that got mangled into URLs
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import get_logger, WIKI_ROOT, get_all_pages, git_commit, append_log

log = get_logger("LinkRepair")


REPO_PATH = "/home/duke/src/tvb-wiki"

def fix_wikilinks_in_urls(text: str) -> str:
    """Remove [[...]] wrappers inside URLs in markdown links."""
    def repl(m):
        url = m.group(1)
        # Remove [[word]] patterns inside URLs
        fixed = re.sub(r'\[\[([^\]]+)\]\]', r'\1', url)
        return f']({fixed})'
    return re.sub(r'\]\(([^)]+)\)', repl, text)


def fix_absolute_paths(text: str) -> str:
    """Strip absolute file paths back to just the filename."""
    def repl(m):
        before = m.group(1)
        url = m.group(2)
        after = m.group(3)
        
        # Handle /home/duke/src/tvb-wiki/... paths
        if url.startswith('/home/duke/src/tvb-wiki/'):
            url = url.replace('/home/duke/src/tvb-wiki/', '')
            # If it's entities/foo.md, keep as foo.md
            url = url.replace('entities/', '').replace('concepts/', '').replace('comparisons/', '')
        # Handle paths with spaces (escaped or not)
        url = url.replace(' ', '-')
        return f'{before}]({url}){after}'
    
    # Match ](url) followed by space or newline (not inside another URL)
    return re.sub(r'(\]\()([^)]+?)(\)(?:\s|$|\n|\\n|\.))', repl, text)


def repair_file(filepath: str) -> tuple[int, int]:
    """Repair a single file. Returns (wikilink_fixes, path_fixes)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        log.warn("Cannot read %s: %s", filepath, e)
        return (0, 0)
    
    fixed = fix_wikilinks_in_urls(text)
    wikilink_fixes = 1 if fixed != text else 0
    
    fixed2 = fix_absolute_paths(fixed)
    path_fixes = 1 if fixed2 != fixed else 0
    
    if fixed2 != text:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed2)
        return (wikilink_fixes, path_fixes)
    return (0, 0)


def run_link_repair_cycle():
    """Run repair across all wiki pages."""
    log.info("Starting link repair cycle")
    
    pages = get_all_pages()
    wikilink_total = 0
    path_total = 0
    files_changed = 0
    
    for slug, filepath in pages.items():
        w, p = repair_file(filepath)
        if w > 0 or p > 0:
            files_changed += 1
            wikilink_total += w
            path_total += p
            log.info("  Fixed %s: %d wikilink-in-URL, %d abs-path", slug, w, p)
    
    # Also fix files in docs/ (synced copies)
    docs_dir = os.path.join(WIKI_ROOT, 'docs')
    if os.path.isdir(docs_dir):
        for root, _, files in os.walk(docs_dir):
            for fn in files:
                if not fn.endswith('.md'):
                    continue
                filepath = os.path.join(root, fn)
                w, p = repair_file(filepath)
                if w > 0 or p > 0:
                    files_changed += 1
                    wikilink_total += w
                    path_total += p
    
    log.info("Done: %d files changed, %d wikilink-in-URL fixes, %d abs-path fixes",
             files_changed, wikilink_total, path_total)
    
    if files_changed > 0:
        msg = f"LinkRepair: fixed {files_changed} files ({wikilink_total} wikilink-in-URL, {path_total} abs-path)"
        git_commit(msg)
        append_log(msg)
    
    return files_changed


if __name__ == '__main__':
    run_link_repair_cycle()
