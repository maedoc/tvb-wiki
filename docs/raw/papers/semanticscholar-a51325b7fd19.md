# Ultra-High Resolution 9.4T Brain MRI Segmentation via a Newly Engineered Multi-Scale Residual Nested U-Net with Gated Attention

**Source**: semantic-scholar
**ID**: a51325b7fd19a82894f0b43928dbd47a8d287a89
**DOI**: 10.3390/bioengineering12101014
**URL**: https://www.semanticscholar.org/paper/a51325b7fd19a82894f0b43928dbd47a8d287a89
**Date**: 2025-09-24
**Year**: 2025
**Authors**: Aryan Kalluvila, Jay B. Patel, Jason M. Johnson
**Venue**: Bioengineering
**Citations**: 0

## Abstract

A 9.4T brain MRI is the highest resolution MRI scanner in the public market. It offers submillimeter brain imaging with exceptional anatomical detail, making it one of the most powerful tools for detecting subtle structural changes associated with neurological conditions. Current segmentation models are optimized for lower-field MRI (1.5T–3T), and they struggle to perform well on 9.4T data. In this study, we present the GA-MS-UNet++, the world’s first deep learning-based model specifically designed for 9.4T brain MRI segmentation. Our model integrates multi-scale residual blocks, gated skip connections, and spatial channel attention mechanisms to improve both local and global feature extraction. The model was trained and evaluated on 12 patients in the UltraCortex 9.4T dataset and benchmarked against four leading segmentation models (Attention U-Net, Nested U-Net, VDSR, and R2UNet). The GA-MS-UNet++ achieved a state-of-the-art performance across both evaluation sets. When tested against manual, radiologist-reviewed ground truth masks, the model achieved a Dice score of 0.93. On a separate test set using SynthSeg-generated masks as the ground truth, the Dice score was 0.89. Across both evaluations, the model achieved an overall accuracy of 97.29%, precision of 90.02%, and recall of 94.00%. Statistical validation using the Wilcoxon signed-rank test (p < 1 × 10−5) and Kruskal–Wallis test (H = 26,281.98, p < 1 × 10−5) confirmed the significance of these results. Qualitative comparisons also showed a near-exact alignment with ground truth masks, particularly in areas such as the ventricles and gray–white matter interfaces. Volumetric validation further demonstrated a high correlation (R2 = 0.90) between the predicted and ground truth brain volumes. Despite the limited annotated data, the GA-MS-UNet++ maintained a strong performance and has the potential for clinical use. This algorithm represents the first publicly available segmentation model for 9.4T imaging, providing a powerful tool for high-resolution brain segmentation and driving progress in automated neuroimaging analysis.
