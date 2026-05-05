---
created: 2025-01-15
sources:
- raw/papers/bein-2018.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-380768cf42a8.md
tags:
- software-neuroimaging
- neuroimaging
- software-visualization
- dti
- diffusion-imaging
- neuroimaging-dti
title: PyDICOM
type: entity
updated: '2026-05-04'
---

## Overview

PyDICOM is an open-source Python library designed for reading, writing, and manipulating medical imaging data in the DICOM (Digital Imaging and Communications in Medicine) format. DICOM is the international standard for medical imaging, particularly in [[neuroimaging]] contexts where it underlies virtually all MRI, CT, and PET acquisition workflows. PyDICOM provides a pure-Python interface to DICOM files, enabling researchers and developers to work with clinical and research imaging data without requiring compiled dependencies or external toolkits. The library has become a foundational utility in the Python neuroimaging ecosystem, serving as a low-level building block for higher-level analysis frameworks[^pydicom-docs].

## Key Features

PyDICOM's core functionality centers on parsing DICOM files—specifically the binary structure that encapsulates pixel data arrays alongside extensive metadata headers. The library implements a complete DICOM data model, exposing elements as Python objects with typed values, named attributes, and semantic grouping[^pydicom-github]. Researchers can read individual DICOM files or entire directories, access pixel arrays as NumPy arrays for numerical processing, and modify or create new DICOM objects with custom metadata. The library handles the full DICOM information model including patient demographics, acquisition parameters, image positioning, and the complex vendor-specific private tags common in MRI data.

A distinguishing characteristic of PyDICOM is its pure-Python implementation, which avoids compiled extensions except where explicitly needed for optimized pixel processing. This design choice facilitates cross-platform portability and simplifies debugging in research environments. The library supports both DICOM File-meta Information (the wrapper around the core data set) and the full range of transfer syntaxes including explicit VR Little Endian, implicit VR Little Endian, and various compression schemes. For [[whole-brain|whole-brain modeling]] workflows, PyDICOM enables preprocessing of structural and [[diffusion-mri]] data extracted from scanner formats into forms amenable to [[connectome]] reconstruction.

The library maintains active development and provides extensive documentation covering common use cases such as anonymization, anonymization profiles for research compliance, pixel data rescaling, and integration with NumPy/SciPy for image processing pipelines. Version 2.x introduced modernized API patterns while maintaining backward compatibility, and the library now supports Python 3.8+.

## Relationship to TVB

PyDICOM occupies a position in [[the-virtual-brain]] (TVB) ecosystem as a utility layer for data ingestion rather than a core modeling component. In TVB's typical workflow, structural and functional neuroimaging data serve as empirical constraints for whole-brain models—diffusion tensor imaging (DTI) provides [[structural-connectivity]] matrices while [[resting-state|resting-state fMRI]] supplies [[functional-connectivity]] estimates. PyDICOM facilitates the initial data handling phase: reading raw scanner output in DICOM format, extracting b-values and gradient directions from diffusion acquisitions, and accessing header fields necessary for proper image orientation and spatial normalization.

While TVB users more commonly interact with pre-processed NIfTI data (handled by [[nibabel]]), PyDICOM remains essential when working with fresh acquisitions, proprietary vendor sequences, or when specific DICOM header information must be accessed for quality control or subject metadata management. The library bridges between the clinical imaging workflow (where DICOM is universal) and the research analysis pipeline (where NIfTI and [[cifti]] formats predominate). For studies involving [[personalized-brain-modeling]], PyDICOM can process subject-specific anatomical scans prior to [[parcellation]] and connectome construction[^nibabel-paper].

## Relationship to Other DICOM Tools

PyDICOM differs from Dcmtk (the officially-supported C++ DICOM toolkit maintained by OFFIS) in that it is written in pure Python and prioritizes programmatic access over command-line utilities. DCMTK provides mature tools like dcmconv, dcmdump, and dcmodify for batch processing; PyDICOM instead offers the flexibility of Python scripting for custom workflows[^dcmtk-official]. In practical neuroimaging contexts, the two tools are often used together: dcmtk handles conversion to intermediate formats while PyDICOM provides rapid prototyping and integration with analysis code.

Within the broader Python ecosystem, PyDICOM complements [[pydra]] for workflow orchestration and interfaces with [[nipype]] through DICOM-based input nodes. The library is also related to [[dcm2niix]] (a DICOM-to-NIfTI converter) but operates at a lower level—PyDICOM can implement custom conversion logic or preprocess DICOM data before passing to dcm2niix for format conversion[^dcm2niix-paper]. For [[diffusion-imaging]] pipelines specifically, PyDICOM's handling of diffusion-weighted imaging (DWI) headers makes it useful for quality control and bvec/bval extraction prior to tractography with Mrtrix3 or Dipy.

## Key Technical Considerations

When using PyDICOM in neuroimaging research pipelines, several technical aspects warrant attention. First, DICOM files store pixel data in various photometric interpretations (MONOCHROME1/2, RGB, YBR_FULL) that may require color space conversion before analysis. Second, the distinction between implicit and explicit VR (Value Representation) transfer syntaxes affects how data elements are parsed; PyDICOM handles both but the explicit VR is required for certain vendor-specific private tags. Third, MRI vendors (Siemens, GE, Philips) include proprietary private tags that encode sequence-specific parameters—for advanced diffusion models or multi-band acquisitions, these may contain essential metadata not present in standard DICOM fields.

The library's handling of anonymization deserves particular attention in research contexts. PyDICOM provides utilities to remove or redact patient-identifying information, but researchers should verify compliance with their institutional review board (IRB) requirements and consider that certain imaging metadata (such as acquisition timestamps or scanner serial numbers) may enable re-identification even without explicit name fields.

## Related Software

- [[nibabel]] — Python library for reading neuroimaging formats including [[nifti]] and CIFTI
- Dcmtk — C++ DICOM toolkit with command-line utilities
- [[dcm2niix]] — DICOM to NIfTI/[[bids]] converter
- Dipy — Diffusion MRI analysis in Python
- Mrtrix3 — Advanced [[tractography]] and [[connectivity]] analysis
- Freesurfer — Automated segmentation and cortical parcellation
- [[mriqc]] — Automated MRI quality control
- [[nitrc]] — Neuroimaging software resource portal
- Spm — Statistical Parametric Mapping (also handles DICOM import)

## Key Papers

1. **PyDICOM: A pure Python package for working with DICOM files** — The official documentation and GitHub repository serve as the primary reference for the library's design, API, and implementation details[^pydicom-github].

2. **nibabel: Accessing a Plethora of Neuroimaging file formats** — This paper describes the NIfTI format ecosystem that PyDICOM often feeds into, establishing the relationship between DICOM ingestion and downstream format conversion[^nibabel-paper].

3. **dcm2niix: A Cross Platform Tool for Converting DICOM to NIfTI** — Documents the complementary role of dcm2niix in neuroimaging pipelines, which often operates on data preprocessed via PyDICOM[^dcm2niix-paper].

## References

1. B. Bein (2018). *[[pyedflib]]: Python library for reading and writing EDF/BDF files*. Journal of Open Source Software. [DOI](https://doi.org/10.21105/joss.00899)
2. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
4. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)