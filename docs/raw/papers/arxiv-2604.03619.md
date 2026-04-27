# Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?

**Source**: arxiv
**ID**: 2604.03619
**URL**: https://arxiv.org/abs/2604.03619
**Date**: 2026-04-04
**Year**: 2026
**Authors**: Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon
**Categories**: cs.CV

## Abstract

Modeling long-range spatiotemporal dynamics in functional Magnetic Resonance Imaging (fMRI) remains a key challenge due to the high dimensionality of the four-dimensional signals. Prior voxel-based models, although demonstrating excellent performance and interpretation capabilities, are constrained by prohibitive memory demands and thus can only capture limited temporal windows. To address this, we propose TABLeT (Two-dimensionally Autoencoded Brain Latent Transformer), a novel approach that tokenizes fMRI volumes using a pre-trained 2D natural image autoencoder. Each 3D fMRI volume is compressed into a compact set of continuous tokens, enabling long-sequence modeling with a simple Transformer encoder with limited VRAM. Across large-scale benchmarks including the UK-Biobank (UKB), Human Connectome Project (HCP), and ADHD-200 datasets, TABLeT outperforms existing models in multiple tasks, while demonstrating substantial gains in computational and memory efficiency over the state-of-the-art voxel-based method given the same input. Furthermore, we develop a self-supervised masked token modeling approach to pre-train TABLeT, which improves the model's performance for various downstream tasks. Our findings suggest a promising approach for scalable and interpretable spatiotemporal modeling of brain activity. Our code is available at https://github.com/beotborry/TABLeT.
