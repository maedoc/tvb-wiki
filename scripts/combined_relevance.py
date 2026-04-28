#!/usr/bin/env python3
"""
scripts/combined_relevance.py — Combined graph distance + embedding relevance filter.

Goal: avoid false negatives on relevant pages that exist as content but are
not yet linked from the TVB core pages (orphans).

Usage:
    python3 scripts/combined_relevance.py --all  # score every page
    python3 scripts/combined_relevance.py --flag   # list rejection candidates
"""

import json, os, glob, re, sys, queue
import argparse
import numpy as np

WIKI_ROOT = os.path.dirname(os.path.dirname(__file__))
META_DIR = os.path.join(WIKI_ROOT, "meta", "embeddings")

# TVB core pages for graph BFS anchor set
CORE_LINKS = {"the-virtual-brain", "tvb", "whole-brain-modeling", "connectome",
                "neural-mass-model", "forward-model", "source-localization",
                "eeg", "meg", "neuroimaging", "computational-neuroscience",
                "fsl", "freesurfer", "nilearn", "nest", "brian2", "mne-python"}


def real_wc(path):
    """Count non-template words after stripping frontmatter."""
    try:
        with open(path) as fh:
            raw = fh.read()
        parts = raw.split("---")
        body = parts[-1] if len(parts) >= 3 else raw
        lines = [ln for ln in body.splitlines()
                 if not re.match(r"\*Placeholder|##?\s+", ln.strip())]
        return len(" ".join(lines).split())
    except Exception:
        return 0


def load_graph(wiki_root):
    """Return (outlinks dict, indegree dict, all_slugs set)."""
    outlinks = {}
    indegree = {}
    for p in glob.glob(os.path.join(wiki_root, "entities/*.md")) + \
            glob.glob(os.path.join(wiki_root, "concepts/*.md")) + \
            glob.glob(os.path.join(wiki_root, "comparisons/*.md")):
        slug = os.path.basename(p)[:-3]
        with open(p) as f:
            text = f.read()
        links = re.findall(r"\[\[(?P<slug>[^|\]]+)", text)
        outlinks[slug] = links
        for t in links:
            indegree[t] = indegree.get(t, 0) + 1
    all_slugs = set(list(outlinks.keys()) + list(indegree.keys()))
    return outlinks, indegree, all_slugs


def bfs_distances(outlinks, all_slugs, core):
    """Graph distance from any core page. 999 = unreachable."""
    dist = {s: 0 for s in core if s in all_slugs}
    q = queue.Queue()
    for c in dist:
        q.put(c)
    while not q.empty():
        curr = q.get()
        for t in outlinks.get(curr, []):
            if t not in dist:
                dist[t] = dist[curr] + 1
                q.put(t)
    for s in all_slugs:
        if s not in dist:
            dist[s] = 999
    return dist


def load_embeddings(wiki_root):
    """Return (page_embs dict, centroid np.array, core_indices list, sim matrix, mat_n)."""
    idx = json.load(open(os.path.join(META_DIR, "wiki_index.json")))
    emb = np.load(os.path.join(META_DIR, "wiki_embeddings.npy"))

    page_embs = {}
    for e in idx:
        if e["count"] == 0:
            continue
        vecs = emb[e["offset"]:e["offset"]+e["count"]]
        page_embs[e["slug"]] = np.mean(vecs, axis=0)

    slugs_emb = list(page_embs.keys())
    mat = np.vstack([page_embs[s] for s in slugs_emb])
    mat_n = mat / np.linalg.norm(mat, axis=1, keepdims=True)
    core_i = [i for i, s in enumerate(slugs_emb) if s in CORE_LINKS]
    centroid = np.mean(mat[core_i], axis=0)
    centroid /= np.linalg.norm(centroid)
    sim = mat_n @ mat_n.T
    return page_embs, slugs_emb, centroid, core_i, sim, mat_n


def get_emb_scores(slug, page_embs, slugs_emb, mat_n, centroid, core_i, sim):
    if slug not in page_embs:
        return None, None, None
    i = slugs_emb.index(slug)
    c_score = float(np.dot(mat_n[i], centroid))
    top_nei = np.argsort(-sim[i])[1:31]
    p_score = len([n for n in top_nei if n in core_i]) / 30.0
    h_score = c_score * p_score
    return c_score, p_score, h_score


def decision(wc, g_dist, c_score, h_score):
    """
    Combined decision logic:

      - stub             -> always flag (regardless of graph distance)
      - g_dist 0-3       -> accept (graph-linked relevance)
      - g_dist finite, emb high -> accept (orphan but semantically relevant)
      - g_dist finite, emb low  -> review
      - g_dist infinite, emb high -> accept (unlinked orphan, maybe new content)
      - g_dist infinite, emb low  -> reject (isolated + semantically distant)
    """
    if wc < 20:
        return "stub", "Almost empty — likely auto-generated stub"

    if g_dist <= 3:
        return "accept", f"Graph-linked (distance {g_dist})"

    if c_score is None:
        # no embedding: treat as unknown
        if g_dist == 999:
            return "review", "Unreachable graph + no embedding"
        return "review", f"Distance {g_dist} but no embedding"

    if g_dist == 999 and h_score >= 0.03:
        return "accept", f"Unlinked orphan but high semantic relevance (hybrid={h_score:.3f})"

    if g_dist == 999 and h_score < 0.03:
        return "reject", f"Unreachable graph + low semantic relevance (hybrid={h_score:.3f})"

    if h_score >= 0.03:
        return "accept", f"Semantically relevant even at graph distance {g_dist}"

    return "review", f"Distant graph ({g_dist}) + moderate semantics (hybrid={h_score:.3f})"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--flag", action="store_true", help="List rejection candidates")
    args = parser.parse_args()

    outlinks, indegree, all_slugs = load_graph(WIKI_ROOT)
    page_embs, slugs_emb, centroid, core_i, sim, mat_n = load_embeddings(WIKI_ROOT)
    g_dist = bfs_distances(outlinks, all_slugs, CORE_LINKS)

    # Index slug -> path
    slug_path = {}
    for e in json.load(open(os.path.join(META_DIR, "wiki_index.json"))):
        if e.get("path"):
            slug_path[e["slug"]] = e["path"]

    results = []
    categories = {"accept": 0, "stub": 0, "reject": 0, "review": 0}

    for slug in sorted(all_slugs):
        path_tmp = slug_path.get(slug)
        wc = real_wc(path_tmp) if path_tmp else 0
        d = g_dist.get(slug, 999)
        c, p, h = get_emb_scores(slug, page_embs, slugs_emb, mat_n, centroid, core_i, sim)
        cat, reason = decision(wc, d, c, h)
        categories[cat] = categories.get(cat, 0) + 1
        results.append({
            "slug": slug, "wc": wc, "indeg": indegree.get(slug, 0),
            "g_dist": d,
            "centroid": c, "hybrid": h,
            "cat": cat, "reason": reason,
            "path": path_tmp,
        })

    print(f"Total pages: {len(all_slugs)}")
    print(f"  accept : {categories['accept']}")
    print(f"  review : {categories['review']}")
    print(f"  reject : {categories['reject']}")
    print(f"  stub   : {categories['stub']}")

    # Header
    hdr = f"{'page':<30s} {'wc':>5s} {'in':>4s} {'g':>3s} {'centroid':>8s} {'hybrid':>6s} {'verdict':<8s}"
    print(f"\n{hdr}")
    print("-" * len(hdr))

    if args.flag:
        # Show only non-accepted for triage
        for r in sorted(results, key=lambda x: (x["cat"] != "reject", x["cat"] != "stub",
                                                 x["cat"] != "review", -x["g_dist"], x["slug"])):
            if r["cat"] == "accept":
                continue
            cs = f"{r['centroid']:.2f}" if r['centroid'] is not None else " ---"
            hs = f"{r['hybrid']:.3f}" if r['hybrid'] is not None else " ---"
            dg = "∞" if r["g_dist"] == 999 else str(r["g_dist"])
            print(f"{r['slug']:<30s} {r['wc']:>5d} {r['indeg']:>4d} {dg:>3s} {cs:>8s} {hs:>6s}  {r['cat']}")
    else:
        # Show a mix of examples
        examples = [
            ("core", "the-virtual-brain"), ("core", "tvb"),
            ("core", "connectome"), ("core", "neural-mass-model"),
            ("math/bio", "bifurcation-theory"), ("math/bio", "dynamical-systems-theory"),
            ("math/bio", "nonlinear-dynamics"), ("math/bio", "izhikevich"),
            ("generic", "plotly"), ("generic", "pandas"), ("generic", "matplotlib"),
            ("distant", "carlsim"), ("distant", "steps"), ("distant", "psyneulink"),
        ]
        for label, slug in examples:
            r = next((x for x in results if x["slug"] == slug), None)
            if not r:
                continue
            cs = f"{r['centroid']:.2f}" if r['centroid'] is not None else " ---"
            hs = f"{r['hybrid']:.3f}" if r['hybrid'] is not None else " ---"
            dg = "∞" if r["g_dist"] == 999 else str(r["g_dist"])
            print(f"{r['slug']:<30s} {r['wc']:>5d} {r['indeg']:>4d} {dg:>3s} {cs:>8s} {hs:>6s}  {r['cat']}  ({label})")


if __name__ == "__main__":
    main()
