# Training Deep Normalization-Free Spiking Neural Networks with Lateral Inhibition

**Source**: semantic-scholar
**ID**: 18ddb52abf6953238a95fed6e7912aa93e34a160
**DOI**: 10.48550/arXiv.2509.23253
**URL**: https://www.semanticscholar.org/paper/18ddb52abf6953238a95fed6e7912aa93e34a160
**Date**: 2025-09-27
**Year**: 2025
**Authors**: Peiyu Liu, Jianhao Ding, Zhaofei Yu
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Spiking Neural Networks (SNNs) have garnered significant attention as a central paradigm in neuromorphic computing, owing to their energy efficiency and biological plausibility. However, training deep SNNs has critically depended on explicit normalization schemes, leading to a trade-off between performance and biological realism. To resolve this conflict, we propose a normalization-free learning framework that incorporates lateral inhibition inspired by cortical circuits. Our framework replaces the traditional feedforward SNN layer with distinct excitatory (E) and inhibitory (I) neuronal populations that capture the key features of the cortical E-I interaction. The E-I circuit dynamically regulates neuronal activity through subtractive and divisive inhibition, which respectively control the excitability and gain of neurons. To stabilize end-to-end training of the biologically constrained SNNs, we propose two key techniques: E-I Init and E-I Prop. E-I Init is a dynamic parameter initialization scheme that balances excitatory and inhibitory inputs while performing gain control. E-I Prop decouples the backpropagation of the circuit from the forward pass, regulating gradient flow. Experiments across multiple datasets and network architectures demonstrate that our framework enables stable training of deep normalization-free SNNs with biological realism, achieving competitive performance. Therefore, our work not only provides a solution to training deep SNNs but also serves as a computational platform for further exploring the functions of E-I interaction in large-scale cortical computation. Code is available at https://github.com/vwOvOwv/DeepEISNN.
