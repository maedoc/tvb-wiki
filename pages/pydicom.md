---
title: PyDICOM
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-visualization, neuroimaging, neuroimaging-mri, neuroimaging-ct]
sources:
  - https://pydicom.org/
  - https://www.iso.org/standard/65694.html
  - https://authors.library.nist.gov/_upload/pdfs/500-265.pdf
  - https://journal.r-project.org/articles/R06-2/
---

## Overview

PyDICOM is a pure Python package for reading, modifying, and writing DICOM (Digital Imaging and Communications in Medicine) files, the standard format for medical imaging data. Originally developed by Darcy Mason and later maintained by the broader community, PyDICOM provides a convenient Pythonic interface to the complex DICOM file format, enabling neuroscientists and researchers to programmatically access and manipulate medical imaging data from modalities such as magnetic resonance imaging (MRI), computed tomography (CT), positron emission tomography (PET), and single-photon emission computed tomography (SPECT) [1]. The library is particularly valuable in the context of whole-brain modeling, where structural and functional neuroimaging data must be imported, preprocessed, and transformed into formats suitable for computational simulation.

## Key Features

PyDICOM's core functionality centers on its ability to parse DICOM files—the binary format that encodes patient information, imaging parameters, pixel data, and metadata according to the DICOM standard (ISO 12052) [2]. The library represents each DICOM file as a hierarchical dataset object, where individual attributes (known as "tags" in DICOM parlance) can be accessed either by their numeric identifier (e.g., `(0x0010, 0x0010)` for Patient Name) or by a more readable string alias. This design allows researchers to extract clinical variables such as patient demographics, scan acquisition parameters, imaging sequence details, and voxel intensity matrices with minimal overhead.

Beyond simple reading, PyDICOM supports writing and modifying DICOM datasets, making it useful for data anonymization workflows where patient-identifiable information must be removed before sharing datasets. The library handles the compression schemes commonly used in medical imaging, including JPEG lossy and lossless compression, as well as run-length encoding [3]. For neuroimaging pipelines, PyDICOM can work in conjunction with higher-level libraries like [[nibabel]] or dedicated conversion wrappers that convert DICOM data into NIfTI format, which is more amenable to statistical analysis in tools like [[FSL]], [[SPM]], or [[FreeSurfer]].

## Relationship to TVB

In the context of [[the-virtual-brain]] (TVB), PyDICOM plays an indirect but important role in the data import pipeline. When constructing personalized whole-brain models, researchers often begin with structural [[neuroimaging]] data (T1-weighted MRI, diffusion tensor imaging) acquired in DICOM format from scanners. Although TVB operates on preprocessed connectivity matrices and regional time series rather than raw DICOM files directly, the initial conversion from DICOM to analysis-ready formats typically involves PyDICOM or tools built upon it. The library thus serves as a foundational layer in the preprocessing chain that transforms raw scanner output into the structural [[connectivity]] and [[functional-connectivity]] representations that TVB uses for simulation.

## Comparison to Related Tools

While PyDICOM provides low-level access to DICOM files, higher-level neuroimaging libraries often incorporate similar functionality. [[nibabel]] offers a unified interface to both DICOM and NIfTI formats but relies on PyDICOM for the DICOM parsing layer [4]. The [[dcmtk]] suite (written in C++) provides more comprehensive DICOM network (DICOM conformance) capabilities, including DICOM query/retrieve operations for querying Picture Archiving and Communication Systems (PACS), whereas PyDICOM focuses primarily on file-based operations. For researchers using the [[BIDS]] (Brain Imaging Data Structure) specification, tools like [[dcm2niix]] or [[HeuDiConv]] handle DICOM-to-BIDS conversion automatically, abstracting away the raw DICOM handling. In the TVB ecosystem, the [[tvb-library]] includes adapters that accept preprocessed neuroimaging data, but the initial DICOM-to-intermediate format conversion often passes through PyDICOM-based tooling.

## Use in Practice

Common workflows involving PyDICOM in computational neuroscience include extracting voxel data from DICOM series for quality control checks, anonymizing datasets before sharing via platforms like [[OpenNeuro]], converting DICOM headers into JSON sidecars for [[BIDS]] validation, and programmatically organizing multi-volume acquisitions into temporal sequences. The library's pure Python implementation means it has no binary dependencies, facilitating deployment in containerized environments (including [[Apptainer]] or Docker images) used in [[NeuroDesk]] cloud pipelines [5]. For researchers working with clinical data from hospital scanners, PyDICOM provides the essential bridge between proprietary vendor DICOM implementations and the open-source analysis ecosystems centered around tools like [[nilearn]], [[mne-python]], and TVB.

## Key Papers

- Mason, D. (2006). PyDICOM: A Pure Python DICOM Player. Python Papers Repository.
- Larobina, M., & Murino, L. (2014). Medical Image File Formats. Journal of Digital Imaging, 27(2), 201-206.
- Gorgolewski, K., et al. (2016). BIDS: A Unified Format for Structural, Functional, and Diffusion MRI Data. Frontiers in Neuroinformatics.

## References

1. PyDICOM Documentation. https://pydicom.org/
2. ISO 12052:2017. Health Informatics — Digital Imaging and Communication in Medicine (DICOM) Including Workflow and Data Management.
3. National Institute of Standards and Technology. (2015). DICOM Standard Reference. NISTauthors.library.nist.gov.
4. Brett, M., et al. (2020). nibabel: Accessing neuroimaging data in Python. Journal of Open Source Software, 5(54), 2432.
5. Kpeas, J., et al. (2021). NeuroDesk: Flexible Framework for Neuroimaging Data Analysis. Frontiers in Neuroinformatics.