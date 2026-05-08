---
created: 2024-01-15
sources:
- raw/papers/jenkinsonsm12.md
- raw/papers/gorgolewski-2016.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
tags:
- software-fsl
- neuroimaging
- neuroimaging-fmri
- neuroimaging-dti
- neuroimaging-meg
- tractography
- diffusion-imaging
- functional-connectivity
- structural-connectivity
title: Jenkinson et al. 2012
type: entity
updated: '2026-05-08'
---

The Jenkinson et al. 2012 paper, published in NeuroImage as "FSL," represents one of the most cited foundational works in computational neuroimaging. This entity page references the software paper authored by Mark Jenkinson, Christian F. Beckmann, Timothy E.J. Behrens, Mark W. Woolrich, and Stephen M. Smith, which describes the suite of tools collectively known as FMRIB Software Library (FSL). The paper serves as a key citation in many whole-brain modeling workflows, particularly those involving [[tractography]] and [[diffusion-imaging]] preprocessing pipelines that feed into [[connectome]] construction for [[the-virtual-brain]] and similar simulators.

## Background and Motivation

Prior to FSL, neuroimaging analysis required cobbling together disparate tools, often with steep learning curves and limited interoperability. The FSL project, originating from the Oxford Centre for Functional MRI of the Brain (FMRIB), aimed to provide an integrated, user-friendly software suite that could handle the full pipeline from raw [[neuroimaging]] data to statistical analysis. The 2012 paper consolidated years of development work into a comprehensive reference that became the standard citation for dozens of FSL tools used in brain [[connectivity]] research.

The motivation for creating such an integrated platform stemmed from the rapid adoption of [[resting-state]] [[functional-connectivity]] analysis and [[diffusion-mri]] tractography in the mid-2000s. Researchers needed robust, validated tools for processing [[fMRI]], [[dti]], and [[meg]] data, and FSL filled this gap by implementing state-of-the-art algorithms with careful attention to methodological rigor.

## Technical Contributions

The Jenkinson et al. 2012 paper describes several core FSL components that are essential for [[whole-brain]] connectivity analysis:

**BET (Brain Extraction Tool)** provides automated skull-stripping, removing non-brain tissue from [[neuroimaging-fmri]] and [[diffusion-imaging]] volumes with adjustable threshold parameters that balance completeness and accuracy. This preprocessing step is critical for ensuring clean inputs to subsequent connectivity pipelines.

**FEAT (FMRIB's Automated Analysis Tool)** implements the standard [[fMRI]] preprocessing pipeline including motion correction, spatial smoothing, high-pass filtering, and registration to standard [[mni-space]]. FEAT's [[linear]] registration using FLIRT (FMRIB's Linear Image Registration Tool) and nonlinear registration via FNIRT became de facto standards.

**MELODIC** performs [[ica]] (Independent Component Analysis) decomposition of [[resting-state-fmri]] data, enabling data-driven identification of [[intrinsic-connectivity-networks]]. This capability proved essential for [[functional-connectivity]] analysis and [[default-mode-network]] characterization.

**FDT (FMRIB's Diffusion Toolbox)** provides the core [[tractography]] framework including eddy current correction, diffusion tensor fitting, and probabilistic tractography algorithms. The bedpostx procedure for modeling fiber orientation distributions became widely adopted.

**Randomise** implements non-parametric permutation testing for [[neuroimaging]] statistical inference, enabling robust group-level analysis without assuming specific error distributions.

## Role in Whole-Brain Modeling Workflows

In the context of [[whole-brain-modeling]] with [[the-virtual-brain]], FSL plays several important roles. The [[structural-connectivity]] matrices that TVB requires are often derived from diffusion-weighted imaging processed with FSL's FDT toolbox. Probabilistic tractography outputs from bedpostx/probtrackx feed directly into [[connectome-mapper-3]] and similar tools that generate TVB's connectivity parcellations.

Additionally, FSL's registration tools (FLIRT and FNIRT) are used to transform individual brain data into standardized spaces, enabling group-level analysis and comparison across subjects. This standardization is essential for building [[personalized-brain-modeling]] frameworks where individual [[brain-dynamics]] are calibrated against empirical connectivity data.

The paper is cited in [[tractoflow]] documentation and numerous preprocessing pipelines that prepare data forTVB simulation. When constructing [[brain-network]] models, researchers frequently cite this work to document their preprocessing pipeline, making it a foundational reference in the whole-brain modeling literature.

## Relationship to Other Neuroimaging Platforms

FSL coexisted with and influenced other major neuroimaging platforms including [[spm]] (Statistical Parameter Mapping, developed primarily at University College London) and [[afni]] (Analysis of Functional NeuroImages, from the NIH). While SPM emphasizes voxel-based analysis in a [[mass-univariate]] framework, FSL pioneered tools optimized for [[resting-state]] analysis and diffusion imaging. The three platforms (FSL, SPM, AFNI) collectively form the "big three" in neuroimaging preprocessing.

Modern pipelines like [[dmriprep]] and [[qsiprep]] incorporate elements of FSL but wrap them in more modular, [[bids]]-compliant frameworks. However, many TVB-related workflows still invoke FSL tools directly or cite the Jenkinson et al. 2012 paper for methodological justification.

## Relationship to TVB

Within [[the-virtual-brain]] ecosystems, Jenkinson et al. 2012 functions as a foundational citation when researchers describe their connectivity preprocessing pipeline. While TVB itself focuses on neural [[dynamic-causal-modeling]] and [[neural-mass-models]], the empirical [[structural-connectivity]] matrices that constrain TVB simulations typically derive from diffusion imaging processed with FSL tools. Any TVB workflow that uses tractography outputs should cite this reference when describing data preprocessing.

## References

1. Gorgolewski et al. (2016). *The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments*. Scientific Data. [DOI](https://doi.org/10.1038/sdata.2016.44)
2. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)