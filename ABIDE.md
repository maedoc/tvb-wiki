---
title: ABIDE
created: 2025-01-15
updated: 2026-05-06
type: entity
tags: [dataset, neuroimaging-fmri, resting-state, autism, database]
sources:
  - Di Martino, A., Yan, C. G., Li, Q., et al. (2014). The autism brain imaging data exchange: towards a large-scale assessment of intrinsic functional brain connectivity in autism. Molecular Autism, 5(1), 36.
  - Di Martino, A., Yan, C. G., Li, Z., et al. (2017). Enhancing studies of the connectome in autism using the autism brain imaging data exchange II. Scientific Data, 4, 170010.
---

The Autism Brain Imaging Data Exchange (ABIDE) is a collaborative consortium that aggregates and publicly shares neuroimaging datasets from individuals with autism spectrum disorder (ASD) and matched neurotypical controls. Launched in 2012, ABIDE represents one of the earliest large-scale open-science initiatives in psychiatric neuroimaging, providing researchers worldwide with access to preprocessed and raw resting-state functional magnetic resonance imaging (fMRI) data collected across multiple institutions (Di Martino et al., 2014). The consortium addresses a fundamental barrier in autism research: the scarcity of large, multi-site datasets needed to achieve statistical power for detecting subtle yet clinically meaningful patterns of brain dysfunction.

## Motivation and Scientific Context

Autism spectrum disorder is a heterogeneous neurodevelopmental condition characterized by differences in social communication, interaction, and behavior. Understanding the neural basis of ASD requires large sample sizes to account for intersite variability, individual differences, and the subtle effect sizes typical of psychiatric neuroimaging findings. Historically, individual research labs possessed modest datasets insufficient for robust characterization of whole-brain connectivity patterns. ABIDE emerged to solve this problem by establishing a standardized data-sharing framework that harmonizes imaging protocols across sites while preserving statistical power through data aggregation.

The dataset has enabled investigators to investigate alterations in [[resting-state]] functional connectivity associated with ASD, including differences in [[default-mode-network]] integrity, [[functional-connectivity]] between frontal and posterior brain regions, and patterns of [[brain-network]] organization. By providing both raw and preprocessed data, ABIDE supports methodologically diverse approaches—whether using [[graph-theory]] based network analysis, [[ICA]]-based decomposition, or region-of-interest correlation methods.

## Key Features

ABIDE encompasses data from over 1,000 individuals with ASD and neurotypical controls across approximately 20 imaging sites worldwide. The consortium released two principal datasets: ABIDE I (released 2012) and ABIDE II (released 2017), with the latter incorporating additional samples and improved metadata standardization (Di Martino et al., 2017). Each dataset includes high-resolution T1-weighted structural images and resting-state fMRI acquisitions, accompanied by detailed phenotypic information including age, sex, IQ measures, and clinical measures such as ADOS (Autism Diagnostic Observation Schedule) and ADI-R (Autism Diagnostic Interview-Revised) scores where available.

Data are hosted on the [[nitrc]] platform and the [[LONI]] (Laboratory of Neuro Imaging) Image Data Archive, with preprocessing pipelines including approaches implemented in [[SPM]], [[FSL]], and [[AFNI]] freely available. The dataset employs quality control measures and excludes individuals with significant motion artifacts, though motion remains a consideration in analyzing developmental and clinical cohorts.

## Relationship to TVB

ABIDE has become a critical resource for The Virtual Brain ecosystem in several ways. First, researchers building Personalized [[whole-brain-modeling]] simulations frequently use ABIDE-derived structural connectivity matrices as the structural backbone for [[TVB]] simulations. The consortium's multi-site data enables investigation of how anatomical connectome differences influence emergent dynamics in neural mass models. Second, ABIDE provides empirical validation data against which [[whole-brain-modeling]] outputs can be compared—investigators can simulate typical and atypical brain dynamics and assess correspondence with observed [[functional-connectivity]] patterns from the dataset. Third, the dataset supports parameter estimation workflows in TVB by providing target functional connectivity states for model fitting. Finally, ABIDE enables comparative studies between [[personalized-brain-modeling]] approaches and empirical findings on autism, supporting research into [[epilepsy-modeling]] comorbidity and other conditions frequently co-occurring with ASD.

## Key Papers

- Di Martino, A., Yan, C. G., Li, Q., et al. (2014). The autism brain imaging data exchange: towards a large-scale assessment of intrinsic functional brain connectivity in autism. *Molecular Autism*, 5(1), 36.
- Di Martino, A., Yan, C. G., Li, Z., et al. (2017). Enhancing studies of the connectome in autism using the autism brain imaging data exchange II. *Scientific Data*, 4, 170010.

## Related Software

- [[TVB]]
- [[nilearn-datasets]]
- [[brain-connectivity-toolbox]]
- [[connectome-workbench]]
- [[FSL]]

## References

1. Di Martino, A., Yan, C. G., Li, Q., et al. (2014). The autism brain imaging data exchange: towards a large-scale assessment of intrinsic functional brain connectivity in autism. *Molecular Autism*, 5(1), 36.

2. Di Martino, A., Yan, C. G., Li, Z., et al. (2017). Enhancing studies of the connectome in autism using the autism brain imaging data exchange II. *Scientific Data*, 4, 170010.