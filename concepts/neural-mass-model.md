---
created: 2026-04-20
sources:
- raw/papers/freeman-1975.md
- raw/papers/wilson-cowan-1972.md
- raw/papers/jansen-rit-1995.md
- raw/papers/dayan-abbott-2001.md
- raw/papers/gerstner-2014.md
- raw/papers/semanticscholar-e5e78e93bf31.md
- raw/papers/arxiv-2509.02799.md
- raw/papers/arxiv-2506.22951.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/wendling-2002.md
tags:
- neural-mass-models
- whole-brain-modeling
- brain-oscillations
title: Neural Mass Model
type: concept
updated: '2026-04-27'
---

# Neural Mass Model

Neural mass models (NMMs) are mathematical descriptions of the collective behavior of large populations of neurons, using mean-field approximations to reduce the high-dimensional dynamics of individual neurons to low-dimensional differential equations describing population activity.

## Definition

A neural mass model represents the average activity (firing rate, membrane potential, or synaptic current) of a homogeneous population of neurons as a function of time, typically through coupled differential equations. These models capture the mesoscopic scale—intermediate between single neurons and the whole brain.

## Historical Development

| Year | Milestone | Contribution |
|------|-----------|--------------|
| 1956 | Beurle | Early population activity equations |
| 1963 | Griffith | Statistical mechanics of neural populations |
| 1972 | Wilson-Cowan | Canonical firing-rate model (E-I populations) |
| 1974 | Lopes da Silva | First EEG-specific model (thalamic alpha) |
| 1975 | Freeman | K-set hierarchy for olfactory system |
| 1995 | Jansen-Rit | Three-population cortical column model |
| 2003 | David-Friston | Dynamic Causal Modeling (DCM) framework |

## Mathematical Framework

### Basic Structure

Most NMMs follow a common structure:

1. **Population activity**: Variables representing mean firing rate (E, I) or mean membrane potential
2. **Synaptic dynamics**: Post-synaptic responses modeled as linear filters (alpha functions, exponentials)
3. **Population coupling**: Connectivity between populations (recurrent, feedforward)
4. **Nonlinear activation**: Sigmoid or threshold functions converting input to output

### Example: Wilson-Cowan

The canonical two-population model:

```
τ_E dE/dt = -E + S_E(aE - bI + P)
τ_I dI/dt = -I + S_I(cE - dI + Q)
```

Where S_E, S_I are sigmoid response functions, P and Q are external inputs.

## Types of Neural Mass Models

### Classical Models

| Model | Populations | Primary Use | Key Feature |
|-------|-------------|-------------|-------------|
| [[Wilson-Cowan]] | 2 (E, I) | General dynamics | Firing-rate formulation |
| Lopes da Silva | 3 (E, E, I) | EEG/alpha rhythms | Thalamocortical loops |
| [[Jansen-Rit]] | 3 (P, E, I) | EEG/MEG/VEP | Cortical column structure |
| Wendling | 4 (P, E, I_slow, I_fast) | Epilepsy | Separate GABA-A/GABA-B |
| Zetterberg | 3+ | Sleep rhythms | Multiple cortical layers |

### TVB Model Library

| Model | Dim | Best For | Key Characteristics |
|-------|-----|----------|---------------------|
| [[Epileptor]] | 6D | Seizure dynamics | Composite fast/slow system |
| [[EpileptorCodim3]] | 2D | Bifurcation analysis | Universal unfolding |
| [[EpileptorRS]] | 6D+ | Resting-state | Stochastic interictal |
| [[Wong-Wang]] | 1D | fMRI/BOLD | NMDA-mediated, slow |
| [[Wong-Wang Exc-Inh]] | 2D | E-I balance | Separate populations |
| [[Larter-Breakspear]] | 3D | Complex dynamics | Ion channel conductances |
| [[Zerlaut]] | 2D+adapt | Adaptation | Spike-frequency adaptation |
| [[Stefanescu-Jirsa]] | 2D | Reduced seizures | Center manifold reduction |
| [[K-Ion Exchange]] | 3D | Metabolism | Potassium homeostasis |
| [[Infinite Theta]] | 2D | Exact mean-field | QIF neuron reduction |
| [[Hopfield]] | N | Memory | Discrete attractors |
| [[Oscillator]] | 2D | Universal | Generic phase plane |
| [[Linear]] | 1D | Testing | Baseline dynamics |

## Role in Whole-Brain Modeling

Neural mass models enable whole-brain simulation by:

1. **Dimension reduction**: Reducing millions of neurons to ~3-4 variables per brain region
2. **Computational tractability**: Enabling large-scale network simulations (TVB, DCM)
3. **Forward modeling**: Generating EEG/MEG/fMRI signals for comparison with data
4. **Parameter inference**: Estimating effective connectivity from neuroimaging

### TVB Implementation

The Virtual Brain uses NMMs as node dynamics coupled via empirical structural connectivity:
- Default: Jansen-Rit (3 populations)
- Alternative: Wilson-Cowan, Zetterberg, custom models
- Coupling: Delayed interactions via tractography-derived connectivity

## Dynamical Regimes

Neural mass models exhibit diverse dynamics depending on parameters:

- **Fixed point**: Low activity (resting state)
- **Limit cycle**: Rhythmic oscillations (alpha, beta, gamma)
- **Quasiperiodic**: Multi-frequency activity
- **Chaotic**: Irregular dynamics (interictal states)
- **Bistability**: Coexisting stable states (seizure onset)

## Clinical Applications

| Condition | Modeling Approach | Key Insight |
|-----------|-------------------|-------------|
| Epilepsy | Jansen-Rit/Wendling | Parameter changes → bifurcation to seizure |
| Schizophrenia | DCM | Altered effective connectivity |
| Sleep | Zetterberg | State transitions in thalamocortical loops |
| Stroke | TVB | Disrupted connectivity → functional deficits |

## Limitations

- **Homogeneity assumption**: Real populations are heterogeneous
- **Mean-field approximation**: Ignores correlations between neurons
- **Fixed connectivity**: Plasticity not typically included
- **Parameter identifiability**: Multiple parameter sets can produce similar dynamics

## Related Concepts

- [[Wilson-Cowan]] – Canonical firing-rate model
- [[Jansen-Rit]] – EEG/MEG-focused cortical column model
- [[Epileptor]] – Comprehensive seizure model
- [[Wong-Wang]] – fMRI/BOLD optimized model
- [[Larter-Breakspear]] – Ion channel-based model
- [[mean field theory]] – Mathematical foundation
- [[dynamic causal modeling]] – Bayesian inference with NMMs
- [[bifurcation analysis]] – Understanding regime transitions
- [[epilepsy modeling]] – Pathological applications
- [[whole brain]] – Large-scale network implementations

## References

1. Walter J. Freeman. *Mass Action in the Nervous System*.
2. Hugh R. Wilson, Jack D. Cowan. *Excitatory and inhibitory interactions in localized populations of model neurons*. Biophysical Journal. [DOI](https://doi.org/10.1016/S0006-3495(72)86068-5)
3. Benjamin H. Jansen, Vincent G. Rit. *Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns*. Biological Cybernetics. [DOI](https://doi.org/10.1007/BF00199471)
4. Peter Dayan, Larry F. Abbott. *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems*.
5. Wulfram Gerstner, Werner M. Kistler, Richard Naud, Liam Paninski. *Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition*.
6. Raul de Palma Aristides, Pau Clusella, R. Sanchez-Todo, G. Ruffini, Jordi García-Ojalvo. (2026). *Emergence of multifrequency activity in a laminar neural mass model*. PLoS Computational Biology. [DOI](https://doi.org/10.1371/journal.pcbi.1014022)
7. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven mean-field within whole-brain models*. [Link](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886)
8. Ramiro Plüss, Hernán Villota, Patricio Orio. (2025). *Hemispheric-Specific Coupling Improves Modeling of Functional Connectivity Using Wilson-Cowan Dynamics*. [Link](https://arxiv.org/abs/2506.22951)
9. Rosa Maria Delicado, Gemma Huguet, Pau Clusella. (2025). *Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation Neural Mass Models*. [Link](https://arxiv.org/abs/2512.03907)
10. Wendling F., Bartolomei F., Bellanger J.J., Chauvel P. *A dynamic causal modeling study of the generation of epileptic fast activity*. NeuroImage. [DOI](https://doi.org/10.1006/nimg.2002.1234)