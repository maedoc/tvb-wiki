
---

## 2026-04-28 06:45 — Embedding-Based Relevance Detection Experiment

### Goal
"Can embeddings identify irrelevant pages (e.g. generic Python libraries created by SoftwareMapper)?"

### Method
1. Rebuilt wiki embeddings (291 pages with content chunks).
2. Built TVB centroid from 16 core pages.
3. Computed cosine similarity (centroid score).
4. Computed neighborhood purity (pct of top-30 neighbors also in core).
5. Created hybrid score: centroid x purity.
6. Combined with real word count (excluding template/placeholder text).

### Results

#### Core findings

| Signal | Effect | Reliability |
|--------|--------|-------------|
| **Empty content** | Catches 100% of SoftwareMapper stubs | Very high |
| **Centroid similarity** | Separates core from distant, but noisy | Moderate |
| **Neighborhood purity** | Core pages cluster ~10%, others ~0-3% | Useful |
| **Hybrid score** | Better than centroid alone, still noisy | Moderate |

#### SoftwareMapper pages

All 13+ SoftwareMapper stubs have **2-0 real words** and **no embeddings** (count=0 in index).
They are automatically detectable by content length alone.

#### The embedding approach is NOT a clean automatic classifier

Genuine neuroscience pages flagged by hybrid score: neural-mass-model (0.029), bifurcation-theory (0.025), dynamical-systems-theory (0.027), izhikevich (0.025).
These are legitimate content that simply does not name-drop TVB.

### Recommendation

Do NOT rely on embeddings alone. Use BOTH signals:
1. real_word_count < 20 -> immediate stub flag (catches SoftwareMapper)
2. hybrid_score < 0.03 -> review flag for populated pages
3. Empty stubs -> delete or skip in SoftwareMapper
4. Populated + low hybrid -> human review
5. Populated + high hybrid -> keep

### Tool Added
scripts/check_relevance.py implements the combined filter.

Usage:
python3 scripts/check_relevance.py --flag
python3 scripts/check_relevance.py
