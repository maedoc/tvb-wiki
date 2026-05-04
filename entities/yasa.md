---
created: 2026-04-23
sources:
- raw/papers/semanticscholar-2a455dab8f2b.md
- raw/papers/smith-2013-connectomics.md
- raw/papers/arxiv-2604.16463.md
- raw/papers/semanticscholar-5f7f3cdfe9e8.md
tags:
- software-brain-modeling
- neuroimaging-eeg
- brain-oscillations
title: YASA
type: entity
updated: '2026-04-30'
---

# YASA

## Overview

YASA (Yet Another Spindle Algorithm) is an open-source Python toolbox designed for automated analysis of polysomnographic (PSG) sleep recordings Vallat2021. Developed primarily by Raphael Vallat and colleagues, YASA provides a comprehensive suite of functions for processing multi-channel electroencephalography (EEG) data collected during sleep studies. The software enables automated sleep staging, detection of sleep events such as sleep spindles and slow-waves, artifact rejection, spectral analysis, and hypnogram manipulation. Originally conceived as an algorithm for detecting sleep spindles—characteristic oscillatory events occurring during NREM sleep—YASA has evolved into a broadly applicable sleep research platform widely adopted in both academic and clinical settings.

## Key Features

YASA offers an extensive range of functionalities tailored for sleep research and clinical polysomnography analysis. The software's automated sleep staging capability employs machine learning classifiers to predict sleep stages (Wake, N1, N2, N3, and REM) from single or multi-channel EEG recordings, achieving accuracy rates comparable to expert human scorers when validated against gold-standard manual annotations Vallat2021. This automated staging function is particularly valuable for processing large datasets where manual scoring would be prohibitively time-consuming.

The event detection module forms a core component of YASA's functionality. The software implements validated algorithms for automatic detection of sleep spindles (12-16 Hz oscillatory events characteristic of stage N2 and N3 sleep) Lacourse2018 Bertrand2018, slow-waves (0.5‑4 Hz high‑amplitude waves central to deep sleep), and rapid eye movements (REMs) that define REM sleep. Detection parameters are tunable, allowing researchers to adjust sensitivity thresholds based on their specific data characteristics and research requirements. The output includes detailed summaries of detected events with metrics such as frequency, amplitude, duration, and topographic distribution across recording channels.

Spectral analysis capabilities in YASA extend beyond simple bandpower calculations. The toolbox implements Welch's method for power spectral density estimation Vallat2021, enabling quantification of EEG power in standard frequency bands (delta, theta, alpha, beta, gamma) with options for both absolute and relative power calculations. Advanced features include phase‑amplitude coupling analysis, 1/f slope estimation (characterizing the aperiodic component of the EEG spectrum) Vallat2021, and full‑night spectrogram visualization. These spectral features are computable either across the entire recording or segmented by sleep stage, enabling sophisticated characterizations of sleep micro‑structure.

Additional utilities include artifact rejection algorithms for identifying and removing epochs contaminated by eye movements, muscle artifacts, or electrode artifacts. The hypnogram manipulation tools support loading standard sleep stage files, computing sleep statistics (total sleep time, sleep efficiency, sleep latency, wake after sleep onset), generating stage transition matrices, and visualizing sleep architecture. YASA interfaces seamlessly with data formats commonly used in sleep research, including European Data Format (EDF) and BioSemi formats Vallat2021, and can be integrated with the MNE‑Python ecosystem for enhanced preprocessing pipelines.

## Relationship to Whole‑Brain Modeling and TVB

While YASA is primarily positioned in the sleep research domain rather than directly within the [[whole-brain|whole-brain modeling]] ecosystem, it maintains relevant connections to [[computational-neuroscience]] workflows. The detection and analysis of sleep spindles and slow‑waves aligns with broader research into [[brain-oscillations]] and neural mass model representations of cortical dynamics. Sleep oscillations emerge from the coordinated activity of large neuronal populations, and characterizing their properties using YASA can inform the parameterization of [[neural-mass-models]] that simulate similar oscillatory behavior during wakefulness or disease states such as [[epilepsy-modeling]].

From a neuroimaging perspective, YASA processes [[EEG]] data that can be compared against [[fMRI]] measurements or used to validate forward models linking neural activity to electromagnetic fields. The spectral analysis features enable characterization of frequency‑specific neural activity that relates to the [[neural‑mass‑model]] framework used in [[whole‑brain‑modeling]] platforms like [[TVB]]. Sleep deprivation and sleep quality have been shown to alter functional brain connectivity patterns Campruzi2020, and tools like YASA that enable detailed sleep phenotyping can contribute to personalized brain modeling by providing subject‑specific physiological state information.

In practical workflows, YASA may be used in conjunction with [[MNE‑Python]] for comprehensive EEG preprocessing, or its output may be correlated with [[functional‑connectivity]] metrics derived from resting‑state [[fMRI]] data. The software represents a specialized tool within the broader [[neuroimaging]] ecosystem, complementing general‑purpose EEG analysis platforms like [[EEGLab]] while providing domain‑specific functionality for sleep research that is not directly replicated in whole‑brain simulation frameworks. Within the TVB context, YASA serves as a preprocessing and signal analysis layer that can provide physiologically‑informed parameters for whole‑brain models.

## Key Papers

The primary citation for YASA is Vallat and Walker (2021), published in eLife, which introduced the automated sleep staging algorithm and demonstrated its performance against expert human scorers across multiple datasets Vallat2021. This paper established YASA's credibility as a research‑grade tool and remains the standard reference for citations. The software documentation and GitHub repository provide extensive tutorials and examples that supplement the primary publication, including detailed notebooks demonstrating event detection, spectral analysis, and integration with MNE‑Python preprocessing pipelines.

Additional important references include Lacourse et al. (2018), which established the spindle detection methodology upon which YASA's detection algorithms are built Lacourse2018, and Bertrand et al. (2018), which provided validation for automated slow‑wave detection approaches incorporated in the toolbox Bertrand2018.

## Related Software

YASA operates within the broader EEG and sleep analysis software ecosystem. As a Python‑based toolbox, it shares the scientific computing foundation with [[MNE‑Python]] for raw data handling and preprocessing, [[EEGLab]] (primarily MATLAB‑based but with Python equivalents), and fieldtrip (MATLAB‑based). For sleep‑specific analysis, YASA competes with and complements tools such as SleepTrip (built on MNE‑Python) and various commercial polysomnography analysis packages. Within the TVB Wiki context, YASA relates most closely to software involved in [[neuromorpho‑toolkit]] processing, [[brain‑oscillations]] analysis, and ultimately connects to [[TVB]] for whole‑brain modeling workflows.

## Technical Implementation

YASA is implemented in Python and depends on scientific computing libraries including NumPy, SciPy, Pandas, and MNE‑Python for certain operations. The software is distributed via PyPI and conda‑forge, facilitating straightforward installation via standard Python package managers. The codebase emphasizes performance optimization for handling full‑night polysomnography recordings, which may contain millions of data points across multiple EEG channels. Detection algorithms implement validated approaches from the sleep research literature, with the spindle detection method based on the algorithm described by Lacourse et al. (2018) Lacourse2018. The sleep staging module employs a trained classifier approach, with the specific algorithm details available in the eLife publication Vallat2021.