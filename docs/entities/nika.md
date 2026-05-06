---
created: 2025-01-15
sources:
- authors: Bellec P, et al.
  title: 'NIAK: Neuroimaging Analysis Kit'
  url: https://github.com/SIMEXP/niak
  year: '2014'
- authors: Bellec P, et al.
  title: 'BASC: A method for identifying stable clusters in brain parcellations'
  url: https://doi.org/10.1016/j.neuroimage.2010.06.041
  year: '2010'
- authors: Bellec P, et al.
  title: 'The pipeline system for Octave and Matlab (PSOM): a lightweight scripting
    framework and execution engine for scientific workflows'
  url: https://doi.org/10.3389/fninf.2012.00063
  year: '2012'
- title: NIAK on NITRC
  url: https://www.nitrc.org/projects/niak/
  year: '2014'
- raw/papers/arxiv-2603.26971.md
- raw/papers/huntenburg-2018.md
- raw/papers/semanticscholar-d6e43299345d.md
tags:
- software-neuroimaging
- neuroimaging-fmri
- neuroimaging-preprocessing
- functional-connectivity
- connectomics
title: NIAK
type: entity
updated: '2026-05-06'
---

# NIAK

## Overview

NIAK (NeuroImaging Analysis Kit) is an open-source software library for the preprocessing and connectivity analysis of large-scale functional neuroimaging datasets, with a primary focus on [[fmri]] data. Originally developed by Pierre Bellec and collaborators at the ACELab (Analysis of Neuro Images Computational Engineering Laboratory) at McGill University's Montreal Neurological Institute, NIAK provides a comprehensive pipeline system for transforming raw MRI acquisitions into analysis-ready time series suitable for [[functional-connectivity]] studies and [[brain-parcellations]] construction. The software is written in GNU Octave and MATLAB, making it accessible to researchers who prefer these high-level numerical computing environments over Python-based solutions.

## Key Features

### Preprocessing Pipeline

NIAK implements a complete fMRI preprocessing workflow that includes motion correction, slice timing correction, non-uniformity intensity normalization (N3 bias field correction), spatial normalization to MNI stereotaxic space, and spatial smoothing with configurable Gaussian kernels. The pipeline integrates seamlessly with the MINC (Medical Image NetCDF) file format native to the Montreal Neurological Institute, while also supporting [[nifti]] format through conversion utilities. A distinctive feature of NIAK is its emphasis on quality control, generating detailed reports at each preprocessing stage that allow researchers to identify and exclude problematic volumes or subjects from subsequent analyses.

### PSOM Framework

The Pipeline System for Octave and Matlab (PSOM) underlying NIAK enables automatic parallel execution of processing Steps across multi-core workstations and high-performance computing clusters. PSOM handles dependency resolution, ensuring that downstream processing steps only execute after their prerequisites complete successfully. This design allows researchers to define complex multi-step workflows with minimal overhead and automatically benefits from parallel processing resources without manual parallelization code.

### Connectivity Analysis

Beyond preprocessing, NIAK includes modules for functional [[connectivity]] analysis, including seed-based correlation, group-level stability analysis using bootstrap resampling, and the BASC (Bootstrap Analysis of Stable Clusters) framework for identifying robust brain parcellations. The BASC pipeline implements innovative methods for determining the optimal number of clusters using MSTEPS (Multi-Scale Stability [[parameter-estimation]]), helping researchers avoid arbitrary choices in [[parcellation]] resolution.

### Region Growing

A signature capability of NIAK is its region-growing algorithm for spatially constrained parcellation of [[neuroimaging]] data. This method progressively builds regions by aggregating adjacent voxels based on similarity of their fMRI time series, producing anatomically meaningful parcels that maintain homogeneous temporal profiles. The algorithm can operate either on individual subject data or on concatenated multi-subject datasets, enabling generation of group-wise parcellations that respect population-level homogeneity while maintaining individual variability.

## Relationship to TVB

While NIAK and [[the-virtual-brain]] (TVB) serve different primary purposes—they are not directly integrated—they share philosophical underpinnings in the analysis of large-scale brain dynamics. NIAK provides the preprocessing infrastructure that can generate the cleaned time series data required as input for whole-brain modeling pipelines like TVB. Researchers studying [[whole-brain-modeling]] or [[personalized-brain-modeling]] often use preprocessing tools like NIAK to prepare empirical data for subsequent model fitting and simulation. Additionally, NIAK's emphasis on [[resting-state]] analysis and functional connectivity aligns with TVB's capacity to simulate spontaneous brain activity at rest, making it a potential complementary tool in computational psychiatry applications where [[epilepsy-modeling]] or [[schizophrenia-models]] are investigated.

## Key Papers

The foundational paper describing NIAK's pipeline architecture is "The pipeline system for Octave and Matlab (PSOM): a lightweight scripting framework and execution engine for scientific workflows" (Bellec et al., 2012, Frontiers in Neuroinformatics). NIAK played a critical role in preprocessing the [[abide]] (Autism Brain Imaging Data Exchange) dataset, making possible numerous studies of [[functional-connectivity]] alterations in autism spectrum disorder. The ABIDE preprocessed dataset using NIAK has been cited extensively in the [[connectomics]] literature.

## Historical Context and Current Status

NIAK was initiated around 2008 and saw active development through approximately 2017, with the SIMEXP laboratory at Université de Montréal assuming maintenance responsibilities. As documented in the GitHub repository, the SIMEXP lab announced cessation of active development around 2022, though the software remains available on GitHub and [[nitrc]] for researchers who have existing pipelines or methodological reasons to continue using it. The Python ecosystem, particularly packages like Nilearn and [[bids]]-based workflows (including [[fmriprep]]), has largely absorbed the user community seeking modern, actively maintained neuroimaging preprocessing solutions.

## Related Software

- [[fmriprep]] — popular Python-based fMRI preprocessing pipeline
- [[nilearn]] — Python library for neuroimaging data analysis
- [[bids]] — standard data format for neuroimaging datasets
- [[aal-atlas]] — Automated Anatomical Labeling atlas used in NIAK pipelines

## References

1. Abigail Kelly, Ramchandra Rimal, Arpan Sainju. (2026). *Graph Attention Network-Based Detection of Autism Spectrum Disorder*. [Link](](https://arxiv.org/abs/2603.26971))
2. (authors unknown). *[[nighres]]: processing tools for high-resolution neuroimaging*.
3. A. Dehsarvi, Lukas Frontzkowski, Anna Dewenter, Michael Schöll, N. Franzmeier. (2025). *ADprep – A Fully‐Automated Software for Large‐scale Multimodal MRI and PET Imaging Workflows*. Alzheimer's & Dementia. [DOI](](https://doi.org/10.1002/alz70856_101373))