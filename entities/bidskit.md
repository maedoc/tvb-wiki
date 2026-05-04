---
created: 2026-04-30
sources:
- raw/papers/semanticscholar-d6e43299345d.md
- raw/papers/mijalkov-2017-braph.md
- raw/papers/semanticscholar-a324c47ea982.md
tags:
- software-brain-modeling
- software-bids
title: BIDSkit
type: entity
updated: '2026-05-04'
---

# BIDSkit

## Overview

BIDSkit is a Python-based command-line tool designed to convert raw neuroimaging DICOM data into the [[BIDS]] (Brain Imaging Data Structure) format. Originally developed by Mike Tyszka at Caltech and first released in August 2016 (Tyszka, 2016), bidskit provides a streamlined two-pass conversion workflow that takes advantage of the [[dcm2niix]] DICOM-to-[[nifti]] converter while automating the creation of BIDS-compliant directory structures and JSON sidecar metadata. The tool is distributed via PyPI and Docker, making it accessible across different computing environments without requiring complex dependency management.

## Motivation and Context

The proliferation of [[neuroimaging]] datasets in [[computational-neuroscience]] and [[whole-brain modeling]] research created an urgent need for standardized data organization. Raw MRI scanner output arrives in vendor-specific DICOM formats that are difficult to share, reproduce, and process with automated pipelines. While the BIDS specification defines a rigorous file organization scheme (Gorgolewski et al., 2016), manually converting datasets to comply with this standard is time-consuming and error-prone. BIDSkit emerged as part of a broader ecosystem of DICOM-to-BIDS converters (including [[heudiconv]], [[dcm]], and [[bidscoin]]) offering different tradeoffs between flexibility, automation, and user control. The tool specifically addresses the needs of research labs performing [[fMRI]] and [[structural-connectivity]] studies who require a reproducible pipeline that can handle multiple subjects and sessions while preserving metadata necessary for downstream analysis with tools like [[fmriprep]], [[nilearn]], and [[the-virtual-brain]].

## Key Features

**Two-Pass Conversion Architecture:** BIDSkit employs a deliberate two-stage workflow that separates data organization from conversion. The first pass scans the DICOM directory tree and generates a Protocol_Translator.json file in the code/ subdirectory. This JSON file contains placeholder entries for each discovered imaging series, initially marked with "EXCLUDE_BIDS_Directory" or "EXCLUDE_BIDS_Name" values. Users edit this translator file to specify the desired BIDS directory (anat, func, fmap, dwi), filename suffix (e.g., task-rest_bold, T1w), and intended-for relationships between fieldmaps and their target EPI sequences. The second pass then executes the actual conversion with these specifications, producing the final BIDS hierarchy.

**Session and Subject Management:** The tool supports multi-subject and multi-session datasets, requiring users to organize their source DICOM data in a directory structure with sourcedata/ subdirectories organized by subject ID (e.g., sub-Cc0001) and session names (e.g., ses-first, ses-second). This hierarchical organization maps naturally onto the BIDS subject/session hierarchy and accommodates longitudinal studies common in [[personalized-brain-modeling]] research. A --no-sessions flag allows omission of session directories for single-session studies.

**Metadata Handling:** During conversion, bidskit extracts available metadata from DICOM headers and populates JSON sidecar files accompanying each NIfTI image. These sidecars contain essential acquisition parameters including repetition time (TR), echo time (TE), flip angle, and voxel dimensions. However, the tool deliberately leaves certain BIDS-required files (dataset_description.json, participants.tsv, task event files) as templates that users must complete, encouraging explicit documentation of experimental metadata.

**Docker and Environment Support:** Beyond pip installation, bidskit is available as a Docker container (jmtyszka/bidskit), facilitating deployment on compute clusters and ensuring [[reproducibility]] across platforms. The Docker variant includes all dependencies pre-installed and provides a consistent runtime environment.

## Technical Workflow

The conversion process begins with a sourcedata/ directory containing raw DICOM files organized by subject and session. Bidskit accepts the dataset root directory as input (or uses the current directory if run without arguments). During the first pass, the tool invokes [[dcm2niix]] to convert DICOM images to NIfTI-1 format and creates the Protocol_Translator.json mapping file. Users then customize this translator to specify how each scanner protocol should map to BIDS datatype directories and filename suffixes. The IntendedFor field allows explicit linking of fieldmap acquisitions to the BOLD or DWI series they are intended to correct, essential for [[diffusion-imaging]] and [[resting-state]] fMRI preprocessing pipelines.

The second pass reads the completed translator and generates the BIDS directory structure in the work/ folder, including derivatives/ for processed outputs. Finally, the tool moves converted files from work/ to the top-level subject directories (sub-*) and updates the participants.tsv file with demographic information extracted from DICOM headers or manually added by users.

## Relationship to Whole-Brain Modeling

BIDSkit plays a supporting but essential role in [[whole-brain-modeling]] workflows by ensuring that [[neuroimaging]] data used as input to models like [[the-virtual-brain]] is properly organized and documented. Whole-brain simulations require structural [[connectivity]] matrices derived from [[diffusion-imaging]] data (processed via [[tractography]] tools like [[mrtrix3]] or [[fsl]]) and functional time series from [[fMRI]] or [[eeg]]. By standardizing data organization, bidskit facilitates reproducibility across modeling studies and enables seamless integration with preprocessing pipelines such as [[fmriprep]] and [[mriqc]] that produce BIDS-compliant derivatives. The standardized format also simplifies data sharing on platforms like [[openneuro]] and supports meta-analyses across multiple datasets.

## Key Papers

- Tyszka, J. M. (2016). bidskit (Version 0.1) [Software]. Caltech. https://github.com/jmtyszka/bidskit
- Gorgolewski, K., Auer, T., Calhoun, V. D., Craddock, R. C., Das, S., Duff, E. P., ... & Poldrack, R. A. (2016). The brain imaging data structure (BIDS): A standard format for organizing output from neuroimaging studies. Frontiers in Neuroinformatics, 10, 9.

## Related Software

* [[dcm2niix]] — DICOM to NIfTI converter that bidskit depends upon
* [[heudiconv]] — Flexible heuristic-based DICOM converter for BIDS
* [[dcm]] — Alternative DICOM to BIDS converter using dcm2niix
* [[bidscoin]] — GUI-enabled BIDS converter supporting multiple modalities
* [[pybids]] — Python API for parsing and manipulating BIDS datasets
* [[fmriprep]] — Preprocessing pipeline accepting BIDS input
* [[nilearn]] — Machine learning and statistical analysis on BIDS data
* [[mne-bids]] — BIDS conversion for EEG/MEG data

## References

1. A. Dehsarvi, Lukas Frontzkowski, Anna Dewenter, Michael Schöll, N. Franzmeier. (2025). *ADprep – A Fully‐Automated Software for Large‐scale Multimodal MRI and PET Imaging Workflows*. Alzheimer's & Dementia. [DOI](https://doi.org/10.1002/alz70856_101373)
2. (authors unknown). *[[braph]]: A Pipeline for Brain Connectivity Analysis*.
3. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2025). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research*. bioRxiv. [DOI](https://doi.org/10.1101/2025.10.06.680781)