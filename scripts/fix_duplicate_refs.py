#!/usr/bin/env python3
"""
Remove hardcoded ## References sections from page bodies when YAML sources: exist.
The hooks/obsidian_support.py already renders references from YAML frontmatter,
so the body-embedded section is a duplicate and often lower quality
(e.g. '(authors unknown)', plain text instead of formatted citations).

Pages WITHOUT YAML sources: kept untouched for now.
"""
import glob
import re
import sys

PAGE_PATTERNS = ['concepts/*.md', 'entities/*.md', 'comparisons/*.md']


def split_frontmatter_markdown(path: str) -> tuple[str, str]:
    """Return (frontmatter_text, body_text) for a --- delimited file."""
    with open(path, 'r') as f:
        content = f.read()
    if not content.startswith('---'):
        return '', content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return '', content
    return parts[1], parts[2]


def has_yaml_sources(frontmatter: str) -> bool:
    """True if frontmatter contains a non-empty sources: list."""
    return bool(re.search(r'^sources:\s*$\n^\s*-', frontmatter, re.MULTILINE))


def remove_body_references(body: str) -> str | None:
    """
    Remove the body ## References section if present.
    Returns new body, or None if nothing changed.
    """
    # Match from ## References to end of file (these are typically the last section)
    # Allow for optional trailing whitespace/newlines
    pattern = re.compile(
        r'\n## References\s*\n.*$',
        re.DOTALL | re.IGNORECASE,
    )
    new_body = pattern.sub('\n', body)
    if new_body == body:
        return None
    # Clean up trailing whitespace from removal
    new_body = new_body.rstrip() + '\n'
    return new_body


def main():
    changed = 0
    unchanged = 0
    skipped_no_yaml = 0
    skipped_no_body = 0

    for pattern in PAGE_PATTERNS:
        for path in glob.glob(pattern):
            fm, body = split_frontmatter_markdown(path)
            if not fm:
                continue

            if not has_yaml_sources(fm):
                skipped_no_yaml += 1
                continue

            if '## References' not in body:
                skipped_no_body += 1
                continue

            new_body = remove_body_references(body)
            if new_body is None:
                unchanged += 1
                continue

            # Write back
            with open(path, 'w') as f:
                f.write('---')
                f.write(fm)
                f.write('---')
                f.write(new_body)
            changed += 1
            print(f'REMOVED body refs: {path}')

    print(f'\nSummary: {changed} fixed, {unchanged} unchanged, '
          f'{skipped_no_yaml} skipped (no YAML sources), '
          f'{skipped_no_body} skipped (no body refs)')


if __name__ == '__main__':
    main()
