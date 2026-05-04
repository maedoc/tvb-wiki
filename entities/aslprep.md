---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-109de470e443.md
tags:
- software-preprocessing
- neuroimaging-fmri
- bids
- perfusion-mri
- arterial-spin-labeling
- python
- reproducibility
title: ASLPrep
type: software
updated: '2026-05-04'
---

# ASLPrep

## Overview

ASLPrep is a preprocessing pipeline designed for arterial spin labeling (ASL) magnetic resonance imaging data. Developed as part of the BIDS Apps ecosystem, ASLPrep provides a comprehensive, automated workflow for converting raw ASL MRI data into analysis-ready derivatives, handling the unique challenges posed by perfusion-weighted imaging sequences that differ substantially from conventional blood‑oxygen‑level‑dependent (BOLD) fMRI preprocessing. The pipeline is implemented in Python using [[nipype]] as its computational backbone, enabling seamless integration with other neuroimaging tools and workflows in the [[nilearn]] and [[fMRIPrep]] ecosystem.

Arterial spin labeling is a non‑invasive MRI technique that uses magnetically labeled arterial blood water as an endogenous tracer to measure cerebral blood flow (CBF). Unlike contrast‑agent perfusion imaging, ASL requires no external tracers and can be repeated multiple times, making it particularly valuable for studying brain function in clinical and research populations. However, ASL data processing presents unique challenges including low signal‑to‑noise ratio, complex subtraction between label and control images, and sensitivity to motion artifacts that necessitate specialized preprocessing algorithms not available in standard [[fmri]] tools [@doi:10.1002/mrm.25197].

## Motivation and Context

The development of ASLPrep emerged from a critical gap in the neuroimaging software landscape. While dedicated tools existed for processing conventional BOLD fMRI data—including [[fMRIPrep]], [[FSL]], and [[SPM]]—the ASL community lacked a standardized, reproducible preprocessing pipeline that could handle the unique characteristics of perfusion data. Researchers were forced to develop custom processing scripts, often leading to non‑reproducible methods across studies and significant barriers to replication and comparison of results.

The broader context for ASLPrep lies in the movement toward open science and reproducibility in neuroimaging, exemplified by initiatives like the [[human-connectome-project]] and the adoption of the [[BIDS]] data standard. ASLPrep was designed to follow the same philosophy as [[fMRIPrep]]: providing a “black box” preprocessing solution that produces rigorously documented, BIDS‑compliant outputs while allowing users to understand and modify individual processing steps if needed [@doi:10.1016/j.neuroimage.2020.117336]. This approach reduces the computational expertise required to perform high‑quality ASL preprocessing, lowering barriers for laboratories without dedicated imaging informatics teams.

ASLPrep also addresses the growing clinical interest in perfusion imaging. CBF measurements from ASL have shown promise in characterizing neurological conditions including stroke, dementia, and brain tumors, where altered cerebral blood flow serves as a key diagnostic and prognostic biomarker. A standardized preprocessing pipeline enables more consistent multi‑site studies and facilitates the translation of ASL from research to clinical practice.

## Technical Implementation

ASLPrep implements a modular processing pipeline that proceeds through several stages, each handling specific aspects of ASL data quality assurance and preprocessing. The pipeline begins with anatomical preprocessing, where T1‑weighted structural images are processed using [[FreeSurfer]] to generate skull‑stripped brain masks, tissue segmentations, and cortical parcellations. For ASL‑specific processing, the pipeline handles the unique requirements of perfusion data including motion correction across the entire label‑control time series, spatial smoothing adapted to the typically lower spatial resolution of ASL data, and CBF quantification using established models.

A distinguishing feature of ASLPrep is its integrated quality control system. The pipeline generates comprehensive diagnostic reports including temporal signal‑to‑noise ratios, motion parameters, and registration quality metrics that enable researchers to identify and potentially exclude problematic acquisitions before statistical analysis. This quality assurance framework draws on approaches developed for [[fMRIPrep]] and [[mriqc]], extending them with ASL‑specific metrics appropriate for perfusion data.

The computational architecture of ASLPrep leverages [[nipype]] for workflow management, enabling parallel execution of independent processing [[steps]] and facilitating integration with containerized deployment solutions. ASLPrep is available as a [[BIDS]] application, meaning it can process datasets organized according to the BIDS specification without manual intervention, further enhancing [[reproducibility]] by eliminating dataset‑specific configuration requirements.

## Key Features

ASLPrep provides several features that make it suitable for ASL data preprocessing in large‑scale studies. First, the pipeline implements automatic CBF quantification using the simplified kinetic model, the most widely accepted model for quantitative perfusion mapping from pulsed or continuous ASL data. Second, ASLPrep supports multiple ASL acquisition variants including pulsed ASL (PASL), continuous ASL (CASL), and pseudo‑continuous ASL (pCASL), accommodating data from different vendors and acquisition protocols. Third, the pipeline produces outputs in both native space and standardized spaces **including [[mni-space]] space**, facilitating group‑level analyses using tools like [[nilearn]] or [[FSL]].

The pipeline also handles multi‑band accelerated acquisitions common in modern ASL protocols, applying appropriate corrections for reconstruction artifacts specific to accelerated imaging. Integration with [[FSL]] tools enables advanced processing options including ICA‑based denoising through [[ica‑aroma]] when requested, though users must exercise caution as aggressive denoising can affect perfusion quantification. Additional features include BIDS‑compliant output formatting, automatic metadata extraction, and support for both 2D and 3D acquisition schemes commonly used in clinical settings.

## Relationship to The Virtual Brain

While ASLPrep focuses on preprocessing perfusion MRI data, its outputs can serve as input for whole‑brain modeling efforts using [[the-virtual‑brain]] (TVB). Cerebral blood flow measurements from ASL provide valuable constraints for personalized brain models, enabling researchers to calibrate hemodynamic parameters in neural mass models such as the [[jansen‑rit‑model]] or [[wong‑wang‑model]]. The [[whole‑brain‑modeling]] framework in TVB benefits from empirical perfusion data to establish baseline cerebral metabolism rates across brain regions, which can inform the initialization of excitation‑inhibition parameters in [[neural‑mass‑models]].

Furthermore, ASL‑derived CBF maps can be compared against [[functional‑connectivity]] estimates from [[bold‑signal|BOLD]] data, enabling multi‑modal validation of [[whole‑brain]] network models. The integration of perfusion information addresses a current limitation in many whole‑brain models that rely exclusively on [[structural‑connectivity]] from [[diffusion‑imaging]] (DTI) without accounting for hemodynamic state. ASLPrep thus serves as a valuable preprocessing component for researchers seeking to build more biophysically realistic brain models in TVB.

## Related Software

ASLPrep is part of a broader ecosystem of BIDS Apps and preprocessing tools for neuroimaging. Key related software include: [[fMRIPrep]] (the BOLD‑focused counterpart to ASLPrep), [[FSL]] (providing low‑level image processing utilities), [[SPM]] (an alternative MATLAB‑based analysis framework), [[FreeSurfer]] (for structural processing), and [[mriqc]] (for quality control). Additional related tools include [[ExploreASL]] (an alternative ASL processing pipeline with different features), [[BIDS]] (the data standard enabling automated preprocessing), and [[nilearn]] (for subsequent statistical analysis of processed data). For whole‑brain modeling applications, ASLPrep outputs may be used in conjunction with [[the‑virtual‑brain]], [[connectome‑workbench]], and [[brainsuite]] tools to create detailed computational models of brain dynamics.

## Key Papers

- **ASLPrep: A Robust Preprocessing Pipeline for ASL Data** [@doi:10.1101/2023.04.04.535856] — Original ASLPrep publication describing the pipeline architecture and validation.
- **fMRIPrep: A Robust Preprocessing Pipeline for Functional MRI** [@doi:10.1016/j.neuroimage.2020.117336] — The foundational paper for the preprocessing philosophy that ASLPrep draws upon.
- **Recommended ASL Processing Steps and Sources** [@doi:10.1002/mrm.25197] — Consensus paper on standard ASL processing methods and nomenclature.
- **BIDS Application Specification** [@doi:10.1002/hbm.25230] — Description of the BIDS Apps ecosystem and standardization approach.