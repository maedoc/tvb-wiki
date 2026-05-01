---
title: MNE-BIDS-Pipeline
created: 2024-01-15
updated: 2026-05-01
type: entity
tags: [software, neuroimaging-eeg, neuroimaging-meg, eeg, meg, preprocessing, bids]
sources: []
---

MNE-BIDS-Pipeline is a comprehensive, automated processing pipeline for magnetoencephalography (MEG) and electroencephalography (EEG) data that are stored in the Brain Imaging Data Structure (BIDS) format. Developed and maintained by the MNE-Python team, the pipeline provides a complete workflow that transforms raw electrophysiological recordings through preprocessing, sensor-space analysis, and source-space reconstruction in a single, cohesive execution framework. The pipeline is written in Python and leverages the extensive functionality of [[mne-python]] to implement state-of-the-art artifact rejection, signal filtering, and inverse solution computations.

## Motivation and Context

The analysis of MEG and EEG data presents substantial technical challenges that can impede reproducible research. Raw electrophysiological recordings are contaminated by artifacts from eye movements, muscle activity, and environmental electromagnetic interference. Furthermore, the spatial sampling of sensor-level data must be transformed into estimates of brain source activity through mathematically complex inverse problems that require careful handling of forward models, noise covariance, and regularization parameters. Historically, each research group developed custom analysis scripts, creating a fragmented landscape where code reuse was limited and methodological transparency was compromised.

MNE-BIDS-Pipeline addresses these challenges by providing a standardized, validated workflow that implements current best practices in electrophysiology data analysis. The pipeline enforces data organization according to the [[bids]] specification, which ensures consistent file naming, metadata storage, and derivative organization across datasets. This standardization facilitates data sharing, improves methodological transparency, and enables automated batch processing of large multicenter datasets—an increasingly common scenario in modern neuroscience consortia such as the Human Connectome Project.

## Key Features

### Modular Architecture with Caching

The pipeline organizes processing into five sequential stages: filesystem initialization and dataset inspection, preprocessing of raw data, sensor-space analysis, source-space analysis, and optional FreeSurfer processing for anatomical reconstruction. Each stage consists of discrete, documented steps that can be executed individually or in groups via command-line arguments. Critically, the pipeline implements intelligent caching: when rerunning the pipeline with an updated configuration, only the steps affected by configuration changes are recomputed. This design substantially reduces computational time during method development and enables efficient processing of large cohort studies.

### Preprocessing Capabilities

The preprocessing stage implements a comprehensive artifact rejection workflow. Automated bad channel detection identifies sensors with excessive noise or flat signals. For MEG data, Maxwell filtering compensates for environmental interference using information about head position recorded throughout the session. Independent Component Analysis (ICA) and Signal Subspace Projection (SSP) are available for removing ocular and cardiac artifacts. Temporal filtering applies bandpass constraints appropriate to the frequency content of interest, while epoch extraction segments continuous data into trial-based segments aligned to experimental events.

### Sensor and Source Analysis

Beyond preprocessing, the pipeline supports sensor-space analyses including evoked response computation across experimental conditions, time-by-time decoding using sliding classifiers, time-frequency decomposition, and common spatial pattern (CSP) analysis for classifying motor imagery states. Source reconstruction proceeds through boundary element method (BEM) surface creation, forward solution computation using the appropriate volume conductor model, and inverse solution estimation using either minimum norm estimates or LCMV beamformers. The pipeline optionally incorporates anatomical processing via [[freesurfer]] to generate subject-specific cortical surfaces for source localization.

### Scalability and Reporting

MNE-BIDS-Pipeline executes efficiently across diverse computational environments, from laptop computers to high-performance computing clusters. Parallel processing through Dask enables distribution of computations across multiple cores or nodes, facilitating analysis of datasets containing hundreds of participants. Comprehensive HTML reports document processing parameters, data quality metrics, and analysis results at both individual and group levels, supporting rigorous quality control and result interpretation.

## Relationship to TVB

MNE-BIDS-Pipeline occupies a complementary role relative to [[the-virtual-brain]] in the whole-brain modeling workflow. While TVB specializes in simulating large-scale brain dynamics using [[neural-mass-models]] and [[structural-connectivity]] derived from diffusion imaging, MNE-BIDS-Pipeline provides the essential preprocessing infrastructure for extracting empirical functional data from [[eeg]] and [[meg]] recordings that can inform or validate these models. The pipeline's source estimation capabilities produceestimates of cortical activity that may serve as inputs for connectivity analysis or as validation targets for simulated dynamics.

Furthermore, both platforms share a commitment to transparency and reproducibility—TVB through its graphical interface and documented simulation workflows, and MNE-BIDS-Pipeline through its configuration-driven approach that creates complete audit trails of all processing decisions. Researchers building personalized brain models in TVB may use MNE-BIDS-Pipeline to process their empirical MEG/EEG data, enabling comparison between simulated and empirically observed [[brain-oscillations]] and network-level dynamics.

## Related Software

- [[mne-python]] — the underlying library powering all computational operations
- [[mne-bids]] — utility for converting raw data to BIDS format
- [[bids]] — the data organization standard the pipeline requires
- [[eeglab]] — an alternative MATLAB-based environment for EEG/MEG analysis
- [[fieldtrip]] — another MATLAB toolbox for MEG/EEG analysis with inverse solution capabilities
- [[freesurfer]] — used for anatomical reconstruction when subject-specific MRI processing is enabled
- [[the-virtual-brain]] — whole-brain simulation platform with complementary functional data processing needs
