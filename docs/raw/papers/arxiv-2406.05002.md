# Deep Jansen-Rit Parameter Inference for Model-Driven Analysis of Brain Activity

**arXiv ID**: 2406.05002
**Published**: 2024-06-07
**Updated**: 2025-03-18
**Authors**: Deepa Tilwani, Christian O'Reilly
**Categories**: q-bio.NC, cs.AI
**URL**: https://arxiv.org/abs/2406.05002
**PDF**: https://arxiv.org/pdf/2406.05002
**Source**: arXiv

## Abstract

Accurately modeling effective connectivity (EC) is critical for understanding how the brain processes and integrates sensory information. Yet, it remains a formidable challenge due to complex neural dynamics and noisy measurements such as those obtained from the electroencephalogram (EEG). Model-driven EC infers local (within a brain region) and global (between brain regions) EC parameters by fitting a generative model of neural activity onto experimental data. This approach offers a promising route for various applications, including investigating neurodevelopmental disorders. However, current approaches fail to scale to whole-brain analyses and are highly noise-sensitive. In this work, we employ three deep-learning architectures--a transformer, a long short-term memory (LSTM) network, and a convolutional neural network and bidirectional LSTM (CNN-BiLSTM) network--for inverse modeling and compare their performance with simulation-based inference in estimating the Jansen-Rit neural mass model (JR-NMM) parameters from simulated EEG data under various noise conditions. We demonstrate a reliable estimation of key local parameters, such as synaptic gains and time constants. However, other parameters like local JR-NMM connectivity cannot be evaluated reliably from evoked-related potentials (ERP). We also conduct a sensitivity analysis to characterize the influence of JR-NMM parameters on ERP and evaluate their learnability. Our results show the feasibility of deep-learning approaches to estimate the subset of learnable JR-NMM parameters.
