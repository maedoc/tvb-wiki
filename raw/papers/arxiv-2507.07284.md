# A Robust, Open-Source Framework for Spiking Neural Networks on Low-End FPGAs

**Source**: semantic-scholar
**ID**: f9e58f94607cc3fae2769c52eb247e1f38affcf4
**DOI**: 10.48550/arXiv.2507.07284
**URL**: https://www.semanticscholar.org/paper/f9e58f94607cc3fae2769c52eb247e1f38affcf4
**Date**: 2025-07-09
**Year**: 2025
**Authors**: Andrew Fan, Simon D. Levy
**Venue**: arXiv.org
**Citations**: 1

## Abstract

As the demand for compute power in traditional neural networks has increased significantly, spiking neural networks (SNNs) have emerged as a potential solution to increasingly power-hungry neural networks. By operating on 0/1 spikes emitted by neurons instead of arithmetic multiply-and-accumulate operations, SNNs propagate information temporally and spatially, allowing for more efficient compute power. To this end, many architectures for accelerating and simulating SNNs have been developed, including Loihi, TrueNorth, and SpiNNaker. However, these chips are largely inaccessible to the wider community. Field programmable gate arrays (FPGAs) have been explored to serve as a middle ground between neuromorphic and non-neuromorphic hardware, but many proposed architectures require expensive high-end FPGAs or target a single SNN topology. This paper presents a framework consisting of a robust SNN acceleration architecture and a Pytorch-based SNN model compiler. Targeting any-to-any and/or fully connected SNNs, the FPGA architecture features a synaptic array that tiles across the SNN to propagate spikes. The architecture targets low-end FPGAs and requires very little (6358 LUT, 40.5 BRAM) resources. The framework, tested on a low-end Xilinx Artix-7 FPGA at 100 MHz, achieves competitive speed in recognizing MNIST digits (0.52 ms/img). Further experiments also show accurate simulation of hand coded any-to-any spiking neural networks on toy problems. All code and setup instructions are available at https://github.com/im-afan/snn-fpga}{\texttt{https://github.com/im-afan/snn-fpga.
