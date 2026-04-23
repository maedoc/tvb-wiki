---
created: 2026-04-20
sources:
- raw/papers/jansen-rit-1995.md
- raw/papers/rit-2013.md
- raw/papers/arxiv-2411.16449.md
- raw/papers/izhikevich-2007.md
- raw/papers/semanticscholar-cc2129666e15.md
- raw/papers/arxiv-2510.02545.md
- raw/papers/zavaglia-2006.md
tags:
- people-researcher
- neural-mass-models
- eeg
title: Benjamin H. Jansen
type: entity
updated: '2026-04-23'
---

# Benjamin H. Jansen

Dutch biomedical engineer and neuroscientist. Co-developer of the Jansen-Rit model of cortical column dynamics for EEG/VEP generation. Applied nonlinear dynamics and system identification to neural signal analysis.

## Key Contributions

- **Jansen-Rit model**: Three-population neural mass model for cortical columns (1995, with Vincent Rit)
- **Visual evoked potential modeling**: Generation of realistic VEP waveforms from population dynamics
- **Nonlinear system identification**: Methods for parameter estimation in biological systems
- **Biomedical signal processing**: Application of advanced signal analysis to clinical EEG

## Major Publications

- Jansen & Rit (1995) "Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns"
- Jansen (1991) "Quantitative analysis of electroencephalograms: is there chaos in the brain?"
- Rit & Jansen (2013) "A neural mass model for the generation of electroencephalograms"

## Model Architecture

The Jansen-Rit model consists of:
- **Population 1 (pyramidal)**: Main output cells projecting to both interneuron types
- **Population 2 (excitatory interneurons)**: Receive from pyramidal, project back
- **Population 3 (inhibitory interneurons)**: Slow inhibition via GABA-B

Post-synaptic responses are modeled as alpha functions (convolutions with exponential kernels), creating biologically realistic temporal dynamics.

## Related Concepts

- [[Jansen-Rit]]
- [[neural mass model]]
- [[eeg]]
- [[Vincent Rit]]