# A Low-Latency Hybrid Cryptographic Framework for Secure Spiking Neural Network Inference

**Source**: semantic-scholar
**ID**: 5c0c91c6a902e99027df4df9549c1be0a5e514ae
**DOI**: 10.1109/FTCS68006.2025.11405774
**URL**: https://www.semanticscholar.org/paper/5c0c91c6a902e99027df4df9549c1be0a5e514ae
**Date**: 2025-11-21
**Year**: 2025
**Authors**: Xiaoliang Zhang, Jundong Feng, Junchao Wang
**Venue**: International Symposium on Fault-Tolerant Computing
**Citations**: 0

## Abstract

The growing adoption of Machine Learning as a Service (MLaaS) has raised critical privacy concerns regarding both client data and proprietary model parameters during cloud-based inference. While Spiking Neural Networks (SNNs) offer energy-efficient, event-driven computation, their privacypreserving inference remains challenging. Existing pure Fully Homomorphic Encryption (FHE) approaches suffer from prohibitive latency due to expensive polynomial approximations for nonlinear dynamics, while conventional hybrid frameworks designed for Convolutional Neural Networks (CNNs) fail to exploit the temporal sparsity inherent in SNNs. To address these limitations, this paper proposes a novel hybrid-cryptographic framework that strategically combines a sparsity-aware homomorphic encryption kernel for efficient linear layer computation with a low-overhead garbled circuit protocol for exact Leaky Integrate-and-Fire (LIF) activation evaluations. The framework introduces an efficient HE-GC domain-switching mechanism that fully leverages SNNs’ temporal dynamics and event-driven sparsity in encrypted domains. Experiments on MNIST and Fashion-MNIST datasets demonstrate that our approach maintains high inference accuracy while achieving up to $48 \times$ reduction in end-to-end latency and significantly reduced communication costs compared to pure-FHE baselines. These results confirm our framework’s potential for enabling practical and scalable privacy-preserving SNN inference in MLaaS environments.
