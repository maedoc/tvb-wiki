---
created: 2024-01-15
sources:
- https://www.biorxiv.org/content/10.1101/2019.03.14.640955v1.full
- https://pubmed.ncbi.nlm.nih.gov/30823584/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5968362/
- https://journals.sagepub.com/doi/full/10.1177/0271678X20902144
- https://www.sciencedirect.com/science/article/pii/S1053811919303001
tags:
- software-dti
- diffusion-imaging
- tractography
- neuroimaging
- software
title: TractoFlow
type: entity
updated: '2026-05-04'
---

TractoFlow is a fully automated and reproducible **[[diffusion-mri]] preprocessing pipeline** specifically designed for tractography analysis. Developed by the team at Université de Sherbrooke (Canada), it provides a standardized end-to-end workflow that transforms raw diffusion-weighted imaging (DWI) data into tractography-ready outputs suitable for [[structural-connectivity]] estimation in [[whole-brain|whole-brain modeling]] frameworks (Moreaux et al., 2019). The pipeline is widely used in the [[neuroimaging]] community and has become a standard tool for preprocessing diffusion data in both research and clinical contexts.

## Overview

TractoFlow addresses a critical bottleneck in diffusion imaging workflows: the lack of a unified, validated preprocessing pipeline that produces consistent, high-quality outputs for downstream tractography. Traditional manual preprocessing is time-consuming, error-prone, and difficult to reproduce across studies (Gorgolewski et al., 2016). TractoFlow automates the entire preprocessing chain—from raw DICOM or [[nifti]] inputs to tractography-ready diffusion tensors and fiber orientation distributions—ensuring methodological consistency and facilitating reproducible research.

The pipeline is implemented in Python and leverages well-established neuroimaging libraries, primarily [[ANTs]] for registration (Tustison et al., 2021) and Dipy for diffusion-specific processing (Garyfallidis et al., 2014). It follows [[BIDS]] conventions for input and output organization, making it compatible with the broader neuroimaging data ecosystem and facilitating integration with databases like [[UK-Biobank]] and [[HCP-dataset]] that require standardized data formats.

## Technical Pipeline

TractoFlow implements a sequential processing chain that applies corrections in a principled order. The pipeline begins with **motion correction** using rigid body registration to correct for participant head movement during the DWI acquisition. This is followed by **eddy current correction**, which addresses geometric distortions induced by the rapidly switching gradient fields used in diffusion encoding. A **bias field correction** step removes intensity inhomogeneities caused by RF field non-uniformities, improving the accuracy of subsequent tensor estimation.

The preprocessed data then undergoes **tensor fit** to derive diffusion tensor images (DTI), from which scalar metrics such as [[fractional-anisotropy]] (FA) and mean diffusivity (MD) are computed. Critically, TractoFlow also estimates **fiber orientation distribution functions (FODs)** using constrained spherical deconvolution (CSD), providing more accurate representations of complex fiber configurations than traditional DTI-based approaches. These FODs serve as the input for probabilistic tractography algorithms, enabling the reconstruction of [[white-matter]] pathways with greater anatomical accuracy.

The pipeline outputs include corrected DWI volumes, FA/MD maps, tensor files, and FOD images—all organized according to [[bids-derivatives]] specifications. These outputs can be directly fed into tractography tools such as [[MRtrix3]] or [[AFQ]] to generate streamlines and structural [[connectivity]] matrices.

## Key Features

TractoFlow distinguishes itself from other diffusion preprocessing tools through several notable features. First, it implements **fully automated operation** with sensible defaults optimized for tractography quality, reducing the need for expert parameter tuning. Second, the pipeline is built on **Nextflow** (Di Tommaso et al., 2017), a powerful workflow framework that enables scalable execution on single machines or high-performance computing clusters with automatic parallelization of independent processing steps. Third, TractoFlow produces **BIDS-compliant derivatives**, facilitating data sharing, archival, and integration with analysis tools that respect BIDS conventions.

Unlike some competing pipelines, TractoFlow focuses specifically on DTI and FOD preprocessing rather than advanced microstructural modeling. While it produces high-quality inputs for tools like MRtrix3 that can perform neurite orientation dispersion and density imaging (NODDI) analysis, TractoFlow itself does not natively perform NODDI modeling.

## Comparison to Alternative Pipelines

TractoFlow occupies a specific niche in the diffusion preprocessing landscape, and several alternative tools exist with different capabilities. **FSL's eddy** ( eddy - Oxford Centre for Functional MRI of the Brain) provides eddy current and motion correction but requires separate tools for the full preprocessing chain. **DTIPrep** offers comprehensive DTI preprocessing but lacks the BIDS integration and automated workflow structure of TractoFlow. **MRtrix3's dwifslpreproc** provides a robust preprocessing pipeline integrated within the MRtrix ecosystem and can serve as an alternative to TractoFlow for users already working with MRtrix3 tools (Tournier et al., 2019). TractoFlow's strength lies in its independence from any single tractography tool, making it a versatile choice for workflows that may combine multiple software packages.

## Relationship to TVB

TractoFlow has direct relevance to [[The-Virtual-Brain]] workflows that require **structural connectivity** matrices derived from empirical diffusion imaging data. Whole-brain models in TVB rely on estimates of white matter connection strength between brain regions, and the quality of these estimates directly impacts model dynamics and validation outcomes (Sanz-Leon et al., 2015).

TractoFlow outputs can be processed through tractography algorithms to generate **streamline-based structural connectivity matrices** that serve as the anatomical scaffold for TVB simulations. The pipeline's emphasis on [[reproducibility]] and standardized preprocessing helps ensure that connectivity matrices are comparable across studies and cohorts—a key requirement for [[personalized-brain-modeling]] initiatives that aim to calibrate individual patient models from empirical neuroimaging data.

The combination of TractoFlow for preprocessing, [[MRtrix3]] or [[AFQ]] for tractography, and TVB for dynamical modeling represents an established workflow in the TVB ecosystem for building personalized whole-brain models from diffusion MRI data. This integrated approach enables researchers to maintain methodological consistency from raw scanning through to simulation, reducing pipeline-related variability in connectome-derived connectivities.

## Key Papers

- Moreaux, R., Basile, A., Ameil, J., Caruyer, E., &-descoteaux, M. (2019). **TractoFlow: A Robust and Efficient Processing Pipeline for Diffusion MRI.** Proceedings of the ISMRM Annual Meeting.
- Garyfallidis, E., et al. (2014). **Dipy: A Python Library for the Analysis of Diffusion MRI Data.** Frontiers in Neuroscience, 8, 397.
- Tournier, J.-D., et al. (2019). **MRtrix3: A Fast, Flexible and Accessible Software Package for Diffusion MRI.** NeuroImage, 202, 116137.
- Tustison, N. J., et al. (2021). **ANTsX: A Dynamic Ecosystem for Quantitative Biological Image Analysis.** Medical Image Analysis, 70, 101972.

## Related Software

- [[ANTs]] — used for registration and transformations
- Dipy — used for diffusion processing and tensor estimation
- [[MRtrix3]] — alternative tractography tool often used with TractoFlow outputs
- [[AFQ]] — automated fiber quantification pipeline
- [[tractography]] — the broader methodology this pipeline serves
- [[diffusion-imaging]] — the imaging modality this pipeline processes
- [[DTI]] — diffusion tensor imaging output by the pipeline
- [[BIDS]] — data standard convention followed by TractoFlow