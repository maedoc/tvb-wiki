---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-cabf914d6370.md
- raw/papers/semanticscholar-44da8d4ab79e.md
- raw/papers/glasser-2013.md
tags:
- database
- neuroimaging
- resting-state
- diffusion-imaging
- dataset
title: AOMIC (Amsterdam Open MRI Collection)
type: entity
updated: '2026-05-05'
---

The Amsterdam Open MRI Collection (AOMIC) is a large-scale open [[neuroimaging]] dataset originating from the Netherlands, designed to advance research on brain [[connectivity]], cognition, and individual differences in brain structure and function across the adult lifespan. The AOMIC dataset comprises multimodal magnetic resonance imaging (MRI) data from over 1,400 healthy adult participants, including structural MRI, resting-state functional MRI (rs-[[fmri]]), diffusion tensor imaging (DTI), and behavioral measurements. The collection was assembled to address the growing need for publicly accessible neuroimaging datasets that capture individual differences in brain organization across the adult lifespan.

## Motivation and Scientific Context

The AOMIC dataset emerged in response to the broader movement toward open science in neuroimaging, following the success of initiatives such as the [[human-connectome-project]] and [[uk-biobank]] [@snoek_et_al_2020]. While these large-scale consortia have provided invaluable resources, they often involve complex acquisition protocols and restricted access models. AOMIC was designed to complement these efforts by providing a more accessible dataset with detailed phenotyping. The cohort addresses a fundamental question in modern neuroscience: how do various lifestyle factors and individual characteristics modulate [[functional-connectivity]] and [[structural-connectivity]] patterns in the healthy brain?

The dataset specifically targets the adult lifespan (18–65 years), a period during which subtle but meaningful changes in brain network organization occur. This age range is critical because it spans both the peak of cognitive performance and the onset of age-related declines in [[brain-network]] integrity. By releasing data from a well-characterized cohort with detailed phenotyping, AOMIC enables researchers to investigate questions about [[resting-state]] networks, [[structural-connectivity]] trajectories, and the neural correlates of individual differences in cognition.

## Dataset Characteristics and Structure

The AOMIC collection comprises three principal sub-datasets that were acquired as separate studies and subsequently made available as a unified resource. The **PIOP1** (Psychiatric Imaging Cohort Open Imaging Platform 1) dataset includes approximately 216 participants scanned at UMC Utrecht [@openneuro_piops]. The **PIOP2** cohort, also from the same acquisition series, contains roughly 216 additional participants. The largest component is **ID1000** (Imaging Depression 1000), which encompasses approximately 1,000 individuals designed to capture the full spectrum of individual differences in brain structure and function across the adult lifespan.

All participants were screened for neurological and psychiatric conditions to ensure a sample of healthy individuals. Behavioral assessments include cognitive batteries, questionnaires on various lifestyle variables including physical activity, sleep patterns, and mood assessments. The comprehensive phenotyping enables researchers to investigate associations between behavioral measures and neuroimaging findings.

## Acquisition and Preprocessing

The AOMIC cohort includes high-resolution T1-weighted structural images used for volumetric and morphometric analyses, resting-state fMRI acquisitions for examining [[functional-connectivity]] between brain regions, and diffusion-weighted imaging for reconstructing [[white-matter]] tracts and computing metrics such as [[fractional-anisotropy]]. All MRI data were collected on 3T MRI scanners following standardized acquisition protocols to ensure data quality and consistency across participants.

The data were preprocessed using established pipelines including Fsl, Freesurfer, and Mrtrix3, with derivative outputs such as gray matter volumes, [[resting-state]] network maps, and tractography files made available through the OpenNeuro repository [@openneuro_aomic]. This standardized preprocessing enables direct comparison across studies and facilitates [[reproducibility]]—a persistent challenge in neuroimaging research. All data are released in [[bids]] format, following community standards for neuroimaging data organization.

## Scientific Applications

AOMIC has been used in numerous studies examining [[functional-connectivity]] patterns, [[brain-network]] topology, and the effects of various factors on brain structure. Researchers have leveraged the dataset to investigate individual differences in [[default-mode-network]] connectivity, the relationship between physical activity and white matter integrity, and the stability of [[resting-state]] networks across scan sessions [@default_mode_study]. The cohort has also supported method development work in [[diffusion-imaging]] analysis, [[community-detection]] algorithms for brain networks, and machine-learning approaches to brain age prediction.

## Relationship to TVB

While AOMIC was not explicitly designed for whole-brain modeling, its multimodal imaging data provide excellent input for constructing personalized brain connectomes in [[the-virtual-brain]] (TVB). The [[structural-connectivity]] matrices derived from AOMIC DTI data can be used as anatomical skeletons in TVB simulations, enabling researchers to investigate how empirical connectivity patterns constrain [[network-dynamics]]. The resting-state fMRI data offer opportunities for validating TVB model outputs against empirical functional connectivity, supporting [[model-validation]] workflows. Because AOMIC is openly available on OpenNeuro, it serves as a useful test case for developing TVB preprocessing pipelines that convert [[bids]]-format data into TVB-compatible connectivity matrices. The dataset thus contributes to the broader ecosystem of neuroimaging resources that enable computational modeling approaches in [[whole-brain-modeling]].

## References

1. M. M. Esfahani, Vladislav Esaulov, Hemanth Venkateswara, V. Calhoun. (2025). *NEUROMARK DFNC PATTERNS: A FULLY AUTOMATED PIPELINE TO ESTIMATE SUBJECT-SPECIFIC STATES FROM RS-FMRI DATA VIA CONSTRAINED ICA OF DFNC IN +100K SUBJECTS*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.01.29.635539))
2. B. Sarton, Giulia Maria Mattia, Eve Cervoni, Julie Decourt, Patrice Péran, Béatrice Riu, Fanny Bounes, Edouard Naboulsi, P. Barttfeld, Jean-Marc Olivot, Stein Silva, Sylvain Cussat-Blanc. (2026). *Explainable Machine Learning for Coma Outcome Prediction Based on Structural and Functional Brain MRI.*. Critical Care Medicine. [DOI](](https://doi.org/10.1097/CCM.0000000000007068))
3. (authors unknown). *The Minimal Preprocessing Pipelines for the Human [[connectome]] Project*.