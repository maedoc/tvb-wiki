---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-e08252ec3941.md
- raw/papers/semanticscholar-a6fa6ab4802f.md
- raw/papers/semanticscholar-c836b6f72ba9.md
tags:
- neuroimaging-fmri
- bold
- functional-connectivity
- resting-state
title: Functional MRI
type: concept
updated: '2026-05-07'
---

# Functional MRI

**Functional Magnetic Resonance Imaging ([[fmri]])** is a [[neuroimaging]] technique that measures brain activity by detecting changes in blood flow. It is the dominant method for mapping human brain function in vivo.

## Overview

fMRI relies on the **blood-oxygen-level-dependent (BOLD)** contrast, which reflects the hemodynamic response to neural activity:
- Neural activation increases local blood flow
- This delivers more oxygenated blood, changing local magnetic susceptibility
- T2*-weighted MRI sequences detect these changes

Key paradigms:
- [[resting-state-fmri|[[resting-state]] fMRI]] — measures spontaneous brain activity
- [[resting-state-fmri|Task-based fMRI]] — measures evoked responses to stimuli

## Relationship to TVB

fMRI is the primary empirical constraint for TVB [[whole-brain]] models:
- TVB simulates BOLD signals from [[neural-mass-models]] using the [[hrf|hemodynamic response function]]
- Resting-state [[functional-connectivity]] matrices calibrate TVB [[structural-connectivity]] weights
- TVB predicts task-evoked BOLD changes that can be validated against task fMRI
- TVB models [[effective-connectivity]] via DCM and compare to fMRI-derived [[connectivity]]

## Related

- [[bold-signal]] — BOLD signal modeling and hemodynamics
- [[resting-state-vs-task-fmri]] — comparison of paradigms
- [[neuroimaging-eeg]] — complementary electrophysiological imaging
- [[dandi]] — archive for neurophysiology and neuroimaging data

## References

1. Mennahtullah Mabrouk, Reem Reda, Hana Hisham, Abdelrahman Hazem, Bola Hosny, Hossam Elsawaf, Saif Elaswad, Sameh Sherif. (2025). *A Hybrid Learning Approach for Detection of Autism Spectrum Disorder Using fMRI Data*. 2025 13th International Japan-Africa Conference on Electronics, Communications, and Computations (JAC-ECC). [DOI](https://doi.org/10.1109/JAC-ECC67970.2025.11417627))
2. L. Raimondo, Jurjen Heij, Tomas Knapen, Jeroen C. W. Siero, W. van der Zwaag, Serge O. Dumoulin. (2025). *Does the Cortical-Depth Dependence of the [[hemodynamic-response-function]] Differ Between Age Groups?*. Brain Topography. [DOI](https://doi.org/10.1007/s10548-025-01107-0))
3. N. J. Fesharaki, Artemy Vinogradov, David Ress, Jung Hwan Kim. (2026). *Spatial evolution in temporal dynamics of hemodynamic response function in human superior colliculi with ultra-high-resolution MRI at 9.4T*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2026.1741923))