---
title: ABCBIDS
created: 2025-01-01
updated: 2026-05-04
type: entity
tags: [software-bids, neuroimaging-fmri, pipeline, bids-apps, preprocessing]
sources: [raw/papers/arxiv-1234.56789.md]
---

# ABCBIDS (ABCD-HCP BIDS Pipeline)

## Overview

ABCBIDS, more precisely known as the ABCD-HCP BIDS fMRI pipeline or abcd-hcp-pipeline, is a BIDS App designed for processing BIDS-formatted MRI datasets using methods from both the Human Connectome Project's minimal preprocessing pipeline and the DCAN Labs resting state fMRI analysis tools. The pipeline outputs preprocessed MRI data in both volume and surface spaces, making it particularly suitable for large-scale developmental neuroimaging studies. Originally developed to process data from the Adolescent Brain Cognitive Development (ABCD) Study, the pipeline has found broader application in pediatric and adult neuroimaging research where robust, scanner-agnostic preprocessing is essential.

The pipeline operates as a containerized application (Docker or Singularity) that takes minimally configured BIDS input and produces thoroughly processed outputs suitable for connectivity analysis, surface-based statistics, and group-level comparisons. Its design philosophy emphasizes minimal user configuration while maintaining flexibility for different acquisition protocols and scanner manufacturers.

## Relationship to TVB

While ABCBIDS is primarily a preprocessing pipeline for fMRI data rather than a [[whole-brain-modeling]] tool, it produces data derivatives that can serve as input to [[the-virtual-brain]] and other large-scale brain simulators. The pipeline's outputs in CIFTI format (dtseries) provide time series data for brain regions defined by various parcellation schemes, which can be extracted and used to calibrate [[neural-mass-models]] or [[whole-brain-modeling]] frameworks. The ABCD-BIDS pipeline's emphasis on producing motion-censored, nuisance-regressed time series makes it particularly useful for generating clean resting-state data needed for [[functional-connectivity]] analyses that inform brain network models in TVB.

Additionally, the pipeline's handling of pediatric data is relevant to [[neurodevelopment]] research, which aligns with TVB's growing interest in developmental brain modeling. The preprocessing outputs can feed into [[personalized-brain-modeling]] workflows where individual connectivity matrices derived from ABCBIDS-processed data are used to constrain model parameters.

## Key Features

The ABCD-HCP BIDS pipeline encompasses several processing stages that transform raw MRI data into analysis-ready derivatives. Each stage serves a distinct purpose in the preprocessing stream, and understanding these stages helps users appreciate the pipeline's capabilities and limitations.

### Stage Overview

The pipeline consists of nine primary stages arranged in a serial workflow. The PreFreeSurfer stage handles anatomical data, performing bias field correction using ANTs and preparing brain-extracted images for FreeSurfer processing. A notable modification from the original HCP pipeline is the use of ANTs for denoising and N4 bias field correction, which significantly improves results for data from GE and Philips scanners that often exhibit higher noise levels and incomplete scanner-side normalization.

The FreeSurfer stage performs standard segmentation, cortical surface reconstruction, and surface registration to the FreeSurfer atlas, largely unchanged from the original HCP minimal preprocessing pipeline. Following this, the PostFreeSurfer stage generates CIFTI surface files and applies surface registration to the Conte-69 template, using ANTs' diffeomorphic registration method which the developers found outperforms FSL's FNIRT-based approach.

The FMRIVolume stage begins functional processing with gradient-nonlinearity distortion correction, motion correction using rigid-body registration to the initial frame, and distortion correction using spin echo field maps with opposite phase encoding directions via FSL's topup. The FMRISurface stage maps the volume time series into CIFTI grayordinates space. Finally, the DCANBOLDProcessing stage applies nuisance regression including global signal regression, white matter and CSF regression, and bandpass filtering between 0.008 and 0.09 Hz, along with motion censoring at a 0.3 mm framewise displacement threshold.

### Respiratory Motion Filtering

A distinctive feature of the ABCD-BIDS pipeline is its respiratory motion filter, developed in response to artifacts observed in multiband fMRI data. The filter removes respiratory-related frequencies (18.582 to 25.726 breaths per minute) from motion realignment parameters before calculating framewise displacement, producing more accurate motion estimates and consequently more appropriate motion censoring decisions. Users processing data with TR ≤ 1.0 seconds are strongly encouraged to apply this filter.

### Parcellated Time Series Generation

The pipeline automatically generates parcellated time series for predefined atlases including Gordon's 333 ROI template, Power's 264 ROI template, Yeo's 118 ROI template, and the HCP's 360 ROI template. These ready-to-use parcellated outputs facilitate downstream connectivity matrix construction and network analysis without additional processing steps.

## Technical Specifications

The pipeline requires BIDS-formatted input data adhering to the BIDS specification version 1.2.0 or later. Required inputs include T1-weighted images, T2-weighted images (optional but recommended for myelin mapping), functional BOLD runs, and spin echo EPI field maps with opposite phase encoding directions for distortion correction. The pipeline outputs data in both volume space (MNI152) and surface space (fsLR32k grayordinates), with CIFTI dtseries files for dense time series and ptseries files for parcellated data.

Computational requirements are substantial: the pipeline typically requires 12GB or more of RAM and can take 24+ hours to process a single subject when run on a single core. Multi-core processing is supported and recommended, with the developers suggesting at least 4 cores for reasonable processing times. The pipeline requires a FreeSurfer license, which users must obtain separately from the FreeSurfer website.

## Alternatives and Context

The ABCD-BIDS pipeline occupies a specific niche in the neuroimaging preprocessing landscape. It is closely related to but distinct from [[fmriprep]] (another BIDS App for fMRI preprocessing) and [[qsiprep]] (for diffusion MRI). While all three are BIDS Apps following similar design principles, ABCD-BIDS includes the DCAN-specific BOLD processing stages focused on motion censoring and nuisance regression that are particularly optimized for pediatric and young adult populations.

The pipeline builds directly upon the [[human-connectome-project]] minimal preprocessing pipelines developed by Glasser et al. (2013), extending them with features tailored to developmental populations and multi-site data. This heritage connects ABCD-BIDS to the broader ecosystem of HCP-style processing tools including those implemented in [[freesurfer]] and [[fsl]].

## Related Software

- [[bids]] - The Brain Imaging Data Structure standard that ABCBIDS inputs must conform to
- [[fmriprep]] - Another BIDS App for fMRI preprocessing, often used for comparison
- [[qsiprep]] - BIDS App for diffusion MRI preprocessing
- [[freesurfer]] - Used internally for cortical reconstruction
- [[fsl]] - Used for registration and distortion correction
- [[connectome-workbench]] - Required for CIFTI file manipulation
- [[dcabids]] - Alternative BIDS conversion tool (mentioned in pipeline documentation)