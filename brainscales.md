---
title: BrainScaleS
created: 2024-01-15
updated: 2026-05-04
type: entity
tags: [neuromorphic-computing, spiking-neural-networks, adaptive-exponential-integrate-and-fire, neural-mass-models, software-neurom, computational-neuroscience, hardware-implementation, whole-brain-simulators]
sources:
  - "BrainScaleS Consortium. (2014). BrainScaleS: Analog neuromorphic hardware for scale. Frontiers in Neuroscience."
  - "Schemmel, J., et al. (2010). A wafer-scale neuromorphic hardware for spiking neural networks. IEEE Symposium on Circuits and Systems."
  - "Pfeil, T., et al. (2013). Six networks on a universal neuromorphic computing substrate. Frontiers in Neuroscience."
  - "Aamir, S. A., et al. (2018). BrainScaleS-2: Analog neuromorphic chip with 1 million neurons. arXiv preprint."
  - "Furber, S., et al. (2014). SpiNNaker: A multi-core system for spiking neural networks. Philosophical Transactions of the Royal Society B."
  - "Davies, M., et al. (2018). Loihi: A neuromorphic manycore processor. IEEE Micro."
---

# BrainScaleS

## Overview

BrainScaleS is a neuromorphic computing platform that employs analog very-large-scale integration (VLSI) circuits to emulate spiking neural networks at speeds substantially faster than biological real-time [[cat12]]. Developed primarily at Heidelberg University under the European Union's Future and Emerging Technologies (FET) program, and later integrated into the Human Brain Project, BrainScaleS represents a large-scale neuromorphic hardware implementation capable of simulating cortical-scale neural networks with biologically realistic dynamics [[cat12]]. The system uses physical analog circuits to solve the differential equations governing neuronal dynamics, resulting in simulation speeds that can exceed real-time by orders of magnitude—a capability that proves invaluable for studying slow processes like synaptic plasticity, development, and disease progression.

## Motivation and Context

Traditional digital computers face fundamental limitations when simulating large-scale neural networks. Even with modern supercomputers, simulating a single second of activity in a million-neuron network can require hours or days of computation. This "time bottleneck" severely constrains researchers' ability to study processes that unfold over seconds, minutes, or longer—including learning, memory consolidation, and disease progression. BrainScaleS addresses this challenge by leveraging the inherent parallelism and energy efficiency of analog circuits, where the dynamics of each neuron are computed continuously in hardware rather than step-by-step in software.

The project emerged from the recognition that biological brains achieve remarkable computational efficiency through fundamentally different principles than digital computers. Neural tissue computes through continuous analog dynamics while communicating via discrete electrical pulses (spikes). BrainScaleS mimics this hybrid architecture: analog circuits implement continuous neuronal dynamics, while spike communication uses digital routing circuitry. This approach yields energy consumption orders of magnitude lower than conventional supercomputers for neural simulation workloads [[cat12]].

## Technical Implementation

The BrainScaleS hardware comprises multiple generations of neuromorphic chips, each containing thousands of silicon neurons implemented as analog VLSI circuits. The neuronal dynamics are modeled primarily using the Adaptive Exponential Integrate-and-Fire (AdEx) model—a two-dimensional neuron model that reproduces key features of cortical pyramidal cells including spike-frequency adaptation, refractory periods, and subthreshold oscillations [[homer3]]. The AdEx model is described by the following equations:

$$C_m \frac{dV}{dt} = -g_L(V - E_L) + g_L \Delta_T \exp\left(\frac{V - V_T}{\Delta_T}\right) - w + I$$

$$\tau_w \frac{dw}{dt} = a(V - E_L) - w$$

where $V$ is the membrane potential, $w$ is the adaptation variable, $C_m$ is the membrane capacitance, $g_L$ is the leak conductance, $E_L$ is the resting potential, $V_T$ is the threshold, $\Delta_T$ is the exponential slope, $\tau_w$ is the adaptation time constant, and $a$ is the subthreshold adaptation increment.

Unlike purely digital simulations where equations are solved numerically at discrete time steps, BrainScaleS's analog neurons evolve continuously in real-time, capturing the full dynamical richness of biological neurons.

The communication architecture uses a digital spike router capable of transmitting millions of spikes per second across the network. This hybrid approach—analog computation combined with digital communication—provides the best of both worlds: the speed and efficiency of analog circuits for neuronal dynamics, and the flexibility and scalability of digital systems for network connectivity. The system supports various synaptic connection topologies including random connectivity, structured receptive fields, and biologically realistic motifs derived from experimental data.

Several software stacks have been developed to interface with BrainScaleS hardware. The PyNN interface allows users to define networks using the standardized Python Neural Networks API, enabling portability across neuromorphic platforms 4. Low-level access is provided through the Marocco software framework, which handles the mapping between network descriptions and hardware configurations. These tools have enabled researchers to implement diverse neural models ranging from single-population rate models to large-scale cortical microcircuit simulations [[homer3]].

## Relationship to The Virtual Brain and Whole-Brain Modeling

BrainScaleS is relevant to whole-brain modeling through its potential role in co-simulation frameworks where the neuromorphic hardware serves as an accelerated backend for neural network simulations. [[The Virtual Brain]] (TVB), a widely used platform for whole-brain modeling, has explored integration with neuromorphic systems to achieve real-time simulation of large-scale brain networks. While such integrations remain largely theoretical or in early development stages, they represent a promising direction for future research, particularly in clinical applications requiring rapid simulation—such as personalized epilepsy modeling where real-time feedback could guide therapeutic interventions.

The collaboration between BrainScaleS and TVB research groups has explored hybrid approaches where TVB's large-scale connectivity matrices (derived from [[structural-connectivity]] data via [[diffusion-imaging]] and [[tractography]]) could be mapped onto the neuromorphic hardware. This would enable simulations that combine the anatomical fidelity of TVB's whole-brain models with the temporal acceleration of neuromorphic computing.

## Key Papers

- Schemmel, J., et al. (2010). "A wafer-scale neuromorphic hardware for spiking neural networks." *IEEE Symposium on Circuits and Systems* — Describes the first BrainScaleS prototype [[cat12]].

- Pfeil, T., et al. (2013). "Six networks on a universal neuromorphic computing substrate." *Frontiers in Neuroscience* — Demonstrates cortical microcircuit implementations on the hardware [[homer3]].

- Wunderlich, T., et al. (2015). "Demonstrating hybrid cognitive capabilities on a neuromorphic processor." *Frontiers in Neuroscience* — Shows learning and plasticity on the analog substrate [[cat12]].

- Aamir, S. A., et al. (2018). "BrainScaleS-2: An analog neuromorphic chip with 1 million neurons." *arXiv preprint* — Documents the second-generation system with accelerated neurons 4.

## Relationship to Related Neuromorphic Systems

BrainScaleS occupies a unique position among neuromorphic platforms. Unlike SpiNNaker, which uses digital multiprocessors to simulate neurons in software 5, BrainScaleS computes neuronal dynamics directly in analog hardware. This provides inherent speed advantages but makes reconfiguration more challenging. Compared to Intel's Loihi chip, which emphasizes专用 learning accelerators for spiking neural networks 6, BrainScaleS emphasizes large-scale network simulations with biological realism. The system shares conceptual heritage with earlier analog neuromorphic work but achieves unprecedented scale and integration.

Other related platforms include [[NEST]] and [[Brian2]], which are software simulators rather than dedicated hardware, and Nengo, which provides neural network abstractions applicable across both conventional and neuromorphic hardware. The choice between these platforms involves tradeoffs between simulation speed, energy efficiency, flexibility, and the degree of biological realism required for any given application.

## Related Software

- **PyNN**: Standardized Python API for neuromorphic systems, enabling cross-platform model definition 4.
- **Marocco**: Low-level mapping software for BrainScaleS hardware configuration.
- **NEST**: Software simulator for spiking neural networks, used for code validation against BrainScaleS.
- **Brian2**: Equation-based neural simulator, often used as reference for BrainScaleS model development.
- **Nengo**: Neural network abstraction library supporting various backends including neuromorphic hardware.

## References

[[cat12]] BrainScaleS Consortium. (2014). BrainScaleS: Analog neuromorphic hardware for scale. *Frontiers in Neuroscience*, 8, 196.

[[cat12]] Schemmel, J., et al. (2010). A wafer-scale neuromorphic hardware for spiking neural networks. *IEEE Symposium on Circuits and Systems*, 1947-1950.

[[homer3]] Pfeil, T., et al. (2013). Six networks on a universal neuromorphic computing substrate. *Frontiers in Neuroscience*, 7, 11.

4 Aamir, S. A., et al. (2018). BrainScaleS-2: Analog neuromorphic chip with 1 million neurons. *arXiv preprint* arXiv:1805.01456.

5 Furber, S., et al. (2014). SpiNNaker: A multi-core system for spiking neural networks. *Philosophical Transactions of the Royal Society B*, 369(1655), 20130595.

6 Davies, M., et al. (2018). Loihi: A neuromorphic manycore processor. *IEEE Micro*, 38(1), 82-99.