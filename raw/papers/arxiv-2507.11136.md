# Interpretable Bayesian Tensor Network Kernel Machines with Automatic Rank and Feature Selection

**Source**: semantic-scholar
**ID**: 8b2ccb878043aab5c79c4fc4ce19ef289e63c308
**DOI**: 10.48550/arXiv.2507.11136
**URL**: https://www.semanticscholar.org/paper/8b2ccb878043aab5c79c4fc4ce19ef289e63c308
**Date**: 2025-07-15
**Year**: 2025
**Authors**: Afra Kilic, Kim Batselier
**Venue**: arXiv.org
**Citations**: 2

## Abstract

Tensor Network (TN) Kernel Machines speed up model learning by representing parameters as low-rank TNs, reducing computation and memory use. However, most TN-based Kernel methods are deterministic and ignore parameter uncertainty. Further, they require manual tuning of model complexity hyperparameters like tensor rank and feature dimensions, often through trial-and-error or computationally costly methods like cross-validation. We propose Bayesian Tensor Network Kernel Machines, a fully probabilistic framework that uses sparsity-inducing hierarchical priors on TN factors to automatically infer model complexity. This enables automatic inference of tensor rank and feature dimensions, while also identifying the most relevant features for prediction, thereby enhancing model interpretability. All the model parameters and hyperparameters are treated as latent variables with corresponding priors. Given the Bayesian approach and latent variable dependencies, we apply a mean-field variational inference to approximate their posteriors. We show that applying a mean-field approximation to TN factors yields a Bayesian ALS algorithm with the same computational complexity as its deterministic counterpart, enabling uncertainty quantification at no extra computational cost. Experiments on synthetic and real-world datasets demonstrate the superior performance of our model in prediction accuracy, uncertainty quantification, interpretability, and scalability.
