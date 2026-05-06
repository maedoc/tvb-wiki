---
created: 2026-05-06
sources:
- raw/papers/david-friston-2003.md
- raw/papers/glean-github.md
- raw/papers/sanz-leon-2013.md
tags:
- software-spm
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- statistics
- image-processing
title: SPM
type: entity
updated: '2026-05-06'
---

# SPM

**SPM** (Statistical Parametric Mapping) is a software suite for the analysis of brain imaging data sequences ([[fmri]], PET, SPECT, EEG, MEG). Developed at the Wellcome Centre for Human [[neuroimaging]] at University College London, SPM is one of the most influential neuroimaging analysis packages.

## Overview

SPM is built on MATLAB and provides:
- fMRI preprocessing and statistical inference
- PET/SPECT kinetic modeling
- EEG/MEG source reconstruction and time-series analysis
- Dynamic Causal Modeling (DCM) for [[effective-connectivity]]
- [[bayesian]] model selection and averaging

## Core Modules

| Module | Purpose |
|--------|---------|
| **SPM-fMRI** | Preprocessing (realignment, normalization, smoothing) and GLM analysis |
| **SPM-PET** | PET kinetic modeling and statistical analysis |
| **SPM-EEG/MEG** | EEG/MEG preprocessing, source reconstruction, time-frequency analysis |
| **DCM** | Dynamic Causal Modeling for effective connectivity |
| **VBM** | Voxel-based morphometry for structural analysis |

## Relationship to TVB

SPM and TVB are complementary tools for different scales of brain analysis:
- **DCM** (Dynamic Causal Modeling) estimates effective [[connectivity]] from fMRI/EEG/MEG data — these connectivity matrices can inform TVB simulations
- **Source reconstruction** (SPM-EEG) provides empirical time series for TVB [[model-validation]]
- **fMRI preprocessing** outputs from SPM feed into TVB connectivity pipelines
- SPM's **VBM** structural analysis provides atrophy maps for disease modeling in TVB
- The [[dynamic-causal-modeling]] framework in SPM shares theoretical foundations with TVB's neural mass modeling approach

## Dynamic Causal Modeling

SPM's DCM is particularly relevant to TVB:
- DCM estimates directed connectivity using Bayesian inference
- DCM for fMRI uses a biophysical [[forward-model]] (Balloon model) similar to TVB's [[bold-signal|BOLD]] modeling
- DCM for MEG/EEG uses [[neural-mass-models]] ([[jansen-rit]], Moran-David) that are also implemented in TVB
- DCM connectivity estimates can seed TVB simulation parameters
- [[dcm]] pages detail the mathematical connections between the two frameworks

## Software Ecosystem

- [[fsl]] — alternative fMRI analysis
- [[eeglab]] — alternative EEG analysis
- fieldtrip — alternative MEG/EEG analysis
- [[the-virtual-brain]] — [[whole-brain]] simulation using DCM-derived connectivity

## References

- SPM website: https://www.fil.ion.ucl.ac.uk/spm/
- Friston et al. (1994) — Statistical parametric maps in functional imaging
- Friston et al. (2003) — Dynamic causal modelling
- Penny et al. (2004) — Comparing dynamic causal models