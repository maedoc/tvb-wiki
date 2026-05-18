---
title: RABIES
created: 2025-01-15
updated: 2026-05-18
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, structural-connectivity, personalized-brain-modeling, alzheimers-modeling]
sources: [raw/papers/ritter-2013.md, raw/papers/sanz-leon-2013.md, raw/papers/huntenburg-2018.md]
---

RABIES (Robust Astute Segmentation of Images via a Bayesian framework) is an open-source neuroimaging software package for automated segmentation of brain structures and pathological lesions in magnetic resonance imaging (MRI) data. The software applies Bayesian probabilistic models to achieve robust segmentation across heterogeneous clinical and research datasets, making it valuable for population studies involving aging brains and neurological disease cohorts.

## Overview

RABIES incorporates Bayesian inference to model uncertainty in image intensity distributions and anatomical boundaries, enabling adaptation to different scanner types, acquisition protocols, and patient populations. The framework was developed to address challenges in segmenting white matter hyperintensities and subcortical structures, which are clinically relevant biomarkers for diseases including [[alzheimers-disease]], vascular dementia, and small vessel disease. By constructing statistical models of expected tissue class distributions and using Bayesian updating to refine segmentation probabilities from observed image intensities, RABIES produces confidence maps alongside hard segmentations, supporting quality control in large-scale studies.

## Key Features

The Bayesian formulation enables explicit modeling of prior knowledge about anatomical structures derived from established atlases such as [[mni-space]] templates. Spatial regularization through Markov random field models encourages anatomically coherent segmentations and suppresses isolated misclassifications. Built-in support for multispectral segmentation integrates multiple MRI contrasts (T1-weighted, T2-weighted, FLAIR, PD) to improve accuracy, which is particularly important for lesion segmentation where tissue types may have overlapping intensities in a single contrast. The framework also includes modular preprocessing pipelines covering bias field correction, intensity normalization, and registration to standard space, with tools for longitudinal analysis of lesion load changes over time.

RABIES outputs results in standard NIfTI format, facilitating integration with downstream tools including [[mrtrix3-connectome]] and connectivity analysis packages.

## Relationship to TVB

RABIES is not directly integrated into [[the-virtual-brain]] (TVB), but it occupies a complementary position in the TVB ecosystem. TVB constructs personalized [[whole-brain-modeling]] simulations by coupling [[neural-mass-models]] with subject-specific [[structural-connectivity]] data derived from diffusion MRI tractography Sanz Leon et al. (2013). The integration of multimodal neuroimaging data — spanning structural, functional, and diffusion modalities — is central to TVB's methodology for translating clinical imaging into mechanistic, simulation-ready brain models Ritter et al. (2013).

Segmentation outputs from tools like RABIES — particularly white matter parcellations and lesion maps — can serve as anatomical constraints for these personalized brain models. In [[personalized-brain-modeling]] workflows, individual patient segmentations define region-of-interest boundaries and inform the spatial embedding of TVB's [[neural-mass-model]] populations. This is especially relevant for clinical applications in [[epilepsy-modeling]] and neurodegenerative disease, where accurate anatomical personalization is critical for capturing pathology-specific [[network-dynamics]].

## Related Software

RABIES occupies a niche alongside other brain segmentation tools. [[nighres]] provides processing tools for high-resolution neuroimaging including brain extraction, segmentation, and cortex reconstruction, making specialized CBS High-Res Brain Processing Tools accessible through a documented Python interface Huntenburg et al. (2018). The closest functional equivalents for structural segmentation include [[ants]], which provides the Atropos segmentation module, and [[brainvisa]], which offers cortical reconstruction through probabilistic labeling based on Bayesian inference combined with anatomical constraints. For whole-brain parcellation, RABIES outputs can be combined with established atlases such as the [[schaefer-atlas]], [[glasser-atlas]], or [[desikan-killiany-atlas]] to produce study-specific parcellations that incorporate lesion information.
