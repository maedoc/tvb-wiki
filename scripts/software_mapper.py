#!/usr/bin/env python3
"""
Ralph Software Mapper Agent — weekly, ensures every tool in the TVB ecosystem has a page.

Two-model approach: both kimi-k2.6 and glm-5.1 independently identify gaps,
union of results creates pages, then reviewer checks accuracy.
"""
import os
import sys
import re
import json
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    SCHEMA_PATH, append_log, git_commit, get_all_pages, run_pi,
    WRITER_MODEL, REVIEWER_MODEL,
)

log = get_logger("SoftwareMapper")

# ── Known TVB ecosystem software ──────────────────────────────────────

KNOWN_SOFTWARE = {
    'tvb': 'TVB (The Virtual Brain)',
    'the-virtual-epileptic-brain': 'The Virtual Epileptic Brain',
    'nest': 'NEST Simulator',
    'neuron': 'NEURON',
    'brian': 'Brian',
    'brian2': 'Brian2',
    'arbor': 'Arbor',
    'coreneuron': 'CoreNEURON',
    'dynasim': 'DynaSim',
    'spm': 'SPM (Statistical Parametric Mapping)',
    'fsl': 'FSL (FMRIB Software Library)',
    'ants': 'ANTs (Advanced Normalization Tools)',
    'freesurfer': 'FreeSurfer',
    'mrtrix': 'MRtrix3',
    'mrtrix3': 'MRtrix3',
    'dsi-studio': 'DSI Studio',
    'graphvar': 'GraphVar',
    'brain-connectivity-toolbox': 'Brain Connectivity Toolbox',
    'nilearn': 'Nilearn',
    'conn': 'CONN Toolbox',
    'fieldtrip': 'FieldTrip',
    'mne-python': 'MNE-Python',
    'eeglab': 'EEGLAB',
    'brainstorm': 'Brainstorm',
    'itk-snap': 'ITK-SNAP',
    'paraview': 'ParaView',
    'modeldb': 'ModelDB',
    'neuromorpho': 'NeuroMorpho.Org',
    'allen-brain-atlas': 'Allen Brain Atlas',
    'openneuro': 'OpenNeuro',
    'human-connectome-project': 'Human Connectome Project',
    'netneuroscience': 'netneuroscience toolkit',
    'neuroml': 'NeuroML',
    'lfp-lib': 'LFPy',
    'tvb-multiscale': 'TVB-NEST multiscale',
    'tvb-library': 'TVB Library',
    'tvb-adapters': 'TVB Adapters',
}


def find_missing_software() -> list[tuple[str, str]]:
    """Find known software that doesn't have a page yet."""
    pages = get_all_pages()
    missing = []

    for slug, title in KNOWN_SOFTWARE.items():
        if slug not in pages:
            missing.append((slug, title))

    return sorted(missing)


def create_software_page(slug: str, title: str) -> bool:
    """Create a stub page for a software tool."""
    filepath = os.path.join(ENTITIES_DIR, f"{slug}.md")
    if os.path.exists(filepath):
        return False

    os.makedirs(ENTITIES_DIR, exist_ok=True)
    today = datetime.date.today().isoformat()

    content = f"""---
title: {title}
created: {today}
updated: {today}
type: entity
tags: [software-brain-modeling]
sources: []
---

# {title}

## Overview
*Placeholder — awaiting content from Ralph Improver.*

## Key Features
*Placeholder*

## Relationship to TVB
*Placeholder*

## Key Papers
*Placeholder*

## Related Software
* [[TVB]]

## References
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def build_gap_analysis_prompt() -> str:
    """Build a prompt asking the LLM to identify missing software."""
    pages = get_all_pages()

    # List existing entity pages
    entity_pages = sorted([slug for slug in pages if os.path.exists(
        os.path.join(ENTITIES_DIR, f"{slug}.md"))])

    prompt = f"""You are analyzing a TVB Wiki (The Virtual Brain ecosystem knowledge base).
Your task is to identify software tools that should have pages but are missing.

EXISTING ENTITY PAGES:
{chr(10).join('- ' + p for p in entity_pages)}

DOMAIN: Whole-brain modeling, computational neuroscience, neuroimaging, connectomics.

List software tools that are important to this domain but DON'T have pages yet.
For each tool, provide:
- Tool name
- Slug (lowercase, hyphens)
- Category (simulation, neuroimaging, connectivity-analysis, eeg-meg, atlas, database, visualization)
- One-line description

Output as a JSON array:
[
  {{"name": "Tool Name", "slug": "tool-name", "category": "simulation", "description": "one line"}}
]

List up to 20 tools. Output ONLY valid JSON, no other text."""
    return prompt


def llm_gap_analysis(model: str) -> list[dict]:
    """Ask an LLM to identify missing software."""
    prompt = build_gap_analysis_prompt()
    success, output = run_pi(prompt, model=model)

    if not success:
        log.warn("Gap analysis failed with %s: %s", model, output[:100])
        return []

    # Extract JSON from output
    try:
        # Try to find JSON array in output
        json_match = re.search(r'\[.*\]', output, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except json.JSONDecodeError:
        log.warn("Could not parse JSON from %s gap analysis", model)

    return []


def review_new_pages(slugs: list[str]) -> dict:
    """Have the reviewer check newly created pages."""
    results = {}
    for slug in slugs:
        filepath = os.path.join(ENTITIES_DIR, f"{slug}.md")
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        prompt = f"""Review this new wiki page for the TVB Wiki.
Check: Is this software tool real? Is the description accurate?
Does it belong in a TVB/whole-brain modeling wiki?

PAGE: {slug}
{content[:2000]}

Reply ONLY: VERDICT: OK or VERDICT: REMOVE (with reason)"""

        success, output = run_pi(prompt, model=REVIEWER_MODEL, tools="read")
        if success:
            results[slug] = 'ok' if 'ok' in output.lower() else 'flagged'
        else:
            results[slug] = 'unknown'

    return results


# ── Main mapper cycle ─────────────────────────────────────────────────

def run_software_mapper_cycle():
    """Run one software mapper cycle."""
    log.info("Starting weekly cycle")

    # 1. Find missing from known list
    missing_known = find_missing_software()
    log.info("Known software missing pages: %d", len(missing_known))

    # 2. Create stubs for known missing software
    created = 0
    for slug, title in missing_known:
        if create_software_page(slug, title):
            log.info("Created stub: %s", slug)
            created += 1

    # 3. LLM gap analysis — both models independently
    log.info("Running gap analysis with %s...", WRITER_MODEL)
    gaps_a = llm_gap_analysis(WRITER_MODEL)
    log.info("  Found %d gaps", len(gaps_a))

    log.info("Running gap analysis with %s...", REVIEWER_MODEL)
    gaps_b = llm_gap_analysis(REVIEWER_MODEL)
    log.info("  Found %d gaps", len(gaps_b))

    # 4. Union of gaps
    all_gaps = {}
    for item in gaps_a + gaps_b:
        slug = item.get('slug', '')
        if slug:
            all_gaps[slug] = item

    # 5. Create pages for LLM-identified gaps
    pages = get_all_pages()
    llm_created = 0
    for slug, info in all_gaps.items():
        if slug not in pages:
            title = info.get('name', slug.replace('-', ' ').title())
            if create_software_page(slug, title):
                log.info("Created LLM-identified: %s — %s", slug, info.get('description', '')[:60])
                llm_created += 1

    # 6. Review new pages
    new_slugs = [s for s, _ in missing_known] + list(all_gaps.keys())
    if new_slugs:
        log.info("Reviewing %d new pages...", len(new_slugs))
        reviews = review_new_pages(new_slugs[:10])
        for slug, verdict in reviews.items():
            if verdict == 'flagged':
                log.warn("Reviewer flagged: %s", slug)

    # 7. Git commit
    total_created = created + llm_created
    if total_created > 0:
        msg = f"Map: created {total_created} software pages ({created} known, {llm_created} LLM-identified) (SoftwareMapper)"
        git_commit(msg)
        append_log(f"SoftwareMapper: {total_created} pages created")

    log.info("Cycle complete. %d pages created.", total_created)
    return total_created


# ── CLI entry point ───────────────────────────────────────────────────

if __name__ == '__main__':
    run_software_mapper_cycle()
