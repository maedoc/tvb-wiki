# Fast Variational Bayes for Large Spatial Data

**Source**: semantic-scholar
**ID**: cf411c0c3ddd70aaef0e5a777b87b4a6ae72cdb7
**URL**: https://www.semanticscholar.org/paper/cf411c0c3ddd70aaef0e5a777b87b4a6ae72cdb7
**Date**: 2025-07-16
**Year**: 2025
**Authors**: Jiafang Song, Abhirup Datta
**Citations**: 2

## Abstract

Recent variational Bayes methods for geospatial regression, proposed as an alternative to computationally expensive Markov chain Monte Carlo (MCMC) sampling, have leveraged Nearest Neighbor Gaussian processes (NNGP) to achieve scalability. Yet, these variational methods remain inferior in accuracy and speed compared to spNNGP, the state-of-the-art MCMC-based software for NNGP. We introduce spVarBayes, a suite of fast variational Bayesian approaches for large-scale geospatial data analysis using NNGP. Our contributions are primarily computational. We replace auto-differentiation with a combination of calculus of variations, closed-form gradient updates, and linear response corrections for improved variance estimation. We also accommodate covariates (fixed effects) in the model and offer inference on the variance parameters. Simulation experiments demonstrate that we achieve comparable accuracy to spNNGP but with reduced computational costs, and considerably outperform existing variational inference methods in terms of both accuracy and speed. Analysis of a large forest canopy height dataset illustrates the practical implementation of proposed methods and shows that the inference results are consistent with those obtained from the MCMC approach. The proposed methods are implemented in publicly available Github R-package spVarBayes.
