---
title: TVB Library
created: 2026-04-20
updated: 2026-05-12
type: entity
tags: [software-tvb, software-neuroimaging, whole-brain-modeling, python, neural-mass-models]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/schirner-2018.md, raw/papers/arxiv-2509.12873.md]
---

# _preamble

TVB Library (`tvb-library`) is the standalone Python simulation kernel of [[the-virtual-brain]], providing the computational engine and analysis infrastructure for [[whole-brain-modeling]]. Originally introduced as the simulation core of an open-source neuroinformatics platform [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]], the library enables researchers to construct large-scale brain network simulations using biologically realistic [[structural-connectivity]] derived from [[diffusion-imaging]] tractography. It implements forward models that translate neural activity into simulated [[eeg|EEG]], [[meg|MEG]], and [[fmri|fMRI]] signals, allowing direct comparison with empirical recordings [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]][[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. The library is designed to integrate subject-specific [[structural-connectivity]] matrices into personalized brain models capable of reproducing individual [[resting-state]] and evoked dynamics [[raw/papers/ritter-2013.md|Ritter et al. (2013)]][[raw/papers/schirner-2018.md|Schirner et al. (2018)]], and it serves as the simulation backend for automated pipelines and newer reproducibility frameworks such as the TVB Ontology [[raw/papers/semanticscholar-9afbfd2d37be.md|Martin et al. (2025)]][[raw/papers/arxiv-2509.12873.md|Gaglioti et al. (2025)]].