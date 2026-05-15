---
created: 2025-05-13
sources: []
tags:
- software-brain-modeling
- neuroimaging-meg
- neuroimaging-eeg
- neuroimaging-fmri
- source-reconstruction
- functional-connectivity
- effective-connectivity
- dynamic-causal-modeling
- beamforming
- brain-oscillations
- resting-state
- task-based
title: NUTMEG
type: entity
updated: '2026-05-13'
---

**NUTMEG** (Neurodynamic Utility Toolbox for Magnetoencephalography/Electroencephalography) is an open-source MATLAB toolbox for spatiotemporal source reconstruction, functional [[connectivity]] estimation, and statistical mapping of [[meg]] and [[eeg]] data. It combines adaptive spatial filtering (beamforming) with dynamic statistical parametric mapping (dSPM) and functional connectivity analysis within a unified graphical interface, making it a practical bridge between sensor-level electromagnetic recordings and source-space [[whole-brain]] analyses.

## Motivation and Context

Magnetoencephalography and electroencephalography record cortical activity with millisecond temporal resolution, but the raw sensor-level signals suffer from [[volume-conduction]], field spread, and poor spatial localization. Reconstructing the underlying cortical sources—the inverse problem—is essential for linking these rich temporal signals to specific brain regions and for comparing empirical dynamics against computational models of large-scale brain networks. NUTMEG addresses this problem by providing a streamlined pipeline that takes preprocessed MEG/EEG data through source reconstruction, time-frequency decomposition, and connectivity analysis, all within a single environment. The toolbox occupies a middle ground in the MEG/EEG software landscape: it is more focused and accessible than fully general-purpose packages like [[fieldtrip]], yet offers deeper source-space analysis capabilities than basic sensor-level toolkits.

The broader significance of NUTMEG lies in how it enables the kind of source-space electromagnetic data that whole-brain modeling frameworks depend on. When modeling large-scale neural dynamics—for example, using [[the-virtual-brain]] or [[dynamic-causal-modeling]]—the empirical target is typically a set of regional time series derived from source-reconstructed MEG/EEG or [[resting-state]] [[neuroimaging-fmri]]. NUTMEG produces precisely this output: voxel-level and region-of-interest time courses that can be aggregated into parcellated regional activity and connected to structural [[connectomics]] frameworks. Without such source reconstruction, MEG/EEG data cannot be meaningfully compared to simulations of macroscopic neural dynamics.

## Source Reconstruction Engine

NUTMEG's core reconstruction engine is built around adaptive spatial filtering, specifically the linearly constrained minimum variance (LCMV) beamformer. The beamformer operates as a spatial filter that passes activity from a target location while suppressing contributions from elsewhere, with weights adaptively estimated from the data covariance matrix. This approach does not assume a fixed number of dipoles and is inherently data-driven. The toolbox supports multiple beamformer variants, including the eigenspace-projection beamformer that projects weights onto the signal subspace, improving robustness against noise and correlated sources.

Beyond beamforming, NUTMEG implements minimum-norm estimates (MNE) and dynamic statistical parametric mapping. The dSPM approach combines minimum-norm solutions with noise-normalization, producing statistical maps (z-scores or t-values) rather than raw current estimates, which aids interpretation. Source spaces can be defined on individual cortical surfaces or normalized to a common template such as the MNI brain, enabling group-level analyses. The [[forward-model]] computation—the lead field matrix that maps from cortical sources to sensors—typically relies on single-shell or overlapping-sphere head models, though NUTMEG can ingest forward solutions computed externally (e.g., from [[spm]] or [[fieldtrip]]).

## Time-Frequency and Connectivity Analysis

A distinguishing feature of NUTMEG is its integration of source reconstruction with time-frequency analysis in a single workflow. After reconstructing source activity at each voxel, the toolbox computes time-frequency representations via Morlet wavelet convolution or multi-taper spectral estimation. This enables the identification of task-related oscillatory power changes—event-related synchronization and desynchronization—directly in source space, avoiding the pitfalls of sensor-level interpretations where spatial mixing obscures the generators of oscillatory [[brain-oscillations]].

The connectivity module within NUTMEG supports both [[functional-connectivity]] and [[effective-connectivity]] measures computed on source-space time series. Available metrics include coherence, the phase-locking value (PLV), imaginary coherence (which suppresses zero-lag volume conduction artifacts), and Granger causality. The toolbox can also interface with [[dynamic-causal-modeling]] for model-based effective connectivity analysis, allowing users to specify and invert neural mass or conductance-based DCMs on source-extracted time series from regions of interest. This pipeline—source reconstruction followed by DCM—has been applied in studies of motor control, language processing, and clinical conditions including epilepsy.

## Relationship to The Virtual Brain

NUTMEG and [[the-virtual-brain]] (TVB) occupy complementary positions in the computational neuroscience workflow. NUTMEG operates at the empirical end, extracting source-space neural signals from MEG/EEG recordings. TVB operates at the modeling end, simulating large-scale neural dynamics on individualized [[structural-connectivity]] derived from [[diffusion-imaging]] and [[tractography]]. The natural junction between the two is the comparison of simulated regional time series from TVB against source-reconstructed empirical time series from NUTMEG.

A concrete integration scenario involves using NUTMEG to extract source-space functional connectivity matrices (e.g., PLV or imaginary coherence matrices) from resting-state MEG data. These empirical matrices can then serve as fitting targets for TVB simulations, where model parameters such as regional excitability or conduction delays are tuned to maximize the match between simulated and empirical functional connectivity. This approach has been used to investigate how structural connectivity constrains functional dynamics and to identify model parameter regimes that correspond to healthy versus pathological brain states. More broadly, NUTMEG-processed MEG/EEG data provides the empirical grounding needed to validate the [[neural-mass-models]] (e.g., the reduced [[wong-wang|Wong-Wang model]] or the [[stefanescu-jirsa|Stefanescu-Jirsa model]]) that TVB simulates, closing the loop between data and theory in whole-brain modeling.

NUTMEG additionally complements TVB's [[fmri]]-centric validation by providing the millisecond-scale temporal resolution that hemodynamic measures cannot capture. While [[neuroimaging-fmri]] functional connectivity reflects slow (~0.01–0.1 Hz) blood-oxygen-level-dependent fluctuations, MEG/EEG source-space connectivity from NUTMEG captures neural interactions across the full physiological frequency range—delta through gamma—offering a richer set of empirical constraints for model development.

## Key Papers and Development

NUTMEG was developed at the University of California, San Francisco (UCSF), with the initial public release appearing alongside a detailed methods paper that described the beamforming core, time-frequency decomposition pipeline, and statistical framework. Subsequent updates have expanded connectivity analysis options, improved the graphical user interface, and strengthened interoperability with external toolboxes including [[spm]], [[fieldtrip]], and [[brainstorm]]. The toolbox remains under active development, with a user community that contributes bug reports, feature requests, and extensions through its GitHub repository. As an open-source package, NUTMEG has been adopted by MEG/EEG laboratories worldwide for tasks ranging from clinical pre-surgical mapping to basic cognitive neuroscience experiments studying attention, memory, and language.

## Related Software

- [[the-virtual-brain]]
- [[dynamic-causal-modeling]]
- [[spm]]
- [[fieldtrip]]
- [[brainstorm]]
- [[source-reconstruction]]
- [[beamforming]]
- [[resting-state]]