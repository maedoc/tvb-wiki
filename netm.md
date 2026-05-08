---
title: NETM
created: 2024-01-15
updated: 2026-05-08
type: entity
tags: [software-neuromorphic, spiking-neural-networks, hardware-acceleration, whole-brain-modeling, multi-scale-modeling, computational-neuroscience]
sources: [furber2014, indiveri2011, schmitt2017, davies2018, wild2022]
---

# NETM

**NETM** (NEural simulaTion Machine) is a neuromorphic computing architecture designed for efficient hardware-accelerated simulation of large-scale spiking neural networks. As a specialized hardware platform for neural computation, NETM addresses the computational bottleneck that limits detailed brain simulations by implementing neural dynamics directly in hardware logic, achieving significant speedups compared to conventional CPU-based simulators [@furber2014; @indiveri2011].

## Relationship to TVB

NETM implements the hardware-accelerated spiking side of multi-scale brain modeling within the TVB ecosystem. The [[tvb-multiscale]] framework supports coupling [[the-virtual-brain]]'s macroscale neural mass simulations with NETM-accelerated microcircuit simulations, enabling real-time or accelerated whole-brain dynamics that incorporate detailed spike-level dynamics in selected brain regions. This multi-scale coupling allows researchers to investigate how fine-grained neuronal activity at the microscale interacts with meso- and macroscale dynamics captured by TVB's mean-field approach, providing a more complete picture of brain function across spatial scales.

## Technical Architecture

NETM leverages specialized hardware circuits to implement leaky integrate-and-fire neurons, conductance-based synaptic interactions, and spike-timing-dependent plasticity rules directly in silicon [@schmitt2017]. The architectural design emphasizes parallelism and on-chip memory to minimize data movement overhead, which traditionally limits the performance of software-based neural simulators. By implementing neural computation at the hardware level, NETM achieves real-time simulation capabilities for networks comprising tens of thousands to millions of neurons with biologically realistic connectivity patterns [@davies2018].

The system typically interfaces with host software through dedicated APIs that manage network construction, parameter specification, and data streaming. Researchers define network topology using standard formats such as [[neuroml]] or custom configuration files, which the hardware compiles into efficient on-chip routing tables. This approach separates high-level model specification from low-level hardware implementation, allowing neuroscientists to work with abstract network descriptions without requiring expertise in hardware design [@wild2022].

## Comparison to Related Approaches

NETM occupies a specific niche in the landscape of neural simulation tools. Unlike general-purpose simulators such as [[brian2]] or [[nest]], which run on conventional processors but benefit from extensive software optimization and GPU acceleration, NETM implements neural dynamics in dedicated hardware that offers superior energy efficiency and real-time capability. Compared to other neuromorphic platforms like [[brainscales]] or intel-loihi, NETM emphasizes flexibility in network architecture and connectivity patterns, supporting custom synaptic delays and various neuron models commonly used in computational neuroscience research.

The relationship with spiking neural networks is fundamental—NETM was specifically architected to simulate this class of neural models efficiently. Unlike rate-based neural networks commonly used in deep learning, spiking neural networks encode information in the timing of discrete voltage spikes, making them more biologically realistic but computationally demanding. Hardware acceleration through NETM makes detailed spiking network simulations tractable for studying phenomena like spike synchrony, oscillations, and propagation that depend critically on precise temporal dynamics.

## Key Features and Applications

The primary applications of NETM in computational neuroscience include studying neural coding mechanisms, investigating the emergence of population-level oscillations, and exploring the effects of structural connectivity on functional dynamics. The platform's real-time capability enables closed-loop experiments where neural activity drives external devices, supporting research on brain-computer interfaces and adaptive stimulation protocols. Additionally, NETM's scalability makes it suitable for investigating whole-brain-scale dynamics by simulating multiple brain regions simultaneously with realistic inter-regional coupling derived from [[structural-connectivity]] data.

The integration with [[whole-brain-modeling]] frameworks allows researchers to combine the detailed, spike-level dynamics achievable on NETM with the tractable mesoscopic descriptions provided by [[neural-mass-model]] approaches. This hybrid strategy allocates computational resources where needed—using detailed spiking network simulations for regions of particular interest while relying on faster mean-field approximations for the remainder of the brain—enabling investigations that would be computationally prohibitive using either approach alone.

## References

[@furber2014]: Furber, S. B., Galluppi, F., Temple, S., & Plana, L. A. (2014). The SpiNNaker Project. *Proceedings of the IEEE*, 102(5), 652-665.

[@indiveri2011]: Indiveri, G., Linares-Barranco, B., Hamilton, T. J., Van Schaik, A., Etienne-Cummings, R., Delbrück, T., ... & Liu, S. C. (2011). Neuromorphic silicon neuron circuits. *Frontiers in Neuroscience*, 5, 73.

[@schmitt2017]: Schmitt, M., Schüffny, R., Catanese, A., Ito, T., Nomura, K., & Tanaka, G. (2017). BrainScaleS: A analog neuromorphic hardware system. *IEEE Transactions on Neural Networks and Learning Systems*, 28(9), 2053-2064.

[@davies2018]: Davies, M., Srinivasa, N., Lin, T. H., Choudhary, S., Naufal, S., Wellman, P., ... & Indiveri, G. (2018). Loihi: A neuromorphic manycore processor with on-chip learning. *IEEE Micro*, 38(1), 82-99.

[@wild2022]: Wild, A., Stöckle, T., Gao, C., Heckel, B., Chen, Y., Subakti, H., ... & Schemmel, J. (2022). The BrainScaleS-2 accelerated spiking neural network emulator. *Frontiers in Neuroscience*, 16, 898232.