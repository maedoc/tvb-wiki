---
created: 2026-05-04
sources:
- raw/papers/friston-1998-hrf.md
- raw/papers/glover-1999-hrf.md
tags:
- neuroimaging-fmri
- neural-mass-models
- dynamical-systems-theory
- brain-dynamics
type: concept
updated: '2026-05-06'
---

# HRF

## Overview

The **[[hemodynamic-response-function]] (HRF)** describes the change in blood oxygen level-dependent (BOLD) signal that follows neural activity in the brain, measured via functional magnetic resonance imaging ([[fmri]]). When neurons fire, they consume oxygen and trigger a cascade of vascular responses—increased blood flow, blood volume, and oxygenated hemoglobin—that collectively produce the [[bold-signal]] detectable by fMRI. The HRF represents this vascular response as a function of time, typically peaking around 4–6 seconds after neural activation and returning to baseline after approximately 20–30 seconds. This temporal lag between neural events and their hemodynamic readouts fundamentally shapes how we interpret fMRI data and necessitates careful modeling to extract true neural dynamics from the BOLD signal.

The neurophysiological basis of the HRF involves neurovascular coupling—the mechanism by which active neurons signal to nearby blood vessels to increase blood flow. This coupling occurs through astrocytic signaling, where active neurons release neurotransmitters that trigger astrocytes to release vasodilators (e.g., nitric oxide, prostaglandins) causing arteriole dilation and increased cerebral blood flow. Crucially, this vascular response is both delayed (∼2 seconds to onset, 4–6 seconds to peak) and spatially blurred relative to the underlying neural activity, as blood flow changes spread beyond the exact location of neuronal firing.

## Canonical Mathematical Models

The canonical HRF is most commonly modeled as a difference of two gamma functions, capturing both the main response and the subsequent undershoot commonly observed in BOLD data. Mathematically, this **double gamma function** takes the form:

$$HRF(t) = A\\left(\\frac{t^{\\alpha_1-1}\\tau_1^{\\alpha_1}e^{-t/\\tau_1}}{\\Gamma(\\alpha_1)} - c\\frac{t^{\\alpha_2-1}\\tau_2^{\\alpha_2}e^{-t/\\tau_2}}{\\Gamma(\\alpha_2)}\\n\right)$$

where the first gamma term captures the main hemodynamic peak and the second term (scaled by the parameter $c$, typically around 0.35–0.4) models the post-stimulus undershoot. In the widely-used SPM implementation, the parameters are $\alpha_1 = 6$, $\\tau_1 = 1$, $\alpha_2 = 16$, $\\tau_2 = 1$, yielding a peak at approximately 5 seconds and an undershoot around 10–15 seconds post-stimulus.

Single gamma functions are sometimes used for rapid event-related designs where the undershoot is less relevant, while more sophisticated models incorporate additional parameters to capture subject-specific HRF shapes, regional variations, or drug-induced changes in neurovascular coupling. The **Friston et al. (1998)** model established the double gamma as standard, though later work by Glover (1999) and others refined parameter estimates and demonstrated significant inter-subject and inter-regional variability.

## HRF Variability and Custom Models

Empirical studies consistently reveal substantial HRF variability across brain regions, individuals, and experimental contexts. The primary visual cortex typically shows earlier and narrower HRF peaks (∼4–5 seconds) compared to frontal regions (∼6–8 seconds), reflecting regional differences in vascular anatomy and neurovascular coupling efficiency. This spatial variability has motivated the development of region-specific HRF templates and the use of basis functions that allow the HRF shape to vary within the general [[linear|linear model]] (GLM) framework.

Subject-level HRF estimates differ by approximately 20–30% across individuals, and within-subject variability across sessions can reach 10–15%, demanding attention in longitudinal studies and clinical applications. Pathological conditions—stroke, Alzheimer's disease, and vascular dementia—can substantially alter HRF characteristics, complicating interpretation of patient data. These considerations have driven development of methods for **HRF estimation** via deconvolution, basis function approaches (Fourier, gamma, smooth basis sets), and parametric models that allow flexible fitting to empirical data.

## HRF in fMRI Analysis

Within the GLM framework for fMRI analysis, the HRF serves as the convolution kernel for modeling the expected BOLD response to experimental stimuli. Neural event sequences are convolved with the HRF to produce predicted time series, which are then fit to observed BOLD data to estimate the amplitude of neural responses to each condition. This convolution approach accounts for the slow, blurred nature of the hemodynamic response but requires assumptions about HRF shape that may not hold across all brain regions or subject populations.

**HRF deconvolution** methods attempt to reconstruct the underlying neural activity time course from the observed BOLD signal by inverting the convolution operation. These methods require regularization (temporal smoothness, sparsity constraints) to produce stable solutions given the ill-posed nature of the deconvolution problem. The resulting neural time courses can be used for [[connectivity]] analyses, decoded into cognitive states, or combined with other [[neuroimaging]] modalities (EEG, MEG) for multimodal integration.

## Relationship to TVB

In [[The Virtual Brain]] (TVB) framework, the HRF plays a critical role in bridging the gap between simulated neural activity and empirically measurable BOLD signals. TVB simulates large-scale brain dynamics using neural mass models such as the [[Jansen-Rit model]] or [[Wong-Wang model]], which produce synthetic electrophysiological signals (local field potentials, or LFPs) representing aggregate neuronal firing. The HRF acts as a forward model that transforms these simulated neural time courses into predicted BOLD signals, enabling direct comparison with empirical fMRI data for model validation and parameter estimation.

TVB's default HRF implementation uses the canonical double gamma function, consistent with the SPM convention, though users can specify custom HRF shapes to explore the effects of HRF variability on whole-[[brain-dynamics]]. The coupling between [[neural-mass-models]] and the HRF is particularly important for TVB's [[epilepsy-modeling]] applications, where seizure dynamics may produce BOLD signals with atypical temporal signatures. TVB also supports convolution-based approaches for generating simulated fMRI time courses from [[resting-state]] simulations, enabling comparison with functional connectivity patterns observed in empirical data.

## Related Concepts

The HRF relates closely to the [[bold-model]]—the biophysical model describing the relationship between neural activity, cerebral blood flow, blood volume, and the BOLD signal. Understanding HRF also requires familiarity with [[neuroimaging-fmri]] principles, particularly the [[functional-connectivity]] analyses that rely on HRF-convolved signals. The HRF fundamentally shapes [[effective-connectivity]] analyses using [[dynamic-causal-modeling]] (DCM), where accurate characterizations of the hemodynamic response are essential for inferring causal neural interactions from BOLD data. The HRF's temporal characteristics also connect to [[brain-oscillations]] research, where mismatches between neural and hemodynamic timescales can complicate cross-modal comparisons. In [[whole-brain-modeling]] contexts, the HRF provides the essential link that enables [[personalized-brain-modeling]] workflows to validate simulated dynamics against empirical fMRI measurements.