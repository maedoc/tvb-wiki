# High-Dimensional Bayesian Model Comparison in Cosmology with GPU-accelerated Nested Sampling and Neural Emulators

**Source**: semantic-scholar
**ID**: ab1d9e59494bdd186ff2cd353d37026e5188f348
**URL**: https://www.semanticscholar.org/paper/ab1d9e59494bdd186ff2cd353d37026e5188f348
**Date**: 2025-09-16
**Year**: 2025
**Authors**: Toby Lovick, D. Yallup, Davide Piras, A. S. Mancini, W. Handley
**Citations**: 5

## Abstract

We demonstrate a GPU-accelerated nested sampling framework for efficient high-dimensional Bayesian inference in cosmology. Using JAX-based neural emulators and likelihoods for cosmic microwave background and cosmic shear analyses, our approach provides parameter constraints and direct calculation of Bayesian evidence. In the 39-dimensional $\Lambda$CDM vs $w_0w_a$ shear analysis, we produce Bayes factors and a robust error bar in just 2 days on a single A100 GPU, without loss of accuracy. Where CPU-based nested sampling can now be outpaced by methods relying on MCMC sampling and decoupled evidence estimation, we demonstrate that with GPU acceleration nested sampling offers the necessary speed-up to put it on equal computational footing with these methods, especially where reliable model comparison is paramount. We also explore interpolation in the matter power spectrum for cosmic shear analysis, finding a further factor of 4 speed-up with consistent posterior contours and Bayes factor. We put forward both nested and gradient-based sampling as useful tools for the modern cosmologist, where cutting-edge inference pipelines can yield orders of magnitude improvements in computation time.
