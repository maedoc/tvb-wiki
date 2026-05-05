# DDTracking: A Deep Generative Framework for Diffusion MRI Tractography with Streamline Local-Global Spatiotemporal Modeling

**Source**: semantic-scholar
**ID**: 92acbc4d3a7f53355a54e42e30c90a9974e7dcca
**DOI**: 10.1016/j.media.2026.103967
**URL**: https://www.semanticscholar.org/paper/92acbc4d3a7f53355a54e42e30c90a9974e7dcca
**Date**: 2025-08-06
**Year**: 2025
**Authors**: Yijie Li, Wei Zhang, Xi Zhu, Ye Wu, Y. Rathi, Lauren J. O’Donnell, Fan Zhang
**Venue**: Medical Image Anal.
**Citations**: 2

## Abstract

Diffusion MRI (dMRI) tractography is an advanced technique that uniquely enables in vivo mapping of brain fiber pathways. Traditional methods rely on tissue modeling to estimate fiber orientations for streamline propagation, which are computationally intensive and remain sensitive to noise and artifacts. Recent deep learning-based approaches enable data-driven fiber tracking by directly mapping dMRI signals to orientations, demonstrating both improved efficiency and accuracy. However, existing methods typically operate by either leveraging local signal information or learning global dependencies along streamlines. This paper presents DDTracking, a deep generative framework for tractography. One key innovation is the reformulation of streamline propagation as a conditional denoising diffusion process. To the best of our knowledge, this is the first work to apply diffusion models for fiber tracking. Our network architecture incorporates two new designs, including: (1) a dual-pathway encoding scheme that extracts complementary local spatial features and global temporal context, and (2) a conditional diffusion model module that integrates the spatiotemporal features to predict propagation orientations. All components are trained jointly in an end-to-end manner without any pretraining. In this way, DDTracking can capture fine-scale structural details at each point while ensuring long-range consistency across the entire streamline. We conduct a comprehensive evaluation across diverse datasets, including both synthetic and clinical data. Experiments demonstrate that DDTracking outperforms traditional model-based and state-of-the-art deep learning-based methods in terms of tracking accuracy and computational efficiency. Furthermore, our results highlight DDTracking's high generalizability across heterogeneous datasets, spanning varying health conditions, age groups, imaging protocols, and scanner types. Code is available at: https://github.com/yishengpoxiao/DDTracking.git.
