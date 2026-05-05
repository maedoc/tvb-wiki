# Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions

**Source**: arxiv
**ID**: 2605.02863
**URL**: https://arxiv.org/abs/2605.02863
**Date**: 2026-05-04
**Year**: 2026
**Authors**: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
**Categories**: cs.CV

## Abstract

Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
