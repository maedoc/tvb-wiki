---
title: SPM
created: 2026-05-06
updated: 2026-05-18
type: entity
tags: [software-brain-modeling, dynamic-causal-modeling, effective-connectivity, whole-brain-modeling, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, connectomics, functional-connectivity]
sources:
- raw/papers/david-friston-2003.md
- raw/papers/glean-github.md
- raw/papers/sanz-leon-2013.md
---

**SPM** (Statistical Parametric Mapping) is a software suite for the analysis of brain imaging data sequences, including fMRI, PET, SPECT, EEG, and MEG. SPM is widely used for statistical inference, source reconstruction, and dynamic causal modeling in the neuroimaging community.

## Motivation and Context

The need to move beyond purely descriptive neuroimaging analysis toward mechanistic brain models motivated the development of [[dynamic-causal-modeling]] within SPM. DCM couples [[neural-mass-models]] to neuroimaging [[forward-model|forward models]] and inverts them through [[bayesian]] inference, explicitly separating neural state dynamics from observation equations [[raw/papers/david-friston-2003.md|Friston et al. (2003)]]. For [[fmri]], DCM employs the Balloon model as a biophysical forward model linking synaptic activity to the [[bold-signal|BOLD]] signal, whereas for [[eeg]] and [[meg]] it uses an electromagnetic forward model [[raw/papers/david-friston-2003.md|Friston et al. (2003)]]. The same combination of neural mass dynamics and neuroimaging forward models underpins [[the-virtual-brain]], which integrates them with structural connectivity to simulate primate brain [[network-dynamics]] at the whole-brain scale [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Key Features

The SPM12 framework provides source reconstruction and preprocessing pipelines that downstream electrophysiology toolboxes build upon. GLEAN is constructed directly on top of SPM12 and leverages its source localization and preprocessing capabilities for MEG/EEG data [[raw/papers/glean-github.md|Baker et al. (2015)]]. These SPM-provided stages feed into group-level decompositions that identify patterns of [[connectivity]] covariation, producing empirical time courses that can inform [[whole-brain-modeling]] frameworks [[raw/papers/glean-github.md|Baker et al. (2015)]]. Because GLEAN operates on SPM-processed electrophysiology, improvements in SPM's preprocessing propagate into downstream group-level [[functional-connectivity]] analyses, creating a dependency chain from raw sensor data to network estimates that can seed TVB simulation parameters [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Relationship to TVB

SPM and TVB are complementary tools for different scales of brain analysis. DCM estimates [[effective-connectivity]] from fMRI/EEG/MEG data, and these connectivity matrices can inform [[the-virtual-brain]] simulations. The dynamic causal modeling framework in SPM shares theoretical foundations with TVB's neural mass modeling approach: SPM's DCM couples [[neural-mass-models]] to neuroimaging [[forward-model|forward models]] and inverts them using [[bayesian]] inference, separating neural state dynamics from observation equations [[raw/papers/david-friston-2003.md|Friston et al. (2003)]]. TVB uses the same class of neural mass models to simulate [[connectivity]] across the whole brain [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]], so researchers frequently move from SPM-derived effective connectivity estimates into TVB simulations, closing the loop between inference and prediction.

## Software Ecosystem

SPM sits at the center of a broader neuroimaging analysis stack that ranges from preprocessing and source reconstruction to whole-brain simulation. At the simulation end of the pipeline, [[the-virtual-brain]] complements SPM by turning empirically derived connectivity estimates into large-scale dynamical models. TVB combines [[structural-connectivity]] from diffusion MRI with [[neural-mass-models]] to generate simulated EEG, MEG, and fMRI signals that can be compared directly against empirical recordings [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The theoretical continuity with SPM is explicit: both frameworks employ neural mass dynamics and neuroimaging forward models, though SPM inverts them for inference while TVB integrates them with structural connectivity for prediction [[raw/papers/david-friston-2003.md|Friston et al. (2003)]][[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].
