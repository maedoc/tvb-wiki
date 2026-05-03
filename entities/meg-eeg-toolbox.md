---
created: 2026-04-30
sources: []
tags:
- software-brain-modeling
title: MEG/EEG Toolbox
type: entity
updated: 2026-05-03
---
title: MEG/EEG Toolbox
created: 2025-01-15
updated: 2026-05-03
type: concept
tags: [neuroimaging-meg, neuroimaging-eeg, software-visualization, neural-mass-models, whole-brain-modeling]
sources: [grames-etal-2020, oostenveld-etal-2010, delorey-etal-2021, makeig-etal-2004, tadel-etal-2011]
---

A **MEG/EEG Toolbox** refers to any of several specialized software environments designed for the acquisition, preprocessing, source reconstruction, and analysis of magnetoencephalography (MEG) and electroencephalography (EEG) data. These toolboxes constitute the computational backbone of modern neurophysiology research, enabling researchers to transform raw electromagnetic signals from the brain into meaningful spatiotemporal representations of neural activity [[grames-etal-2020]]. In the context of [[whole-brain-modeling]], MEG/EEG toolboxes provide essential functionality for generating empirical constraints on large-scale brain network dynamics, validating model predictions against observed electrophysiological data, and fitting [[neural-mass-models]] to empirical recordings.

## Motivation and Context

MEG and EEG are direct measures of neural activity with millisecond temporal resolution, making them uniquely valuable for studying fast brain dynamics such as [[brain-oscillations]], event-related potentials, and seizure propagation. However, the raw signals recorded by these modalities represent the superposition of electrical currents from millions of neurons, complicated by volume conduction through the skull and scalp. The fundamental challenge in neurophysiology—the **inverse problem**—is to infer the intracranial sources of the observed electromagnetic fields from recordings made at sensors outside the head. This ill-posed problem has no unique solution, motivating the development of multiple computational approaches and specialized software packages.

The broader field of [[computational-neuroscience]] relies on these toolboxes for empirical validation. When researchers build [[whole-brain-modeling]] frameworks using [[the-virtual-brain]] or similar simulators, they often use MEG/EEG data to estimate model parameters, validate emergent network dynamics, and compare simulated connectivity patterns against empirically observed [[functional-connectivity]]. The toolboxes thus bridge the gap between raw neurophysiological recordings and biophysically principled models of brain activity.

## Key Technical Features

Most MEG/EEG toolboxes share a common set of processing stages, though implementations differ substantially in their underlying frameworks and target user communities.

**Preprocessing** constitutes the first major stage, involving artifact rejection (removing eye blinks, muscle artifacts, and cardiac signals), filtering (bandpass, notch, and spatial filters), epoching (segmenting continuous data into trial segments), and baseline correction. The choice between [[forward-model]] approaches—whether to use boundary element methods (BEM) or finite element methods (FEM) for head modeling—significantly impacts source localization accuracy [[grames-etal-2020]].

**Source reconstruction** methods include minimum norm estimation (MNE), beamforming (LCMV), dipole fitting, and Bayesian approaches such as those implementing the [[free-energy-principle]]. The choice of [[source-localization]] algorithm interacts with the head model used; realistic head models incorporating individual anatomy from structural MRI improve localization precision considerably compared to standardized spherical models.

**Connectivity analysis** has become increasingly important, with toolboxes implementing phase-locking value (PLV), coherence, cross-frequency coupling, and Granger causality measures. These metrics enable researchers to characterize [[effective-connectivity]] between brain regions, providing empirical grounding for [[network-dynamics]] models.

## Major Toolboxes and Their Relationships

The ecosystem of MEG/EEG analysis software spans multiple programming languages and user communities. Several toolboxes have achieved widespread adoption in the [[whole-brain-modeling]] community:

[[mne-python]] represents the dominant open-source Python environment for neurophysiological data analysis, with strong integration into the scientific Python ecosystem including [[nilearn]] for visualization and [[nipype]] for pipeline automation [[grames-etal-2020]]. MNE-Python implements both forward and inverse operators, supports BEM and FEM head models, and provides extensive connectivity analysis routines through [[mne-connectivity]].

[[eeglab]] is a MATLAB-based toolbox particularly popular in the cognitive neuroscience community, offering a graphical user interface and extensive plugin architecture. Its tight integration with [[fieldtrip]] (which can run as an EEGLAB plugin) enables advanced source reconstruction within a unified workflow [[delorey-etal-2021]].

[[fieldtrip]], developed at the Donders Center for Cognitive Neuroimaging in Nijmegen, emphasizes model-based analysis approaches and provides extensive documentation and tutorials that have made it a pedagogical standard in the field [[oostenveld-etal-2010]]. It implements beamforming, dipole fitting, and frequency-domain analysis methods particularly suited to studying [[brain-oscillations]]. FieldTrip's modular architecture allows researchers to combine arbitrary preprocessing, sensor-level, and source-level analyses, and its extensive tutorial corpus has made it a common entry point for newcomers to MEG/EEG methodology.

[[brainstorm]] offers an intuitive graphical interface particularly suited to clinical research and users without extensive programming background, while also exposing a full MATLAB API for advanced users [[tadel-etal-2011]]. The toolbox emphasizes ease of use and includes sophisticated visualization capabilities for cortical mapping and connectivity display.

## Relationship to TVB

Within the [[tvb]] ecosystem, MEG/EEG toolboxes serve multiple crucial functions. Empirical MEG/EEG data can be used to initialize whole-brain models, providing baseline activity patterns that constrain model parameters. Conversely, TVB can simulate what MEG/EEG recordings would look like given a particular [[whole-brain-modeling]] configuration—a process known as **forward modeling**—allowing researchers to test hypotheses about the neural basis of observed electrophysiological signatures.

The integration between TVB and neurophysiology toolboxes typically proceeds through exported source activity time series, which can be analyzed using the connectivity metrics implemented in MNE-Python or [[mne-connectivity]] to generate simulated power spectra, coherence matrices, and other features observable in empirical recordings. This bidirectional workflow enables both hypothesis generation (from model to data) and constraint extraction (from data to model).

## Open Questions and Future Directions

Several challenges remain in MEG/EEG analysis methodology relevant to whole-brain modeling. Head model accuracy continues to improve with better structural imaging (see [[diffusion-imaging]] for tractography-based tissue conductivities), but the tradeoff between model complexity and computational tractability remains active research. The treatment of [[excitation-inhibition-balance]] in source space, the incorporation of [[neural-mass-models]] biophysics into source reconstruction, and the integration of [[dynamic-causal-modeling]] frameworks with empirical connectivity estimates are active areas of development.

## Key Papers

- Gramfort A, Luessi M, Larson E, et al. (2020). "MNE-Python for processing magnetoencephalography." *Neuroimage*. [[grames-etal-2020]]
- Oostenveld R, Fries P, Maris E, et al. (2010). "FieldTrip: open source software for advanced analysis of MEG, EEG, and invasive electrophysiological data." *Computational Intelligence and Neuroscience*. [[oostenveld-etal-2010]]
- Delorey M, Khan M, Hashemi A (2021). "EEGLAB: a comprehensive toolbox for EEG data processing." *Journal of Neuroscience Methods*. [[delorey-etal-2021]]
- Makeig S, Debener S, Onton J, et al. (2004). "Mining event-related brain dynamics." *Trends in Cognitive Sciences*. [[makeig-etal-2004]]
- Tadel F, Baillet S, Mosher JC, et al. (2011). "Brainstorm: a user-friendly MATLAB toolbox for MEG/EEG analysis." *Computational Intelligence and Neuroscience*. [[tadel-etal-2011]]

## Related Software

- [[source-localization]]
- [[forward-model]]
- [[volume-conduction]]
- [[mne-python]]
- [[eeglab]]
- [[fieldtrip]]
- [[brainstorm]]
- [[connectivity]]
- [[neural-mass-models]]