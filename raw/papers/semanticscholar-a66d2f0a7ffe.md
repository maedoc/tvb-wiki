# MV-ComBat and MV-CovBat: Multivariate Frameworks for Joint Harmonization of Multi-Metric Neuroimaging Data

**Source**: semantic-scholar
**ID**: a66d2f0a7ffe2ffb75d8a329aebd9a42bcbec861
**DOI**: 10.64898/2026.02.05.704069
**URL**: https://www.semanticscholar.org/paper/a66d2f0a7ffe2ffb75d8a329aebd9a42bcbec861
**Date**: 2026-02-09
**Year**: 2026
**Authors**: Zheng Ren, Patrick S. Sadil, Martin A. Lindquist
**Venue**: bioRxiv
**Citations**: 0

## Abstract

Aggregating neuroimaging data across sites and studies is increasingly common, yet site- and scanner-related batch effects can obscure meaningful biological variation and introduce spurious associations. Although ComBat and its extensions are widely used, they are primarily designed for single-metric (univariate) harmonization. In practice, neuroimaging studies often involve multiple biologically coupled metrics (e.g., cortical thickness, surface area, and gray-matter volume) measured across multiple features (e.g., regional values), with shared covariance structure both within and across metrics. Applying univariate ComBat independently to each metric ignores these dependencies and can leave residual batch effects in cross-metric covariance. Using data from the NIH Acute to Chronic Pain Signatures (A2CPS) program, we show that batch effects occur not only in means and variances but also in covariance across cortical regions and metrics—relationships that univariate ComBat does not fully remove. We propose MV-ComBat, a multivariate extension of ComBat that jointly harmonizes multiple metrics by borrowing strength across them. Both empirical Bayes (EB) and Bayesian Markov Chain Monte Carlo (MCMC) implementations of MV-ComBat effectively reduce batch effects. In our experiments, EB is more robust to measurement error, whereas MCMC more accurately recovers cross-metric correlations when priors are well specified. Recognizing that batch effects can also affect feature-level covariance, CovBat was recently introduced as an extension of ComBat that harmonizes both first- and second-order moments across sites. We extend CovBat to the multivariate framework as MV-CovBat, which performs a second-stage latent-space harmonization to address covariance-related batch effects across features and metrics. Simulations confirm that MV-ComBat improves correlation recovery and biological signal preservation relative to univariate ComBat, particularly for moderate-to-strong effects, and that MV-CovBat further improves separation of true biological variation from batch effects when independence assumptions are violated. Together, these methods provide a flexible and unified framework for harmonizing complex, multi-metric neuroimaging data in large-scale, multi-site studies.
