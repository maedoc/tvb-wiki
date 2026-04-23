---
created: 2026-04-20
sources:
- raw/papers/jansen-rit-1995.md
- raw/papers/wilson-cowan-1972.md
- raw/papers/wilson-cowan-1973.md
- raw/papers/rit-2013.md
- raw/papers/destexhe-sejnowski-2009.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/arxiv-2504.17491.md
- raw/papers/arxiv-2510.22022.md
tags:
- comparison
- neural-mass-models
- brain-oscillations
- eeg
- whole-brain-modeling
title: 'Neural Mass Models: Jansen-Rit vs Wilson-Cowan'
type: comparison
updated: '2026-04-23'
---

# Neural Mass Models: Jansen-Rit vs Wilson-Cowan

Comparison of the two most influential neural mass models: the Wilson-Cowan model (1972) as the canonical firing-rate model, and the Jansen-Rit model (1995) as the standard for EEG/MEG simulation.

## What is Being Compared

Both models describe collective neural population dynamics but differ in:
- **Biological focus**: General population dynamics vs. cortical column EEG generation
- **Mathematical formulation**: Firing rates vs. post-synaptic potentials
- **Output**: Generic activity vs. specific EEG/MEG signals
- **Implementation**: TVB supports both but defaults to Jansen-Rit

## Model Origins

| Aspect | Wilson-Cowan | Jansen-Rit |
|--------|--------------|------------|
| **Year** | 1972 (spatial: 1973) | 1995 |
| **Authors** | Hugh Wilson, Jack Cowan | Benjamin Jansen, Vincent Rit |
| **Institution** | University of Chicago | University of Twente |
| **Motivation** | General neural population theory | EEG/VEP generation |
| **Predecessor** | Beurle (1956), Griffith (1963) | Lopes da Silva (1974) |

## Architecture Comparison

### Population Structure

| Feature | Wilson-Cowan | Jansen-Rit |
|---------|--------------|------------|
| **Populations** | 2 (E, I) | 3 (P, E, I) |
| **E population** | Generic excitatory | Pyramidal cells |
| **I population** | Generic inhibitory | Interneurons |
| **Additional** | - | Excitatory interneurons |
| **Hierarchy** | Single level | Cortical column structure |

### Connectivity Patterns

**Wilson-Cowan**:
```
E ↔ E (recurrent excitation)
E → I (feedforward excitation)
I → E (feedback inhibition)
I ↔ I (recurrent inhibition)
```

**Jansen-Rit**:
```
P → E → P (excitatory loop)
P → I → P (inhibitory loop)
P (output to other columns)
```

## Mathematical Formulation

### Variables

| Model | State Variables | Units |
|-------|-----------------|-------|
| Wilson-Cowan | E(t), I(t) | Firing rates (Hz) |
| Jansen-Rit | y₁(t), y₂(t), y₃(t) | Post-synaptic potentials (mV) |

### Equations

**Wilson-Cowan**:
```
τ_E dE/dt = -E + S_E(aE - bI + P)
τ_I dI/dt = -I + S_I(cE - dI + Q)
```

**Jansen-Rit**:
```
y₁ = ∫ h_e(t-s) · S(y₂ - y₃) ds  (pyramidal PSP)
y₂ = ∫ h_e(t-s) · S(C₁y₁) ds     (excitatory PSP)
y₃ = ∫ h_i(t-s) · S(C₃y₁) ds     (inhibitory PSP)
```

Where h_e, h_i are alpha-function post-synaptic responses.

### Key Differences

| Aspect | Wilson-Cowan | Jansen-Rit |
|--------|--------------|------------|
| **Nonlinearity** | Sigmoid on input | Sigmoid on potential |
| **Dynamics** | Instantaneous activation | Synaptic filtering |
| **Time scales** | Single τ per population | Multiple (synaptic) |
| **Output** | Firing rate | Membrane potential |

## Dynamical Properties

### Oscillatory Regimes

| Model | Frequency Range | Mechanism |
|-------|-----------------|-----------|
| Wilson-Cowan | 10-100 Hz | E-I feedback loop |
| Jansen-Rit | 8-13 Hz (alpha) | P-E-I interactions |
| | 14-30 Hz (beta) | Higher input |

### Bifurcation Structure

Both models exhibit:
- **Saddle-node**: Threshold behavior
- **Hopf**: Oscillation onset
- **Global**: Complex dynamics

**Differences**:
- Wilson-Cowan: Simpler 2D phase plane
- Jansen-Rit: Higher-dimensional, richer dynamics

## Applications

### Wilson-Cowan Applications

| Domain | Use Case |
|--------|----------|
| General | Theoretical neuroscience |
| Visual cortex | Hallucination patterns |
| Development | Pattern formation |
| Disease | Spreading depression |
| TVB | Alternative node model |

### Jansen-Rit Applications

| Domain | Use Case |
|--------|----------|
| EEG/MEG | Signal generation |
| DCM | Connectivity inference |
| Epilepsy | Seizure modeling |
| VEP | Evoked responses |
| TVB | Default node model |

## TVB Implementation

### Code Examples

**Wilson-Cowan**:
```python
from tvb.simulator.models import WilsonCowan
model = WilsonCowan(
    c_ee=numpy.array([12.0]),
    c_ei=numpy.array([4.0]),
    c_ie=numpy.array([13.0]),
    c_ii=numpy.array([11.0])
)
```

**Jansen-Rit**:
```python
from tvb.simulator.models import JansenRit
model = JansenRit(
    A=numpy.array([3.25]),  # excitatory amplitude
    B=numpy.array([22.0]),  # inhibitory amplitude
    a=numpy.array([100.0]), # excitatory rate
    b=numpy.array([50.0])   # inhibitory rate
)
```

### Default Usage

- **Jansen-Rit**: Default for EEG/MEG simulations
- **Wilson-Cowan**: Available alternative, simpler dynamics
- **Zetterberg**: Available for sleep modeling

## Strengths and Weaknesses

### Wilson-Cowan

**Strengths**:
- Mathematical simplicity
- Analytical tractability
- Rich bifurcation structure
- Historical foundation
- Spatial extension (neural fields)

**Weaknesses**:
- No explicit EEG output
- Simplified synaptic dynamics
- Limited for clinical applications

### Jansen-Rit

**Strengths**:
- Direct EEG/MEG output
- Biologically realistic PSPs
- Validated against clinical data
- DCM integration
- TVB default

**Weaknesses**:
- More complex (higher dimensional)
- More parameters
- No spatial extension (single column)

## When to Use Which

| Scenario | Recommended Model |
|----------|-------------------|
| EEG/MEG simulation | Jansen-Rit |
| DCM analysis | Jansen-Rit |
| Theoretical study | Wilson-Cowan |
| Pattern formation | Wilson-Cowan (spatial) |
| Seizure modeling | Jansen-Rit (or Wendling extension) |
| Educational | Wilson-Cowan (simpler) |
| Clinical application | Jansen-Rit |
| Large-scale efficiency | Wilson-Cowan (simpler) |

## Synthesis

Both models are essential in computational neuroscience:

- **Wilson-Cowan** provides the theoretical foundation and is preferred for mathematical analysis and spatial pattern formation

- **Jansen-Rit** is the practical choice for neuroimaging applications and clinical modeling, particularly in TVB and DCM

The choice depends on the specific question: use Wilson-Cowan for theoretical insight and Jansen-Rit for clinical applications and EEG/MEG modeling.

## Related Concepts

- [[neural mass model]] – General framework
- [[Hugh Wilson]] – Co-developer of Wilson-Cowan
- [[Jack Cowan]] – Co-developer of Wilson-Cowan
- [[Benjamin Jansen]] – Co-developer of Jansen-Rit
- [[Vincent Rit]] – Co-developer of Jansen-Rit
- [[eeg]] – Signal generation (Jansen-Rit strength)
- [[dynamic causal modeling]] – Uses Jansen-Rit
- [[TVB]] – Supports both models