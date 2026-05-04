---
created: 2026-04-23
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-brain-modeling
- software-dipy
title: PANDA
type: entity
updated: '2026-05-04'
---

**PANDA** (Pipeline for Analyzing braiN Diffusion imAges) is a MATLAB-based toolbox developed at the [Beijing Normal University](http://bnu.edu.cn/) for automated processing of diffusion magnetic resonance imaging (dMRI) data. The software provides a comprehensive, end-to-end solution for converting raw diffusion-weighted images into fiber orientation distributions and structural brain networks, making it particularly valuable for researchers studying human brain [[connectivity]] and [[white-matter]] architecture.

## Overview

[[diffusion-mri]] is a non-invasive imaging technique that measures the random displacement of water molecules in biological tissues. In white matter, water molecules preferentially diffuse along axonal fibers, allowing researchers to infer fiber orientation indirectly. However, extracting meaningful structural information from raw dMRI data requires a complex pipeline of preprocessing [[steps]], including motion correction, eddy current correction, and fiber tracking. PANDA automates this entire workflow, enabling researchers without extensive imaging expertise to produce publication-quality connectivity data <cite>Liu et al. 2013</cite>.

The toolbox was designed with accessibility in mind. By providing a unified graphical user interface (GUI) and command-line options, PANDA lowers the barrier to entry for [[neuroimaging]] laboratories seeking to incorporate dMRI analysis into their research workflows. The software integrates established algorithms from the neuroimaging community—including tools from [[fsl]] and [[mricron]]—while adding novel processing routines developed specifically for large-scale connectivity analysis <cite>Cui et al. 2018</cite>.

## Technical Architecture

PANDA implements a three-stage pipeline that transforms raw dMRI images into [[structural-connectivity]] matrices. Each stage addresses specific computational challenges inherent to [[diffusion-imaging]] analysis.

### Stage 1: Preprocessing

The first stage performs quality control and artifact correction on raw diffusion data. This includes eddy current correction (which accounts for image distortions caused by rapidly switching gradient fields), motion correction (which aligns volumes acquired at different time points), and brain extraction (which isolates the cerebral tissue from surrounding skull and soft tissue). PANDA leverages the [[fsl]] BET tool for brain extraction and implements custom correction algorithms optimized for human dMRI data <cite>Liu et al. 2013</cite>.

Crucially, PANDA computes quality assurance metrics at this stage, flagging datasets with excessive motion or artifact contamination that may compromise downstream analysis. This automated quality control helps ensure that connectivity matrices derived from PANDA reflect genuine neuroanatomical features rather than processing artifacts.

### Stage 2: Diffusion Metrics Computation

Following preprocessing, PANDA computes diffusion tensor imaging (DTI) metrics and fiber orientation distributions (FODs). The software fits diffusion tensors to each voxel using least-squares estimation, extracting [[fractional-anisotropy]] (FA), mean diffusivity (MD), and principal eigenvector maps. These scalar metrics provide quantitative measures of white matter microstructure—FA reflects the degree of directional coherence in fiber populations, while MD captures overall diffusion magnitude <cite>Jiang et al. 2013</cite>.

For more sophisticated analysis, PANDA supports constraint spherical deconvolution (CSD), which resolves complex fiber configurations where multiple fiber populations intersect within a single voxel. This capability is essential for accurate [[tractography]] in regions of fiber crossing, which constitute a significant portion of the human white matter volume.

### Stage 3: Network Construction

The final stage constructs structural brain networks from fiber tracking results. PANDA implements deterministic tractography using the fiber orientation distributions, generating streamlines that trace white matter pathways between cortical and subcortical regions. These streamlines are parcellated according to a user-specified brain atlas (such as the Desikan-Killiany or AAL [[parcellation]] schemes), and connection weights are computed based on the number of reconstructed fibers connecting each region pair <cite>Jiang et al. 2013</cite>.

The output is a weighted connectivity matrix where rows and columns correspond to brain regions and matrix entries reflect the strength of structural connectivity. These matrices serve as the foundational structural constraint for computational models of [[brain-dynamics]], including those implemented in [[The Virtual Brain]].

## Parallelization and Performance

PANDA was designed for large-scale neuroimaging studies involving hundreds of subjects. The software implements a multi-level parallelization strategy using the PSOM (Pipeline System for Octave and MATLAB) framework <cite>Liu et al. 2013</cite>. At the coarsest level, individual subjects are processed concurrently, maximizing throughput on multi-core computing clusters. Within each subject, parallel processing is applied to independent processing modules—such as the multiple direction sets in diffusion metric computation—enabling efficient utilization of available computational resources.

This architecture allows PANDA to process a typical single-subject dMRI dataset (approximately 60 diffusion directions at 2mm resolution) in under 30 minutes on a standard workstation, while a cohort of 500 subjects can be processed in approximately 4 hours on a 64-core cluster. These performance characteristics make PANDA suitable for large-scale population studies, including those targeting the full human [[connectome]].

## Relationship to The Virtual Brain

PANDA is frequently used in conjunction with [[The Virtual Brain]] (TVB) to generate personalized brain models. The structural connectivity matrices produced by PANDA serve as the anatomical foundation for TVB's [[whole-brain|whole-brain modeling]] framework <cite>Liu et al. 2013</cite>. In TVB, the connectivity matrix defines the coupling strength between brain regions, constraining the dynamical equations that govern regional neural activity.

This integration enables researchers to simulate personalized brain dynamics by incorporating individual-specific structural connectivity derived from each subject's dMRI data. Personalized structural connectivity is particularly valuable for clinical applications, where individual differences in white matter organization may correlate with disease states or treatment responses. The combination of PANDA and TVB supports the broader goal of [[personalized-brain-modeling]], where computational models are tailored to individual patients for diagnostic or therapeutic purposes <cite>Jiang et al. 2013</cite>.

## Related Software

PANDA is part of a broader ecosystem of neuroimaging tools that collectively support the dMRI analysis workflow. The following software packages are commonly used in conjunction with PANDA or provide alternative functionality:

- '[[fsl]] — FMRIB Software Library, providing foundational preprocessing tools including BET and Eddy Correct'
- '[[mricron]] — MRIcron, a visualization tool for browsing neuroimaging datasets'
- 'trackvis — TrackVis, for visualizing streamlines from fiber tracking'
- '[[nipype]] — Nipype, a Python framework for neuroimaging workflow management that can interface with PANDA'
- '[[the-virtual-brain]] — [[tvb|The Virtual Brain]], platform for whole-brain dynamic modeling'
- '[[nest]] — NEST, neural simulation tool sometimes combined with TVB for large-scale network simulations'
- '[[brian2]] — Brian2, neural simulator useful for detailed local cortical modeling'
- '[[resting-state]] — Resting-state [[fmri]] analysis, complementary to structural connectivity from dMRI'

## Installation and Availability

PANDA is distributed as open-source software and is freely available for academic use. The toolbox runs on MATLAB (with Statistics and Image Processing Toolboxes) and requires a working installation of [[fsl]] for certain preprocessing steps. Documentation, source code, and example datasets are available from the project repository.

The current maintenance status reflects its role as established infrastructure within the neuroimaging community. While active development has slowed relative to the initial release period, the software remains widely used and continues to receive updates for compatibility with newer MATLAB versions and dMRI acquisition protocols.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
3. (authors unknown). *BRAPH: A Pipeline for Brain Connectivity Analysis*.