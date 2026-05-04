#!/usr/bin/env python3
"""
Strip hardcoded ## References sections from page bodies.
YAML sources: frontmatter will render via obsidian_support.py hook.
Handles both trailing refs and refs followed by other sections.
"""

import os, re, frontmatter, glob, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def strip_refs_from_file(filepath):
    """Remove ## References section from body. Returns True if modified."""
    try:
        post = frontmatter.load(filepath)
    except Exception as e:
        print(f"  SKIP (parse error): {filepath}: {e}")
        return False
    
    body = post.content
    if '## References' not in body:
        return False
    
    # Find the ## References heading
    idx = body.index('## References')
    
    # Check if there's a following ## heading
    after = body[idx:]
    match = re.search(r'\n## [^#]', after[1:])  # skip the ## References itself
    
    if match:
        # There's another heading after references — strip only up to that heading
        end_idx = idx + 1 + match.start()
        new_body = body[:idx].rstrip()
    else:
        # References at end — strip to end
        new_body = body[:idx].rstrip()
    
    if new_body == body.rstrip():
        return False
    
    post.content = new_body
    
    # Write back preserving frontmatter format
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    
    return True

def main():
    dirs = ['entities', 'concepts', 'comparisons']
    modified = 0
    skipped = 0
    
    for d in dirs:
        for f in glob.glob(os.path.join(REPO, d, '*.md')):
            if strip_refs_from_file(f):
                modified += 1
                print(f"  STRIPPED: {os.path.relpath(f, REPO)}")
    
    print(f"\n=== Results ===")
    print(f"Modified: {modified} pages")
    print(f"Skipped (no ## References or parse error): remaining")

if __name__ == '__main__':
    main()
