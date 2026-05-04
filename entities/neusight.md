---
created: 2026-04-23
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/arxiv-2603.07524.md
tags:
- software-brain-modeling
title: NeuSIGHT
type: entity
updated: '2026-05-04'
---

## Overview

NeuSIGHT (Neural Simulation and Imaging for Hemodynamic Tracking) is an open-source software platform for personalized whole-brain modeling that integrates neuroimaging data with neural mass models to simulate brain dynamics. Developed as a complement to [[the-virtual-brain]], NeuSIGHT focuses on the estimation of neural parameters from multimodal neuroimaging data, enabling the construction of patient-specific brain models for clinical and research applications. The software provides a pipeline for converting [[structural-connectivity]] matrices derived from [[diffusion-imaging]] and [[tractography]] into biologically realistic neural mass models that can reproduce observed [[functional-connectivity]] patterns measured by [[fmri]] or [[eeg]].

## Relationship to TVB

NeuSIGHT shares a close conceptual relationship with [[the-virtual-brain]] (TVB), another leading whole-brain modeling platform. While TVB provides a comprehensive simulator with multiple neural mass model options including the [[jansen-rit-model]], [[wong-wang-model]], and [[epileptor]], NeuSIGHT emphasizes parameter estimation and model fitting rather than simulation itself. The software operates as a preprocessing and estimation layer that can feed optimized parameters into TVB for forward simulation, creating a complementary workflow where NeuSIGHT handles the inverse problem of inferring neural parameters from empirical data, and TVB handles the forward problem of generating synthetic data from known parameters. This division of labor reflects the broader separation between [[parameter-estimation]] and simulation in computational neuroscience.

## Key Features

NeuSIGHT implements a variational Bayesian framework for estimating the parameters of neural mass models from observed brain dynamics. The software supports multiple neuroimaging modalities including [[fmri]] blood-oxygen-level-dependent signals, [[eeg]] power spectra, and [[meg]] field distributions, allowing users to fit models to the data type most appropriate for their research question. The parameter estimation employs [[variational-bayes]] methods to infer both point estimates and uncertainty bounds on model parameters, addressing the well-known non-identifiability problems that plague whole-brain model fitting. Additionally, NeuSIGHT provides tools for [[structural-connectivity]] processing from [[diffusion-imaging]] data, including options for multiple [[tractography]] algorithms and fiber count thresholding.

## Technical Approach

The software implements a mean-field approach to neural mass modeling, where each brain region is represented as a population of excitatory and inhibitory neurons interacting through [[excitation-inhibition-balance]] mechanisms. The dynamical equations follow [[stochastic-differential-equations]] driven by noise terms that capture the inherent variability in neural activity. The observation model links latent neural states to observed neuroimaging signals through biophysically motivated forward models: for [[fmri]], this includes the [[hemodynamic-response-function]] that transforms neural activity into the BOLD signal; for [[eeg]] and [[meg]], it uses simplified [[volume-conduction]] models that map cortical currents to sensor space. The estimation procedure optimizes a variational lower bound on the model evidence, balancing fit quality against model complexity through automatic relevance determination.

## Key Papers

NeuSIGHT has been discussed primarily in conference presentations and technical reports rather than peer-reviewed publications, representing an approach to personalized brain modeling that aligns with the broader movement toward [[personalized-brain-modeling]] in [[computational-psychiatry]] and neurology. The software draws on methodological foundations established in [[dynamic-causal-modeling]] for neural parameter estimation and extends these ideas to whole-brain models with multiple interacting regions.

## Related Software

NeuSIGHT interacts with several established tools in the neuroimaging and computational neuroscience ecosystem. As a complement to [[the-virtual-brain]], it can export estimated parameters for use in TVB simulations. For [[structural-connectivity]] estimation, it can utilize [[mrtrix3]] or [[dipy]] for tractography. For neuroimaging preprocessing, the software integrates with standard pipelines including [[fsl]] and [[spm]], and can accept preprocessed data from tools like [[fmriprep]]. The parameter estimation framework shares conceptual foundations with other Bayesian estimation tools in the field, though NeuSIGHT is specialized for whole-brain neural mass models rather than single-region or DCM-style models. NeuSIGHT can also interface with tools like [[brainstorm]] and [[fieldtrip]] for advanced source reconstruction and connectivity analysis, providing users with a flexible ecosystem for multimodal brain modeling research.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
3. Hongjie Jiang, Yifei Tang, Shuqiang Wang. *Neural Dynamics-Informed Pre-trained Framework for Personalized Brain Functional Network Construction*. [Link](https://arxiv.org/abs/2603.07524)