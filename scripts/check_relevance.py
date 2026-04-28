#!/usr/bin/env python3
"""
scripts/check_relevance.py — Test whether embeddings can automatically identify
irrelevant pages (e.g. generic software created by SoftwareMapper).

Usage: python3 scripts/check_relevance.py [--flag] [--threshold 0.03]
"""
import json, numpy as np, os, sys, re
import argparse

WIKI_ROOT = os.path.dirname(os.path.dirname(__file__))
META_DIR = os.path.join(WIKI_ROOT, "meta", "embeddings")
WIKI_EMBED_FILE = os.path.join(META_DIR, "wiki_embeddings.npy")
WIKI_INDEX_FILE = os.path.join(META_DIR, "wiki_index.json")

# Core TVB-relevant pages used to build centroid
TVB_CORE = [
    "the-virtual-brain", "tvb", "neural-mass-model", "brain-network",
    "connectome", "forward-model", "source-localization",
    "eeg", "meg", "neuroimaging", "computational-neuroscience",
    "fsl", "freesurfer", "nilearn", "nest", "brian2",
]


def load_embs():
    idx = json.load(open(WIKI_INDEX_FILE))
    emb = np.load(WIKI_EMBED_FILE)

    page_embs = {}
    for entry in idx:
        if entry["count"] == 0:
            continue
        vecs = emb[entry["offset"]:entry["offset"] + entry["count"]]
        page_embs[entry["slug"]] = np.mean(vecs, axis=0)
    return page_embs, idx


def real_word_count(path):
    """Count words that are NOT placeholder/template text."""
    try:
        with open(path) as fh:
            raw = fh.read()
    except:
        return -1

    # Strip frontmatter
    parts = raw.split("---")
    body = parts[-1] if len(parts) >= 3 else raw

    # Remove placeholder lines and markdown headings
    lines = [ln for ln in body.splitlines() if not re.match(r"\*Placeholder|##?\s+", ln.strip())]
    text = " ".join(lines)
    return len(text.split())


def cosine_sim(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def compute_scores(page_embs):
    slugs = list(page_embs.keys())
    mat = np.vstack([page_embs[s] for s in slugs])
    mat_n = mat / np.linalg.norm(mat, axis=1, keepdims=True)
    core_i = [i for i, s in enumerate(slugs) if s in TVB_CORE and s in page_embs]

    # centroid
    centroid = np.mean(mat[core_i], axis=0)
    centroid /= np.linalg.norm(centroid)
    centroid_scores = {s: cosine_sim(mat_n[i], centroid) for i, s in enumerate(slugs)}

    # neighborhood purity
    sim = mat_n @ mat_n.T
    purity = {}
    for i, s in enumerate(slugs):
        top_nei = np.argsort(-sim[i])[1:31]
        core_nei = [n for n in top_nei if n in core_i]
        purity[s] = len(core_nei) / 30.0

    # hybrid
    hybrid = {s: centroid_scores[s] * purity[s] for s in slugs}
    return centroid_scores, purity, hybrid


def scan_all(centroid_scores, purity, hybrid, idx):
    """Return flagged pages sorted by hybrid score."""
    idx_map = {e["slug"]: e for e in idx}
    flags = []

    for entry in idx:
        slug = entry["slug"]
        wc = real_word_count(entry["path"])

        reasons = []
        if wc < 20:
            reasons.append(f"almost_empty ({wc}w)")

        if slug in hybrid:
            h = hybrid[slug]
            c = centroid_scores[slug]
            p = purity[slug]
            if h < 0.03:
                reasons.append(f"hybrid_low ({h:.3f})")
            if c < 0.50:
                reasons.append(f"centroid_low ({c:.3f})")
            if p < 0.01:
                reasons.append(f"isolated ({p:.1%})")
        else:
            # no embedding at all
            reasons.append("no_embedding")

        if reasons:
            flags.append((slug, wc, hybrid.get(slug, 0), reasons, entry["path"]))

    # sort by hybrid score ascending (least relevant first)
    flags.sort(key=lambda x: x[2] if x[2] else 0)
    return flags


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--flag", action="store_true", help="Flag low-relevance pages")
    parser.add_argument("--threshold", type=float, default=0.03, help="Hybrid threshold (default 0.03)")
    args = parser.parse_args()

    print("Loading embeddings...")
    page_embs, idx = load_embs()
    centroid, purity, hybrid = compute_scores(page_embs)

    print(f"\nScored {len(page_embs)} pages. Core centroid built from {sum(1 for s in TVB_CORE if s in page_embs)} pages.")
    print(f"Centroid mean={np.mean(list(centroid.values())):.3f} std={np.std(list(centroid.values())):.3f}")
    print(f"Purity mean={np.mean(list(purity.values())):.3f} std={np.std(list(purity.values())):.3f}")

    # Show example categories
    print("\n=== EXAMPLE SCORES ===")
    for label, pages in [
        ("Core TVB", ["the-virtual-brain", "tvb", "neural-mass-model"]),
        ("TVB Tools", ["fsl", "nest", "brian2", "nilearn"]),
        ("Generic", ["plotly"] + [e["slug"] for e in idx if e["slug"] in ("pandas","matplotlib","scipy")]),
        ("Distant Neuro", ["carlsim", "steps", "psyneulink"]),
    ]:
        print(f"\n{label}:")
        for s in pages:
            if s in page_embs:
                print(f"  {s:<20s} h={hybrid[s]:.3f} c={centroid[s]:.3f} p={purity[s]:.1%}")
            elif s in {e['slug'] for e in idx}:
                print(f"  {s:<20s} (no embedding)")

    if args.flag:
        flags = scan_all(centroid, purity, hybrid, idx)
        print(f"\n\n=== {len(flags)} PAGES FLAGGED AS LOW-RELEVANCE ===")
        print(f"{'slug':<25s} {'words':>6s} {'hybrid':>7s} {'reasons'}")
        for slug, wc, h, reasons, path in flags:
            reason_str = ", ".join(reasons)
            print(f"{slug:<25s} {wc:>6d} {h:>7.3f}  {reason_str}")
    else:
        # Just show top/bottom hybrid
        hybrids = sorted(hybrid.items(), key=lambda kv: kv[1])
        print("\n\nBottom 10 hybrid:")
        for s, v in hybrids[:10]:
            print(f"  {s:<25s} {v:.3f}")

if __name__ == "__main__":
    main()
