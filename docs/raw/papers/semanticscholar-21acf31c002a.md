# DGLA-Net: Robust MRI-PET Fusion Method Based on Deep Global-Local Attention and Multi-Scale Supervision

**Source**: semantic-scholar
**ID**: 21acf31c002a126009552a8c15ddb56e31d4dd35
**DOI**: 10.1109/ISCAIT69154.2026.11477440
**URL**: https://www.semanticscholar.org/paper/21acf31c002a126009552a8c15ddb56e31d4dd35
**Date**: 2026-01-23
**Year**: 2026
**Authors**: Ruicheng Liu
**Venue**: 2026 5th International Symposium on Computer Applications and Information Technology (ISCAIT)
**Citations**: 0

## Abstract

MRI-PET image fusion aims to integrate anatomical and functional information, which is crucial for precise diagnosis. However, existing deep learning methods struggle to balance texture details with functional fidelity, often facing bottlenecks such as difficulty in bridging the semantic gap, interference from background noise, and the blurring of critical lesions. This paper proposes an improved model, DGLA-Net, based on the UNet++ architecture and a dual robust information fusion attention mechanism (DGLA), aimed at optimizing fusion performance through deep global-local attention. The model utilizes a Nested UNet (UNet++) as the backbone architecture, leveraging its dense nested skip connections to effectively bridge the semantic gap between the encoder and decoder, thereby preserving multi-scale anatomical structural features to the maximum extent. Building on this, the core innovations include three aspects: First, a Deep Global-Local Attention (DGLA) module is designed to be highly compatible with UNet++ multi-level feature paths. By coupling global pooling with local convolution operations, it realizes dynamic screening and interaction of cross-modal features, balancing global context dependency with local texture details. Second, a Residual Denoising Spatial Attention (RDSA) module is introduced, utilizing residual connection mechanisms to strengthen deep feature extraction capabilities and effectively suppress background noise in functional images. Finally, an Adaptive Hybrid Loss function is constructed, synergistically integrating gradient loss, SSIM loss, and PET saliency-weighted intensity loss. Extensive experiments on MRI-PET multi-modal datasets demonstrate that DGLA-Net significantly outperforms existing state-of-the-art fusion algorithms. Compared to other models, DGLA-Net not only retains brain anatomical contours more clearly but also locates tumor metabolic regions more precisely through attention heatmaps, effectively achieving an optimal balance between structural fidelity and functional saliency, demonstrating excellent potential for clinical application.
