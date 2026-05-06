---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-e5e78e93bf31.md
- raw/papers/arxiv-2506.22951.md
- raw/papers/wilson-cowan-1972.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/strogatz-1994.md
tags:
- neural-mass-models
- whole-brain-modeling
- mean-field-theory
- dynamical-systems-theory
- network-dynamics
- parameter-estimation
- brain-oscillations
- epilepsy-modeling
title: Neural Mass Models
type: concept
updated: '2026-05-06'
---

## Definition

Neural mass models (NMMs) are mathematical models that represent the collective dynamics of large populations of neurons using a reduced set of state variables. Rather than simulating individual neurons and synapses, NMMs abstract the behavior of thousands or millions of neurons into a small number of coupled differential equations that describe the mean activity of excitatory and inhibitory neuronal pools. This reductionist approach makes it possible to simulate large-scale brain networks at tractable computational cost while retaining the essential dynamical features of the underlying neurophysiology. Neural mass models were pioneered in the 1990s by Benjamin Jansen and Vincent Rit (the [[jansen-rit]] model) and built upon earlier work by Hugh Wilson and [[wilson-cowan]] on population dynamics.

## Role in Whole-Brain Modeling

In the context of [[whole-brain]] modeling, neural mass models serve as the fundamental dynamical unit that is embedded in a network defined by [[structural-connectivity]] matrices derived from diffusion imaging and tractography. Each brain region is represented by a neural mass model whose state evolves over time according to its intrinsic dynamics and the inputs it receives from other regions via the connectome. The resulting simulations produce synthetic [[functional-connectivity]] patterns that can be compared with empirically observed [[resting-state]] networks measured via [[fmri]] [[hrf]], [[eeg]], [[meg]], or the [[meg-eeg-toolbox]].

The appeal of neural mass models for whole-brain simulations lies in their computational efficiency. A single neural mass model typically requires only 3–8 state variables and can be integrated in real-time or faster on modest hardware. When coupled across 68–360 brain regions (depending on the [[parcellation]] used), whole-brain simulations using neural mass models can complete in minutes rather than the hours or days required by [[spiking-neural-networks]] (for which the [[lfpykern]] library offers LFP computation tools) that simulate individual neurons. This efficiency enables parameter sweeps, [[bifurcation-analysis]], and clinical applications such as [[personalized-brain-modeling]] for epilepsy Surgical planning.

## Mathematical Framework

Neural mass models are derived from [[mean-field-theory]], which approximates the collective behavior of a neuronal population by averaging over the activities of its constituent neurons. The key assumption is that, in a large homogeneous population, fluctuations around the mean activity become negligible, allowing the population to be described by macroscopic variables such as the average membrane potential or firing rate.

The simplest neural mass model is a two-variable system describing the interactions between an excitatory population and an inhibitory population. The dynamics can be expressed in the general form:

$$\tau_e \frac{dx_e}{dt} = -x_e + S(W_{ee} \cdot x_e - W_{ei} \cdot x_i + I_{ext})$$

$$\tau_i \frac{dx_i}{dt} = -x_i + S(W_{ie} \cdot x_e - W_{ii} \cdot x_i + I_{ext})$$

where $x_e$ and $x_i$ represent the mean activity of excitatory and inhibitory populations, $\\tau_e$ and $\\tau_i$ are their respective time constants, $W_{ij}$ are the coupling weights, and $S(\\cdot)$ is a nonlinear activation function (often sigmoidal or exponential). The input term $I_{ext}$ may represent external driving from sensory stimuli or endogenous noise.

More sophisticated neural mass models incorporate multiple state variables to capture effects such as synaptic dynamics, post‑synaptic potentials, and gating variables. The [[jansen-rit]] model, for example, uses six state variables: three for excitatory post‑synaptic potentials (EPSPs) and three for inhibitory post‑synaptic potentials (IPSPs).

## Key Neural Mass Models

### Jansen‑Rit Model

The [[jansen-rit]] model, developed in 1995, is the most widely used neural mass model in [[dynamic-causal-modeling]] (DCM) and [[tvb]] simulations. It consists of three coupled populations (pyramidal cells, excitatory interneurons, and inhibitory interneurons) that generate realistic EEG rhythms in the alpha (8–12 Hz) and beta (13–30 Hz) bands. The model's popularity stems from its relative simplicity and its ability to produce biologically plausible oscillations without extensive parameter tuning. Fooof

### Wilson‑Cowan Model

The [[wilson-cowan]] model, published in 1972, was one of the earliest formal models of population neural dynamics. It introduced the mathematical framework of excitatory and inhibitory populations with nonlinear interaction terms, demonstrating how localized cortical activity can produce traveling waves and oscillations. While simpler than modern NMMs, the Wilson‑Cowan equations remain a foundational reference for understanding population‑level dynamics.

### Wong‑Wang Model

The [[wong-wang]] model (also known as the [[wong-wang-exc-inh]] model) extends the two‑population framework with a detailed treatment of synaptic dynamics, including NMDA‑mediated excitation and GABA‑mediated inhibition. It has been particularly influential in studies of [[oscillator]] and schizophrenia models, where it reproduces the altered gamma oscillations observed in clinical populations.

### Epileptor Model

The [[epileptor]] model was developed specifically for [[epilepsy-modeling]] and features a set of five coupled differential equations that can exhibit seizure‑like discharges. It represents a neural mass model designed to capture the transition from normal [[brain-dynamics]] to pathological epileptiform activity, making it a key tool for predicting seizure onset and evaluating surgical interventions.

## Relationship to Other Approaches

Neural mass models occupy an intermediate position between detailed biophysical models (such as those simulated in [[nest]] or Brian2) and purely descriptive models (such as autoregressive models of fMRI time series). Unlike [[spiking-neural-networks]] that simulate individual neurons with anatomical realism, NMMs aggregate neurons into populations, sacrificing single‑neuron specificity for speed and tractability. However, they retain sufficient biological interpretability to be mapped to physiological mechanisms.

The relationship between neural mass models and [[dynamic-causal-modeling]] is particularly close: DCM uses the Jansen‑Rit model as its [[forward-model]] for generating synthetic EEG/MEG data, and parameter estimation in DCM amounts to inverting the neural mass model to fit observed neuroimaging data. Similarly, [[tvb]] provides a platform for whole‑brain simulations using multiple neural mass models (Jansen‑Rit, Wong‑Wang, Epileptor) embedded in patient‑specific connectomes.

**See also [[marsatlas]] and [[bids]] for a software platform that integrates neural mass models in whole‑brain simulations.**

## Parameter Estimation and Calibration

A critical challenge in applying neural mass models is estimating the free parameters (synaptic gains, time constants, connection strengths) from empirical data. Traditional approaches include Bayesian inversion via DCM (which uses [[variational-bayes]] to approximate the posterior distribution over parameters) and optimization‑based fitting to match simulated and observed [[functional-connectivity]] patterns. More recently, machine learning approaches have been applied to accelerate [[parameter-estimation]], enabling personalized brain models to be calibrated to individual subjects within practical time constraints.

## Open Questions and Limitations

Despite their widespread use, neural mass models face several open questions. The validity of the mean‑field approximation breaks down when population‑level correlations become strong (as near critical points or during seizures), and it remains unclear how well NMMs capture the effects of cell‑type‑specific [[connectivity]]. Parameter identifiability is also a concern: many parameter combinations can produce similar functional dynamics, complicating biological interpretation. Ongoing research aims to address these limitations through more biophysically grounded neural mass formulations and hybrid models that combine population‑level dynamics with selected single‑[[neuron]] detail.

## References

1. Raul de Palma Aristides, Pau Clusella, R. Sanchez-Todo, G. Ruffini, Jordi García-Ojalvo. (2026). *Emergence of multifrequency activity in a laminar neural mass model*. PLoS Computational Biology. [DOI](](https://doi.org/10.1371/journal.pcbi.1014022))
2. Ramiro Plüss, Hernán Villota, Patricio Orio. (2025). *Hemispheric-Specific Coupling Improves Modeling of Functional Connectivity Using Wilson-Cowan Dynamics*. [Link](](https://arxiv.org/abs/2506.22951))
3. Hugh R. Wilson, Jack D. Cowan. *Excitatory and inhibitory interactions in localized populations of model neurons*. Biophysical Journal. [DOI](https://doi.org/10.1016/S0006-3495(72)86068-5)
4. Rosa Maria Delicado, Gemma Huguet, Pau Clusella. (2025). *Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation Neural Mass Models*. [Link](](https://arxiv.org/abs/2512.03907))
5. (authors unknown). *[[nonlinear-dynamics]] and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*.

## ORPHAN PAGE CONTEXT (hrf)
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

The **[[hemodynamic-response-function]] (HRF)** describes the change in blood oxygen level-dependent (BOLD) signal that follows neural activity in the brain, measured via functional magnetic resonance imaging ([[fmri]]). When neurons fire, they consu

## ORPHAN PAGE CONTEXT (lfpykern)
---
created: 2024-03-15
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/semanticscholar-bceb6bea8311.md
tags:
- software
- lfp
- volume-conduction
- computational-neuroscience
title: LFPykern
type: entity
updated: '2026-05-05'
---

LFPykern is a Python library for computing local field potentials (LFPs) from spiking neural network simulations. The software implements a kernel-based approach to calculating the extracellular electric potential re