#!/usr/bin/env python3
"""
Convert Obsidian‑style wikilinks [[page]] to standard Markdown links.
Maps link text to page title or filename.
"""
import os, re, sys, argparse, unicodedata
import frontmatter

def normalize(text):
    """Convert any dash‑like characters and spaces to hyphens, lower case."""
    # replace non‑breaking hyphen (U+2011), en dash, em dash, hyphen‑minus, spaces
    text = re.sub(r'[\s\u2010-\u2015\u002d\u00ad\u2011\u2212]+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text.lower()

def find_markdown_files(root):
    """Yield all .md files under root."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for f in filenames:
            if f.lower().endswith('.md'):
                yield os.path.join(dirpath, f)

def build_title_map(docs_root):
    """Return dict mapping normalized page title to relative path (without extension)."""
    title_to_path = {}
    for path in find_markdown_files(docs_root):
        rel = os.path.relpath(path, docs_root)
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
                base = os.path.splitext(os.path.basename(path))[0]
                norm_base = normalize(base)
                title_to_path[norm_base] = os.path.splitext(rel)[0]
    return title_to_path

def convert_wikilinks_in_file(path, title_map, dry_run=False):
    """Replace wikilinks in the file with markdown links."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = re.compile(r'\[\[([^\]]+)\]\]')
    changes = []
    
    def replace(match):
        inner = match.group(1)
        if '|' in inner:
            target, alias = inner.split('|', 1)
            target = target.strip()
            alias = alias.strip()
        else:
            target = inner.strip()
            alias = target
        
        norm = normalize(target)
        if norm in title_map:
            rel_path = title_map[norm]
            if not rel_path.endswith('.md'):
                rel_path += '.md'
            current_dir = os.path.dirname(path)
            # target_full is inside docs/
            target_full = os.path.join(os.path.dirname(docs_root), 'docs', rel_path)
            rel_link = os.path.relpath(target_full, current_dir)
            changes.append((target, rel_link))
            return f'[{alias}]({rel_link})'
        else:
            if target not in ['wikilinks']:
                print(f"  Warning: unknown link target '{target}' (normalized '{norm}') in {path}")
            return match.group(0)
    
    new_content = pattern.sub(replace, content)
    if new_content != content and not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return len(changes) > 0, changes

def main():
    parser = argparse.ArgumentParser(description="Convert wikilinks to markdown links")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be changed without writing")
    parser.add_argument("--verbose", action="store_true", help="Print mapping and changes")
    args = parser.parse_args()
    
    docs_root = os.path.join(os.path.dirname(__file__), '..', 'docs')
    docs_root = os.path.abspath(docs_root)
    print(f"Building title map from {docs_root}...")
    title_map = build_title_map(docs_root)
    print(f"Found {len(title_map)} title mappings.")
    
    if args.verbose:
        for norm, rel in sorted(title_map.items()):
            print(f"  {norm} -> {rel}")
    
    converted = 0
    total_changes = 0
    for path in find_markdown_files(docs_root):
        changed, changes = convert_wikilinks_in_file(path, title_map, dry_run=args.dry_run)
        if changed:
            converted += 1
            total_changes += len(changes)
            if args.verbose:
                print(f"  {os.path.relpath(path, docs_root)}: {len(changes)} links")
                for target, link in changes[:3]:
                    print(f"    [[{target}]] → {link}")
    
    if args.dry_run:
        print(f"Dry run: would convert {total_changes} links in {converted} files.")
    else:
        print(f"Converted {total_changes} wikilinks in {converted} files.")

if __name__ == '__main__':
    main()