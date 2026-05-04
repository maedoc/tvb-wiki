# SIMBA: Scalable Image Modeling using a Bayesian Approach, A Consistent Framework for Including Spatial Dependencies in fMRI Studies

**Source**: semantic-scholar
**ID**: dc7ba77017bb9e90de4ea96bf586dfba0dae40ab
**URL**: https://www.semanticscholar.org/paper/dc7ba77017bb9e90de4ea96bf586dfba0dae40ab
**Date**: 2025-11-16
**Year**: 2025
**Authors**: Yuan Zhong, Gang Chen, Paul A. Taylor, Jian Kang
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Bayesian spatial modeling provides a flexible framework for whole-brain fMRI analysis by explicitly incorporating spatial dependencies, overcoming the limitations of traditional massive univariate approaches that lead to information waste. In this work, we introduce SIMBA, a Scalable Image Modeling using a Bayesian Approach, for group-level fMRI analysis, which places Gaussian process (GP) priors on spatially varying functions to capture smooth and interpretable spatial association patterns across the brain volume. To address the significant computational challenges of GP inference in high-dimensional neuroimaging data, we employ a low-rank kernel approximation that enables projection into a reduced-dimensional subspace. This allows for efficient posterior computation without sacrificing spatial resolution, and we have developed efficient algorithms for this implemented in Python that achieve fully Bayesian inference either within minutes using the Gibbs sampler or within seconds using mean-field variational inference (VI). Through extensive simulation studies, we first show that SIMBA outperforms competing methods in estimation accuracy, activation detection sensitivity, and uncertainty quantification, especially in low signal-to-noise settings. We further demonstrate the scalability and interpretability of SIMBA in large-scale task-based fMRI applications, analyzing both volumetric and cortical surface data from the NARPS and ABCD studies.
