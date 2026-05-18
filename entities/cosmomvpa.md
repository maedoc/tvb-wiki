---
created: 2026-05-13
sources:
- raw/papers/woodman-2014.md
- raw/papers/semanticscholar-db98f2ae6803.md
- raw/papers/arxiv-2507.09747.md
tags:
- software-brain-modeling
- machine-learning
- brain-decoding
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- classification
- representational-similarity-analysis
title: CoSMoMVPA
type: entity
updated: '2026-05-18'
---

# CoSMoMVPA

## Overview

CoSMoMVPA (Connectome-based Similarity — Multi-Variate Pattern Analysis) is an open-source MATLAB and GNU Octave toolbox for multivariate pattern analysis of [[neuroimaging]] data. Developed by Nikolaas N. Oosterhof and colleagues, it provides a unified framework for applying [[machine-learning]] classifiers to [[fmri]], [[eeg]], and [[meg]] data, with particular strengths in searchlight analysis and representational similarity analysis. The toolbox bridges the gap between whole-brain [[brain-decoding]] and [[connectomics]] by emphasizing spatially structured, connectivity-informed approaches to pattern discrimination.

## Motivation and Context

Multivariate pattern analysis emerged as a response to the limitations of classical mass-univariate general linear model approaches in [[neuroimaging-fmri]]. While univariate methods test each voxel independently for task-related activation, MVPA recognizes that cognitive states are encoded in distributed patterns of neural activity spanning multiple brain regions. CoSMoMVPA was designed to make these techniques accessible to researchers working in the MATLAB ecosystem, complementing the Python-based [[pymvpa]] toolbox. By building on top of widely used neuroimaging platforms such as [[spm]] and [[afni]], CoSMoMVPA allows researchers to integrate MVPA into existing preprocessing pipelines without switching software environments or programming languages.

The toolbox is particularly notable for its emphasis on statistical rigor. All classification results are evaluated through non-parametric permutation testing, where the null distribution of classification accuracy is estimated by repeatedly shuffling condition labels and recomputing accuracy. This approach avoids parametric assumptions about the distribution of accuracy scores and provides valid inference even for small sample sizes, a common concern in clinical and cognitive neuroscience studies.

## Key Features

CoSMoMVPA implements three complementary spatial scales of multivariate analysis. At the finest grain, **searchlight analysis** slides a spherical kernel across the brain, training and testing a classifier on the voxels within each sphere to produce a [[whole-brain]] map of local information content. This technique, introduced by Kriegeskorte, Goebel, and Bandettini (2006), reveals which brain regions carry decodable information about experimental conditions without requiring a priori definition of regions of interest.

At the intermediate level, **region-of-interest (ROI) analysis** applies MVPA to anatomically or functionally defined parcels, enabling investigation of distributed information within known brain networks. At the coarsest scale, **whole-brain MVPA** treats the entire brain volume as a single feature vector, addressing questions about global pattern discriminability. The toolbox also supports **representational similarity analysis (RSA)**, in which the similarity structure of neural patterns is compared across conditions, subjects, or modalities using distance matrices and second-order inferential statistics.

Classification is supported by multiple algorithms including linear [[support-vector-machines]], correlation-based classifiers, and nearest-neighbor methods. Cross-validation schemes — including leave-one-out, k-fold, and leave-one-session-out — protect against overfitting by ensuring that training and testing data are drawn from independent partitions. The toolbox handles both [[neuroimaging-fmri]] data in [[nifti]] format and electrophysiological data from [[eeg]] and [[meg]] recordings, supporting time-resolved MVPA for tracking the temporal evolution of neural representations.

## Relationship to TVB

CoSMoMVPA occupies a complementary role to [[tvb]] in the [[whole-brain-modeling]] ecosystem. While TVB generates simulated [[bold-signal]] time series from [[neural-mass-models]] and [[structural-connectivity]] data, CoSMoMVPA provides the tools for comparing simulated activity patterns against empirically observed ones. A typical integrative workflow involves fitting a personalized TVB model to individual subject data, generating simulated BOLD time series, and then applying CoSMoMVPA to assess whether the simulated patterns capture the same multivariate information structure present in the empirical data.

This approach enables a form of [[model-validation]] that goes beyond univariate measures of [[functional-connectivity]]. If a fitted TVB model reproduces not only regional BOLD amplitudes but also the distributed pattern information that distinguishes experimental conditions, it provides stronger evidence that the model captures behaviourally relevant aspects of [[brain-dynamics]]. The RSA framework in CoSMoMVPA is particularly well suited to this comparison, as representational dissimilarity matrices computed from simulated and empirical data can be compared directly using correlation metrics, regardless of differences in absolute signal scale.

## Related Software

CoSMoMVPA is the MATLAB counterpart to [[pymvpa]], with both toolboxes sharing a similar conceptual architecture while differing in implementation language and ecosystem integration. The [[the-decoding-toolbox]] offers additional MATLAB-based MVPA functionality with a focus on fMRI decoding studies. For researchers preferring Python, [[nilearn]] provides higher-level machine learning interfaces built on scikit-learn, with native support for neuroimaging data formats. Compared to these alternatives, CoSMoMVPA distinguishes itself through its deep integration with representational similarity analysis and its emphasis on permutation-based statistical inference.

Preprocessing of fMRI data for CoSMoMVPA is typically performed in [[spm]] or [[afni]], after which the toolbox reads resulting statistical maps or preprocessed volumes for classification. The toolbox also interoperates with [[neuroml]] representations of brain structure, enabling connectivity-informed MVPA that incorporates anatomical priors into the classification framework.

## References

1. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
2. Daniel Haenelt, D. Chaimow, M. E. Schmidt, S. Nasr, N. Weiskopf, R. Trampel. (2025). *Decoding of columnar-level organization across cortical depth using BOLD- and CBV-fMRI at 7 T*. bioRxiv. [DOI](https://doi.org/10.1101/2023.09.28.560016)
3. Dongyang Li, Haoyang Qin, Mingyang Wu, Chen Wei, Quanying Liu. (2025). *BrainFLORA: Uncovering Brain Concept Representation via Multimodal Neural Embeddings*. ACM Multimedia. [DOI](https://doi.org/10.1145/3746027.3754996)