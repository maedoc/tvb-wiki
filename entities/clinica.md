---
title: Clinica
created: 2024-01-15
updated: 2026-05-18
type: entity
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
- database-uk-biobank
- connectomics
sources:
- raw/papers/schirner-2018.md
- raw/papers/glasser-2013.md
- raw/papers/semanticscholar-4d73a30d5c84.md
- raw/papers/semanticscholar-d6e43299345d.md
---

Clinica is an open-source software platform developed by the Aramis team at Inria for clinical neuroimaging data processing and analysis. The platform integrates established neuroimaging processing tools into standardized, reproducible pipelines that adhere to the [[bids]] specification, providing researchers with a unified command-line interface for processing structural, functional, and molecular imaging data consistently across studies.

## Motivation and Context

The development of Clinica reflects a broader recognition in computational neuroscience that reliable whole-brain modeling and cross-study comparison depend on rigorous, standardized preprocessing of neuroimaging data. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] established the importance of minimal preprocessing pipelines for large-scale connectomics projects such as the [[human-connectome-project]], demonstrating that systematic anatomical and functional processing is essential for robust downstream network analyses. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] highlighted that lab-specific image processing approaches remain a major roadblock for harmonization across sites, and that developing uniform, user-friendly workflows is crucial for inter-site standardization and for reducing bias introduced by different preprocessing strategies. [[raw/papers/schirner-2018.md|Schirner et al. (2015)]] further demonstrated that constructing personalized virtual brains for biophysical simulation depends critically on high-quality structural connectomes derived from carefully processed anatomical and diffusion data. By enforcing data organization through the BIDS standard at the point of processing rather than through post-hoc conversion, Clinica reduces the methodological heterogeneity that otherwise limits reproducibility across clinical neuroimaging studies.

## Key Features

Clinica's architecture centers on processing pipelines for T1-weighted MRI, PET, and diffusion MRI data, extracting biomarkers relevant to neurological and psychiatric populations. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] showed that state-of-the-art multimodal pipelines must integrate volumetric and cortical thickness assessments, spatial normalization, and atlas-based outputs to facilitate downstream statistical analyses. The T1-weighted pipeline in Clinica produces cortical parcellations and volumetric segmentations that can serve as anatomical constraints for connectome construction, while the PET pipeline includes motion correction, spatial normalization to [[mni-space]], and standardized uptake value computations. For functional imaging, Clinica supports resting-state [[fmri]] preprocessing for [[functional-connectivity]] analyses. [[raw/papers/semanticscholar-4d73a30d5c84.md|Wang et al. (2026)]] emphasized that robust preprocessing is particularly critical for functional MRI data, where motion-related artifacts and susceptibility-induced signal loss must be carefully controlled to preserve the validity of downstream connectivity estimates. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] showed that producing outputs in standard neuroimaging formats such as [[nifti]] and [[cifti]] facilitates cross-tool interoperability, a principle reflected in Clinica's design. The platform also supports diffusion MRI processing for [[structural-connectivity]] analysis via integration with tractography tools.

## Relationship to TVB

Although Clinica focuses on preprocessing and biomarker extraction rather than biophysical modeling, it functions as an essential upstream component for [[whole-brain-modeling]] workflows that require subject-specific connectomes as input. [[raw/papers/schirner-2018.md|Schirner et al. (2015)]] developed an automated pipeline for constructing personalized virtual brains in [[the-virtual-brain]] (TVB), demonstrating that processed structural connectomes derived from diffusion MRI and parcellated anatomical surfaces can be directly imported into neural mass models. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] established that standardized preprocessing enables reliable subject-specific network analyses across cohorts, reinforcing the value of enforcing methodological consistency before data enter simulation environments. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] noted that large-scale multimodal datasets require containerized, automated processing with low failure rates to ensure that subject-specific outputs are suitable for downstream modeling. This integration is particularly relevant for clinical applications such as [[epilepsy-modeling]], where patient-specific anatomical constraints improve the fidelity of seizure propagation simulations, and for [[alzheimers-modeling]] studies investigating how pathological biomarkers spread across large-scale networks.

## Related Software

Clinica occupies a specialized position in the neuroimaging software ecosystem alongside workflow engines such as [[nipype]] and graph-theoretic analysis tools such as the [[brain-connectivity-toolbox]]. Unlike general-purpose pipeline managers, Clinica emphasizes clinical study requirements and tight BIDS integration. [[raw/papers/semanticscholar-d6e43299345d.md|Dehsarvi et al. (2025)]] described ADprep as a similar containerized, fully automated neuroimaging toolbox that works on BIDS-formatted data and was developed in Nipype, generating standardized outputs for multimodal MRI and PET analyses. [[raw/papers/glasser-2013.md|Glasser et al. (2013)]] established the HCP minimal preprocessing pipelines that similarly emphasize standardization across large cohorts. [[raw/papers/semanticscholar-4d73a30d5c84.md|Wang et al. (2026)]] further advanced multi-echo fMRI preprocessing frameworks that complement the broader landscape of standardized neuroimaging pipelines. Its outputs interface with specialized clinical software such as [[lead-dbs]] for deep brain stimulation planning, and the processed connectomes it generates complement these broader preprocessing landscapes established by large-scale neuroimaging initiatives.
