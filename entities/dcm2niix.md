---
title: dcm2niix
created: 2026-04-28
updated: 2026-05-18
type: entity
tags:
- software-brain-modeling
- neuroimaging-dti
- neuroimaging-fmri
- diffusion-imaging
- tractography
- structural-connectivity
- whole-brain-modeling
sources:
- raw/papers/semanticscholar-f45e6044c92f.md
- raw/papers/sanz-leon-2013.md
- raw/papers/basser-1994.md
---

dcm2niix is an established neuroimaging tool that performs DICOM conversion, translating raw scanner output into [[nifti]] volumes compatible with analysis pipelines throughout the [[computational-neuroscience]] and [[neuroimaging]] ecosystem. [[raw/papers/semanticscholar-f45e6044c92f|Haber et al. (2026)]] integrate it alongside SimNIBS and [[freesurfer]] within end-to-end workflows encompassing structural MRI preprocessing, [[volume-conduction]] modeling, montage optimization, electric field simulation, and region-of-interest analysis for non-invasive [[brain-stimulation]] research. [[raw/papers/semanticscholar-f45e6044c92f|Haber et al. (2026)]] further note that the platform automates the complete research pipeline from DICOM conversion through final field analysis, embedding dcm2niix within containerized deployment frameworks that ensure reproducibility and cross-platform compatibility.

## Motivation and Context

Whole-brain modeling frameworks require standardized neuroimaging data to constrain network simulations and enable comparison between simulated and empirical recordings. [[raw/papers/sanz-leon-2013|Sanz Leon et al. (2013)]] describe how [[the-virtual-brain]] constructs personalized brain network models by combining empirical [[structural-connectivity]] derived from diffusion MRI tractography with [[neural-mass-models]] and forward models for [[neuroimaging-fmri|fMRI]] time series. [[raw/papers/basser-1994|Basser et al. (1994)]] introduced diffusion tensor imaging as a method for characterizing water diffusion anisotropy in biological tissues, establishing the tensor model that underlies modern [[tractography]] methods reconstructing white-matter pathways. [[raw/papers/semanticscholar-f45e6044c92f|Haber et al. (2026)]] observe that dcm2niix performs the DICOM conversion step required before these downstream preprocessing and modeling pipelines can generate the connectivity estimates that feed whole-brain simulation platforms.

## Role in Neuroimaging Preprocessing

Diffusion MRI and structural imaging provide the anatomical constraints that define connectivity in whole-brain network models. [[raw/papers/basser-1994|Basser et al. (1994)]] demonstrated that diffusion tensor measurements capture tissue microstructure non-invasively, establishing the mathematical framework that enables non-invasive reconstruction of white-matter pathways via [[tractography]]. [[raw/papers/sanz-leon-2013|Sanz Leon et al. (2013)]] detail how TVB integrates empirical structural connectivity with neural mass models and forward models for [[neuroimaging-eeg|EEG]], [[neuroimaging-meg|MEG]], and [[neuroimaging-fmri|fMRI]], enabling simulated signals to be compared directly against empirical recordings. [[raw/papers/semanticscholar-f45e6044c92f|Haber et al. (2026)]] employ dcm2niix specifically to convert raw scanner DICOM output into standardized volumes, feeding subsequent structural MRI preprocessing and [[volume-conduction]] modeling stages that generate anatomical constraints for platforms such as [[the-virtual-brain]].

## Relationship to TVB

Although dcm2niix is not specific to [[the-virtual-brain]], it occupies a critical upstream position in the preprocessing chain that supplies whole-brain models with empirical neuroimaging data. [[raw/papers/sanz-leon-2013|Sanz Leon et al. (2013)]] explain that TVB combines empirical [[structural-connectivity]] with [[neural-mass-models]] and forward models for [[neuroimaging-eeg|EEG]], [[neuroimaging-meg|MEG]], and [[neuroimaging-fmri|fMRI]] to enable personalized brain modeling from subject-specific neuroimaging. [[raw/papers/basser-1994|Basser et al. (1994)]] established that diffusion tensor imaging captures tissue microstructure non-invasively, providing the anatomical substrate for [[tractography]]-based [[connectome]] reconstruction that constrains large-scale brain network models. [[raw/papers/semanticscholar-f45e6044c92f|Haber et al. (2026)]] illustrate this pipeline architecture by embedding dcm2niix within TI-Toolbox, where the initial DICOM conversion enables subsequent preprocessing and modeling stages before analysis.

## Ecosystem Integration

dcm2niix is embedded within containerized deployment frameworks that ensure reproducibility and cross-platform compatibility in computational neuroscience. [[raw/papers/semanticscholar-f45e6044c92f|Haber et al. (2026)]] describe how TI-Toolbox automates the complete research pipeline from DICOM conversion through final field analysis, leveraging dcm2niix alongside SimNIBS and [[freesurfer]] to perform structural MRI preprocessing, [[volume-conduction]] modeling, montage optimization, electric field simulation, and region-of-interest analysis. [[raw/papers/sanz-leon-2013|Sanz Leon et al. (2013)]] show that TVB combines empirical structural connectivity with neural mass models and forward models for multiple neuroimaging modalities, enabling simulated signals to be compared directly against empirical recordings. [[raw/papers/basser-1994|Basser et al. (1994)]] established that diffusion tensor imaging captures tissue microstructure non-invasively, providing the biological foundation for the structural connectivity matrices that define large-scale network dynamics in simulation platforms.
