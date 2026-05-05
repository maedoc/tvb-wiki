# A Multimodal Deep Learning Approach for White Matter Shape Prediction in Diffusion MRI Tractography

**Source**: semantic-scholar
**ID**: 277cc01022028689f2050826a4c5bb847c2423d8
**DOI**: 10.1002/hbm.70396
**URL**: https://www.semanticscholar.org/paper/277cc01022028689f2050826a4c5bb847c2423d8
**Date**: 2025-04-25
**Year**: 2025
**Authors**: Yui Lo, Yuqian Chen, Dongnan Liu, L. Zekelman, Jarrett Rushmore, Y. Rathi, N. Makris, Alexandra J. Golby, Fan Zhang, Weidong Cai, L. O’Donnell
**Venue**: Human Brain Mapping
**Citations**: 2

## Abstract

Recently, shape measures have emerged as promising descriptors of white matter tractography, offering complementary insights into anatomical variability and associations with cognitive and clinical phenotypes. However, conventional methods for computing shape measures are computationally expensive and time‐consuming for large‐scale datasets due to reliance on voxel‐based representations. To address these limitations, we introduce Tract2Shape, a novel multimodal deep learning framework that integrates geometric streamline features (as point clouds) with scalar data descriptors (as tabular data) from tractography to predict 10 white matter tractography shape measures. We propose a Siamese architecture in which each subnetwork incorporates a dual‐encoder design, enabling each encoder to learn modality‐specific representations. To enhance model efficiency, we utilize a dimensionality reduction algorithm for the model to predict five primary shape components. The model is trained and evaluated on two independently acquired datasets: the Human Connectome Project minimally preprocessed young adults (HCP‐YA) dataset and the Parkinson's Progression Markers Initiative (PPMI) dataset. Tract2Shape is trained and tested on the HCP‐YA dataset, with performance compared against state‐of‐the‐art models. To assess robustness and generalization, we further evaluate the model on the unseen PPMI dataset. Tract2Shape outperforms state‐of‐the‐art deep learning models across all 10 shape measures, achieving the highest average Pearson's r and the lowest normalized mean squared error (nMSE) on the HCP‐YA dataset. The ablation study shows that both multimodal input and PCA benefit performance. On the unseen testing PPMI dataset, Tract2Shape maintains a high Pearson's r and low nMSE, demonstrating strong generalizability in cross‐dataset evaluation. In comparison with traditional voxel‐representation‐based shape computation, Tract2Shape achieves a 99.2% improvement in efficiency (< 0.1 s per subject). Tract2Shape enables fast, accurate, and generalizable prediction of white matter shape measures from tractography data, supporting scalable analysis across datasets. This framework lays a promising foundation for future large‐scale white matter shape analysis.
