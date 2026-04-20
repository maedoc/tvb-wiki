#!/usr/bin/env python3
"""
Sync the wiki source (entities/, concepts/, etc.) to the docs/ directory,
convert wikilinks, and optionally build the static site.
"""
import os, sys, shutil, subprocess, datetime, argparse

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(WIKI_ROOT, 'docs')

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def clean_dir(path):
    """Remove all .md files in directory, keep subdirectories."""
    if not os.path.exists(path):
        return
    for f in os.listdir(path):
        if f.endswith('.md'):
            os.remove(os.path.join(path, f))

def copy_md_files(src, dst):
    """Copy all .md files from src to dst."""
    if not os.path.exists(src):
        return 0
    count = 0
    for f in os.listdir(src):
        if f.endswith('.md'):
            shutil.copy2(os.path.join(src, f), os.path.join(dst, f))
            count += 1
    return count

def sync(args):
    print(f"🔀 Syncing wiki to docs at {datetime.datetime.now().isoformat()}")
    
    # Ensure directories
    for d in ['entities', 'concepts', 'comparisons', 'queries']:
        ensure_dir(os.path.join(DOCS_DIR, d))
    
    # Clean existing .md files (except index.md and about.md)
    for d in ['entities', 'concepts', 'comparisons', 'queries']:
        clean_dir(os.path.join(DOCS_DIR, d))
    
    # Copy source files
    ent_count = copy_md_files(
        os.path.join(WIKI_ROOT, 'entities'),
        os.path.join(DOCS_DIR, 'entities')
    )
    conc_count = copy_md_files(
        os.path.join(WIKI_ROOT, 'concepts'),
        os.path.join(DOCS_DIR, 'concepts')
    )
    
    # Copy index files if they exist
    index_files = [
        (os.path.join(WIKI_ROOT, 'index.md'), os.path.join(DOCS_DIR, 'index.md')),
        (os.path.join(WIKI_ROOT, 'SCHEMA.md'), os.path.join(DOCS_DIR, 'schema.md')),
        (os.path.join(WIKI_ROOT, 'about.md'), os.path.join(DOCS_DIR, 'about.md')),
        (os.path.join(WIKI_ROOT, 'comparisons', 'index.md'), os.path.join(DOCS_DIR, 'comparisons', 'index.md')),
        (os.path.join(WIKI_ROOT, 'queries', 'index.md'), os.path.join(DOCS_DIR, 'queries', 'index.md')),
    ]
    for src, dst in index_files:
        if os.path.exists(src):
            ensure_dir(os.path.dirname(dst))
            shutil.copy2(src, dst)
    
    print(f"  Copied {ent_count} entity files, {conc_count} concept files.")
    
    # Run wikilink conversion
    conv_script = os.path.join(WIKI_ROOT, 'scripts', 'convert_wikilinks.py')
    if os.path.exists(conv_script):
        subprocess.run([sys.executable, conv_script], cwd=WIKI_ROOT, check=False)
        print("  Ran wikilink conversion.")
    else:
        print("  Warning: convert_wikilinks.py not found.")
    
    # Build static site if requested
    if args.build:
        mkdocs_path = shutil.which('mkdocs')
        if mkdocs_path:
            print("  Building static site...")
            subprocess.run([mkdocs_path, 'build'], cwd=WIKI_ROOT, check=True)
            print("  Site built.")
        else:
            print("  Error: mkdocs not found in PATH.")
    
    print("✅ Sync complete.")

def main():
    parser = argparse.ArgumentParser(description="Sync wiki to docs directory")
    parser.add_argument("--build", action="store_true", help="Build static site after sync")
    args = parser.parse_args()
    sync(args)

if __name__ == '__main__':
    main()