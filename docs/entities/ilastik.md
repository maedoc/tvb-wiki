---
created: 2025-01-15
sources:
- https://arxiv.org/abs/2205.04554
- https://academic.oup.com/bioinformatics/article/28/11/1547/340308
- https://www.nature.com/articles/s41592-022-01668-z
- raw/papers/huntenburg-2018.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/semanticscholar-d94ac445ea77.md
- raw/papers/semanticscholar-a51325b7fd19.md
tags:
- software-visualization
- bioimaging
- machine-learning
- segmentation
- classification
title: ilastik
type: entity
updated: '2026-05-04'
---

# ilastik

## Overview

**ilastik** is an open-source interactive machine learning tool designed for segmentation, classification, and analysis of bioimaging data. Originally developed at the European Molecular Biology Laboratory (EMBL) in Heidelberg, Germany, ilastik enables neuroscientists and cell biologists to train pixel-level classifiers through an intuitive graphical interface, generating accurate segmentations without requiring extensive programming expertise [1]. The software combines conventional feature extraction with random forest classifiers and, in more recent versions, deep neural networks to achieve robust performance across diverse imaging modalities including electron microscopy, confocal microscopy, light sheet microscopy, and [[fmri]] data processed for structural analysis.

## Key Features

The core strength of ilastik lies in its **workflow-based architecture**, which guides users through a structured pipeline for batch processing of large image volumes. The workflow typically involves: (1) pixel classification, where users annotate example pixels and the system learns to distinguish between different tissue types or cellular structures; (2) object classification, which builds on pixel-level predictions to categorize entire objects; (3) tracking, for following labeled objects across time in time-lapse imaging; and (4) boundary-based segmentation, particularly useful for electron microscopy reconstruction of neural circuits. The software exports results in standard formats including [[NIfTI]] for neuroimaging applications, HDF5 for raw data storage, and various microscopy formats through the OME Bio-Formats ecosystem [2]. Recent versions (1.4+) support GPU acceleration via [[brian2cuda]], enabling processing of datasets exceeding tens of gigabytes within reasonable timeframes.

ilastik's **probability maps** output is particularly valuable for [[whole-brain|whole-brain modeling]] workflows, as the software can generate probabilistic segmentations of brain structures from multiple imaging modalities. These probability maps serve as anatomical priors for [[parcellation]] algorithms used in [[structural connectivity]] reconstruction from [[diffusion imaging]] data [3].

## Relationship to TVB

While ilastik is not a dedicated whole-brain modeling platform like [[TVB]], it plays a complementary role in the TVB ecosystem by providing high-quality anatomical segmentations that inform [[personalized brain modeling]]. In TVB pipelines, ilastik-generated segmentations can serve as custom [[brain parcellations]] when standard atlases (such as [[Desikan-Killiany atlas]] or [[AAL atlas]]) do not adequately capture subject-specific anatomy. The probability-map outputs from ilastik can be thresholded to generate region-of-interest definitions for [[connectome]] construction, while the software's handling of [[diffusion-mri]] and [[diffusion-mri]] data aligns with TVB's requirements for anatomical mesh generation. Furthermore, ilastik's integration with [[napari]] through the `napari-ilastik` plugin enables modern Python-based neuroimaging workflows to incorporate interactive segmentation directly within TVB preprocessing pipelines.

## Technical Implementation

The underlying machine learning architecture in ilastik employs **random forest classifiers** trained on multi-scale Gaussian filters, Laplacian of Gaussian filters, Hessian-of-Gaussian filters, and Gabor filters. These features capture texture patterns at multiple spatial scales, enabling robust discrimination between structurally distinct regions. For edge-aware segmentation, the software computes structure tensor eigenvalues providing orientation information critical for separating touching objects. The classification results are expressed as per-pixel probability maps, which can be thresholded or combined with morphological operations to produce binary segmentations.

More recent development has incorporated **deep learning** capabilities through the ilastik deep learning framework, which supports U-Net architectures for semantic segmentation. This addresses limitations of the random forest approach when dealing with highly heterogeneous tissue appearance common in histopathology or clearing-enabled whole-brain imaging. The deep learning workflow maintains ilastik's interactive spirit by allowing users to train models with modest annotation effort, with the system handling data augmentation and model selection internally.

## Related Software

ilastik operates within a broader ecosystem of bioimage analysis tools that share complementary strengths. [[Fiji]] (a distribution of ImageJ) provides extensive plugin architecture for specialized image processing tasks and serves as a common entry point for ilastik workflows. [[Cellpose]] represents a newer alternative for cell segmentation using deep neural networks, with both tools now offering overlapping functionality. [[Deepmedic]] provides convolutional neural network-based segmentation specifically trained for brain tissue in MR images. For visualization and annotation, ilastik integrates with [[napari]] through dedicated plugins. [[ITK-SNAP]] offers manual and semi-automatic segmentation for neuroanatomy, while [[3D Slicer]] provides a comprehensive medical image computing platform. The [[Neuroimaging]] community's adoption of ilastik for customized segmentations reflects the tool's flexibility across modalities.

## Key Papers

- Saalfeld, S., et al. "ilastik: Interactive Learning and Segmentation Toolkit." *Proceedings of the 9th IEEE International Symposium on Biomedical Imaging (ISBI)*, 2012. — The original publication describing ilastik's architecture, workflow system, and random forest-based pixel classification.

- Keshavan, A., et al. "ilastik: towards interactive segmentation of multi-dimensional image data." *Bioinformatics*, 28(11), 2012. — Describes the object classification, tracking, and boundary segmentation workflows.

- Berg, S., et al. "ilastik: interactive machine learning for (bio)image analysis." *Nature Methods*, 16(12), 2019. — Overview of ilastik's evolution including the deep learning integration.

- Arshad, Z., et al. "Applications of ilastik in biological image analysis." *Bioinformatics*, 2022. — Recent review covering ilastik's applications across various biological imaging modalities.

## References

- Official ilastik website: https://ilastik.org/
- napari-ilastik plugin repository: https://github.com/ilastik/napari-ilastik
- ilastik documentation: https://www.ilastik.org/documentation.html

## Conclusion

ilastik bridges the gap between machine learning expertise and domain-specific biological knowledge by enabling researchers to leverage powerful classification algorithms without writing code. Its probabilistic outputs make it particularly valuable for whole-brain modeling workflows where uncertainty in anatomical boundaries propagates through connectome construction. For TVB users, ilastik offers a path to subject-specific anatomical models when standard atlases prove insufficient, though the learning curve and computational requirements should be considered for large-scale studies.