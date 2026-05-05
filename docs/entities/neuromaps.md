---
created: 2026-04-30
referenced_by:
- markello2022
sources:
- raw/papers/winkler-2014-palm.md
- raw/papers/semanticscholar-028f7c6ac41d.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/semanticscholar-dacc3b888fa6.md
- raw/papers/semanticscholar-ebab0fdee30d.md
tags:
- software-neuromaps
- neuroimaging
- brain-parcellations
- connectomics
- software-visualization
title: neuromaps
type: entity
updated: '2026-05-04'
---

# neuromaps

## Overview

neuromaps is a Python toolbox designed to facilitate rigorous comparisons between brain maps (also termed "brain annotations") across different [[neuroimaging]] modalities, coordinate spaces, and spatial resolutions. Developed by the [[netneuroscience|Network Neuroscience]] Lab, the toolbox addresses a fundamental challenge in contemporary neuroimaging: the difficulty of comparing data that exist in heterogeneous formats, spaces, and representations. By providing standardized interfaces for fetching, transforming, and statistically comparing brain maps, neuromaps enables researchers to investigate correspondences between diverse imaging-derived measures—including [[functional-connectivity]] patterns, [[structural-connectivity]] metrics, receptor density distributions, and electrophysiological measurements—within a unified computational framework.

The toolbox was first released in 2021(@neuromaps-github) and subsequently published in *Nature Methods* (@markello2022), establishing it as a community-standard resource for map-to-map comparisons in network neuroscience. neuromaps operates as an open-source project (GitHub: netneurolab/neuromaps) distributed under a Creative Commons CC-BY-NC-SA license (@neuromaps-license), with ongoing development supported by the broader neuroimaging community.

## Motivation and Context

The proliferation of large-scale neuroimaging datasets—such as the [[human-connectome-project]] (HCP), [[uk-biobank]], and various task-based fMRI repositories—has generated an abundance of brain maps spanning multiple modalities and spatial scales. Researchers increasingly seek to relate these diverse measurements to one another: for example, correlating [[resting-state]] [[functional-connectivity]] with [[structural-connectivity]] derived from [[diffusion-imaging]], or comparing receptor density maps from [[neuroimaging-pet]] with [[neuromorpho-toolkit]] activity patterns. However, such cross-modal comparisons are technically challenging because brain maps are typically represented in different coordinate systems (e.g., MNI152 volumetric space vs. FreeSurfer's fsaverage or fsLR surface spaces), at different spatial resolutions, and with different parcellation schemes.

Prior to neuromaps, researchers had to individually implement transformation pipelines, locate and download appropriate atlases, and code custom statistical models to assess map correspondences—a process that was error-prone, poorly standardized, and difficult to reproduce. neuromaps addresses this fragmentation by providing a cohesive software ecosystem that handles atlas fetching, space transformation, [[parcellation]], and statistical inference through a coherent API. This unification is particularly valuable for [[whole-brain|whole-brain modeling]] efforts, where empirical neuroimaging data must be integrated to constrain [[whole-brain-modeling|whole-brain models]] such as those implemented in [[tvb|The Virtual Brain]].

## Key Features

### Brain Map Repository

neuromaps includes a growing library of pre-processed brain maps ("annotations") spanning multiple domains. These maps are stored in their original coordinate spaces and cover diverse neurobiological measurements including cortical microstructure indicators (e.g., T1/T2 ratios, myelin content), task-based and [[resting-state]] [[functional-connectivity]] patterns, electrophysiological source estimates, neurotransmitter receptor densities, and genetic expression profiles. Users can programmatically access these annotations through the `datasets` module, which handles downloading, caching, and metadata management. This feature dramatically reduces the barrier to entry for cross-modal analyses, as researchers no longer need to locate and preprocess individual datasets from original sources.

### Coordinate Space Transformations

A core capability of neuromaps is robust transformation between major neuroimaging coordinate spaces. The toolbox supports bidirectional conversions between volumetric (MNI152) and surface-based (fsaverage, fsLR, [[civet]]) representations through established registration fusion and multimodal surface matching algorithms. Volume-to-surface transformations leverage the "registration fusion" approach originally proposed by buckner2011 and implemented by @wu2018, which combines anatomical and functional information to project volumetric signals onto the cortical surface. Surface-to-surface transformations employ the multimodal surface matching (MSM) algorithm developed by Robinson and colleagues (@robinson2014, @robinson2018), enabling accurate cross-subject alignment based on multiple features including myelin patterns and functional [[connectivity]]. These transformation capabilities are essential for comparing maps that natively exist in different representations—a common scenario when integrating multimodal neuroimaging data.

### Spatial Null Models

A distinctive feature of neuromaps is its implementation of spatial null models for statistically assessing correspondences between brain maps. Traditional correlation analysis between spatial maps is confounded by spatial autocorrelation—the fact that nearby brain regions tend to exhibit similar values, inflating apparent correlations and leading to inflated false positive rates. neuromaps addresses this by providing several spatial null model implementations that preserve the spatial structure of the data while generating random surrogate maps under appropriate null hypotheses. These include the Alexander-Bloch method (@alexander-bloch2018), which rotates the map on the cortical surface, the @burt2018 parametric spatial null model, the Vázquez-Rodríguez et al. (@vazquez-rodriguez2019) rotation test, and various parcel-based permutation approaches. Implementing these null models is crucial for conducting statistically rigorous map comparisons, particularly when working with high-resolution [[brain-parcellations|parcellations]] or surface-based representations.

### Parcellation and Resampling Utilities

neuromaps provides utilities for parcellating volumetric and surface data into region-based representations, as well as functions for resampling images to common spaces and resolutions. The `Parcellater` class implements flexible parcellation workflows that can handle arbitrary atlas definitions, while resampling functions ensure that maps being compared exist in compatible spatial configurations. These utilities complement the transformation pipeline and enable seamless integration with downstream analyses in tools like Nilearn or [[the-virtual-brain]].

## Relationship to TVB

neuromaps provides complementary functionality to [[the-virtual-brain|TVB]] in the broader ecosystem of whole-brain modeling and connectome-based research. While TVB focuses on dynamical system simulation—using [[neural-mass-models|neural mass models]] constrained by empirical [[structural-connectivity]] to generate simulated [[functional-connectivity]] and neuroimaging signals—neuromaps focuses on the preprocessing, transformation, and statistical comparison of empirical neuroimaging data that serve as inputs to such models.

In practice, the two tools can be integrated in several ways. First, neuromaps can be used to prepare [[structural-connectivity]] matrices from [[diffusion-imaging]] data (e.g., tractography-derived connectivity matrices) that subsequently feed into TVB simulations. The coordinate transformation capabilities enable researchers to parcellate white matter tractograms into region-based connectivity matrices compatible with TVB's connectivity framework. Second, neuromaps can be used to compare simulated brain dynamics from TVB with empirical [[functional-connectivity]] patterns, assessing model validity by examining the correspondence between model-generated and observed resting-state networks. The spatial null model functionality is particularly valuable in this context, as it provides proper statistical benchmarks for evaluating similarity between simulated and empirical maps. Third, both tools share a commitment to open science and reproducibility, with TVB's emphasis on collaborative model sharing and neuromaps' provision of transparent, documented workflows for neuroimaging data processing.

## Key Papers

The primary neuromaps methodology paper, published in *Nature Methods* (@markello2022), establishes the toolbox's core functionality and demonstrates its application to several canonical problems in network neuroscience. The paper details the transformation algorithms, spatial null models, and dataset access patterns that form the backbone of the software. Related methodological contributions include the original formulations of spatial null models (@alexander-bloch2018; @burt2018, @burt2020), registration fusion approaches for volume-to-surface projection (buckner2011; @wu2018), and multimodal surface matching algorithms (@robinson2014, @robinson2018). Users of neuromaps should cite both the toolbox paper and the original sources of any annotation data employed in their analyses.

## Related Software

neuromaps intersects with several other tools in the neuroimaging ecosystem. Nilearn provides general-purpose machine learning and statistical learning capabilities for neuroimaging data, with some overlapping functionality in terms of atlas fetching and basic transformations. [[templateflow]] offers a complementary repository for neuroimaging templates and atlases, focusing on template-specific resources rather than cross-modal comparison tools. The [[brain-connectivity-toolbox|brain connectivity toolbox (BCT)]] provides network analysis functions for examining topological properties of brain networks, complementing neuromaps' emphasis on spatial map comparisons. [[connectome-workbench]]—specifically the `wb_command` utility—provides the underlying transformation engine that neuromaps wraps, and must be installed for full functionality. Additional related tools include [[brainspace]] for surface-based visualization and Brainiak for advanced intersubject correlation analyses.

## Technical Implementation

neuromaps is written in Python (version 3.8+) (@neuromaps-docs) and depends on established scientific computing libraries including [[nibabel]] for neuroimaging file I/O, Nilearn for basic image operations, NumPy/SciPy for numerical computing, and scikit-learn for machine learning utilities. The toolbox provides both a programmatic Python API and command-line interfaces for common operations. Installation is available via PyPI (`pip install neuromaps`) or directly from the GitHub repository. Notably, full transformation functionality requires [[connectome-workbench]] to be installed and accessible on the system PATH, as neuromaps delegates computational heavy-lifting to Workbench's `wb_command` utility.

The toolbox's architecture is organized into functional modules: `datasets` for annotation and atlas fetching, `transforms` for coordinate space conversions, `nulls` for spatial null model generation, `parcellate` for region-based summarization, `stats` for statistical comparisons, and `plotting` for visualization utilities. This modular design enables users to employ specific components in isolation while maintaining interoperability across the full analysis pipeline.

## References

1. (authors unknown). *Permutation inference for the general [[linear|linear model]]*.
2. Shengjie Qi, Xinda Song, Le Jia, Hongyu Cui, Yuchen Suo, Teng Long, Zhendong Wu, Xiaolin Ning. (2025). *The impact of channel density, inverse solutions, connectivity metrics and calibration errors on OPM-MEG connectivity analysis: A simulation study*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2025.121056)
3. Sakul Mahat, Sharmistha Guha, Jessica Bernard. (2026). *A Bayesian Framework for Quantifying Association Between Functional and Structural Data in Neuroimaging*. [Link](https://arxiv.org/abs/2603.21067)
4. Jui-To Wang, Ching-Po Lin, Huei-Min Liu, Carlo Pierpaoli, C. Lo. (2025). *Beyond [[tractography]] in brain connectivity mapping with dMRI morphometry and functional networks*. Brain Structure and Function. [DOI](https://doi.org/10.1007/s00429-025-03016-1)
5. Borja [[camino]]-Pontes, A. Jimenez-Marin, I. Tellaetxe-Elorriaga, Izaro Fernandez-Iriondo, A. Erramuzpe, I. Díez, Paolo Bonifazi, Marilyn Gatica, Fernando E. Rosas, D. Marinazzo, S. Stramaglia, Jesús M. Cortés. (2025). *Brain structural modules associated to functional high-order interactions in the human brain*. bioRxiv. [DOI](https://doi.org/10.1101/2025.03.21.644509)