# Efficient Joint Communication and Computation Placement for Large-scale SNN Simulation on Supercomputers

**Source**: semantic-scholar
**ID**: e3fce558f99511b5f2f5d617c04e75965402ae5c
**DOI**: 10.1109/ICDCS63083.2025.00035
**URL**: https://www.semanticscholar.org/paper/e3fce558f99511b5f2f5d617c04e75965402ae5c
**Date**: 2025-07-21
**Year**: 2025
**Authors**: Yubing Bao, Zhihui Lu, Xin Du, Qiang Duan, Jirui Yang, Jin Zhao, Geyong Min, Yang Chen, Shijing Hu, Xin Wang
**Venue**: IEEE International Conference on Distributed Computing Systems
**Citations**: 0

## Abstract

Spiking Neural Network (SNN) simulation involves emulating the activation and firing of spiking neurons on hardware platforms. This is a highly time-sensitive task, requiring the simulation of billions of neurons and their intercommunication within a few milliseconds. Each neuron performs a complex, interdependent multi-stage communication and computation task. We consider the task placement of SNN on supercomputers to accelerate SNN simulation. Existing task placement methods for SNN simulations have two major limitations. First, they lack the capability to handle large-scale SNNs with billions of neurons. Second, they focus primarily on optimizing communication delay, while neglecting multi-stage computation delays in SNN simulations. In this paper, we formalize the SNN Joint Multi-stage Communication and Computation Placement (SJCCP) problem. We demonstrate that SJCCP can be solved using an approximation algorithm with an approximation ratio of $O\left( {{k^2}\sqrt {\log n\log k} } \right)$, where n is the number of voxels in the SNN and k is the number of GPUs. To further reduce the time complexity of solving SJCCP in practice, we propose a novel efficient framework, FastSJP, tailored for large-scale SNN placement. Then we apply the FastSJP framework to a human brain simulation that runs a large-scale SNN model derived from authentic biological data on a supercomputer equipped with 1024 GPUs. Experimental results verify that our framework notably reduces time overhead, ranging from 17.31% to 28.45%, compared to state-of-the-art methods. Leveraging the computational power of the supercomputer, FastSJP maximizes the problem size and processing performance, significantly advancing the development of brain-inspired intelligence.
