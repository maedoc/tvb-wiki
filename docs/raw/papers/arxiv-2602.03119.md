# Function-Space Empirical Bayes Regularisation with Large Vision-Language Model Priors

**Source**: semantic-scholar
**ID**: f44b224a1c93856c05f04f81ffc4a57c08aa5099
**DOI**: 10.48550/arXiv.2602.03119
**URL**: https://www.semanticscholar.org/paper/f44b224a1c93856c05f04f81ffc4a57c08aa5099
**Date**: 2026-02-03
**Year**: 2026
**Authors**: Pengcheng Hao, Huaze Tang, E. Kuruoglu, Wenbo Ding
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Bayesian deep learning (BDL) provides a principled framework for reliable uncertainty quantification by combining deep neural networks with Bayesian inference. A central challenge in BDL lies in the design of informative prior distributions that scale effectively to high-dimensional data. Recent functional variational inference (VI) approaches address this issue by imposing priors directly in function space; however, most existing methods rely on Gaussian process (GP) priors, whose expressiveness and generalisation capabilities become limited in high-dimensional regimes. In this work, we propose VLM-FS-EB, a novel function-space empirical Bayes regularisation framework, leveraging large vision-language models (VLMs) to generates semantically meaningful context points. These synthetic samples are then used VLMs for embeddings to construct expressive functional priors. Furthermore, the proposed method is evaluated against various baselines, and experimental results demonstrate that our method consistently improves predictive performance and yields more reliable uncertainty estimates, particularly in out-of-distribution (OOD) detection tasks and data-scarce regimes.
