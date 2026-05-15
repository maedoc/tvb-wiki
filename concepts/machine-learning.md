---
created: 2026-05-06
sources:
- raw/papers/arxiv-2512.24901.md
- raw/papers/semanticscholar-301489ffb9de.md
- raw/papers/semanticscholar-25c577d0323b.md
- raw/papers/semanticscholar-6885821c890b.md
tags:
- machine-learning
- artificial-intelligence
- computational-neuroscience
- pattern-recognition
- classification
title: Machine Learning
type: concept
updated: '2026-05-14'
---

# Machine Learning

**Machine learning** refers to computational methods that learn patterns from data without explicit programming. In neuroscience, machine learning is used for [[brain-decoding]], predictive modeling, automated segmentation, and discovering biomarkers from [[neuroimaging]] data.

## Overview

Machine learning encompasses several paradigms:
- **Supervised learning**: Training models on labeled data (e.g., classifying [[fmri]] patterns by task condition)
- **Unsupervised learning**: Discovering structure in unlabeled data (e.g., clustering [[resting-state]] networks)
- **Reinforcement learning**: Learning optimal policies through reward feedback

Key applications in neuroscience:
- Brain decoding and mind reading from fMRI/EEG
- Automated neuroimaging segmentation
- Prediction of clinical outcomes from brain data
- Discovery of disease biomarkers
- [[connectome]] fingerprinting for individual identification

## Relationship to TVB

Machine learning complements TVB in several ways:
- **[[parameter-estimation]]**: ML approaches learn TVB model parameters from empirical data faster than traditional optimization
- **Model classification**: Classifiers distinguish between healthy and pathological [[brain-dynamics]]
- **Feature extraction**: Deep learning extracts relevant features from high-dimensional neuroimaging data for TVB input
- **Validation**: Cross-validated ML predictions validate TVB model outputs against empirical observations
- [[nilearn]] provides standard ML tools for neuroimaging that integrate with TVB workflows
- [[machine-learning]] approaches increasingly inform both spatial [[parcellation]] and temporal dynamics in [[whole-brain]] models
[[sbi]]

## Related Concepts

- [[machine-learning]] — [[neural-network]]-based machine learning
- [[brain-map]] — predicting mental states from brain data
- [[connectomics]] — graph-based analysis of brain networks
- [[dynamic-causal-modeling]] — forecasting brain states from current data

## References

1. Debasis Maji, Arghya Banerjee, Debaditya Barman. *Spectral Graph Neural Networks for Cognitive Task Classification in fMRI Connectomes*. [Link](](https://arxiv.org/abs/2512.24901))
2. Muhammad Nabi Yasinzai, R. Mito, M. Pedersen. (2025). *BrainScape: An open-source framework for integrating and preprocessing anatomical MRI datasets*. Imaging neuroscience. [DOI](](https://doi.org/10.1162/IMAG.a.944))
3. Mai P. Ho, Yang Song, Perminder S. Sachdev, Lei Fan, Jiyang Jiang, Wei Wen. (2026). *A prior-sampling conditional variational autoencoder for neuroimaging normative modelling: Benchmarking deep learning against statistical approaches*. Imaging neuroscience. [DOI](](https://doi.org/10.1162/IMAG.a.1098))

## ORPHAN PAGE CONTEXT (sbi)
---
created: 2024-01-15
sources:
- raw/papers/arxiv-2510.22651.md
- raw/papers/arxiv-2601.22367.md
- raw/papers/arxiv-2506.04558.md
- raw/papers/semanticscholar-8133a79e2e93.md
- raw/papers/arxiv-2505.22685.md
tags:
- parameter-estimation
- machine-learning
- whole-brain-modeling
- variational-bayes
- dynamical-systems-theory
title: Simulation-Based Inference
type: concept
updated: '2026-05-13'
---

# Simulation-Based Inference

## Overview
Simulation-based inference (SBI) denotes a class of Bay