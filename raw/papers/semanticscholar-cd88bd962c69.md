# PHENICS: A Scalable Neuromorphic FPGA Architecture for Million-Neuron Cortical Simulation With 4.6× Real-Time Acceleration

**Source**: semantic-scholar
**ID**: cd88bd962c69180ddc85c8b56bbe5107b6017a08
**DOI**: 10.1109/TCSI.2025.3648865
**URL**: https://www.semanticscholar.org/paper/cd88bd962c69180ddc85c8b56bbe5107b6017a08
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Fan Yang, Lufei Fan, Qi Jiang, Yuhan He, Hanwen Ou, Xun He, Lirong Zheng, Zhuo Zou
**Venue**: IEEE Transactions on Circuits and Systems Part 1: Regular Papers
**Citations**: 0

## Abstract

Traditional brain simulations using CPU/GPU architectures face critical limitations in both speed and scalability, particularly when modeling large-scale biological neural networks. Cortical models exhibit distinctive features, recurrent, random and sparse connectivity, and ultra-high synaptic density that fundamentally differ from the structured and dense architectures of deep neural networks (DNNs). As a result, conventional accelerators suffer from inefficiencies: communication overhead scales linearly with neuron count, and memory architectures exhibit poor utilization efficiency under complex connectivity, severely constraining scalability. To address these challenges, we present <bold>PHENICS</bold> (<italic>Pyramidal Hierarchical Event-driven Neuromorphic Infrastructure for Cortical Simulation</italic>), a scalable FPGA-based architecture tailored for large-scale spiking neural network simulations. At the communication level, PHENICS introduces a pyramidal multi-tier on-chip network combined with a <italic>Busy-Aware Threshold Adaptation (BATA)</italic> routing strategy and a lightweight router design to mitigate network congestion and improve spike transmission efficiency. At the storage level, we employ a multi-level addressing scheme adapted to sparse, irregular synaptic connectivity and leverage high-bandwidth memory (HBM) for efficient large-scale synaptic access. PHENICS is implemented on the Xilinx Alveo U50 system, successfully simulating a one-million-neuron Leaky Integrate-and-Fire (LIF) cortical model with 4 billion synapses, achieving a <inline-formula> <tex-math notation="LaTeX">$4.6\times $ </tex-math></inline-formula> real-time acceleration. It achieves this with only 25% of the memory bandwidth available on GPU platforms, yet delivers a <inline-formula> <tex-math notation="LaTeX">$5\times $ </tex-math></inline-formula> speedup compared to GPU-based simulators. Furthermore, our architecture reduces synaptic storage overhead by <inline-formula> <tex-math notation="LaTeX">$3\times $ </tex-math></inline-formula> through compressed encoding and HBM-backed sparse addressing. Moreover, it exhibits sub-linear communication time growth with increasing neuron counts. These advancements pave the way for real-time simulation of billion-neuron brain-scale models, opening new frontiers in neuroscience and neuromorphic computing.
