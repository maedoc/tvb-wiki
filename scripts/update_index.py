#!/usr/bin/env python3
"""
Update index.md with real summaries extracted from pages.
Also performs linting: broken links, orphan pages (no inbound links), pages missing from index.
Logs issues to meta/lint.log and log.md.
"""
import os, re, datetime, json, argparse

WIKI_ROOT = os.path.expanduser("~/tvb-wiki")
ENTITIES_DIR = os.path.join(WIKI_ROOT, "entities")
CONCEPTS_DIR = os.path.join(WIKI_ROOT, "concepts")
COMPARISONS_DIR = os.path.join(WIKI_ROOT, "comparisons")
INDEX_PATH = os.path.join(WIKI_ROOT, "index.md")
META_DIR = os.path.join(WIKI_ROOT, "meta")
LOG_MD = os.path.join(WIKI_ROOT, "log.md")

def extract_summary(filepath):
    """Extract first paragraph or description from a wiki page."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line or line.startswith('---') or line.startswith('#'):
            continue
        if '*Placeholder*' in line or line.startswith('* [['):
            continue
        if line.startswith('Software tool') or line.startswith('Key concept'):
            continue
        if len(line) > 20:
            return line[:100] + ('...' if len(line) > 100 else '')
    return None

def get_all_wikilinks():
    """Extract all wikilinks from all pages."""
    all_links = set()
    all_pages = set()
    
    for directory in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR]:
        if not os.path.exists(directory):
            continue
        for filename in os.listdir(directory):
            if filename.endswith('.md'):
                page_name = filename[:-3]
                all_pages.add(page_name)
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as f:
                    content = f.read()
                links = re.findall(r'\[\[([^\]]+)\]\]', content)
                for link in links:
                    # Remove alias
                    if '|' in link:
                        link = link.split('|')[0]
                    normalized = link.lower().replace(' ', '-').replace('‑', '-')
                    all_links.add((normalized, page_name))
    return all_links, all_pages

def find_broken_links(all_links, all_pages):
    """Find links that point to non-existent pages."""
    broken = []
    for link, source in all_links:
        if link not in all_pages:
            broken.append((link, source))
    return broken

def find_orphan_pages_no_inbound(all_links, all_pages):
    """Find pages with no inbound links."""
    linked_pages = set(link for link, _ in all_links)
    orphans = all_pages - linked_pages
    return orphans

def find_pages_missing_from_index():
    """Find pages not listed in index.md (classic orphan detection)."""
    with open(INDEX_PATH, 'r') as f:
        index_content = f.read()
    index_links = re.findall(r'\[\[([^\]]+)\]\]', index_content)
    index_page_names = {link.lower().replace(' ', '-') for link in index_links}
    
    missing = []
    for directory in [ENTITIES_DIR, CONCEPTS_DIR]:
        if not os.path.exists(directory):
            continue
        for filename in os.listdir(directory):
            if filename.endswith('.md'):
                page_name = filename[:-3]
                if page_name not in index_page_names:
                    missing.append(os.path.join(directory, filename))
    return missing

def generate_index():
    """Generate the index.md content."""
    entities = []
    for filename in sorted(os.listdir(ENTITIES_DIR)):
        if filename.endswith('.md'):
            filepath = os.path.join(ENTITIES_DIR, filename)
            name = filename[:-3].replace('-', ' ')
            summary = extract_summary(filepath) or "*needs summary*"
            entities.append((name, filename[:-3], summary))
    
    concepts = []
    for filename in sorted(os.listdir(CONCEPTS_DIR)):
        if filename.endswith('.md'):
            filepath = os.path.join(CONCEPTS_DIR, filename)
            name = filename[:-3].replace('-', ' ')
            summary = extract_summary(filepath) or "*needs summary*"
            concepts.append((name, filename[:-3], summary))
    
    comparisons = []
    if os.path.exists(COMPARISONS_DIR):
        for filename in sorted(os.listdir(COMPARISONS_DIR)):
            if filename.endswith('.md') and filename != 'index.md':
                filepath = os.path.join(COMPARISONS_DIR, filename)
                name = filename[:-3].replace('-', ' ')
                summary = extract_summary(filepath) or "*needs summary*"
                comparisons.append((name, filename[:-3], summary))
    
    lines = [
        "# Wiki Index",
        "",
        "> Content catalog. Every wiki page listed under its type with a one‑line summary.",
        "> Read this first to find relevant pages for any query.",
    ]
    
    today = datetime.date.today().isoformat()
    total = len(entities) + len(concepts) + len(comparisons)
    lines.append(f"> Last updated: {today} | Total pages: {total}")
    lines.append("")
    
    lines.append("## Entities")
    lines.append("<!-- Software, people, datasets, labs -->")
    for name, slug, summary in entities:
        lines.append(f"- [[{name}]] – {summary}")
    lines.append("")
    
    lines.append("## Concepts")
    lines.append("<!-- Methods, modalities, topics -->")
    for name, slug, summary in concepts:
        lines.append(f"- [[{name}]] – {summary}")
    lines.append("")
    
    if comparisons:
        lines.append("## Comparisons")
        lines.append("<!-- Side-by-side analyses -->")
        for name, slug, summary in comparisons:
            lines.append(f"- [[{name}]] – {summary}")
        lines.append("")
    
    lines.append("## Queries")
    lines.append("<!-- Saved search patterns -->")
    lines.append("")
    
    return '\n'.join(lines)

def write_lint_log(broken_links, orphans_no_inbound, missing_from_index):
    """Write lint results to meta/lint.log and log.md."""
    os.makedirs(META_DIR, exist_ok=True)
    log_path = os.path.join(META_DIR, 'lint.log')
    timestamp = datetime.datetime.now().isoformat()
    
    with open(log_path, 'a') as f:
        f.write(f"\n## Lint {timestamp}\n")
        f.write(f"- Broken links: {len(broken_links)}\n")
        f.write(f"- Orphan pages (no inbound links): {len(orphans_no_inbound)}\n")
        f.write(f"- Pages missing from index.md: {len(missing_from_index)}\n")
        if broken_links:
            f.write("  Broken links:\n")
            for link, source in broken_links:
                f.write(f"    - {source} -> [[{link}]]\n")
        if orphans_no_inbound:
            f.write("  Orphan pages (no inbound links):\n")
            for page in sorted(orphans_no_inbound):
                f.write(f"    - [[{page}]]\n")
        if missing_from_index:
            f.write("  Pages missing from index.md:\n")
            for path in missing_from_index:
                f.write(f"    - {os.path.relpath(path, WIKI_ROOT)}\n")
    
    with open(LOG_MD, 'a') as f:
        f.write(f"\n## [{datetime.date.today().isoformat()}] lint | {len(broken_links)} broken links, {len(orphans_no_inbound)} orphans, {len(missing_from_index)} missing from index\n")

def main():
    parser = argparse.ArgumentParser(description="Update wiki index and/or run lint")
    parser.add_argument("--lint-only", action="store_true", help="Only run lint, don't update index")
    parser.add_argument("--index-only", action="store_true", help="Only update index, skip lint")
    args = parser.parse_args()
    
    print("Wiki Index & Lint")
    print("=" * 60)
    
    # Lint analysis
    all_links, all_pages = get_all_wikilinks()
    broken = find_broken_links(all_links, all_pages)
    orphans_no_inbound = find_orphan_pages_no_inbound(all_links, all_pages)
    missing_from_index = find_pages_missing_from_index()
    
    if not args.index_only:
        print("\n📊 Lint Statistics:")
        print(f"  Total pages: {len(all_pages)}")
        print(f"  Total links: {len(all_links)}")
        print(f"  Broken links: {len(broken)}")
        print(f"  Orphan pages (no inbound links): {len(orphans_no_inbound)}")
        print(f"  Pages missing from index.md: {len(missing_from_index)}")
        
        if broken:
            print(f"\n⚠️  Broken links (top 10):")
            for link, source in broken[:10]:
                print(f"  [[{link}]] in {source}")
        
        if orphans_no_inbound:
            print(f"\n📝 Orphan pages (no inbound links):")
            for page in sorted(orphans_no_inbound)[:10]:
                print(f"  [[{page}]]")
        
        if missing_from_index:
            print(f"\n📄 Pages missing from index.md (top 10):")
            for path in missing_from_index[:10]:
                print(f"  {os.path.relpath(path, WIKI_ROOT)}")
        
        write_lint_log(broken, orphans_no_inbound, missing_from_index)
        print(f"\n✓ Lint logged to meta/lint.log and log.md")
    
    # Index update
    if not args.lint_only:
        index_content = generate_index()
        with open(INDEX_PATH, 'w') as f:
            f.write(index_content)
        print(f"\n✓ Updated index.md")
    
    # Save link report (optional)
    report_path = os.path.join(WIKI_ROOT, 'meta', 'link_report.txt')
    with open(report_path, 'w') as f:
        f.write(f"Link Report - {datetime.datetime.now().isoformat()}\n")
        f.write(f"Broken links: {len(broken)}\n")
        for link, source in broken:
            f.write(f"  [[{link}]] from {source}\n")
        f.write(f"\nOrphan pages (no inbound): {len(orphans_no_inbound)}\n")
        for page in sorted(orphans_no_inbound):
            f.write(f"  [[{page}]]\n")
        f.write(f"\nMissing from index: {len(missing_from_index)}\n")
        for path in missing_from_index:
            f.write(f"  {os.path.relpath(path, WIKI_ROOT)}\n")
    
    print(f"✓ Link report saved: {report_path}")
    print("\nDone.")

if __name__ == '__main__':
    main()