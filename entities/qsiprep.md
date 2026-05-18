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
updated: '2026-05-07'
---
# QSIprep

**QSIprep** is a [[bids]]-App for preprocessing and reconstructing [[diffusion-mri]] (dMRI) data. It provides a standardized, reproducible pipeline for quality control, preprocessing, and reconstruction of diffusion-weighted imaging data within the Brain Imaging Data Structure (BIDS) framework.

## Overview
The [[diffusion-mri|diffusion MRI]] processing pipeline spans multiple sequential stages, beginning with preprocessing and local fiber reconstruction before advancing to [[tractography]] and connectivity analysis [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]. Within this landscape, QSIprep functions as a diffusion MRI analysis instrument included alongside [[mrtrix3]] and similar tools in the Neurodesk platform's comprehensive neuroimaging suite [[raw/papers/Renton2024.md|Renton et al. (2024)]]. The Neurodesk platform demonstrated empirically that containerized software eliminates inter‑computer differences that occur with locally installed tools, establishing a foundation for consistent preprocessing outcomes across heterogeneous hardware [[raw/papers/Renton2024.md|Renton et al. (2024)]]. QSIprep is one of more than one hundred neuroimaging applications accessible through this portable environment, which supports analysis on personal workstations, high‑performance computers, and cloud infrastructure [[raw/papers/Renton2024.md|Renton et al. (2024)]]. The outputs from diffusion MRI pipelines such as QSIprep feed directly into structural [[connectome]] matrices that serve as inputs for network‑based whole‑brain simulators such as [[the-virtual-brain|TVB]], bridging raw diffusion‑weighted data and large‑scale brain network modeling [[raw/papers/Renton2024.md|Renton et al. (2024)]].

This diffusion‑focused role operates within a broader preprocessing landscape that also includes structural MRI pipelines. While deepmriprep leverages deep neural networks to perform voxel‑based morphometry preprocessing on T1‑weighted images, illustrating the complementary specialization of modern neuroimaging tools [[raw/papers/semanticscholar-a0cce22e2ffc.md|Fisch et al. (2026)]], the dMRI pipeline encompasses sequential stages of denoising, spatial registration, and local fiber reconstruction that prepare data for subsequent tractography and connectivity analyses [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]. By functioning within reproducible, containerized platforms alongside companion instruments, QSIprep serves as a bridge between raw dMRI acquisitions and downstream connectome modeling workflows.
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
