---
created: 2026-05-11
sources:
- raw/papers/gramfort-2013.md
tags:
- software-visualization
- neuroimaging-eeg
- neuroimaging-meg
- neural-mass-models
- brain-oscillations
- network-dynamics
title: NeuroDSP
type: entity
updated: '2026-05-11'
---

NeuroDSP (Neural Digital Signal Processing) is a Python toolbox designed for the analysis of neural electrophysiological time series data, particularly electroencephalography (EEG), magnetoencephalography (MEG), and intracranial recordings. Developed primarily by Cole Voytas and colleagues, the library provides a comprehensive suite of algorithms for decomposing neural signals into their constituent oscillatory components, quantifying phase-amplitude coupling, estimating directional [[connectivity]], and characterizing transient neural events such as bursts and seizures. The toolkit is built with an emphasis on [[reproducibility]] and flexibility, offering both low-level signal processing functions and high-level analysis pipelines that integrate seamlessly with other Python neuroscience libraries like [[mne-python]] and [[eeglab]].

## Motivation and Context

The analysis of neural oscillations and connectivity has become a central focus in modern neuroscience, with implications for understanding cognitive processes, neurological disorders, and [[brain-stimulation]] effects. However, existing signal processing toolboxes either focused on general-purpose digital signal processing (DSP) without neuronspecific implementations, or were embedded within larger analysis frameworks that made isolated oscillatory analysis cumbersome. NeuroDSP emerged to fill this gap by providing a dedicated, well-documented Python library specifically optimized for the unique characteristics of neural time series: their non-stationarity, the presence of multiple overlapping sources, and the need for robust artifact rejection and connectivity estimation in the presence of [[volume-conduction]].

The field of [[brain-oscillations]] research relies heavily on decomposition techniques such as amplitude decomposition, baseline normalization, and goodness-of-fit metrics to distinguish true neural dynamics from artifacts and noise. Traditional approaches using custom MATLAB scripts were difficult to reproduce and share, limiting methodological consistency across laboratories. NeuroDSP addresses this by implementing published algorithms from the literature—such as the yasa sleep staging algorithm and various phase-amplitude coupling measures—in a unified, open-source framework that enables both routine analysis and methodological innovation.

## Key Features

NeuroDSP provides several categories of analysis tools organized into modular functions. The first major category is **oscillatory decomposition**, which includes algorithms for identifying and extracting rhythmic components from multi-channel neural recordings. The package implements variations of the oscillation detection approach, where candidate oscillations are identified by their spectral peaks above a threshold defined relative to a baseline period. Unlike general-purpose spectral decomposition, these functions account for the specific statistical properties of neural signals, including the characteristic 1/f power spectral density and the presence of narrowband theta, alpha, beta, and gamma oscillations that are temporally transient rather than stationary.

The second category encompasses **connectivity estimation** methods tailored for electrophysiological data. The library includes implementations of phase-lag index (PLI), weighted phase-lag index (wPLI), and envelope correlation approaches that are robust to volume conduction artifacts that plague scalp EEG and MEG. These methods operate on the premise that meaningful connectivity between brain regions should manifest as consistent phase relationships between their activity, rather than simple amplitude correlations that may arise from shared physical proximity. The connectivity functions integrate with [[bctpy]] and other graph-theoretical toolboxes for subsequent network analysis of brain connectivity patterns.

A third key feature is **phase-amplitude coupling (PAC)** analysis, which quantifies the degree to which the phase of a low-frequency oscillation modulates the amplitude of a high-frequency oscillation. PAC has been implicated in various cognitive processes and is a key signature in computational models of [[epilepsy-modeling]] and normal [[brain-dynamics]]. NeuroDSP implements multiple PAC estimators including the mean vector length, KL divergence, and MI-based methods, allowing users to compare different assumptions about the coupling structure.

The fourth feature area consists of **burst detection** algorithms that identify periods of elevated oscillatory activity as distinct from background idle cortical dynamics. These algorithms use threshold-based approaches on either instantaneous amplitude or power in specific frequency bands, enabling characterization of the temporal structure of oscillations across different brain states. This capability is particularly relevant for comparing simulation outputs from [[the-virtual-brain]] with empirical data, as both the mean activity levels and the burst statistics can serve as validation metrics.

## Relationship to TVB

[[The Virtual Brain]] (TVB) is a [[whole-brain]] simulation platform that combines [[structural-connectivity]] matrices derived from [[diffusion-imaging]] with [[neural-mass-models]] to generate simulated electrophysiological signals. NeuroDSP provides the complementary analysis layer for empirically recorded data that can be used to constrain, validate, or compare with TVB simulations. In practice, researchers applying TVB workflows often need to validate their simulated signals against empirical data using identical metrics—a process that requires extracting oscillatory features, connectivity estimates, and burst statistics from both real and simulated data. NeuroDSP's modular design makes it straightforward to apply the same analysis pipeline to TVB output (saved in standard formats like FIF or NWE) as to raw empirical recordings.

The integration between TVB and NeuroDSP is particularly valuable in the context of [[personalized-brain-modeling]], where individual subject data used to configure TVB simulations must be preprocessed and characterized using tools like NeuroDSP before being mapped onto model parameters. Furthermore, the comparison of empirical and simulated phase-amplitude coupling using NeuroDSP has been proposed as a validation metric for whole-brain models seeking to reproduce the nested oscillatory architecture observed in empirical human [[electrophysiology]].

## Related Software

NeuroDSP shares conceptual and practical overlap with several other neurophysiology analysis packages. [[MNE-Python]] provides a comprehensive framework for electrophysiological data preprocessing, source estimation, and visualization, with some overlapping functionality for connectivity and spectral analysis. [[EEGLAB]] offers a graphical environment for EEG/MEG processing with both MATLAB and Python implementations. [[yasa]] is a complementary library specifically optimized for sleep stage classification that builds upon NeuroDSP's base functionality. [[Nitime]] provides time-series analysis tools for neuroscience but takes a more general approach less optimized for the specific statistical properties of neural oscillations. The combination of these tools—with NeuroDSP providing oscillatory-specific analysis—enables comprehensive analysis pipelines from raw data preprocessing through advanced connectivity and coupling characterization.

## References

1. Gramfort et al. (2013). *MEG and EEG: From Acquisition to Analysis*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fnins.2013.00010)