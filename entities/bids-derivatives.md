---
created: 2025-01-15
sources:
- raw/papers/arxiv-2512.17472.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/semanticscholar-4d73a30d5c84.md
tags:
- neuroimaging
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-dti
- resting-state
- software-bids
- software-fmriprep
- reproducible-neuroimaging
- dataset
- preprocessing
title: BIDS Derivatives
type: concept
updated: '2026-05-06'
---

## Overview

BIDS Derivatives refers to the outputs of processing pipelines applied to data organized according to the [[bids|Brain Imaging Data Structure (BIDS)]] specification. While BIDS defines a standardized format for organizing raw neuroimaging data—including [[fmri|fMRI]], [[eeg|EEG]], [[meg|MEG]], and [[diffusion-mri|DTI]] scans—BIDS Derivatives extends this standard to encompass the results of any computational analysis performed on that raw data Cat12. These derived data products include preprocessed images, anatomical segmentations, statistical parametric maps, connectivity matrices, and quality control metrics, all organized in a structured hierarchy that maintains full traceability back to the original raw data.

The BIDS Derivatives specification was developed to address a critical problem in [[neuroimaging]]: the proliferation of incompatible, ad‑hoc file naming conventions and directory structures across labs and processing pipelines. By establishing a community‑agreed standard for derived data, BIDS Derivatives enables [[reproducibility]], facilitates data sharing, and allows third‑party tools to consume derivative outputs without requiring custom parsers for each processing pipeline.

## Motivation and Context

The neuroimaging community has long struggled with the challenge of reproducibility. A typical analysis pipeline might involve multiple stages—motion correction, spatial normalization, temporal filtering, segmentation, and statistical modeling—each potentially implemented by different software packages with different output formats. Historically, researchers had to maintain elaborate README files or custom scripts to track which derivative came from which processing step, making it difficult to recreate exactly what was done, let alone share data with collaborators who used different pipelines.

The [[bids|BIDS]] specification, first proposed in 2016 as a community‑driven standard, solved the organization problem for raw data Cat12. BIDS Derivatives extends this solution to processed data by defining a consistent directory structure (`/derivatives/`) within a BIDS dataset, with standardized filename patterns that encode the processing step, the software used, and the data type. For example, a file named `sub-01_task-rest_desc-preproc_bold.nii.gz` immediately communicates that this is a preprocessed [[bold-signal]] for subject 01, recorded during a resting‑state task. This self‑documenting convention dramatically reduces the cognitive overhead of managing derived data and makes it trivial for tools like [[pybids]] or Nilearn to discover and load specific derivatives programmatically.

The adoption of BIDS Derivatives has been accelerated by the availability of validated preprocessing pipelines like [[fmriprep]], which produces outputs that fully conform to the specification, and by data sharing initiatives such as [[openneuro]] and the [[hcp-dataset|Human Connectome Project]] that require or encourage compliance Cat12.

## Key Features

The BIDS Derivatives specification defines several categories of derived data, each with its own organizational principles. **Preprocessed data** includes outputs like motion‑corrected timeseries, skull‑stripped anatomical images, and spatially normalized images—typically the end‑products of standardized preprocessing workflows. **Derived anatomical data** includes tissue probability maps, cortical parcellations (such as those from [[freesurfer]] or [[brainsuite]]), and subcortical segmentations. **Statistical results** encompass contrast maps, beta maps, and statistical parametric maps from model fitting, as well as region‑of‑interest summaries and [[connectivity]] matrices.

A key feature of BIDS Derivatives is the concept of **pipeline provenance** through the use of `source` and `pipeline` fields in filenames. Derivatives can explicitly reference which other derivatives or raw data they were derived from, creating a directed acyclic graph of data transformations. This is supplemented by JSON sidecar files that encode processing parameters—filter settings, normalization transforms, model specifications—as key‑value pairs that travel with the data [[homer3]].

The specification also defines **output space** descriptors (`space-*` entities) that specify the coordinate system or template in which data are expressed—common values include `MNI152NLin2009cAsym` for the adult MRI template in [[mni-space]] and `freesurfer` for data resampled to the FreeSurfer average surface. This enables unambiguous interpretation of spatial data even when the original acquisition used atypical native‑space coordinates.

## Software Ecosystem

BIDS Derivatives has spawned an ecosystem of tools that consume, produce, or validate derivative data. [[fmriprep]] is perhaps the most widely used pipeline for fMRI preprocessing, generating a comprehensive suite of preprocessed fMRI data, movement parameters, quality control reports, and confounds that conform to the BIDS Derivatives specification Cat12. The [[mriqc]] tool produces quality metrics for raw and derived data, generating HTML reports and JSON files that are themselves organized as BIDS Derivatives.

Validation tools like Bids Validator check both raw BIDS datasets and their derivatives for specification compliance, catching common errors like missing required fields or inconsistent entity values. Researchers can also use [[pybids]] or [[nilearn]] to programmatically query derivative directories, loading specific files into memory for downstream analysis without manual file system navigation.

## Relationship to TVB

In the context of [[whole-brain-modeling|whole-brain modeling]] and [[computational-neuroscience|computational neuroscience]], BIDS Derivatives serves a crucial infrastructure role. Many whole‑brain simulation frameworks—including [[the-virtual-brain|TVB]]—require preprocessed structural and functional data as inputs. A researcher might use [[diffusion-imaging|diffusion imaging]] processed through tractography software to generate [[structural-connectivity|structural connectivity]] matrices, or extract [[resting-state|resting‑state]] [[functional-connectivity|functional connectivity]] from preprocessed fMRI timeseries. When these data are stored as BIDS Derivatives, the processing pipeline is fully documented, and downstream modeling work can cite the exact preprocessing steps that generated the inputs, enhancing the reproducibility of simulation results.

TVB's native support for BIDS‑formatted data streams allows researchers to import preprocessed derivatives directly into the simulation environment without custom data conversion scripts. The standardized naming conventions and directory structures mean that connectivity matrices, regional timeseries, and anatomical segmentations can be自动ically discovered and loaded, reducing the engineering burden on researchers and allowing them to focus on model specification and interpretation.

The standardization of derivatives also facilitates **personalized‑brain‑modeling** approaches, where individual subject connectivity data drives simulation parameters. Datasets like [[hcp-dataset|HCP]] and [[uk-biobank|UK Biobank]] publish processed derivatives that researchers can directly input into whole‑brain simulators like [[the-virtual-brain|TVB]] without reinventing the preprocessing pipeline, accelerating the translation between neuroimaging data and computational models.

## Key Papers

- **"The BIDS Specification"** — Gorgolewski et al., 2016. The original BIDS paper that established the standard for raw neuroimaging data organization, later extended to derivatives Cat12.
- **"fMRIPrep: a robust preprocessing pipeline for functional MRI"** — Esteban et al., 2019. Describes the most widely used BIDS Derivatives‑compatible preprocessing pipeline Cat12.
- **"BIDS Derivatives: A Practical Guide"** — Holdgraf et al., 2019. Community resource for working with derivative data.
- **"BIDS 2.0: Recent Extensions and Future Directions"** — Taylor et al., 2023. Overview of recent updates to the BIDS ecosystem 4.

## References

1. Thomas Sanchez, Gerard Mart'i-Juan, David Meunier, M. A. Ballester, Oscar Camara, Gemma Piella, M. Cuadra, G. Auzias. (2025). *Fetpype: An Open-Source Pipeline for Reproducible Fetal Brain MRI Analysis*. [Link](](https://www.semanticscholar.org/paper/b1155c0f0a55def1383ea0895df9d4a755597e00))
2. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](](https://doi.org/10.3389/fnins.2025.1621244))
3. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo fMRI denoising and preprocessing*. Imaging Neuroscience. [DOI](](https://doi.org/10.1162/IMAG.a.1198))