---
created: 2026-04-20
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/gewaltig-diesmann-2007.md
- raw/papers/hines-carnevale-1997.md
- raw/papers/jordan-2018.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/ritter-2013.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/semanticscholar-899d3552b2ad.md
tags:
- comparison
- software-tvb
- software-nest
- software-neuron
- whole-brain-modeling
- spiking-neural-networks
title: TVB vs NEST vs NEURON
type: comparison
updated: '2026-05-06'
---

# TVB vs NEST vs NEURON

Comparison of major [[neural-simulation]] platforms for [[whole-brain]] modeling and spiking network simulations.

## What is Being Compared

Three major open-source platforms for [[computational-neuroscience]] simulation:

- **TVB** — Whole-[[brain-network]] modeling using [[neural-mass-models]]
- **[[nest]]** — Large-scale [[spiking-neural-networks|spiking neural network]] simulation
- **[[neuron]]** — Detailed multi-compartment neuron modeling

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

**TVB** uses neural mass models (e.g., Jansen-Rit, [[wilson-cowan]]) where each brain region is represented as a population of excitatory and inhibitory neurons described by mean-field differential equations. This coarse-graining enables whole-brain simulation with realistic [[structural-connectivity]] derived from [[diffusion-mri]] [[tractography]].

**NEST** simulates individual point neurons connected via synapses with realistic spike-timing-dependent [[plasticity]]. It is optimized for networks of integrate-and-fire or Hodgkin-Huxley type neurons where dendritic morphology is collapsed to a single compartment. This enables simulation of cortical microcircuits with biologically realistic cell counts.

**NEURON** solves cable equations for spatially extended neurons with distributed ion channels and synapses. It is essential when dendritic morphology, axonal propagation, or subcellular processes critically influence network behavior.

### Scale and Scope

| Platform | Typical Network Size | Biological Detail | Simulation Domain |
|----------|---------------------|-------------------|-------------------|
| TVB | 68–512 brain regions | Low (population mean) | Entire cortex + subcortical |
| NEST | 10^4–10^11 neurons | Moderate (spike timing) | Local circuits to whole brain |
| NEURON | 1–10^4 compartments | High (spatial, ionic) | Single neuron to small networks |

### Integration with Neuroimaging

**TVB** is designed specifically for [[neuroimaging]] integration:
- Uses DTI-derived structural [[connectivity]]
- Generates simulated EEG, MEG, and [[fmri]] [[bold-signal|BOLD]] signals
- Validates against [[resting-state]] [[functional-connectivity]]
- Personalization from individual MRI data

**NEST and NEURON** require post-processing for neuroimaging comparison:
- LFP proxies from weighted spike sums
- fMRI BOLD via the Balloon-Windkessel transform
- Less direct neuroimaging pipeline integration

## Synthesis

### When to Use Each Platform

**Choose TVB when:**
- Modeling whole-[[brain-dynamics]] at the scale of neuroimaging
- Simulating clinical populations or individual patients
- Generating predictions for EEG, MEG, or fMRI
- Integrating DTI structural connectivity
- Speed is essential for parameter exploration

**Choose NEST when:**
- Spiking dynamics and precise timing matter
- Simulating cortical microcircuits with realistic cell counts
- Studying [[synaptic-plasticity]] or learning
- Scaling to very large networks (10^6+ neurons)
- Running on HPC clusters or supercomputers

**Choose NEURON when:**
- Dendritic integration or axonal propagation is critical
- [[ion-channel]] distributions shape network behavior
- Validating against detailed electrophysiological recordings
- Teaching compartmental modeling concepts

### Complementary Use

These platforms are increasingly used together:
- **TVB + NEST**: [[mean-field-theory|Mean-field]] reduction of detailed spiking networks for whole-brain scaling (e.g., [[stefanescu-jirsa]] models in TVB)
- **NEST + NEURON**: Point neurons informed by detailed compartmental studies
- **NEURON → NEST → TVB**: Hierarchy of model abstraction for multiscale brain simulation

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Gewaltig & Diesmann (2007). *NEST (NEural Simulation Tool)*. Scholarpedia. [DOI](](https://doi.org/10.4249/scholarpedia.1430))
3. Hines & Carnevale (1997). *The NEURON simulation environment*. Neural Computation. [DOI](](https://doi.org/10.1162/neco.1997.9.6.1179))
4. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2018.00002))
5. Gianluca Gaglioti, Alessandra Cardinale, Cosimo Lupo, Thierry Nieus, Federico Marmoreo, Elena Focacci, Robin Gutzen, Michael Denker, Andrea Pigorini, Marcello Massimini, Simone Sarasso, Pier Stanislao Paolucci, Giulia De Bonis. *Emergent complexity and rhythms in evoked and spontaneous dynamics of human whole-brain models after tuning through analysis tools*. [Link](](https://arxiv.org/abs/2509.12873))
6. Ritter et al. (2013). *[[tvb|The Virtual Brain]] integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](](https://doi.org/10.1089/brain.2012.0120))
7. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](](https://arxiv.org/abs/2505.16861))
8. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](](https://doi.org/10.3389/fncom.2025.1731161))
9. Maxime Carriere, Fynn R. Dobler, H. Plesser, Agata Feledyn, Rosario Tomasello, Thomas Wennekers, F. Pulvermüller. (2026). *A brain-constrained neural model of cognition and language with NEST: transitioning from the Felix framework*. Cognitive Neurodynamics. [DOI](](https://doi.org/10.1007/s11571-026-10415-5))