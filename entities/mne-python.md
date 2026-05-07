---
created: 2024-01-15
sources:
- gramfort2013
- gramfort2014
- hauk2004
- lin2006
- dalal2014
- pisetta2024
- jansen1993
- raw/papers/gramfort-2013.md
tags:
- software
- neuroimaging-eeg
- neuroimaging-meg
- software-visualization
- source-localization
title: MNE-Python
type: entity
updated: '2026-05-07'
---

**MNE-Python** is an open-source Python library for the analysis of magnetoencephalography (MEG), electroencephalography (EEG), stereotactic EEG (sEEG), and electrocorticography (ECoG) data. Developed primarily at the Martinos Center for Biomedical Imaging at Massachusetts General Hospital, MNE-Python provides comprehensive tools for preprocessing, [[source-localization]], time-frequency analysis, statistical inference, and visualization of neurophysiological data. The library implements the minimum norm estimation (MNE) method after which it is named, along with numerous other inverse solving approaches, making it a cornerstone tool for translating sensor-level recordings into anatomically interpretable source-space estimates.

## Motivation and Context

The analysis of MEG and EEG data presents significant computational and methodological challenges that motivated the development of MNE-Python. Unlike functional magnetic resonance imaging ([[fmri]]), which offers excellent spatial resolution but poor temporal resolution, electrophysiological modalities provide millisecond-level temporal precision but suffer from ambiguous spatial reconstruction due to the ill-posed inverse problem of source localization. Before MNE-Python, researchers often relied on closed-source commercial software with limited flexibility, restricting methodological innovation and [[reproducibility]]. The library emerged to fill this gap by providing a freely accessible, extensible, and well-documented platform that implements state-of-the-art algorithms from the literature while enabling customization for specialized research questions. This democratization of analysis tools has been particularly important for the [[whole-brain|whole-brain modeling]] community, where empirical electrophysiological data serves as both validation for computational models and as initialization for forward simulations.

## Core Functionality

MNE-Python implements a complete analysis pipeline from raw sensor data to refined source estimates. The preprocessing module handles filtering (bandpass, notch, and high-pass), artifact rejection (EOG, ECG, and muscle artifacts), independent component analysis (ICA) for blind [[source-separation]], and raw data visualization for quality control. The library supports all standard data formats including FIF (Neuromag), BrainVision, EDF, and [[bids]]-compliant datasets, facilitating integration with diverse acquisition systems. For source localization, MNE-Python provides multiple inverse solutions including minimum norm estimation (MNE), weighted minimum norm estimation (wMNE), dipole fitting, beamforming (LCMV and DICS), and sparse inverse methods. These methods require forward models encoding the geometry and conductivity properties of the head, which MNE-Python can compute using boundary element methods (BEM) or finite element methods (FEM) from individual MRI scans or template anatomies.

The time-frequency analysis module implements multitaper spectral estimation, Morlet wavelet convolution, and Hilbert transform methods for computing event-related synchronization and desynchronization (ERS/ERD). Statistical inference is supported through cluster-based permutation tests, which elegantly handle the multiple comparisons problem inherent in high-dimensional [[neuroimaging]] data. Visualization capabilities include 2D and 3D topographic maps, source estimates overlaid on cortical surfaces, [[connectivity]] graphs, and interactive time-frequency representations. The [[mne-bids]] pipeline extends these capabilities to automated batch processing of large multi-subject datasets according to BIDS standards.

## Key Features

Several features distinguish MNE-Python as a leading platform for electrophysiological analysis. The integration with the MNE-C command-line tools ensures backward compatibility with established preprocessing workflows. The objects-based data structure (Raw, Epochs, Evoked, SourceEstimate) provides intuitive interfaces while maintaining computational efficiency through lazy evaluation and memory mapping for large datasets. The connectivity module implements phase-locking value, coherence, imaginary coherence, and granger causality for investigating [[functional-connectivity]] between brain regions. The cortical [[parcellation]] system enables extraction of regional time courses for region-of-interest analyses, which is particularly relevant for comparing empirical data with [[whole-brain-modeling|whole-brain model]] outputs.

## Relationship to TVB

MNE-Python and [[the-virtual-brain]] share complementary roles in whole-brain electrophysiology research. While MNE-Python performs source localization to transform sensor-level MEG/EEG recordings into anatomically constrained time series, TVB simulates whole-brain dynamics at the source level using neural mass models such as the [[jansen-rit-model]] or [[wong-wang-model]]. The two platforms integrate through the TVB forward modeling pipeline: TVB accepts leadfield matrices computed by MNE-Python to generate predicted EEG and MEG sensor data from simulated source activity, enabling direct comparison between empirical and model-derived signals. Conversely, MNE-Python-derived source time courses can seed TVB simulations as empirical constraints, providing personalized initial conditions for whole-brain models. This bidirectional workflow is particularly valuable in [[epilepsy-modeling]], where patient-specific source estimates from MEG or EEG inform seizure propagation simulations in TVB. The [[forward-model]] infrastructure in both platforms ensures compatibility, though users must carefully align sourcemaps, anatomies, and sampling frequencies when transferring data between systems.

## References

1. Gramfort et al. (2013). *MEG and EEG: From Acquisition to Analysis*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fnins.2013.00010)