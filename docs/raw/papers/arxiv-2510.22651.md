# Variational Polya Tree

**Source**: semantic-scholar
**ID**: 3b46dd2a35b555a3df3776070843b944a543c9f8
**DOI**: 10.48550/arXiv.2510.22651
**URL**: https://www.semanticscholar.org/paper/3b46dd2a35b555a3df3776070843b944a543c9f8
**Date**: 2025-10-26
**Year**: 2025
**Authors**: Lu Xu, Tsai Hor Chan, Kwok Fai Lam, Lequan Yu, Guosheng Yin
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Density estimation is essential for generative modeling, particularly with the rise of modern neural networks. While existing methods capture complex data distributions, they often lack interpretability and uncertainty quantification. Bayesian nonparametric methods, especially the \polya tree, offer a robust framework that addresses these issues by accurately capturing function behavior over small intervals. Traditional techniques like Markov chain Monte Carlo (MCMC) face high computational complexity and scalability limitations, hindering the use of Bayesian nonparametric methods in deep learning. To tackle this, we introduce the variational \polya tree (VPT) model, which employs stochastic variational inference to compute posterior distributions. This model provides a flexible, nonparametric Bayesian prior that captures latent densities and works well with stochastic gradient optimization. We also leverage the joint distribution likelihood for a more precise variational posterior approximation than traditional mean-field methods. We evaluate the model performance on both real data and images, and demonstrate its competitiveness with other state-of-the-art deep density estimation methods. We also explore its ability in enhancing interpretability and uncertainty quantification. Code is available at https://github.com/howardchanth/var-polya-tree.
