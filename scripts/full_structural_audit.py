#!/usr/bin/env python3
"""
Full structural audit of the TVB Wiki.
Checks for all major structural issues across entities, concepts, comparisons.
Outputs a JSON report to meta/structural_audit.json
"""

import os, json, glob, frontmatter
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META_DIR = os.path.join(REPO, "meta")
os.makedirs(META_DIR, exist_ok=True)

META_PHRASES = [
    'here is the revised',
    'i should note',
    'i have added',
    'as requested',
    'per your request',
    'i have updated',
    'below is the',
    'the following changes',
    'i have incorporated',
    'i have included',
    'revision complete',
    'updated version',
    'let me know',
    'feel free to',
    'i hope this',
]

def audit():
    pages = []
    for d in ['entities', 'concepts', 'comparisons']:
        pages.extend(glob.glob(os.path.join(REPO, d, '*.md')))
    
    results = {
        'scanned_at': __import__('datetime').datetime.now().isoformat(),
        'total_pages': len(pages),
        'issues': {
            'both_sources_and_refs_section': [],
            'empty_body': [],
            'thin_content': [],
            'leaked_frontmatter': [],
            'meta_commentary': [],
            'duplicate_sources': [],
            'parse_errors': [],
            'missing_required_fields': [],
            'hardcoded_refs_section': [],
        }
    }
    
    for f in sorted(pages):
        relpath = os.path.relpath(f, REPO)
        try:
            post = frontmatter.load(f)
            body = post.content
            sources = post.metadata.get('sources', [])
            word_count = len(body.split())
            
            # 1. Both YAML sources AND ## References section
            has_refs_section = '## References' in body
            if sources and has_refs_section:
                results['issues']['both_sources_and_refs_section'].append({
                    'file': relpath,
                    'source_count': len(sources),
                    'word_count': word_count,
                })
            
            # 2. Empty body
            if word_count < 20:
                results['issues']['empty_body'].append({
                    'file': relpath,
                    'word_count': word_count,
                })
            
            # 3. Thin content
            elif word_count < 100:
                results['issues']['thin_content'].append({
                    'file': relpath,
                    'word_count': word_count,
                })
            
            # 4. Leaked frontmatter
            body_start = body.strip()[:300].lower()
            if 'title:' in body_start or body.strip().startswith('title:') or '---\ntitle:' in body[:500]:
                results['issues']['leaked_frontmatter'].append({
                    'file': relpath,
                    'snippet': body.strip()[:200],
                })
            
            # 5. Meta commentary
            body_lower = body.lower()
            found_phrases = [p for p in META_PHRASES if p in body_lower]
            if found_phrases:
                results['issues']['meta_commentary'].append({
                    'file': relpath,
                    'phrases': found_phrases,
                })
            
            # 6. Duplicate sources in frontmatter
            dois = []
            titles = []
            for s in sources:
                if isinstance(s, dict):
                    if 'doi' in s:
                        dois.append(s['doi'])
                    if 'title' in s:
                        titles.append(s['title'])
                elif isinstance(s, str):
                    titles.append(s)
            dup_dois = [d for d, c in Counter(dois).items() if c > 1]
            dup_titles = [t for t, c in Counter(titles).items() if c > 1]
            if dup_dois or dup_titles:
                results['issues']['duplicate_sources'].append({
                    'file': relpath,
                    'dup_dois': dup_dois,
                    'dup_titles': dup_titles[:3],
                })
            
            # 7. Missing required fields
            required = ['title']
            missing = [field for field in required if field not in post.metadata]
            if missing:
                results['issues']['missing_required_fields'].append({
                    'file': relpath,
                    'missing': missing,
                })
            
            # 8. Hardcoded refs section (even without sources)
            if has_refs_section and not sources:
                results['issues']['hardcoded_refs_section'].append({
                    'file': relpath,
                    'word_count': word_count,
                })
                
        except Exception as e:
            results['issues']['parse_errors'].append({
                'file': relpath,
                'error': str(e),
            })
    
    # Summary
    summary = {}
    for issue_type, items in results['issues'].items():
        summary[issue_type] = len(items)
    results['summary'] = summary
    
    # Write report
    report_path = os.path.join(META_DIR, 'structural_audit.json')
    with open(report_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"=== Structural Audit Report ===")
    print(f"Total pages scanned: {results['total_pages']}")
    print()
    for issue_type, count in summary.items():
        if count > 0:
            print(f"  {issue_type}: {count} pages")
    print()
    print(f"Full report: {report_path}")
    
    return results

if __name__ == '__main__':
    audit()
