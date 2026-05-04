---
title: Nilearn
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-visualization, neuroimaging-fmri, neuroimaging-eeg, computational-neuroscience]
sources: []
---

Nilearn is an open-source Python library designed for fast and easy statistical learning on neuroimaging data. Built on top of [[nibabel]] for file I/O and [[scikit-learn]] for machine learning primitives, nilearn provides high-level tools for loading, visualizing, cleaning, and analyzing brain imaging data—particularly functional magnetic resonance imaging (fMRI) volumes and cortical surfaces. The library has become a standard tool in the neuroimaging community for decoding, pattern analysis, and connectivity studies.

## Overview

Nilearn addresses a fundamental challenge in neuroimaging: translating raw brain scan data into interpretable statistical models. The library abstracts away the complexity of handling NIfTI files, surface data formats, and various atlases, enabling researchers to focus on scientific questions rather than file format gymnastics. It excels at multivariate pattern analysis (MVPA), also known as brain decoding, where the goal is to predict cognitive states or disease conditions from distributed patterns of brain activity.

The library follows a consistent API design influenced by [[scikit-learn]], making it accessible to researchers familiar with machine learning workflows. This principled approach has contributed to nilearn's popularity in both the cognitive neuroscience and clinical research communities.

## Key Features

**Data Loading and Manipulation**: Nilearn provides unified interfaces for loading neuroimaging data from various formats including NIfTI, CIFTI, and GIFTI. The library integrates seamlessly with [[bids]] datasets through [[pybids]], enabling reproducible analysis pipelines that comply with community data standards.

**Atlas and Parcellation Support**: The library includes convenient access to numerous brain parcellations including the [[schaefer-atlas]], [[yeo-atlas]], [[desikan-killiany-atlas]], and many others. Researchers can easily extract region-of-interest (ROI) time series for connectivity analysis or define searchlight volumes for local pattern classification.

**Statistical Learning**: Nilearn implements decoding algorithms including support vector machines (SVM), logistic regression, and ridge regression for brain state prediction. The library provides cross-validation utilities, permutation testing for significance assessment, and tools for model selection and hyperparameter tuning.

**Connectivity Analysis**: Functional connectivity estimation is streamlined through built-in correlation-based methods. Users can compute connectivity matrices from fMRI time series and export these for downstream analyses in tools like [[the-virtual-brain]] or the [[brain-connectivity-toolbox]].

**Visualization**: High-quality visualization capabilities include glass brain renders,statistical maps overlaid on anatomical templates, connectome visualizations, and interactive plotting using [[plotly]] compatibility. These figures are publication-ready and support multiple coordinate systems.

**Signal Cleaning**: Basic preprocessing utilities for fMRI data include detrending, temporal filtering, and confound regression. While nilearn is not a full preprocessing pipeline (for which researchers use [[fmriprep]]), it provides essential cleaning steps for decoding analyses.

## Relationship to TVB

Nilearn serves as a valuable preprocessor and feature extractor for [[whole-brain modeling]] workflows in The Virtual Brain. Researchers often use nilearn to extract regional time series from preprocessed fMRI data, which can then be used to estimate functional connectivity matrices as inputs to TVB's generative models. The library's atlas manipulation tools enable seamless conversion between different parcellation schemes, facilitating the integration of empirical connectivity data into personalized brain models.

Conversely, TVB's simulation outputs can be analyzed using nilearn's statistical learning tools for model validation or to compare simulated dynamics against empirical recordings. The complementary nature of these tools—the former focused on empirical data analysis and the latter on dynamical system simulation—makes them natural partners in research workflows combining [[computational-neuroscience]] with data-driven inference.

## Key Papers

The nilearn library is described in "Nilearn: Fast and Easy Statistical Learning for Neuroimaging" (Abraham et al., 2014, Frontiers in Neuroinformatics), which provides the primary methodological reference for the library's design and capabilities. Additional documentation and examples are maintained on the project website and in Jupyter notebook tutorials.

## Related Software

- [[nibabel]] - Neuroimaging file I/O library that nilearn builds upon
- [[scikit-learn]] - Machine learning framework providing nilearn's classification primitives
- [[fmriprep]] - Comprehensive fMRI preprocessing pipeline
- [[brain-connectivity-toolbox]] - Graph-theoretic analysis of brain networks
- [[pybids]] - BIDS-compatible data handling
- [[mne-connectivity]] - Connectivity analysis for M/EEG data
- [[the-virtual-brain]] - Whole-brain modeling simulator
