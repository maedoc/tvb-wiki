---
created: 2026-04-28
sources:
- raw/papers/wang-etal-2015-gretna.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
tags:
- software-brain-modeling
title: DPABI
type: entity
updated: '2026-04-30'
---

title: DPABI
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [software-visualization, neuroimaging-fmri, [[resting-state]], data-processing]
sources:
  - https://doi.org/10.1016/j.neuroimage.2014.06.030
  - https://doi.org/10.3389/fnins.2014.00671

# DPABI

## Overview

DPABI (Data Processing Assistant for Brain Imaging) is a MATLAB-based toolbox that provides graphical user interface (GUI) and batch processing capabilities for analyzing neuroimaging data, with a primary focus on resting-state functional magnetic resonance imaging (fMRI). Developed by Chao‑Gan Yan and colleagues at the Institute of Psychology, Chinese Academy of Sciences, DPABI integrates commonly used preprocessing [[steps]] and analysis routines into a unified framework, enabling researchers to perform complete data analysis workflows without writing extensive custom code. The toolbox has become one of the most widely adopted open‑source packages for resting‑state fMRI analysis, particularly among researchers who prefer GUI‑driven workflows over command‑line interfaces.

## Key Features

DPABI encompasses several interconnected modules that address distinct stages of neuroimaging data processing. The **Data Processing** module implements the standard preprocessing pipeline for resting‑state fMRI, including slice timing correction, motion correction (realignment), spatial normalization to [[mni-space]], and spatial smoothing with a Gaussian kernel. These steps follow conventions established by the neuroimaging community and are configurable through the GUI, allowing users to adjust parameters such as the order of operations, smoothing kernel size, and scrubbing thresholds for motion artifacts.

The **RESTplus** component constitutes a comprehensive toolkit for resting‑state functional [[connectivity]] analysis. REST (RESting‑state fMRI data analysis toolkit) provides calculations of regional homogeneity (ReHo), amplitude of low‑frequency fluctuation (ALFF), and fractional ALFF (fALFF), which serve as basic metrics of local brain activity. Beyond these voxelwise measures, RESTplus computes seed‑based functional connectivity using correlation analysis, enabling researchers to examine [[whole‑brain]] connectivity patterns seeded from regions of interest. The toolbox also implements graph theoretical analysis through integration with the [[neuromorpho‑toolkit]], allowing computation of small‑world properties, [[modularity]], and hub metrics at both regional and network levels.

DPABI includes dedicated tools for [[mne‑connectivity]] analysis, facilitating examination of time‑varying connectivity patterns that may reveal transient neural coordination mechanisms. The **GRETNA** module provides graph theory‑based network analysis capabilities, including network construction (thresholding, binarization, weighted networks), topological metric computation, and network‑based statistical testing. This makes DPABI particularly valuable for researchers studying the [[small‑world‑networks]] properties of brain connectivity or [[rich‑club]] organization in [[neural‑mass‑models]].

The toolbox further supports surface‑based visualization through integration with [[connectome‑workbench]], allowing researchers to project volumetric results onto cortical surfaces for visualization on standard brain atlases such as the [[aal‑atlas|Automated Anatomical Labeling]] and [[yeo‑atlas|Yeo 7‑network]] parcellations.

## Relationship to TVB

DPABI occupies a complementary role relative to [[the‑virtual‑brain]] (TVB) in the broader landscape of [[whole‑brain‑modeling]] tools. While TVB focuses on constructing and simulating [[computational‑neuroscience|computational models]] of large‑scale brain networks using [[neural‑mass‑models]], DPABI provides the empirical data preprocessing and analysis foundation that informs such modeling efforts. In typical research workflows, DPABI processes empirical [[fmri]] data to extract [[functional‑connectivity]] matrices, which may subsequently inform the construction of personalized [[whole‑brain‑modeling|whole‑brain models]] in TVB.

The connection between these tools operates bidirectionally: DPABI‑derived connectivity patterns can be used to constrain TVB model parameters through [[parameter‑estimation]] techniques, while TVB simulations can generate synthetic fMRI data that benchmark DPABI analysis pipelines. Both tools benefit from structured [[neuroimaging]] data formats and benefit from integration with preprocessing pipelines such as [[fmriprep]] and visualization platforms like [[connectome‑workbench]]. Researchers pursuing [[personalized‑brain‑modeling]] applications frequently employ DPABI for extracting individual subject connectivity features that drive TVB model personalization.

## Key Papers

The original DPABI publication by Yan et al. (2014) introduced the toolbox as a unified environment for resting‑state fMRI analysis, demonstrating its capabilities through applications to the [[hcp‑dataset|Human [[connectome]] Project]] data. The paper emphasized the toolbox's accessibility to novice users through its GUI while maintaining computational efficiency through MATLAB‑based implementation. Subsequent methodological papers have detailed specific DPABI modules, including the RESTplus component for [[functional-connectivity]] analysis and dynamic connectivity tools for examining time‑varying network properties.

A subsequent publication by Yan et al. (2014b) introduced DPARSF (Data Processing Assistant for Resting‑State fMRI) as a dedicated resting‑state preprocessing pipeline, which was later integrated into the broader DPABI framework. This work established many of the preprocessing conventions and quality control measures that remain central to DPABI's functionality.

## Related Software

DPABI shares methodological foundations with several other neuroimaging toolboxes in the ecosystem. It complements [[spm]] (Statistical Parametric Mapping) and [[fsl]] (FMRIB Software Library) by providing resting‑state‑specific analysis routines that extend general‑purpose preprocessing capabilities. For connectivity analysis, DPABI overlaps functionally with the [[neuromorpho‑toolkit]], which provides graph theoretical methods, and [[conn]], another GUI‑driven connectivity analysis toolbox. The visualization components of DPABI integrate with [[afni]], [[freesurfer]], and [[connectome‑workbench]], enabling multi‑modal visualization workflows.

| Feature | DPABI | SPM | FSL | Conn |
|--------|-------|-----|-----|------|
| GUI‑driven | ✓ | Partial | Partial | ✓ |
| Resting‑state metrics | ✓ | Limited | Limited | ✓ |
| Graph theory | ✓ | ✗ | Limited | ✓ |
| Dynamic connectivity | ✓ | ✗ | ✗ | ✓ |
| Surface visualization | ✓ | ✗ | ✓ | ✓ |

The choice between these tools often depends on user expertise, specific analysis requirements, and integration with other pipelines. DPABI remains particularly popular in the East Asian neuroscience community and among researchers prioritizing rapid GUI‑based analysis workflows.

## References

1. Wang, J., Wang, X., Xia, M., Liao, X., Evans, A., & He, Y. (2015). *GRETNA: a graph theoretical network analysis toolbox for MATLAB*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2015.04.016)
2. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)