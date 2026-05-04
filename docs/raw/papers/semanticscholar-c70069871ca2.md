# When to Harmonize? Evaluating Stage-Specific Harmonization in Federated Brain Age Estimation

**Source**: semantic-scholar
**ID**: c70069871ca2465b7a6b1687fb63f5bb9e654415
**DOI**: 10.1109/ICKG66886.2025.00025
**URL**: https://www.semanticscholar.org/paper/c70069871ca2465b7a6b1687fb63f5bb9e654415
**Date**: 2025-11-13
**Year**: 2025
**Authors**: Tanurima Halder, Kunal Deo, Nicolás Nieto, Kaustubh R. Patil, K. Jadhav
**Venue**: 2025 IEEE International Conference on Knowledge Graph (ICKG)
**Citations**: 0

## Abstract

Federated learning (FL) is a promising solution for healthcare Artificial Intelligence (AI), striking a balance between patient privacy and the need for diverse datasets. FL enables collaborative model training across institutions, preserving confidentiality and advancing clinical tasks such as diagnosis and treatment planning. However, a key challenge in this setting is the inherent heterogeneity of medical datasets acquired in different institutions, which can undermine the generalizability and performance of the model. This issue is particularly pronounced in neuroimaging applications, such as Magnetic resonance imaging (MRI), where site-specific biases arise from variations in scanner hardware, acquisition protocols, and preprocessing pipelines. These differences introduce non-biological variability that can jeopardize downstream analyses and model training. To remove the effect of sites, harmonization techniques are essential tools to improve robustness and reliability. Harmonization techniques are usually applied at the feature level; however, given the limited access to the data possessed by FL schemes, feature-level harmonization may not be enough to remove site effects. In this work, we propose two complementary harmonization strategies within the FL framework: (1) the traditional feature harmonization, by applying ComBat to directly correct the MRI-derived features; and (2) gradient harmonization, which aligns local model updates, particularly the gradients of fully connected layers, across sites to mitigate inter-site distributional shifts before global aggregation. Together, these approaches aim to improve cross-site consistency and improve the model's overall performance in federated medical imaging tasks.
