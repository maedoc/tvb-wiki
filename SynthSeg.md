---
title: SynthSeg
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [neuroimaging, neuroimaging-mri, software-tools, deep-learning, segmentation, brain-parcellations, synthseg, mri-processing, fastsurfer, freesurfer]
sources: [https://github.com/BBillot/SynthSeg, https://www.sciencedirect.com/science/article/pii/S1361841523000506, https://www.pnas.org/doi/full/10.1073/pnas.2216399120]
---

# SynthSeg

## Overview

SynthSeg is a deep learning-based framework for automatic segmentation of brain magnetic resonance imaging (MRI) scans that operates without any task-specific training data. Originally developed by Benjamin Billot and colleagues at the Martinos Center for Biomedical Imaging, Massachusetts General Hospital and Harvard Medical School (in collaboration with University College London and Technical University of Denmark), SynthSeg uses a domain adaptation approach whereby a neural network is trained exclusively on synthetic data and then generalizes to real brain images without fine-tuning [[1]]. The framework achieved state-of-the-art performance on diverse MRI contrasts including T1-weighted, T2-weighted, FLAIR, and others, demonstrating remarkable robustness to acquisition parameters, scanner types, and pathological variations [[1]]. Unlike traditional segmentation methods that require manually annotated training datasets, SynthSeg leverages a generative model to create unlimited labeled training examples, bypassing one of the most labor-intensive bottlenecks in medical image analysis. The published implementation processes scans rapidly (typically under one minute per volume on GPU), making it suitable for large-scale dataset processing [[1]].

## Motivation and Context

The segmentation of brain structures from MRI scans is a fundamental preprocessing step in virtually every neuroimaging study, serving as the foundation for volume quantification, parcellation-based connectivity analysis, and morphological measurements [[1]]. However, existing segmentation tools such as [freesurfer], [fastsurfer], and [segmentation] approaches relying on atlases like [desikan-killiany-atlas] or [destrieux-atlas] require substantial training datasets with manual annotations—an expensive and time-consuming endeavor. Furthermore, these methods often degrade when applied to data from scanners or protocols outside their training distribution.

SynthSeg addresses these limitations through a synthetic training approach. The method generates training data using a realistic anatomical model that produces varied brain geometries, which are then rendered with random MR imaging contrasts using a physics-based simulator. By training on this unlimited synthetic dataset, the network learns segmentation features that transfer effectively to real clinical and research scans. This approach also provides a principled solution to privacy concerns surrounding patient data, as no real medical images are used during training. The work emerged from research at Massachusetts General Hospital and Harvard Medical School (the FreeSurfer lab), building on foundational contributions to deep learning in medical imaging and representing a broader trend toward self-supervised and domain adaptation techniques in neuroimaging [[1]].

## Technical Approach

SynthSeg employs a convolutional neural network with a U-Net architecture that takes an MRI scan as input and produces dense per-voxel segmentations. The key innovation lies in its training paradigm: rather than learning from labeled real images, the network learns from synthetic brain scans generated through a stochastic anatomical model combined with an MRI simulation pipeline. The anatomical model randomly samples parameters governing sulcal patterns, ventricular size, brain shape, and tissue properties, while the MRI simulator emulates physical acquisition effects including relaxation times, flip angles, and noise profiles [[1]].

During training, the network optimizes a segmentation loss between predicted and synthetic labels. Critically, the authors demonstrated that the learned features generalize across contrasts—a single model trained on synthetic T1, T2, FLAIR, and PD scans achieves high accuracy on all corresponding real acquisitions. The framework also incorporates a domain-agnostic uncertainty quantification mechanism that estimates segmentation confidence on a per-structure basis, enabling downstream quality control in research pipelines [[1]].

## Key Features

SynthSeg provides several capabilities that distinguish it from conventional segmentation tools. First, it operates without any task-specific labeled data, eliminating the need for costly manual annotations. Second, the same network handles multiple MRI contrasts, reducing the need for contrast-specific models. Third, the framework processes scans rapidly (typically under one minute per volume on GPU, and as fast as 15 seconds with optimization), making it suitable for large-scale dataset processing [[1]]. Fourth, it segments a standard set of cortical and subcortical structures comparable to [freesurfer]'s output, enabling integration with downstream tools that expect these parcellation schemas. Finally, the published implementation includes both a command-line interface and Python API, facilitating integration into neuroimaging processing pipelines built on frameworks like [nilearn] or [nipype].

## Relationship to Whole-Brain Modeling

In the context of whole-brain modeling, accurate anatomical segmentations are essential for constructing subject-specific brain networks. Parcellations generated by tools like SynthSeg define the nodes of connectome-based models, providing the regional boundaries from which [structural-connectivity] matrices are derived or onto which [functional-connectivity] patterns are mapped. The ability to rapidly generate consistent segmentations across heterogeneous datasets supports the development of personalized brain models, a key goal in initiatives like the [human-connectome-project] and efforts toward [personalized-brain-modeling]. Furthermore, SynthSeg's capacity to handle pathological brains makes it particularly valuable for clinical populations studied in [epilepsy-modeling] and [alzheimers-modeling] applications, where scanner variability and atypical anatomy challenge conventional approaches. The robustness to white matter lesions and ability to process scans without preprocessing further enhance its utility for clinical neuroimaging studies [[2]].

## Key Papers

The following publications are essential references for understanding and citing SynthSeg:

- **Billot et al. (2023)**: "SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining" — Medical Image Analysis. The original paper presenting the core SynthSeg methodology, demonstrating contrast and resolution invariance without fine-tuning [[1]].

- **Billot et al. (2023)**: "Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets" — Proceedings of the National Academy of Sciences (PNAS). This follow-up work (SynthSeg+) extends the framework to include cortical parcellation, automated quality control, and intracranial volume estimation, with demonstrations on over 14,000 clinical scans [[2]].

- **Iglesias et al. (2023)**: "SynthSR: A public AI tool to turn heterogeneous clinical brain scans into high-resolution T1-weighted images for 3D morphometry" — Science Advances. Related work on super-resolution synthesis of clinical scans, complementing SynthSeg's segmentation capabilities.

## Related Software

SynthSeg builds upon and relates to several established neuroimaging tools in the ecosystem. It performs a similar function to [freesurfer], the most widely used cortical reconstruction software, but without training data requirements. Compared to [fastsurfer], which accelerates freesurfer processing through deep learning while retaining the same anatomical model, SynthSeg takes a fundamentally different training approach. Other related segmentation tools include [brainsuite], [mindboggle], and [cat12], each offering distinct feature sets. For preprocessing, SynthSeg often complements tools like [fsl], [ants], and [elastix] that handle registration and normalization, while output segmentations may be visualized using [freesurfer]'s [freeview] or general neuroimaging viewers like [fsleyes].

## References

[1] Billot B, Greve DN, Puonti O, Thielscher A, Van Leemput K, Fischl B, Dalca AV, Iglesias JE. SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining. Medical Image Analysis. 2023;86:102789.

[2] Billot B, Colin M, Cheng Y, Arnold SE, Das S, Iglesias JE. Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. Proceedings of the National Academy of Sciences. 2023;120(9):e2216399120.