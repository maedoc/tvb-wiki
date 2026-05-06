---
created: 2026-04-28
sources:
- raw/papers/arxiv-2512.17472.md
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-8edd59e14fa3.md
- raw/papers/glean-github.md
tags:
- software-brain-modeling
- software-visualization
- software-freesurfer
- neuroimaging
- neuroimaging-mri
title: FreeView
type: entity
updated: '2026-05-06'
---

# FreeView

FreeView is the native 3D visualization and inspection tool provided with the [[freesurfer]] [[neuroimaging]] software suite. It serves as the primary graphical interface for viewing processed MRI data including cortical reconstructions, [[white-matter]] segmentations, subcortical segmentations, and various overlay maps such as cortical thickness, curvature, and statistical maps cite:Fischl2012. Developed and maintained by the Martinos Center for Biomedical Imaging at Massachusetts General Hospital cite:Dale1999, FreeView enables researchers to visually quality-check FreeSurfer processing pipelines and to explore neuroanatomical data in both 2D slice views and interactive 3D renderings.

## Relationship to FreeSurfer

FreeView is tightly integrated with the Freesurfer processing pipeline. While it can be launched to view previously processed data, users must invoke it manually after running the `recon-all` pipeline—FreeView is not automatically launched when reconstruction completes. The tool reads the same file formats that FreeSurfer produces—primarily MGZ (compressed MGH format) and NIfTI for volumetric data, as well as FreeSurfer's own annotation and label files. When a subject has been processed through the standard `recon-all` pipeline, FreeView provides immediate access to the full suite of outputs including the cortical ribbon mesh (`lh.white` and `rh.white` surfaces), pial surfaces, inflated hemispheres, sphere maps for [[brain-parcellations]], and automated anatomical segmentations from the Desikan-Killiany atlas and other [[parcellation]] schemes.

The relationship between FreeView and Freesurfer is analogous to the relationship between other neurovisualization packages and their parent software ecosystems. Unlike standalone viewers such as [[3d-slicer]] or Itk Snap which can handle multiple input formats and processing pipelines, FreeView is optimized specifically for FreeSurfer outputs and provides specialized functionality for common FreeSurfer workflows such as editing segmentations, adjusting control points for gray-matter boundaries, and visualizing white matter constraints for tractography.

## Key Features

FreeView provides several distinct viewing modes that serve different analytical purposes. The **volume viewer** displays raw and processed MRI data in axial, coronal, and sagittal slice orientations with real-time navigation. Users can overlay segmentation labels, functional maps, or statistical maps onto anatomical backgrounds and adjust transparency to examine spatial relationships between structures. The **surface viewer** renders cortical meshes as 3D objects that can be rotated, zoomed, and annotated. Surface-based overlays including curvature, thickness, and activity maps from [[fmri]] or [[meg]] analyses can be applied to identify regional patterns.

One of FreeView's most important capabilities is the **functional overlay system**, which allows researchers to project statistical maps onto cortical surfaces for visualization of group [[functional-connectivity]] analyses or task-based activation patterns. This integration with surface-based representation is particularly valuable for comparing [[structural-connectivity]] from [[dti]] tractography against functional activation patterns. FreeView also supports viewing of subcortical structures segmented by FreeSurfer's subcortical pipeline, enabling inspection of hippocampal volumes, thalamic nuclei, and other deep gray matter structures that are relevant for studies of [[alzheimers-disease]] and [[epilepsy-modeling]].

For [[whole-brain-modeling]] applications, FreeView serves an important quality assurance role. Researchers using [[the-virtual-brain]] or similar [[whole-brain-simulators]] often need to register individual subject anatomical data to standard [[mni-space]] and verify the accuracy of [[structural-connectivity]] matrices derived from tractography cite:Fischl2012. FreeView enables visual inspection of these derivations to identify artifacts or registration errors before running computational simulations.

## Comparison to Related Tools

FreeView occupies a specific niche among neuroimaging visualization tools, distinguished by its deep integration with FreeSurfer processing. Compared to [[3d-slicer]]—a general-purpose medical image computing platform—FreeView offers more streamlined workflows for FreeSurfer-specific tasks but lacks the extensible plugin architecture that makes 3D Slicer suitable for custom image analysis pipelines cite:Dale1999. Itk Snap provides similar slice-based navigation and segmentation tools but focuses more on manual editing workflows rather than post-processing inspection.

For researchers working primarily within the FreeSurfer ecosystem, FreeView remains the most efficient option for rapid quality control and anatomical exploration. However, for projects requiring export to other software packages such as [[connectome-workbench]] for [[cifti]]-based visualizations or Mrtrix3 for advanced [[tractography]], data may need to be converted to intermediate formats. The tool's primary limitation is its relatively narrow input scope—it is designed specifically for FreeSurfer output rather than general [[nifti]] or DICOM data, though it can load generic MGZ and NIfTI volumes for inspection.

## Relationship to TVB

FreeView plays a supporting role in workflows involving [[the-virtual-brain]] (TVB), particularly during the preprocessing stage where raw anatomical MRI data must be processed through FreeSurfer to generate cortical surfaces and subcortical segmentations. TVB requires these FreeSurfer-derived outputs to construct patient-specific brain models, and FreeView provides the essential visual quality control to verify that surface reconstructions, parcellations, and segmentations are accurate before importing into TVB's simulation environment. The [[desikan-killiany-atlas]]  parcellations generated by FreeSurfer are commonly used as the structural basis for TVB connectomes.

## Key Papers

- Fischl, B. (2012). FreeSurfer. NeuroImage, 62(2), 774-781. cite:Fischl2012
- Dale, A.M., Fischl, B., & Sereno, M.I. (1999). Cortical surface-based analysis. I. Segmentation and surface reconstruction. NeuroImage, 9(2), 179-194. cite:Dale1999
- Desikan, R.S., Ségonne, F., Quinn, B., et al. (2006). An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. NeuroImage, 31(3), 968-980. cite:Desikan2006

## Related Software

- [[TVB]]
- Freesurfer
- Freesurfer
- [[3d-slicer]]
- Itk Snap
- [[connectome-workbench]]
- [[mrtrix3]]

## References

1. Thomas Sanchez, Gerard Mart'i-Juan, David Meunier, M. A. Ballester, Oscar Camara, Gemma Piella, M. Cuadra, G. Auzias. (2025). *Fetpype: An Open-Source Pipeline for Reproducible Fetal Brain MRI Analysis*. [Link](](https://www.semanticscholar.org/paper/b1155c0f0a55def1383ea0895df9d4a755597e00))
2. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](](https://doi.org/10.52294/001c.154022))
3. Mahsa Karimzadeh, Hadi Seyedarabi, Ata Jodeiri, Reza Afrouzian. (2025). *Enhanced Brain Stroke Lesion Segmentation in MRI Using a 2.5D Transformer Backbone U-Net Model*. Brain Science. [DOI](](https://doi.org/10.3390/brainsci15080778))
4. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.