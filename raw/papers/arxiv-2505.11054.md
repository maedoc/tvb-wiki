# NeuralSurv: Deep Survival Analysis with Bayesian Uncertainty Quantification

**Source**: semantic-scholar
**ID**: 6c14fe2308ecbd850141f9cdbd4e70b30f57e74a
**DOI**: 10.48550/arXiv.2505.11054
**URL**: https://www.semanticscholar.org/paper/6c14fe2308ecbd850141f9cdbd4e70b30f57e74a
**Date**: 2025-05-16
**Year**: 2025
**Authors**: M'elodie Monod, Alessandro Micheli, Samir Bhatt
**Venue**: arXiv.org
**Citations**: 2

## Abstract

We introduce NeuralSurv, the first deep survival model to incorporate Bayesian uncertainty quantification. Our non-parametric, architecture-agnostic framework captures time-varying covariate-risk relationships in continuous time via a novel two-stage data-augmentation scheme, for which we establish theoretical guarantees. For efficient posterior inference, we introduce a mean-field variational algorithm with coordinate-ascent updates that scale linearly in model size. By locally linearizing the Bayesian neural network, we obtain full conjugacy and derive all coordinate updates in closed form. In experiments, NeuralSurv delivers superior calibration compared to state-of-the-art deep survival models, while matching or exceeding their discriminative performance across both synthetic benchmarks and real-world datasets. Our results demonstrate the value of Bayesian principles in data-scarce regimes by enhancing model calibration and providing robust, well-calibrated uncertainty estimates for the survival function.
