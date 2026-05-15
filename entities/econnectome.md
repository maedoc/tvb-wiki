---
created: 2026-05-13
sources:
- raw/papers/arxiv-2604.16463.md
- raw/papers/sanz-leon-2013.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-brain-modeling
- effective-connectivity
- functional-connectivity
- connectomics
- neuroimaging-eeg
- neuroimaging-meg
- graph-theory
- network-dynamics
- electrophysiology
- source-localization
title: eConnectome
type: entity
updated: '2026-05-15'
---

eConnectome is an open-source MATLAB toolbox for mapping, imaging, and analyzing brain [[functional-connectivity]] and [[effective-connectivity]] from electrophysiological signals including scalp electroencephalography ([[eeg]]), electrocorticography (ECoG), and magnetoencephalography ([[meg]]). Developed at the University of Minnesota and first described by He et al. (2011), the toolbox provides an integrated workflow that spans from cortical source imaging through connectivity estimation to graph-theoretic network analysis and three-dimensional visualization. eConnectome was among the earliest comprehensive software packages to bring the full [[connectomics]] analysis pipeline to the electrophysiology domain, offering both a graphical user interface and a scriptable command-line environment.

## Motivation and Context

The analysis of brain connectivity from electrophysiological recordings poses challenges that differ fundamentally from those encountered in functional magnetic resonance imaging ([[neuroimaging-fmri]]). Electrophysiological signals offer millisecond temporal resolution, capturing the rapid [[network-dynamics]] that underlie cognition, perception, and [[brain-oscillations]] across canonical frequency bands. However, extracting interpretable connectivity patterns from these signals requires careful handling of volume conduction effects — where a single neural source contributes to multiple scalp electrodes — and the need for multivariate models that can disambiguate direct from indirect causal influences.

Before eConnectome, researchers studying electrophysiological [[connectivity]] typically assembled bespoke analysis pipelines from disparate toolboxes, each handling only one stage of the workflow. [[eeglab]] provided preprocessing and independent component analysis, the [[brain-connectivity-toolbox]] offered graph-theoretic measures, and specialized scripts implemented Granger causality or directed transfer function computations. eConnectome unified these stages under a single graphical interface, lowering the barrier to entry for researchers without extensive programming expertise and promoting methodological consistency across studies. The toolbox was designed with a modular object-oriented architecture, allowing advanced users to extend its capabilities while providing turnkey analysis for clinical and experimental applications.

## Key Features

eConnectome's analysis pipeline begins with **cortical source imaging**, which projects scalp-recorded signals onto the cortical surface to mitigate the spatial smearing introduced by [[volume-conduction]]. The toolbox implements cortical current density (CCD) source estimation using realistic head models constructed from magnetic resonance imaging (MRI) data, with boundary element method (BEM) forward solutions. This source-space reconstruction is critical for interpretable connectivity analysis, as sensor-level connectivity estimates can be severely confounded by common-source effects.

For **functional connectivity**, eConnectome computes a suite of undirected measures including spectral coherence, cross-correlation, and phase synchrony indices, applicable to both sensor-level and source-reconstructed time series. These measures quantify the statistical interdependence between brain regions without specifying the direction of information flow, complementing the causal analyses described below.

The toolbox's **effective connectivity** module is one of its most distinctive contributions. It implements multivariate autoregressive (MVAR) modeling with several directional measures: the directed transfer function (DTF), partial directed coherence (PDC), and time-varying [[granger-causality]] computed via adaptive MVAR models. Unlike the [[mvgc]] toolbox — which focuses specifically on Granger causality inference — eConnectome provides these within a broader imaging framework that supports visualization of causal networks as three-dimensional cortical maps. The adaptive MVAR implementation is particularly valuable for [[resting-state]] and event-related paradigms where connectivity patterns evolve over time, enabling the study of dynamic rather than static [[effective-connectivity]].

After connectivity matrices are constructed, eConnectome applies **graph-theoretic analysis** to characterize the topological organization of the resulting brain networks. Global measures such as [[small-world-networks]] properties, clustering coefficient, characteristic path length, and [[modularity]] can be computed alongside nodal metrics including degree, betweenness centrality, and local efficiency. These analyses enable researchers to identify [[network-hubs]], assess network integration and segregation, and compare topological properties between experimental conditions or clinical populations — analyses that have proven informative in studies of [[epilepsy-modeling]], [[alzheimers-modeling]], and [[schizophrenia-models]].

For **visualization**, eConnectome renders connectivity patterns directly onto three-dimensional cortical surface models, displaying functional and effective connectivity as color-coded edges or scalp/cortical maps. The graphical interface supports interactive exploration of connectivity graphs, network measures, and time-frequency representations, facilitating hypothesis generation and quality control.

## Relationship to TVB

eConnectome and [[the-virtual-brain]] (TVB) occupy complementary positions in the [[whole-brain-modeling]] workflow. TVB is a forward-modeling platform that simulates large-scale [[network-dynamics]] using [[neural-mass-models]] parameterized by [[structural-connectivity]] derived from [[diffusion-imaging]] tractography. eConnectome, by contrast, is a purely empirical analysis tool that estimates connectivity patterns directly from recorded electrophysiological data without requiring a generative model.

The two tools can be integrated in a validation-driven research pipeline. Connectivity patterns estimated by eConnectome from empirical EEG or MEG recordings — particularly effective connectivity networks identified via DTF or Granger causality — can serve as target statistics against which TVB simulation outputs are compared during [[parameter-estimation]] and [[model-validation]]. If a TVB [[neural-mass-model]] such as the [[jansen-rit]] model, when embedded in a subject-specific [[connectome]], reproduces the empirical causal connectivity pattern estimated by eConnectome, this provides evidence that the model captures physiologically relevant dynamics. Conversely, discrepancies between simulated and empirically estimated connectivity can guide model refinement.

This complementarity extends to modality coverage. While TVB supports [[neuroimaging-fmri]] simulation via hemodynamic forward models (the [[bold-signal]]), eConnectome is optimized for the millisecond timescale of electrophysiology, making it a natural choice for validating TVB models against EEG/MEG data. The [[source-localization]] step performed by eConnectome also overlaps conceptually with TVB's forward-model infrastructure for EEG and MEG, though TVB computes forward solutions to generate synthetic sensor data from simulated neural activity, whereas eConnectome inverts the problem to estimate cortical sources from recorded sensor data.

## Related Software

eConnectome operates within a rich ecosystem of [[electrophysiology]] and connectivity analysis tools, each offering distinct capabilities:

- **[[brainstorm]]**: Provides comprehensive MEG/EEG source imaging and connectivity analysis with a polished GUI; shares eConnectome's emphasis on source-space connectivity but adds beamforming approaches and broader import format support
- **[[eeglab]]**: The dominant MATLAB environment for EEG preprocessing and independent component analysis; often used upstream of eConnectome for artifact removal and data preparation
- **[[mne-python]]**: Offers Python-native implementations of source imaging and connectivity measures, including MVAR-based effective connectivity, providing a non-MATLAB alternative to eConnectome's workflow
- **[[mvgc]]**: A MATLAB toolbox specialized for multivariate Granger causality inference with rigorous statistical testing; narrower in scope than eConnectome but deeper in causality-specific methodology
- **[[brain-connectivity-toolbox]]**: The foundational MATLAB toolbox for graph-theoretic network analysis; its measures are complementary to eConnectome's, which focuses upstream on constructing the connectivity matrices that BCT then analyzes
- **[[braph]]**: A MATLAB package for graph-theoretic brain connectivity analysis with longitudinal comparison support; shares eConnectome's goal of GUI-accessible connectivity analysis but emphasizes MRI modalities and multilayer graphs
- **[[the-virtual-brain]]**: The [[whole-brain]] simulation platform against which eConnectome-derived empirical connectivity patterns can be validated