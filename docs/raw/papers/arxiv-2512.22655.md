# Bend to Mend: Toward Trustworthy Variational Bayes with Valid Uncertainty Quantification

**arXiv ID**: 2512.22655
**Published**: 2025-12-27
**Updated**: 2025-12-27
**Authors**: Jiaming Liu, Meng Li
**Categories**: stat.ME
**URL**: https://arxiv.org/abs/2512.22655
**PDF**: https://arxiv.org/pdf/2512.22655
**Source**: arXiv

## Abstract

Variational Bayes (VB) is a popular and computationally efficient method to approximate the posterior distribution in Bayesian inference, especially when the exact posterior is analytically intractable and sampling-based approaches are computationally prohibitive. While VB often yields accurate point estimates, its uncertainty quantification (UQ) is known to be unreliable. For example, credible intervals derived from VB posteriors tend to exhibit undercoverage, failing to achieve nominal frequentist coverage probabilities. In this article, we address this challenge by proposing Trustworthy Variational Bayes (TVB), a method to recalibrate the UQ of broad classes of VB procedures. Our approach follows a bend-to-mend strategy: we intentionally misspecify the likelihood to correct VB's flawed UQ. In particular, we first relax VB by building on a recent fractional VB method, and then identify the optimal fraction parameter using conformal techniques such as sample splitting and bootstrapping. This yields recalibrated UQ for any given parameter of interest. On the theoretical front, we establish that the calibrated credible intervals achieve asymptotically correct frequentist coverage for a given parameter of interest; this, to the best of our knowledge, is the first such theoretical guarantee for VB. On the practical front, we introduce the "TVB table", which enables (1) massive parallelization and remains agnostic to the parameter of interest during its construction, and (2) efficient identification of the optimal fraction parameter for any specified parameter of interest. The proposed method is illustrated via Gaussian mixture models and Bayesian mixture linear regression models, and numerical experiments demonstrate that the TVB method outperforms standard VB and achieves normal frequentist coverage in finite samples. A real data application is also discussed.
