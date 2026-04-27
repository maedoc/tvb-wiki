# Dataset-Aware Preprocessing for Hippocampal Segmentation: Insights from Ablation and Transfer Learning

**Source**: semantic-scholar
**ID**: 55a43781dd1f53b4f7a02ee010366307dd170c11
**DOI**: 10.3390/math13203309
**URL**: https://www.semanticscholar.org/paper/55a43781dd1f53b4f7a02ee010366307dd170c11
**Date**: 2025-10-16
**Year**: 2025
**Authors**: Faizaan Fazal Khan, Jun-Hyung Kim, Ji-In Kim, Goo-Rak Kwon
**Venue**: Mathematics
**Citations**: 1

## Abstract

Accurate hippocampal segmentation in 3D MRI is essential for neurodegenerative disease research and diagnosis. Preprocessing pipelines can strongly influence segmentation accuracy, yet their impact across datasets and in transfer learning scenarios remains underexplored. This study systematically compares a No Preprocessing (NP) pipeline and a Full Preprocessing (FP) pipeline for hippocampal segmentation on the EADC-ADNI HarP clinical dataset and the multi-site MSD dataset using a 3D U-Net with residual connections and dropout regularization. Evaluations employed standard overlap metrics, Hausdorff Distance (HD), and Wilcoxon signed-rank tests, complemented by qualitative analysis. Results show that NP consistently outperformed FP in Dice, Jaccard, and F1 metrics on HarP (e.g., Dice 0.8876 vs. 0.8753, p < 0.05), while FP achieved superior HD, indicating better boundary precision. Similar trends emerged in transfer learning from MSD to HarP, with NP improving overlap measures and FP maintaining lower HD. To test whether the findings generalize across architectures, experiments on Harp Dataset were also repeated with a 3D V-Net backbone, which reproduced the same trend. Comparative analysis with recent studies confirmed the competitiveness of the proposed approach despite lower input resolution and reduced model complexity. These findings highlight that preprocessing choice should be tailored to dataset characteristics and the target evaluation metric. The results provide practical guidance for selecting segmentation workflows in clinical and multi-center neuroimaging applications.
