# TReND: Transformer derived features and Regularized NMF for neonatal functional network Delineation

**Source**: semantic-scholar
**ID**: 6fa60ec47a3b11c5a06161ac669b8bad90d8e8e1
**DOI**: 10.48550/arXiv.2503.02685
**URL**: https://www.semanticscholar.org/paper/6fa60ec47a3b11c5a06161ac669b8bad90d8e8e1
**Date**: 2025-03-04
**Year**: 2025
**Authors**: Sovesh Mohapatra, M. Ouyang, Shufang Tan, Jianlin Guo, Lianglong Sun, Yong He, Hao Huang
**Venue**: International Conference on Medical Image Computing and Computer-Assisted Intervention
**Citations**: 1

## Abstract

Precise parcellation of functional networks (FNs) of early developing human brain is the fundamental basis for identifying biomarker of developmental disorders and understanding functional development. Resting-state fMRI (rs-fMRI) enables in vivo exploration of functional changes, but adult FN parcellations cannot be directly applied to the neonates due to incomplete network maturation. No standardized neonatal functional atlas is currently available. To solve this fundamental issue, we propose TReND, a novel and fully automated self-supervised transformer-autoencoder framework that integrates regularized nonnegative matrix factorization (RNMF) to unveil the FNs in neonates. TReND effectively disentangles spatiotemporal features in voxel-wise rs-fMRI data. The framework integrates confidence-adaptive masks into transformer self-attention layers to mitigate noise influence. A self supervised decoder acts as a regulator to refine the encoder's latent embeddings, which serve as reliable temporal features. For spatial coherence, we incorporate brain surface-based geodesic distances as spatial encodings along with functional connectivity from temporal features. The TReND clustering approach processes these features under sparsity and smoothness constraints, producing robust and biologically plausible parcellations. We extensively validated our TReND framework on three different rs-fMRI datasets: simulated, dHCP and HCP-YA against comparable traditional feature extraction and clustering techniques. Our results demonstrated the superiority of the TReND framework in the delineation of neonate FNs with significantly better spatial contiguity and functional homogeneity. Collectively, we established TReND, a novel and robust framework, for neonatal FN delineation. TReND-derived neonatal FNs could serve as a neonatal functional atlas for perinatal populations in health and disease.
