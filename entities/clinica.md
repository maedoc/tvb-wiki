---
created: 2024-01-15
sources:
- raw/papers/schirner-2018.md
- raw/papers/glasser-2013.md
- raw/papers/semanticscholar-4d73a30d5c84.md
- raw/papers/semanticscholar-d6e43299345d.md
tags:
- software-brain-modeling
- whole-brain-modeling
- personalized-brain-modeling
- neuroimaging-fmri
- neuroimaging-pet
- neuroimaging-dti
- structural-connectivity
- functional-connectivity
- resting-state
- reproducibility
- database-hcp
- connectomics
title: Clinica
type: entity
updated: '2026-05-19'
---

Clinica is an open-source software platform developed by the Aramis team at Inria for clinical [[neuroimaging]] data processing and analysis. It integrates established neuroimaging processing tools into standardized, reproducible pipelines that adhere to the [[bids]] specification, providing a unified command-line interface for processing structural, functional, and molecular imaging data consistently across studies.

## Motivation and Context

Reliable [[whole-brain-modeling]] and cross-study comparison depend on standardized preprocessing of neuroimaging data. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] established the importance of minimal preprocessing pipelines for large-scale connectomics projects such as the [[human-connectome-project]], demonstrating that systematic processing is essential for robust downstream analyses. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] highlighted that lab-specific image processing approaches remain a major roadblock for harmonization across sites, and that uniform workflows are crucial for inter-site standardization and for reducing preprocessing bias. [[raw/papers/schirner-2018.md|Schirner et al. (2018)]] further demonstrated that constructing personalized virtual brains for biophysical simulation depends critically on high-quality structural connectomes derived from carefully processed anatomical and diffusion data. By enforcing BIDS organization at the point of processing rather than through post-hoc conversion, Clinica reduces methodological heterogeneity that limits reproducibility.

## Key Features

Clinica's architecture centers on processing pipelines for T1-weighted MRI, PET, and diffusion MRI data. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] showed that state-of-the-art multimodal pipelines must integrate volumetric and cortical thickness assessments, spatial normalization, and atlas-based outputs. The T1-weighted pipeline produces cortical parcellations and volumetric segmentations, while functional imaging supports resting-state [[fmri]] preprocessing for [[functional-connectivity]] analyses. [[raw/papers/semanticscholar-4d73a30d5c84.md|Wang et al. (2026)]] emphasized that robust preprocessing is critical for functional MRI data, where motion-related artifacts and susceptibility-induced signal loss must be carefully controlled. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] showed that standard neuroimaging formats such as [[nifti]] and [[cifti]] facilitate cross-tool interoperability, a principle reflected in Clinica's design. The platform also supports diffusion MRI processing for [[structural-connectivity]] analysis via integration with [[tractography]] tools.

## Relationship to TVB

Clinica functions as an essential upstream component for [[whole-brain-modeling]] workflows that require subject-specific connectomes as input. [[raw/papers/schirner-2018.md|Schirner et al. (2018)]] developed an automated pipeline for constructing personalized virtual brains in [[the-virtual-brain]] (TVB), demonstrating that processed structural connectomes can be directly imported into [[neural-mass-models]]. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] established that standardized preprocessing enables reliable subject-specific network analyses across cohorts, reinforcing the value of methodological consistency before data enter simulation environments. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] noted that large-scale multimodal datasets require containerized, automated processing with low failure rates. This integration is particularly relevant for clinical applications such as [[epilepsy-modeling]], where patient-specific anatomical constraints improve seizure propagation simulations, and for [[alzheimers-modeling]] studies of pathological biomarker spread.

## Related Software

Clinica occupies a specialized position alongside workflow engines such as [[nipype]] and graph-theoretic tools such as the [[brain-connectivity-toolbox]]. Unlike general-purpose pipeline managers, Clinica emphasizes clinical study requirements and tight BIDS integration. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] described ADprep as a similar containerized, fully automated toolbox that works on BIDS-formatted data and was developed in Nipype, generating standardized outputs for multimodal MRI and PET. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] established the HCP minimal preprocessing pipelines that similarly emphasize standardization across large cohorts. [[raw/papers/semanticscholar-4d73a30d5c84.md|Wang et al. (2026)]] further advanced multi-echo fMRI preprocessing frameworks that complement standardized neuroimaging pipelines. Its outputs interface with specialized clinical software such as [[lead-dbs]] for deep brain stimulation planning.

## References

1. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
2. (authors unknown). *The Minimal Preprocessing Pipelines for the Human Connectome Project*.
3. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo fMRI denoising and preprocessing*. Imaging Neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.1198)
4. A. Dehsarvi, Lukas Frontzkowski, Anna Dewenter, Michael Schöll, N. Franzmeier. (2025). *ADprep – A Fully‐Automated Software for Large‐scale Multimodal MRI and PET Imaging Workflows*. Alzheimer's & Dementia. [DOI](https://doi.org/10.1002/alz70856_101373)