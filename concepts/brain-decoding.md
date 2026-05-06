---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-a225a1c661a7.md
- raw/papers/semanticscholar-c92bc1391211.md
- raw/papers/arxiv-2512.24901.md
- raw/papers/semanticscholar-b0ceb704952b.md
- raw/papers/glean-github.md
tags:
- brain-decoding
- machine-learning
- neuroimaging-fmri
- classification
- eeg
title: Brain Decoding
type: concept
updated: '2026-05-06'
---

# Brain Decoding

**Brain decoding** (or "mind reading") refers to the process of predicting mental states, stimuli, or cognitive variables from brain activity patterns, typically using [[machine-learning]] methods.

## Overview

Common decoding approaches include:
- **Multivariate Pattern Analysis (MVPA)**: Classifying distributed patterns of brain activity
- **Searchlight decoding**: Running classifiers in sliding spatial windows
- **Representational Similarity Analysis (RSA)**: Comparing representational geometries between brain and models
- **Encoding models**: Predicting brain activity from stimulus features
- **Decoding models**: Predicting stimulus features from brain activity

## Relationship to TVB

Brain decoding validates TVB models by bridging simulation and empirical data:
- TVB generates simulated [[bold-signal|BOLD]] or EEG/MEG patterns that can be decoded
- If TVB captures the right neural mechanisms, its simulated patterns should be decodable in the same ways as empirical data
- Decoding accuracy from TVB-simulated data can discriminate between competing models
- TVB parameters can be optimized to maximize alignment between simulated and empirically decoded patterns

## Related

- [[machine-learning]] — algorithms and methods for brain decoding
- [[bayesian]] — probabilistic frameworks for decoding
- [[nilearn]] — Python library for [[neuroimaging]] machine learning

## References

1. Yunfei Wang, Yanming Wang, Bensheng Qiu, Xiaoxiao Wang. (2026). *Few-Shot Transfer Learning for Cross-Subject Visual Brain Decoding via [[whole-brain]] Functional Magnetic Resonance Imaging*. 2026 6th International Conference on Neural Networks, Information and Communication Engineering (NNICE). [DOI](https://doi.org/10.1109/NNICE68970.2026.11466215)
2. P. Pawar, Nilima Kulkarni. (2025). *NeuroClean: A Benchmarking and Optimization Framework for EEG Preprocessing in Semantic Brain-to-Text Decoding*. 2025 3rd International Conference on Computational Intelligence and Network Systems (CINS). [DOI](https://doi.org/10.1109/CINS67018.2025.11412037)
3. Debasis Maji, Arghya Banerjee, Debaditya Barman. *Spectral Graph Neural Networks for Cognitive Task Classification in [[fmri]] Connectomes*. [Link](https://arxiv.org/abs/2512.24901)