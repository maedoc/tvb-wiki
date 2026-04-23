#!/usr/bin/env python3
"""
Daily lint script for TVB Wiki.
- Checks for broken wikilinks
- Finds orphan pages (no inbound links)
- Identifies pages missing from index.md
- Logs results to meta/lint.log and log.md
"""
import os
import re
import datetime
import sys

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_DIR = os.path.join(WIKI_ROOT, "entities")
CONCEPTS_DIR = os.path.join(WIKI_ROOT, "concepts")
COMPARISONS_DIR = os.path.join(WIKI_ROOT, "comparisons")
DOCS_DIR = os.path.join(WIKI_ROOT, "docs")
INDEX_PATH = os.path.join(WIKI_ROOT, "catalog.md")
META_DIR = os.path.join(WIKI_ROOT, "meta")
LOG_MD = os.path.join(WIKI_ROOT, "log.md")


def get_all_pages():
    """Get all wiki pages from entities, concepts, comparisons, and docs directories."""
    all_pages = set()
    
    for directory in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR, DOCS_DIR]:
        if not os.path.exists(directory):
            continue
        for filename in os.listdir(directory):
            if filename.endswith('.md'):
                page_name = filename[:-3]
                all_pages.add(page_name)
    
    return all_pages


def extract_wikilinks_from_file(filepath):
    """Extract all wikilinks from a file."""
    links = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Find all [[link]] or [[link|alias]] patterns
        matches = re.findall(r'\[\[([^\]]+)\]\]', content)
        for match in matches:
            # Remove alias if present
            if '|' in match:
                match = match.split('|')[0]
            # Normalize: lowercase and replace spaces/hyphens
            normalized = match.lower().replace(' ', '-').replace('‑', '-')
            links.append((normalized, match))
    except Exception as e:
        print(f"  Warning: Could not read {filepath}: {e}")
    
    return links


def get_all_wikilinks(all_pages):
    """Extract all wikilinks from all pages with their sources."""
    all_links = []  # List of (normalized_link, display_text, source_page)
    
    for directory in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR, DOCS_DIR]:
        if not os.path.exists(directory):
            continue
        for filename in os.listdir(directory):
            if filename.endswith('.md'):
                source_page = filename[:-3]
                filepath = os.path.join(directory, filename)
                links = extract_wikilinks_from_file(filepath)
                for normalized, original in links:
                    all_links.append((normalized, original, source_page))
    
    return all_links


def find_broken_links(all_links, all_pages):
    """Find links that point to non-existent pages."""
    broken = []
    for normalized, original, source in all_links:
        if normalized not in all_pages:
            broken.append((normalized, original, source))
    return broken


def find_orphan_pages(all_links, all_pages):
    """Find pages with no inbound links."""
    linked_pages = set(link for link, _, _ in all_links)
    orphans = all_pages - linked_pages
    return orphans


def find_pages_missing_from_index():
    """Find pages not listed in index.md."""
    if not os.path.exists(INDEX_PATH):
        return []
    
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Extract all wikilinks from index
    index_links = re.findall(r'\[\[([^\]]+)\]\]', index_content)
    index_page_names = set()
    for link in index_links:
        if '|' in link:
            link = link.split('|')[0]
        normalized = link.lower().replace(' ', '-').replace('‑', '-')
        index_page_names.add(normalized)
    
    # Find pages not in index
    missing = []
    for directory, dir_name in [(ENTITIES_DIR, 'entities'), 
                                 (CONCEPTS_DIR, 'concepts'),
                                 (COMPARISONS_DIR, 'comparisons')]:
        if not os.path.exists(directory):
            continue
        for filename in os.listdir(directory):
            if filename.endswith('.md'):
                page_name = filename[:-3]
                if page_name not in index_page_names:
                    missing.append((dir_name, page_name, os.path.join(directory, filename)))
    
    return missing


def write_lint_report(broken_links, orphan_pages, missing_from_index):
    """Write lint results to meta/lint.log and log.md."""
    os.makedirs(META_DIR, exist_ok=True)
    log_path = os.path.join(META_DIR, 'lint.log')
    timestamp = datetime.datetime.now().isoformat()
    date_str = datetime.date.today().isoformat()
    
    # Write to lint.log
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"\n## Lint {timestamp}\n")
        f.write(f"- Orphan pages: {len(orphan_pages)}\n")
        f.write(f"- Broken links: {len(broken_links)}\n")
        
        if broken_links:
            f.write("  Broken links:\n")
            # Group by source for cleaner output
            by_source = {}
            for normalized, original, source in broken_links:
                if source not in by_source:
                    by_source[source] = []
                by_source[source].append(original)
            
            for source in sorted(by_source.keys()):
                for link in sorted(by_source[source]):
                    f.write(f"    - {source} -> [[{link}]]\n")
    
    # Write to log.md
    with open(LOG_MD, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{date_str}] daily-lint | {len(broken_links)} broken, {len(orphan_pages)} orphans, {len(missing_from_index)} missing from index\n")
    
    return log_path


def print_report(broken_links, orphan_pages, missing_from_index):
    """Print lint report to console."""
    print("\n" + "=" * 60)
    print("DAILY LINT REPORT")
    print("=" * 60)
    print(f"Timestamp: {datetime.datetime.now().isoformat()}")
    print()
    
    # Summary
    print(f"📊 Summary:")
    print(f"  - Broken links: {len(broken_links)}")
    print(f"  - Orphan pages (no inbound links): {len(orphan_pages)}")
    print(f"  - Pages missing from index: {len(missing_from_index)}")
    print()
    
    # Broken links
    if broken_links:
        print(f"⚠️  Broken Links ({len(broken_links)}):")
        # Group by source
        by_source = {}
        for normalized, original, source in broken_links:
            if source not in by_source:
                by_source[source] = set()
            by_source[source].add(original)
        
        for source in sorted(by_source.keys())[:10]:  # Limit output
            print(f"  In [[{source}]]:")
            for link in sorted(by_source[source])[:5]:  # Limit per source
                print(f"    - [[{link}]]")
            if len(by_source[source]) > 5:
                print(f"    ... and {len(by_source[source]) - 5} more")
        if len(by_source) > 10:
            print(f"  ... and {len(by_source) - 10} more files with broken links")
        print()
    
    # Orphan pages
    if orphan_pages:
        print(f"📝 Orphan Pages (no inbound links) - {len(orphan_pages)}:")
        for page in sorted(orphan_pages)[:15]:
            print(f"  - [[{page}]]")
        if len(orphan_pages) > 15:
            print(f"  ... and {len(orphan_pages) - 15} more")
        print()
    
    # Missing from index
    if missing_from_index:
        print(f"📄 Pages Missing from Index - {len(missing_from_index)}:")
        for dir_name, page_name, _ in missing_from_index[:15]:
            print(f"  - [{dir_name}] [[{page_name}]]")
        if len(missing_from_index) > 15:
            print(f"  ... and {len(missing_from_index) - 15} more")
        print()
    
    if not broken_links and not orphan_pages and not missing_from_index:
        print("✅ All checks passed! No issues found.")
        print()


def main():
    print("🔍 TVB Wiki Daily Lint")
    print("=" * 60)
    
    # Ensure directories exist
    os.makedirs(META_DIR, exist_ok=True)
    
    # Gather data
    print("\n📂 Scanning wiki pages...")
    all_pages = get_all_pages()
    print(f"  Found {len(all_pages)} pages")
    
    print("\n🔗 Extracting wikilinks...")
    all_links = get_all_wikilinks(all_pages)
    print(f"  Found {len(all_links)} wikilinks")
    
    # Run checks
    print("\n🧪 Running lint checks...")
    broken_links = find_broken_links(all_links, all_pages)
    orphan_pages = find_orphan_pages(all_links, all_pages)
    missing_from_index = find_pages_missing_from_index()
    
    # Write reports
    print("\n📝 Writing reports...")
    log_path = write_lint_report(broken_links, orphan_pages, missing_from_index)
    
    # Print report
    print_report(broken_links, orphan_pages, missing_from_index)
    
    print(f"✅ Lint complete. Report saved to:")
    print(f"   - {log_path}")
    print(f"   - {LOG_MD}")
    
    # Return exit code based on issues found
    total_issues = len(broken_links) + len(orphan_pages) + len(missing_from_index)
    if total_issues > 0:
        print(f"\n⚠️  {total_issues} issue(s) found.")
        return 1
    else:
        print("\n✨ No issues found!")
        return 0


if __name__ == '__main__':
    sys.exit(main())
