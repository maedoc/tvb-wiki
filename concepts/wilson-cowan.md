---
created: 2026-04-20
sources:
- raw/papers/wilson-cowan-1972.md
- raw/papers/arxiv-2510.08436.md
- raw/papers/arxiv-2512.22093.md
- raw/papers/wilson-cowan-1973.md
- raw/papers/arxiv-2411.16449.md
- raw/papers/arxiv-2510.22022.md
tags:
- neural-mass-models
- brain-oscillations
- network-dynamics
title: Wilson-Cowan Model
type: concept
updated: '2026-04-23'
---

# Wilson-Cowan Model

The Wilson-Cowan model is the canonical firing-rate model of coupled excitatory and inhibitory neural populations. Introduced in 1972, it provides the mathematical foundation for most subsequent neural mass modeling, including implementations in TVB and DCM.

## Overview

Developed by Hugh Wilson and Jack Cowan at the University of Chicago, the model describes the mean firing rates of excitatory and inhibitory populations through coupled nonlinear differential equations. The 1973 extension added spatial structure, founding neural field theory.

## Mathematical Formulation

### Original Model (1972)

The activity of excitatory (E) and inhibitory (I) populations:

```
τ_E dE/dt = -E + S_E(aE - bI + P)
τ_I dI/dt = -I + S_I(cE - dI + Q)
```

Where:
- E, I: Mean firing rates of excitatory and inhibitory populations
- τ_E, τ_I: Time constants
- a, b, c, d: Connection strengths (within/across populations)
- P, Q: External inputs
- S_E, S_I: Sigmoid response functions

### Sigmoid Function

```
S(x) = 1 / (1 + exp(-r(x - θ)))
```

Where r is slope and θ is threshold. This captures:
- Threshold behavior (no output below threshold)
- Saturation (maximum firing rate at high input)
- Smooth transition between states

### Spatial Extension (1973)

Neural field equations with spatial coupling:

```
∂E/∂t = -E + S_E(∫w_EE(r-r')E(r')dr' - ∫w_EI(r-r')I(r')dr' + P)
∂I/∂t = -I + S_I(∫w_IE(r-r')E(r')dr' - ∫w_II(r-r')I(r')dr' + Q)
```

Where w are connectivity kernels (typically Gaussian or Mexican-hat).

## Dynamical Properties

### Fixed Points

Setting dE/dt = dI/dt = 0 gives steady states. The nullclines can intersect in 1-3 points, allowing:
- Single stable state (monostability)
- Two stable states (bistability)
- Three fixed points (excitability)

### Oscillations

Oscillatory activity emerges when:
- Inhibitory time constant > excitatory time constant (τ_I > τ_E)
- Recurrent excitation is strong enough
- Feedback inhibition creates delayed negative feedback

Oscillation frequency depends on:
- τ_I (slower inhibition → lower frequency)
- Connection strengths (stronger coupling → higher amplitude)

### Phase Plane Analysis

The E-I phase plane reveals:
- **Nullclines**: Curves where dE/dt=0 or dI/dt=0
- **Fixed points**: Intersections of nullclines
- **Stability**: Determined by eigenvalues of Jacobian
- **Limit cycles**: Closed trajectories (oscillations)
- **Separatrices**: Boundaries between basins of attraction

## Biological Interpretation

| Model Component | Biological Correlate |
|-----------------|----------------------|
| E population | Pyramidal neurons, excitatory interneurons |
| I population | Inhibitory interneurons (PV, SST) |
| Sigmoid | Population activation function |
| Time constants | Membrane and synaptic time scales |
| Coupling weights | Synaptic strengths (AMPA, GABA) |
| External inputs | Sensory drive, neuromodulation |

## Applications

### Pattern Formation

The spatial model produces:
- **Standing waves**: Stationary patterns of activity
- **Traveling waves**: Activity propagating across tissue
- **Turing patterns**: Spontaneous spatial organization
- **Hallucinations**: Geometric patterns (with Ermentrout)

### Brain States

| State | Mechanism |
|-------|-----------|
| Resting | Low activity fixed point |
| Oscillatory | Stable limit cycle |
| Seizure | High-amplitude oscillation |
| Bistable | Two stable fixed points |

### Clinical Applications

- **Epilepsy**: Seizure onset as bifurcation
- **Hallucinations**: Pattern formation in visual cortex
- **Migraine**: Cortical spreading depression as traveling wave
- **Schizophrenia**: Altered E/I balance

## Relationship to Other Models

| Aspect | Wilson-Cowan | Jansen-Rit |
|--------|--------------|------------|
| Populations | 2 (E, I) | 3 (P, E, I) |
| Variables | Firing rates | Post-synaptic potentials |
| Output | Firing rates | EEG/MEG signals |
| Time course | Instantaneous | Synaptic filtering |
| Spatial | Yes (field theory) | No (single column) |

The Jansen-Rit model can be seen as a specific instantiation of Wilson-Cowan dynamics with:
- Three populations instead of two
- Post-synaptic filtering (alpha functions)
- Specific focus on EEG/MEG generation

## TVB Implementation

TVB includes Wilson-Cowan as an alternative to Jansen-Rit:

```python
from tvb.simulator.models import WilsonCowan
model = WilsonCowan()
```

Parameters:
- c_ee, c_ei, c_ie, c_ii: Connection strengths
- tau_e, tau_i: Time constants
- a_e, a_i: Sigmoid parameters

## Limitations

1. **Mean-field approximation**: Ignores correlations and fluctuations
2. **Fixed connectivity**: No plasticity or learning
3. **Simplified neurons**: No spike timing, adaptation
4. **Homogeneity**: Assumes identical neurons within populations

## Related Concepts

- [[neural mass model]] – General framework
- [[Jansen-Rit]] – EEG-focused extension
- [[mean field theory]] – Mathematical foundation
- [[bifurcation analysis]] – Understanding transitions

## References

1. Wilson, H. R., & Cowan, J. D. (1972). Excitatory and inhibitory interactions in localized populations of model neurons. *Biophysical Journal*, 12(1), 1–24. https://doi.org/10.1016/S0006-3495(72)86068-5

2. Wilson, H. R., & Cowan, J. D. (1973). A mathematical theory of the functional dynamics of cortical and thalamic nervous tissue. *Kybernetik*, 13(2), 55–80. https://doi.org/10.1007/BF00288786

3. Destexhe, A., & Sejnowski, T. J. (2009). The Wilson-Cowan model, 36 years later. *Biological Cybernetics*, 101(1), 1–2. https://doi.org/10.1007/s00422-009-0328-3