# Excessive data censoring in fMRI undermines individual precision and weakens brain-behavior associations

**Source**: arxiv
**ID**: 2603.07380
**URL**: https://arxiv.org/abs/2603.07380
**Date**: 2026-03-07
**Year**: 2026
**Authors**: Amanda Mejia, Joanne Hwang, Damon Pham, Stephanie Noble, Theodore D. Satterthwaite, Thomas E. Nichols, B. T. Thomas Yeo
**Categories**: stat.AP

## Abstract

Censoring high-motion volumes in fMRI is common practice to reduce effects of head motion on functional connectivity (FC). Although aggressive censoring removes more noise, it causes extensive data loss, creating a tradeoff that may ultimately improve or degrade FC accuracy. Here, we evaluate how censoring affects FC estimation and downstream brain-wide association studies (BWAS). Using extensively sampled participants from the Human Connectome Project (HCP) Retest dataset, we establish individual "ground truth" FC and assess the accuracy of FC estimated from 5-30 minute scans. We find that censoring degrades FC accuracy, with more aggressive censoring being more detrimental, particularly among participants exhibiting above-average motion. In these participants, aggressive censoring reduces FC accuracy by 30% for 30-minute scans denoised with ICA-FIX, an advanced denoising method, and by 3% for scans denoised with conventional confound regression. These effects reflect substantial data loss (34%) that outweighs comparatively modest noise reductions: 7% with ICA-FIX and 18% with confound regression. Compensating for this would require substantially longer scans (62% with confound regression; 76% with ICA-FIX), inflating data collection budgets. Introducing a repeated measures framework to separate motion trait from artifact, we find that standard QC metrics are dominated by motion trait and overstate motion bias, which is effectively mitigated with less aggressive censoring. Finally, using data from nearly 1,000 HCP participants, we demonstrate that unreliable FC substantially attenuates BWAS correlations: by ~30% under optimal conditions (longer ICA-FIX scans with no censoring) but exceeding 75% in short, aggressively censored scans. Our findings support the use of advanced denoising methods, limiting censoring, and collecting longer scans to maximize fidelity of FC and BWAS.
