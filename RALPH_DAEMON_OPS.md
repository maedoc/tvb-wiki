
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


---

## 2026-04-28 07:00 — Combined Filter: Graph Distance + Embeddings

### Goal
"Can we avoid false negatives on relevant pages that exist as content but are not yet linked from the TVB core pages?"

### What failed
Embedding-only hybrid score wrongly flagged neural-mass-model, bifurcation-theory, dynamical-systems-theory as low-relevance. But these are foundational TVB concepts.

### Why it failed
Neural-mass-model contains dense math (mean-field theory, differential equations) with TVB links. The embedding centroid was built from mostly descriptive/software pages, while its language is formal math — semantically different even though topically central.

### Graph distance tells the truth

- neural-mass-model: in-degree 52, graph dist 0 (in core!) → correctly accepted
- bifurcation-theory: in-degree 10, graph dist 1 → correctly accepted
- dynamical-systems-theory: in-degree 25, graph dist 1 → correctly accepted
- pandas/matplotlib: 2 real words, graph dist ∞ → correctly stubbed

### Combined decision logic

```
if real_word_count < 20:
    verdict = "stub"
elif graph_distance <= 3:
    verdict = "accept"
elif graph_distance == 999 and hybrid_score >= 0.03:
    verdict = "accept"      # orphan but semantically relevant
elif graph_distance == 999 and hybrid_score < 0.03:
    verdict = "reject"      # unreachable + semantically distant
else:
    verdict = "review"
```

### Results

- accept: 269  (core + linked neuroscience + plausible orphans)
- stub: 247    (empty pages; most SoftwareMapper stubs)
- reject: 10   (unlinked biographical stubs + distant tools)
- review: 0    (no ambiguous cases)

### Tool Added
scripts/combined_relevance.py

### Key Lesson
Use graph distance as PRIMARY signal, embeddings as SECONDARY backup for orphan detection. Never use embeddings alone.
