# Deep unfolding of MCMC kernels: scalable, modular & explainable GANs for high-dimensional posterior sampling

**Source**: semantic-scholar
**ID**: 5d454eb1c46828c6dc4a0f834771a289a5705edb
**DOI**: 10.48550/arXiv.2602.20758
**URL**: https://www.semanticscholar.org/paper/5d454eb1c46828c6dc4a0f834771a289a5705edb
**Date**: 2026-02-24
**Year**: 2026
**Authors**: Jonathan Spence, T. Liaudat, Konstantinos Zygalakis, M. Pereyra
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Markov chain Monte Carlo (MCMC) methods are fundamental to Bayesian computation, but can be computationally intensive, especially in high-dimensional settings. Push-forward generative models, such as generative adversarial networks (GANs), variational auto-encoders and normalising flows offer a computationally efficient alternative for posterior sampling. However, push-forward models are opaque as they lack the modularity of Bayes Theorem, leading to poor generalisation with respect to changes in the likelihood function. In this work, we introduce a novel approach to GAN architecture design by applying deep unfolding to Langevin MCMC algorithms. This paradigm maps fixed-step iterative algorithms onto modular neural networks, yielding architectures that are both flexible and amenable to interpretation. Crucially, our design allows key model parameters to be specified at inference time, offering robustness to changes in the likelihood parameters. We train these unfolded samplers end-to-end using a supervised regularized Wasserstein GAN framework for posterior sampling. Through extensive Bayesian imaging experiments, we demonstrate that our proposed approach achieves high sampling accuracy and excellent computational efficiency, while retaining the physics consistency, adaptability and interpretability of classical MCMC strategies.
