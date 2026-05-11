---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-visualization
- neuroimaging
- neuroimaging-fmri
- neuroimaging-dti
- python
title: Napari
type: entity
updated: '2026-05-11'
---

## Overview

Napari is a fast, interactive, and extensible multi-dimensional image viewer built in Python. It provides a graphical user interface for exploring large scientific datasets—particularly those common in [[neuroimaging]] such as volumetric MRI scans, diffusion tensor images, and [[connectome]] matrices—without requiring users to write extensive visualization code. Napari is designed to bridge the gap between lightweight quick-look tools and full-featured desktop applications, offering layer-based visualization, plugin extensibility, and integration with the broader scientific Python ecosystem including NumPy, scikit-image, and [[nilearn]]. Originally developed with support from the Chan Zuckerberg Initiative and emerging primarily from the microscopy and biomedical imaging communities, napari has become a widely adopted tool for visualizing brain imaging data across modalities.

## Motivation and Context

Neuroimaging research produces massive datasets: a single [[fMRI]] run can generate hundreds of gigabytes of volumetric time-series data, while [[diffusion-imaging]] tractography produces complex 3D streamline representations that strain conventional viewers. Traditional tools like Fsl's fsleyes or Freesurfer's [[freeview]] are powerful but limited to specific file formats and workflows. Meanwhile, general-purpose image viewers lack the domain-specific features neuroscientists need—support for [[nifti]] headers, atlas overlays, and connectivity matrices.

Napari emerged to address this gap by providing a performant, Python-native viewer that accepts any NumPy array as input. This means researchers can load preprocessed data directly from [[nipype]] pipelines, visualize outputs from tractography tools like [[mrtrix3]] or [[dipy]], or render custom analyses without data conversion. The plugin architecture also allows developers to add domain-specific functionality—plugins have been developed for brain atlases, electrode localization, and various neuroscience visualization needs.

## Key Features

Napari's architecture centers on a layer-based system where each layer represents a different type of data: image layers for volumetric data, points layers for electrode coordinates or [[neuron]] positions, shapes layers for regions of interest, and labels layers for segmentations. This design supports simultaneous visualization of diverse data types—a common need in [[whole-brain|whole-brain modeling]] where one might overlay [[structural-connectivity]] matrices on [[aal-atlas]] parcellations.

The viewer leverages GPU acceleration through vispy for handling large datasets, enabling interactive exploration of full-brain volumes at near-realtime frame rates. Beyond multi-dimensional support accommodating up to five dimensions (time, z, y, x, channels) with intuitive scrolling and slicing, napari provides a full Python API for programmatic control, enabling seamless integration into analysis pipelines. Users can perform dimensionality transformation operations including transposing, reshaping, and reorienting data interactively. The annotation tools allow drawing regions of interest directly on images, which is particularly valuable for defining anatomical regions or marking病灶 for further analysis.

## Relationship to TVB

While [[the-virtual-brain]] (TVB) focuses on whole-brain dynamics simulation, napari serves as a complementary visualization tool for inspecting model inputs and outputs. Researchers using TVB can leverage napari to visualize empirical [[structural-connectivity]] matrices from [[dti]] tractography before importing to TVB, simulated [[bold-signal]] time-series outputs as 4D volumes, and source spaces or electrode localizations for [[eeg]]/[[meg]] forward modeling. Napari's Python-native design makes it particularly suitable for integration with TVB's Python ecosystem, where data can be passed directly between simulation and visualization without file I/O overhead.

## Comparison to Related Tools

Napari occupies a unique position in the neuroimaging visualization landscape. Unlike Fsleyes (part of Fsl) or freeview (part of [[freesurfer]]), napari is format-agnostic—any NumPy-compatible data can be visualized. Compared to Itk Snap, napari offers Python scripting capabilities. Against [[brainnet-viewer]] or Brainrender, napari provides greater flexibility for arbitrary data types while those tools specialize in specific connectome or anatomy visualizations.

| Feature | Napari | fsleyes | freeview | brainnet-viewer |
|---------|--------|---------|----------|-----------------|
| Python API | Full | Limited | Minimal | No |
| Plugin system | Yes | No | No | No |
| NIfTI support | Indirect | Native | Native | Limited |
| Connectome viz | Points/Shapes | Overlay | Surface | Native |
| GPU acceleration | Yes | Partial | Yes | Limited |

## Key Plugins for Neuroimaging

The napari ecosystem includes several plugins particularly relevant to [[computational-neuroscience]]. The **brainreg** plugin provides automated atlas-based registration of brain images, enabling researchers to align their data to standard anatomical templates without manual intervention. **napari-stress** offers tools for stress tensor visualization, useful for analyzing mechanical forces in brain tissue models. Additional plugins support integration with various neuroscience tools and formats, though users should verify compatibility with their specific analysis workflows.

## Related Software

- [[the-virtual-brain]]
- Nilearn
- [[nipype]]
- Freesurfer
- Fsl
- Itk Snap
- Brainrender
- [[pycortex]]
- Dipy
- Mrtrix3
- [[connectome-workbench]]

## Key Papers

- Ahlers, H., et al. (2024). "Napari: a multi-dimensional image viewer for Python." *Nature Methods*. https://www.nature.com/articles/s41592-019-0612-4
- Sofroniew, N., et al. (2020). "Napari: fast, easy-to-use bioimage analysis." *BioRxiv*. https://www.biorxiv.org/content/10.1101/2020.10.26.248542v1

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *[[tractography]] analysis with the scilpy toolbox*. Aperture Neuro. [DOI](](https://doi.org/10.52294/001c.154022))
3. (authors unknown). *[[braph]]: A Pipeline for Brain [[connectivity]] Analysis*.