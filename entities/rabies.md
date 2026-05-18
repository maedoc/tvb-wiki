---
created: 2026-04-20
sources:
- raw/papers/desrosiers-gregoire-2024.md
- raw/papers/ritter-2013.md
- raw/papers/sanz-leon-2013.md
- raw/papers/huntenburg-2018.md
tags:
- software-brain-modeling
- neuroimaging-fmri
- resting-state
- functional-connectivity
- reproducibility
- whole-brain-modeling
- connectomics
title: RABIES
type: entity
updated: '2026-05-18'
---
RABIES (Rodent Automated Bold Improvement of EPI Sequences) is an open-source software pipeline for preprocessing, quality control, confound correction, and resting-state functional connectivity analysis of rodent functional magnetic resonance imaging data [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. Built using Nipype and distributed via Docker and Singularity containers, it requires BIDS-formatted inputs and produces standardized outputs including motion-corrected EPI volumes, common-space alignments, and functional connectivity matrices [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. The pipeline was validated across 23 multi-site datasets encompassing mice and rats acquired at field strengths ranging from 4.7 to 11.7 T, achieving near-perfect success rates for brain masking and cross-subject registration [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]].

## Motivation and Context

Unlike human neuroimaging, where frameworks such as [[fmriprep]] have standardized preprocessing, the rodent fMRI community historically lacked validated pipelines for confound correction and connectivity analysis [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. Variability in acquisition sites, coil geometries, anesthesia protocols, and field strengths introduces substantial heterogeneity that complicates cross-study comparisons [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. RABIES addresses this gap by integrating adaptive image registration with principled confound correction strategies—covering regression, censoring, and frequency filtering—and by furnishing automated quality control reports that classify scans according to network detectability and spurious connectivity signatures [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. These reports compile spatiotemporal diagnostics including BOLD variability maps, global signal covariance, and network confound timecourses, enabling researchers to identify acquisition-level issues before proceeding to group statistics [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]].

## Relationship to TVB

Whole-brain modeling platforms such as [[tvb]] construct network models by coupling empirical connectivity data with [[neural-mass-models]] to simulate large-scale [[network-dynamics]], and they depend critically on preprocessing consistency to ensure that simulated differences reflect neurobiological variation rather than methodological artifacts [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]][[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. Although RABIES is not natively integrated into TVB, the [[functional-connectivity]] matrices and quality-controlled [[resting-state]] outputs it generates are conceptually aligned with the empirical data required to parameterize and validate such models [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. TVB's forward models for simulating [[neuroimaging-fmri]] signals and comparing them against empirical recordings presuppose rigorous preprocessing and confound management [[raw/papers/ritter-2013.md|Ritter et al. (2013)]], practices that RABIES formalizes for rodent datasets through its containerized architecture and evidence-based guidelines for network-analysis quality control [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. Subject-specific functional connectivity derived from resting-state fMRI can constrain personalized [[brain-network]] models, and automated pipelines that reduce operator-dependent variability support cohort-scale simulations with systematically comparable inputs [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]][[raw/papers/ritter-2013.md|Ritter et al. (2013)]].

## Related Tools

RABIES occupies a methodological position alongside other neuroimaging pipelines that translate raw MRI data into analysis-ready connectivity estimates. While it specializes in rodent acquisitions, human counterparts such as [[fmriprep]] share its Nipype-based architecture and emphasis on reproducible preprocessing and automated quality control [[raw/papers/desrosiers-gregoire-2024.md|Desrosiers-Grégoire et al. (2024)]]. For high-resolution structural segmentation and cortical surface extraction, tools such as [[nighres]] provide complementary capabilities including MGDM tissue classification and CRUISE surface reconstruction [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]]. These diverse preprocessing ecosystems collectively supply the anatomical and functional constraints that whole-brain simulators require to map simulated neural activity onto empirical neuroimaging signals [[raw/papers/ritter-2013.md|Ritter et al. (2013)]][[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].
