#!/usr/bin/env python3
"""
Ralph Crosslink Agent — suggests wikilinks between wiki pages using embeddings.
Uses the existing embedding index from the Matcher.
"""
import os, sys, re, json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ralph_config import get_logger, WIKI_ROOT, get_all_pages, read_page

log = get_logger("Crosslink")

EMBED_DIR = os.path.join(WIKI_ROOT, "meta", "embeddings")
WIKI_EMBED_FILE = os.path.join(EMBED_DIR, "wiki_embeddings.npy")
WIKI_INDEX_FILE = os.path.join(EMBED_DIR, "wiki_index.json")
OUTPUT_FILE = os.path.join(EMBED_DIR, "crosslink_suggestions.json")

SIM_THRESHOLD = 0.6
MIN_MATCHING = 2
MAX_SUGGESTIONS = 200


def normalize(v):
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    return v / np.maximum(norms, 1e-8)


def get_existing_links(slug: str) -> set[str]:
    """Get set of slugs already linked from this page."""
    pages = get_all_pages()
    if slug not in pages:
        return set()
    try:
        _, content = read_page(pages[slug])
        links = re.findall(r'\[\[([^\]|]+)', content)
        return {l.strip().lower().replace(' ', '-') for l in links}
    except:
        return set()


def find_crosslinks():
    """Find cross-page link suggestions using embedding similarity."""
    emb = np.load(WIKI_EMBED_FILE)
    with open(WIKI_INDEX_FILE) as f:
        idx = json.load(f)
    
    emb_norm = normalize(emb)
    pages = get_all_pages()
    
    # Build page offset map
    page_map = {}
    for entry in idx:
        page_map[entry['slug']] = entry
    
    # Compute full similarity matrix
    log.info("Computing wiki self-similarity (%d sentences)...", emb.shape[0])
    sims = emb_norm @ emb_norm.T
    
    # For each page pair, count matching sentences
    suggestions = []
    all_slugs = [e['slug'] for e in idx if e['count'] > 0]
    
    for i, slug_a in enumerate(all_slugs):
        entry_a = page_map[slug_a]
        existing = get_existing_links(slug_a)
        
        for j, slug_b in enumerate(all_slugs):
            if slug_a == slug_b or slug_b in existing:
                continue
            
            entry_b = page_map[slug_b]
            
            # Slice similarity: page_a sentences vs page_b sentences
            sub = sims[entry_a['offset']:entry_a['offset']+entry_a['count'],
                       entry_b['offset']:entry_b['offset']+entry_b['count']]
            
            # Count how many of page_a's sentences have a good match in page_b
            max_per_a = sub.max(axis=1)
            matching = int((max_per_a >= SIM_THRESHOLD).sum())
            
            if matching >= MIN_MATCHING:
                score = float(max_per_a.max()) * (1 + 0.1 * matching)
                suggestions.append({
                    "from": slug_a,
                    "to": slug_b,
                    "score": round(score, 3),
                    "matching_sentences": matching,
                    "best_sim": round(float(max_per_a.max()), 3),
                })
    
    # Sort and limit
    suggestions.sort(key=lambda x: x['score'], reverse=True)
    suggestions = suggestions[:MAX_SUGGESTIONS]
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(suggestions, f, indent=2)
    
    log.info("Found %d crosslink suggestions (saved to %s)", len(suggestions), OUTPUT_FILE)
    return suggestions


if __name__ == '__main__':
    find_crosslinks()
