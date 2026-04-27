# Classification of Epileptic iEEG using Topological Machine Learning

**Source**: arxiv
**ID**: 2604.11971
**URL**: https://arxiv.org/abs/2604.11971
**Date**: 2026-04-13
**Year**: 2026
**Authors**: Sunia Tanweer, Narayan Puthanmadam Subramaniyam, Firas A. Khasawneh
**Categories**: cs.LG, stat.AP

## Abstract

Epileptic seizure detection from EEG signals remains challenging due to the high dimensionality and nonlinear, potentially stochastic, dynamics of neural activity. In this work, we investigate whether features derived from topological data analysis (TDA) can improve the classification of brain states in preictal, ictal and interictal iEEG recordings from epilepsy patients using multichannel data. We analyze data from 55 patients, significantly larger than many previous studies that rely on patient-specific models. Persistence diagrams derived from iEEG signals are vectorized using several TDA representations, including Carlsson coordinates, persistence images, and template functions. To understand how topological representations interact with modern machine learning pipelines, we conduct a large-scale ablation study across multiple iEEG frequency bands, dimensionality reduction techniques, feature representations, and classifier architectures. Our experiments show that dimension-reduced topological representations achieve up to 80\% balanced accuracy for three-class classification. Interestingly, classical machine learning models perform comparably to deep learning models, achieving up to 79.17\% balanced accuracy, suggesting that carefully designed topological features can substantially reduce model complexity requirements. In contrast, pipelines preserving the full multichannel feature structure exhibit severe overfitting due to the high-dimensional feature space. These findings highlight the importance of structure-preserving dimensionality reduction when applying topology-based representations to multichannel neural data.
