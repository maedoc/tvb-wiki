# BrainMT: A Hybrid Mamba-Transformer Architecture for Modeling Long-Range Dependencies in Functional MRI Data

**Source**: semantic-scholar
**ID**: 86ef1717eb2f95cbbf8c42f7a855f607850b7adb
**DOI**: 10.48550/arXiv.2506.22591
**URL**: https://www.semanticscholar.org/paper/86ef1717eb2f95cbbf8c42f7a855f607850b7adb
**Date**: 2025-06-27
**Year**: 2025
**Authors**: Arunkumar Kannan, M. A. Lindquist, Brian S Caffo
**Venue**: International Conference on Medical Image Computing and Computer-Assisted Intervention
**Citations**: 3

## Abstract

Recent advances in deep learning have made it possible to predict phenotypic measures directly from functional magnetic resonance imaging (fMRI) brain volumes, sparking significant interest in the neuroimaging community. However, existing approaches, primarily based on convolutional neural networks or transformer architectures, often struggle to model the complex relationships inherent in fMRI data, limited by their inability to capture long-range spatial and temporal dependencies. To overcome these shortcomings, we introduce BrainMT, a novel hybrid framework designed to efficiently learn and integrate long-range spatiotemporal attributes in fMRI data. Our framework operates in two stages: (1) a bidirectional Mamba block with a temporal-first scanning mechanism to capture global temporal interactions in a computationally efficient manner; and (2) a transformer block leveraging self-attention to model global spatial relationships across the deep features processed by the Mamba block. Extensive experiments on two large-scale public datasets, UKBioBank and the Human Connectome Project, demonstrate that BrainMT achieves state-of-the-art performance on both classification (sex prediction) and regression (cognitive intelligence prediction) tasks, outperforming existing methods by a significant margin. Our code and implementation details will be made publicly available at this https://github.com/arunkumar-kannan/BrainMT-fMRI
