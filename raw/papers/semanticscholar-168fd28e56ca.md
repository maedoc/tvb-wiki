# Low-Power Resource-Efficient FPGA Implementation of Modified FitzHugh–Nagumo Neuron for Spiking Neural Networks

**Source**: semantic-scholar
**ID**: 168fd28e56ca4513b8e7bf1d7a23463139b561bf
**DOI**: 10.1109/TCSII.2025.3615935
**URL**: https://www.semanticscholar.org/paper/168fd28e56ca4513b8e7bf1d7a23463139b561bf
**Date**: 2025-11-01
**Year**: 2025
**Authors**: Reza Badiei, S. Timarchi, Alireza Zakaleh
**Venue**: IEEE Transactions on Circuits and Systems - II - Express Briefs
**Citations**: 0

## Abstract

The primary goals of neuromorphic engineering are to study, simulate, model, and implement neural behavior of the human brain. In this work, we propose a modified version of the original FitzHugh-Nagumo (FHN) neuron model in which the nonlinear term is replaced with a power-of-two-based approximation. The modification eliminates the need for multipliers, reducing hardware resource utilization while maintaining high fidelity in reproducing the dynamic behaviors of the original model. To validate the proposed model, we conduct dynamic behavior analysis, error evaluation, and network behavior simulation, demonstrating that it accurately reproduces the key characteristics of the FHN model with minimal error. An efficient digital hardware solution for implementing neurons optimized for large-scale Spiking Neural Networks (SNNs), leveraging resource-sharing techniques and pipelining strategies, is presented. The design is described using the VHSIC Hardware Description Language (VHDL), simulated and synthesized in Vivado, and implemented on a Xilinx Zynq Field-Programmable Gate Array (FPGA). Experimental results demonstrate that the proposed model achieves a normalized RMSE of 0.36, while utilizing only 0.38% of the available resources, including 0.27% of slice LUTs and 0.16% of registers. Additionally, it operates at a frequency of 255 MHz while consuming only 29 mW of power. Moreover, the FPGA implementation of our proposed model requires fewer resources and lower power consumption compared to previous works, while maintaining a comparable error rate.
