---
created: 2026-04-24
sources:
  - https://github.com/voxelmorph/voxelmorph
  - https://doi.org/10.1109/TMI.2019.2897538
  - https://doi.org/10.1007/978-3-030-32245-8_7
tags:
- software-brain-modeling
- structural-connectivity
- connectomics
- neuroimaging-fmri
title: VoxelMorph
type: entity
updated: 2026-04-24
---

# VoxelMorph

## Overview

VoxelMorph is a deep learning framework for unsupervised deformable medical image registration. Developed by researchers at MIT CSAIL[^1][^2], it uses convolutional neural networks (CNNs) to learn a mapping between moving and fixed images, achieving registration in seconds—orders of magnitude faster than traditional optimization-based methods[^1]. The framework has become influential in neuroimaging preprocessing workflows and connectomics research.

## Key Features

### Deep Learning Architecture
VoxelMorph employs a U-Net convolutional neural network architecture[^2] to predict dense deformation fields. Given a pair of fixed and moving images, the network outputs a voxel-wise displacement field that warps the moving image to align with the fixed image. The architecture consists of an encoder-decoder pathway with skip connections, operating directly on 3D image volumes.

### Unsupervised Training
Unlike earlier deep learning approaches that required ground truth deformations, VoxelMorph trains in a fully unsupervised manner[^1][^2]. The loss function combines:
- **Image similarity**: Local normalized cross-correlation or mean squared error between registered pairs[^1]
- **Spatial smoothness**: Regularization on deformation field gradients to encourage smooth, physically plausible transformations[^1]

This unsupervised approach enables training on any unlabeled image dataset, dramatically expanding applicability.

### Diffeomorphic Transformation
The VoxelMorph-diff variant produces diffeomorphic (topology-preserving) registration by predicting a stationary velocity field rather than direct displacements[^3]. Through scaling-and-squaring integration—an iterative composition of velocity field exponentiation—velocity fields generate diffeomorphic deformations that preserve anatomical topology[^3]. This is critical for longitudinal studies and valid Jacobian analysis.

### Computational Efficiency
Traditional registration algorithms like [[ANTs]] SyN or [[FSL]] FNIRT require minutes to hours per image pair. VoxelMorph performs registration in under a second on GPU[^1][^2], enabling:
- Real-time registration during image acquisition
- Large-scale dataset processing
- Interactive visualization and quality control

## Software Availability

VoxelMorph is open-source software available under the Apache 2.0 license. The official implementation, including pre-trained models and training scripts, is maintained on GitHub at [voxelmorph/voxelmorph](https://github.com/voxelmorph/voxelmorph)[^1]. The repository includes:
- TensorFlow and PyTorch implementations
- Pre-trained models for brain MRI registration
- Atlas-based and template-building utilities
- Integration examples for common neuroimaging pipelines

The framework can be integrated as a preprocessing step in FreeSurfer workflows and is compatible with fMRIPrep-style processing pipelines for large-scale neuroimaging studies.

## Architecture Details

The standard U-Net architecture processes input image pairs through:
1. **Encoder**: Captures hierarchical features at multiple spatial scales
2. **Bottleneck**: Compact representation encoding spatial correspondence
3. **Decoder**: Upsamples to full-resolution deformation field
4. **Spatial Transformer**: Applies predicted warps using differentiable sampling[^2]

For diffeomorphic registration, the network predicts a velocity field $v$ that is integrated via scaling-and-squaring to produce the final deformation $\phi = \exp(v)$[^3]. This iterative integration ensures the resulting transformation is diffeomorphic—smooth, invertible, and topology-preserving.

## Relationship to TVB

VoxelMorph complements [[TVB]] workflows in several ways:

**Atlas Registration**: TVB simulations require anatomical parcellations aligned to subject space. VoxelMorph enables rapid registration of standard atlases (e.g., [[Desikan-Killiany Atlas|Desikan-Killiany]], [[AAL Atlas|AAL]]) to individual MRI volumes, generating region masks for connectome construction.

**Structural Connectivity Preprocessing**: For [[diffusion MRI]] tractography, accurate co-registration of T1-weighted and diffusion-weighted images is essential. VoxelMorph provides fast alignment for downstream [[structural connectivity]] matrix generation.

**Longitudinal Modeling**: TVB studies of disease progression (e.g., [[aging brain|aging]], [[Alzheimer's modeling|Alzheimer's]]) benefit from consistent anatomical correspondence across timepoints. The diffeomorphic variant ensures topology preservation during longitudinal registration.

**Population Templates**: Creating study-specific templates from large cohorts becomes feasible with VoxelMorph's speed, supporting cohort-wise [[connectomics]] analyses prior to TVB parameterization.

## Key Papers

- **Balakrishnan, G., Zhao, A., Sabuncu, M. R., Guttag, J., & Dalca, A. V. (2019).** "VoxelMorph: A Learning Framework for Deformable Medical Image Registration." *IEEE Transactions on Medical Imaging*, 38(8), 1788–1800. [https://doi.org/10.1109/TMI.2019.2897538](https://doi.org/10.1109/TMI.2019.2897538)[^1]

- **Balakrishnan, G., Zhao, A., Sabuncu, M. R., Guttag, J., & Dalca, A. V. (2018).** "An Unsupervised Learning Model for Deformable Medical Image Registration." *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 9252–9260. [https://openaccess.thecvf.com/content_cvpr_2018/html/Balakrishnan_An_Unsupervised_Learning_CVPR_2018_paper.html](https://openaccess.thecvf.com/content_cvpr_2018/html/Balakrishnan_An_Unsupervised_Learning_CVPR_2018_paper.html)[^2]

- **Dalca, A. V., Balakrishnan, G., Guttag, J., & Sabuncu, M. R. (2019).** "Unsupervised Learning for Fast Probabilistic Diffeomorphic Registration." *International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)*, 729–738. [https://doi.org/10.1007/978-3-030-32245-8_7](https://doi.org/10.1007/978-3-030-32245-8_7)[^3]

## Related Software

- [[ANTs]] — Traditional diffeomorphic registration (SyN algorithm); often used for comparison and validation
- [[FSL]] — Comprehensive neuroimaging suite with FLIRT/FNIRT registration tools
- [[FreeSurfer]] — Surface-based registration and cortical parcellation
- [[NiftyReg]] — GPU-accelerated traditional registration methods
- [[SynthSeg]] — Deep learning segmentation tool often paired with VoxelMorph in preprocessing pipelines
- [[Nibabel]] — Python library for neuroimaging I/O used in VoxelMorph workflows

## References

[^1]: Balakrishnan, G., Zhao, A., Sabuncu, M. R., Guttag, J., & Dalca, A. V. (2019). VoxelMorph: A Learning Framework for Deformable Medical Image Registration. *IEEE Transactions on Medical Imaging*, 38(8), 1788–1800. https://doi.org/10.1109/TMI.2019.2897538

[^2]: Balakrishnan, G., Zhao, A., Sabuncu, M. R., Guttag, J., & Dalca, A. V. (2018). An Unsupervised Learning Model for Deformable Medical Image Registration. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 9252–9260.

[^3]: Dalca, A. V., Balakrishnan, G., Guttag, J., & Sabuncu, M. R. (2019). Unsupervised Learning for Fast Probabilistic Diffeomorphic Registration. *International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)*, 729–738. https://doi.org/10.1007/978-3-030-32245-8_7