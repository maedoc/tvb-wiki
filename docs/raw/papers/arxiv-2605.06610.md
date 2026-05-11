# SoftSAE: Dynamic Top-K Selection for Adaptive Sparse Autoencoders

**Source**: arxiv
**ID**: 2605.06610
**URL**: https://arxiv.org/abs/2605.06610
**Date**: 2026-05-07
**Year**: 2026
**Authors**: Jakub Stępień, Marcin Mazur, Jacek Tabor, Przemysław Spurek
**Categories**: cs.LG, cs.CV

## Abstract

Sparse Autoencoders (SAEs) have become an important tool in mechanistic interpretability, helping to analyze internal representations in both Large Language Models (LLMs) and Vision Transformers (ViTs). By decomposing polysemantic activations into sparse sets of monosemantic features, SAEs aim to translate neural network computations into human-understandable concepts. However, common architectures such as TopK SAEs rely on a fixed sparsity level. They enforce the same number of active features (K) across all inputs, ignoring the varying complexity of real-world data. Natural data often lies on manifolds with varying local intrinsic dimensionality, meaning the number of relevant factors can change significantly across samples. This suggests that a fixed sparsity level is not optimal. Simple inputs may require only a few features, while more complex ones need more expressive representations. Using a constant K can therefore introduce noise in simple cases or miss important structure in more complex ones. To address this issue, we propose SoftSAE, a sparse autoencoder with a Dynamic Top-K selection mechanism. Our method uses a differentiable Soft Top-K operator to learn an input-dependent sparsity level k. This allows the model to adjust the number of active features based on the complexity of each input. As a result, the representation better matches the structure of the data, and the explanation length reflects the amount of information in the input. Experimental results confirm that SoftSAE not only finds meaningful features, but also selects the right number of features for each concept. The source code is available at: https://anonymous.4open.science/r/SoftSAE-8F71/.
