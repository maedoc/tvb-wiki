# Efficient Training of Deep Spiking Neural Networks Using a Modified Learning Rate Scheduler

**Source**: semantic-scholar
**ID**: 9c1878619f03977d2c4a9f0148cc5f7bf7f5adea
**DOI**: 10.3390/math13081361
**URL**: https://www.semanticscholar.org/paper/9c1878619f03977d2c4a9f0148cc5f7bf7f5adea
**Date**: 2025-04-21
**Year**: 2025
**Authors**: S. Cha, Dong-Sun Kim
**Venue**: Mathematics
**Citations**: 2

## Abstract

Deep neural networks (DNNs) have achieved high accuracy in various applications, but with the rapid growth of AI and the increasing scale and complexity of datasets, their computational cost and power consumption have become even more significant challenges. Spiking neural networks (SNNs), inspired by biological neurons, offer an energy-efficient alternative by using spike-based information processing. However, training SNNs is difficult due to the non-differentiability of their activation function and the challenges in constructing deep architectures. This study addresses these issues by integrating DNN-like backpropagation into SNNs using a supervised learning approach. A surrogate gradient descent based on the arctangent function is applied to approximate the non-differentiable activation function, enabling stable gradient-based learning. The study also explores the interplay between the spatial domain (layer-wise propagation) and the temporal domain (time step), ensuring proper gradient propagation using the chain rule. Additionally, mini-batch training, Adam optimization, and layer normalization are incorporated to improve training efficiency and mitigate gradient vanishing. A softmax-based probability representation and cross-entropy loss function are used to optimize classification performance. Along with these techniques, a deep SNN was designed to converge to the optimal point faster than other models in the early stages of training by utilizing a modified learning rate scheduler. The proposed learning method allows deep SNNs to achieve competitive accuracy while maintaining their inherent low-power characteristics. These findings contribute to making SNNs more practical for machine learning applications by combining the advantages of deep learning and biologically inspired computing. In summary, this study contributes to the field by analyzing and adapting deep learning techniques—such as dropout, layer normalization, mini-batch training, and Adam optimization—to the spiking domain, and by proposing a novel learning rate scheduler that enables faster convergence during early training phases with fewer epochs.
