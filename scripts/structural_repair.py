#!/usr/bin/env python3
"""
Structural Repair Script — Fix pages with leaked frontmatter or broken YAML.

Usage:
    python3 scripts/structural_repair.py [--dry-run]
"""
import os
import sys
import re
import glob
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import read_page, save_page, git_commit

def repair_leaked_frontmatter(filepath: str) -> bool:
    """
    Fix pages where frontmatter.load parsed the first FM block,
    but a second FM block is embedded in the content.
    
    Strategy: Use the FIRST frontmatter (daemon-generated, links to stubs),
    but strip the leaked second frontmatter from the body.
    Keep any real body content after the leaked FM.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    
    if not raw.startswith('---'):
        return False
    
    # Find the first frontmatter end
    lines = raw.split('\n')
    first_fm_end = -1
    for i in range(1, len(lines)):
        if lines[i].strip().rstrip('-') == '' and lines[i].strip().startswith('---'):
            first_fm_end = i
            break
    
    if first_fm_end == -1:
        return False
    
    # Now find if there's a SECOND frontmatter block starting shortly after
    second_fm_start = -1
    for i in range(first_fm_end + 1, min(first_fm_end + 20, len(lines))):
        if lines[i].strip().startswith('title:'):
            second_fm_start = i
            break
    
    if second_fm_start == -1:
        return False
    
    # Find the end of the second frontmatter block
    second_fm_end = -1
    for i in range(second_fm_start, len(lines)):
        if lines[i].strip().rstrip('-') == '' and lines[i].strip().startswith('---'):
            second_fm_end = i
            break
    
    if second_fm_end == -1:
        return False
    
    # Reconstruct: first_fm_lines + body_lines
    first_fm = '\n'.join(lines[:first_fm_end]) + '\n---\n\n'
    body = '\n'.join(lines[second_fm_end + 1:])
    
    # Also strip any hardcoded References section
    body = re.sub(r'\n## References\n.*?(?=\n## |\Z)', '\n', body, flags=re.DOTALL)
    
    new_text = first_fm + body.strip()
    
    if new_text != raw:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_text + ('\n' if not new_text.endswith('\n') else ''))
        return True
    return False


def repair_broken_yaml(filepath: str) -> bool:
    """
    Fix pages with YAML parse errors by manually rewriting frontmatter.
    Common issues: unquoted colons in titles/sources, missing closing ---.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    
    if not raw.startswith('---'):
        return False
    
    # Extract frontmatter text
    parts = raw.split('---', 2)
    if len(parts) < 3:
        # Missing closing --- — find where body starts
        lines = raw.split('\n')
        # Find first blank line followed by non-metadata line
        fm_end = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == '' or lines[i].strip().startswith('#'):
                fm_end = i - 1
                break
            if lines[i].strip() == '' and i + 1 < len(lines) and not lines[i+1].strip().startswith(tuple('abcdefghijklmnopqrstuvwxyz')):
                fm_end = i
                break
        
        # Just try to fix by splitting on first blank line after metadata
        if '\n\n#' in raw:
            fm_text, body = raw.split('\n\n#', 1)
            body = '#' + body
        else:
            return False
    else:
        fm_text = parts[1]
        body = parts[2]
    
    # Try parsing it
    try:
        fm = yaml.safe_load(fm_text)
        if fm:
            # Already parses fine? Maybe not broken
            # But could still be missing closing ---
            if len(parts) < 3:
                new_text = '---\n' + fm_text + '\n---\n\n' + body.strip()
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_text)
                return True
            return False
    except yaml.YAMLError:
        pass
    
    # Fix common YAML issues line by line
    fixed_lines = []
    for line in fm_text.split('\n'):
        # Quote titles with colons
        m = re.match(r'^(title:\s+)(.+:.+)$', line)
        if m:
            fixed_lines.append(m.group(1) + '"' + m.group(2).strip('"') + '"')
            continue
        # Quote source titles with colons
        m = re.match(r'^(\s+title:\s+)(.+:.+)$', line)
        if m:
            fixed_lines.append(m.group(1) + '"' + m.group(2).strip('"') + '"')
            continue
        # Quote DOI values
        m = re.match(r'^(\s+doi:\s+)(\S+)$', line)
        if m:
            fixed_lines.append(m.group(1) + '"' + m.group(2).strip('"') + '"')
            continue
        # Quote venue with colons
        m = re.match(r'^(\s+venue:\s+)(.+:.+)$', line)
        if m:
            fixed_lines.append(m.group(1) + '"' + m.group(2).strip('"') + '"')
            continue
        # Quote hanging id values
        m = re.match(r'^(\s+id:\s+)(\S+)$', line)
        if m and not m.group(2).isdigit():
            fixed_lines.append(m.group(1) + '"' + m.group(2) + '"')
            continue
        # Fix authors with colons in brackets
        m = re.match(r'^(\s+authors:\s+)(.+)$', line)
        if m and ':' in m.group(2) and not m.group(2).startswith('['):
            fixed_lines.append(m.group(1) + '"' + m.group(2).strip('"') + '"')
            continue
        fixed_lines.append(line)
    
    fixed_fm_text = '\n'.join(fixed_lines)
    
    try:
        fm = yaml.safe_load(fixed_fm_text)
        if fm is not None:
            new_text = '---\n' + fixed_fm_text + '\n---\n\n' + body.strip()
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_text)
            return True
    except yaml.YAMLError:
        pass
    
    return False


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    
    leaked_fixed = 0
    yaml_fixed = 0
    
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ralph_config import read_page
    
    for d in ['entities', 'concepts', 'comparisons']:
        for f in glob.glob(f'{d}/*.md'):
            try:
                meta, content = read_page(f)
                content_start = content.strip()[:20].lower()
                if content_start.startswith('title:') or content_start.startswith('---'):
                    if not args.dry_run:
                        if repair_leaked_frontmatter(f):
                            leaked_fixed += 1
                    else:
                        print(f'WOULD FIX LEAKED: {f}')
                        leaked_fixed += 1
            except Exception as e:
                if not args.dry_run:
                    if repair_broken_yaml(f):
                        yaml_fixed += 1
                else:
                    print(f'WOULD FIX YAML: {f} ({str(e)[:40]})')
                    yaml_fixed += 1
    
    print(f'Results:')
    print(f'  Leaked frontmatter fixed: {leaked_fixed}')
    print(f'  Broken YAML fixed: {yaml_fixed}')
    
    if not args.dry_run and (leaked_fixed > 0 or yaml_fixed > 0):
        git_commit(f"Structural repair: fix {leaked_fixed} leaked frontmatter + {yaml_fixed} broken YAML pages")


if __name__ == '__main__':
    main()
