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
SPM sits at the center of a broader neuroimaging analysis stack that ranges from preprocessing and source reconstruction to whole-brain simulation. The GLEAN toolbox, for example, is built directly on top of the SPM12 framework because SPM already provides validated source reconstruction and preprocessing pipelines for MEG and EEG data [[raw/papers/glean-github.md|Baker et al. (2015)]]. GLEAN leverages SPM's beamforming capabilities for source localization and its established routines for filtering and artifact rejection, as documented in SPM's own EEG-MEG analysis literature [[raw/papers/glean-github.md|Litvak et al. (2011)]], then adds group-level Hidden Markov Model and Independent Component Analysis decompositions on band-limited power time courses extracted from source-reconstructed data [[raw/papers/glean-github.md|Baker et al. (2015)]]. Because GLEAN operates on SPM-processed electrophysiology, improvements in SPM's preprocessing or beamforming propagate into downstream group-level [[connectivity]] analyses, creating a dependency chain from raw sensor data to network estimates.

At the simulation end of the pipeline, [[the-virtual-brain]] complements SPM by turning empirically derived connectivity estimates into large-scale dynamical models. TVB combines structural connectivity from diffusion MRI with [[neural-mass-models]] to generate simulated EEG, MEG, and fMRI signals that can be compared directly against empirical recordings [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The theoretical continuity with SPM is explicit: SPM's Dynamic Causal Modeling couples neural mass models to neuroimaging forward models and inverts them using Bayesian inference, separating neural state dynamics from observation equations [[raw/papers/david-friston-2003.md|David and Friston (2003)]]. TVB uses the same class of neural mass models to simulate [[connectivity]] across the whole brain [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]], so researchers frequently move from SPM-derived [[effective-connectivity]] estimates into TVB simulations, closing the loop between inference and prediction.
