#!/usr/bin/env python3
"""
Create stubs for missing concept pages that are referenced by wikilinks.
For pages with 5+ refs, creates slightly larger stubs.
For pages with <5 refs, creates minimal stubs with frontmatter.
"""
import os
import json
import datetime

WIKI_ROOT = "/home/duke/src/tvb-wiki"

def create_stub(target, count, sources_list, all_pages):
    """Create a stub page for a missing target."""
    # Determine directory
    if any(x in target for x in ['software-', 'tool', 'suite', 'platform', 'library']):
        directory = os.path.join(WIKI_ROOT, "entities")
        ptype = "entity"
    else:
        directory = os.path.join(WIKI_ROOT, "concepts")
        ptype = "concept"
    
    filepath = os.path.join(directory, f"{target}.md")
    if os.path.exists(filepath):
        return False
    
    # Generate related links from source pages (filter to existing pages)
    related = [s for s in sources_list if s in all_pages and s != target][:8]
    related_md = "\n".join(f"* [[{r}]]" for r in related) or "* Placeholder for related concepts"
    
    title = target.replace('-', ' ').title()
    
    if count >= 5:
        # Larger stub for high-impact pages
        content = f"""---
created: {datetime.date.today().isoformat()}
sources: []
tags:
- {target}
title: {title}
type: {ptype}
updated: {datetime.date.today().isoformat()}
---

{title} is a key concept in {ptype == 'concept' and 'computational neuroscience and whole-brain modeling' or 'the neuroimaging software ecosystem'}. This page provides an overview of {title} and its role in the broader landscape of brain modeling and analysis.

## Definition
*Placeholder for formal definition of {title}.*

## Role in Whole-Brain Modeling
*Placeholder for how this concept is used in modeling.*

## Related Concepts
{related_md}

## References
*Links to relevant papers.*
"""
    else:
        # Minimal stub
        content = f"""---
created: {datetime.date.today().isoformat()}
sources: []
tags:
- {target}
title: {title}
type: {ptype}
updated: {datetime.date.today().isoformat()}
---

{title} — a concept in whole-brain modeling and computational neuroscience.

## Related Concepts
{related_md}
"""

    with open(filepath, 'w') as f:
        f.write(content)
    return True

if __name__ == '__main__':
    import re
    from collections import Counter, defaultdict

    # Load audit data
    with open(os.path.join(WIKI_ROOT, "meta/audit_report.json")) as f:
        d = json.load(f)
    
    # Build existing pages and refs-to list
    all_pages = set()
    for dir in ['concepts', 'entities', 'comparisons']:
        for p in os.listdir(os.path.join(WIKI_ROOT, dir)):
            if p.endswith('.md'):
                all_pages.add(p[:-3])
    
    broken_targets = Counter(b['target'] for b in d['broken_wikilinks'])
    refs_to = defaultdict(list)
    for b in d['broken_wikilinks']:
        refs_to[b['target']].append(b['source'])
    
    # Filter to truly missing pages
    skip_chars = ['[', ']', '|', '–', '#', ',']
    missing = []
    for target, count in broken_targets.most_common():
        if target in all_pages:
            continue
        if any(c in target for c in skip_chars):
            continue
        if len(target) < 2 or len(target) > 80:
            continue
        missing.append((target, count, refs_to[target]))
    
    created = 0
    for target, count, sources in missing:
        if create_stub(target, count, sources, all_pages):
            created += 1
            print(f"Created stub: {target} ({count} refs)")
    
    print(f"\nTotal stubs created: {created}")
