---
title: MEG/EEG Toolbox
created: 2025-01-01
updated: 2026-05-03
type: entity
tags: [software, neuroimaging-meg, neuroimaging-eeg, software-fieldtrip, source-localization, time-frequency-analysis, connectivity, electrophysiology]
sources: []
---

The MEG/EEG Toolbox (commonly known as **FieldTrip**) is a comprehensive MATLAB software toolbox for analyzing magnetoencephalography (MEG), electroencephalography (EEG), and intracranial electrophysiological (iEEG/SEEG/ECoG) data. It is developed and maintained by the Donders Institute for Brain, Cognition and Behaviour at Radboud University in Nijmegen, the Netherlands, with contributions from collaborators at institutions worldwide.

## Overview

FieldTrip provides researchers with a flexible, open-source platform for preprocessing, analyzing, and visualizing electromagnetic brain signals. Unlike commercial analysis packages that offer fixed preprocessing pipelines, FieldTrip functions as a library of modular components that users combine to construct custom analysis protocols in MATLAB. This design philosophy enables both novice users to apply established analysis routines through provided tutorials and advanced researchers to implement novel methods for electromagnetic brain imaging.

The toolbox supports data formats from all major MEG systems—including CTF, Neuromag/Elekta/Megin, BTi/4D, Yokogawa/Ricoh, and FieldLine—and most popular EEG systems. New formats can be added through user-defined reading functions, making the toolbox highly extensible.

## Key Features

### Preprocessing and artifact handling
FieldTrip provides comprehensive preprocessing functions for importing raw data, applying digital filters (high-pass, low-pass, band-pass, and notch filters for line noise removal), epoching data around experimental events, and handling artifacts. The toolbox implements both automated and semi-automated artifact rejection procedures for eye movements, muscle artifacts, and bad channels. Artifact detection routines can operate on raw continuous data or segmented epochs, enabling researchers to clean large datasets efficiently.

### Time-frequency analysis
The toolbox supports time-frequency decomposition using multiple methods including short-time Fourier transform, wavelet convolution (Morlet wavelets), and multitaper spectral estimation. Researchers can compute event-related synchronization/desynchronization (ERS/ERD), inter-trial coherence, and phase-locking value (PLV) analyses. Time-frequency representations can be visualized as power spectra over time, topographic maps, or frequency-by-time plots.

### Source reconstruction
One of FieldTrip's core strengths is its implementations of source localization algorithms. The toolbox supports multiple approaches to reconstructing neuronal activity from sensor data: **dipole fitting** (equivalent current dipole localization), **distributed source models** (minimum norm estimation, LAURA, LORETA, sLORETA, and weighted minimum norm), and **beamformers** (LCMV, SAM, and DICS). Forward modeling capabilities include spherical conductor models, boundary element methods (BEM), and finite element methods (FEM) for realistic head modeling.

### Connectivity analysis
FieldTrip implements a broad range of functional and effective [[connectivity]] metrics including coherence, phase-locking value, partial coherence, correlation, and transfer entropy. For effective [[connectivity-types]] estimation, the toolbox includes implementations of **dynamic causal modeling (DCM)** for MEG/EEG (via integration with [[spm]]), as well as granger causality and cross-frequency coupling measures. The connectivity routines enable analysis of cortical networks during resting state or task conditions.

### Statistical inference
The toolbox provides non-parametric statistical testing procedures specifically designed for neuroimaging data. These include cluster-based permutation tests that address the multiple comparison problem inherent in high-density sensor or source space analyses. Statistical functions support both within-subject and between-group comparisons, with options for false discovery rate (FDR) correction and family-wise error rate (FWER) control.

## Relationship to TVB and Whole-Brain Modeling

FieldTrip plays a complementary role to [[the-virtual-brain]] in the broader ecosystem of [[whole-brain-modeling]]. While TVB focuses on constructing and simulating large-scale computational models of brain dynamics, FieldTrip provides the analysis pipeline for empirical MEG/EEG data that can be used to **parameterize**, **validate**, and **compare** with such models.

In practice, researchers often use FieldTrip to analyze empirical resting-state or task-based MEG/EEG data to extract:
- **Empirical functional networks** derived from sensor or source-level connectivity patterns
- **Oscillatory dynamics** including peak frequencies, bandwidths, and reactivity of [[brain-oscillations]] such as alpha (8-12 Hz), beta (13-30 Hz), and gamma (30-100 Hz) bands
- **Evoked and induced responses** that can be compared with model-generated dynamics
- **Phase-amplitude coupling** and other cross-frequency interactions that inform [[neural-mass-model]] design

The combination of FieldTrip analysis and TVB simulation enables the **personalized brain modeling** approach described in the TVB framework, where individual subject's empirical connectivity patterns (derived from MEG/EEG or [[fmri]] data) are used to constrain model parameters [[personalized-brain-modeling]].

## Relationship to Other Software

FieldTrip has formal collaborative relationships with other major neuroimaging software packages:

- **[[spm]]**: FieldTrip and [[spm]] share routines for data conversion, digital filtering, spectral estimation, and forward modeling. SPM contains a version of FieldTrip, allowing users to combine both toolboxes in custom scripts. SPM focuses on specific analysis methods (particularly Bayesian source reconstruction and [[dynamic-causal-modeling]]), while FieldTrip provides a more general repository of diverse methods.

- **[[eeglab]]**: While EEGLAB provides a graphical user interface (GUI) optimized for interactive processing, FieldTrip offers a script-based workflow better suited for batch processing and reproducibility. Both toolboxes complement each other, with EEGLAB's GUI accessibility complemented by FieldTrip's flexibility for advanced users.

- **[[mne-python]]**: The MNE-Python project represents a Python-based alternative to FieldTrip's MATLAB implementation. Both tools share similar analysis philosophies and increasingly share underlying algorithms, reflecting broader efforts toward open-source neuroscience software interoperability.

## Key Contributors and Citations

The primary developers of FieldTrip include Robert Oostenveld, Jan-Mathijs Schoffelen, Pascal Fries, Eric Maris, and numerous other contributors from the Donders Institute and collaborating laboratories worldwide. The canonical citation for the toolbox is:

> Oostenveld R, Fries P, Maris E, Schoffelen JM. FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data. *Computational Intelligence and Neuroscience*. 2011; 156869.

## Related Software

- [[eeglab]] - EEGLAB toolbox (alternative MEG/EEG toolbox with GUI)
- [[spm]] - Statistical Parametric Mapping (includes M/EEG functionality)
- [[mne-python]] - Python-based MEG/EEG analysis
- [[the-virtual-brain]] - Whole-brain modeling simulator
- [[brain-connectivity-toolbox]] - Graph theory network analysis
- [[connectome-workbench]] - Visualisation and analysis of connectivity data