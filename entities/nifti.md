---
created: 2026-04-20
sources:
- raw/papers/friston-1993.md
- raw/papers/smith-2013-connectomics.md
- raw/papers/sporns-2011.md
- raw/papers/semanticscholar-d2dfba2091a2.md
- raw/papers/semanticscholar-cabf914d6370.md
- raw/papers/semanticscholar-dacc3b888fa6.md
tags:
- neuroimaging
- software-neuroimaging
- neuroimaging-fmri
- neuroimaging-dti
- neuroimaging-eeg
title: NIfTI
type: concept
updated: '2026-05-06'
---

NIfTI ([[neuroimaging]] Informatics Technology Initiative) is a file format standard for storing neuroimaging data, particularly volumetric magnetic resonance imaging data such as functional magnetic resonance imaging ([[fmri]]), diffusion tensor imaging (DTI), and structural MRI. The format was developed to address limitations in the earlier Analyze format and has become the de facto standard for sharing neuroimaging data across software platforms, databases, and research laboratories worldwide.

## Historical Context and Motivation

The NIfTI format emerged in the early 2000s from a standardization effort led by the Neuroimaging Informatics Technology Initiative, a working group funded by the National Institutes of Health. Prior to NIfTI, the Analyze format (specifically the .img and .hdr file pair) was widely used, but it lacked unambiguous specification of spatial coordinate systems, leading to frequent confusion about the orientation and alignment of neuroimaging data. This ambiguity posed significant challenges for multi-site studies, longitudinal analyses, and the integration of data across different software packages. The NIfTI format introduced a unified coordinate system and header structure that resolved these ambiguities, making it possible to reliably share and combine neuroimaging datasets from different scanners, processing pipelines, and research groups [see @nifti-1-spec, 2004].

The formal specification, known as NIfTI-1, was published in 2004 and quickly adopted by major neuroimaging software packages including [[freesurfer]], [[afni]], [[fsl]], and [[spm]]. Later, NIfTI-2 was introduced to support larger datasets with 64-bit addressing, though NIfTI-1 remains the most widely used variant in practice.

## Technical Specification

The NIfTI format stores neuroimaging data in a single file (with extension .nii) rather than the separate header and image files used by Analyze. The header contains 348 bytes of metadata that specify the data dimensions, voxel sizes, spatial orientation, and coordinate system. Critically, the header includes the quaternion conversion coefficients that unambiguously define the orientation of the data in space, eliminating the confusion that plagued earlier formats.

The data can be stored in various numeric types including 8-bit unsigned integers, 16-bit signed integers, 32-bit floating point, and 64-bit floating point. For neuroimaging applications, 16-bit signed integers (sufficient for storing raw MRI signal intensities) and 32-bit floating point (used after preprocessing to preserve precision) are most common. The format supports up to seven spatial dimensions, though four-dimensional data (three spatial dimensions plus time) is the standard for fMRI and other time-series neuroimaging modalities.

In practice, NIfTI files are often stored in gzip-compressed form with the `.nii.gz` extension, which reduces file size significantly without data loss—this is the most common storage format in modern neuroimaging pipelines.

## Relationship to Whole-Brain Modeling

In the context of [[whole-brain-modeling|whole-brain modeling]] and [[the-virtual-brain|TVB]], NIfTI serves as a primary input format for structural and functional connectivity data. TVB accepts structural connectivity matrices derived from diffusion-weighted imaging data, which are typically stored in NIfTI format during preprocessing. Similarly, preprocessed fMRI timeseries used to derive [[functional-connectivity]] matrices are commonly stored as NIfTI files. The format's compatibility with major neuroimaging toolboxes makes it straightforward to prepare data for TVB simulation using preprocessing pipelines built with [[nibabel]], [[nipype]], or other Python-based neuroimaging libraries.

The [[mrtrix3-connectome]] and similar large-scale datasets distribute their imaging data almost exclusively in NIfTI format, making it the standard interchange format for obtaining empirical [[connectivity]] data used in personalized brain models. When constructing [[personalized-brain-modeling|personalized brain models]], researchers typically begin with NIfTI-format anatomical scans, diffusion images, and functional timeseries as inputs to TVB's connectivity pipeline.

## Relationship to Related Formats and Tools

NIfTI shares conceptual territory with several other neuroimaging data formats. The [[cifti]] format, developed by the [[human-[[connectome]]-project]] to address the needs of surface-based neuroimaging, extends NIfTI capabilities to dense timeseries on cortical surfaces, complementing the volumetric representation of traditional NIfTI data [see @hcp-reference, 2013]. The [[bids]] (Brain Imaging Data Structure) standard provides a recommended directory organization scheme for neuroimaging data and frequently stores primary data in NIfTI format within a standardized hierarchy.

The Python library [[nibabel]] provides programmatic access to NIfTI files, allowing researchers to read, write, and manipulate neuroimaging data in Python scripts and pipelines. This library is a dependency of many preprocessing workflows and is directly compatible with TVB's data handling routines. Similarly, [[nipype]] provides a workflow framework that operates on NIfTI data, enabling standardized preprocessing pipelines that produce TVB-ready outputs. These Python libraries have become essential tools in the neuroimaging ecosystem, facilitating reproducible analysis pipelines across laboratories.

## Current Status and Open Questions

NIfTI remains the dominant format for storing and sharing neuroimaging timeseries and volumetric data. However, the format has known limitations that continue to motivate development of alternatives. NIfTI's single-file approach, while simpler than Analyze's two-file system, can be cumbersome for very large datasets common in modern neuroimaging. The format lacks built-in support for data compression, storage of metadata beyond basic header fields, and explicit representation of non-volumetric data such as surfaces or parcels.

Despite these limitations, NIfTI's simplicity, widespread adoption, and robust tool support ensure it will remain central to neuroimaging data interchange for the foreseeable future. Researchers building [[whole-brain]] models frequently encounter NIfTI files as their primary input, making understanding of the format essential for [[computational-neuroscience]] workflows.

## References

1. (authors unknown). *Functional Connectivity: The Principal-Component Analysis of Large (PET and fMRI) Data Sets*.
2. (authors unknown). *Functional [[connectomics]] from [[resting-state|Resting-State fMRI]]*.
3. (authors unknown). *Networks of the Brain*.