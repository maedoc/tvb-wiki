# Fine-scale striatal parcellation using diffusion MRI tractography and graph neural networks

**Source**: semantic-scholar
**ID**: 2c2bad38488555047874f7ef634ab48ede78f4f4
**DOI**: 10.1016/j.media.2025.103482
**URL**: https://www.semanticscholar.org/paper/2c2bad38488555047874f7ef634ab48ede78f4f4
**Date**: 2025-02-01
**Year**: 2025
**Authors**: Jingjing Gao, Mingqi Liu, Maomin Qian, Heping Tang, Junyi Wang, Liang Ma, Yanling Li, Xin Dai, Zhengning Wang, Fengmei Lu, Fan Zhang
**Venue**: Medical Image Anal.
**Citations**: 1

## Abstract

The striatum, a crucial part of the basal ganglia, plays a key role in various brain functions through its interactions with the cortex. The complex structural and functional diversity across subdivisions within the striatum highlights the necessity for precise striatal segmentation. In this study, we introduce a novel deep clustering pipeline for automated, fine-scale parcellation of the striatum using diffusion MRI (dMRI) tractography. Initially, we employ a voxel-based probabilistic fiber tractography algorithm combined with a fiber-tract embedding technique to capture intricate dMRI connectivity patterns. To maintain critical inter-voxel relationships, our approach employs Graph Neural Networks (GNNs) to create accurate graph representations of the striatum. This involves encoding probabilistic fiber bundle characteristics as node attributes and refining edge weights using activation functions to enhance the graph's interpretability and accuracy. The methodology incorporates a Transformer-based GraphConv autoencoder in the pre-training phase to extract critical spatial features while minimizing reconstruction loss. In the fine-tuning phase, a novel joint loss mechanism markedly improves segmentation precision and anatomical fidelity. Integration of traditional clustering techniques with multi-head self-attention mechanisms further elevates the accuracy and robustness of our segmentation approach. This methodology provides new insights into the striatum's role in cognition and behavior and offers potential clinical applications for neurological disorders.
