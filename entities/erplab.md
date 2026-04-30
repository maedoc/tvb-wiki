---
created: 2025-01-15
sources:
- raw/papers/arxiv-2604.16463.md
- raw/papers/semanticscholar-9e42d6a25d21.md
- raw/papers/semanticscholar-d45f5742871a.md
tags:
- neuroimaging-eeg
- electrophysiology
- software-visualization
- neural-mass-models
title: ERPLAB
type: entity
updated: '2026-04-30'
---

ERPLAB is a popular open-source MATLAB toolbox for processing and analyzing event-related potential (ERP) data, designed as a plugin extension to [[eeglab]]. The toolbox provides comprehensive functionality for preprocessing, filtering, artifact rejection, and statistical analysis of ERP waveforms, making it an essential tool for researchers studying cognitive electrophysiology. ERPLAB was developed to address the growing need for specialized ERP analysis tools within the EEGLAB environment, allowing users to leverage EEGLAB's general EEG processing capabilities while adding ERP-specific workflows tailored to the unique requirements of cognitive neuroscience experiments.

## Motivation and Context

Event-related potentials are time-locked neural responses to stimuli that provide millisecond-resolution insights into cognitive processes such as attention, perception, and decision-making. The analysis of ERP data requires specialized workflows that differ substantially from standard EEG analysis, including baseline correction, epoching with specific time windows, artifact rejection procedures optimized for ERP artifacts (such as blinks and saccades), and amplitude measurement across specified time windows. Prior to ERPLAB, researchers often relied on proprietary software or custom scripts, limiting [[reproducibility]] and sharing of analysis pipelines. ERPLAB emerged as a community-driven solution to standardize ERP processing workflows, enabling transparent and replicable analyses that could be shared across laboratories through EEGLAB's scriptable environment.

The development of ERPLAB reflects the broader movement toward open science in [[neuroimaging]] and [[electrophysiology]] research. By integrating closely with [[eeglab]], ERPLAB benefits from EEGLAB's established infrastructure for data import, pipeline scripting, and batch processing, while adding domain-specific functionality for ERP analysis that would be cumbersome to implement from scratch. EEGLAB supports data import in numerous formats, and the EEGLAB-BIDS plugin enables working with data in BIDS format, though this requires installing the separate BIDS extension.

## Key Features

ERPLAB provides a comprehensive suite of tools organized into processing stages that mirror the typical ERP analysis pipeline. The preprocessing capabilities include filtering options tailored to ERP analysis (such as high-pass filters designed to preserve slow wave components while removing drift), channel rejection based on amplitude thresholds or statistical criteria, and independent component analysis (ICA) decompositions via EEGLAB's implementation for removing artifacts like eye movements and muscle activity.

Epoching functionality in ERPLAB allows researchers to extract time-locked segments from continuous data with precise control over baseline periods and time windows. The toolbox supports multiple epoch rejection strategies including amplitude thresholds, joint probability checks, and spatial gradient detection for identifying artifacts. Once epochs are extracted, ERPLAB facilitates averaging across trials to create ERP waveforms, with support for weighted averaging based on trial counts or signal quality.

For statistical analysis, ERPLAB implements popular approaches for ERP data including time-point by time-point t-tests, permutation tests, and planned comparisons across conditions. The visualization tools enable researchers to plot ERP waveforms, topographic maps at specified latencies, and difference waves comparing conditions. Researchers requiring advanced cluster-based permutation statistics for controlling Type I error across multiple channels and time points often integrate with [[fieldtrip]] for these specialized analyses, which provides more advanced statistical implementations.

## Relationship to TVB

While [[the-virtual-brain]] (TVB) focuses on [[whole-brain-modeling]] and large-scale network dynamics, ERPLAB serves a complementary role in the [[computational-neuroscience]] ecosystem by providing tools for analyzing experimental data that can inform or validate such models. TVB simulations often produce synthetic electrophysiological data that can be analyzed using tools like ERPLAB to compare model predictions with empirical findings. Additionally, ERP research increasingly intersects with [[dynamic-causal-modeling]] frameworks that aim to infer effective connectivity from neuroimaging data, potentially bridging empirical ERP analysis with [[whole-brain-modeling]] approaches. ERPLAB's compatibility with [[eeglab]] and the broader [[electrophysiology]] analysis ecosystem makes it a valuable component for researchers working at the intersection of empirical cognitive neuroscience and computational modeling.

## Related Software

ERPLAB operates within the [[eeglab]] ecosystem, which itself is built on MATLAB and integrates with tools like [[fieldtrip]] for advanced source analysis and statistical implementations. For researchers interested in [[neural-mass-models]] or [[dynamic-causal-modeling]], ERPLAB provides the empirical data analysis foundation that can complement model fitting procedures. The toolbox is related to other [[neuromorpho-toolkit]] software including [[brainstorm]] and [[openvibe]], though ERPLAB's focus specifically on ERP analysis distinguishes it from these more general EEG/MEG analysis platforms.

## Key Papers

- Lopez-Calderon, J., & Luck, S. J. (2014). ERPLAB: An open-source toolbox for the analysis of event-related potentials. *Frontiers in Psychology*, 5, 213. https://doi.org/10.3389/fpsyg.2014.00213
- Luck, S. J., & Lopez-Calderon, J. (2012). ERPLAB: A toolbox for ERP data analysis. *ERP Tools*. https://erpinfo.org/erplab

## References

1. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f)
2. D. Y. Lodema, Herman J van Dellen, W. de Haan, Margot van Hest, A. Hillebrand, E. van Dellen. (2026). *EEG-Pype: An accessible [[mne-python]] pipeline with graphical user interface for preprocessing and analysis of [[resting-state]] electroencephalography data.*. PLoS Computational Biology. [DOI](https://doi.org/10.1371/journal.pcbi.1014043)
3. M. A. van den Boom, Nicholas M. Gregg, G. Valencia, B. Lundstrom, K. J. Miller, D. van Blooijs, G. Huiskamp, F. Leijten, G. Worrell, Dora [[hermes]]. (2025). *ER-detect: a pipeline for robust detection of early evoked responses in [[bids]]-iEEG electrical stimulation data.*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2025.110389)