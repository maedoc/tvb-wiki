---
created: 2026-04-20
sources:
- raw/papers/jordan-2018.md
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2604.03619.md
- raw/papers/gorgolewski-2016.md
tags:
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- software-neuroimaging
- data-standard
- neuroimaging-dti
title: Brain Imaging Data Structure (BIDS)
type: concept
updated: '2026-05-07'
---

The Brain Imaging Data Structure (BIDS) is a **standard specification for organizing neuroimaging datasets** that enables reproducible, tool-independent data sharing across the [[computational-neuroscience]] community. BIDS defines a hierarchical file structure and naming convention for brain imaging data, along with metadata specifications in JSON sidecar files that capture acquisition parameters, processing history, and subject metadata. The specification has become the de facto standard for data sharing in neuroimaging, supported by over 200 software tools and adopted by major data repositories including the [[human-connectome-project]] (HCP), [[openneuro]], and UK Biobank (which supports BIDS as one of several acceptable formats for data submission) [@raw/papers/jordan-2018].

## Motivation and Background

Prior to BIDS, [[neuroimaging]] datasets were organized in ad hoc, lab-specific conventions that varied dramatically in structure, naming conventions, and metadata documentation. This heterogeneity created substantial friction when attempting to share data between groups, reuse analysis pipelines across datasets, or aggregate data for meta-analyses. Researchers spent considerable time writing custom preprocessing scripts to adapt each new dataset to their pipeline, and the lack of standardized metadata made it difficult to reproduce analyses or compare findings across studies. BIDS emerged from the realization that the long-term sustainability of neuroimaging research depended on adopting community-wide data standards analogous to those used in other scientific disciplines.

The BIDS specification was first proposed in 2016 by a consortium of neuroimaging researchers including Cyril Gorgolewski and collaborators, building on earlier efforts to standardize data formats [@raw/papers/sanz-leon-2013]. The initial motivation was to create a machine-readable specification that would allow automated preprocessing pipelines to discover, validate, and process neuroimaging datasets without manual intervention. Over time, BIDS has expanded beyond its original focus on MRI to encompass electroencephalography (EEG), magnetoencephalography (MEG), positron emission tomography (PET), intracranial EEG, and other neuroimaging modalities.

## Technical Specification

A BIDS-compliant dataset follows a directory hierarchy that encodes the imaging modality, subject identity, session, and data type. The [[root]] directory contains a `dataset_description.json` file with metadata about the study, and subdirectories organize data by modality (anat, func, dwi, eeg, meg, pet) and optionally by processing step. File names follow a strict pattern that includes the modality, subject identifier, session (if applicable), acquisition label, and suffix indicating the data type. For example, a subject's [[resting-state|resting-state fMRI]] scan might be located at `sub-01/func/sub-01_task-rest_bold.nii.gz`, with corresponding JSON metadata at `sub-01/func/sub-01_task-rest_bold.json`.

The JSON sidecar files capture acquisition parameters essential for preprocessing and analysis, including repetition time (TR), echo time (TE), flip angle, voxel dimensions, and phase encoding direction for MRI data. These files may also contain custom fields specific to a given study or acquisition protocol. BIDS also defines extensions for derived data (processed through a pipeline) through the [[bids-derivatives]] specification, which maintains provenance information linking results back to their source data.

### Key Design Principles

BIDS is designed around several core principles that have contributed to its widespread adoption. First, the specification is human-readable—while automated tools can parse the structure, researchers can also navigate datasets manually. Second, BIDS is intentionally restrictive, specifying a limited set of allowed structures rather than accommodating every possible variation. This constraint simplifies validation and tool development. Third, the specification is extensible through "extensions" that add new modalities or data types while maintaining backward compatibility. The BIDS validator is a crucial tool that checks datasets for compliance with the specification, catching organizational errors before they propagate through analysis pipelines.

## Relationship to Whole-Brain Modeling

In the context of [[whole-brain-modeling]] and [[the-virtual-brain]], BIDS plays an important role in the data preprocessing pipeline that precedes simulation. TVB and similar simulators require structural connectivity matrices derived from [[diffusion-mri]] tractography as primary inputs. When researchers share datasets in BIDS format, the standardized directory structure and metadata make it straightforward to extract diffusion-weighted images (DWI) and compute [[structural-connectivity]] matrices using tools like [[mrtrix3]], [[tractography]], or [[dipy]]. The metadata in BIDS JSON sidecar files captures the acquisition parameters needed to properly preprocess DWI data—such as b-values, b-vectors, and phase encoding information—ensuring consistent processing across subjects and studies.

BIDS also facilitates the integration of functional neuroimaging data for model validation. Resting-state fMRI data organized in BIDS format can be used to compute [[functional-connectivity]] matrices that serve as empirical benchmarks for comparing simulated brain dynamics against observed [[brain-dynamics]]. Researchers can use tools like [[pybids]] to programmatically query BIDS datasets, extracting specific runs, sessions, or modalities for analysis without manual file navigation. This programmatic access is particularly valuable when constructing personalized brain models that require processing multiple subjects or longitudinal sessions.

## Ecosystem and Tools

The BIDS ecosystem includes numerous tools that operate on BIDS datasets. [[pybids]] is a Python library that provides programmatic access to BIDS datasets, enabling queries for specific subjects, sessions, or file types. [[bidskit]] is a command-line toolkit for converting raw DICOM data to BIDS format during initial data organization. [[bids-apps]] are dockerized neuroimaging pipelines that accept BIDS datasets as input, implementing standardized processing workflows that can be run reproducibly across computing environments. Tools like [[mne-bids]] and [[dcm2niix]] bridge between specific acquisition formats and the BIDS specification.

Several major preprocessing pipelines expect BIDS-formatted input, including [[fmriprep]] for fMRI, [[qsiprep]] for diffusion MRI, and [[aslprep]] for arterial spin labeling. These pipelines produce [[bids-derivatives]] outputs that maintain the BIDS structure while documenting the processing steps applied. This end-to-end standardization—from raw acquisition through preprocessing to analysis—has substantially improved reproducibility in neuroimaging research.

## Related Concepts

BIDS interacts with several related standards and tools in the neuroimaging ecosystem. [[nipype]] provides a workflow system that can operate on BIDS datasets, connecting different processing tools into reproducible pipelines. [[neurovault]] serves as a repository for statistical maps and parcellations that often originate from BIDS-analyzed datasets. The relationship between BIDS and other data standards reflects a broader trend toward formalization in neuroimaging, supporting the goals of open science and reproducible research.

## References

1. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2018.00002))
2. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
3. Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon. (2026). *Can Natural Image Autoencoders Compactly Tokenize [[fmri]] Volumes for Long-Range Dynamics Modeling?*. [Link](](https://arxiv.org/abs/2604.03619))