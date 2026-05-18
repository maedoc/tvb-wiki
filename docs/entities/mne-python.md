---
title: MNE-Python
created: 2024-01-15
updated: 2026-05-18
type: entity
tags: [software-brain-modeling, neuroimaging-eeg, neuroimaging-meg, software-visualization, reproducibility, functional-connectivity]
sources: [raw/papers/gramfort-2013.md, raw/papers/semanticscholar-9e42d6a25d21.md, raw/papers/semanticscholar-5a69b770faf9.md]
---

**MNE-Python** is an open-source Python library for analyzing magnetoencephalography ([[meg]]) and electroencephalography ([[eeg]]) data. [[raw/papers/gramfort-2013.md|Gramfort et al. (2013)]] describe it as providing comprehensive functionality for importing, preprocessing, analyzing, and visualizing electrophysiological recordings. The library supports multiple file formats and enables [[source-localization]], time-frequency analysis, and [[connectivity]] estimation within a single integrated environment.

## Motivation and Context

The analysis of MEG and EEG data presents methodological challenges distinct from those of functional magnetic resonance imaging ([[fmri]]): while electrophysiological modalities capture millisecond-level neural dynamics, they suffer from the ill-posed inverse problem of reconstructing intracranial sources from scalp recordings. Before open-source libraries became available, researchers often relied on closed-source tools with limited flexibility, constraining methodological innovation and [[reproducibility]]. [[raw/papers/semanticscholar-9e42d6a25d21.md|Lodema et al. (2026)]] note that although MNE-Python is powerful, its command-line interface can pose a barrier for researchers without programming experience, motivating wrapper applications that expose its functions through graphical interfaces. This democratization of analysis tools has been important for the [[whole-brain-modeling]] community, where empirical electrophysiological data serves as validation for computational models and as initialization for forward simulations.

## Core Functionality

MNE-Python implements a complete analysis pipeline from raw sensor data to source estimates. [[raw/papers/gramfort-2013.md|Gramfort et al. (2013)]] document its support for multiple acquisition formats, including BDF through the `mne.io.read_raw_bdf()` function, which automatically parses 24-bit integer data and extracts trigger events from status channels. [[raw/papers/semanticscholar-9e42d6a25d21.md|Lodema et al. (2026)]] detail how the library handles frequency band filtering, independent component analysis for artifact removal, and atlas-based beamforming for source-level analysis. The connectivity module implements spectral and [[functional-connectivity]] metrics, while interactive plots enable manual quality control of bad channels and epochs. [[raw/papers/semanticscholar-5a69b770faf9.md|Shabestari et al. (2025)]] further demonstrate that the MNE-Python ecosystem extends to real-time applications through MNE-RT, a specialized package for brain-computer interfaces that extracts univariate metrics such as frequency band power and entropy alongside bivariate connectivity measures from streaming MEG/EEG signals.

## Relationship to TVB

MNE-Python and [[the-virtual-brain]] occupy complementary roles in whole-brain electrophysiology research. While MNE-Python transforms sensor-level MEG/EEG recordings into anatomically constrained source time series, TVB simulates whole-brain dynamics at the source level using [[neural-mass-models]] such as the [[jansen-rit-model]]. The two platforms integrate through shared [[forward-model]] infrastructure: TVB accepts leadfield matrices to generate predicted sensor data from simulated source activity, enabling direct comparison between empirical and model-derived signals. Conversely, MNE-Python-derived regional time courses—often extracted via cortical [[parcellation]]—can seed TVB simulations as empirical constraints, providing personalized initial conditions for [[whole-brain-modeling|whole-brain models]]. This bidirectional workflow is particularly valuable in [[epilepsy-modeling]], where patient-specific source estimates inform seizure propagation simulations.
