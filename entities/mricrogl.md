---
created: 2026-04-23
sources: []
tags:
- software-brain-modeling
title: MRIcroGL
type: entity
updated: 2026-05-03
---
title: MRIcroGL
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-visualization, neuroimaging, neuroimaging-fmri, neuroimaging-dti]
sources: ["https://www.nitrc.org/projects/mricrogl/", "https://github.com/neurolibuscui/mricrogl", "https://www.nitrc.org/projects/mricron/"]
---

MRIcroGL is a lightweight, cross-platform medical imaging visualization program designed primarily for viewing three-dimensional neuroimaging datasets in formats such as NIfTI and DICOM. Originally developed as a modern OpenGL-based successor to the older MRIcron application, MRIcroGL provides neuroscientists with a fast, no-frills viewer that loads large brain volumes efficiently without the overhead of more comprehensive neuroimaging software suites. The program is particularly valued in the whole-brain modeling community for its ability to quickly inspect structural and functional data, verify preprocessing outputs, and perform basic region-of-interest analysis prior to fitting [[whole-brain-modeling|whole-brain models]] in simulators like [[the-virtual-brain|The Virtual Brain]].

## Overview

MRIcroGL was created to address the need for a simple, high-performance viewer that could handle modern high-resolution neuroimaging datasets without requiring extensive system resources or complex installation procedures. The software renders volumetric data using OpenGL acceleration, enabling smooth navigation through three-dimensional brain images across multiple planes (axial, coronal, sagittal) as well as arbitrary oblique orientations. Unlike full-featured analysis pipelines such as [[fsl|FSL]], [[freesurfer|FreeSurfer]], or [[spm|SPM]], MRIcroGL focuses exclusively on visualization and basic manipulation, making it an ideal complementary tool for researchers who need to quickly inspect data at various stages of processing—from raw DICOM conversions using tools like [[dcm2niix|dcm2niix]] to final statistical maps ready for interpretation. <ref>Rorden et al. (2012). Transforming structural data into normalized space. Neuroinformatics.</ref>

The program's architecture supports multiple image formats common in neuroimaging research, with primary support for NIfTI-1 format files widely used in the [[neuroimaging]] community. It can also import DICOM files directly, which is useful for working with data directly from scanners before conversion to more portable formats. MRIcroGL operates through a simple graphical user interface with intuitive mouse controls for panning, zooming, and scrolling through image slices, requiring minimal learning curve for new users.

## Key Features

One of MRIcroGL's distinguishing characteristics is its fast loading speed for large volumetric datasets. Modern high-resolution neuroimaging datasets—particularly those from the [[hcp-dataset|Human Connectome Project]] or [[uk-biobank|UK Biobank]]—can exceed several gigabytes in size, and many viewers struggle to load these efficiently. MRIcroGL handles such datasets with relative ease, making it practical for quality control workflows where researchers need to rapidly examine preprocessing outputs across many subjects.

The software includes a range of visualization capabilities suited to different imaging modalities. For [[diffusion-mri|Diffusion MRI]] data, MRIcroGL can display fractional anisotropy maps, direction-encoded color maps, and tractography streamlines when properly formatted. For [[fmri|fMRI]] data, it renders statistical parametric maps overlaid on anatomical backgrounds, with adjustable transparency to balance visibility of activation patterns against underlying structural images. The program supports multiple colormaps commonly used in neuroimaging, including grayscale, hot metal, jet, and custom schemes for displaying positive and negative activations simultaneously.

Region-of-interest analysis is facilitated through the built-in drawing tools that allow users to define spherical or arbitrary-shaped regions on any plane and generate summary statistics. While this functionality is basic compared to dedicated analysis packages, it proves useful for quick visual confirmation of coverage or for defining simple masks that can be exported for use in downstream analyses. The program also supports time-series animation, enabling visualization of [[resting-state|resting-state]] fMRI data as a movie rather than static frames.

## Relationship to TVB

In the context of [[whole-brain-modeling|whole-brain modeling]] workflows facilitated by [[the-virtual-brain|TVB]], MRIcroGL serves as a complementary visualization tool rather than a core component of the simulation pipeline. Researchers using TVB typically begin their workflows with structural [[neuroimaging-dti|DTI]] data to construct [[structural-connectivity|structural connectivity]] matrices derived from [[tractography]] tractograms. Before importing these data into TVB, researchers often use MRIcroGL to verify the quality of their preprocessing steps, confirm that parcellation labels from atlases such as [[aal-atlas|AAL]] or [[desikan-killiany-atlas|Desikan-Killiany]] align correctly with their structural images, and ensure that any intermediate files are properly oriented in [[mni-space|MNI space]].

Similarly, when model fitting produces [[functional-connectivity|functional connectivity]] outputs or [[bold-signal|BOLD signal]] predictions, MRIcroGL enables quick visual comparison between empirical and simulated time series. While TVB provides its own internal visualization capabilities through its web-based interface, many researchers find it helpful to export simulation results as NIfTI files and inspect them in MRIcroGL for independent validation. The lightweight nature of MRIcroGL makes it particularly useful in these quick-look scenarios where launching the full TVB simulation environment would be disproportionate to the task.

## Technical Considerations

MRIcroGL was developed by Chris Rorden using the Lazarus development environment (Free Pascal) and is distributed as open-source software under the BSD license. <ref>Rorden C. MRIcroGL documentation. https://www.nitrc.org/projects/mricrogl/</ref> The program runs natively on Windows, macOS, and Linux operating systems, with versions available as both standalone executables and through package managers. The software requires OpenGL 2.0 compatible graphics hardware, which is satisfied by virtually any modern computer. Installation is straightforward—the program requires no dependencies beyond the standard runtime libraries for each operating system—making it accessible even on computing environments where installing full software suites would require administrative privileges or complex configuration.

The first release of MRIcroGL as an OpenGL-based viewer came after the original MRIcron program, providing hardware-accelerated rendering that became increasingly important as neuroimaging datasets grew in size. The project continues to be maintained and updated, with periodic releases addressing compatibility with new operating system versions and neuroimaging format specifications.

For users requiring more advanced visualization capabilities beyond what MRIcroGL offers, complementary tools include [[3d-slicer|3D Slicer]] for comprehensive medical image computing, [[brainnet-viewer|BrainNet Viewer]] for cortical surface visualization of connectivity data, [[connectome-workbench|Connectome Workbench]] for visualization of CIFTI format data developed by the [[human-connectome-project|Human Connectome Project]], and [[itk-snap|ITK-SNAP]] for active contour-based segmentation. Each of these tools addresses different use cases: 3D Slicer provides a complete development environment for medical image computing, BrainNet Viewer specializes in network visualization on cortical surfaces, and Connectome Workbench excels with CIFTI data structures common in HCP-style datasets. MRIcroGL occupies a distinct niche as a fast, simple option for basic volume inspection tasks.

## Key Papers

- Rorden C, Karnath HO, Bonilha L (2007). Improving lesion-symptom mapping. *Journal of Cognitive Neuroscience*. https://doi.org/10.1162/jocn.2007.19.7.1081
- Rorden C, Bonilha L, Fridriksson J, Bender B, Karnath HO (2012). Age-specific CT and MRI templates for spatial normalization. *Neuroimage*. https://doi.org/10.1016/j.neuroimage.2011.10.054

## Related Software

MRIcroGL should not be confused with its predecessor [[mricron|MRIcron]], which remains available but lacks the OpenGL-based rendering improvements of the newer version. Both tools share a common heritage in the neuroimaging open-source ecosystem and continue to be maintained in parallel. Other visualization alternatives in the ecosystem include [[fsl|FSLeyes]] (part of the FSL suite), [[mrtrix3|MRTrix3]] for advanced diffusion imaging visualization, and [[nilearn|Nilearn]] for Python-based programmatic visualization workflows. The choice among these tools typically depends on the specific visualization task, the data format being used, and integration requirements with existing analysis pipelines.

## References

<references>
- MRIcroGL project page. NITRC. https://www.nitrc.org/projects/mricrogl/
- MRIcron project page. NITRC. https://www.nitrc.org/projects/mricron/
- Rorden C, Karnath HO, Bonilha L (2007). Improving lesion-symptom mapping. Journal of Cognitive Neuroscience.
- Rorden C, Bonilha L, Fridriksson J, Bender B, Karnath HO (2012). Age-specific CT and MRI templates for spatial normalization. Neuroimage.
</references>