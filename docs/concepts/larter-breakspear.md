---
created: 2026-04-20
sources:
- raw/papers/breakspear-2006.md
- raw/papers/wendling-2002.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/semanticscholar-71ffb8153870.md
- raw/papers/semanticscholar-7733d5476149.md
tags:
- neural-mass-models
- epilepsy-modeling
- nonlinear-dynamics
- bifurcation-analysis
- whole-brain-modeling
title: Larter-Breakspear Model
type: entity
updated: '2026-04-30'
---

# Larter-Breakspear Model

The Larter-Breakspear model is a conductance-based neural mass model that extends the Morris-Lecar equations to include three coupled populations: pyramidal cells, fast inhibitory interneurons, and a slow modulator population. Originally developed for simulating epileptic seizures, the model has become a foundational tool for studying bifurcation dynamics in large-scale brain networks and has been extensively used in [[whole-brain-modeling]] frameworks to generate [[resting-state]] [[functional-connectivity]] patterns.

## Historical Context and Motivation

The model emerged from a need to understand the collective dynamics of neuronal populations during epileptic seizures. The original lattice model by Larter, Speelman, and Worth (1999) formulated a system of coupled ordinary differential equations describing the membrane potentials of excitatory and inhibitory neural populations. This work built upon the Morris-Lecar formulation, which itself was an extension of the Hodgkin-Huxley model reduced to two variables. The key innovation was the inclusion of coupling between populations that could transition from stable resting dynamics to seizure-like oscillations through parameter variations.

Breakspear, Terry, and Friston (2003) substantially refined the model by introducing a third "modulatory" population that captures slow inhibitory dynamics mediated by GABA-B receptors and voltage-dependent conductances. This extension enabled the model to reproduce a richer repertoire of dynamical behaviors including alpha oscillations, burst synchronization, and the transition to seizure-like epileptiform activity. The model thus bridges the gap between single-[[neuron]] conductance-based models and population-level [[neural-mass-models]] like the [[jansen-rit]] model.

## Model Architecture

### Three Population Framework

The model comprises three distinct neural populations that interact through coupling terms. Understanding each population's role is essential for interpreting the model's behavior:

| Population | Variable | Biophysical Correlate | Timescale |
|------------|----------|----------------------|-----------|
| **Pyramidal (E)** | V | Principal excitatory neurons | Fast (ms) |
| **Fast Inhibitory (I)** | W | Parvalbumin interneurons | Fast (ms) |
| **Slow Modulatory (Z)** | M | SOM interneurons, GABA-B | Slow (100ms) |

The pyramidal population represents the primary excitatory output of the cortex, transmitting signals to other brain regions via long-range [[structural-connectivity]]. The fast inhibitory population provides rapid feedback control, analogous to feedforward inhibition in cortical microcircuits. The modulatory population introduces slower dynamics that can entrain network oscillations—a feature particularly relevant for modeling [[oscillator]] in the alpha (8-12 Hz) and beta (13-30 Hz) bands.

## Mathematical Formulation

The governing equations extend the Morris-Lecar formalism with coupling terms between populations. The membrane potential dynamics for the pyramidal population follow:

$$\ddot{V} = -g_{Ca} \cdot m_{Ca}(V) \cdot (V - V_{Ca}) - g_K \cdot W \cdot (V - V_K) - g_L \cdot (V - V_L) - g_{Na} \cdot m_{Na}(V) \cdot (V - V_{Na}) - d_v \cdot (V - V_E) + I_{ext}$$

where the variables represent maximal conductances ($g$) and reversal potentials ($V$) for calcium, potassium, leak, and sodium channels. The term $d_v$ represents the coupling strength from excitatory to excitatory populations—a key parameter governing the transition between healthy and epileptic dynamics. The parameter $I_{ext}$ represents external input current, which can be interpreted as sensory drive or endogenous cortical input.

The inhibitory and modulatory populations evolve according to similar equations but with different gating dynamics. The slow modulatory variable M evolves on a timescale approximately ten times slower than the fast variables, capturing the kinetics of slower inhibitory synaptic currents. This multi-timescale structure is a hallmark of the model and enables the generation of complex [[nonlinear-dynamics]] including [[bifurcation-analysis]] phenomena such as saddle-node and Hopf bifurcations.

## Parameter Regimes and Bifurcations

The Larter-Breakspear model exhibits rich bifurcation behavior as parameters are varied. The coupling parameter $d_v$ plays a particularly important role: at low values, the system rests in a stable fixed point corresponding to asynchronous baseline activity. As $d_v$ increases beyond a critical threshold, the system undergoes a Hopf bifurcation giving rise to oscillatory dynamics that mimic seizure onset. Further parameter changes can produce more complex dynamics including chaotic behavior.

Key parameters and their physiological interpretations:

| Parameter | Range | Biological Interpretation |
|-----------|-------|---------------------------|
| $g_{Ca}$ | 0.0-1.0 | L-type calcium channel density |
| $g_K$ | 0.0-2.0 | Potassium (delayed rectifier) conductance |
| $d_v$ | 0.0-0.55 | E→E coupling (recurrent excitation) |
| $I_{ext}$ | varies | External input / driving current |

## Relationship to Other Models

The Larter-Brekspear model occupies a specific niche in the hierarchy of [[neural-mass-models]]. Unlike the seminal [[wong-wang]] model (a firing-rate model for excitatory-inhibitory networks), the Larter-Breakspear formulation is conductance-based and captures membrane potential dynamics directly—similar to the reduced [[epileptor]] model used in [[epilepsy-modeling]]. However, it differs from the [[jansen-rit]] model in its level of abstraction: the Jansen-Rit framework uses a sigmoid function to convert synaptic input to firing rate, whereas the Larter-Breakspear model retains explicit voltage dynamics.

Compared to [[wilson-cowan]] formulations, the Larter-Breakspear model incorporates more biophysical detail regarding specific ionic currents (Na+, K+, Ca2+), making it better suited for studying pharmacological interventions and seizure dynamics but computationally more expensive for whole-brain simulations.

## Applications in Whole-Brain Modeling

The model has found extensive application in [[whole-brain]] simulations where it is embedded across brain regions using [[structural-connectivity]] matrices derived from [[diffusion-mri]] tractography. When coupled via large-scale connectivity, the Larter-Breakspear model can reproduce key features of empirical [[functional-connectivity]] including the presence of resting-state networks and their temporal dynamics. This application was notably explored by Honey, Kötter, Breakspear, and Sporns (2007), who demonstrated that the network structure of cerebral cortex shapes functional connectivity on multiple time scales.

The model's ability to generate seizure-like dynamics has also made it a cornerstone of frameworks like [[the-virtual-epileptic-brain]], where it serves to simulate pathological brain states and predict stimulation interventions. The three-population architecture provides a mechanistic basis for understanding how imbalances between excitation and inhibition—central to the [[epilepsy-modeling]] literature—give rise to pathological oscillations.

## Current Usage and Extensions

Contemporary work extends the Larter-Breakspear framework in several directions. The model has been incorporated into the [[tvb]] ecosystem for personalized brain modeling, where individual structural connectivity informs region-to-region coupling. Parameter estimation techniques based on Bayesian inference and [[variational-bayes]] allow researchers to fit the model to individual subject fMRI or EEG data, enabling patient-specific seizure modeling. The [[bifurcation-analysis]] of the model continues to yield insights into the dynamical mechanisms of seizure onset and termination, with implications for closed-loop [[brain-stimulation]] interventions.

## Related Concepts

- [[neural-mass-models]] — Theoretical framework for population-level modeling
- [[epilepsy-modeling]] — Clinical applications including seizure simulation
- [[nonlinear-dynamics]] — Chaos, bifurcations, and complexity in neural systems
- [[jansen-rit]] — Related three-population neural mass model
- [[bifurcation-analysis]] — Mathematical analysis of dynamic transitions
- [[whole-brain-modeling]] — Large-scale network simulations
- [[functional-connectivity]] — Correlated neural activity patterns
- [[oscillator]] — Rhythmic neural activity and its mechanisms
- [[structural-connectivity]] — Anatomical [[white-matter]] [[connectivity]]
- [[the-virtual-epileptic-brain]] — Clinical simulation platform