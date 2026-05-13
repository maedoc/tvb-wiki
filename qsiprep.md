---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/Renton2024.md
- raw/papers/semanticscholar-deecd9987645.md
tags:
- software-bids
- neuroimaging-dti
- preprocessing
- neuroimaging-fmri
- quality-control
title: QSIprep
type: entity
updated: '2026-05-13'
---

# QSIprep

**QSIprep** is a [[bids]]-App for preprocessing and reconstructing [[diffusion-mri]] (dMRI) data. It provides a standardized, reproducible pipeline for quality control, preprocessing, and reconstruction of diffusion-weighted imaging data within the Brain Imaging Data Structure (BIDS) framework.

## Overview

The [[diffusion-mri|diffusion MRI]] processing pipeline spans multiple stages, beginning with preprocessing and local fiber reconstruction before advancing to [[tractography]] and post‑processing of tractograms [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]. Within this landscape, QSIprep functions as a tool for preprocessing diffusion‑weighted imaging data, included alongside [[mrtrix3]] and dsistudio in the Neurodesk platform's diffusion MRI tool suite [[raw/papers/Renton2024.md|Renton et al. (2024)]]. The software performs first‑level preprocessing of diffusion‑weighted images and generates parametric maps and connectivity matrices [[raw/papers/semanticscholar-deecd9987645.md|Asay et al. (2025)]], and these outputs feed directly into structural [[connectome]] analyses for whole‑brain network modeling [[raw/papers/Renton2024.md|Renton et al. (2024)]]. Its outputs further support downstream data management and integration with quality‑assurance pipelines [[raw/papers/semanticscholar-deecd9987645.md|Asay et al. (2025)]].

QSIprep participates in a broader movement toward reproducible, containerized neuroimaging analysis. The Neurodesk platform demonstrated empirically that containerized software eliminates inter‑computer differences that occur with locally installed tools, establishing a foundation for consistent preprocessing outcomes across heterogeneous hardware [[raw/papers/Renton2024.md|Renton et al. (2024)]]. QSIprep is one of more than one hundred neuroimaging applications accessible through this portable environment, which supports analysis on personal workstations, high‑performance computers, and cloud infrastructure [[raw/papers/Renton2024.md|Renton et al. (2024)]]. Its preprocessed diffusion outputs serve as critical inputs for whole‑brain network simulators such as [[the-virtual-brain|TVB]], where they are transformed into structural connectivity matrices for large‑scale brain modeling [[raw/papers/Renton2024.md|Renton et al. (2024)]]. By operating within containerized platforms alongside companion preprocessors, QSIprep functions as a reproducible bridge between raw dMRI acquisitions and downstream [[connectome]] modeling workflows [[raw/papers/Renton2024.md|Renton et al. (2024)]][[raw/papers/semanticscholar-deecd9987645.md|Asay et al. (2025)]].

## History and Motivation

Diffusion-weighted magnetic resonance imaging (dMRI) has become the primary method for noninvasively studying white matter organization in the human brain. However, the rapid advancement of dMRI technology has produced a fragmented landscape of acquisition schemes, analysis approaches, and file formats that are frequently incompatible with one another (Cieslak et al., 2021). Most research teams tend to use a limited set of methods, failing to capitalize upon the complementary capabilities of different software tools. This motivated the development of QSIprep as a unified platform that could handle diverse sampling schemes while leveraging the strengths of multiple software packages.

QSIprep was developed by Matthew Cieslak and colleagues at the University of Pennsylvania, with substantial contributions from researchers at multiple institutions including the University of Pittsburgh, Indiana University, Stanford University, and the University of Washington (Cieslak et al., 2021). The software was first publicly released in December 2019, and the platform was formally described in a publication in Nature Methods in 2021. The development model adopted the framework and philosophy established by fMRIPrep, extending the BIDS-App paradigm to the diffusion MRI domain.

## Design Philosophy

The core design philosophy of QSIprep emphasizes software interoperability and adaptive pipeline construction. Rather than implementing its own algorithms for every processing step, QSIprep draws upon a diverse set of established software suites—including FSL, DSI Studio, DIPY, ANTs, and MRtrix3—to capitalize upon their complementary strengths (Cieslak et al., 2021). The pipeline automatically configures itself based on the metadata recorded in BIDS, allowing a single command to produce appropriate preprocessing for nearly any dMRI acquisition scheme.

A key innovation of QSIprep is its ability to process both shelled sampling schemes (single-shell DTI and multi-shell acquisitions) and non-shelled schemes (such as Diffusion Spectrum Imaging and compressed-sensing DSI). For non-shelled sequences, QSIprep implements the SHORELine algorithm, a novel head motion estimation method based on 3dSHORE q-space interpolation. This dramatically increases the accessibility of advanced non-shelled acquisition sequences by allowing standard analytic methods to be applied where previously only custom pipelines could be used.

## Preprocessing Features

QSIprep provides comprehensive preprocessing that addresses the unique challenges of dMRI data. The pipeline includes MP-PCA denoising using random matrix theory principles, Gibbs unringing for artifact correction, and bias field correction. Head motion correction, eddy current correction, and susceptibility distortion correction are combined into a unified workflow, as these operations are intrinsically interdependent (Cieslak et al., 2021).

Distortion correction can be performed using BIDS-defined fieldmaps with FSL's TOPUP and eddy tools, or through experimental fieldmapless SyN-based registration when no fieldmaps are available. For single-shell and multi-shell data, FSL's eddy is used, while the SHORELine method handles DSI and compressed-sensing acquisitions. The final resampling combines all transformations—motion correction, eddy current correction, distortion correction, and registration to the T1w image—into a single interpolation step to minimize image smoothing artifacts.

## Reconstruction and Connectivity

Beyond preprocessing, QSIprep includes curated reconstruction workflows that consume preprocessed data and implement advanced reconstruction methods. These workflows support DTI, Diffusion Kurtosis Imaging (DKI), Constrained Spherical Deconvolution (CSD), and NODDI models. The platform provides outputs from MRtrix3, DSI Studio, and DIPY in standardized formats, facilitating direct comparison between reconstruction methods.

For whole-brain structural connectomics, QSIprep generates tractography outputs and connectivity matrices using multiple algorithms. The software supports several popular parcellation schemes including the Schaefer atlases (100, 200, and 400 parcels), Brainnetome atlas, AICHA, Gordon, AAL, and Power atlases. Connectivity matrices are stored in HDF5 format, ensuring they are directly comparable across participants and methods.

## Quality Control and Reporting

QSIprep generates comprehensive HTML reports at each preprocessing step, providing visual "before vs. after" comparisons that enable rapid Quality Assurance assessment. The reports include head motion metrics, framewise displacement summaries, and outlier volume detection. These quality control outputs help identify subjects with poor data quality before downstream analyses such as connectome construction.

The software employs continuous integration testing and maintains an open development environment, enabling rapid bug detection and integration of feature requests from its user base (Cieslak et al., 2021). QSIprep is distributed as both a Python package and as Docker containers, ensuring reproducibility across computing environments.

## Relationship to TVB

QSIprep serves as a critical preprocessing tool for TVB [[connectome]] construction workflows. The software generates motion-corrected, distortion-corrected DWI series that feed into tractography pipelines using [[mrtrix3]] and [[dipy]]. Quality control outputs help identify subjects with poor data quality before connectome construction begins, preventing the propagation of artifacts into downstream analyses. BIDS-structured outputs facilitate integration with TVB's data management workflows, and QSIprep can be used alongside [[fmriprep]] for multi-modal preprocessing in TVB pipelines.

## Software Ecosystem

QSIprep exists within a broader ecosystem of diffusion MRI processing tools. The [[scilpy]] toolbox provides additional Python-based scripts for dMRI and tractography analysis, complementing QSIprep's capabilities with specialized post-processing and bundle analysis features (Renauld et al., 2026). Alternative automated pipelines such as [[tractoflow]] offer similar end-to-end processing, while the Neurodesk platform includes QSIprep as part of its containerized neuroimaging environment for reproducible analysis (Renton et al., 2024).

| Tool | Role in Ecosystem |
|------|-------------------|
| [[fmriprep]] | Companion BIDS-App for functional MRI preprocessing |
| [[mrtrix3]] | Tractography using QSIprep outputs |
| [[dipy]] | Python-based diffusion analysis library |
| [[tractoflow]] | Alternative automated tractography pipeline |
| [[afq]] | Automated fiber quantification |
| [[scilpy]] | Additional dMRI analysis scripts |

## Limitations

Several limitations should be noted when using QSIprep. The software does not currently support double diffusion encoding q-space imaging or gradient tensor imaging, as these scanning sequences are not widely used, not supported by BIDS, and lack open preprocessing software (Cieslak et al., 2021). Additionally, the reconstruction workflows implement current best practices but do not claim optimality for any particular method—the question of optimality in reconstruction and tractography remains an open research area. Users should also note that preprocessing necessarily introduces some spatial smoothing, though QSIprep has been shown to produce less blur than many custom pipelines designed for specific acquisition schemes.

## References

- Cieslak, M., Cook, P.A., He, X., Yeh, F.C., Dhollander, T., Adebimpe, A., ... & Satterthwaite, T.D. (2021). QSIPrep: an integrative platform for preprocessing and reconstructing diffusion MRI data. Nature Methods, 18(7), 775-778.
- Renton, A.I., Dao, T.T., Johnstone, T., Civier, O., Sullivan, R.P., White, D.J., ... & Bollmann, S. (2024). Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging. Nature Methods, 21(5), 804-808.
- Renauld, E., Boré, A., Poirier, C., Valcourt-Caron, A., Karan, P., Théberge, A., ... & Descoteaux, M. (2026). Tractography analysis with the scilpy toolbox. Aperture Neuro.