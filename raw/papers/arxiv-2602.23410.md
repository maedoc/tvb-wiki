# Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG

**Source**: semantic-scholar
**ID**: 2465ed2c1921e01c770cbcfe36c143a04a88835d
**DOI**: 10.48550/arXiv.2602.23410
**URL**: https://www.semanticscholar.org/paper/2465ed2c1921e01c770cbcfe36c143a04a88835d
**Date**: 2026-02-26
**Year**: 2026
**Authors**: Hanning Guo, Farah Abdellatif, H. Bi, Andrei Galbenus, Nadim Joni Shah, Abigail Morrison, J. Dammers
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Brain foundation models have achieved remarkable advances across a wide range of neuroscience tasks. However, most existing models are limited to a single functional modality, restricting their ability to exploit complementary spatiotemporal dynamics and the collective data scale across imaging techniques. To address this limitation, we propose Brain-OF, the first omnifunctional brain foundation model jointly pretrained on fMRI, EEG and MEG, capable of handling both unimodal and multimodal inputs within a unified framework. To reconcile heterogeneous spatiotemporal resolutions, we introduce the Any-Resolution Neural Signal Sampler, which projects diverse brain signals into a shared semantic space. To further manage semantic shifts, the Brain-OF backbone integrates DINT attention with a Sparse Mixture of Experts, where shared experts capture modality-invariant representations and routed experts specialize in modality-specific semantics. Furthermore, we propose Masked Temporal-Frequency Modeling, a dual-domain pretraining objective that jointly reconstructs brain signals in both the time and frequency domains. Brain-OF is pretrained on a large-scale corpus comprising around 40 datasets and demonstrates superior performance across diverse downstream tasks, highlighting the benefits of joint multimodal integration and dual-domain pretraining.
