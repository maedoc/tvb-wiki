# Learning Neuron Dynamics within Deep Spiking Neural Networks

**Source**: semantic-scholar
**ID**: 5611da46490b5ceb89dc897167ee40a023dfed1a
**DOI**: 10.48550/arXiv.2510.07341
**URL**: https://www.semanticscholar.org/paper/5611da46490b5ceb89dc897167ee40a023dfed1a
**Date**: 2025-10-07
**Year**: 2025
**Authors**: Eric Jahns, Davi Moreno, Michel A. Kinsy
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Spiking Neural Networks (SNNs) offer a promising energy-efficient alternative to Artificial Neural Networks (ANNs) by utilizing sparse and asynchronous processing through discrete spike-based computation. However, the performance of deep SNNs remains limited by their reliance on simple neuron models, such as the Leaky Integrate-and-Fire (LIF) model, which cannot capture rich temporal dynamics. While more expressive neuron models exist, they require careful manual tuning of hyperparameters and are difficult to scale effectively. This difficulty is evident in the lack of successful implementations of complex neuron models in high-performance deep SNNs. In this work, we address this limitation by introducing Learnable Neuron Models (LNMs). LNMs are a general, parametric formulation for non-linear integrate-and-fire dynamics that learn neuron dynamics during training. By learning neuron dynamics directly from data, LNMs enhance the performance of deep SNNs. We instantiate LNMs using low-degree polynomial parameterizations, enabling efficient and stable training. We demonstrate state-of-the-art performance in a variety of datasets, including CIFAR-10, CIFAR-100, ImageNet, and CIFAR-10 DVS. LNMs offer a promising path toward more scalable and high-performing spiking architectures.
