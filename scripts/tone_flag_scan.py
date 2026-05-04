#!/usr/bin/env python3
"""
Regex tone flag: scan all pages for conversational/promotional/non-wiki language.
Outputs JSON report to meta/tone_flag_report.json
"""

import os, re, json, glob, frontmatter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Patterns that suggest non-encyclopedic tone
TONE_PATTERNS = [
    (r'\bI think\b', 'first_person_opinion'),
    (r'\bI believe\b', 'first_person_opinion'),
    (r'\bI suggest\b', 'first_person_instruction'),
    (r'\bI recommend\b', 'first_person_instruction'),
    (r'\bI will\b', 'first_person_future'),
    (r'\bI have\b', 'first_person_experience'),
    (r'\bYou should\b', 'second_person_instruction'),
    (r'\bYou can\b', 'second_person_instruction'),
    (r'\bYou may\b', 'second_person_instruction'),
    (r'\bLet me\b', 'first_person_instruction'),
    (r'\bLet us\b', 'first_person_instruction'),
    (r'\bAs you can see\b', 'reader_directive'),
    (r'\bAs you know\b', 'reader_assumption'),
    (r'\bIt is important to note\b', 'meta_commentary'),
    (r'\bIt is worth noting\b', 'meta_commentary'),
    (r'\bIt should be noted\b', 'meta_commentary'),
    (r'\bPlease note\b', 'reader_directive'),
    (r'\bDon\'t forget\b', 'reader_directive'),
    (r'\bKeep in mind\b', 'reader_directive'),
    (r'\bRemember that\b', 'reader_directive'),
    (r'\bWe can see\b', 'first_person_observation'),
    (r'\bWe recommend\b', 'first_person_instruction'),
    (r'\bIn conclusion\b', 'essay_structure'),
    (r'\bTo sum up\b', 'essay_structure'),
    (r'\bOverall\b', 'essay_structure'),
    (r'\bIn summary\b', 'essay_structure'),
    (r'\bFirstly\b', 'essay_structure'),
    (r'\bSecondly\b', 'essay_structure'),
    (r'\bThirdly\b', 'essay_structure'),
    (r'\bMoreover\b', 'essay_transition'),
    (r'\bFurthermore\b', 'essay_transition'),
    (r'\bNevertheless\b', 'essay_transition'),
    (r'\bHowever\b', 'essay_transition'),
    (r'\bTherefore\b', 'essay_transition'),
    (r'\bThus\b', 'essay_transition'),
    (r'\bConsequently\b', 'essay_transition'),
    (r'\bOn the other hand\b', 'essay_transition'),
    (r'\bIn other words\b', 'meta_commentary'),
    (r'\bIn this paper\b', 'academic_paper_reference'),
    (r'\bIn this study\b', 'academic_paper_reference'),
    (r'\bThe authors\b', 'academic_paper_reference'),
    (r'\bBest practices?\b', 'promotional_language'),
    (r'\bHighly recommended\b', 'promotional_language'),
    (r'\bstate-of-the-art\b', 'promotional_language'),
    (r'\bcutting-edge\b', 'promotional_language'),
    (r'\bgroundbreaking\b', 'promotional_language'),
    (r'\brevolutionary\b', 'promotional_language'),
    (r'\bleading\b', 'promotional_language'),
    (r'\bpioneering\b', 'promotional_language'),
    (r'\bworld-class\b', 'promotional_language'),
    (r'\bexpert\b', 'promotional_language'),
    (r'\bunparalleled\b', 'promotional_language'),
    (r'\bunmatched\b', 'promotional_language'),
    (r'\bsuperior\b', 'promotional_language'),
]

def flag_page(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip frontmatter for tone analysis
        if content.startswith('---'):
            end_fm = content.find('---', 3)
            if end_fm != -1:
                body = content[end_fm+3:]
            else:
                body = content
        else:
            body = content
        
        body_lower = body.lower()
        hits = []
        for pattern, category in TONE_PATTERNS:
            matches = re.findall(pattern, body_lower, re.IGNORECASE)
            for m in matches:
                hits.append({'match': m, 'category': category})
        
        return hits
    except Exception as e:
        return [{'match': f'ERROR: {e}', 'category': 'parse_error'}]

def main():
    results = []
    
    for d in ['entities', 'concepts', 'comparisons']:
        for f in glob.glob(os.path.join(REPO, d, '*.md')):
            hits = flag_page(f)
            if hits:
                relpath = os.path.relpath(f, REPO)
                # Count by category
                categories = {}
                for h in hits:
                    cat = h['category']
                    categories[cat] = categories.get(cat, 0) + 1
                
                results.append({
                    'file': relpath,
                    'total_hits': len(hits),
                    'categories': categories,
                    'samples': list(set(h['match'] for h in hits))[:5],
                })
    
    # Sort by total hits descending
    results.sort(key=lambda x: -x['total_hits'])
    
    report = {
        'scanned_at': __import__('datetime').datetime.now().isoformat(),
        'total_pages_scanned': sum(1 for d in ['entities', 'concepts', 'comparisons'] for _ in glob.glob(os.path.join(REPO, d, '*.md'))),
        'flagged_pages': len(results),
        'pages': results,
    }
    
    report_path = os.path.join(REPO, 'meta', 'tone_flag_report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"=== Tone Flag Report ===")
    print(f"Total pages scanned: {report['total_pages_scanned']}")
    print(f"Flagged pages: {report['flagged_pages']}")
    print()
    print("Top 20 most flagged pages:")
    for r in results[:20]:
        print(f"  {r['file']}: {r['total_hits']} hits — {r['samples'][:3]}")
    
    print(f"\nFull report: {report_path}")

if __name__ == '__main__':
    main()
