# A Hitchhiker's Guide to Poisson Gradient Estimation

**Source**: semantic-scholar
**ID**: b0dae6999a023450a5e4700c4a354a6c8085a946
**DOI**: 10.48550/arXiv.2602.03896
**URL**: https://www.semanticscholar.org/paper/b0dae6999a023450a5e4700c4a354a6c8085a946
**Date**: 2026-02-03
**Year**: 2026
**Authors**: M. Ibrahim, Han Zhao, Eli Sennesh, Zhi Li, Anqi Wu, Jacob L. Yates, Chengrui Li, Hadi Vafaii
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Poisson-distributed latent variable models are widely used in computational neuroscience, but differentiating through discrete stochastic samples remains challenging. Two approaches address this: Exponential Arrival Time (EAT) simulation and Gumbel-SoftMax (GSM) relaxation. We provide the first systematic comparison of these methods, along with practical guidance for practitioners. Our main technical contribution is a modification to the EAT method that theoretically guarantees an unbiased first moment (exactly matching the firing rate), and reduces second-moment bias. We evaluate these methods on their distributional fidelity, gradient quality, and performance on two tasks: (1) variational autoencoders with Poisson latents, and (2) partially observable generalized linear models, where latent neural connectivity must be inferred from observed spike trains. Across all metrics, our modified EAT method exhibits better overall performance (often comparable to exact gradients), and substantially higher robustness to hyperparameter choices. Together, our results clarify the trade-offs between these methods and offer concrete recommendations for practitioners working with Poisson latent variable models.
