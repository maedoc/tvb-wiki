# HPC Acceleration of Recursive Least-Squares Sparse Spiking Neural Networks for Scalable Brain-Inspired Intelligence

**Source**: semantic-scholar
**ID**: b353031e924c5c06485c5c8f705fad92d9a77c2c
**DOI**: 10.1109/AIAHPC66801.2025.11290072
**URL**: https://www.semanticscholar.org/paper/b353031e924c5c06485c5c8f705fad92d9a77c2c
**Date**: 2025-09-19
**Year**: 2025
**Authors**: Liangsen Shao, Zhiwei Xu, Qiang Sun, Qi Yang
**Venue**: 2025 5th International Conference on Artificial Intelligence, Automation and High Performance Computing (AIAHPC)
**Citations**: 0

## Abstract

Spiking neural networks (SNNs) represent a biologically inspired computing paradigm capable of approximating complex temporal dynamics through sparse spiking activity. In this study, we investigate a sparse SNN trained with a recursive least-squares (RLS) learning rule to assess its ability to stabilize chaotic recurrent activity and reproduce target trajectories. Using layered analyses, we first evaluate the fidelity of spiking dynamics and decoder weight adaptation during learning, then benchmark runtime performance of conventional multilayer perceptrons (MLPs) and convolutional neural networks (CNNs) on baseline CPU and high-performance computing (HPC) accelerated GPU platforms. Finally, we extend benchmarking to RLS-based sparse SNNs, revealing that while ANNs consistently benefit from HPC accelerated parallelization, SNNs exhibit non-monotonic scaling. For RLS sparse SNN, while baseline execution outperforms HPC acceleration at small to intermediate network sizes, HPC acceleration dominates at larger scales. These findings highlight fundamental differences in computational scaling between matrix-driven ANNs and event-driven SNNs, and emphasize the need for optimized simulators and neuromorphic hardware to fully exploit brain-like intelligence.
