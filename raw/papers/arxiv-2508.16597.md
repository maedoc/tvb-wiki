# Bridging Foundation Models and Efficient Architectures: A Modular Brain Imaging Framework with Local Masking and Pretrained Representation Learning

**Source**: semantic-scholar
**ID**: 139b125c5f2429866d9931e0f7f80b906b974d00
**DOI**: 10.48550/arXiv.2508.16597
**URL**: https://www.semanticscholar.org/paper/139b125c5f2429866d9931e0f7f80b906b974d00
**Date**: 2025-08-09
**Year**: 2025
**Authors**: Yanwen Wang, Xinglin Zhao, Yijin Song, Xiaobo Liu, Yanrong Hao, Rui Cao, Xin Wen
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Functional connectivity (FC) derived from resting-state fMRI plays a critical role in personalized predictions such as age and cognitive performance. However, applying foundation models(FM) to fMRI data remains challenging due to its high dimensionality, computational complexity, and the difficulty in capturing complex spatiotemporal dynamics and indirect region-of-interest (ROI) interactions. To address these limitations, we propose a modular neuroimaging framework that integrates principles from FM with efficient, domain-specific architectures. Our approach begins with a Local Masked Autoencoder (LMAE) for pretraining, which reduces the influence of hemodynamic response function (HRF) dynamics and suppresses noise. This is followed by a Random Walk Mixture of Experts (RWMOE) module that clusters features across spatial and temporal dimensions, effectively capturing intricate brain interactions. Finally, a state-space model (SSM)-based predictor performs downstream task inference. Evaluated on the Cambridge Centre for Ageing and Neuroscience (Cam-CAN) dataset, our framework achieved mean absolute errors (MAEs) of 5.343 for age prediction and 2.940 for fluid intelligence, with Pearson correlation coefficients (PCCs) of 0.928 and 0.887, respectively-outperforming existing state-of-the-art methods. Visualization of expert distribution weights further enhances interpretability by identifying key brain regions. This work provides a robust, interpretable alternative to LLM-based approaches for fMRI analysis, offering novel insights into brain aging and cognitive function.
