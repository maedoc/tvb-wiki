---
created: 2026-04-20
sources:
- raw/papers/david-friston-2003.md
- raw/papers/glean-github.md
- raw/papers/sanz-leon-2013.md
tags:
- software-brain-modeling
- dynamic-causal-modeling
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- effective-connectivity
- neural-mass-models
- whole-brain-modeling
title: SPM
type: entity
updated: '2026-05-19'
---

# SPM

**SPM** (Statistical Parametric Mapping) is a MATLAB-based software suite for the statistical analysis of brain imaging data sequences, including [[fmri]], PET, SPECT, EEG, and MEG. Developed at the Wellcome Centre for Human [[neuroimaging]] at University College London, it has become one of the most widely used neuroimaging analysis packages in computational neuroscience, serving as a foundational tool for both experimental studies and mechanistic modeling.

## Overview

SPM provides an integrated environment spanning preprocessing, statistical inference, and mechanistic modeling. Its functionality includes statistical parametric mapping for task-based and resting-state [[fmri]], kinetic modeling for PET and SPECT, electromagnetic source reconstruction for EEG and MEG, and [[dynamic-causal-modeling]] for inferring directed [[effective-connectivity]] through [[bayesian]] inversion of biophysically informed models [[raw/papers/david-friston-2003.md|Friston et al. (2003)]]. By combining general linear model-based inference with biophysical modeling, SPM enables researchers to move beyond mere description of activation patterns toward hypothesis-driven investigations of brain network mechanisms.

## Dynamic Causal Modeling

The Dynamic Causal Modeling module couples [[neural-mass-models]] to neuroimaging [[forward-model|forward models]] and inverts them via [[bayesian]] inference, explicitly separating neural state dynamics from observation equations [[raw/papers/david-friston-2003.md|Friston et al. (2003)]]. For [[fmri]], DCM employs a biophysical [[forward-model]] linking synaptic activity to the [[bold-signal|BOLD]] signal, whereas for EEG and MEG it uses an electromagnetic forward model grounded in the same neural mass dynamics [[raw/papers/david-friston-2003.md|Friston et al. (2003)]]. This theoretical architecture aligns closely with [[the-virtual-brain]], which integrates similar [[neural-mass-models]] with structural connectivity to simulate primate [[brain-network]] dynamics at the whole-brain scale [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Relationship to TVB

SPM and [[the-virtual-brain]] are complementary tools operating at different stages of the brain modeling pipeline. [[dcm]] estimates of [[effective-connectivity]] derived from SPM analyses can inform parameter selection for TVB simulations, creating a bridge from empirical inference to predictive [[whole-brain-modeling]] [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Preprocessing and source reconstruction outputs from SPM feed into TVB connectivity pipelines and model validation workflows. Conversely, TVB's large-scale simulations generate synthetic neuroimaging signals that can be compared against SPM-processed empirical data, closing the loop between simulation and observation [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The [[neural-mass-models]] at the heart of both frameworks ensure conceptual continuity across the inference-simulation boundary, allowing researchers to translate connectivity estimates from individuals into population-level dynamical predictions.

## Research Ecosystem

SPM sits within a broader neuroimaging analysis ecosystem that connects data preprocessing to network estimation and whole-brain simulation. Toolboxes such as GLEAN illustrate the extension of SPM-derived data into group-level network analyses that inform downstream computational modeling [[raw/papers/glean-github.md|Baker et al. (2015)]]. Because structural and functional [[connectivity]] estimates derived from SPM pipelines feed into [[the-virtual-brain]] simulations, improvements in SPM preprocessing propagate through the entire modeling chain from raw sensor data to large-scale [[network-dynamics]] [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. These dependencies underscore how SPM-derived empirical estimates serve as a foundation for computational workflows that span from statistical inference to mechanistic prediction.

## References

1. O. David, K.J. Friston. *Dynamic causal modelling*. NeuroImage. [DOI](https://doi.org/10.1016/S1053-8119(03)00202-7)
2. (authors unknown). *GLEAN: Group Level Exploratory Analysis of Networks*.
3. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)