# Function-Space Empirical Bayes Regularisation with Student's t Priors

**Source**: semantic-scholar
**ID**: b0292c084fa5a240753a64c7b10fc38b053dc56c
**DOI**: 10.48550/arXiv.2602.22015
**URL**: https://www.semanticscholar.org/paper/b0292c084fa5a240753a64c7b10fc38b053dc56c
**Date**: 2026-02-25
**Year**: 2026
**Authors**: Pengcheng Hao, E. Kuruoglu
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Bayesian deep learning (BDL) has emerged as a principled approach to produce reliable uncertainty estimates by integrating deep neural networks with Bayesian inference, and the selection of informative prior distributions remains a significant challenge. Various function-space variational inference (FSVI) regularisation methods have been presented, assigning meaningful priors over model predictions. However, these methods typically rely on a Gaussian prior, which fails to capture the heavy-tailed statistical characteristics inherent in neural network outputs. By contrast, this work proposes a novel function-space empirical Bayes regularisation framework -- termed ST-FS-EB -- which employs heavy-tailed Student's $t$ priors in both parameter and function spaces. Also, we approximate the posterior distribution through variational inference (VI), inducing an evidence lower bound (ELBO) objective based on Monte Carlo (MC) dropout. Furthermore, the proposed method is evaluated against various VI-based BDL baselines, and the results demonstrate its robust performance in in-distribution prediction, out-of-distribution (OOD) detection and handling distribution shifts.
