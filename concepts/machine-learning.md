---
title: "Machine Learning"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [machine-learning, artificial-intelligence, computational-neuroscience, pattern-recognition, classification]
sources: []
---

# Machine Learning

**Machine learning** refers to computational methods that learn patterns from data without explicit programming. In neuroscience, machine learning is used for brain decoding, predictive modeling, automated segmentation, and discovering biomarkers from neuroimaging data.

## Overview

Machine learning encompasses several paradigments:
- **Supervised learning**: Training models on labeled data (e.g., classifying fMRI patterns by task condition)
- **Unsupervised learning**: Discovering structure in unlabeled data (e.g., clustering resting-state networks)
- **Reinforcement learning**: Learning optimal policies through reward feedback

Key applications in neuroscience:
- Brain decoding and mind reading from fMRI/EEG
- Automated neuroimaging segmentation
- Prediction of clinical outcomes from brain data
- Discovery of disease biomarkers
- Connectome fingerprinting for individual identification

## Relationship to TVB

Machine learning complements TVB in several ways:
- **Parameter estimation**: ML approaches learn TVB model parameters from empirical data faster than traditional optimization
- **Model classification**: Classifiers distinguish between healthy and pathological brain dynamics
- **Feature extraction**: Deep learning extracts relevant features from high-dimensional neuroimaging data for TVB input
- **Validation**: Cross-validated ML predictions validate TVB model outputs against empirical observations
- [[nilearn]] provides standard ML tools for neuroimaging that integrate with TVB workflows
- [[deep-learning]] approaches increasingly inform both spatial parcellation and temporal dynamics in whole-brain models

## Related Concepts

- [[deep-learning]] — neural network-based machine learning
- [[brain-decoding]] — predicting mental states from brain data
- [[connectomics]] — graph-based analysis of brain networks
- [[predictive-modeling]] — forecasting brain states from current data
