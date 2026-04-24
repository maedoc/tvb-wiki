Now I'll write the improved version incorporating all three source papers more deeply.

```yaml
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
  - effective-connectivity
sources:
  - raw/papers/arxiv-2508.04824.md
  - raw/papers/arxiv-2603.25991.md
  - raw/papers/breakspear-2006.md
---

# Epileptor Model

The **Epileptor** is a composite [[neural-mass-models|neural mass model]] that captures epileptic seizure phenomenology across fast, slow, and ultra-slow timescales. Introduced by Jirsa and colleagues in 2014, it couples two nonlinear subsystems—one generating rapid ictal discharges and another governing slower inhibitory control—through a permittivity variable that drives transitions between interictal and ictal regimes. Its low-dimensional formulation embeds naturally into [[structural-connectivity]] networks, making it the default seizure model in [[tvb|The Virtual Brain]] and the [[the-virtual-epileptic-brain|Virtual Epileptic Patient]] platform.

## Motivation and Historical Context

Before the Epileptor, population-level seizure models were either too abstract to capture clinical waveforms or too detailed to scale to patient-specific [[brain-network]]s. Earlier frameworks such as the [[jansen-rit]] and [[larter-breakspear]] models reproduced rhythmic cortical activity but were not designed for the full sequence of seizure onset, recruitment, evolution, and termination. Breakspear et al. (2006) took an important step by extending the Jansen-Rit model into a spatially distributed neural field, using asymptotic analysis to show that primary generalized seizure dynamics—including 3 Hz spike-wave discharges typical of absence seizures and tonic-clonic transitions—could be reduced to low-dimensional bifurcation topology. This work established that large-scale seizure propagation depends on the interplay between local columnar excitability and long-range couplings, a principle the Epileptor would later refine with explicit multi-timescale architecture.

The Epileptor closes the gap between these earlier neural field models and clinical neurology by folding seizure biophysics into a small set of interpretable differential equations with a dedicated slow variable for seizure termination—a feature earlier models lacked. This design reflects a broader shift in computational neurology toward clinically validated, [[personalized-brain-modeling|personalized dynamical models]]. In the Virtual Epileptic Patient workflow, region-specific parameters are assigned to each node of a [[connectome]] reconstructed from [[diffusion-mri|diffusion MRI]], turning the Epileptor into a patient-specific testbed for surgical planning and [[brain-stimulation|neuromodulation]].

## Mathematical Formulation

The canonical Epileptor comprises five state variables across two coupled populations.

**Population 1 (fast seizure dynamics):**
```
ẋ₁ = y₁ - f₁(x₁) - z + I_ext₁
ẏ₁ = c - d·x₁² - y₁
ż = r·(4(x₁ - x₀) - z)
```

Variables x₁ and y₁ form a fast subsystem analogous to mean membrane potential and recovery current in a cortical pyramidal population. The cubic nonlinearity f₁(x₁) = a·x₁³ + b·x₁² enables bistability, allowing the population to switch between a stable fixed point and a limit cycle depending on the ultra-slow permittivity variable z. This slow variable captures homeostatic processes—such as extracellular potassium accumulation, metabolic demand, or shifts in [[k-ion-exchange|ionic homeostasis]]—that modulate excitability over seconds to minutes. The parameter x₀, the **epileptogenicity index**, quantifies how far a region is from seizure threshold. Because z evolves roughly three orders of magnitude more slowly than x₁ (r ≈ 0.00035), the system behaves as a relaxation oscillator, a structure studied extensively through [[dynamical-systems-theory|dynamical systems theory]] and [[bifurcation-analysis|bifurcation analysis]].

**Population 2 (slow inhibitory gate):**
```
ẋ₂ = -y₂ + x₂ - x₂³ + I_ext₂ + K_s·z - K_f·(x₁ - x₀)
ẏ₂ = (-y₂ + f₂(x₂)) / τ
```

Population 2 sculpts seizure offset through slower inhibitory feedback, with τ setting the inhibitory timescale. Coupling terms K_s and K_f link the permittivity variable to delayed feedback, a mechanism that Proix et al. (2014) termed **permittivity coupling** and showed determines how seizures recruit neighbouring regions in partial epilepsy. The output x₂ − x₁ approximates the macroscopic field potential or intracranial [[eeg|EEG]]. The interplay between the excitable fast subsystem and slower inhibition generates the stereotyped waveform of focal seizures: abrupt low-voltage fast oscillations followed by rhythmic spike-and-wave complexes that gradually slow before termination.

## Dynamical Regimes

As x₀ is varied, the Epileptor traverses distinct regimes separated by bifurcations.

When x₀ ≲ −2.0, the system rests at a stable fixed point—the **interictal** state—where perturbations decay rapidly. In the **pre-ictal** window (−2.0 < x₀ < −1.5), noise can transiently push the system across a saddle-node on invariant circle (SNIC) bifurcation, producing intermittent bursts proposed as seizure-prediction markers. For x₀ ≳ −1.5, the fixed point loses stability and the system enters a sustained limit cycle—the **ictal** state—with rhythmic discharges that persist until z accumulates enough to force the system back across a homoclinic bifurcation. This fast-slow hysteresis explains why seizures cannot stop instantaneously: the permittivity variable must degrade first, mirroring the clinical observation that seizures run their natural course before post-ictal depression sets in.

## Biological Grounding of Parameters

Each parameter maps onto measurable physiology, which is essential for clinical translation. The epileptogenicity index x₀ proxies local tissue excitability—influenced by pathological neuron density, gliosis, and altered ionic homeostasis—and can be estimated from clinical markers such as interictal spike frequency or [[functional-connectivity|functional connectivity]] anomalies. The permittivity variable z reflects slow ionic or metabolic buildup; experimental evidence implicates extracellular potassium accumulation and hypoxia as drivers of the ultra-slow dynamics that govern seizure termination. The coupling parameters K_s and K_f weight how strongly nearby regions influence seizure propagation, linking model dynamics to the underlying [[structural-connectivity|structural connectome]] reconstructed from [[tractography]].

## Clinical Translation and Control

At the network scale, Triebkorn et al. (2025) embedded excitable Epileptor neural fields in a millimetre-scale virtual brain reconstructed from diffusion MRI of a drug-resistant epilepsy patient. They demonstrated that realistic [[effective-connectivity|cortico-cortical delays]] alone are sufficient to generate self-sustaining re-entry loops—a long-suspected driver of human seizures. Systematic parameter sweeps revealed a narrow delay-coupling window that predicted oscillation frequency and seizure duration across 184 recorded seizures, and precisely timed biphasic stimuli or sub-millimetre virtual lesions aborted re-entry in silico. The resulting phase-dependent termination rules were validated against intracranial recordings, establishing a patient-specific testbed for precision neuromodulation and minimally invasive disconnection surgery.

Acharya and Nozari (2026) provided the first rigorous [[dynamic-causal-modeling|passivity-based control]] analysis of the Epileptor, motivated by the fact that only 18% of drug-resistant epilepsy patients who undergo closed-loop neuromodulation become seizure-free with current clinical methods. They proved that standard seizure dynamics are neither passive nor trivially passivatable, yet demonstrated that sufficiently strong passive feedback can stabilize the system, and that output redesign can render it passive. These results supply a principled framework for sensor placement and feedback gain selection in next-generation [[brain-stimulation|closed-loop neurostimulation]] devices.

## Relationship to Other Models and Variants

The Epileptor occupies a middle ground between detailed [[spiking-neural-networks]] and abstract [[oscillator]] models. Compared to the [[wilson-cowan]] equations—which describe population firing rates with a single timescale—the Epileptor adds multi-timescale bifurcation architecture tailored to seizure generation and termination. Unlike the [[jansen-rit]] model, which is optimized for evoked and resting-state [[eeg|EEG]] rhythms in non-epileptic cortex, the Epileptor's permittivity variable creates intrinsic bistability that captures the all-or-none character of seizure initiation. The Breakspear et al. (2006) neural field approach, while pioneering in its asymptotic treatment of generalized seizures, did not include the dedicated termination mechanism that the Epileptor's slow variable provides.

Several variants extend the framework. The [[epileptorcodim3|EpileptorCodim3]] variant introduces additional bifurcation parameters to classify both SNIC and Hopf seizure onsets—important because the two onset types require different surgical strategies. The [[epileptor-rs|EpileptorRS]] variant adapts the dynamics for resting-state [[functional-connectivity]] studies in epilepsy cohorts, removing the slow variable to produce stochastic fluctuations consistent with interictal data. Together, these extensions have cemented the Epileptor as the standard workhorse for large-scale seizure simulation in [[whole-brain-modeling]] and personalized epilepsy management pipelines.
```
