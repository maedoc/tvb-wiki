---
title: ABCBIDS
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-bids, dataset, neuroimaging-fmri, neuroimaging-dti, database-hcp, software-fsl, software-freesurfer]
sources: []
---

# ABCBIDS

## Overview

ABCBIDS refers to the ecosystem of tools and data formats developed around the Adolescent Brain Cognitive Development (ABCD) Study for converting, validating, and processing neuroimaging data in the Brain Imaging Data Structure (BIDS) standard. While not a single unified software package, the term encompasses the DICOM-to-BIDS conversion wrappers, preprocessing pipelines, and derivative datasets that together form a standards-compliant neuroimaging processing framework widely used in developmental neuroscience research. The ABCD Study itself is the largest longitudinal study of brain development in the United States, following approximately 12,000 children from ages 9-10 into adulthood, with comprehensive neuroimaging, cognitive, behavioral, and genetic assessments.

The ABCBIDS ecosystem addresses a critical challenge in large-scale neuroimaging: converting heterogeneous scanner-specific DICOM data into a standardized, interoperable format that enables reproducible analysis across sites and scanners. The ABCD Study collected data from 21 sites using three major scanner vendors (Siemens, Philips, and General Electric), making standardization essential for meaningful multi-site analysis. The tools developed for this purpose have since been adopted more broadly in the neuroimaging community.

## Relationship to TVB

[[The Virtual Brain]] (TVB) leverages neuroimaging datasets like those produced by the ABCBIDS ecosystem in several important ways for [[whole-brain modeling]] and [[computational neuroscience]] research. The structural [[connectivity]] matrices derived from [[diffusion-imaging]] (DWI) data—which ABCBIDS processes through pipelines like QSIPrep and QSIRecon—form the anatomical foundation for TVB's [[connectome]]-based simulations. Similarly, the preprocessed functional MRI data (both task-based and [[resting-state]]) provide empirical constraints for model parameter estimation and validation.

The ABCC derivatives include [[functional-connectivity]] matrices computed from resting-state fMRI at multiple thresholds and parcellation schemes (Gordon2014, HCP2016, Power2011, Yeo2011), which TVB researchers can use directly as empirical functional networks for comparison with simulated dynamics. The individual-level processing outputs also enable population-level analyses of brain [[network-dynamics]], supporting TVB's focus on [[personalized-brain-modeling]] approaches that tailor [[neural-mass-models]] to individual subject connectomes.

## Key Tools and Components

### ABCD DICOM to BIDS Converters

The primary conversion tools in the ABCBIDS ecosystem include `abcd-dicom2bids` and `abcc_dicom2bids_s3`, both developed by the DCAN Labs at Oregon Health & Science University (OHSU). These Python-based wrappers orchestrate the multi-step process of downloading ABCD Study DICOM data from the NIMH Data Archive (NDA), performing quality control filtering based on the FastTrack QC spreadsheet, converting DICOMs to NIfTI files using [[dcm2niix]] (by Chris Rorden's Lab), restructuring the output into BIDS-compliant directory structure using [[Dcm2Bids]], and finally running the official BIDS validator to ensure compliance.

A notable feature of the conversion process is the optimal spin echo field map selection algorithm. Because field maps are highly susceptible to motion artifacts and can substantially impact distortion correction quality, the wrappers select the field map pair with the least variance from the registered group average for each subject's session. The chosen pair is then associated with all anatomical and functional scans via the `IntendedFor` field in the JSON sidecar files, following BIDS specification requirements. This automated selection substantially improves preprocessing robustness compared to manual selection.

### ABCD-HCP BIDS Pipeline

The ABCD-HCP pipeline is a BIDS App—a containerized software package that takes BIDS-formatted input and produces BIDS-compliant derivatives with minimal user configuration. Built upon the [[Human Connectome Project]]'s minimal preprocessing pipeline (Glasser et al., 2013), it outputs preprocessed MRI data in both volume (NIfTI) and surface (CIFTI/GIFTI) spaces. The pipeline is available as both Docker and Singularity images, facilitating deployment across different computing environments including high-performance computing clusters.

The pipeline consists of nine processing stages: PreFreeSurfer (gradient distortion correction, brain extraction, T1w/T2w registration), FreeSurfer (segmentation, cortical surface reconstruction), PostFreeSurfer (CIFTI generation, atlas registration), FMRIVolume (motion correction, distortion correction using [[FSL]]'s topup, volume registration to MNI), FMRISurface (projection to CIFTI grayordinates space), DCANBOLDProcessing (nuisance regression, motion censoring, bandpass filtering), ExecutiveSummary (HTML visual quality control), CustomClean (removal of non-critical outputs), and FileMapper (organizing outputs into valid BIDS derivatives).

A distinguishing feature of the ABCD-HCP pipeline is its robust handling of scanner vendor differences. Siemens, Philips, and General Electric scanners produce data with different characteristics—for example, GE anatomical images lack scanner-based intensity normalization. To address this, the pipeline incorporates [[ants]] (Advanced Normalization Tools) denoising and N4 bias field correction in the PreFreeSurfer stage, and uses [[ants]] diffeomorphic registration instead of [[FSL]]'s FNIRT for improved atlas alignment across vendors. Additionally, a respiratory motion filter addresses artifacts specific to multiband acquisition, with bandstop filtering applied to motion parameters in the 18.582–25.726 breaths-per-minute range (the interquartile range for adolescent respiratory rates).

## ABCC Dataset

The ABCD-BIDS Community Collection (ABCC) is a curated release of ABCD Study neuroimaging data following BIDS standards and the NMIND reproducibility framework. As of release 3.1.0, the dataset includes approximately 11,751 participants with ABCD-HCP derivatives and 8,852 participants with QSIPrep derivatives from the baseline session, with corresponding numbers for the 2-year, 4-year, and 6-year follow-up visits.

The ABCC derivatives span multiple modalities and processing streams. For structural MRI, FreeSurfer 5.3.0-HCP outputs include segmentation statistics and surface morphometrics. For functional MRI, the ABCD-HCP pipeline produces both volume-based (processed with FSL) and surface-based (CIFTI format) outputs, including connectivity matrices at multiple frame-displacement thresholds. For diffusion MRI, QSIPrep provides preprocessed DWI data with options like Gibbs ringing removal and multiple phase-encoding direction handling, while QSIRecon generates various diffusion models including DTI, DKI, NODDI, and MSMT tractography.

A distinctive aspect of ABCC is its emphasis on quality control at multiple stages. Raw data quality is ensured through DAIRC (Data Analysis and Informatics Resource Center) operator QC, while processed data quality is assessed through BrainSwipes, a community-driven visual QC platform. The collection also provides versioned releases with detailed changelogs, enabling reproducible science—researchers can trace exactly which pipeline version and parameter settings produced specific derivatives.

## Related Software and Pipelines

The ABCBIDS ecosystem integrates with numerous established neuroimaging tools. For preprocessing, [[fMRIPrep]] provides an alternative functional MRI processing stream that ABCD investigators have also applied to the data, with derivatives available for the baseline sample. [[QSIPrep]] serves as the primary diffusion MRI preprocessing pipeline, analogous to fMRIPrep but specialized for DWI data. For quality control, the collection includes outputs from tools like [[MRIQC]] for raw data and custom QC visualizations in the ExecutiveSummary HTML reports.

The pipeline dependencies include [[FreeSurfer]] (for segmentation and surface reconstruction), [[FSL]] (for topup, FLIRT, and general image processing), and [[ants]] (for registration and normalization). The DICOM handling relies on [[dcm2niix]] for conversion and DCMTK for metadata extraction. The entire ecosystem uses [[Docker]] and Singularity containers for reproducibility and portability.

## Key Papers

The foundational methodology papers for the ABCBIDS ecosystem include Feczko et al. (2021), which describes the ABCD-BIDS Community Collection and its processing standards in detail. The pipeline methodology builds on Glasser et al. (2013) for the HCP minimal preprocessing approach, while the respiratory motion filter is validated in Fair et al. (2019). More recent methodological advances appear in Cieslak et al. (2021) for QSIPrep and in the NMIND framework paper (Kiar et al., 2023).

## Related Pages

- [[bids]] — The underlying data standard
- [[bids-derivatives]] — BIDS-compliant derivative outputs
- [[human-connectome-project]] — Original pipeline source
- [[freesurfer]] — Segmentation and surface processing
- [[fsl]] — Volume-based image processing
- [[ants]] — Advanced normalization tools
- [[qsiprep]] — Diffusion MRI preprocessing
- [[fmriprep]] — Functional MRI preprocessing
- [[diffusion-imaging]] — DWI acquisition and processing
- [[resting-state]] — Resting-state fMRI methodology
- [[functional-connectivity]] — Connectivity analysis
- [[connectome]] — Structural connectivity frameworks
- [[whole-brain-modeling]] — TVB modeling approaches