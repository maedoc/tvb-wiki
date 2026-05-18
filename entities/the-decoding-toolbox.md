---
created: 2025-07-20
sources:
- raw/papers/hebart-2015-decoding-toolbox.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/winkler-2014-palm.md
tags:
- software-brain-modeling
- machine-learning
- neuroimaging-fmri
- paper-methods
title: The Decoding Toolbox
type: entity
updated: '2026-05-18'
---

## Overview

The Decoding Toolbox (TDT) is an open-source MATLAB toolbox for multivariate pattern analysis ([[multivariate-pattern-analysis]]) of [[fmri]] data. Developed by Martin Hebart, Kai Görgen, and John-Dylan Haynes at the Berlin Center for Advanced Neuroimaging, TDT provides a flexible framework for decoding mental states from distributed patterns of [[bold-signal]] activity using supervised learning classifiers such as [[support-vector-machines]]. It supports a broad range of analysis strategies, including volume-based searchlight decoding ([[searchlight-analysis]]), surface-based decoding, region-of-interest (ROI) analysis, and [[representational-similarity-analysis]], making it one of the most versatile decoding packages available for fMRI research.

## Motivation and Context

Conventional mass-univariate fMRI analysis tests each voxel independently for task-related activation, treating the brain's spatial structure as noise. [[multivariate-pattern-analysis]] flips this logic: the distributed pattern of activity across many voxels *is* the signal, encoding information about stimuli, cognitive states, or behavioral variables that may be invisible to a voxel-by-voxel approach. TDT was designed to make this style of analysis accessible and reproducible, offering a unified interface that abstracts away the algorithmic complexity of classification, [[cross-validation]], and permutation testing while remaining transparent enough for methodologists to extend.

Decoding connects naturally to computational models of brain function. A whole-brain model such as [[tvb]] produces simulated [[bold-signal]] time series whose spatiotemporal patterns can be subjected to the same decoding pipelines applied to empirical data. If a model captures the representations that the brain uses to distinguish stimulus categories or cognitive conditions, a classifier should perform similarly on simulated and real data — a form of model validation that goes beyond correlating functional connectivity matrices ([[functional-connectivity]]).

## Core Capabilities

TDT is organized around a modular pipeline: data loading, feature extraction, classifier training, and statistical evaluation. The toolbox ships with a library of [[linear]] and nonlinear classifiers — including linear [[support-vector-machines]], L2-regularized logistic regression, and naive Bayes — and supports both classification and regression targets. For model assessment, TDT automates stratified k-fold [[cross-validation]], leave-one-run-out schemes, and nonparametric permutation tests to derive significance thresholds.

The searchlight module is TDT's most widely used feature. A spherical "searchlight" is centered on every voxel in the brain; at each location a local classification or regression model is trained on the voxels within the sphere, and the resulting accuracy or correlation is written to the center voxel, producing a [[whole-brain]] information map. TDT extends this approach to cortical surface meshes (e.g., [[freesurfer]] reconstructions), supporting vertex-wise analyses that respect cortical folding geometry. For data-format flexibility, TDT accepts preprocessed volumes from [[spm]], [[afni]], FSL, and [[brainvoyager]], lowering the barrier to entry for labs with heterogeneous preprocessing pipelines.

## Relationship to TVB

[[tvb]] simulates neural population dynamics on a structural connectome and generates forward-modeled [[bold-signal]] that can be analyzed with the same tools as empirical fMRI. TDT provides a natural bridge: simulated BOLD from TVB can be fed into TDT's decoding pipeline, and model-derived representational geometries can be compared quantitatively against empirical patterns via [[representational-similarity-analysis]]. This enables a rigorous model-comparison framework — if a [[tvb]] model with a particular neural mass parameterization produces representational dissimilarity matrices that correlate with those derived from [[resting-state]] or [[task-based]] fMRI, the model has captured something structurally meaningful about cortical information processing. Conversely, mismatches between simulated and empirical decoding accuracies can guide model refinement, making TDT a useful tool in the iterative cycle of whole-brain model building and validation.

## Key Features

TDT's design emphasizes scriptability and [[reproducibility]]. All analyses are specified in MATLAB scripts rather than through a graphical user interface, ensuring that every processing step — from [[cross-validation]] folds to classifier hyperparameters — is recorded and executable. The toolbox's open-source license encourages community contributions, and it has been adopted in studies spanning object recognition, working memory, decision-making, and clinical applications in neurology and psychiatry.

## Related Software

* [[tvb]]
* [[representational-similarity-analysis]]
* [[multivariate-pattern-analysis]]

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
3. (authors unknown). *Permutation inference for the general linear model*.