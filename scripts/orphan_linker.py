#!/usr/bin/env python3
"""
Ralph Orphan Linker — bi-weekly agent that links valid orphans into the core graph.

Finds pages with graph_dist=999 but hybrid>=0.03 (accepted, relevant, but unlinked).
Adds wikilinks from nearest graph-connected pages' "Related Concepts" sections.
"""
import os, sys, re, datetime, queue
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import (
    get_logger, WIKI_ROOT, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
    get_all_pages, git_commit, append_log,
)
from combined_relevance import load_graph, load_embeddings, bfs_distances, CORE_LINKS, get_emb_scores

log = get_logger("OrphanLinker")


def find_orphans():
    """Find accepted but unlinked pages."""
    outlinks, indegree, all_slugs = load_graph(WIKI_ROOT)
    page_embs, slugs_emb, centroid, core_i, sim, mat_n = load_embeddings(WIKI_ROOT)
    g_dist = bfs_distances(outlinks, all_slugs, CORE_LINKS)
    
    orphan_pages = []
    for slug in all_slugs:
        d = g_dist.get(slug, 999)
        if d == 999:
            c, p, h = get_emb_scores(slug, page_embs, slugs_emb, mat_n, centroid, core_i, sim)
            if h is not None and h >= 0.03:
                orphan_pages.append((slug, h, indegree.get(slug, 0)))
    return sorted(orphan_pages, key=lambda x: x[1], reverse=True)


def find_nearest_linked(slug, all_slugs, outlinks, g_dist):
    """BFS from orphan backwards to find nearest linked page (reverse BFS on inlinks)."""
    # Build reverse link graph
    inlinks = {s: [] for s in all_slugs}
    for s, targets in outlinks.items():
        for t in targets:
            if t in inlinks:
                inlinks[t].append(s)
            else:
                inlinks[t] = [s]
    
    # BFS from orphan outward on incoming links
    visited = {slug}
    q = queue.Queue()
    q.put((slug, 0))
    while not q.empty():
        curr, dist = q.get()
        sources = inlinks.get(curr, [])
        for src in sources:
            if g_dist.get(src, 999) < 999:  # Found a linked page!
                return src, dist + 1
            if src not in visited:
                visited.add(src)
                q.put((src, dist + 1))
    return None, -1


def add_link_to_page(target_slug, source_slug):
    """Add a wikilink to target_slug in source_slug's Related Concepts section."""
    filepath = None
    for d in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR]:
        f = os.path.join(d, f'{source_slug}.md')
        if os.path.exists(f):
            filepath = f
            break
    if not filepath:
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if link already exists
    if f'[[{target_slug}]]' in content or f'[[{target_slug}|' in content:
        return False
    
    # Find Related Concepts section
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if re.match(r'## Related Concepts', line, re.I):
            # Insert before next heading or end of section
            for j in range(i + 1, len(lines)):
                if lines[j].startswith('## '):
                    lines.insert(j, f"- [[{target_slug}]]")
                    break
            else:
                lines.append(f"- [[{target_slug}]]")
            break
    else:
        # No Related Concepts section → add one before References
        for i, line in enumerate(lines):
            if re.match(r'## References', line, re.I):
                lines.insert(i, '')
                lines.insert(i, f'- [[{target_slug}]]')
                lines.insert(i, '## Related Concepts')
                break
    
    new_content = '\n'.join(lines)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def run_orphan_linker_cycle(max_links: int = 20):
    """Run one orphan linker cycle. Returns number of links added."""
    log.info("Starting orphan linker cycle")
    
    outlinks, indegree, all_slugs = load_graph(WIKI_ROOT)
    page_embs, slugs_emb, centroid, core_i, sim, mat_n = load_embeddings(WIKI_ROOT)
    g_dist = bfs_distances(outlinks, all_slugs, CORE_LINKS)
    
    orphans = []
    for slug in all_slugs:
        d = g_dist.get(slug, 999)
        if d == 999:
            c, p, h = get_emb_scores(slug, page_embs, slugs_emb, mat_n, centroid, core_i, sim)
            if h is not None and h >= 0.03:
                orphans.append(slug)
    
    if not orphans:
        log.info("No orphans to link")
        return 0
    
    log.info("Found %d accepted orphans to link", len(orphans))
    
    added = 0
    linked_orphans = []
    for slug in orphans[:max_links]:
        source, dist = find_nearest_linked(slug, all_slugs, outlinks, g_dist)
        if source and dist > 0:
            if add_link_to_page(slug, source):
                log.info("Linked orphan %s from %s (distance %d)", slug, source, dist)
                added += 1
                linked_orphans.append(slug)
            else:
                log.info("Could not add link for %s (already linked or no section)", slug)
    
    if added > 0:
        msg = f"OrphanLinker: linked {added} orphans ({', '.join(linked_orphans)})"
        git_commit(msg)
        append_log(msg)
    
    log.info("Cycle complete. %d links added.", added)
    return added


if __name__ == '__main__':
    run_orphan_linker_cycle()
