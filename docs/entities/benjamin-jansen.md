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
- raw/papers/arxiv-2510.22022.md
tags:
- people-researcher
- neural-mass-models
- eeg
title: Benjamin H. Jansen
type: entity
updated: '2026-04-27'
---

# Benjamin H. Jansen

Dutch biomedical engineer and neuroscientist. Co-developer of the Jansen-Rit model of cortical column dynamics for EEG/VEP generation. Applied [[nonlinear-dynamics]] and system identification to neural signal analysis.

## Key Contributions

- **Jansen-Rit model**: Three-population [[neural-mass-models|neural mass model]] for cortical columns (1995, with Vincent Rit)
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

## References

1. Benjamin H. Jansen, Vincent G. Rit. *Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns*. Biological Cybernetics. [DOI](https://doi.org/10.1007/BF00199471)
2. Vincent G. Rit, Benjamin H. Jansen. *A neural mass model for the generation of electroencephalograms*. Critical Reviews in Biomedical Engineering.
3. Huda Mahdi, Jan Sieber, [[krasimira-tsaneva-atanasova]]. *Alpha-Delta Transitions in Cortical Rhythms as grazing bifurcations*. [Link](https://arxiv.org/abs/2411.16449)
4. [[eugene-izhikevich|Eugene M. Izhikevich]]. *Dynamical Systems in Neuroscience: The Geometry of Excitability and Bursting*.
5. Gianluca Gaglioti, L. Porta, M. Colombo, Simone Russo, Thierry Nieus, G. Deco, M. Corbetta, S. Sarasso, M. V. Sanchez-Vives, M. Massimini. (2026). *Slow wave generation and propagation in a model of brain lesions*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2026.121817)
6. Pascal Helson, Etienne Tanré, Romain Veltz. *[[mean-field-theory|Mean-field]] analysis of a neural network with stochastic STDP*. [Link](https://arxiv.org/abs/2510.02545)
7. Lucia Zavaglia, Laura Astolfi, Federico Babiloni, Melani B.C. *Comparison of a mean-field model of electroencephalographic activity to individual brain networks*. IEEE Engineering in Medicine and Biology.
8. Cyprien Tamekue, ShiNung Ching. *Control of [[neural-field-theory|neural field]] equations with step-function inputs*. [Link](https://arxiv.org/abs/2510.22022)