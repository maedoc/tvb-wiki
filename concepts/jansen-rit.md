---
title: "Jansen-Rit Model"
created: 2026-04-20
updated: 2026-04-21
type: concept
tags: [neural-mass-models, eeg, meg, brain-oscillations]
---

# Jansen-Rit Model

The Jansen-Rit model is a neural mass model of a single cortical column capable of generating realistic EEG and MEG signals. It is the default neural mass model in The Virtual Brain (TVB) and the foundation of Dynamic Causal Modeling (DCM) for EEG/MEG.

## Overview

Developed by Benjamin Jansen and Vincent Rit in 1995, the model extends earlier work by Lopes da Silva on thalamocortical alpha rhythms to specifically model cortical columns and their contribution to scalp EEG/MEG signals.

## Model Architecture

### Three Populations

The Jansen-Rit model consists of three interconnected neural populations:

| Population | Description | Neurotransmitter | Postsynaptic Effect |
|------------|-------------|------------------|---------------------|
| **P (Pyramidal)** | Main output neurons | Glutamate (AMPA) | Excitatory |
| **E (Excitatory interneurons)** | Local excitatory cells | Glutamate (AMPA) | Excitatory |
| **I (Inhibitory interneurons)** | Local inhibitory cells | GABA (GABA-B) | Inhibitory (slow) |

### Connectivity

```
        ┌─────────────────────────────────────────┐
        │                                         │
        ▼                                         │
   ┌─────────┐      ┌─────────┐      ┌─────────┐ │
   │    P    │◄─────│    E    │◄─────│    P    │─┘
   │(output) │      │(excit.) │      │(output) │
   └────┬────┘      └────┬────┘      └────┬────┘
        │                │                │
        │                │                │
        └───────────────►│◄───────────────┘
                         │
                   ┌─────────┐
                   │    I    │
                   │(inhib.) │
                   └────┬────┘
                        │
                        └──────────────────────►
```

### Mathematical Formulation

The model uses post-synaptic impulse response functions (PSPs) modeled as alpha functions:

```
PSP(t) = (A·t/τ)·exp(-t/τ)   for t ≥ 0
```

Where A is maximum amplitude and τ is time constant.

**Equations** (for each population i):

```
y_i(t) = ∫ PSP_i(t-s) · Sigmoid(x_i(s)) ds
```

Where x_i is the net input to population i, and Sigmoid is a logistic function converting membrane potential to firing rate.

### Standard Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| A (pyramidal) | 3.25 mV | Excitatory PSP amplitude |
| B (inhibitory) | 22 mV | Inhibitory PSP amplitude |
| a (exc. time const) | 100 s⁻¹ | 1/τ_AMPA |
| b (inh. time const) | 50 s⁻¹ | 1/τ_GABA-B |
| v₀ | 6 mV | Sigmoid threshold |
| e₀ | 2.5 s⁻¹ | Maximum firing rate |
| r | 0.56 mV⁻¹ | Sigmoid slope |

## Dynamical Regimes

The Jansen-Rit model exhibits different behaviors depending on parameters:

### 1. Low Activity (Fixed Point)
- Parameters: Low input (p ≈ 0-50 Hz)
- Output: Near-zero activity
- Interpretation: Resting state

### 2. Alpha Rhythm (Limit Cycle)
- Parameters: Moderate input (p ≈ 100-200 Hz)
- Output: 8-13 Hz oscillations
- Interpretation: Relaxed wakefulness

### 3. Spindles (Limit Cycle)
- Parameters: Specific input combinations
- Output: 12-14 Hz bursts
- Interpretation: Sleep stage 2

### 4. Epileptic Activity
- Parameters: High excitation/inhibition ratio
- Output: High-amplitude rhythmic activity
- Interpretation: Seizure-like dynamics

## Extensions

### Wendling Model (4-population)
Adds separate populations for fast (GABA-A) and slow (GABA-B) inhibition:
- Critical for modeling epileptic fast activity (14-60 Hz)
- Better captures seizure dynamics

### DCM Extension
- Bayesian parameter estimation
- Coupled column networks
- Forward models for EEG/MEG

### TVB Implementation
- Multiple coupled columns
- Empirical structural connectivity
- Delays from tractography

## Applications

| Application | Implementation | Key Finding |
|-------------|----------------|-------------|
| EEG simulation | Single column | Reproduces alpha, beta rhythms |
| Evoked potentials | Single column + input | VEP waveform generation |
| Epilepsy modeling | Extended (Wendling) | Seizure dynamics |
| Connectivity inference | DCM | Effective connectivity estimates |
| Whole-brain | TVB | Resting-state networks |

## Comparison with Other Models

| Feature | Jansen-Rit | Wilson-Cowan | Lopes da Silva |
|---------|------------|--------------|----------------|
| Populations | 3 | 2 | 2-3 |
| Focus | Cortical column | General population | Thalamocortical |
| Output | EEG/MEG | Firing rates | EEG |
| Inhibition | Slow (GABA-B) | Generic | Mixed |
| Default in TVB | Yes | Alternative | No |

## Limitations

1. **Fixed connectivity**: No plasticity
2. **Homogeneous populations**: Ignores cell-type diversity
3. **Simplified synapses**: No NMDA, conductance-based dynamics
4. **Single column**: Requires extension for whole-brain

## Related Concepts

- [[neural mass model]] – General framework
- [[Wilson-Cowan]] – Alternative two-population model
- [[eeg]] – Signal generation
- [[meg]] – Magnetic field modeling
- [[dynamic causal modeling]] – Parameter estimation
- [[epilepsy modeling]] – Pathological applications

## References

1. Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(4), 357–366. https://doi.org/10.1007/BF00199471

2. Lopes da Silva, F. H., Hoeks, A., Smits, H., & Zetterberg, L. H. (1974). Model of brain rhythmic activity. The alpha-rhythm of the thalamus. *Kybernetik*, 15(1), 27–37. https://doi.org/10.1007/BF00270757

3. Wendling, F., Bellanger, J. J., Bartolomei, F., & Chauvel, P. (2000). Relevance of nonlinear lumped-parameter models in the analysis of depth-EEG epileptic signals. *Biological Cybernetics*, 83(4), 367–378. https://doi.org/10.1007/s004220000160
