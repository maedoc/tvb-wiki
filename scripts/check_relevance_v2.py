"""
Relevance detection v2:
1. Centroid similarity (TVB core affinity)
2. Neighborhood purity: fraction of nearest neighbors in TVB core
"""
import json, numpy as np, os

META_DIR = os.path.join(os.path.dirname(__file__), "..", "meta", "embeddings")
emb = np.load(os.path.join(META_DIR, "wiki_embeddings.npy"))
idx = json.load(open(os.path.join(META_DIR, "wiki_index.json")))

# Build per-page averaged embeddings
page_embs = {}
for entry in idx:
    if entry['count'] == 0: continue
    slug = entry['slug']
    vecs = emb[entry['offset']:entry['offset']+entry['count']]
    page_embs[slug] = np.mean(vecs, axis=0)

slugs = list(page_embs.keys())
mat = np.vstack([page_embs[s] for s in slugs])
mat_n = mat / np.linalg.norm(mat, axis=1, keepdims=True)

# Compute pairwise cosine similarity matrix
sim = mat_n @ mat_n.T  # n x n similarity

# Core pages
TVB_CORE = [
    'the-virtual-brain', 'tvb', 'neural-mass-model', 'brain-network',
    'connectome', 'forward-model', 'source-localization', 'eeg', 'meg',
    'neuroimaging', 'computational-neuroscience', 'fsl', 'freesurfer',
    'nilearn', 'nest', 'brian2'
]
core_indices = [i for i, s in enumerate(slugs) if s in TVB_CORE]
print(f"Core pages with embeddings: {len(core_indices)}")

# 1. Centroid similarity
centroid = np.mean(mat[core_indices], axis=0)
centroid /= np.linalg.norm(centroid)
centroid_scores = {s: float(np.dot(mat_n[i], centroid)) for i, s in enumerate(slugs)}

# 2. Neighborhood purity (among top-30 nearest neighbors, what fraction are core?)
purity_scores = {}
for i, s in enumerate(slugs):
    neighbors = np.argsort(-sim[i])[1:31]  # top 30 (excluding self)
    core_neighbors = [n for n in neighbors if n in core_indices]
    purity_scores[s] = len(core_neighbors) / 30.0

# Pages to evaluate
TEST_PAGES = {
    'irrelevant_generic': [
        'pandas', 'matplotlib', 'scipy', 'joblib', 'h5py',
        'seaborn', 'statsmodels', 'scikit-learn', 'pytorch', 'pyvista',
        'surfstat', 'braincode', 'pyedflib'
    ],
    'irrelevant_software': ['plotly', 'networkx'],  # improved, may be TVB-related
    'relevant_tools': [
        'fsl', 'freesurfer', 'the-virtual-brain', 'brian2', 'nest',
        'nilearn', 'elephant', 'modeldb'
    ],
    'distant_neurosci': [
        'carlsim', 'steps', 'lfp-lib', 'psyneulink', 'fastsurfer', 'afni'
    ]
}

print("\n=== RELEVANCE SCORING ===")
print(f"{'Page':<25s} {'Centroid':>8s} {'Purity':>8s} {'Content':>8s} Category")
print("-" * 75)

def wordcount(slug):
    for entry in idx:
        if entry['slug'] == slug:
            if entry['count'] == 0: return 0
    f = None
    for entry in idx:
        if entry['slug'] == slug:
            f = entry['path']
            break
    try:
        with open(f) as fh:
            body = []
            in_fm = False
            for line in fh:
                if line.strip() == '---':
                    in_fm = not in_fm
                    continue
                if not in_fm:
                    body.append(line)
            text = ' '.join(body)
            return len(text.split())
    except:
        return -1

for category, pages in TEST_PAGES.items():
    for slug in sorted(pages):
        if slug == 'networkx' and slug not in page_embs:
            # networkx might exist
            pass
        if slug not in page_embs:
            print(f"{slug:<25s} {'?' :>8s} {'?' :>8s} {wordcount(slug):>8d}  {category}")
        else:
            print(f"{slug:<25s} {centroid_scores[slug]:>8.3f} {purity_scores[slug]:>6.1%} {wordcount(slug):>8d}  {category}")

# Summary stats
print("\n=== DISTRIBUTION ===")
all_cent = list(centroid_scores.values())
all_purity = list(purity_scores.values())
print(f"Centroid  mean={np.mean(all_cent):.3f} std={np.std(all_cent):.3f}")
print(f"Purity    mean={np.mean(all_purity):.3f} std={np.std(all_purity):.3f}")

# Hybrid score = centroid * purity
print("\n=== HYBRID SCORE (centroid * purity) ===")
for cat in ['relevant_tools', 'distant_neurosci', 'irrelevant_software', 'irrelevant_generic']:
    print(f"\n{cat}:")
    for slug in sorted(TEST_PAGES[cat]):
        if slug in page_embs:
            h = centroid_scores[slug] * purity_scores[slug]
            print(f"  {slug:<20s} hybrid={h:.3f}  centroid={centroid_scores[slug]:.3f}  purity={purity_scores[slug]:.1%}")
        else:
            print(f"  {slug:<20s} (no embedding)")
