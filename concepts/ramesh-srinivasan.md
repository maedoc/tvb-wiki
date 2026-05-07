---
created: 2026-04-27
sources:
- raw/papers/nunez-srinivasan-2006.md
- raw/papers/semanticscholar-3ac0a350bdb3.md
- raw/papers/semanticscholar-dacc3b888fa6.md
- raw/papers/arxiv-2602.09034.md
- raw/papers/anticevic-2012.md
tags:
- neuroimaging-eeg
- volume-conduction
- source-localization
- neural-mass-models
- brain-oscillations
- tutorial
title: EEG Neurophysics
type: concept
updated: '2026-05-07'
---

The neurophysics of electroencephalography (EEG) encompasses the physical principles underlying the generation, propagation, and measurement of electric fields produced by neural activity in the brain. This domain bridges [[computational-neuroscience]] with electromagnetic theory, providing the foundational framework for interpreting scalp-recorded EEG signals and for relating [[neural-mass-model]] activity to measurable electrophysiological data.

## Physical Basis of EEG Signal Generation

Electrical activity in the brain arises primarily from postsynaptic potentials in cortical pyramidal neurons. When thousands of synchronously active neurons produce excitatory or inhibitory postsynaptic potentials, their transmembrane currents generate electric fields that propagate through the head volume. The resulting scalp potentials—typically measured in microvolts—reflect the summed activity of large neuronal populations, though the precise relationship between source configuration and scalp measurements depends critically on the conductive properties of brain tissue, cerebrospinal fluid, skull, and scalp.

The governing physics follows from Maxwell's equations in the quasi-static regime, where the frequency content of EEG signals (typically 0.5–100 Hz) justifies neglecting inductive effects. The relationship between neural current sources and scalp potentials is described by the *lead field* or *gain matrix*, which quantifies how each unit of current at a given location contributes to potential differences at each electrode position. This forms the basis of the [[forward-model]] in EEG source localization.

## Volume Conduction and the Forward Problem

The forward problem in EEG neurophysics concerns predicting scalp potentials given a known configuration of neural sources. This requires modeling the conductive geometry of the head—typically approximated as a set of concentric spherical shells or, more accurately, as individualized anisotropic conductivity distributions derived from [[neuroimaging-fmri|MRI]] segmentation.

Volume conduction theory establishes that scalp potentials are spatially smoothed relative to their underlying sources due to the conductive properties of the skull and other tissues. This volume conduction effect means that a point source at the cortical surface produces a potentials field extending across the entire scalp, with amplitudes falling approximately inversely with distance. Understanding this relationship is essential for interpreting [[functional-connectivity]] estimates derived from EEG, as volume conduction can produce spurious correlations between electrodes that must be corrected through appropriate preprocessing or source reconstruction.

## Source Localization and the Inverse Problem

Reconstructing the intracranial sources of observed scalp potentials constitutes the EEG inverse problem. This is inherently ill-posed: infinitely many source configurations can produce identical scalp recordings. Neurophysics provides several approaches to constrain the solution, including:

- ** Equivalent current dipoles**: Modeling the activat as a small number of point sources, appropriate for focal events such as epileptic spikes
- **Distributed source models**: Estimating activation across a dense grid of candidate locations, typically constrained by anatomical priors from [[brain-parcellation|parcellation]] schemas
- **Beamforming**: Spatial filtering techniques that pass neural activity from specific locations while attenuating contributions from other regions

The choice of inverse solution profoundly affects the interpretation of EEG data in [[whole-brain-modeling]], where model parameters are often fit to empirical [[connectivity]] estimates derived from source-space EEG.

## Relationship to Whole-Brain Modeling

The [[the-virtual-brain]] and similar [[whole-brain-modeling]] frameworks require forward models to predict EEG (and [[neuroimaging-meg|MEG]]) signals from simulated neural activity. Understanding volume conduction is essential for:

1. **[[model-validation]]**: Comparing simulated source activity to empirical EEG recordings requires a biophysically realistic forward model
2. **Connectivity estimation**: EEG-derived functional connectivity depends critically on how volume conduction effects are handled in preprocessing
3. **Source-space analysis**: Moving from sensor space to source space enables comparison with [[structural-connectivity]] anatomy derived from [[dti|DTI]]

The neural mass models employed in whole-brain simulations—such as the [[jansen-rit-model]] or [[wong-wang-model]]—produce population-level activity that must be translated into predicted scalp potentials through forward modeling. This coupling between [[network-dynamics]] and neurophysical forward models remains an active area of method development.

## Related Concepts

- [[eeg]] — The measurement modality this neurophysics describes
- [[volume-conduction]] — Physical mechanisms governing signal propagation
- [[source-localization]] — Reconstructing intracranial sources from scalp recordings
- [[neural-mass-models]] — Population-level models whose output feeds forward models
- [[forward-model]] — Predicting measurements from known sources
- [[functional-connectivity]] — Statistical dependencies between brain regions, as measured by EEG
- [[whole-brain-modeling]] — Large-scale network models requiring forward model coupling

## References

1. Paul L. Nunez and Ramesh Srinivasan (2006). *Electric Fields of the Brain: The Neurophysics of EEG* (2nd ed.). Oxford University Press.