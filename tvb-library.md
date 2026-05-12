---
title: TVB Library
created: 2026-04-20
updated: 2026-05-12
type: entity
tags: [software-tvb, software-neuroimaging, whole-brain-modeling, python, neural-mass-models]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/schirner-2018.md, raw/papers/arxiv-2509.12873.md]
---

# _preamble

TVB Library (`tvb-library`) is the open-source Python simulation kernel at the core of [[the-virtual-brain]], implementing the computational engine, [[neural-mass-models]] dynamics, and forward-model infrastructure for [[whole-brain-modeling]]. Conceived as the simulation backbone of a neuroinformatics platform for full brain network simulations, it enables researchers to couple biologically realistic [[structural-connectivity]]—derived from [[diffusion-imaging]] tractography—with population-level neural dynamics to generate macroscopic neuroimaging signals [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The library provides forward models that map simulated neural activity onto [[eeg|EEG]], [[meg|MEG]], and [[fmri|fMRI]] time series, allowing direct comparison with empirical recordings and supporting model-based inference across spatial and temporal scales [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]][[raw/papers/ritter-2013.md|Ritter et al. (2013)]].

Architected for integration with subject-specific neuroimaging data, TVB Library ingests individualized [[structural-connectivity]] matrices to construct personalized models capable of reproducing [[resting-state]] and task-evoked dynamics, and it serves as the simulation backend for automated pipeline workflows as well as newer reproducibility frameworks such as the TVB Ontology [[raw/papers/ritter-2013.md|Ritter et al. (2013)]][[raw/papers/schirner-2018.md|Schirner et al. (2018)]][[raw/papers/semanticscholar-9afbfd2d37be.md|Martin et al. (2025)]]. Recent work also demonstrates its use alongside analysis platforms such as Cobrawap for quantitative calibration and tuning of model parameters against biological observables [[raw/papers/arxiv-2509.12873.md|Gaglioti et al. (2025)]].