# NeuroCoreX: An Open-Source FPGA-Based Spiking Neural Network Emulator with On-Chip Learning

**Source**: semantic-scholar
**ID**: 8bb8745e5cfc291f11cb70d1b77372500cfc8487
**DOI**: 10.48550/arXiv.2506.14138
**URL**: https://www.semanticscholar.org/paper/8bb8745e5cfc291f11cb70d1b77372500cfc8487
**Date**: 2025-06-17
**Year**: 2025
**Authors**: Ashish Gautam, Prasanna Date, S. Kulkarni, Robert M. Patton, Tom Potok
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Spiking Neural Networks (SNNs) are computational models inspired by the structure and dynamics of biological neuronal networks. Their event-driven nature enables them to achieve high energy efficiency, particularly when deployed on neuromorphic hardware platforms. Unlike conventional Artificial Neural Networks (ANNs), which primarily rely on layered architectures, SNNs naturally support a wide range of connectivity patterns, from traditional layered structures to small-world graphs characterized by locally dense and globally sparse connections. In this work, we introduce NeuroCoreX, an FPGA-based emulator designed for the flexible co-design and testing of SNNs. NeuroCoreX supports all-to-all connectivity, providing the capability to implement diverse network topologies without architectural restrictions. It features a biologically motivated local learning mechanism based on Spike-Timing-Dependent Plasticity (STDP). The neuron model implemented within NeuroCoreX is the Leaky Integrate-and-Fire (LIF) model, with current-based synapses facilitating spike integration and transmission . A Universal Asynchronous Receiver-Transmitter (UART) interface is provided for programming and configuring the network parameters, including neuron, synapse, and learning rule settings. Users interact with the emulator through a simple Python-based interface, streamlining SNN deployment from model design to hardware execution. NeuroCoreX is released as an open-source framework, aiming to accelerate research and development in energy-efficient, biologically inspired computing.
