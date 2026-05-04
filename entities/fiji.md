---
created: 2025-01-15
sources:
- raw/papers/Renton2024.md
tags:
- software-visualization
- neuroimaging
- software-neuroimaging
title: Fiji
type: entity
updated: '2026-05-04'
---

# Fiji

## Overview

Fiji (Fiji Is Just ImageJ) is an open-source image processing platform that extends ImageJ2 with a curated collection of plugins and libraries for scientific image analysis. Originally developed by Johannes Schindelin and colleagues at the Max Planck Institute of Molecular Cell Biology and Genetics (MPI-CBG), Fiji has become a cornerstone tool in neuroscience laboratories worldwide for preprocessing, visualizing, and analyzing [[neuroimaging]] data including MRI, [[fmri]], and diffusion tensor imaging datasets [[schindelin2012fiji]]. The platform is written in Java and runs on all major operating systems, providing a consistent graphical user interface for tasks ranging from basic image viewing to complex automated segmentation workflows.

## Key Features

Fiji's architecture centers on a plugin-based extension system that allows researchers to install and manage specialized functionality through a built-in updater. The distribution includes over 300 pre-bundled plugins covering virtually every common image processing operation—filters, segmentations, registration, feature detection, and morphological operations [[schindelin2012fiji]]. Of particular relevance to [[whole-brain|whole-brain modeling]] is the **ImageJ-OPS** library, which provides standardized operations for image processing pipelines, and the **AnalyzeSkeleton** plugin for analyzing morphological skeletons of neurons or vascular networks.

For neuroimaging specifically, Fiji integrates with several key file formats through plugins like **Bio-Formats**, which supports reading over 150 file formats including DICOM (the standard clinical imaging format), [[nifti]] (common in neuroscience research), and various scanner-specific formats [[bioformats]]. The platform can handle 3D and 4D image stacks, making it suitable for analyzing fMRI time series data and [[diffusion-mri]] [[tractography]] results. Researchers can also leverage Fiji's scripting capabilities (via ImageJ Macro, Python via pyimagej, or BeanShell) to automate repetitive preprocessing [[steps]] in their whole-brain modeling pipelines.

The **Trainable Weka Segmentation** plugin deserves special mention for neuroscience applications—it provides a machine learning-based approach to segmenting brain structures, white matter lesions, or other anatomical features without requiring extensive programming expertise [[weka]]. Combined with **Interactive Annotations** and **MorphoLibJ** (for mathematical morphology operations), Fiji enables rapid prototyping of segmentation workflows that may later be ported to more automated pipeline frameworks like [[snakemake]] or [[nipype]].

## Relationship to TVB

While Fiji is not a neural simulation environment itself, it plays an important supporting role in The Virtual Brain ([[TVB]]) workflows by facilitating the preprocessing and quality control of neuroimaging data used to construct personalized brain models. Researchers typically use Fiji to inspect and segment structural MRI scans for [[personalized-brain-modeling]] applications, where anatomical parcellations derived from tools like [[freesurfer]] or [[fsl]] may be refined using Fiji's interactive tools. The software also serves as a visual inspection tool for reviewing [[structural-connectivity]] matrices derived from [[diffusion-imaging]] tractography, allowing researchers to verify fiber tracking results before input to TVB's connectome construction pipeline.

In practice, a typical TVB preprocessing pipeline might involve: (1) acquiring raw T1-weighted MRI and diffusion MRI scans, (2) performing initial brain extraction and bias correction using [[fsl]] bet or [[ants]], (3) importing results into Fiji for visual quality control and manual intervention if needed, and (4) exporting processed images to TVB for forward modeling. This hybrid approach leverages Fiji's interactivity for tasks requiring human judgment while automating computationally intensive operations in dedicated tools.

## Relationship to Other Imaging Software

Fiji occupies a unique niche in the neuroimaging software ecosystem that complements rather than competes with other tools. Unlike dedicated neuroimaging packages like [[fsl]], [[freesurfer]], or [[spm]], Fiji is not specialized for any particular modality but instead provides general-purpose image processing applicable across MRI, histology, microscopy, and other imaging domains. This generality makes it especially valuable for researchers working across multiple imaging modalities or developing novel analysis approaches.

Compared to 3D visualization tools like [[3d-slicer]] or [[itk-snap]], Fiji emphasizes 2D slice-by-slice viewing and batch processing more than 3D rendering, though it does support basic 3D visualization through plugins like the **3D Viewer** [[schindelin2012fiji]]. The relationship with [[itk]] (Insight Toolkit) is particularly significant—Fiji's **elastix** plugin integrates the elastix registration library (also used by [[ants]]), enabling sophisticated affine and non-linear registration within Fiji's interface. For researchers needing more advanced 3D visualization, Fiji often serves as a preprocessing companion to these specialized viewers rather than a replacement.

## Key Capabilities for Whole-Brain Modeling

Fiji contributes to whole-brain modeling workflows in several concrete ways that researchers should be aware of. First, **quality control**: before feeding any neuroimaging data into a brain model, researchers need to verify that preprocessing steps succeeded—Fiji provides quick visual inspection of brain masks, registration quality, and segmentations. Second, **manual annotation**: when automated segmentations fail (as they often do in pathological brains), Fiji's precise drawing tools allow researchers to manually edit regions of interest. Third, **custom measurements**: the platform's measurement tools can extract region volumes, intensities, or morphological statistics that inform brain model parameters. Fourth, **pipeline prototyping**: researchers developing novel preprocessing approaches often prototype these in Fiji before implementing them in production pipelines.

## Key Papers

- Schindelin, J., Arganda-Carreras, I., Frise, E., Kaynig, V., Longair, M., Pietzsch, T., ... & Cardona, A. (2012). Fiji: an open-source platform for biological-image analysis. *Nature Methods*, 9(7), 676-682. [[schindelin2012fiji]]
- Ackermann, M. & Schindelin, J. (2014). ImageJ2: An extensible Java library for scientific image analysis. *Nature Methods*, 11(8), 805-806. [[imagej2]]
- Linkert, M., Rueden, C.T., Allan, C., Burel, J.M., Moore, W., Patterson, A., ... & Carpenter, A.E. (2010). Bio-Formats: an open-source software for managing microscopy image format data. *Bioinformatics*, 26(7), 932-939. [[bioformats]]
- Arganda-Carreras, I., Kaynig, V., Rueden, C., Eliceiri, K.W., Schindelin, J., Cardona, A., & Sebastian, H. (2017). Trainable Weka Segmentation: a machine learning tool for microscopy image classification. *Nature Methods*, 14(2), 122-123. [[weka]]

## Related Software

- [[itk-snap]] — specialized 3D neuroimaging viewer and editor
- [[3d-slicer]] — comprehensive medical image computing platform
- [[fsl]] — comprehensive neuroimaging analysis suite
- [[freesurfer]] — cortical reconstruction and [[parcellation]]
- [[nipype]] — Python pipeline framework for neuroimaging
- [[spm]] — statistical parametric mapping toolbox

## References

1. (authors unknown). *Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging*.