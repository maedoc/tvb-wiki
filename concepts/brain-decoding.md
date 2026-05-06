---
created: 2026-05-06
sources: []
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