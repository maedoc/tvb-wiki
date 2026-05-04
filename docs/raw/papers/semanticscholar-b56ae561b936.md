# From Structural Morphology to BrainNet Transformer: Harmonized Morphological Networks for Multi-site Autism Diagnosis

**Source**: semantic-scholar
**ID**: b56ae561b9369800204f8be267648ee9e1733e5b
**DOI**: 10.1109/AIBDF67964.2025.11440727
**URL**: https://www.semanticscholar.org/paper/b56ae561b9369800204f8be267648ee9e1733e5b
**Date**: 2025-12-26
**Year**: 2025
**Authors**: Guolin Guo, Yijie Teng, Hao Wang, Lin Lu
**Venue**: 2025 5th International Symposium on Artificial Intelligence and Big Data (AIBDF)
**Citations**: 0

## Abstract

Autism spectrum disorder (ASD) presents substantial diagnostic challenges due to its heterogeneous manifestations and the subjectivity inherent in behavioral assessments. Structural MRI provides valuable morphological information, but its diagnostic utility is hindered by pronounced interindividual variability and non-biological site effects in large multi-center cohorts. We propose Harmonized Morphological Networks (HMN), a multi-site ASD classification framework that integrates distribution-based morphological brain networks, edge-level ComBat harmonization, and graph-based deep learning. Morphological networks were constructed from regional gray-matter morphology using a distribution-based similarity measure across three cortical parcellations. ComBat was applied after network construction to harmonize edge weights while preserving biological covariates, substantially reducing residual site effects and improving cross-site consistency. Building on the harmonized networks, we adapted the BrainNet Transformer (BrainNetTF) and benchmarked it against hi-GCN and BrainNetCNN, with a domain-adversarial GNN included as a supplementary harmonization-aware baseline. Experiments on ABIDEII demonstrate that ComBat markedly mitigates site-related variability and yields modest gains for CNN/GCN-based models, while BrainNetTF achieves the highest accuracy and improved stability, and hi-GCN attains the best AUROC. These findings highlight the importance of jointly considering harmonization strategy and model architecture, and support transformer-based learning on harmonized morphological networks as a scalable approach for multi-site ASD classification.
