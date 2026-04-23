# Automated Brain Tumour Detection And Segmentation Using Attention U-Net Architecture

**Source**: openalex
**ID**: https://openalex.org/W7155055067
**DOI**: 10.47392/irjaem.2026.0140
**URL**: https://doi.org/10.47392/irjaem.2026.0140
**Year**: 2026
**Authors**: S Murugavalli, L Inigho Benjamin, S S Loga Prasath, R Vasil Hassan
**Venue**: International Research Journal on Advanced Engineering and Management (IRJAEM)

## Abstract

The accurate segmentation of brain tumors from multi-modal Magnetic Resonance Imaging (MRI) is a critical prerequisite for oncological care, yet manual delineation remains highly subjective, error-prone, and exceptionally time-consuming. While standard U-Net convolutional architectures provide a strong baseline, they inherently struggle with minute, irregular boundaries and frequently generate false positives by propagating irrelevant background representations. This research proposes an advanced Attention U-Net framework to address these critical limitations. By integrating Attention Gate (AG) mechanisms into standard skip connections, the model dynamically highlights salient tumor features while autonomously suppressing background noise. Evaluated on the benchmark BraTS dataset, this architecture demonstrates superior quantitative performance, achieving an exceptional Dice Similarity Coefficient (DSC) exceeding 0.94 for Whole Tumor (WT) and 0.9877 for Enhancing Tumor (ET) cores. Furthermore, the model is strictly optimized for resource-constrained, consumer-grade hardware (NVIDIA RTX 4050) using mixed-precision training paradigms. The results underscore the Attention U-Net as a highly efficacious, computationally efficient solution for automated neuro-oncological
