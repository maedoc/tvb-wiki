---
title: TVB vs NEST vs NEURON
created: 2026-04-20
updated: 2026-04-20
type: comparison
tags: [comparison, software-tvb, software-nest, software-neuron, whole-brain-modeling, spiking-neural-networks]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/gewaltig-diesmann-2007.md, raw/papers/hines-carnevale-1997.md, raw/papers/jordan-2018.md]
---

# TVB vs NEST vs NEURON

Comparison of major neural simulation platforms for whole-brain modeling and spiking network simulations.

## What is Being Compared

Three major open-source platforms for computational neuroscience simulation:

- **TVB** — Whole-brain network modeling using neural mass models
- **NEST** — Large-scale spiking neural network simulation
- **NEURON** — Detailed multi-compartment neuron modeling

Each platform occupies a distinct niche in the modeling hierarchy, from population-level (TVB) to single-neuron detail (NEURON) to large networks (NEST).

## Dimensions of Comparison

| Dimension | TVB | NEST | NEURON |
|-----------|-----|------|--------|
| **Model Level** | Neural mass (population) | Point neuron (spiking) | Multi-compartment (biophysical) |
| **Scale** | Whole brain (~100 nodes) | 10^3–10^9 neurons | Single neuron to local networks |
| **Dynamics** | Firing rates/field potentials | Discrete spikes | Voltage-gated ion channels |
| **Speed** | Fast (minutes per simulation) | Moderate (scales with size) | Slower (detailed ODEs) |
| **Use Case** | Clinical brain simulation, fMRI/EEG prediction | Large cortical circuits, plasticity | Detailed dendritic computation |
| **Connectivity** | Structural (DTI-based) | Synaptic, user-defined | Synaptic, morphologically placed |
| **Forward Models** | EEG, MEG, fMRI BOLD | Spike trains, LFP approximations | LFP, membrane voltages |
| **Parallelization** | OpenMP | MPI + OpenMP (exascale-ready) | MPI for networks |
| **Interface** | Python, GUI | PyNEST (Python), SLI | hoc, Python, RxD |

## Detailed Comparison

### Computational Approach

**TVB** uses neural mass models (e.g., Jansen-Rit, Wilson-Cowan) where each brain region is represented as a population of excitatory and inhibitory neurons described by mean-field differential equations. This coarse-graining enables whole-brain simulation with realistic structural connectivity derived from diffusion MRI tractography.

**NEST** simulates individual point neurons connected via synapses with realistic spike-timing-dependent plasticity. It is optimized for networks of integrate-and-fire or Hodgkin-Huxley type neurons where dendritic morphology is collapsed to a single compartment. This enables simulation of cortical microcircuits with biologically realistic cell counts.

**NEURON** solves cable equations for spatially extended neurons with distributed ion channels and synapses. It is essential when dendritic morphology, axonal propagation, or subcellular processes critically influence network behavior.

### Scale and Scope

| Platform | Typical Network Size | Biological Detail | Simulation Domain |
|----------|---------------------|-------------------|-------------------|
| TVB | 68–512 brain regions | Low (population mean) | Entire cortex + subcortical |
| NEST | 10^4–10^11 neurons | Moderate (spike timing) | Local circuits to whole brain |
| NEURON | 1–10^4 compartments | High (spatial, ionic) | Single neuron to small networks |

### Integration with Neuroimaging

**TVB** is designed specifically for neuroimaging integration:
- Uses DTI-derived structural connectivity
- Generates simulated EEG, MEG, and fMRI BOLD signals
- Validates against resting-state functional connectivity
- Personalization from individual MRI data

**NEST and NEURON** require post-processing for neuroimaging comparison:
- LFP proxies from weighted spike sums
- fMRI BOLD via the Balloon-Windkessel transform
- Less direct neuroimaging pipeline integration

## Synthesis

### When to Use Each Platform

**Choose TVB when:**
- Modeling whole-brain dynamics at the scale of neuroimaging
- Simulating clinical populations or individual patients
- Generating predictions for EEG, MEG, or fMRI
- Integrating DTI structural connectivity
- Speed is essential for parameter exploration

**Choose NEST when:**
- Spiking dynamics and precise timing matter
- Simulating cortical microcircuits with realistic cell counts
- Studying synaptic plasticity or learning
- Scaling to very large networks (10^6+ neurons)
- Running on HPC clusters or supercomputers

**Choose NEURON when:**
- Dendritic integration or axonal propagation is critical
- Ion channel distributions shape network behavior
- Validating against detailed electrophysiological recordings
- Teaching compartmental modeling concepts

### Complementary Use

These platforms are increasingly used together:
- **TVB + NEST**: Mean-field reduction of detailed spiking networks for whole-brain scaling (e.g., Stefanescu-Jirsa models in TVB)
- **NEST + NEURON**: Point neurons informed by detailed compartmental studies
- **NEURON → NEST → TVB**: Hierarchy of model abstraction for multiscale brain simulation

## References

- Sanz Leon et al. (2013) — TVB introduction sanz-leon-2013
- Gewaltig & Diesmann (2007) — NEST introduction gewaltig-diesmann-2007
- Hines & Carnevale (1997) — NEURON environment hines-carnevale-1997
- Jordan et al. (2018) — NEST exascale scaling jordan-2018
