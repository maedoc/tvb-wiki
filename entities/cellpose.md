---
created: 2025-01-15
sources:
- raw/papers/Renton2024.md
- raw/papers/semanticscholar-d94ac445ea77.md
- raw/papers/sanz-leon-2013.md
tags:
- software-visualization
- neuroimaging-microscopy
- deep-learning
- image-segmentation
- neuroinformatics
title: Cellpose
type: entity
updated: '2026-05-04'
---

# Cellpose

## Overview

Cellpose is a deep learning-based algorithm for automated segmentation of cells, nuclei, and other subcellular structures in microscopy images. Originally developed by Carsen Stringer and Marius Pachitariu at Janelia Research Campus and published in *Nature Methods* (2020)[^1], Cellpose has become a widely adopted tool in [[computational-neuroscience]], neuroinformatics, and biomedical image analysis pipelines. In 2022, the team released Cellpose 2.0[^2], which introduced specialist models and a model zoo for improved performance on specific cell types. Unlike traditional threshold-based or watershed segmentation methods, Cellpose leverages a convolutional [[neural-network]] trained on thousands of annotated cell images to robustly segment structures across diverse cell types, imaging modalities, and experimental conditions. The algorithm takes as input 2D or 3D grayscale microscopy images (e.g., confocal, two-photon, Lightsheet) and outputs binary masks delineating individual cells or nuclei, along with flow vectors that can be used for subsequent tracking or analysis.

## Motivation and Context

Automated cell segmentation has historically been a major bottleneck in high-throughput microscopy analysis pipelines. Traditional methods such as Otsu thresholding, watershed segmentation, or active contours require extensive manual parameter tuning and often fail when confronted with heterogeneous cell populations, touching cells, or variable image quality. The emergence of deep learning approaches promised improved robustness, but early implementations required substantial labeled data and expertise to train. Cellpose addressed these challenges by providing a pre‑trained, generalist model that achieves high accuracy across diverse cell types without requiring users to collect their own training data—a paradigm that proved transformative for the neuroimaging and microscopy communities. In the context of [[whole-brain|whole-brain modeling]] and computational neuroscience, Cellpose enables quantitative analysis of cellular populations in histological sections, enabling researchers to extract cellular density distributions, morphometric features, and spatial statistics that can inform [[whole-brain-modeling]] approaches or parameterize [[neural-mass-models]] at the cellular level.

## Technical Approach

Cellpose employs a U‑net style architecture with several innovative modifications. The network takes as input a grayscale image and outputs two outputs: pixel‑wise cell probability masks and pixel‑wise flow vectors pointing toward the center of each cell. The flow field representation allows the algorithm to handle touching or overlapping cells by providing a gradient that separates adjacent cellular boundaries. During training, Cellpose uses a combination of a dice loss for segmentation accuracy and a flow loss that encourages correct vector fields, enabling end‑to‑end optimization. Importantly, the pre‑trained Cellpose model was trained on a curated dataset of over 70,000 segmented cells across diverse labels, giving it zero‑shot generalization to new cell types[^1]. For specialized applications, users can fine‑tune the model on small custom datasets using the built‑in training interface. The algorithm runs efficiently on both CPU and GPU, with typical inference times of 1–2 seconds per 512×512 image on modern hardware.

## Key Features

Cellpose offers several features that have contributed to its widespread adoption in neuroimaging pipelines. First, the pre‑trained model handles diverse cell types—including neurons, glia, and various subcellular organelles—without requiring user‑provided training data. Second, the algorithm supports both 2D and 3D image stacks, enabling volumetric analysis of tissue sections. Third, Cellpose provides a Python API (`cellpose` package) for integration into automated pipelines, alongside a [[Fiji]] plugin for interactive use. Fourth, the model includes a diameter estimation step that automatically determines the characteristic size of cells in the input images, reducing the need for manual parameter specification. Fifth, Cellpose can be combined with downstream analysis tools such as [[napari]] for visualization or custom scripts for morphometric measurement. The algorithm has been validated against manual segmentations across multiple datasets, demonstrating better to previous approaches in both accuracy and generalization.

## Relationship to TVB

While Cellpose is primarily a tool for microscopy image analysis rather than a whole‑brain simulator, it relates to [[The Virtual Brain]] (TVB) in several indirect ways. In personalized [[whole-brain-modeling]] pipelines, cellular‑level anatomical data derived from histological segmentation—including regional cell density estimates, layer‑specific cell counts, and morphological statistics—can inform the parameterization of [[neural-mass-models]] or [[connectomics]]‑based connectivity matrices. Cellpose may be used to extract such metrics from postmortem brain tissue or experimental animal models, enabling researchers to build more biophysically detailed models. Additionally, researchers using [[brainvoyager]], [[freesurfer]], or other [[neuroimaging]] tools to analyze cellular‑resolution imaging data may incorporate Cellpose into their preprocessing workflows. The tool exemplifies the growing integration of deep learning methods from computer vision into the broader neuroinformatics ecosystem that supports whole‑brain computational modeling.

## Key Papers

1. Stringer, C., & Pachitariu, M. (2020). Cellpose: a generalist algorithm for cellular segmentation. *Nature Methods*, 18(1), 100‑106.[^1]
2. Stringer, C., Wang, T., Michaelos, M., & Pachitariu, M. (2022). Cellpose 2.0: software for robust segmentation of cell dynamics across experiments. *Nature Methods*, 19(11), 1440‑1448.[^2]

## Related Software

Cellpose belongs to a broader ecosystem of segmentation and analysis tools for microscopy images. [[Ilastik]] provides interactive machine learning segmentation with a complementary approach to Cellpose. [[Suite2p]] offers a complete pipeline for calcium imaging analysis including cell detection, registration, and spike extraction. [[DeepMediC]] represents another deep learning framework for medical image segmentation. [[Fiji]] (a distribution of ImageJ) provides the plugin infrastructure for running Cellpose interactively. [[Napari]] serves as a common visualization platform for Cellpose outputs. [[Neuron]] and related neuronal reconstruction tools address the complementary problem of tracing axonal and dendritic arbors from microscopy data. Researchers interested in cell tracking over time may combine Cellpose with [[Suite2p]] or custom tracking algorithms to generate longitudinal measurements of cellular dynamics.

## References

1. (authors unknown). *[[neurodesk]]: an accessible, flexible and portable data analysis environment for reproducible neuroimaging*.
2. Maya Iratni, Amirali Abdullah, Mariam Aldhaheri, Omar Elharrouss, Alaa A. Abd-alrazaq, Zahiriddin Rustamov, Nazar Zaki, Rafat Damseh. (2025). *Transformers for Neuroimage Segmentation: Scoping Review*. Journal of Medical Internet Research. [DOI](https://doi.org/10.2196/57723)
3. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)