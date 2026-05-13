# GraSTI-ACL: Graph spatial-temporal infomax with adversarial contrastive learning for brain disorders diagnosis based on resting-state fMRI

**Source**: semantic-scholar
**ID**: b0145d012f306b4f2e45d7fdb0e9d93be9d2b541
**DOI**: 10.1016/j.media.2025.103815
**URL**: https://www.semanticscholar.org/paper/b0145d012f306b4f2e45d7fdb0e9d93be9d2b541
**Date**: 2025-09-20
**Year**: 2025
**Authors**: Biao He, Erni Ji, X. Zong, Zhen Liang, Gan Huang, Li Zhang
**Venue**: Medical Image Anal.
**Citations**: 1

## Abstract

Resting-state functional magnetic resonance imaging (rs-fMRI) has been widely used in research on brain disorders due to its informative spatial and temporal resolution, and it shows growing potential as a noninvasive tool for assisting clinical diagnosis. Among various methods based on rs-fMRI, graph neural networks have received significant attention because of their inherent structural similarity to functional connectivity networks (FCNs) of the brain. However, constructing FCNs that effectively capture both spatial and temporal information from rs-fMRI remains challenging, as traditional methods often rely on static, fully connected graphs that risk redundancy and neglect dynamic patterns. Based on the information bottleneck principle, this paper proposes a graph augmentation strategy named Graph Spatial-Temporal Infomax (GraSTI) to adaptively preserve both global spatial brain-wide FCNs and local temporal dynamics. We integrate GraSTI with theoretical explanations and design a practical implementation to adapt to our graph augmentation strategy and enhance feature capture capability. Furthermore, GraSTI is incorporated into an adversarial contrastive learning framework to achieve a mutual information equilibrium between graph representation effectiveness and robustness for downstream brain disorders diagnosis tasks. The proposed method is evaluated on datasets from three different brain disorders: Alzheimer's disease (AD), major depressive disorder (MDD), and bipolar disorder (BD). Extensive experiments demonstrate that the proposed GraSTI-ACL achieves diagnostic accuracy gains of 0.13% to 23.56% for AD, 1.23% to 13.81% for MDD, and 2.53% to 24.53% for BD diagnosis over existing methods. Meanwhile, our method demonstrates strong interpretability in identifying relevant brain regions and connectivities for different brain disorders.
