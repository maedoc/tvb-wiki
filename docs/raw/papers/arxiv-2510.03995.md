# PrivSpike: Employing Homomorphic Encryption for Private Inference of Deep Spiking Neural Networks

**Source**: semantic-scholar
**ID**: 31fb438c2eedc2c29b36a5a3ea078021034753b8
**DOI**: 10.48550/arXiv.2510.03995
**URL**: https://www.semanticscholar.org/paper/31fb438c2eedc2c29b36a5a3ea078021034753b8
**Date**: 2025-10-05
**Year**: 2025
**Authors**: Nges Brian Njungle, Eric Jahns, Milan Stojkov, Michel A. Kinsy
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Deep learning has become a cornerstone of modern machine learning. It relies heavily on vast datasets and significant computational resources for high performance. This data often contains sensitive information, making privacy a major concern in deep learning. Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to conventional deep learning approaches. Nevertheless, SNNs still depend on large volumes of data, inheriting all the privacy challenges of deep learning. Homomorphic encryption addresses this challenge by allowing computations to be performed on encrypted data, ensuring data confidentiality throughout the entire processing pipeline. In this paper, we introduce PRIVSPIKE, a privacy-preserving inference framework for SNNs using the CKKS homomorphic encryption scheme. PRIVSPIKE supports arbitrary depth SNNs and introduces two key algorithms for evaluating the Leaky Integrate-and-Fire activation function: (1) a polynomial approximation algorithm designed for high-performance SNN inference, and (2) a novel scheme-switching algorithm that optimizes precision at a higher computational cost. We evaluate PRIVSPIKE on MNIST, CIFAR-10, Neuromorphic MNIST, and CIFAR-10 DVS using models from LeNet-5 and ResNet-19 architectures, achieving encrypted inference accuracies of 98.10%, 79.3%, 98.1%, and 66.0%, respectively. On a consumer-grade CPU, SNN LeNet-5 models achieved inference times of 28 seconds on MNIST and 212 seconds on Neuromorphic MNIST. For SNN ResNet-19 models, inference took 784 seconds on CIFAR-10 and 1846 seconds on CIFAR-10 DVS. These results establish PRIVSPIKE as a viable and efficient solution for secure SNN inference, bridging the gap between energy-efficient deep neural networks and strong cryptographic privacy guarantees while outperforming prior encrypted SNN solutions.
