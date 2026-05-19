---
created: 2024-01-15
sources:
- raw/papers/gramfort-2013.md
- raw/papers/semanticscholar-9e42d6a25d21.md
- raw/papers/semanticscholar-5a69b770faf9.md
tags:
- software-brain-modeling
- neuroimaging-eeg
- neuroimaging-meg
- software-visualization
- reproducibility
- functional-connectivity
- resting-state
title: MNE-Python
type: entity
updated: '2026-05-19'
---

**MNE-Python** is an open-source Python library for analyzing magnetoencephalography ([[meg]]) and electroencephalography ([[eeg]]) data. [[raw/papers/gramfort-2013.md|Gramfort et al. (2013)]] describe it as providing comprehensive functionality for importing, preprocessing, analyzing, and visualizing electrophysiological recordings, with support for multiple acquisition file formats. The library enables [[source-localization]], time-frequency analysis, and [[connectivity]] estimation within a single integrated environment, making it a cornerstone tool for translating sensor-level recordings into anatomically interpretable source-space estimates.

## Motivation and Context

The analysis of MEG and EEG data presents methodological challenges distinct from those of functional magnetic resonance imaging ([[fmri]]): while electrophysiological modalities capture millisecond-level neural dynamics, they suffer from the ill-posed inverse problem of reconstructing intracranial sources from scalp recordings. Before open-source libraries became available, researchers often relied on closed-source tools with limited flexibility, constraining methodological innovation and [[reproducibility]]. [[raw/papers/semanticscholar-9e42d6a25d21.md|Lodema et al. (2026)]] note that although MNE-Python is powerful, its command-line interface can pose a barrier for researchers without programming experience, motivating wrapper applications such as EEG-Pype that expose its functions through graphical interfaces. This democratization of analysis tools has been important for the [[whole-brain-modeling]] community, where empirical electrophysiological data serves as validation for computational models and as initialization for forward simulations.

## Core Functionality

MNE-Python implements a complete analysis pipeline from raw sensor data to source estimates. [[raw/papers/gramfort-2013.md|Gramfort et al. (2013)]] document its support for multiple acquisition formats, including BDF through the `mne.io.read_raw_bdf()` function, which automatically parses 24-bit integer data, converts it to float32, and extracts trigger events from status channels for downstream epoching. [[raw/papers/semanticscholar-9e42d6a25d21.md|Lodema et al. (2026)]] detail how the library handles frequency band filtering, independent component analysis for artifact removal, and atlas-based beamforming for source-level analysis, alongside interactive plots for manual quality control of bad channels and epochs. The connectivity module implements spectral and [[functional-connectivity]] metrics, and configuration saving enables batch reruns with improved documentation. [[raw/papers/semanticscholar-5a69b770faf9.md|Shabestari et al. (2025)]] further demonstrate that the ecosystem extends to real-time applications through MNE-RT, a specialized package for brain-computer interfaces that extracts univariate metrics such as frequency band power and entropy alongside bivariate connectivity measures from streaming MEG/EEG signals.

## Ecosystem and Extensions

The MNE-Python ecosystem has grown beyond the core library to address diverse user needs. [[raw/papers/semanticscholar-9e42d6a25d21.md|Lodema et al. (2026)]] present EEG-Pype, an open-source graphical interface built on MNE-Python that targets preprocessing of [[resting-state]] EEG data, guiding clinicians and non-programmers through filtering, ICA, and atlas-based beamforming while saving logs for reproducibility. [[raw/papers/semanticscholar-5a69b770faf9.md|Shabestari et al. (2025)]] introduce MNE-RT for real-time neural feature extraction, compatible with various recording systems and designed to enhance neurofeedback efficacy in brain-computer interface systems. These extensions illustrate how the core library serves as a computational backend for specialized interfaces ranging from standardized batch pipelines to online signal processing.

## Relationship to TVB

MNE-Python and [[the-virtual-brain]] occupy complementary roles in whole-brain electrophysiology research. While MNE-Python transforms sensor-level MEG/EEG recordings into anatomically constrained source time series, TVB simulates whole-brain dynamics at the source level using [[neural-mass-models]] such as the [[jansen-rit-model]]. The two platforms integrate through shared [[forward-model]] infrastructure: TVB accepts leadfield matrices to generate predicted sensor data from simulated source activity, enabling direct comparison between empirical and model-derived signals. Conversely, MNE-Python-derived regional time courses—often extracted via cortical [[parcellation]]—can seed TVB simulations as empirical constraints, providing personalized initial conditions for [[whole-brain-modeling|whole-brain models]]. This bidirectional workflow is particularly valuable in [[epilepsy-modeling]], where patient-specific source estimates inform seizure propagation simulations.

## References

1. Gramfort et al. (2013). *MEG and EEG: From Acquisition to Analysis*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fnins.2013.00010)
2. D. Y. Lodema, Herman J van Dellen, W. de Haan, Margot van Hest, A. Hillebrand, E. van Dellen. (2026). *EEG-Pype: An accessible MNE-Python pipeline with graphical user interface for preprocessing and analysis of resting-state electroencephalography data.*. PLoS Computational Biology. [DOI](https://doi.org/10.1371/journal.pcbi.1014043)
3. P. S. Shabestari, Delphine Ribes, Lara Défayes, Danpeng Cai, Emily Groves, Harry H. Behjat, D. Van de Ville, Tobias Kleinjung, A. Naas, N. Henchoz, A. Sonderegger, Patrick Neff. (2025). *Advances on Real Time M/EEG Neural Feature Extraction*. 2025 IEEE 38th International Symposium on Computer-Based Medical Systems (CBMS). [DOI](https://doi.org/10.1109/CBMS65348.2025.00074)