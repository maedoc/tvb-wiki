# uBrainSurf: Unified Curvature-aware Deformation Framework for Lifespan Brain Cortical Surface Reconstruction.

**Source**: semantic-scholar
**ID**: 0f134e817e53f48ed927abe2a88e9a35ae751e03
**DOI**: 10.1109/TMI.2026.3672432
**URL**: https://www.semanticscholar.org/paper/0f134e817e53f48ed927abe2a88e9a35ae751e03
**Date**: 2026-03-10
**Year**: 2026
**Authors**: Lin Teng, Shen Zhao, Jiadong Zhang, Feng Shi, Dinggang Shen
**Venue**: IEEE Transactions on Medical Imaging
**Citations**: 0

## Abstract

Accurate and automated reconstruction of cortical surfaces across the human lifespan is essential for studying brain development, aging, and the early diagnosis of neurological disorders. However, traditional neuroimaging pipelines require hours per subject, limiting scalability. Existing deep learning methods typically target narrow age ranges, struggling to generalize due to substantial age-related anatomical variability. This leads to inaccurate quantification of cortical properties, such as curvature and cortical thickness, thereby undermining their potential as reliable biomarkers for routine clinical brain analysis. To address these challenges, we present uBrainSurf, a unified curvature-aware deformation framework for lifespan cortical surface reconstruction. Specifically, uBrainSurf learns a sequence of stationary velocity fields (SVFs) from volumetric MR images, gradually deforming a smooth template mesh to subject-specific white-matter and pial surfaces through a coarse-to-fine strategy. To enhance the reconstruction accuracy, we introduce an auxiliary curvature prediction branch that provides an anatomical prior, guiding the model to prioritize anatomically important regions. Furthermore, we propose a novel curvature-driven loss function that encourages consistency between the curvatures of corresponding points on predicted and target surfaces, ensuring the reconstructed surfaces are directly suitable for downstream analyses. The uBrainSurf is evaluated on a large-scale brain dataset comprising 2,132 subjects spanning 0-100 years. Experimental results demonstrate that uBrainSurf achieves superior performance and generalizability while being several orders of magnitude faster than traditional pipelines. Our code is available at https://github.com/TL9792/CCF.
