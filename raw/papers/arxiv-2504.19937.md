# SST-DUNet: Automated preclinical functional MRI skull stripping using Smart Swin Transformer and Dense UNet

**Source**: semantic-scholar
**ID**: 09f39222827511da7c9384e45767eb5e28377a77
**DOI**: 10.48550/arXiv.2504.19937
**URL**: https://www.semanticscholar.org/paper/09f39222827511da7c9384e45767eb5e28377a77
**Date**: 2025-02-27
**Year**: 2025
**Authors**: Sima Soltanpour, Rachel Utama, Arnold Chang, Md Taufiq Nasseef, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Skull stripping is a common preprocessing step that is often performed manually in Magnetic Resonance Imaging (MRI) pipelines, including functional MRI (fMRI). This manual process is time-consuming and operator dependent. Automating this process is challenging for preclinical data due to variations in brain geometry, resolution, and tissue contrast. While existing methods for MRI skull stripping exist, they often struggle with the low resolution and varying slice sizes in preclinical fMRI data. This study proposes a novel method called SST-DUNet, that integrates a dense UNet-based architecture with a feature extractor based on Smart Swin Transformer (SST) for fMRI skull stripping. The Smart Shifted Window Multi-Head Self-Attention (SSW-MSA) module in SST is adapted to replace the mask-based module in the Swin Transformer (ST), enabling the learning of distinct channel-wise features while focusing on relevant dependencies within brain structures. This modification allows the model to better handle the complexities of fMRI skull stripping, such as low resolution and variable slice sizes. To address the issue of class imbalance in preclinical data, a combined loss function using Focal and Dice loss is utilized. The model was trained on rat fMRI images and evaluated across three in-house datasets with a Dice similarity score of 98.65%, 97.86%, and 98.04%. The fMRI results obtained through automatic skull stripping using the SST-DUNet model closely align with those from manual skull stripping for both seed-based and independent component analyses. These results indicate that the SST-DUNet can effectively substitute manual brain extraction in rat fMRI analysis.
