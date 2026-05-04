---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-109de470e443.md
tags:
- software-neuroimaging
- diffusion-imaging
- software-preprocessing
- bids
- neuroimaging-pipeline
- tractography
- diffusion-mri
- structural-connectivity
- white-matter
- preprocessing
title: QSIPrep
type: entity
updated: '2026-04-30'
---

## Overview

QSIPrep is an open-source, [[bids]]-compliant preprocessing pipeline designed specifically for [[diffusion-mri]] (dMRI) data, the [[neuroimaging]] modality that enables reconstruction of [[white-matter]] tracts and quantification of microstructural tissue properties. Developed by the Poldrack Lab at Stanford University and released in 2020 @Cieslak2021QSIPrep, QSIPrep automates the complex sequence of preprocessing [[steps]] required before quantitative analysis of diffusion data, including motion correction, eddy current distortion correction, bias field estimation, and registration to anatomical and standard spaces. The name "QSIPrep" derives from "q-space imaging preprocessing," reflecting its origin in the mathematical framework of diffusion encoding that underlies dMRI acquisition. By providing a robust, containerized solution that produces publication-ready data with minimal manual intervention, QSIPrep has become a foundational tool in the [[connectomics]] and [[whole-brain|whole-brain modeling]] ecosystem, analogous to how [[fmriprep]] transformed the preprocessing of functional MRI data @Gorgolewski2017fMRIPrep.

## Motivation and Context

Diffusion MRI preprocessing presents unique technical challenges that differ substantially from those encountered in other neuroimaging modalities. The acquisition sequence involves repeated application of diffusion-sensitizing gradients along multiple directions, making the data inherently sensitive to subject motion, eddy current distortions induced by the rapidly switching gradient fields, and B0 field inhomogeneities that cause geometric distortions especially in frontal and temporal brain regions @Andersson2016Nonlinear. Historically, researchers spent considerable time manually implementing custom preprocessing workflows using tools like [[dipy]], [[mrtrix3]], [[fsl]], and [[afni]], leading to substantial variability across labs and reduced reproducibility. Studies examining neuroimaging preprocessing pipelines have consistently demonstrated that manual, lab-specific approaches introduce systematic artifacts and batch effects that can obscure genuine biological signals, particularly when comparing connectomes across populations or tracking changes over time.

QSIPrep emerged from the recognition that the diffusion MRI field needed a standardized preprocessing solution comparable to what [[fmriprep]] provided for functional MRI. The project adopted the same design philosophy: full automation with sensible defaults, comprehensive logging and provenance tracking, strict BIDS compliance to enable data sharing, and containerization via [[apptainer]] (formerly Singularity) to ensure computational [[reproducibility]] across different computing environments @Cieslak2021QSIPrep. By automating the most error-prone steps in diffusion preprocessing, QSIPrep enables researchers to focus on scientific questions rather than pipeline engineering, and facilitates direct comparison of results across studies that use the same preprocessing framework.

## Technical Description

QSIPrep implements a comprehensive preprocessing workflow organized into several interconnected stages. The pipeline begins with DICOM to [[nifti]] conversion using [[dcm2niix]], followed by automated quality assessment to identify corrupt volumes or excessive motion. Denoising is performed using Marchenko-Pastur PCA or locally low-rank reconstruction methods implemented in [[dipy]], which exploit the redundancy in multi-shell diffusion data to suppress thermal noise. After denoising, the pipeline applies eddy current and motion correction using FSL's eddy tool @Smith2004Advances, which also models and corrects for susceptibility-derived distortions when reverse-encoded images are available. This "TOPUP" procedure integrates distortion correction with motion estimation to prevent cross-contamination of artifacts @Andersson2016Nonlinear.

The anatomical processing stream within QSIPrep employs [[freesurfer]] for whole-brain segmentation and cortical parcellation, enabling precise registration of diffusion data to anatomical images. The pipeline generates several outputs essential for subsequent analysis: preprocessing derivatives in native diffusion space, warping fields for transformation to standard spaces (MNI152), and orientation vectors (including b-vectors) properly rotated to account for motion and eddy current corrections. For [[tractography]] workflows, QSIPrep can produce preprocessed data in formats compatible with [[mrtrix3]] or other tractography packages, including properly oriented gradient tables and brain masks.

A distinguishing feature of QSIPrep is its handling of multi-shell data, which allows characterization of tissue microstructure at multiple diffusion weightings (b-values). The pipeline supports advanced models including constrained spherical deconvolution (CSD) @Tournier2007Robust, q-ball imaging, and diffusion tensor imaging (DTI), outputting fiber orientation distributions (FODs) that serve as input for probabilistic tractography. The workflow is implemented in Python using [[nipype]] for workflow orchestration, ensuring [[modularity]] and extensibility while maintaining compatibility with the broader Nipype ecosystem of neuroimaging tools.

## Relationship to TVB and Whole-Brain Modeling

In the context of [[whole-brain-modeling]] and [[the-virtual-brain]], QSIPrep plays a critical role in the preparation of structural connectivity data. Whole-brain connectome models require accurate white matter tractography to infer the anatomical pathways through which neural activity propagates between brain regions. The quality of this structural connectome directly impacts the fidelity of simulated brain dynamics, as the connectome serves as the anatomical skeleton upon which [[neural-mass-models]] or [[neural-network]] simulations are run. QSIPrep's preprocessing of diffusion data directly supports the generation of high-quality tractograms using tools like [[mrtrix3-connectome]], which produce connectivity matrices that can be imported into [[the-virtual-brain]] via [[tvb-adapters]].

The relationship between QSIPrep and [[the-virtual-brain]] is therefore one of data preparation: QSIPrep ensures that the diffusion MRI data are properly corrected, registered, and formatted before tractography reconstruction, while TVB utilizes the resulting connectivity matrices to simulate large-scale brain dynamics. Researchers building personalized brain models using [[personalized-brain-modeling]] approaches frequently employ QSIPrep to preprocess patient-specific diffusion data, enabling individualized structural connectomes that capture subject-specific anatomy. The combination of QSIPrep preprocessing with tractography reconstruction using [[mrtrix3]] and subsequent TVB simulation represents a canonical pipeline in the TVB ecosystem for studying how individual differences in white matter structure influence brain dynamics in conditions such as [[epilepsy-modeling]] or [[alzheimers-modeling]].

## Key Features

QSIPrep offers several features that make it particularly valuable for connectomics research. First, its strict BIDS compliance ensures that all outputs follow standardized naming conventions and data organization, facilitating data sharing and integration with other BIDS-compatible tools. Second, the pipeline provides extensive visual reports (HTML format) that document preprocessing quality for each subject, including motion plots, SNR estimates, and registration quality assessments, enabling researchers to identify and exclude problematic data before analysis. Third, QSIPrep supports parallel processing for multi-subject datasets, substantially reducing wall-clock time when preprocessing large cohorts such as those from the [[hcp-dataset]] or [[uk-biobank]].

The pipeline also supports multiple acquisition schemes including single-shell, multi-shell, and hybrid diffusion encoding, with automatic detection of shell configuration and appropriate modeling strategies. Advanced users can customize preprocessing parameters via configuration files, while the default settings reflect best practices established by the diffusion MRI community. Integration with Docker and Apptainer containers ensures identical behavior across computing environments, addressing a major source of non-reproducibility in [[computational-neuroscience]].

## Related Software

QSIPrep is part of a broader ecosystem of neuroimaging preprocessing pipelines that share common design principles and sometimes underlying tools. The most direct comparison is with [[fmriprep]], which performs analogous preprocessing for functional MRI data—both pipelines share the same software infrastructure (Nipype, Docker containers) and similar user interfaces @Gorgolewski2017fMRIPrep. Other related tools include [[mriqc]] for quality assessment of both structural and diffusion data, [[hcp-pipelines]] for processing Human Connectome Project data, and [[bidscoin]] for BIDS-ifying raw datasets before preprocessing. For downstream analysis, QSIPrep outputs are compatible with [[connectome-workbench]] for visualization and graph-theoretic analysis using the [[brain-connectivity-toolbox]], as well as [[nilearn]] for statistical modeling of neuroimaging data.

## Key Papers

- Cieslak, M., et al. (2021). QSIPrep: An integrative pipeline for preprocessing quantitative diffusion MRI. *Free Neuroimaging*.
- Gorgolewski, K., et al. (2017). fMRIPrep: A robust preprocessing pipeline for functional MRI. *Nature Methods*, 14(7), 733–736.

---

## References

1. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical [[fmri]] preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)