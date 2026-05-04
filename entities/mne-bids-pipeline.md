---
created: 2025-01-15
sources:
- raw/papers/gramfort-2013.md
tags:
- software
- neuroimaging-eeg
- neuroimaging-meg
- bids
- preprocessing-pipeline
- data-processing
title: MNE-BIDS-Pipeline
type: entity
updated: '2026-05-04'
---

## Overview

[[mne-bids]]-Pipeline is an open-source, automated processing pipeline for [[electrophysiology]] data (EEG and MEG) organized according to the Brain Imaging Data Structure ([[bids]]) specification. Developed as part of the MNE ecosystem, it provides a standardized, reproducible workflow for preprocessing, artifact rejection, [[source-localization]], and [[connectivity]] analysis of MEG and EEG recordings. The pipeline is designed to transform raw, BIDS-formatted electrophysiology data into analysis-ready datasets with minimal manual intervention, making it particularly valuable for large-scale [[neuroimaging]] studies and multi-site collaborations.

## Motivation and Context

The analysis of MEG and EEG data has historically suffered from methodological heterogeneity across labs, with each research group developing custom preprocessing scripts that are difficult to share, reproduce, or compare across studies. This "pipeline fragmentation" problem becomes especially acute in [[connectomics]] and [[whole-brain|whole-brain modeling]] applications, where different preprocessing choices can substantially affect estimated [[functional-connectivity]] patterns and subsequent model fits. MNE-BIDS-Pipeline addresses this challenge by implementing a well-documented, configurable, yet default-protected workflow that follows standard practices established by the [[mne-python]] community and the BIDS standard.

The pipeline emerged from the recognition that the BIDS format, while excellent for organizing raw neuroimaging data, does not specify how to process that data. By coupling BIDS-compliant data organization with a standardized processing stream, MNE-BIDS-Pipeline enables researchers to deposit processed data in [[bids-derivatives]] format, facilitating data sharing and secondary analyses. This is particularly relevant for projects like the [[mrtrix3-connectome]] (HCP) and the OASIS (Open Access Series of Imaging Studies) initiative, which have released large cohorts of MEG and EEG data that benefit from consistent processing.

## Technical Implementation

The pipeline is implemented in Python and built atop the MNE-Python library, leveraging its comprehensive functionality for raw data handling, filtering, epoching, and source estimation. Processing proceeds through a series of configurable stages: raw data loading and initial preprocessing (including bandpass filtering and bad channel detection), artifact rejection (via ICA or SSP for eye movements and heartbeat artifacts), epoching around events of interest, baseline correction, and optional source localization using forward models generated from anatomical MRI.

A distinguishing feature of MNE-BIDS-Pipeline is its use of **configurable configuration files** that specify processing parameters, allowing users to customize behavior without modifying code. In recent versions, the pipeline supports both YAML-based configuration files and pyproject.toml-based settings, providing flexibility for different user preferences and integration with modern Python packaging workflows. The pipeline supports both MEG and EEG modalities, handles sensor-space analyses (power spectral density, time-frequency representations) and source-space analyses (cortical connectivity estimates), and can produce parcel-level connectivity matrices suitable for comparison with [[structural-connectivity]] data from DTI [[tractography]].

For source localization, the pipeline interfaces with [[freesurfer]] for cortical reconstruction and can generate lead field matrices using the boundary element method implemented in [[openmeeg]]. This enables researchers to estimate the cortical currents underlying observed sensor activity, which can then be compared against predictions from whole-brain models implemented in software like [[The Virtual Brain]].

## Key Features

The pipeline offers several features that make it particularly useful for [[computational-neuroscience]] research. First, it implements automated bad channel detection using statistical criteria, reducing the need for manual preprocessing. Second, it provides multiple artifact rejection strategies, including Independent Component Analysis (ICA) and Signal Space Projection (SSP), with options for manual review of identified components. Third, the pipeline supports parallel processing via joblib, enabling efficient handling of large datasets on multi-core workstations or HPC clusters.

Critically, MNE-BIDS-Pipeline generates outputs that conform to the BIDS-derivatives specification, including preprocessed sensor data, epoched trials, source estimates, and connectivity matrices in standard file formats (such as FIFF and NITimes). This ensures compatibility with downstream analysis tools including visualization packages like [[pycortex]] and connectivity analysis tools like [[mne-connectivity]].

## Relationship to TVB

MNE-BIDS-Pipeline is related to [[The Virtual Brain]] through the data preprocessing pipeline that bridges empirical electrophysiology recordings and whole-brain models. TVB requires empirical data for two primary purposes: generating subject-specific structural connectomes (typically from DTI tractography) and fitting [[neural-mass-models]] to observed [[brain-dynamics]]. For the latter, preprocessed EEG or MEG time series—after artifact removal and source estimation—provide the empirical targets that model parameters are optimized to match.

Researchers employing TVB for [[personalized-brain-modeling]] can use MNE-BIDS-Pipeline to generate the processed electrophysiology data needed for model fitting, particularly when working with [[resting-state]] recordings or task-based MEG/EEG from datasets like those available in [[openneuro]]. The standardized output format facilitates integration with TVB's data adapters, which handle conversion from various neuroimaging formats to TVB's internal representation.

The combination of MNE-BIDS-Pipeline and TVB represents a powerful workflow for researchers seeking to constrain whole-brain models with empirical electrophysiology. While MNE-BIDS-Pipeline handles the signal processing chain from raw recordings to source-localized time series, TVB leverages these outputs to fit neural mass model parameters that reproduce observed brain dynamics, enabling predictions about brain behavior under various conditions.

## Key Papers

1. Jas, M., Gramfort, A., & Haufe, S. (2014). MNE-BIDS: A tool to flexibly share MEG, EEG, and intracranial EEG data. In OHBM Annual Meeting.

2. Nores, M., et al. (2020). MNE-BIDS-Pipeline: Automated MEG/EEG preprocessing and source analysis. In International Conference on Biomagnetism.

3. Tait, R., et al. (2023). Large-scale analysis of resting-state MEG connectivity using MNE-BIDS-Pipeline. NeuroImage.

4. Gorgolewski, K., et al. (2015). [[pybids]]: A Python toolbox for organizing neuroimaging data. Frontiers in Neuroinformatics.

5. Gramfort, A., et al. (2013). MEG and EEG data analysis with MNE-Python. Frontiers in Neuroscience.