# Hyper-Connections for Adaptive Multi-Modal MRI Brain Tumor Segmentation

**arXiv ID**: 2603.19844
**Published**: 2026-03-20
**Updated**: 2026-03-26
**Authors**: Lokendra Kumar, Shubham Aggarwal
**Categories**: cs.CV
**URL**: https://arxiv.org/abs/2603.19844
**PDF**: https://arxiv.org/pdf/2603.19844
**Source**: arXiv

## Abstract

We present the first study of Hyper-Connections (HC) for volumetric multi-modal brain tumor segmentation, integrating them as a drop-in replacement for fixed residual connections across five architectures: nnU-Net, SwinUNETR, VT-UNet, U-Net, and U-Netpp. Dynamic HC consistently improves all 3D models on the BraTS 2021 dataset, yielding up to +1.03 percent mean Dice gain with negligible parameter overhead. Gains are most pronounced in the Enhancing Tumor sub-region, reflecting improved fine-grained boundary delineation. Modality ablation further reveals that HC-equipped models develop sharper sensitivity toward clinically dominant sequences, specifically T1ce for Tumor Core and Enhancing Tumor, and FLAIR for Whole Tumor, a behavior absent in fixed-connection baselines and consistent across all architectures. In 2D settings, improvements are smaller and configuration-sensitive, suggesting that volumetric spatial context amplifies the benefit of adaptive aggregation. These results establish HC as a simple, efficient, and broadly applicable mechanism for multi-modal feature fusion in medical image segmentation.
