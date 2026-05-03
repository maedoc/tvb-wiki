---
title: neuromaps
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-neuromaps, neuroimaging, brain-parcellations, connectomics, software-visualization]
sources: [markello2022]
referenced_by:
  - markello2022
---

# neuromaps

## Overview

neuromaps is a Python toolbox designed to facilitate rigorous comparisons between brain maps (also termed "brain annotations") across different neuroimaging modalities, coordinate spaces, and spatial resolutions. Developed by the Network Neuroscience Lab, the toolbox addresses a fundamental challenge in contemporary neuroimaging: the difficulty of comparing data that exist in heterogeneous formats, spaces, and representations. By providing standardized interfaces for fetching, transforming, and statistically comparing brain maps, neuromaps enables researchers to investigate correspondences between diverse imaging-derived measures—including [[functional-connectivity]] patterns, [[structural-connectivity]] metrics, receptor density distributions, and electrophysiological measurements—within a unified computational framework.

The toolbox was first released in 2021(@neuromaps-github) and subsequently published in *Nature Methods* (@markello2022), establishing it as a community-standard resource for map-to-map comparisons in network neuroscience. neuromaps operates as an open-source project (GitHub: netneurolab/neuromaps) distributed under a Creative Commons CC-BY-NC-SA license (@neuromaps-license), with ongoing development supported by the broader neuroimaging community.

## Motivation and Context

The proliferation of large-scale neuroimaging datasets—such as the [[human-connectome-project]] (HCP), [[uk-biobank]], and various task-based fMRI repositories—has generated an abundance of brain maps spanning multiple modalities and spatial scales. Researchers increasingly seek to relate these diverse measurements to one another: for example, correlating [[resting-state]] [[functional-connectivity]] with [[structural-connectivity]] derived from [[diffusion-imaging]], or comparing receptor density maps from [[neuroimaging-pet]] with [[neuroimaging-fmri|functional MRI]] activity patterns. However, such cross-modal comparisons are technically challenging because brain maps are typically represented in different coordinate systems (e.g., MNI152 volumetric space vs. FreeSurfer's fsaverage or fsLR surface spaces), at different spatial resolutions, and with different parcellation schemes.

Prior to neuromaps, researchers had to individually implement transformation pipelines, locate and download appropriate atlases, and code custom statistical models to assess map correspondences—a process that was error-prone, poorly standardized, and difficult to reproduce. neuromaps addresses this fragmentation by providing a cohesive software ecosystem that handles atlas fetching, space transformation, parcellation, and statistical inference through a coherent API. This unification is particularly valuable for whole-brain modeling efforts, where empirical neuroimaging data must be integrated to constrain [[whole-brain-modeling|whole-brain models]] such as those implemented in [[tvb|The Virtual Brain]].

## Key Features

### Brain Map Repository

neuromaps includes a growing library of pre-processed brain maps ("annotations") spanning multiple domains. These maps are stored in their original coordinate spaces and cover diverse neurobiological measurements including cortical microstructure indicators (e.g., T1/T2 ratios, myelin content), task-based and [[resting-state]] [[functional-connectivity]] patterns, electrophysiological source estimates, neurotransmitter receptor densities, and genetic expression profiles. Users can programmatically access these annotations through the `datasets` module, which handles downloading, caching, and metadata management. This feature dramatically reduces the barrier to entry for cross-modal analyses, as researchers no longer need to locate and preprocess individual datasets from original sources.

### Coordinate Space Transformations

A core capability of neuromaps is robust transformation between major neuroimaging coordinate spaces. The toolbox supports bidirectional conversions between volumetric (MNI152) and surface-based (fsaverage, fsLR, CIVET) representations (@neuromaps-docs) through established registration fusion and multimodal surface matching algorithms. Volume-to-surface transformations leverage the "registration fusion" approach originally proposed by [[buckner2011]] and implemented by @wu2018, which combines anatomical and functional information to project volumetric signals onto the cortical surface. Surface-to-surface transformations employ the multimodal surface matching (MSM) algorithm developed by Robinson and colleagues (@robinson2014, @robinson2018), enabling accurate cross-subject alignment based on multiple features including myelin patterns and functional connectivity. These transformation capabilities are essential for comparing maps that natively exist in different representations—a common scenario when integrating multimodal neuroimaging data.

### Spatial Null Models

A distinctive feature of neuromaps is its implementation of spatial null models for statistically assessing correspondences between brain maps. Traditional correlation analysis between spatial maps is confounded by spatial autocorrelation—the fact that nearby brain regions tend to exhibit similar values, inflating apparent correlations and leading to inflated false positive rates. neuromaps addresses this by providing several spatial null model implementations that preserve the spatial structure of the data while generating random surrogate maps under appropriate null hypotheses. These include the Alexander-Bloch method (@alexander-bloch2018), which rotates the map on the cortical surface, the @burt2018 parametric spatial null model, the Vázquez-Rodríguez et al. (@vazquez-rodriguez2019) rotation test, and various parcel-based permutation approaches. Implementing these null models is crucial for conducting statistically rigorous map comparisons, particularly when working with high-resolution [[brain-parcellations|parcellations]] or surface-based representations.

### Parcellation and Resampling Utilities

neuromaps provides utilities for parcellating volumetric and surface data into region-based representations, as well as functions for resampling images to common spaces and resolutions. The `Parcellater` class implements flexible parcellation workflows that can handle arbitrary atlas definitions, while resampling functions ensure that maps being compared exist in compatible spatial configurations. These utilities complement the transformation pipeline and enable seamless integration with downstream analyses in tools like [[nilearn]] or [[the-virtual-brain]].

## Relationship to TVB

neuromaps provides complementary functionality to [[the-virtual-brain|TVB]] in the broader ecosystem of whole-brain modeling and connectome-based research. While TVB focuses on dynamical system simulation—using [[neural-mass-models|neural mass models]] constrained by empirical [[structural-connectivity]] to generate simulated [[functional-connectivity]] and neuroimaging signals—neuromaps focuses on the preprocessing, transformation, and statistical comparison of empirical neuroimaging data that serve as inputs to such models.

In practice, the two tools can be integrated in several ways. First, neuromaps can be used to prepare [[structural-connectivity]] matrices from [[diffusion-imaging]] data (e.g., tractography-derived connectivity matrices) that subsequently feed into TVB simulations. The coordinate transformation capabilities enable researchers to parcellate white matter tractograms into region-based connectivity matrices compatible with TVB's connectivity framework. Second, neuromaps can be used to compare simulated brain dynamics from TVB with empirical [[functional-connectivity]] patterns, assessing model validity by examining the correspondence between model-generated and observed resting-state networks. The spatial null model functionality is particularly valuable in this context, as it provides proper statistical benchmarks for evaluating similarity between simulated and empirical maps. Third, both tools share a commitment to open science and reproducibility, with TVB's emphasis on collaborative model sharing and neuromaps' provision of transparent, documented workflows for neuroimaging data processing.

## Key Papers

The primary neuromaps methodology paper, published in *Nature Methods* (@markello2022), establishes the toolbox's core functionality and demonstrates its application to several canonical problems in network neuroscience. The paper details the transformation algorithms, spatial null models, and dataset access patterns that form the backbone of the software. Related methodological contributions include the original formulations of spatial null models (@alexander-bloch2018; @burt2018, @burt2020), registration fusion approaches for volume-to-surface projection (@buckner2011; @wu2018), and multimodal surface matching algorithms (@robinson2014, @robinson2018). Users of neuromaps should cite both the toolbox paper and the original sources of any annotation data employed in their analyses.

## Related Software

neuromaps intersects with several other tools in the neuroimaging ecosystem. [[nilearn]] provides general-purpose machine learning and statistical learning capabilities for neuroimaging data, with some overlapping functionality in terms of atlas fetching and basic transformations. [[templateflow]] offers a complementary repository for neuroimaging templates and atlases, focusing on template-specific resources rather than cross-modal comparison tools. The [[brain-connectivity-toolbox|brain connectivity toolbox (BCT)]] provides network analysis functions for examining topological properties of brain networks, complementing neuromaps' emphasis on spatial map comparisons. [[connectome-workbench]]—specifically the `wb_command` utility—provides the underlying transformation engine that neuromaps wraps, and must be installed for full functionality. Additional related tools include [[brainspace]] for surface-based visualization and [[brainiak]] for advanced intersubject correlation analyses.

## Technical Implementation

neuromaps is written in Python (version 3.8+) (@neuromaps-docs) and depends on established scientific computing libraries including [[nibabel]] for neuroimaging file I/O, [[nilearn]] for basic image operations, NumPy/SciPy for numerical computing, and scikit-learn for machine learning utilities. The toolbox provides both a programmatic Python API and command-line interfaces for common operations. Installation is available via PyPI (`pip install neuromaps`) or directly from the GitHub repository. Notably, full transformation functionality requires [[connectome-workbench]] to be installed and accessible on the system PATH, as neuromaps delegates computational heavy-lifting to Workbench's `wb_command` utility.

The toolbox's architecture is organized into functional modules: `datasets` for annotation and atlas fetching, `transforms` for coordinate space conversions, `nulls` for spatial null model generation, `parcellate` for region-based summarization, `stats` for statistical comparisons, and `plotting` for visualization utilities. This modular design enables users to employ specific components in isolation while maintaining interoperability across the full analysis pipeline.

## References

- Alexander-Bloch, A., Shou, H., Liu, S., Satterthwaite, T. D., Glahn, D. C., Shinohara, R. T., Vandekar, S. N., & Raznahan, A. (2018). On testing for spatial correspondence between maps of human brain structure and function. *NeuroImage*, 178, 540-551. https://doi.org/10.1016/j.neuroimage.2018.05.070

- Buckner, R. L., Krienen, F. M., Castellanos, A., Thomas, M. B., & Yeo, B. T. T. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. *Journal of Neurophysiology*, 106(3), 1125-1165. https://doi.org/10.1152/jn.00338.2011

- Burt, J. B., Demirtaş, M., Eckner, W. J., Nave, G., Ji, A., Martin, W. J., ... & Murray, J. D. (2018). Hierarchy of non-random features of spatial autocorrelation in the human brain. *Nature Neuroscience*, 21(10), 1404-1412. https://doi.org/10.1038/s41593-018-0189-4

- Burt, J. B., Zheng, Y., & Helmer, K. (2020). A statistical framework for robust null models applied to neuroimaging data. *NeuroImage*, 223, 117340. https://doi.org/10.1016/j.neuroimage.2020.117340

- Markello, R. D., Bazir, A. J., Paquola, C., Zhang, Y., Amiri, K., Milham, M. P., ... & Margulies, D. S. (2022). neuromaps: a toolbox for standardized and reproducible processing, visualization, and comparison of brain maps. *Nature Methods*, 19(12), 1792-1799. https://doi.org/10.1038/s41592-022-01637-6

- Robinson, E. C., Jbabdi, S., Glasser, M. F., Andersson, J., Burgess, G. C., Harms, M. P., ... & Smith, S. M. (2014). MSM: Multimodal surface matching. *NeuroImage*, 100, 192-206. https://doi.org/10.1016/j.neuroimage.2014.04.069

- Robinson, E. C., Garcia, K., Glasser, M. F., Chen, L., Coalson, T. S., Makropoulos, A., ... & Smith, S. M. (2018). Multimodal surface matching with fast and robust methods. *NeuroImage*, 171, 256-270. https://doi.org/10.1016/j.neuroimage.2018.01.071

- Vázquez-Rodríguez, B., Suárez, L. E., Markello, R. D., Shafiei, G., Paquola, C., Hagmann, P., ... & Misic, B. (2019). Integrating gradient and framework: A structure-function correspondence in the human cortex. *Proceedings of the National Academy of Sciences*, 116(35), 17335-17344. https://doi.org/10.1073/pnas.1814844116

- Wu, J., T., Zalesky, A., & Eickhoff, S. B. (2018). Registration fusion for surface-based neuroimaging. *Human Brain Mapping*, 39(8), 3233-3248. https://doi.org/10.1002/hbm.24071

- neuromaps contributors. (2021). neuromaps v0.1.0 [Software release]. GitHub. https://github.com/netneurolab/neuromaps/releases

- neuromaps contributors. (2024). neuromaps Documentation [Software documentation]. GitHub. https://netneurolab.github.io/neuromaps/

- neuromaps contributors. (2024). neuromaps README: License [Software documentation]. GitHub. https://github.com/netneurolab/neuromaps/blob/main/README.md