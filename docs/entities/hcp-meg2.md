---
created: 2025-01-15
sources:
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-5f347f47ec54.md
- raw/papers/semanticscholar-adcab180dcd3.md
tags:
- database-hcp
- neuroimaging-meg
- resting-state
- functional-connectivity
- source-localization
- dataset
title: HCP MEG2
type: entity
updated: '2026-05-05'
---

The [[mrtrix3-connectome]] (HCP) MEG2 dataset represents one of the highest-quality publicly available magnetoencephalography datasets in the neuroscience community. Released as part of the broader HCP [[aging]] and Young Adult studies, MEG2 provides researchers with heavily preprocessed, minimally analyzed MEG recordings—meaning the data has undergone rigorous artifact rejection and signal cleaning to remove eye movements, cardiac interference, and environmental noise, while remaining in a raw‑enough state for users to apply their own analytical approaches such as custom source reconstruction or [[connectivity]] modeling. These recordings can be used for [[functional-connectivity]] analyses, [[source-localization]] studies, and [[whole-brain|whole-brain modeling]] efforts. The dataset addresses a critical need in the field: while functional magnetic resonance imaging ([[fmri]]) provides excellent spatial resolution for mapping brain networks, its temporal resolution is limited by the hemodynamic response, whereas MEG offers millisecond‑scale temporal precision that captures the rapid dynamics of [[brain-oscillations]] underlying cognition and behavior.

## Motivation and Context

The original HCP MEG dataset comprised resting-state recordings from young healthy adults collected between 2012-2015, but the community increasingly requested access to larger samples with improved preprocessing pipelines and broader demographic representation. The MEG2 release (formally released in 2017 and updated to v2.0 in 2022) addresses these concerns by providing data from the HCP Aging Study, encompassing cognitively healthy individuals across a broader age range. This expansion is particularly valuable for [[computational-neuroscience]] efforts such as those implemented in [[The Virtual Brain]] (TVB), where model parameters often need calibration against age‑appropriate baseline dynamics. Researchers studying brain oscillations, functional connectivity dynamics, or building personalized brain models can leverage MEG2 to validate their approaches against a well‑characterized population dataset with known demographic characteristics and quality‑controlled processing history.

The dataset also fills an important gap in the [[neuroimaging]] ecosystem by providing multi‑modal data that can be linked to [[structural connectivity]] estimates derived from [[diffusion-imaging]] (DWI). This combination of structural and functional data at the MEG temporal resolution enables investigators to examine the relationship between anatomical pathways and dynamic functional networks—a central question in [[whole-brain modeling]] and [[connectomics]] research.

## Key Features

The HCP MEG2 dataset encompasses several distinguishing characteristics that set it apart from conventional MEG repositories. First, the acquisition employs a whole‑head CTF system (275‑channel) with magnetometer sensors, recording at 1200 Hz sampling rate, providing comprehensive coverage of neuromagnetic fields across the scalp. The system was housed at both Massachusetts General Hospital (MGH) and Washington University in St. Louis, with consistent acquisition protocols across sites to ensure data harmonization.

The preprocessing pipeline, developed by the HCP consortium, includes sophisticated artifact rejection algorithms for removing eye movements, cardiac artifacts, and environmental interference while preserving biologically relevant signals. Critically, HCP data is stored in CIFTI/ Grayordinates format for gray matter time series—the native format for HCP—though community‑developed tools such as `hcp-meg` and `mne-bids` facilitate conversion to BIDS‑compliant structures for compatibility with diverse analysis packages including [[mne-bids-pipeline]], [[mne-bids]], and specialized connectivity toolboxes such as [[mne-connectivity]].

The data structure includes both [[resting-state]] recordings (typically 5‑10 minutes per subject with eyes open and closed) and task‑based paradigms, enabling researchers to investigate [[brain-dynamics]] across different cognitive conditions. All data are provided in both sensor space and source space (when available), with source reconstruction performed using beamforming or minimum‑norm estimates.

Importantly, HCP MEG2 includes detailed metadata documentation capturing demographic information, acquisition parameters, preprocessing history, and quality assurance metrics—essential elements for reproducible research and [[personalized brain modeling]] workflows that require rigorous subject‑level characterization.

## Relationship to TVB

HCP MEG2 is directly relevant to [[TVB]] workflows in several important ways. The dataset provides empirically measured brain dynamics that can serve as validation targets for whole‑brain simulations built within the TVB framework. Researchers constructing personalized brain models using individual structural connectivity matrices (derived from DWI) can initialize their models with the frequency‑specific functional connectivity patterns observed in the MEG2 resting‑state data, creating empirically grounded initial conditions for forward simulations.

The high temporal resolution of MEG2 also enables parameter fitting exercises where model parameters (such as those governing [[neural mass models]] or [[local-field-potentials]]) are optimized to reproduce observed spectral properties and connectivity dynamics. TVB's integration with tools like [[tvb-multiscale]] allows researchers to generate simulated MEG signals and compare them directly against HCP MEG2 recordings. Furthermore, the dataset's documentation of cognitive task paradigms provides benchmarks for evaluating TVB's ability to simulate evoked responses and state transitions across different cognitive contexts.

The dataset's multi‑modal nature—combining MEG with structural DWI and, for many subjects, fMRI—makes it particularly valuable for TVB workflows that aim to integrate multiple data modalities into unified brain models. Researchers can validate structural connectivity reconstructions against the empirical MEG functional connectivity, assess model predictions of frequency‑specific network topology, and explore the relationship between [[white-matter]] architecture and dynamic brain states captured at millisecond resolution.

## Key Papers

The primary publications describing the HCP MEG2 dataset and its acquisition methodology provide essential context for researchers. The MEG2 release documentation details the acquisition protocol, preprocessing pipeline, and quality assurance criteria applied to ensure data quality across the lifespan sample. Methodological papers describing the broader HCP acquisition and processing framework provide foundational context for understanding how MEG data fits within the multi‑modal HCP data ecosystem.

## Related Software

The primary analysis ecosystem for HCP MEG2 revolves around [[mne-bids-pipeline]] and its extensions. The [[mne-bids-pipeline]] provides automated preprocessing workflows compatible with HCP‑style data organization, while [[mne-connectivity]] offers comprehensive tools for computing frequency‑specific connectivity metrics including coherence, phase‑locking value, and Granger causality. For source reconstruction, researchers employ custom beamformers or distributed source models available in MNE‑Python's inverse solving routines.

The `hcp-meg` package (available on GitHub) provides utilities for working directly with HCP‑formatted MEG data, including [[cifti]] conversion and preprocessing helpers. The data can also be imported into TVB using adapters from [[tvb-adapters]] for integration with TVB's simulation engines.

For visualization of results, common tools include [[pysurfer]] for cortical surface representations and [[brain-map]] for interactive exploration. The dataset's structure also facilitates analysis within the [[brain-life]] ecosystem, enabling reproducible containers that can be shared across labs.

## References

1. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
2. Masashi Kondo, K. Sehara, Rie Harukuni, Ryo Aoki, Shoya Sugimoto, Yasuhiro R. Tanaka, Masanori Matsuzaki, Ken Nakae. (2025). *Multimodal dataset linking wide‑field calcium imaging to behavior changes in operant lever‑pull task in mice*. Scientific Data. [DOI](https://doi.org/10.1038/s41597-025-05482-y)
3. J. Meier, P. Triebkorn, M. Schirner, [[petra-ritter]]. (2025). *Connectomes, simultaneous EEG‑fMRI resting‑state data and brain simulation results from 50 healthy subjects*. bioRxiv. [DOI](https://doi.org/10.1101/2024.04.17.589718)