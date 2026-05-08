---
title: Jansen Rit Model
created: 2026-04-27
sources:
- raw/papers/arxiv-2411.16449.md
- raw/papers/jansen-rit-1995.md
- raw/papers/arxiv-2503.05564.md
- raw/papers/semanticscholar-cc2129666e15.md
tags:
- jansen-rit-model
- neural-mass-models
- eeg
- computational-neuroscience
- whole-brain-modeling
title: Jansen Rit Model
type: concept
updated: 2026-05-08
---

## Overview

The **Jansen-Rit model** is a neural mass model of a cortical column that generates realistic electroencephalogram (EEG) signals and visual evoked potentials (VEPs). Originally published by Benjamin H. Jansen and Vincent G. Rit in 1995, this model has become a foundational framework in [[computational-neuroscience]] and is widely used in [[whole-brain]] modeling simulations, particularly within the Virtual Brain (TVB) platform [@jansen1995electroenc]. The model captures the collective dynamics of neuronal populations using coupled differential equations, making it computationally efficient while retaining key biophysical properties of cortical circuitry.

## Model Architecture

The Jansen-Rit model represents a single cortical column as three coupled neuronal populations [@jansen1995electroenc]:

1. **Pyramidal cells (P)**: The primary output population that projects to other cortical columns and subcortical structures. This population receives excitatory input from both interneuron populations and provides the model's primary output signal.

2. **Excitatory interneurons (E)**: Fast-spiking interneurons that provide reciprocal excitation to pyramidal cells. These cells use glutamate as their neurotransmitter and mediate local excitatory feedback.

3. **Inhibitory interneurons (I)**: Slow-spiking interneurons that provide feedback inhibition to pyramidal cells. These cells use GABA as their neurotransmitter and are critical for regulating the oscillation frequency and preventing runaway excitation.

The populations are coupled through synaptic connectivity weights and interact via post-synaptic impulse response functions—typically modeled as alpha-shaped kernels that capture the rise and decay of synaptic potentials. The model's dynamics are governed by nonlinear firing-rate functions that relate average membrane potentials to firing rates, typically using a sigmoidal activation function with parameters controlling threshold and gain.

## Dynamical Regimes

The Jansen-Rit model exhibits rich oscillatory behavior that can transition between distinct dynamical regimes by varying its parameters—particularly the coupling strengths between populations and the characteristic time constants of synaptic responses.

### Alpha Oscillations (8–12 Hz)

The model naturally generates alpha-frequency oscillations (8–12 Hz) under physiologically plausible parameter regimes, matching the dominant rhythm observed in resting-state human EEG. These oscillations arise from the interplay between excitatory and inhibitory feedback loops, particularly the delayed inhibition provided by the inhibitory interneuron population [@jansen1995electroenc].

### Delta Oscillations (<4 Hz)

Recent theoretical work has revealed that the Jansen-Rit model can also produce delta-frequency oscillations (< 4 Hz) through a **grazing bifurcation** mechanism [@arxiv-2411.16449]. In this regime, the minimum of the pyramidal-cell output equals the threshold for switching off the excitatory interneuron population, leading to a collapse in excitatory feedback. Delta oscillations exhibit a more complex relaxation-type time profile compared to alpha oscillations and are associated with deep sleep or pathological states.

### Transitions Between Regimes

The transition between alpha and delta oscillations represents a discontinuity-induced bifurcation, highlighting the model's capability to capture state transitions that are physiologically relevant—such as transitions between wakefulness and sleep, or between healthy and pathological brain states.

## Mathematical Framework

The classic Jansen-Rit model consists of the following equations for each population:

$$v_i(t) = \int_0^t h_i(t-\tau) \phi_j(\tau) d\tau$$

where $v_i$ represents the average membrane potential of population $i$, $h_i$ is the post-synaptic response kernel (typically an alpha function), and $\phi_j$ is the firing rate of the presynaptic population $j$. The output of each population is passed through a sigmoidal activation function:

$$\phi(v) = \frac{A}{1 + e^{-a(v - v_0)}}$$

where $A$ determines the maximum firing rate, $a$ controls the slope (gain), and $v_0$ is the firing threshold.

The full system comprises six coupled first-order differential equations (two state variables per population), making it computationally tractable for large-scale simulations involving hundreds or thousands of coupled cortical columns.

## Applications

The Jansen-Rit model serves several key applications in computational neuroscience:

- **EEG/MEG simulation**: Generating spontaneous brain activity and event-related potentials for comparison with empirical neuroimaging data [@jansen1995electroenc].
- **Whole-brain modeling**: Providing the local dynamics for coupling through structural connectomes in large-scale brain network simulations.
- **Neural encoding studies**: Investigating how simple neural circuits can represent information through phase-shifted oscillations [@arxiv-2503.05564].
- **Sleep dynamics**: Modeling slow-wave oscillations and transitions between wake-like and sleep-like states [@semantic-cc2129666e15].
- **Clinical applications**: Serving as a building block for patient-specific models in epilepsy modeling and other neurological disorders.

## Relationship to Other Neural Mass Models

The Jansen-Rit model extends earlier work by Lopes da Silva and colleagues, who developed thalamic models of EEG generation, by focusing specifically on cortical column dynamics. Unlike more recent neural mass formulations—such as the reduced Wong-Wang model or the Epileptor—the Jansen-Rit model retains explicit separability into three distinct populations, making it particularly amenable to bifurcation analysis and parameter interpretation.

## Related Concepts

* [[oscillator]]
* [[opencortex]]
* [[whole-brain]]
* [[computational-neuroscience]]
* [[osi]]
