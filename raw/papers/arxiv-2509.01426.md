# DCA: Graph-Guided Deep Embedding Clustering for Brain Atlases

**Source**: semantic-scholar
**ID**: 65eab37fd9c9ba3ab9decf1ccfe1e498927985e4
**DOI**: 10.48550/arXiv.2509.01426
**URL**: https://www.semanticscholar.org/paper/65eab37fd9c9ba3ab9decf1ccfe1e498927985e4
**Date**: 2025-09-01
**Year**: 2025
**Authors**: Mo Wang, Kaining Peng, Jingsheng Tang, Hongkai Wen, Quanying Liu
**Venue**: arXiv.org
**Citations**: 3

## Abstract

Brain atlases are essential for reducing the dimensionality of neuroimaging data and enabling interpretable analysis. However, most existing atlases are predefined, group-level templates with limited flexibility and resolution. We present Deep Cluster Atlas (DCA), a graph-guided deep embedding clustering framework for generating individualized, voxel-wise brain parcellations. DCA combines a pretrained autoencoder with spatially regularized deep clustering to produce functionally coherent and spatially contiguous regions. Our method supports flexible control over resolution and anatomical scope, and generalizes to arbitrary brain structures. We further introduce a standardized benchmarking platform for atlas evaluation, using multiple large-scale fMRI datasets. Across multiple datasets and scales, DCA outperforms state-of-the-art atlases, improving functional homogeneity by 98.8% and silhouette coefficient by 29%, and achieves superior performance in downstream tasks such as autism diagnosis and cognitive decoding. We also observe that a fine-tuned pretrained model achieves superior results on the corresponding task. Codes and models are available at https://github.com/ncclab-sustech/DCA .
