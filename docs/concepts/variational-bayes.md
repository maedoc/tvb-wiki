---
title: "Variational Bayes"
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [dynamic-causal-modeling, parameter-estimation]
sources: [raw/papers/friston-2007.md, raw/papers/beal-2003.md, raw/papers/blei-kucukelbir-mcauliffe-2017.md, raw/papers/wainwright-jordan-2008.md]
---

## Definition
Variational Bayes (VB) is a method for approximate Bayesian inference that transforms integration (computing posteriors) into optimization (finding best approximating distribution). It provides computationally tractable alternatives to MCMC sampling.

## Mathematical Framework

### Evidence Lower Bound (ELBO)
- Log evidence = ELBO + KL divergence
- Maximizing ELBO tightens bound
- Equivalent to minimizing KL divergence

### Mean-Field Approximation
- Factorized posterior: q(θ) = ∏ q(θᵢ)
- Coordinate ascent updates
- Tractable for conjugate models

### Laplace Approximation
- Gaussian approximation around mode
- Used in [[dynamic causal modeling]]
- Requires Hessian computation

## Advantages
- Deterministic optimization (vs random sampling)
- Faster than MCMC for large models
- Scalable to high dimensions
- Natural model comparison (ELBO as evidence bound)

## Applications

### Neuroimaging
- friston-2007 — DCM parameter estimation
- [[dynamic causal modeling]] inference
- Group-level random effects

### Machine Learning
- blei-kucukelbir-mcauliffe-2017 — Modern review
- Variational autoencoders
- Scalable inference

## Related Concepts
- [[dynamic causal modeling]] — Primary application
- [[free energy principle]] — Theoretical connection
- parameter-estimation — General goal

## References
- beal-2003 — Comprehensive treatment
- wainwright-jordan-2008 — Graphical models perspective
- blei-kucukelbir-mcauliffe-2017 — Modern review
