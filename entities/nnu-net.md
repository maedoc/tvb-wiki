---
created: 2026-04-20
sources:
- Isensee, F., Jaeger, P. F., Kohl, S. A. A., et al. (2021). nnU-Net: Self-adapting
    framework for U-Net-based medical image segmentation. Nature Methods, 18(2), 183-188.
- Antonelli, M., Reinke, A., Bakas, S., et al. (2022). The Medical Segmentation Decathlon.
  Nature Scientific Data, 9(1), 139.
- Ronneberger, O., Fischer, P., & Brox, T. (2015). U-Net: Convolutional networks for
    biomedical image segmentation. International Conference on Medical Image Computing
    and Computer-Assisted Intervention (MICCAI), 234-241.
- Çiçek, Ö., Abdulkadir, A., Lienkamp, S. S., et al. (2016). 3D U-Net: Learning dense
    volumetric segmentation from sparse annotation. International Conference on Medical
    Image Computing and Computer-Assisted Intervention (MICCAI), 424-432.
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/semanticscholar-a51325b7fd19.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-visualization
- neural-network
- neuroimaging
title: nnU-Net
type: entity
updated: '2026-05-04'
---

nnU-Net (No New U-Net) is a self-configuring deep learning framework for medical image segmentation that automatically adapts its network architecture, preprocessing pipelines, and training hyperparameters to any given dataset without manual intervention [[Isensee et al., 2021]](). Originally introduced by Isensee et al. in 2021, nnU-Net emerged from the observation that architectural innovations in U-Net variants often provide marginal improvements over well-tuned baseline architectures [[Ronneberger et al., 2015]](), leading the authors to focus instead on systematic optimization of the training pipeline itself. The framework has become one of the most widely adopted tools for automated segmentation in neuroimaging, particularly for tasks involving MR, CT, and other volumetric medical imaging modalities.

## Motivation and Context

Medical image segmentation traditionally required substantial expert knowledge to design appropriate preprocessing pipelines, select network architectures, and tune hyperparameters for each new dataset. This process was not only time-consuming but also often produced suboptimal results because the optimal configuration depends heavily on properties of the imaging modality, the anatomical structures of interest, and the specific characteristics of the dataset such as resolution, contrast, and signal-to-noise ratio. nnU-Net addresses this challenge by treating the configuration problem as a optimization task: the framework automatically analyzes the properties of the input dataset and determines the optimal preprocessing (e.g., voxel spacing normalization, intensity normalization), patch-based training strategy, network topology (encoder-decoder depth, number of feature channels), and training schedule (learning rate, batch size, data augmentation) [[Isensee et al., 2021]]().

The name "No New U-Net" reflects the authors' deliberate choice to avoid introducing novel architectural components, instead demonstrating that careful optimization of existing U-Net principles yields competitive or superior performance compared to more complex architectures [[Ronneberger et al., 2015]](). This philosophy proved remarkably effective: nnU-Net achieved state-of-the-art results in multiple segments of the Medical Segmentation Decathlon challenge [[Antonelli et al., 2022]]() and has since become a standard baseline in medical image segmentation research. The framework's success lies in its robust handling of the inherent variability across medical imaging datasets, from brain MRI to cardiac CT to abdominal organ segmentation.

## Technical Framework

nnU-Net's configuration pipeline operates through a series of dataset analysis [[steps]]. First, the framework extracts intrinsic properties of the training data, including the voxel spacing distribution, intensity histograms, and anatomical priors. Based on these properties, it automatically determines target voxels per dimension, selects appropriate intensity normalization strategies (e.g., z-score normalization for MR, clipping and scaling for CT), and configures patch-based training to handle datasets that exceed GPU memory constraints. The network architecture itself is parameterized by rules that map dataset properties to architectural choices: for example, smaller voxel spacings typically require deeper networks with more pooling stages to capture sufficient receptive field, while anisotropic data triggers specific adaptations in the decoder path [[Isensee et al., 2021]]().

The training process incorporates extensive data augmentation including random rotations, scaling, elastic deformations, gamma corrections, and mirroring operations. nnU-Net employs a combination of dice loss and cross-entropy loss to handle class imbalance, which is prevalent in medical imaging where foreground structures often occupy small fractions of the total volume. The framework uses a five-fold cross-validation scheme to estimate validation performance and selects the best-performing fold for inference [[Isensee et al., 2021]](). During testing, test-time augmentation (TTA) applies multiple augmented inference passes and averages the results to improve segmentation robustness.

## Relationship to Other Frameworks

nnU-Net shares conceptual foundations with other deep learning segmentation frameworks while distinguished by its automation philosophy. Unlike earlier frameworks such as [[deepmedic]] that require substantial manual configuration, or general-purpose platforms like [[tensorflow]] and [[neural-network]] that provide only low-level primitives, nnU-Net offers an end-to-end solution that can be applied with minimal user input. The framework complements rather than replaces toolkits like [[ants]] for image registration and preprocessing, and integrates with broader neuroimaging ecosystems including [[nilearn]] and [[nibabel]] for loading and processing neuroimaging data in [[niftynet]] and [[nifti]] formats.

Compared to architectural innovations like attention U-Net or residual U-Net [[Çiçek et al., 2016]](), nnU-Net demonstrates that systematic pipeline optimization often delivers comparable performance with reduced complexity. This approach has influenced subsequent work in self-configuring medical imaging systems and has established nnU-Net as a robust default choice for new segmentation tasks in both research and clinical contexts. The framework also serves as a strong baseline against which novel architectural contributions are compared in the medical imaging literature.

## Applications in Neuroimaging

Within the neuroimaging domain, nnU-Net has been applied to segment brain structures from MR images, including whole-brain parcellation, white matter hyperintensity segmentation, and tumor segmentation in neuro-oncology datasets [[Isensee et al., 2021]](). The framework's ability to handle multi-site data with varying acquisition parameters makes it particularly valuable for analyzing large neuroimaging cohorts such as those from the [[human-connectome-project]] or [[uk-biobank]], where scanner and protocol heterogeneity poses challenges for manual pipeline design. nnU-Net's segmentations feed downstream analyses in [[connectome]] construction, [[structural-connectivity]] estimation via [[tractography]], and morphometric analyses using tools like [[freesurfer]].

## See Also

* [[deepmedic]] — Related deep learning segmentation framework for neuroimaging
* [[niftynet]] — Neural network platform originally developed for medical imaging
* [[neural-network]] — Broader class of artificial neural networks
* [[neuroimaging]] — Overview of imaging modalities used in neuroscience
* [[nilearn]] — Python library for neuroimaging data analysis
* [[nibabel]] — Python library for reading neuroimaging file formats
* [[freesurfer]] — Tool for automated segmentation of brain structures
* [[human-connectome-project]] — Large neuroimaging dataset initiative
* [[connectome]] — Framework for mapping brain [[connectivity]]
* [[tractography]] — Fiber tracking methodology for structural connectivity