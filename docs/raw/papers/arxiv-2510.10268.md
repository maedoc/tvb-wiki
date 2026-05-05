# Neural variational inference for cutting feedback during uncertainty propagation

**Source**: semantic-scholar
**ID**: d6ab08dc92733a4cb71ff8c91f4ba71767d52417
**DOI**: 10.48550/arXiv.2510.10268
**URL**: https://www.semanticscholar.org/paper/d6ab08dc92733a4cb71ff8c91f4ba71767d52417
**Date**: 2025-10-11
**Year**: 2025
**Authors**: Jiafang Song, Sandipan Pramanik, Abhirup Datta
**Venue**: arXiv.org
**Citations**: 1

## Abstract

In many scientific applications, uncertainty of estimates from an earlier (upstream) analysis needs to be propagated in subsequent (downstream) Bayesian analysis, without feedback. Cutting feedback methods, also termed cut-Bayes, achieve this by constructing a cut-posterior distribution that prevents backward information flow. Cutting feedback like nested MCMC is computationally challenging while variational inference (VI) cut-Bayes methods need two variational approximations and require access to the upstream data and model. In this manuscript we propose, NeVI-Cut, a provably accurate and modular neural network-based variational inference method for cutting feedback. We directly utilize samples from the upstream analysis without requiring access to the upstream data or model. This simultaneously preserves modularity of analysis and reduces approximation errors by avoiding a variational approximation for the upstream model. We then use normalizing flows to specify the conditional variational family for the downstream parameters and estimate the conditional cut-posterior as a variational solution of Monte Carlo average loss over all the upstream samples. We provide theoretical guarantees on the NeVI-Cut estimate to approximate any cut-posterior. Our results are in a fixed-data regime and provide convergence rates of the actual variational solution, quantifying how richness of the neural architecture and the complexity of the target cut-posterior dictate the approximation quality. In the process, we establish new results on uniform Kullback-Leibler approximation rates of conditional normalizing flows. Simulation studies and two real-world analyses illustrate how NeVI-Cut achieves significant computational gains over traditional cutting feedback methods and is considerably more accurate than parametric variational cut approaches.
