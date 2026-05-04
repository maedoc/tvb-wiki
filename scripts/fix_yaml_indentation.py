#!/usr/bin/env python3
"""
Fix YAML parse errors in frontmatter by properly indenting dict list items.
"""

import yaml, sys

def fix_yaml_indentation(filepath):
    with open(filepath, 'r') as fh:
        raw = fh.read()
    
    if not raw.startswith('---'):
        print(f"SKIP: {filepath} (no frontmatter)")
        return
    
    end = raw.find('---', 3)
    if end == -1:
        print(f"SKIP: {filepath} (unclosed frontmatter)")
        return
    
    fm_text = raw[3:end].strip()
    body = raw[end+3:]
    
    lines = fm_text.split('\n')
    fixed_lines = []
    in_dict_list = False
    dict_indent = None
    
    for line in lines:
        stripped = line.lstrip()
        if not stripped:
            fixed_lines.append(line)
            continue
        
        # Detect start of dict in a list
        if stripped.startswith('- ') and ':' in stripped.split(':')[0]:
            # Check if this is a dict (has key after -) vs a string list item
            remainder = stripped[2:].strip()
            if ':' in remainder and not remainder.startswith('['):
                # It's a dict list item
                in_dict_list = True
                dict_indent = None  # Reset, we'll detect from the line
                # Find the position of the '-'
                dash_pos = line.index('-')
                # The dict keys should be at dash_pos + 2 (two spaces after dash)
                fixed_lines.append(line)
                continue
        
        if in_dict_list and stripped and not stripped.startswith('#'):
            # Check if this should be part of the dict or a new list item
            if stripped.startswith('- '):
                # New list item
                in_dict_list = False
                dict_indent = None
                fixed_lines.append(line)
                continue
            
            # Check if line is at root level (should be indented)
            if not line.startswith(' '):
                # Needs indentation
                fixed_lines.append('  ' + line)
                continue
            elif line.startswith(' ') and len(line) - len(line.lstrip()) < 2:
                # Only 1 space indent, bump to 2
                fixed_lines.append(' ' + line)
                continue
        
        fixed_lines.append(line)
    
    fixed_fm = '\n'.join(fixed_lines)
    
    try:
        yaml.safe_load(fixed_fm)
        # Write back
        new_raw = '---\n' + fixed_fm + '\n---\n' + body
        with open(filepath, 'w') as fh:
            fh.write(new_raw)
        print(f"FIXED: {filepath}")
        return True
    except Exception as e:
        print(f"STILL BROKEN: {filepath}: {e}")
        return False

if __name__ == '__main__':
    for f in sys.argv[1:]:
        fix_yaml_indentation(f)
