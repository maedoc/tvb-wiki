---
title: ICLabel
created: 2026-04-29
updated: 2026-05-01
type: entity
tags: [software-brain-modeling, neuroimaging-eeg, source-separation, eeg]
sources: [raw/papers/semanticscholar-a31e27872281.md, raw/papers/arxiv-1903.06496.md]
---

# ICLabel

## Overview

ICLabel is an automated electroencephalographic (EEG) independent component classifier developed at the Swartz Center for Computational Neuroscience (SCCN) at the University of California, San Diego. The tool addresses a fundamental challenge in EEG preprocessing: when [[ICA]] (independent component analysis) is applied to decompose multichannel EEG recordings into statistically independent source signals, the resulting independent components (ICs) have no intrinsic labels or ordering. Researchers must manually inspect and classify each IC as either representing genuine brain activity or one of many possible artifact sources—a time-consuming process requiring substantial expertise. ICLabel provides an automated solution that classifies ICs into seven categories (Brain, Muscle, Eye, Heart, Line Noise, Channel Noise, and Other) with state-of-the-art accuracy while computing classifications approximately ten times faster than competing methods.

The ICLabel project comprises three integrated components: a large training dataset containing spatiotemporal features from over 200,000 ICs extracted from more than 6,000 EEG recordings, a crowdsourcing website (iclabel.ucsd.edu) that collects labels from EEG researchers worldwide to train and refine the classifier, and the automated ICLabel classifier itself, released as an [[EEGLAB]] plugin written in MATLAB with deep learning foundations built on MatConvNet.

## Motivation and Context

EEG recordings inherently contain mixtures of signals from multiple biological and non-biological sources. Each scalp electrode collects electrical activity from the brain as well as from eyes (producing EOG artifacts), muscles (EMG artifacts), the heart (ECG artifacts), and environmental sources such as 50/60 Hz line noise from electrical equipment. This mixing problem is compounded by volume conduction through the skull and scalp, which causes far-field potentials from distributed cortical regions to appear at nearly all electrode locations. Independent component analysis, particularly infomax ICA and its variants, has proven effective at unmixing these overlapping source signals into temporally independent components that can be attributed to distinct generators.

However, ICA decomposition produces an unordered set of components with no inherent interpretation. The researcher must determine whether each IC represents a neural source of interest or an artifact to be removed. Thismanual classification process is Slow, Inconsistent across researchers, and Impractical for large datasets involving hundreds of subjects. Prior automated classifiers such as [[MARA]] (Multiple Artifact Rejection Algorithm), [[ADJUST]], FASTER, SASICA, and IC_MARC addressed this need but suffered from limitations including binary rather than probabilistic outputs, limited category coverage, relatively slow computation speeds, and training on restricted datasets that limited generalization to new recording conditions.

ICLabel was developed to overcome these limitations through three innovations: training on an unprecedentedly large and diverse dataset spanning multiple recording environments, paradigms, and electrode montages; leveraging deep learning architectures (convolutional neural networks) for improved classification accuracy; and achieving computational efficiency sufficient for near-real-time applications including brain-computer interfaces and real-time source imaging.

## Technical Description

### IC Categories

The ICLabel classifier assigns each independent component a probability vector across seven categories:

**Brain ICs** contain activity originating from locally synchronous cortical patches, typically producing smoothly varying dipolar projections onto the scalp with power spectral densities showing increased power in the 5–30 Hz range and inverse relationship between frequency and power.

**Muscle ICs** capture electromyographic activity from muscle motor units, characterized by high broad-band power at frequencies above 20–30 Hz. These components often appear dipolar but with more localized scalp projections than brain sources due to their extracranial origin.

**Eye ICs** describe activity from the eyes, including blinks (producing brief DC shifts) and horizontal or vertical eye movements. Both exhibit scalp projections centered on the eyes due to the standing dipole of the retina-cornea electrical field.

**Heart ICs**, though relatively rare, represent electrocardiographic signals reaching scalp electrodes, recognizable by QRS complexes in their time series and diagonal gradient scalp topographies.

**Line Noise ICs** capture 50 Hz or 60 Hz alternating current interference from nearby electrical fixtures or poorly grounded amplifiers, showing concentrated power at the local line frequency.

**Channel Noise ICs** indicate components that are nearly independent from other channels, typically caused by high electrode-skin impedance, electrode movement, or other factors affecting single-channel signal quality.

**Other ICs** serve as a catch-all category for components that do not clearly fit other categories, often containing indeterminate noise or poorly separated mixtures of multiple sources.

### Classification Pipeline

The ICLabel classifier extracts multiple features from each ICA-decomposed EEG recording. Scalp topographies (32×32 pixel images showing IC projection patterns across electrode positions) are processed through two-dimensional convolutional neural networks. Power spectral densities (1–100 Hz, calculated using Welch's method with median averaging for artifact robustness) and autocorrelation functions are processed through one-dimensional convolutional networks. These features are concatenated and fed through fully connected layers producing the seven-element compositional probability vector.

The classifier was trained using crowd-sourced labels collected through the ICLabel website, where EEG researchers worldwide contributed labels for thousands of ICs. A Crowd Labeling Latent Dirichlet Allocation (CL-LDA) algorithm was applied to combine redundant labels from multiple labelers into probabilistic reference labels, accounting for varying expertise levels among contributors. Training incorporated data augmentation through left-right symmetry and sign negation of scalp topographies, effectively quadrupling the usable training set size.

### Performance

In systematic comparisons against other publicly available IC classifiers on an expert-labeled test set of 130 ICs, ICLabel achieved balanced accuracy of 0.841 (two-class Brain/Other) and 0.597 (seven-class), outperforming or performing comparably to the previous best method (IC_MARC) while requiring only approximately 170 ms per IC compared to IC_MARC's median runtime of 1.8 seconds—a roughly tenfold speed improvement.

## Key Features

- **Automated IC classification** across seven categories with compositional probability outputs
- **Integration with [[EEGLAB]]** through plugin architecture, callable from GUI or command line
- **Two model variants**: full ICLabel (using scalp topography, PSD, and autocorrelation features) and ICLabelLite (faster version excluding autocorrelation)
- **Near-real-time capability** suitable for brain-computer interface and real-time source imaging applications
- **Crowd-sourced training** leveraging expertise of hundreds of EEG researchers globally
- **Free and open source** distribution through EEGLAB plugin manager and GitHub

## Relationship to TVB

ICLabel is relevant to [[whole-brain-modeling]] and [[computational-neuroscience]] workflows that incorporate EEG data. In [[The Virtual Brain]] (TVB) ecosystem, EEG signals serve as a key neuroimaging modality for estimating functional connectivity and validating model dynamics. EEG preprocessing pipelines often employ ICA decomposition to remove artifacts (eye movements, muscle activity,line noise) before connectivity analysis. ICLabel provides a standardized, reproducible method for automated artifact rejection that can be integrated into TVB preprocessing workflows, particularly when EEG data are used to parameterize or constrain whole-brain models.

Additionally, ICLabel's source separation capabilities align with TVB's forward modeling framework, where simulated neural activity must be projected to sensor space through [[volume-conduction]] models. Clean ICs attributed to cortical sources can be used to derive empirical connectivity estimates (via [[functional-connectivity]] measures such as coherence or phase-locking value) that inform [[neural-mass-model]] parameters in TVB simulations.

Beyond preprocessing, ICLabel classification outcomes can inform [[connectome]]-based analyses by providing estimates of which ICs represent genuine [[electrophysiology]] signals versus artifacts. This is particularly valuable for [[resting-state]] EEG analyses where artifacts can confound connectivity estimates. The resulting "cleaned" component set can be used to construct [[functional-connectivity]] matrices that serve as empirical benchmarks for validating whole-brain simulation outputs.

## Related Software

- [[EEGLAB]]: MATLAB toolbox for EEG processing with which ICLabel integrates as a plugin
- [[fieldtrip]]: MATLAB toolbox for neurophysiology analysis; ICLabel can be run within FieldTrip workflows
- [[MARA]]: Earlier automated EEG IC classifier (Multiple Artifact Rejection Algorithm)
- [[ADJUST]]: IC classifier focused on eye artifact detection
- [[SASICA]]: Semi-automatic IC classification tool with educational features
- [[pyprep]]: Python pipeline for EEG preprocessing (includes IC classification capabilities)

## Key Papers

The primary methodology paper introducing ICLabel was published in NeuroImage:

- Pion-Tonachini, L., Kreutz-Delgado, K., & Makeig, S. (2019). ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. *Neuroimage*, 198, 181-197. doi:10.1016/j.neuroimage.2019.05.026

This paper describes the classifier architecture, training methodology, dataset creation through crowdsourcing, and systematic performance comparisons against MARA, ADJUST, FASTER, SASICA, and IC_MARC.

## Related Concepts

- [[ICA]];
- [[source-separation]];
- [[EEGLAB]];
- [[neuroimaging-eeg]];
- [[functional-connectivity]];
- [[resting-state]];
- [[electrophysiology]];
- [[neural-mass-model]];
- [[whole-brain-modeling]];