---
created: 2026-04-20
sources:
- raw/papers/van-essen-2013.md
- raw/papers/barch-2013.md
- raw/papers/smith-2013-hcp.md
tags:
- database-hcp
- neuroimaging-fmri
- neuroimaging-dti
- connectomics
- structural-connectivity
- functional-connectivity
- resting-state
- task-based
- dataset
title: HCP Dataset
type: concept
updated: '2026-05-04'
---

The **HCP Dataset** refers to the publicly released [[neuroimaging]] data from the Human Connectome Project (HCP), a landmark initiative to map the structural and functional connectivity of the healthy adult human brain. Unlike its parent initiative (the [[human-connectome-project]]), which encompasses the broader research program, the HCP Dataset specifically denotes the curated collection of multimodal brain imaging scans acquired using standardized protocols and made openly available to the neuroscience community. The dataset comprises structural MRI, task-based functional MRI, resting-state functional MRI, and diffusion imaging data from approximately 1200 healthy young adults [1], representing the largest and most comprehensively characterized neuroimaging repository of its kind when first released.

## Motivation and Scientific Context

Prior to the HCP Dataset, whole-brain modeling efforts were constrained by fragmented datasets acquired with heterogeneous protocols across different institutions, making cross-study comparisons difficult and limiting the statistical power of connectivity analyses. The HCP Dataset addressed this by establishing uniform acquisition standards and preprocessing pipelines, enabling researchers to construct [[structural-connectivity]] matrices and [[functional-connectivity]] maps with unprecedented consistency. For [[whole-brain modeling]] specifically, the dataset provides the empirical foundation upon which [[connectome]]-based simulations can be validated, offering both the anatomical wiring diagrams derived from diffusion imaging and the functional dynamics observed in resting-state and task-evoked fMRI acquisitions.

## Dataset Contents and Acquisition Protocols

The HCP Dataset incorporates multiple imaging modalities designed to capture complementary aspects of brain organization. Structural MRI acquisitions include T1w and T2w images at high resolution (0.7 mm isotropic) [1] providing detailed anatomical delineation for [[parcellation]] and [[parameter-estimation]] purposes. The diffusion imaging protocol employs multi-shell HARDI (high angular resolution diffusion imaging) with b-values of 1000, 2000, and 3000 s/mm² [1], enabling robust [[tractography]] reconstruction of white-matter pathways and the derivation of [[structural-connectivity]] matrices at resolutions defined by the [[glasser-atlas]] (360 regions) [1] or alternative parcellation schemes.

Functional MRI data in the HCP Dataset encompasses both [[resting-state]] and task-based acquisitions. Resting-state fMRI was collected using a multiband echo-planar imaging sequence achieving 2 mm isotropic spatial resolution and 0.72 s temporal resolution [2], capturing spontaneous low-frequency fluctuations in the blood-oxygen-level-dependent signal that reveal [[spiking-neural-networks]] such as the [[default-mode-network]]. The task-fMRI component employs a battery of seven paradigm categories [2] probing emotion processing, gambling decisions, language comprehension and production, motor execution, relational reasoning, social cognition, and working memory, enabling characterization of task-evoked activation patterns and comparison with [[functional-connectivity]] dynamics observed at rest.

## Preprocessing and Derived Data Products

A distinguishing feature of the HCP Dataset is the extensive preprocessing pipeline applied before public release, implementing artifact removal, motion correction, and registration to standard [[mni-space]] coordinates. The HCP preprocessing pipelines (available as [[hcp-pipelines]]) employ sophisticated algorithms for fieldmap unwarping, intensity normalization, and surface projection, substantially reducing the analytical burden on downstream users. Derived data products include CIFTI-format dense connectomes representing voxel-wise functional connectivity, grayordinate files combining surface and volume representations, and pre-computed [[connectivity]] matrices parcellated according to multiple atlas schemes [3]. These refined outputs have become reference datasets for benchmarking [[parcellation]] algorithms, [[community-detection]] methods, and [[graph-theory]] metrics applied to brain networks.

## Relationship to The Virtual Brain

The HCP Dataset serves as a critical data source for [[the-virtual-brain]] (TVB) workflows that construct personalized [[whole-brain model]]s from empirical connectivity data. TVB's [[tvb-adapters]] and connectivity pipeline tools can ingest HCP-derived structural connectivity matrices to define the anatomical coupling between neural populations in simulations of brain dynamics. The resting-state fMRI data enables validation of simulated functional connectivity against empirical patterns, facilitating parameter-optimization routines that tune model parameters to match observed brain states. Studies employing HCP data within TVB have investigated [[brain-oscillations]], [[epilepsy-modeling]], and personalized approaches to [[personalized-brain-modeling]] where individual subject connectivity profiles inform simulation parameters. Additionally, the dataset provides the structural basis for [[aal-atlas]]-based connectivity analyses and supports integration with alternative parcellation schemes for comparative whole-brain modeling studies.

## Related Concepts

The HCP Dataset intersects with numerous concepts in the [[connectomics]] and neuroimaging domains. It provides the empirical basis for [[structural-connectivity]] reconstruction, serves as the source data for [[functional-connectivity]] analyses, and supports both [[resting-state]] and task-based research paradigms. The dataset's multi-modal nature enables integration of [[diffusion-imaging]]-derived tractography with [[fmri]]-based functional dynamics, supporting [[effective-connectivity]] analyses and [[dynamic-causal-modeling]] approaches. Alternative large-scale neuroimaging resources include [[abide]] for autism research and the [[uk-biobank]] for population-level studies, though these differ in demographic composition and acquisition protocols.

## References

1. (authors unknown). *The WU-Minn Human Connectome Project: An Overview*.
2. (authors unknown). *Function in the Human Connectome: Task-fMRI and Individual Differences in Behavior*.
3. (authors unknown). *Resting-State fMRI in the Human Connectome Project*.