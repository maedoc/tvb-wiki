---
created: 2026-04-20
sources:
- raw/papers/wendling-2002.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/semanticscholar-15a4a438614f.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/deco-2013.md
tags:
- neural-mass-models
- whole-brain-modeling
- resting-state
- functional-connectivity
- neuroimaging-fmri
- dynamic-causal-modeling
- neural-mass-models-comparison
title: Wong-Wang Model
type: concept
updated: '2026-04-27'
---

# Wong-Wang Model

The **Wong-Wang model** is a reduced [[neural-mass-models|neural mass model]] that describes the dynamics of recurrent cortical circuits at the population level. Originally developed to explain perceptual decision-making in [[neural-mass-model|single-region cortical networks]], it was subsequently adapted for [[whole-brain]] modeling of [[resting-state]] [[functional-connectivity]] as measured by [[fmri]] BOLD signals. The model's popularity stems from its computational tractability—it captures essential dynamical properties of large spiking neural networks while requiring only a single state variable per brain region.

## Motivation and Context

The development of the Wong-Wang model in 2006 addressed a fundamental challenge in [[computational-neuroscience]]: how to build analytically tractable models that nonetheless capture the emergent dynamics of biologically realistic [[spiking-neural-networks]]. Previous approaches, such as the [[jansen-rit|Jansen-Rit]] model, used multiple populations (pyramidal cells, excitatory interneurons, inhibitory interneurons) to generate realistic EEG rhythms, but these models were computationally expensive and difficult to parameterize for whole-brain simulations.

Wong and Wang recognized that the essential dynamics of a recurrent excitatory-inhibitory network could be captured by a single equation describing the evolution of synaptic activity, provided the input-output function captured the network's nonlinear response properties. This reduction made it feasible to fit model parameters to empirical functional [[connectivity]] data and to run simulations across the entire [[connectome]]—a capability that proved crucial for the subsequent whole-brain modeling work by Deco, Corbetta, and colleagues.

## Mathematical Formulation

### Core Dynamical Equation

The model's primary equation describes the rate of change of the NMDA synaptic activity variable S:

```
dS/dt = -S/τ_s + (1 - S) · γ · H(x)
```

This equation embodies two key processes. The first term, `-S/τ_s`, represents exponential decay of synaptic activity with time constant τ_s approximately 100 ms, reflecting the temporal dynamics of NMDA receptor-mediated synaptic currents. The second term describes synaptic activation: the product of the input-output function `H(x)` and the factor `(1 - S)` implements a saturating nonlinearity that prevents activity from exceeding physical bounds, as synaptic resources become increasingly depleted at high firing rates.

### Input-Output Function

The function `H(x)` maps the total synaptic input `x` to a firing rate:

```
H(x) = (a·x - b) / (1 - exp(-d·(a·x - b))))
```

This is a rectified sigmoid function—essentially a smooth, continuous approximation of a threshold-[[linear]] response. The parameters `a` (input gain), `b` (input shift), and `d` (sigmoid steepness) control the nonlinearity's shape. When `x` is low, the function yields near-zero output; above the threshold defined by `b/a`, output grows approximately linearly before saturating at high inputs.

### Input to a Region

The total synaptic input `x` to each population combines external drive and recurrent coupling:

```
x = w · J_N · S + I_o
```

where `w` is a recurrent weight factor (typically 0.6), `J_N` is the coupling strength, and `I_o` represents background input simulating ongoing cortical activity. This formulation allows the model to generate self-sustaining activity in the absence of external stimuli—a key requirement for modeling the resting state.

## Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| a | 0.270 nC⁻¹ | Input gain — controls response sensitivity |
| b | 0.108 kHz | Input shift — sets activation threshold |
| d | 154 ms | Sigmoid steepness — controls nonlinearity |
| γ | 0.641 | Kinetic parameter — synaptic gain |
| τ_s | 100 ms | NMDA decay time constant |
| w | 0.6 | Recurrent weight — recurrent excitation strength |
| J_N | 0.2609 nA | Coupling strength — E→E connection efficacy |
| I_o | 0.33 nA | Background input — baseline drive |

These parameter values were originally fitted by Wong and Wang to reproduce the firing rate dynamics observed in their spiking network simulations. Subsequent whole-brain applications have often retuned parameters to match empirical resting-state functional connectivity patterns.

## Relationship to Other Models

The Wong-Wang model can be understood as a simplification of the [[jansen-rit|Jansen-Rit]] neural mass model, which uses three populations to generate EEG oscillations. By reducing the system to a single variable, the Wong-Wang model sacrifices the ability to produce realistic alpha/beta oscillations but gains analytical tractability and computational efficiency—tradeoffs that proved acceptable for fMRI modeling, where the relevant timescales are considerably slower.

An important extension is the [[wong-wang-exc-inh]] model, which reintroduces separate excitatory and inhibitory populations to capture E-I balance dynamics. This extension has proven valuable for modeling regimes where inhibition plays a critical role, such as during [[brain-stimulation]] or in computational models of [[epilepsy-modeling|epilepsy]].

## Applications in Whole-Brain Modeling

Following the seminal work of Deco and colleagues (2013), the Wong-Wang model became a workhorse for [[whole-brain]] simulations of resting-state [[functional-connectivity]]. In this application, each brain region (typically defined by a [[parcellation]] of the cortex) is modeled as a single Wong-Wang node, and the coupling between nodes is determined by [[structural-connectivity]] data from diffusion tensor imaging. The model successfully reproduces the characteristic temporal dynamics and spatial patterns of empirically observed resting-state networks, including the [[default-mode-network]].

## Biological Interpretation

The S variable in the Wong-Wang model can be interpreted as the average synaptic activity of excitatory pyramidal neurons in a cortical region. The model's parameters map onto biophysical quantities: τ_s reflects NMDA receptor kinetics, the input-output function captures the nonlinear summation of synaptic currents onto dendritic compartments, and the coupling strength J_N represents the efficacy of recurrent excitatory connections. These mappings make the model not merely a phenomenological fit but a theoretically grounded description of cortical dynamics at the mesoscopic scale.

## References

1. Wong, K. F., & Wang, X. J. (2006). A recurrent network mechanism of time integration in perceptual decisions. *Journal of Neuroscience*, 26(4), 1314–1328. https://doi.org/10.1523/JNEUROSCI.3733-05.2006

2. Deco, G., Ponce-Alvarez, A., Mantini, D., Romani, G. L., Hagmann, P., & Corbetta, M. (2013). Resting-state functional connectivity emerges from structurally and dynamically shaped slow linear fluctuations. *Journal of Neuroscience*, 32(27), 11239–11252. https://doi.org/10.1523/JNEUROSCI.1091-12.2013

## Related Concepts

- [[wong-wang-exc-inh]] — Extended excitatory-inhibitory version
- [[neural-mass-model]] — Theoretical framework for population models
- [[neural-mass-models-comparison]] — Comparison with other neural mass approaches
- [[resting-state]] — Network modeling at rest
- [[bold-signal]] — BOLD signal generation and modeling
- [[whole-brain]] — Whole-brain computational modeling
- [[functional-connectivity]] — Empirical functional connectivity
- [[structural-connectivity]] — Anatomical connectivity basis
- [[jansen-rit]] — Precursor neural mass model
- [[gustavo-deco]] — Key researcher in whole-brain adaptation