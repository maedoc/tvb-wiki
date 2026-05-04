# A spatially discretized convolutional neural mass model for studying meso-scale spatio-temporal transformations in the rat hippocampus

**Source**: semantic-scholar
**ID**: 3256c88809858146805c676cabffe66b20de51a6
**DOI**: 10.21203/rs.3.rs-9306977/v1
**URL**: https://www.semanticscholar.org/paper/3256c88809858146805c676cabffe66b20de51a6
**Date**: 2026-04-13
**Year**: 2026
**Authors**: Duy Pham, Gene J. Yu, G. Lazzi, Jean-Marie C Bouteiller
**Venue**: Research Square
**Citations**: 0

## Abstract

Abstract The brain operates across multiple spatial and temporal scales, necessitating computationally efficient models that link micro-scale mechanisms to meso- and macro-scale dynamics. Here, we introduce a novel convolutional neural mass model (CNMM) that computes the meso-scale activity of spatially discretized neural populations (''neural masses") in the rat hippocampal CA3 subregion. The CNMM employs a kernel-based architecture, leveraging first-order Volterra expansions with Laguerre (temporal) and Chebyshev (spatial) basis functions to transform input spike densities from entorhinal cortex (EC), dentate gyrus (DG), and neighboring CA3 masses into output CA3 spike density. The model was trained and validated using data from a biophysically detailed large-scale mechanistic model (LSM) simulating exploratory behavior. The CNMM achieved high predictive accuracy for spike density across 32 neural masses spanning the entire extent of CA3 (mean correlation coefficient \(R\) = 0.951) and replicated theta and beta oscillations consistent with experimental findings. When extended for forward modeling, the CNMM accurately predicted local field potentials (LFPs) at a single neural mass (R = 0.952). Kernel analysis revealed topographic gradients in afferent integration, with DG inputs dominating proximally (CA3c) and associational connections distally (CA3a), aligning with anatomical gradients. Compared to the LSM, the CNMM provided a 658-fold speedup in simulation time, 322-fold reduction in memory usage, and 183-fold less disk space for LFP predictions. This framework offers a scalable, efficient approach for meso-scale modeling of neural tissue, bridging detailed simulations with empirical data for insights into normal and pathological function.
