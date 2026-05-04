#!/usr/bin/env python3
"""
Neutralize promotional language in wiki pages.
Only replaces clearly promotional phrases, not legitimate uses.
Outputs a report of changes made.
"""

import glob, re, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Patterns that are almost always promotional in software/tool descriptions
PROMO_PATTERNS = [
    (r'\bstate-of-the-art\b', 'current', 'state-of-the-art'),
    (r'\bstate of the art\b', 'current', 'state of the art'),
    (r'\bcutting-edge\b', 'advanced', 'cutting-edge'),
    (r'\bcutting edge\b', 'advanced', 'cutting edge'),
    (r'\brevolutionary\b', 'novel', 'revolutionary'),
    (r'\bgroundbreaking\b', 'novel', 'groundbreaking'),
    (r'\bpioneering\b', 'foundational', 'pioneering'),
    (r'\bworld-class\b', '', 'world-class'),
    (r'\bunparalleled\b', '', 'unparalleled'),
    (r'\bunmatched\b', '', 'unmatched'),
    (r'\bunrivaled\b', '', 'unrivaled'),
    (r'\bexceptional\b', '', 'exceptional'),
    (r'\boutstanding\b', '', 'outstanding'),
    (r'\bextraordinary\b', '', 'extraordinary'),
    (r'\bremarkable\b', '', 'remarkable'),
]

# More careful patterns — only replace in clear promotional contexts
CONTEXTUAL_PATTERNS = [
    # "leading" only when followed by nouns suggesting dominance
    (r'\bleading (?:provider|developer|platform|tool|solution|framework|library|package|software|company|group|team|researcher|expert|authority)\b', 'widely used', 'leading'),
    # "superior" only when making comparative claims about tools
    (r'\bsuperior (?:performance|accuracy|results|quality|capability|features?|speed|efficiency|to)\b', 'better', 'superior'),
    # "best practices" → standard practices
    (r'\bbest practices?\b', 'standard practices', 'best practices'),
    # "expert" only in "expert team/users" context, not "expert system"
    (r'\bexpert (?:team|developers?|users?|community|support|assistance|guidance)\b', 'specialist', 'expert'),
]

def apply_replacements(filepath, patterns):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    for pattern, replacement, original_word in patterns:
        def replacer(m):
            match_text = m.group(0)
            # Preserve case
            if match_text.isupper():
                new_text = replacement.upper()
            elif match_text[0].isupper():
                new_text = replacement.capitalize()
            else:
                new_text = replacement
            
            # If replacement is empty, we need to handle gracefully
            if not new_text:
                # Just remove the word, but check if it leaves awkward grammar
                # For now, just return empty and we'll clean up later
                return ''
            
            return new_text
        
        new_content, count = re.subn(pattern, replacer, content, flags=re.IGNORECASE)
        if count > 0:
            changes.append(f"  {original_word}: {count} instance(s)")
            content = new_content
    
    if content != original:
        # Clean up any double spaces left by empty replacements
        content = re.sub(r'  +', ' ', content)
        content = re.sub(r' \n', '\n', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return None

def main():
    all_changes = []
    modified = 0
    
    for d in ['entities', 'concepts', 'comparisons']:
        for f in glob.glob(os.path.join(REPO, d, '*.md')):
            relpath = os.path.relpath(f, REPO)
            
            promo_changes = apply_replacements(f, PROMO_PATTERNS)
            ctx_changes = apply_replacements(f, CONTEXTUAL_PATTERNS)
            
            if promo_changes or ctx_changes:
                modified += 1
                all_changes.append({
                    'file': relpath,
                    'changes': (promo_changes or []) + (ctx_changes or [])
                })
                print(f"{relpath}:")
                for c in (promo_changes or []) + (ctx_changes or []):
                    print(c)
    
    print(f"\n=== Results ===")
    print(f"Modified {modified} files")
    
    # Write report
    import json
    report_path = os.path.join(REPO, 'meta', 'promo_language_fixes.json')
    with open(report_path, 'w') as f:
        json.dump({'modified': modified, 'files': all_changes}, f, indent=2)
    print(f"Report: {report_path}")

if __name__ == '__main__':
    main()
