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
updated: '2026-05-06'
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
- [[task-fmri|Task-based fMRI]] — measures evoked responses to stimuli

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