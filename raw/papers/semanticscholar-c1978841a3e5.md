# Forward-projected cortical eigenmodes provide an efficient sensor-space representation of resting-state EEG

**Source**: semantic-scholar
**ID**: c1978841a3e502a840b64b014d1954c9dbffa6dc
**DOI**: 10.64898/2025.12.08.693061
**URL**: https://www.semanticscholar.org/paper/c1978841a3e502a840b64b014d1954c9dbffa6dc
**Date**: 2025-12-10
**Year**: 2025
**Authors**: Hyung G. Park
**Venue**: bioRxiv
**Citations**: 0

## Abstract

Sensor-space EEG analyses typically rely on electrode layouts or data-driven components and rarely encode cortical geometry, making scalp patterns difficult to link to anatomy and to compare across participants. We introduce a sensor-space basis dictionary that explicitly integrates cortical geometry. Laplace–Beltrami (LB) eigenmodes are computed on a standard cortical template (fsaverage) and mapped by the lead-field matrix of a three-layer boundary-element (BEM) head model to yield cortex-anchored sensor-space harmonics. The leadfield-mapped LB dictionary spans scalp topographies, while pre-serving a meaningful spatial-frequency ordering inherited from the cortical manifold. We assess representational efficiency using ordinary least squares (OLS) projections of resting EEG (eyes-closed/open) across 59-, 32-, and 19-channel montages, and compare against spherical harmonics (SPH), principal components (PCA), and independent components (ICA). Efficiency is quantified by the variance explained R2(K) (by leading K modes) and the efficiency indices K70 and K90 (fewest modes reaching R2 ≥ 0.70 and 0.90) and reliability by ICC(3,1) of eyes-open/closed coefficients. The cortex-anchored basis shows higher early-K R2 than SPH and PCA (e.g., 59-channel eyes-closed at K=4: LB R2 ≈ 0.56 [95% CI: 0.54, 0.59] vs. SPH ≈ 0.44 [0.42, 0.46], PCA ≈ 0.08 [0.07, 0.09]) and reaches 70% and 90% variance with fewer modes (LB K70 ≈ 8.6; SPH ≈ 12.3; PCA ≈ 19.3; ICA ≈ 22.8; LB K90 ≈ 22.6; SPH ≈ 25.3; PCA ≈ 23.2; ICA ≈ 30.2). Mode-wise coefficient reliability (eyes-open vs. eyes-closed) is comparable between LB and SPH. By combining cortical eigenmodes with a forward head model, this approach yields a geometry-aligned, interpretable representation of sensor-space EEG that offers superior fidelity-complexity trade-offs at small K and a principled scaffold for low-dimensional EEG sensor space analysis.
