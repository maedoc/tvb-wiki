# A flexible framework for structural plasticity in GPU-accelerated sparse spiking neural networks

**Source**: semantic-scholar
**ID**: 7a91b1a023d2000ffe6e63b32d3d51b1a1967fc6
**DOI**: 10.1088/2634-4386/ae4535
**URL**: https://www.semanticscholar.org/paper/7a91b1a023d2000ffe6e63b32d3d51b1a1967fc6
**Date**: 2025-10-22
**Year**: 2025
**Authors**: James C. Knight, Johanna Senk, Thomas Nowotny
**Venue**: Neuromorphic Computing and Engineering
**Citations**: 1

## Abstract

The majority of research in both training artificial neural networks (ANNs) and modeling learning in biological brains focuses on synaptic plasticity, where learning equates to changing the strength of existing connections. However, in biological brains, structural plasticity—where new connections are created and others removed—is also vital, not only for effective learning but also for recovery from damage and optimal resource usage. Inspired by structural plasticity, pruning is often used in machine learning (ML) to remove weak connections from trained models to reduce the computational requirements of inference. However, the ML frameworks typically used for backpropagation-based training of both ANNs and spiking neural networks (SNNs) are optimized for dense connectivity, meaning that pruning does not help reduce the training costs of ever-larger models. The GeNN simulator already supports efficient GPU-accelerated simulation of sparse SNNs for computational neuroscience and ML. Here, we present a new flexible framework for implementing GPU-accelerated structural plasticity rules and demonstrate this first using the e-prop supervised learning rule and DEEP R to train efficient, sparse SNN classifiers and then, in an unsupervised learning context, to learn topographic maps. Compared to baseline dense models, our sparse classifiers reduce training time by up to 10 × while the DEEP R rewiring enables them to perform as well as the original models. We demonstrate topographic map formation in faster-than-realtime simulations, provide insights into the connectivity evolution, and measure simulation speed versus network size. The proposed framework will enable further research into achieving and maintaining sparsity in network structure and neural communication, as well as exploring the computational benefits of sparsity in a range of neuromorphic applications.
