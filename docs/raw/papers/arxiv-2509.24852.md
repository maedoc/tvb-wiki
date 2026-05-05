# DelRec: learning delays in recurrent spiking neural networks

**Source**: semantic-scholar
**ID**: 9acbc77e534adb4fec67559d2a3b06ea5d299432
**DOI**: 10.48550/arXiv.2509.24852
**URL**: https://www.semanticscholar.org/paper/9acbc77e534adb4fec67559d2a3b06ea5d299432
**Date**: 2025-09-29
**Year**: 2025
**Authors**: Alexandre Queant, Ulysse Rançon, Benoit R. Cottereau, T. Masquelier
**Venue**: arXiv.org
**Citations**: 8

## Abstract

Spiking neural networks (SNNs) are a bio-inspired alternative to conventional real-valued deep learning models, with the potential for substantially higher energy efficiency. Interest in SNNs has recently exploded due to a major breakthrough: surrogate gradient learning (SGL), which allows training SNNs with backpropagation, strongly outperforming other approaches. In SNNs, each synapse is characterized not only by a weight but also by a transmission delay. While theoretical works have long suggested that trainable delays significantly enhance expressivity, practical methods for learning them have only recently emerged. Here, we introduce ``DelRec'', the first SGL-based method to train axonal or synaptic delays in recurrent spiking layers, compatible with any spiking neuron model. DelRec leverages a differentiable interpolation technique to handle non-integer delays with well-defined gradients at training time. We show that SNNs with trainable recurrent delays outperform feedforward ones, leading to new state-of-the-art (SOTA) on two challenging temporal datasets (Spiking Speech Command, an audio dataset, and Permuted Sequential MNIST, a vision one), and match the SOTA on the now saturated Spiking Heidelberg Digit dataset using only vanilla Leaky-Integrate-and-Fire neurons with stateless (instantaneous) synapses. Our results demonstrate that recurrent delays are critical for temporal processing in SNNs and can be effectively optimized with DelRec, paving the way for efficient deployment on neuromorphic hardware with programmable delays. Our code is available at https://github.com/alexmaxad/DelRec.
