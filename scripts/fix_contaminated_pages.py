#!/usr/bin/env python3
"""
Fix pages contaminated with meta-commentary and wrapped in markdown code blocks.
Extracts actual content from ```markdown ... ``` wrappers.
Also fixes leaked frontmatter.
"""

import frontmatter, re, os, glob

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def extract_from_codeblock(body):
    """Extract content from ```markdown wrapper if present."""
    # Pattern: optional preamble, then ```markdown, then content, then ```
    match = re.search(r'```markdown\s*\n(.*?)\n```', body, re.DOTALL)
    if match:
        inner = match.group(1).strip()
        return inner
    
    # Also handle ```yaml cases (frontmatter inside code block)
    match = re.search(r'```yaml\s*\n(.*?)\n```', body, re.DOTALL)
    if match:
        inner = match.group(1).strip()
        return inner
    
    return None

def fix_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    
    # Parse outer frontmatter
    try:
        post = frontmatter.load(filepath)
    except Exception as e:
        print(f"  PARSE ERROR: {filepath}: {e}")
        return False
    
    body = post.content
    
    # Check for meta-commentary markers
    meta_markers = [
        'here is the corrected',
        'here is the revised',
        'i\'ll fix',
        'i will fix',
        'all issues fixed',
        'now i have all the information',
        'here is the updated',
    ]
    has_meta = any(marker in body.lower()[:500] for marker in meta_markers)
    
    # Check for code block wrapper
    has_codeblock = '```markdown' in body or '```yaml' in body
    
    if not has_meta and not has_codeblock:
        # Just leaked frontmatter without codeblock wrapper
        if body.strip().startswith('title:') or body.strip().startswith('created:') or body.strip().startswith('---'):
            # Strip leaked frontmatter lines from start
            lines = body.split('\n')
            start_idx = 0
            for i, line in enumerate(lines):
                if line.strip() == '---' and i > 0:
                    start_idx = i + 1
                    break
                # If we hit a markdown heading, that's real content
                if line.strip().startswith('# ') or line.strip().startswith('## '):
                    start_idx = i
                    break
            new_body = '\n'.join(lines[start_idx:]).strip()
            if new_body != body.strip():
                post.content = new_body
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(post))
                print(f"  FIXED (leaked frontmatter): {filepath}")
                return True
        return False
    
    if has_codeblock:
        inner = extract_from_codeblock(body)
        if inner:
            # Parse the inner content
            try:
                inner_post = frontmatter.loads(inner)
                # Merge: inner frontmatter overrides outer if both exist
                merged_metadata = dict(post.metadata)
                merged_metadata.update(inner_post.metadata)
                
                new_post = frontmatter.Post(inner_post.content, **merged_metadata)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(new_post))
                print(f"  FIXED (codeblock wrapper): {filepath}")
                return True
            except Exception as e:
                print(f"  ERROR parsing inner content: {filepath}: {e}")
                return False
    
    # Has meta but no codeblock — just strip the meta preamble
    if has_meta:
        lines = body.split('\n')
        content_start = 0
        for i, line in enumerate(lines):
            # Look for first real markdown content
            if line.strip().startswith('# ') or line.strip().startswith('## ') or line.strip().startswith('* ') or line.strip().startswith('- '):
                # Skip "Here is..." lines that might have markdown
                if any(marker in line.lower() for marker in meta_markers):
                    continue
                content_start = i
                break
        
        new_body = '\n'.join(lines[content_start:]).strip()
        if new_body and new_body != body.strip():
            post.content = new_body
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            print(f"  FIXED (meta preamble): {filepath}")
            return True
    
    return False

def main():
    # Fix the 8 known leaked pages
    leaked_pages = [
        'entities/bionet.md',
        'entities/brainvoyager.md',
        'entities/camino.md',
        'entities/carlsim.md',
        'entities/fastsurfer.md',
        'entities/niftyreg.md',
        'entities/psyneulink.md',
        'entities/steps.md',
    ]
    
    fixed = 0
    for f in leaked_pages:
        filepath = os.path.join(REPO, f)
        if os.path.exists(filepath):
            if fix_page(filepath):
                fixed += 1
    
    # Also scan ALL pages for codeblock/meta contamination
    print("\n=== Scanning all pages for contamination ===")
    for d in ['entities', 'concepts', 'comparisons']:
        for f in glob.glob(os.path.join(REPO, d, '*.md')):
            with open(f, 'r', encoding='utf-8') as fh:
                content = fh.read()
            # Quick check for codeblock wrapper or strong meta markers
            if '```markdown' in content or '```yaml' in content:
                relpath = os.path.relpath(f, REPO)
                if relpath not in leaked_pages:
                    print(f"  FOUND codeblock: {relpath}")
                    if fix_page(f):
                        fixed += 1
    
    print(f"\n=== Total fixed: {fixed} pages ===")

if __name__ == '__main__':
    main()
