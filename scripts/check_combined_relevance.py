#!/usr/bin/env python3
"""
Combined relevance filter: graph distance + embedding similarity + word count.
Shows that graph distance from core resolves the embedding false positives.
"""
import re, json, os, glob, queue
import numpy as np

WIKI_ROOT = os.path.expanduser("~/src/tvb-wiki")
os.chdir(WIKI_ROOT)

# === BUILD LINK GRAPH ===
def extract_links(path):
    try:
        with open(path) as f:
            return re.findall(r'\[\[(?P<slug>[^|\]]+)', f.read())
    except:
        return []

outlinks = {}
indegree = {}
for p in glob.glob("entities/*.md") + glob.glob("concepts/*.md") + glob.glob("comparisons/*.md"):
    slug = os.path.basename(p)[:-3]
    links = extract_links(p)
    outlinks[slug] = links
    for t in links:
        indegree[t] = indegree.get(t, 0) + 1

all_slugs = set(list(outlinks.keys()) + list(indegree.keys()))

CORE = {"the-virtual-brain","tvb","whole-brain-modeling","connectome",
        "neural-mass-model","forward-model","source-localization",
        "eeg","neuroimaging","computational-neuroscience",
        "fsl","freesurfer","nilearn","nest","brian2","mne-python"}

dist = {s: 0 for s in CORE if s in all_slugs}
q = queue.Queue()
for c in dist: q.put(c)
while not q.empty():
    curr = q.get()
    for t in outlinks.get(curr, []):
        if t not in dist:
            dist[t] = dist[curr] + 1
            q.put(t)
for s in all_slugs:
    if s not in dist: dist[s] = 999

# === WORD COUNT ===
def real_wc(path):
    try:
        with open(path) as f:
            raw = f.read()
        parts = raw.split("---")
        body = parts[-1] if len(parts) >= 3 else raw
        lines = [ln for ln in body.splitlines() if not re.match(r"\*Placeholder|##?\s+", ln.strip())]
        return len(" ".join(lines).split())
    except: return 0

# === EMBEDDINGS ===
idx = json.load(open("meta/embeddings/wiki_index.json"))
emb = np.load("meta/embeddings/wiki_embeddings.npy")
page_embs = {}
for e in idx:
    if e["count"] == 0: continue
    page_embs[e["slug"]] = np.mean(emb[e["offset"]:e["offset"]+e["count"]], axis=0)

slugs_emb = list(page_embs.keys())
mat = np.vstack([page_embs[s] for s in slugs_emb])
mat_n = mat / np.linalg.norm(mat, axis=1, keepdims=True)
core_i = [i for i, s in enumerate(slugs_emb) if s in CORE]
centroid = np.mean(mat[core_i], axis=0)
centroid /= np.linalg.norm(centroid)
sim = mat_n @ mat_n.T

def get_scores(slug):
    if slug not in page_embs:
        return None, None, None
    i = slugs_emb.index(slug)
    c_score = float(np.dot(mat_n[i], centroid))
    top_nei = np.argsort(-sim[i])[1:31]
    p_score = len([n for n in top_nei if n in core_i]) / 30.0
    return c_score, p_score, c_score * p_score

print("Combined Relevance Filter: graph distance + embeddings")
print("Page                         words in_deg dist emb_c  emb_h   category")
print("-" * 80)

TEST = [
    ("core", "the-virtual-brain"), ("core", "tvb"), ("core", "connectome"),
    ("core", "neural-mass-model"), ("core", "eeg"),
    ("math/bio", "bifurcation-theory"), ("math/bio", "dynamical-systems-theory"),
    ("math/bio", "nonlinear-dynamics"), ("math/bio", "wilson-cowan-model"), ("math/bio", "izhikevich"),
    ("distant", "carlsim"), ("distant", "steps"), ("distant", "psyneulink"), ("distant", "lfp-lib"),
    ("generic", "pandas"), ("generic", "matplotlib"), ("generic", "scipy"),
    ("generic", "seaborn"), ("generic", "plotly"), ("generic", "scikit-learn"),
    ("generic", "pytorch"), ("generic", "braincode"),
]

for cat, slug in TEST:
    path_tmp = None
    for d in ["entities","concepts","comparisons"]:
        p_tmp = f"{d}/{slug}.md"
        if os.path.exists(p_tmp):
            path_tmp = p_tmp
            break
    wc = real_wc(path_tmp) if path_tmp else 0
    ideg = indegree.get(slug, 0)
    d_str = "∞" if dist.get(slug, 999) == 999 else str(dist.get(slug, 999))
    c, p, h = get_scores(slug)
    emb_c_s = f"{c:.2f}" if c is not None else "---"
    emb_h_s = f"{h:.3f}" if h is not None else "---"
    print(f"{slug:<30s} {wc:>5d} {ideg:>6d} {d_str:<3s} {emb_c_s:>6s} {emb_h_s:>6s}  {cat}")

# === COMBINED SCORING ===
print("\n" + "=" * 80)
print("COMBINED FILTER: reject only if word_count < 20 AND dist >= 5")
print("(This keeps math/bio pages connected to core, rejects empty generic stubs)")
print("-" * 80)
rejected = []
for slug in all_slugs:
    path_tmp = None
    for d in ["entities","concepts","comparisons"]:
        p_tmp = f"{d}/{slug}.md"
        if os.path.exists(p_tmp):
            path_tmp = p_tmp
            break
    wc = real_wc(path_tmp) if path_tmp else 0
    d_val = dist.get(slug, 999)
    c, p, h = get_scores(slug)
    if c is None: c = 0
    if h is None: h = 0
    # Combined rejection rule
    if wc < 20 and d_val >= 5:
        rejected.append((slug, wc, d_val, h))

rejected.sort(key=lambda x: x[1])
print(f"Rejected: {len(rejected)} pages")
for slug, wc, d_val, h in rejected[:20]:
    print(f"  {slug:<30s} {wc:>4d} words  dist={d_val:>3d}  hybrid={h:.3f}")
if len(rejected) > 20:
    print(f"  ... and {len(rejected)-20} more")
