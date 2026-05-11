# An Efficient FPGA Implementation of Spiking Neural Networks for N-MNIST Classification

**Source**: semantic-scholar
**ID**: 25651aeea1890e7a71722e9934e6cf55544ac350
**DOI**: 10.1109/ICEE67165.2025.11409707
**URL**: https://www.semanticscholar.org/paper/25651aeea1890e7a71722e9934e6cf55544ac350
**Date**: 2025-12-13
**Year**: 2025
**Authors**: Adhish Js, V. K., Suresh Balanethiram
**Venue**: International Conference on E-Business and E-Government
**Citations**: 0

## Abstract

The demand for low-power artificial intelligence on edge devices has spurred research into brain-inspired computing paradigms like Spiking Neural Networks (SNNs). While SNNs promise significant energy savings, their implementation on resource-constrained hardware like FPGAs presents a considerable challenge for edge applications. This paper details a complete hardware-software co-design workflow for deploying an SNN for handwritten digit classification. A hardware-aware, three-layer SNN is trained offline in Python using a surrogate gradient method, and the learned weights are deployed for inference on a Xilinx Artix-7 FPGA. The architecture features a resource-efficient, multiplier-less digital Leaky Integrate-and-Fire (LIF) neuron and a time-multiplexed dataflow to minimize hardware utilization. Implemented on a Basys 3 board, our design achieves 96.5% classification accuracy on the MNIST dataset, consuming only 4,808 Look-Up Tables (LUTs) and 2 DSP slices. These results demonstrate a highly competitive balance between accuracy and resource efficiency, validating the design’s suitability for low-power edge applications.
