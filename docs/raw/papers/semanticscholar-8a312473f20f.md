# 3D masked autoencoder with spatiotemporal transformer for modeling of 4D fMRI data

**Source**: semantic-scholar
**ID**: 8a312473f20f814293c60e7993328b2806c75186
**DOI**: 10.1016/j.media.2025.103861
**URL**: https://www.semanticscholar.org/paper/8a312473f20f814293c60e7993328b2806c75186
**Date**: 2025-11-01
**Year**: 2025
**Authors**: Jie Gao, Bao Ge, Ning Qiang, Shi-Shun Zhao
**Venue**: Medical Image Anal.
**Citations**: 3

## Abstract

Functional magnetic resonance imaging (fMRI) is a crucial tool in neuroscience for capturing dynamic brain activity across spatial and temporal dimensions. However, fMRI data are high-dimensional, spatiotemporal interdependent, and often noisy, posing significant challenges for representing brain functions and associated applications. To effectively extract spatiotemporal features from fMRI data and map functional brain networks, this study proposes a novel 3D Masked Autoencoder architecture integrated with Spatiotemporal Transformers (MAE-ST). The proposed framework leverages self-supervised learning through partial data masking, enabling efficient spatial feature extraction while mitigating dependence on labeled datasets and enhancing noise robustness. In the MAE-ST encoder, visual transformer (ViT) module and temporal transformer module are employed to extract fMRI spatial features and temporal features respectively, and then the decoder reconstructs fMRI sequence with latent variables that are output by the encoder. After training, the latent variables can be regarded as the temporal features of fMRI data, which are used to estimate functional brain networks by regression analysis. Comprehensive experimental results on HCP task fMRI datasets and ADHD-200 resting state fMRI datasets demonstrated that the proposed MAE-ST model achieves superior performance in mapping both task-evoked networks and resting state networks, compared with the latest deep learning models and traditional methods. Moreover, we construct a classification pipeline based on the MAE-ST model and apply it on ADHD-200 dataset. The MAE-ST model here is used to construct data-driven brain atlas and calculate functional connectivity for classification study. The results indicated that the proposed classification pipeline outperforms several existing methods that used predefined atlases, further demonstrated the effectiveness and superiority of the proposed MAE-ST model. This work highlights the potential of combining masked autoencoders with Transformers for handling global feature extraction in both spatial and temporal dimensions of 4D fMRI data, offering a new framework for functional brain network modeling and brain disorder identification.
