---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/Renton2024.md
tags:
- software-bids
- neuroimaging-dti
- preprocessing
- neuroimaging-fmri
- quality-control
title: QSIprep
type: entity
updated: '2026-05-06'
---

# QSIprep

**QSIprep** is a [[bids]]-App for preprocessing and reconstructing [[diffusion-mri]] (dMRI) data. It provides a standardized, reproducible pipeline for quality control, preprocessing, and reconstruction of diffusion-weighted imaging data within the Brain Imaging Data Structure (BIDS) framework.

## Overview

QSIprep provides:
- Automated dMRI preprocessing (denoising, motion correction, eddy current correction, distortion correction)
- Quality control reports and visual summaries
- Integration with multiple reconstruction algorithms (DTI, DKI, CSD, NODDI)
- BIDS-compatible input/output for reproducible workflows
- Head motion and group-level quality control metrics

## Key Features

| Feature | Description |
|---------|-------------|
| **Preprocessing** | MP-PCA denoising, Gibbs unringing, TOPUP/Eddy distortion correction |
| **QC Reports** | Automated HTML reports with interactive visualizations |
| **Reconstruction** | DTI, DKI, CSD, NODDI, and other multi-compartment models |
| **BIDS Integration** | Native BIDS-App compliant input/output |
| **Group Analysis** | Aggregate QC metrics across subjects |

## Relationship to TVB

QSIprep is a key preprocessing tool for TVB [[connectome]] construction:
- Generates preprocessed dMRI data for [[tractography]] pipelines
- Produces motion-corrected DWI series that feed into [[mrtrix3]] and [[dipy]] tractography
- Quality control outputs help identify subjects with poor data quality before connectome construction
- BIDS-structured outputs facilitate integration with TVB's data management workflows
- Can be used alongside [[fmriprep]] for multi-modal preprocessing in TVB pipelines

## Software Ecosystem

- [[fmriprep]] — companion [[fmri]] preprocessing BIDS-App
- [[mrtrix3]] — tractography using QSIprep outputs
- [[dipy]] — Python-based diffusion analysis
- [[tractoflow]] — alternative automated tractography pipeline
- [[afq]] — automated fiber quantification

## References

- QSIprep documentation: https://qsiprep.readthedocs.io/
- Cieslak et al. (2021) — QSIprep: an integrative platform for preprocessing and reconstructing diffusion MRI data