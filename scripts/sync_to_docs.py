#!/usr/bin/env python3
"""
Sync wiki content into docs/ for MkDocs build WITHOUT converting wikilinks.
Wikilinks are resolved at build time by hooks/obsidian_support.py.
"""
import os, shutil
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIRS = ['entities', 'concepts', 'comparisons', 'raw', 'hooks', 'topics']
TARGET_DIR = os.path.join(REPO, 'docs')

def sync():
    # Ensure target dirs exist
    os.makedirs(TARGET_DIR, exist_ok=True)
    print(f"Syncing wiki to {TARGET_DIR} at {datetime.now().isoformat()}")
    
    copied = 0
    for d in SOURCE_DIRS:
        src = os.path.join(REPO, d)
        if not os.path.isdir(src):
            print(f"  Warning: {src} not found")
            continue
        dst = os.path.join(TARGET_DIR, d)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        n = sum(1 for _, _, fs in os.walk(dst) for _ in fs)
        copied += n
        print(f"  Copied {n} files from {d}/")
    
    # Copy root pages that are not already in docs/
    for fn in ['index.md', 'catalog.md', 'schema.md', 'about.md', 'log.md', 'queries']:
        src = os.path.join(REPO, fn)
        if os.path.exists(src):
            dst = os.path.join(TARGET_DIR, fn)
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
            copied += 1
            print(f"  Copied {fn}")
    
    print(f"✅ Sync complete. {copied} files total.")

if __name__ == '__main__':
    from datetime import datetime
    sync()
