---
title: Epileptor Model
created: 2024-01-01
updated: 2026-04-24
type: concept
tags:
  - neural-mass-models
  - epilepsy-modeling
  - bifurcation-analysis
  - nonlinear-dynamics
  - dynamical-systems-theory
  - whole-brain-modeling
  - software-tvb
  - personalized-brain-modeling
  - structural-connectivity
  - functional-connectivity
  - brain-oscillations
  - brain-stimulation
sources:
  - raw/papers/arxiv-2508.04824.md
  - raw/papers/arxiv-2603.25991.md
  - raw/papers/breakspear-2006.md
---

# Epileptor Model

The **Epileptor** is a composite [[neural-mass-models|neural mass model]] that captures epileptic seizure phenomenology across fast, slow, and ultra-slow timescales. Introduced by Jirsa and colleagues in 2014, it couples two nonlinear subsystems—one generating rapid ictal discharges and another governing slower inhibitory control—through a permittivity variable that drives transitions between interictal and ictal regimes. Its low-dimensional formulation embeds naturally into [[structural-connectivity]] networks, making it the default seizure model in [[tvb|The Virtual Brain]] and the [[the-virtual-epileptic-brain|Virtual Epileptic Patient]] platform.

## Motivation and Historical Context

Before the Epileptor, population-level seizure models were either too abstract to capture clinical waveforms or too detailed to scale to patient-specific [[brain-network]]s. Earlier frameworks such as the [[jansen-rit]] and [[larter-breakspear]] models reproduced rhythmic cortical activity but were not designed for the full sequence of seizure onset, recruitment, evolution, and termination. The Epileptor closes this gap by folding seizure biophysics into a small set of interpretable differential equations, an approach that builds on earlier neural field extensions by Breakspear et al. (2006) while adding explicit multi-timescale bifurcation architecture.

This design reflects a broader shift in computational neurology toward clinically validated, personalized dynamical models. In the Virtual Epileptic Patient workflow, region-specific parameters are assigned to each node of a [[connectome]] reconstructed from diffusion MRI, turning the Epileptor into a patient-specific testbed for surgical planning and neuromodulation.

## Mathematical Formulation

The canonical Epileptor comprises five state variables across two coupled populations.

**Population 1 (fast seizure dynamics):**
```
ẋ₁ = y₁ - f₁(x₁) - z + I_ext₁
ẏ₁ = c - d·x₁² - y₁
ż = r·(4(x₁ - x₀) - z)
```

Variables x₁ and y₁ form a fast subsystem analogous to mean membrane potential and recovery current in a cortical pyramidal population. The cubic nonlinearity f₁(x₁) = a·x₁³ + b·x₁² enables bistability, allowing the population to switch between a stable fixed point and a limit cycle depending on the ultra-slow permittivity variable z. This slow variable captures homeostatic processes—such as extracellular potassium accumulation or metabolic shifts—that modulate excitability over seconds to minutes. The parameter x₀, the **epileptogenicity index**, quantifies how far a region is from seizure threshold. Because z evolves roughly three orders of magnitude more slowly than x₁ (r ≈ 0.00035), the system is a relaxation oscillator studied extensively in [[dynamical-systems-theory|dynamical systems theory]].

**Population 2 (slow inhibitory gate):**
```
ẋ₂ = -y₂ + x₂ - x₂³ + I_ext₂ + K_s·z - K_f·(x₁ - x₀)
ẏ₂ = (-y₂ + f₂(x₂)) / τ
```

Population 2 sculpts seizure offset through slower inhibitory feedback, with τ setting the inhibitory timescale. Coupling terms K_s and K_f link the permittivity variable to delayed feedback. The output x₂ − x₁ approximates the macroscopic field potential or intracranial EEG. The interplay between the excitable fast subsystem and slower inhibition generates the stereotyped waveform of focal seizures: abrupt low-voltage fast oscillations followed by rhythmic spike-and-wave complexes that gradually slow before termination.

## Dynamical Regimes

As x₀ is varied, the Epileptor traverses distinct regimes separated by bifurcations.

When x₀ ≲ −2.0, the system rests at a stable fixed point—the **interictal** state—where perturbations decay rapidly. In the **pre-ictal** window (−2.0 < x₀ < −1.5), noise can transiently push the system across a saddle-node on invariant circle (SNIC) bifurcation, producing intermittent bursts proposed as seizure-prediction markers. For x₀ ≳ −1.5, the fixed point loses stability and the system enters a sustained limit cycle—the **ictal** state—with rhythmic discharges that persist until z accumulates enough to force the system back across a homoclinic bifurcation. This fast-slow hysteresis explains why seizures cannot stop instantaneously: the permittivity variable must degrade first, mirroring the clinical observation that seizures run their natural course.

## Clinical Translation and Control

Parameters map onto measurable physiology: x₀ proxies local tissue excitability (pathological neuron density, gliosis, altered ionic homeostasis), while z reflects slow ionic or metabolic buildup. These interpretations connect the model to clinical biomarkers and justify its use in [[personalized-brain-modeling|patient-specific modeling]].

At the network scale, Triebkorn et al. (2025) embedded Epileptor neural fields in a millimetre-scale virtual brain and showed that realistic cortico-cortical delays alone suffice to generate self-sustaining re-entry loops. A narrow delay-coupling window predicted oscillation frequency and seizure duration across 184 recorded seizures, and phase-dependent termination rules derived from in silico stimulation were validated against intracranial recordings.

Acharya and Nozari (2026) provided the first rigorous passivity-based control analysis of the Epileptor. They proved that standard seizure dynamics are neither passive nor trivially passivatable, yet sufficiently strong passive feedback can stabilize the system, and output redesign can render it passive. These results supply a principled framework for sensor placement and feedback gain selection in closed-loop neurostimulation devices.

## Relationship to Other Models and Variants

The Epileptor sits between detailed [[spiking-neural-networks]] and abstract [[oscillator]] models. Compared to the [[wilson-cowan]] equations, it adds multi-timescale bifurcation architecture tailored to seizures. Unlike the [[jansen-rit]] model—optimized for evoked responses—the Epileptor's permittivity variable creates intrinsic bistability that captures the all-or-none character of seizure initiation.

The [[epileptorcodim3|EpileptorCodim3]] variant introduces additional bifurcation parameters to classify both SNIC and Hopf onsets. The [[epileptor-rs|EpileptorRS]] variant adapts the framework for resting-state [[functional-connectivity]] studies in epilepsy cohorts. Together, these extensions have cemented the Epileptor as the standard workhorse for large-scale seizure simulation in [[whole-brain-modeling]] pipelines.
