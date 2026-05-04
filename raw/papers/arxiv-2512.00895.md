# A Scalable Variational Bayes Approach for Fitting Non-Conjugate Spatial Generalized Linear Mixed Models via Basis Expansions

**Source**: semantic-scholar
**ID**: 1535a92e5581ae836c7b26e72db8f313333e9265
**URL**: https://www.semanticscholar.org/paper/1535a92e5581ae836c7b26e72db8f313333e9265
**Date**: 2025-11-30
**Year**: 2025
**Authors**: Jin Hyung Lee, Ben Lee
**Citations**: 0

## Abstract

Large spatial datasets with non-Gaussian responses are increasingly common in environmental monitoring, ecology, and remote sensing, yet scalable Bayesian inference for such data remains challenging. Markov chain Monte Carlo (MCMC) methods are often prohibitive for large datasets, and existing variational Bayes methods rely on conjugacy or strong approximations that limit their applicability and can underestimate posterior variances. We propose a scalable variational framework that incorporates semi-implicit variational inference (SIVI) with basis representations of spatial generalized linear mixed models (SGLMMs), which may not have conjugacy. Our approach accommodates gamma, negative binomial, Poisson, Bernoulli, and Gaussian responses on continuous spatial domains. Across 20 simulation scenarios with 50,000 locations, SIVI achieves predictive accuracy and posterior distributions comparable to Metropolis-Hastings and Hamiltonian Monte Carlo while providing notable computational speedups. Applications to MODIS land surface temperature and Blue Jay abundance further demonstrate the utility of the approach for large non-Gaussian spatial datasets.
