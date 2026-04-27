# Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay

**Source**: arxiv
**ID**: 2604.14259
**URL**: https://arxiv.org/abs/2604.14259
**Date**: 2026-04-15
**Year**: 2026
**Authors**: Qianyu Chen, Shujian Yu
**Categories**: q-bio.TO, cs.LG, eess.IV

## Abstract

Functional magnetic resonance imaging (fMRI) is widely used for studying and diagnosing brain disorders, with functional connectivity (FC) matrices providing powerful representations of large-scale neural interactions. However, existing diagnostic models are trained either on a single site or under full multi-site access, making them unsuitable for real-world scenarios where clinical data arrive sequentially from different institutions. This results in limited generalization and severe catastrophic forgetting. This paper presents the first continual learning framework specifically designed for fMRI-based diagnosis across heterogeneous clinical sites. Our framework introduces a structure-aware variational autoencoder that synthesizes realistic FC matrices for both patient and control groups. Built on this generative backbone, we develop a multi-level knowledge distillation strategy that aligns predictions and graph representations between new-site data and replayed samples. To further enhance efficiency, we incorporate a hierarchical contextual bandit scheme for adaptive replay sampling. Experiments on multi-site datasets for major depressive disorder (MDD), schizophrenia (SZ), and autism spectrum disorder (ASD) show that the proposed generative model enhances data augmentation quality, and the overall continual learning framework substantially outperforms existing methods in mitigating catastrophic forgetting. Our code is available at https://github.com/4me808/FORGE.
