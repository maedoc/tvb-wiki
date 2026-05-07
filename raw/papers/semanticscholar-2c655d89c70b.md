# SPICE-Level Demonstration of Unsupervised Learning With Spintronic Synapses in Spiking Neural Networks

**Source**: semantic-scholar
**ID**: 2c655d89c70b4e9869728277ab7300381a8a2256
**DOI**: 10.1109/ACCESS.2024.3411519
**URL**: https://www.semanticscholar.org/paper/2c655d89c70b4e9869728277ab7300381a8a2256
**Year**: 2025
**Authors**: Salah Daddinounou, A. Gebregiorgis, Said Hamdioui, E. Vatajelu
**Venue**: IEEE Access
**Citations**: 1

## Abstract

Spiking Neural Networks (SNNs) are Artificial Neural Networks which promise to mimic the biological brain processing with unsupervised online learning capability for various cognitive tasks. However, SNN hardware implementation with online learning support is not trivial and might prove highly inefficient. This paper proposes an energy-efficient hardware implementation for SNN synapses. The implementation is based on parallel-connected Magnetic Tunnel Junction (MTJ) devices and exploits their inherent stochasticity. In addition, it uses a dedicated unsupervised learning rule based on optimized Spike-Timing-Dependent Plasticity (STDP). To facilitate the design of the SNN, its training and evaluation, an open-source Python-based platform is developed; it takes as input the SNN parameters and discrete circuit components, and it automatically generates the associated full netlist in SPICE then launches the simulation; moreover, it extracts the simulation results and makes them available in python for evaluation and manipulation. Unlike conventional neuromorphic hardware that relies on simple weight mapping post-off-line training, our approach emphasizes continuous, unsupervised learning, ensuring an energy efficiency of 11.2nW per synaptic update during training and as low as 109fJ/spike during inference.
