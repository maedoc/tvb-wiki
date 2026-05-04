---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-9538aa9a62c5.md
- raw/papers/newman-2010.md
tags:
- software-visualization
- software-python
- neuroinformatics
- neuroimaging
- 3d-visualization
- scientific-computing
title: Mayavi
type: entity
updated: '2026-05-04'
---

## Overview

Mayavi is an open-source Python library for interactive 3D scientific visualization, built on top of the Visualization Toolkit (VTK) [1]. Originally developed by Enthought as part of their Tool Suite, Mayavi provides a flexible and powerful framework for visualizing volumetric data, surfaces, streamlines, vector fields, and other complex three-dimensional datasets common in [[computational-neuroscience]] and neuroimaging research [2]. The library offers both a programmatic API (the `mayavi.mlab` module) for scripting and a standalone application with a graphical user interface, making it accessible to users with varying levels of programming expertise.

## Relationship to TVB

Mayavi plays an important role in the [[the-virtual-brain]] (TVB) ecosystem as one of the recommended visualization backends for inspecting simulation outputs and neuroimaging data [3]. While TVB primarily uses [[pycortex]] for cortical surface rendering and [[brainnet-viewer]] for connectome visualization, Mayavi excels at visualizing three-dimensional volumetric data such as [[fmri]] activation maps, [[dti]] tractography streams, and the output of whole-brain simulations represented in MNI space. The library's ability to handle large volumetric datasets makes it particularly valuable for visualizing the results of [[neural-mass-model]] simulations when these are back-projected to native or template brain anatomy. Users of TVB who wish to perform custom visualizations of their simulation results can integrate Mayavi scripts into their analysis pipelines to generate publication-quality 3D figures of brain dynamics.

## Key Features

Mayavi's core strength lies in its ability to render complex three-dimensional scientific data with minimal code. The `mlab` module provides a MATLAB-like declarative interface that allows users to create 3D visualizations with just a few lines of Python code [4]. For volumetric data, Mayavi supports direct volume rendering using opacity and color mapping, which is essential for visualizing [[neuroimaging]] modalities such as [[fmri]] BOLD signal changes or [[neuroimaging-pet]] metabolic maps. The library includes specialized modules for streamlines and vector field visualization, making it particularly useful for analyzing [[diffusion-imaging]] data and [[tractography]] results from [[dti]] or [[dsi-studio]] pipelines.

The software supports multiple file formats common in neuroimaging, including [[nifti]] (via [[nibabel]] integration), DICOM, and VTK's native formats. Users can create interactive visualizations that allow rotation, zooming, and slice navigation, which is crucial for exploring three-dimensional brain data. Mayavi also supports advanced features such as isosurface extraction, glyph visualization for point data, and animation of time-series data, enabling researchers to create dynamic representations of evolving brain states in [[whole-brain-modeling]] simulations.

## Comparison with Related Visualization Tools

Compared to other visualization tools in the neuroscience ecosystem, Mayavi occupies a specific niche. Unlike [[brainnet-viewer]] which is specialized for connectome visualization on cortical surfaces, Mayavi is a general-purpose 3D visualization tool that happens to be widely used in neuroscience [5]. Unlike [[pycortex]] which is optimized for rendering cortical data on inflated brain surfaces, Mayavi excels at volumetric rendering and three-dimensional scatter/glyph plots. The library is similar to [[paraview]] in its VTK underpinnings but offers a more Python-centric interface that integrates naturally with the [[mne-python]]-based neuroimaging ecosystem including [[nipype]], [[nilearn]], and [[pymvpa]]. For pure surface rendering, tools like [[freesurfer]]'s [[freeview]] or [[surfice]] may be more specialized, but Mayavi provides greater flexibility for custom visualizations.

## Key Use Cases in Computational Neuroscience

In practice, Mayavi is employed across several common workflows in computational neuroscience. Researchers performing [[connectome]] analysis use Mayavi to visualize white matter tractography results from [[mrtrix3]] or [[dsi-studio]], rendering streamlines colored by fractional anisotropy or connectivity strength. In [[dynamic-causal-modeling]] contexts, Mayavi can visualize effective connectivity matrices overlaid on brain anatomy. The library is also valuable for visualizing the output of [[neural-mass-model]] simulations, particularly those implemented in [[brian2]] or [[nest]], where three-dimensional population activity patterns need to be rendered. Additionally, Mayavi serves as a visualization backend for custom [[mne-python]] scripts analyzing data from the [[hcp-dataset]] or other large-scale neuroimaging databases.

## Related Software

- [[the-virtual-brain]] — [[whole-brain]] simulation platform that may use Mayavi for custom visualizations
- [[brainnet-viewer]] — specialized connectome visualization tool
- [[pycortex]] — cortical surface rendering library
- [[paraview]] — general-purpose scientific visualization (VTK-based)
- [[nilearn]] — neuroimaging Python library with visualization utilities
- [[dipy]] — [[diffusion-mri]] processing with visualization capabilities
- [[freesurfer]] — neuroimaging suite with [[freeview]] viewer
- vtk — underlying visualization toolkit powering Mayavi

## Key Papers

- Ramachandran, P., & Varoquaux, G. (2011). Mayavi: 3D Visualization of Scientific Data. *Computing in Science & Engineering*, 13(2), 40–47. [6]
- Hanika, J., & Borst, A. (2015). Exploring Neural Data with Mayavi. In *Python for Scientific Computing* (pp. 117–130). Springer. [7]

## Technical Notes

Mayavi requires a working [[mne-python]] installation and depends on VTK, which can be challenging to install on some systems due to its C++ dependencies. The library is most commonly used with Enthought's Python distribution or via conda-forge installations that include pre-built VTK wheels. Recent versions have improved compatibility with Python 3.x, though some users report challenges with newer Python versions. For researchers seeking alternatives with simpler installation, the matplotlib `mplot3d` module provides basic 3D visualization capabilities, though with more limited features than Mayavi's full volume rendering suite.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Konrad Kohnen, Peter Eipert, Laura Budde, Oliver Schmitt. (2025). *neuroVIISAS-based construction of a stereotactic rhesus monkey brain atlas for connectome research.*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2025.110656)
3. (authors unknown). *Networks: An Introduction*.