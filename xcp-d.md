---
title: XCP-D
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, resting-state, functional-connectivity, bids]
sources: []
---

XCP-D (eXtensible Connectivity Pipeline – Distributed) is a robust post-processing pipeline for functional magnetic resonance imaging (fMRI) data, developed through a collaborative effort between the PennLINC (Pennsylvania Lifespan Informatics and Neuroimaging Center) at the University of Pennsylvania and the DCAN (Developmental Cognition and Neuroimaging Labs) at the University of Minnesota. The pipeline is designed to extend the preprocessing work initiated by tools like [[fMRIprep]] to produce analysis-ready derivatives for [[resting-state]] [[functional connectivity]] analyses, making it a critical component in the neuroimaging software ecosystem for large-scale brain mapping studies.

## Overview and Motivation

The field of [[neuroimaging]] has achieved substantial standardization in the preprocessing of fMRI data, with widely adopted tools such as [[fMRIprep]] providing robust, minimally preprocessed outputs in compliance with the Brain Imaging Data Structure (BIDS) standard. However, the post-processing stage—which includes essential steps like nuisance regression, motion correction, temporal filtering, and generation of derived measures such as functional connectivity matrices—remains considerably less standardized. This heterogeneity in post-processing approaches has been identified as a significant source of variability and reduced reproducibility across neuroimaging studies, as different denoising strategies can substantially alter the resulting connectivity estimates and potentially introduce spurious findings that cannot be replicated across laboratories.

XCP-D was developed to address this gap by providing a comprehensive, standardized post-processing pipeline that consumes outputs from multiple widely used preprocessing pipelines—including [[fMRIprep]], the Human Connectome Project (HCP) minimal preprocessing pipelines, the ABCD-BIDS pipeline, NiBabies for infant data, and UK Biobank data—while applying consistent and empirically validated denoising strategies. The pipeline builds upon the foundation established by the earlier XCP engine and incorporates modern software engineering practices, including extensive continuous integration testing, modular design using NiPype, and containerized distribution via Docker and Singularity. By automating the path from preprocessed fMRI data to functional connectivity matrices, XCP-D enables researchers to achieve reproducible, scalable analyses across large datasets comprising thousands of participants.

## Technical Features and Processing Pipeline

XCP-D implements a comprehensive post-processing workflow that encompasses several distinct stages, each addressing specific sources of artifact and variability in the BOLD (blood-oxygen-level-dependent) signal. The pipeline begins by identifying high-motion outlier volumes using framewise displacement (FD) calculations, where volumes exceeding a user-specified threshold (default 0.3 mm) are flagged for removal or interpolation. This motion censoring approach, originally popularized by Power and colleagues, is widely regarded as one of the most effective strategies for mitigating the deleterious effects of head motion on functional connectivity estimates.

Following motion assessment, XCP-D applies a configurable nuisance regression strategy to remove structured noise from the BOLD timeseries. The pipeline supports multiple regression models including the 24-parameter model (six motion parameters, their squares, derivatives, and squared derivatives), the 27P model (adding mean white matter and CSF signals), and the 36P model (adding derivatives of the anatomical signals). More advanced options include ACompCor (Anatomical CompCor), which uses principal component analysis to identify and remove noise components from white matter and CSF, and AROMA (ICA-based Automatic Removal of Motion Artifacts), which classify independent components as either neural signal or motion-related noise. Users may also provide custom confounds or combine multiple strategies, such as AROMA with global signal regression.

Temporal filtering is performed using a Butterworth bandpass filter (default 0.01–0.08 Hz), which preserves the low-frequency oscillations that form the basis of resting-state functional connectivity while removing both slow drift and high-frequency noise. The pipeline can optionally apply despiking to attenuate large amplitude spikes in the timeseries, interpolate censored volumes to preserve the original temporal structure, and perform spatial smoothing with a Gaussian kernel (default 6 mm FWHM). XCP-D also supports filtering of motion parameters to remove respiratory artifacts that can contaminate framewise displacement estimates, using either notch or low-pass filters with cutoff frequencies calibrated to the participant's age.

## Supported Input Formats and Atlases

One of XCP-D's distinguishing features is its ability to consume preprocessed data from diverse sources, abstracting away the particularities of each preprocessing pipeline to provide a unified post-processing interface. The pipeline can directly process outputs from [[fMRIprep]] (the most robust support), NiBabies (for infant data from the Healthy Brain and Child Development study), HCP pipelines, ABCD-BIDS pipeline, and UK Biobank. For non-BIDS-compliant preprocessing outputs such as HCP and ABCD-BIDS data, XCP-D performs an ingression step that maps the files into a BIDS-like derivatives structure.

XCP-D generates resting-state derivatives using multiple parcellation atlases, enabling connectivity analyses at various spatial scales. The supported atlases include the Schaefer parcellation (100–1000 parcels across multiple resolutions), the Glasser 360 (a multi-modal parcellation derived from cortical myelin mapping and resting-state connectivity), the Gordon 333 (functional subdivisions of the default mode and control networks), the HCP subcortical atlas, and the Tian subcortical atlas. This atlas flexibility enables researchers to perform voxel-wise analyses (using dense timeseries), region-of-interest analyses, and decomposition-based methods such as independent component analysis (ICA) or non-negative matrix factorization (NMF).

## Quality Control and Visual Reports

Recognizing that automated processing pipelines require rigorous quality assurance, XCP-D generates comprehensive quality control (QC) measures and interactive visual reports for each processed dataset. The QC metrics include summary statistics of motion (mean FD, root-mean-square displacement), temporal derivative variance (DVARS) before and after denoising, and indices of registration quality between the BOLD data and both the structural image and the template space (using Dice similarity coefficients, coverage, and Pearson correlation).

The pipeline produces two types of HTML reports: a NiPreps-style summary that provides a concise overview of processing parameters, quality metrics, and carpet plots showing the timeseries before and after denoising; and a DCAN-style executive summary that includes an interactive BrainSprite viewer for assessing anatomical-functional registration, surface visualizations, and detailed QC plots. Both reports automatically generate a methods boilerplate that can be directly copied into manuscript submissions, ensuring accurate and complete reporting of the post-processing steps applied to the data.

## Relationship to The Virtual Brain

While XCP-D focuses specifically on post-processing of empirical fMRI data to extract clean timeseries and connectivity matrices, it relates to [[The Virtual Brain]] (TVB) in the broader context of whole-brain modeling and connectivity analysis. TVB is a neuroinformatics platform for constructing and simulating [[whole-brain models]] that integrate [[structural connectivity]] (typically derived from [[diffusion imaging]] tractography) with [[neural mass models]] to generate synthetic brain dynamics. The connectivity matrices produced by XCP-D from empirical data can serve as ground truth or validation targets for TVB simulations, enabling researchers to compare model-predicted functional connectivity with empirically observed patterns. Additionally, both tools emphasize reproducibility, open science, and containerized deployment, reflecting shared values in the neuroimaging community regarding computational standardization.

## Relationship to Related Software

XCP-D occupies a specific niche in the neuroimaging software ecosystem, complementing rather than duplicating the functionality of other tools. Unlike general-purpose fMRI analysis packages such as [[FSL]], [[AFNI]], or [[SPM]], which provide individual processing steps that require manual assembly into custom workflows, XCP-D offers a complete, validated pipeline optimized for resting-state connectivity analysis. Compared to alternatives like C-PAC (Configurable Pipeline for the Analysis of Connectomes), CONN, and Connectome Mapper 3, XCP-D distinguishes itself through its explicit focus on consuming preprocessed data from established pipelines and its extensive testing and validation on large-scale datasets including the Philadelphia Neurodevelopmental Cohort (PNC), ABCD study, and HCP young adults.

## Key Papers and Citation

The primary citation for XCP-D is the method paper by Mehta, Salo, Madison, and colleagues (2024) published in Imaging Neuroscience, which describes the pipeline's design, validation benchmarking, and demonstrated performance across multiple large datasets. The pipeline has been downloaded over 3,000 times from DockerHub prior to official release, indicating substantial community adoption and utility. Users should also cite the Zenodo DOI corresponding to the specific version used, as the pipeline continues to be actively developed with new features and improvements released regularly.

## Related Software

- [[fMRIprep]] – Primary preprocessing tool whose output XCP-D consumes
- [[AFNI]] – Used internally for despiking and ReHo calculations
- [[Connectome Workbench]] – Used for CIFTI processing and surface operations
- [[Nilearn]] – Provides baseline denoising functions that XCP-D extends
- [[NiPype]] – Python framework underlying XCP-D's modular architecture
- [[C-PAC]] – Alternative configurable connectivity analysis pipeline
- [[QSIPrep]] – Related preprocessing pipeline for diffusion MRI
- [[ASLPrep]] – Related preprocessing pipeline for arterial spin labeling MRI