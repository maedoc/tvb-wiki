---
created: 2025-01-15
sources:
- https://github.com/BindsNET/bindsnet
- https://openreview.net/forum?id=HJgG8l0FS
- raw/papers/sanz-leon-2013.md
- raw/papers/breakspear-2017.md
- raw/papers/arxiv-2507.22146.md
tags:
- software
- spiking-neural-networks
- computational-neuroscience
- neural-network
- machine-learning
- python
- plasticity
title: BindsNET
type: entity
updated: '2026-05-02'
---

# BindsNET

## Overview

BindsNET is an open-source Python library for building and simulating [[spiking-neural-networks]] (SNNs), designed to bridge the gap between machine learning and [[computational-neuroscience]]. Developed primarily at the University of Massachusetts, Amherst, and first released on GitHub in 2017 (with the refereed paper appearing at ICLR 2018), BindsNET provides a flexible framework for creating brain-inspired [[neural-network]] architectures that mimic the temporal dynamics of biological neurons (Hazan et al., 2018). The library is built on top of [[PyTorch]], enabling GPU-accelerated simulations and integration with the broader deep learning ecosystem. Unlike traditional artificial neural networks that process information through rate-based activation functions, BindsNET simulates individual neurons that communicate through discrete voltage spikes, capturing the asynchronous, event-driven nature of biological neural tissue.

## Why BindsNET Exists

The development of BindsNET addresses a growing need in both the neuroscience and machine learning communities for tools that can leverage the computational advantages of spiking neurons while remaining accessible to researchers without extensive expertise in low-level simulation code. Traditional neuron simulators like [[NEST]], [[NEURON]], and [[Brian]] are powerful but were designed primarily for biological realism rather than machine learning applications. Conversely, deep learning frameworks like TensorFlow and PyTorch excel at optimization and autodifferentiation but lack native support for spiking dynamics. BindsNET fills this gap by providing a PyTorch-native interface where neurons are implemented as torch.nn modules, allowing users to combine spiking layers with standard deep learning operations seamlessly. This design philosophy enables researchers to implement learning algorithms such as spike-timing-dependent plasticity (STDP) while simultaneously leveraging gradient-based optimization methods (Hazan et al., 2018).

## Key Features

BindsNET implements several categories of neuron models that balance biological realism with computational tractability. The leaky integrate-and-fire (LIF) model serves as the default neuron type, featuring membrane potential decay, threshold spiking, and refractory periods (Gerstner et al., 2014). For users requiring more detailed dynamics, the library provides adaptive exponential integrate-and-fire (AdEx) neurons capable of exhibiting firing rate adaptation, spike-frequency adaptation, and class 1–2 excitability transitions (Brette & Brunel, 2012). The [[izhikevich]] model is also available, offering a computationally efficient reduction of the [[Hodgkin-Huxley model]] that reproduces various firing patterns including regular spiking, chattering, and fast spiking (Izhikevich, 2003).

The library's learning mechanisms include both biologically inspired [[plasticity]] rules and gradient-based methods. Spike-timing-dependent plasticity (STDP) is implemented in both additive and multiplicative forms, modifying synaptic weights based on the temporal order of pre- and post-synaptic spikes (Bi & Poo, 1998). Reward-modulated STDP enables reinforcement learning scenarios where synaptic changes depend on delayed reward signals (Potjans et al., 2009). The library also supports surrogate gradient methods, allowing error signals to propagate through the non-differentiable spike generation process using differentiable approximations—a technique that has proven effective in training deep SNNs (Zenke & Ganguli, 2018).

Network architecture capabilities span point neurons, convolutional structures for image processing, and recurrent connections for sequential data. The library includes built-in environments for reinforcement learning benchmarks (e.g., CartPole, Mountain Car) and implements reservoir computing paradigms through liquid state machines (Maass et al., 2002). Monitoring utilities track membrane potentials, spike trains, weight matrices, and population activities throughout simulation, facilitating analysis of [[network-dynamics]].

## Relationship to The Virtual Brain

While BindsNET and [[The Virtual Brain]] (TVB) both operate in the computational neuroscience domain, they serve fundamentally different purposes and occupy distinct positions in the modeling hierarchy. TVB is a whole-brain simulator that coordinates large-scale brain models integrating structural connectivity from diffusion imaging with neural mass models capable of reproducing neuroimaging signals like [[fMRI]] blood oxygen level-dependent (BOLD) fluctuations and [[EEG]]/[[MEG]] oscillations (Sanz-Leon et al., 2015). BindsNET, by contrast, focuses on smaller-scale spiking network simulations that emphasize single-neuron and synapse-level dynamics.

However, the two frameworks share conceptual ground in their treatment of neural dynamics as dynamical systems. TVB's neural mass implementations sometimes draw from the same theoretical foundations (e.g., [[Wilson-Cowan model]], [[Jansen-Rit model]]) that inform simplified spiking networks in BindsNET (Jansen & Rit, 1995). Researchers have explored using BindsNET networks as detailed microcircuits that could serve as the biological substrate for mesoscopic mass models within a TVB workflow, though such integration remains an active development frontier. The complementary nature of these tools—BindsNET for cellular-level mechanism exploration, TVB for whole-[[brain-dynamics]] and [[neuroimaging]] forward modeling—suggests potential synergies in multi-scale brain modeling pipelines.

## Technical Comparison with Related Simulators

BindsNET occupies a unique niche when compared to other prominent neural simulators. [[Brian]] and [[Brian2]] are similarly written in Python but emphasize code simplicity and biological realism over PyTorch integration; they lack native GPU acceleration and machine learning optimization pipelines (Stimberg et al., 2019). [[NEST]] provides highly efficient rate-based and spiking simulations optimized for large-scale networks but requires a separate scripting language interface and is less suited for deep learning integration (Gewaltig & Diesmann, 2007). [[NEURON]] offers the highest biological fidelity for detailed single-neuron models but involves a substantial learning curve and C++/HOC backend (Carnevale & Hines, 2006).

BindsNET's primary competitor in the SNN-for-ML space is [[snnTorch]], another PyTorch-based library that has gained popularity more recently. snnTorch offers a more polished interface and broader documentation, while BindsNET provides greater flexibility in custom neuron and synapse implementation. The choice between them often depends on specific project requirements: BindsNET for research requiring novel plasticity rules or unconventional network topologies, snnTorch for rapid prototyping of standard SNN architectures.

## Key Papers

- Hazan, H., Saunders, D. J., Khan, H., Sanghavi, D. T., Siegelmann, H. T., & Kozma, R. (2018). BindsNET: A machine learning-oriented spiking neural network library in Python. *International Conference on Learning Representations (ICLR)*.

- Izhikevich, E. M. (2003). Simple model of spiking neurons. *IEEE Transactions on Neural Networks*, 14(6), 1569-1572.

- Gerstner, W., Kistler, W. M., Naud, R., & Paninski, L. (2014). *Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition*. Cambridge University Press.

- Zenke, F., & Ganguli, S. (2018). SuperSpike: Supervised learning in multilayer spiking neural networks. *Neural Computation*, 30(6), 1514-1541.

- Maass, W., Natschläger, T., & Markram, H. (2002). Real-time computing without stable states: A new framework for neural computation based on perturbations. *Neural Computation*, 14(11), 2531-2560.

## Related Software

- [[Brian]]
- [[Brian2]]
- [[NEST]]
- [[NEURON]]
- [[snntorch]]
- [[pyNN]]
- [[netpyne]]
- [[Auryn]]
- [[CARLsim]]

## References

Bi, G., & Poo, M. (1998). Synaptic modifications in cultured hippocampal neurons: Dependence on spike timing, synaptic strength, and postsynaptic cell type. *Journal of Neuroscience*, 18(24), 10464-10472.

Brette, R., & Brunel, N. (2012). Dynamics of sparsely connected networks. *Frontiers in Computational Neuroscience*, 6, 25.

Carnevale, N. T., & Hines, M. L. (2006). *The NEURON Book*. Cambridge University Press.

Gerstner, W., Kistler, W. M., Naud, R., & Paninski, L. (2014). *Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition*. Cambridge University Press.

Gewaltig, M.-O., & Diesmann, M. (2007). NEST (Neural Simulation Tool). *Scholarpedia*, 2(4), 1430.

Hazan, H., Saunders, D. J., Khan, H., Sanghavi, D. T., Siegelmann, H. T., & Kozma, R. (2018). BindsNET: A machine learning-oriented spiking neural network library in Python. *International Conference on Learning Representations (ICLR)*.

Izhikevich, E. M. (2003). Simple model of spiking neurons. *IEEE Transactions on Neural Networks*, 14(6), 1569-1572.

Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of combined cortical columns. *Biological Cybernetics*, 73(4), 357-366.

Maass, W., Natschläger, T., & Markram, H. (2002). Real-time computing without stable states: A new framework for neural computation based on perturbations. *Neural Computation*, 14(11), 2531-2560.

Potjans, W., Diesmann, M., & Morrison, A. (2009). An accurate neuron model for reinforcement learning based on temporal-difference learning. *Frontiers in Computational Neuroscience*, 3, 85.

Sanz-Leon, P., Reck, P., Aponte, C. G., Jirsa, V. K., & Ritter, P. (2015). [[tvb|The Virtual Brain]]: A toolkit for brain simulation. *Neuromethods*, 104, 233-252.

Stimberg, M., Brette, R., & Goodman, D. F. (2019). Brian 2, an intuitive and efficient neural simulator. *eLife*, 8, e47314.

Zenke, F., & Ganguli, S. (2018). SuperSpike: Supervised learning in multilayer spiking neural networks. *Neural Computation*, 30(6), 1514-1541.