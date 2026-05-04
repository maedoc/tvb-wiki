---
created: 2026-04-20
sources:
- raw/papers/makeig-1996.md
- raw/papers/cohen-2014.md
- raw/papers/buzsaki-2012.md
- raw/papers/arxiv-2603.21032.md
- raw/papers/semanticscholar-cdd1f61b0ec3.md
- raw/papers/arxiv-2602.18715.md
- raw/papers/arxiv-2506.22951.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/glean-github.md
tags:
- neuroimaging-meg
- neuroimaging-eeg
- neuroimaging-fmri
- neuroimaging-dti
- source-localization
- brain-oscillations
- connectivity-types
- resting-state
- neural-mass-models
- whole-brain-modeling
- software-fieldtrip
- software-mne-python
- software-eeglab
title: MEG
type: concept
updated: '2026-04-30'
---

# MEG

Magnetoencephalography (MEG) is a non-invasive [[neuroimaging]] technique that measures the weak magnetic fields (on the order of tens to hundreds of femtotesla) produced by Postsynaptic currents flowing in the dendrites of pyramidal neurons in the cerebral cortex. The technique provides millisecondTemporal resolution and, due to the magnetic fields' relative invariance through biological tissue, offers superior spatial localization compared to electroencephalography, making it a cornerstone modality for studying rapid neural dynamics in both research and clinical contexts.

## Physical Principles and Measurement

MEG exploits the fundamental relationship between electrical current and magnetic fields described by the Biot-Savart law. When synchronized postsynaptic potentials generate net current flow in elongated pyramidal neurons (particularly those with dendrites oriented perpendicular to the cortical surface), a magnetic field circulates perpendicular to the current direction. Modern MEG systems employ superconducting quantum interference devices (SQUIDs) housed in a magnetically shielded room to detect these extremely weak fields against the backdrop of Earth's magnetic field (approximately 50 μT) and other environmental noise sources.

The forward problem in MEG—computing the magnetic field at the sensor array given a source configuration—requires solving the quasi-static approximation of Maxwell's equations. The lead field (or sensitivity kernel) determines which source configurations produce measurable fields at each sensor. Unlike EEG, where conductivity differences between skull and scalp cause severe spatial blurring, magnetic fields pass through tissue with minimal distortion. However, MEG is preferentially sensitive to tangentially-oriented sources in the sulci, while radially-oriented sources in the gyri produce weaker signals. This complementary sensitivity profile means that combined EEG-MEG recordings provide more complete coverage of cortical sources than either modality alone.

## Role in Whole-Brain Modeling

MEG serves as a critical validation modality for [[whole-brain modeling]] efforts. [[Neural-mass-model]] frameworks such as the [[Jansen-Rit]] model, [[Wilson-Cowan]] equations, or the [[epileptor]] model generate predictions about population-level activity that must be compared against empirical measurements. Forward modeling transforms these simulated neural mass outputs into predicted sensor-level signals through a lead field matrix computed from a [[structural-connectivity]] head model derived from [[diffusion-mri]] and tractography.

The [[resting-state]] networks identified in fMRI (such as the [[default-mode-network]]) exhibit correlates in the MEG frequency domain, particularly in the alpha (8-12 Hz), beta (12-30 Hz), and gamma (30-100 Hz) bands. [[Connectivity-types]] analysis applied to MEG data—using measures such as coherence, phase locking value, or Granger causality—enables comparison with functional connectivity patterns derived from fMRI. This cross-modal validation is essential for establishing that whole-brain models capture biologically realistic [[network-dynamics]].

## Comparison with EEG

While EEG and MEG share the fundamental property of measuring correlates of postsynaptic activity, their physical basis leads to distinct strengths and limitations. Electric fields are strongly affected by the conductive properties of skull tissue, which acts as a spatial low-pass filter, degrading spatial resolution to approximately 10-20 mm. Magnetic fields, being less perturbed by tissue conductivity contrasts, retain theoretical spatial resolution of 2-5 mm under optimal conditions. However, MEG systems require expensive cryogenic instrumentation and magnetically shielded rooms, limiting portability compared to EEG systems.

The source orientation sensitivity differs substantially: EEG detects contributions from both radial and tangential sources, while MEG preferentially samples tangential sources. Clinically, this makes MEG particularly valuable for localizing epileptogenic zones near the cortical surface where tangential currents predominate. For research applications, the choice between modalities depends on whether spatial precision (MEG) or cost/portability (EEG) is prioritized.

## Analysis Methods

MEG data analysis proceeds through preprocessing stages analogous to EEG, including artifact rejection (eye movements, muscle activity, cardiac signals), filtering, and segmentation. Source reconstruction typically employs beamforming approaches such as the synthetic aperture magnetometry (SAM) or minimum-variance beamforming, or distributed inverse solutions like minimum-norm estimation (MNE). The MNE method implemented in [[mne-python]] has become a standard tool for reconstructing distributed source activity from MEG data.

Time-frequency decomposition reveals the spectral content of neural activity, with specific frequency bands linked to distinct cognitive processes. [[Brain-oscillations]] in the gamma band, for example, are associated with feature binding and local processing, while alpha oscillations reflect cortical inhibition and idling states. Connectivity analysis quantifies phase relationships or information flow between brain regions, enabling comparison with [[functional-connectivity]] patterns from fMRI and establishing network-level validity for [[whole-brain]] models.

## Relationship to Other Modalities

MEG occupies a unique position in the neuroimaging ecosystem, complementing both electrophysiological and hemodynamic measures. Compared to [[fmri]], which tracks the blood-oxygen-level-dependent (BOLD) signal with second-scale temporal resolution, MEG provides real-time windows into neural dynamics. However, the [[bold-signal]]'s vascular basis captures slower metabolic processes that may reveal aspects of neural communication invisible to [[electrophysiology]].

The combination of MEG with EEG, [[structural-connectivity]] from DTI, and functional data from fMRI enables multimodal integration that strengthens whole-brain models. Software platforms like [[fieldtrip]] and [[mne-python]] provide pipelines for processing MEG data, while [[tvb]] integrates MEG forward modeling into whole-brain simulation workflows. The field continues to develop hardware improvements (e.g., optically pumped magnetometers) that may increase MEG's accessibility and temporal resolution.