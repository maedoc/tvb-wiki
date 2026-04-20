# Sparse covariate-driven factorization of high-dimensional brain connectivity with application to site effect correction

**arXiv ID**: 2601.09525
**Published**: 2026-01-14
**Updated**: 2026-01-14
**Authors**: Rongqian Zhang, Elena Tuzhilina, Jun Young Park
**Categories**: stat.ME, stat.AP, stat.CO
**URL**: https://arxiv.org/abs/2601.09525
**PDF**: https://arxiv.org/pdf/2601.09525
**Source**: arXiv

## Abstract

Large-scale neuroimaging studies often collect data from multiple scanners across different sites, where variations in scanners, scanning procedures, and other conditions across sites can introduce artificial site effects. These effects may bias brain connectivity measures, such as functional connectivity (FC), which quantify functional network organization derived from functional magnetic resonance imaging (fMRI). How to leverage high-dimensional network structures to effectively mitigate site effects has yet to be addressed. In this paper, we propose SLACC (Sparse LAtent Covariate-driven Connectome) factorization, a multivariate method that explicitly parameterizes covariate effects in latent subject scores corresponding to sparse rank-1 latent patterns derived from brain connectivity. The proposed method identifies localized site-driven variability within and across brain networks, enabling targeted correction. We develop a penalized Expectation-Maximization (EM) algorithm for parameter estimation, incorporating the Bayesian Information Criterion (BIC) to guide optimization. Extensive simulations validate SLACC's robustness in recovering the true parameters and underlying connectivity patterns. Applied to the Autism Brain Imaging Data Exchange (ABIDE) dataset, SLACC demonstrates its ability to reduce site effects. The R package to implement our method is publicly available.
