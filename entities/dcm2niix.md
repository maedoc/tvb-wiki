---
created: 2026-04-28
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-f45e6044c92f.md
- raw/papers/basser-1994.md
tags:
- software-brain-modeling
- neuroimaging-dti
- neuroimaging-fmri
- diffusion-imaging
- tractography
- structural-connectivity
- whole-brain-modeling
title: dcm2niix
type: entity
updated: '2026-05-18'
---

dcm2niix is an open-source command-line utility for converting medical imaging data from DICOM format to NIfTI. In the computational neuroscience ecosystem, it functions as an established neuroimaging tool that performs the DICOM conversion step required for downstream preprocessing pipelines. [[raw/papers/semanticscholar-f45e6044c92f|Haber et al. (2026)]] describe how TI-Toolbox integrates dcm2niix alongside SimNIBS and FreeSurfer within an end-to-end workflow that encompasses structural MRI preprocessing, volume conduction modeling, and analysis, illustrating its role as a foundational component in research pipelines for neuroimaging and non-invasive brain stimulation studies.

## Motivation and Context

Medical imaging scanners universally output data in DICOM format, yet whole-brain modeling frameworks require standardized neuroimaging formats that preserve spatial and temporal information. [[raw/papers/sanz-leon-2013|Sanz Leon et al. (2013)]] describe how [[the-virtual-brain]] constructs personalized brain network models by combining empirical [[structural-connectivity]] derived from diffusion MRI tractography with [[neural-mass-models]] and forward models for [[fmri]] time series. Before these data can be analyzed by tractography or functional connectivity tools, however, the raw DICOM volumes must be converted into a format that these pipelines can consume. dcm2niix bridges this gap, producing NIfTI files that serve as the initial inputs to the analysis chains feeding whole-brain models.

## Role in Diffusion Imaging and Structural Connectivity

The centrality of diffusion imaging to structural connectivity estimation underscores the importance of reliable format conversion. [[raw/papers/basser-1994|Basser et al. (1994)]] introduced diffusion tensor imaging as a method for characterizing water diffusion anisotropy in biological tissues, establishing the mathematical framework that provides the foundation for modern [[tractography]] methods reconstructing white-matter pathways. The diffusion-weighted DICOM files acquired on clinical scanners contain the raw measurements that, once converted to NIfTI by dcm2niix, can be processed by tractography algorithms to generate the [[structural-connectivity]] matrices that constrain [[whole-brain-modeling]] simulations in platforms such as [[the-virtual-brain]].

## Relationship to TVB

Although dcm2niix is not specific to [[the-virtual-brain]], it occupies a critical upstream position in the preprocessing chain that supplies whole-brain models with empirical data. [[raw/papers/sanz-leon-2013|Sanz Leon et al. (2013)]] describe how TVB combines empirical structural connectivity with neural mass models and forward models for EEG, MEG, and fMRI, requiring precisely oriented neuroimaging data as inputs. TVB workflows require structural connectivity from diffusion MRI and functional time series from [[fmri]], both of which originate as DICOM output from scanner consoles. By converting these data to NIfTI while preserving spatial orientation and acquisition geometry, dcm2niix enables the subsequent tractography and functional preprocessing stages that produce the connectivity estimates imported into [[the-virtual-brain]]. Many TVB tutorials and connectivity pipelines assume NIfTI-formatted inputs, making dcm2niix a necessary initial step in the broader computational neuroscience toolbox.

## Ecosystem Integration

dcm2niix integrates with the broader [[bids]] data organization ecosystem and is employed by conversion utilities that structure scanner output into standardized layouts. For quality assessment, researchers apply tools such as [[mriqc]] to the converted volumes, while subsequent functional preprocessing may be performed by platforms like [[fsl-melodic]]. Visualization of converted data can be carried out using [[3d-slicer]] or related viewers. For diffusion acquisitions specifically, the converted NIfTI files feed tractography pipelines such as [[mrtrix3-connectome]], whose outputs directly inform the anatomical connectivity constraints used in [[the-virtual-brain]] and related whole-brain modeling frameworks.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2026). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research.*. Brain Stimulation. [DOI](https://doi.org/10.1016/j.brs.2025.103016)
3. (authors unknown). *MR diffusion tensor spectroscopy and imaging*.