---
title: MRtrix3
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-mrtrix3, neuroimaging-dti, diffusion-imaging, tractography, structural-connectivity, connectomics, software-tvb]
sources: [https://www.mrtrix.org/, https://github.com/MRtrix3/mrtrix3]
---

MRtrix3 is an open-source software package for processing diffusion magnetic resonance imaging (dMRI) data, with particular strength in fiber tractography and construction of structural connectomes. Developed primarily by J-Donald Tournier and colleagues at the Florey Institute of Neuroscience and Mental Health in Melbourne, MRtrix3 provides a comprehensive suite of command-line tools that enable researchers to go from raw diffusion-weighted MRI scans to streamline-based representations of white-matter pathways. The software has become a standard tool in the neuroimaging community, particularly for studies requiring high-quality tractography for connectomic analyses.

## Overview and Motivation

Diffusion MRI measures the random thermal motion of water molecules, which in white matter is constrained by axonal membranes and myelin sheaths, causing water to diffuse preferentially along fiber orientations. This anisotropic diffusion enables inference about the underlying tissue structure, but extracting biologically meaningful fiber orientation distributions and reconstructing anatomical pathways requires sophisticated computational processing. MRtrix3 addresses this challenge through a combination of robust statistical estimators, model-based analysis approaches, and flexible workflow designs that accommodate various acquisition schemes and research questions.

The software emerged from the need for tractography methods that are both computationally efficient and biologically accurate. Traditional deterministic tractography approaches suffered from limitations in handling complex fiber configurations such as crossings, branchings, and kissings. MRtrix3 implements advanced algorithms including constrained spherical deconvolution (CSD), responsive function estimation, and both probabilistic and deterministic streamline tractography that handle these challenges more robustly [Tournier et al. 2007]. For whole-brain modeling efforts, the quality of tractography directly impacts the fidelity of structural connectivity matrices, making tools like MRtrix3 essential preprocessing steps.

## Key Features

MRtrix3 implements several notable technical capabilities. The software employs constrained spherical deconvolution to estimate fiber orientation distribution functions (fODFs) from diffusion data, which provides superior angular resolution compared to earlier diffusion tensor imaging approaches [Tournier et al. 2004]. The algorithm handles the challenging problem of resolving multiple fiber populations within a single imaging voxel, which is critical for accurate tractography in regions where fiber pathways cross or intersect.

The tractography engine supports multiple algorithms including iFOD2 (second-order Integration over Fiber Orientation Distributions), a second-order integration approach that provides more accurate pathway reconstruction than simpler methods [Tournier et al. 2019]. Researchers can also perform SIFT (Spherical deconvolution Informed Filtering of Tractograms) to reduce spurious streamlines and produce more biologically plausible fiber populations [Smith et al. 2013]. For connectome construction, MRtrix3 includes tools for parcellating the brain, mapping streamlines to regions, and generating connectivity matrices that quantify the density or probability of anatomical connections between regions.

The software operates through a command-line interface with consistent syntax across tools, enabling scripted processing pipelines. MRtrix3 supports various input formats common in neuroimaging and produces outputs compatible with visualization tools and connectivity analysis packages.

## Relationship to TVB

MRtrix3 plays an important role in The Virtual Brain workflow for personalized whole-brain modeling. The structural connectivity matrix used in TVB simulations is typically derived from diffusion MRI tractography, and MRtrix3 is one of the primary tools for generating high-quality structural connectomes from DWI data. Researchers using TVB frequently employ MRtrix3 to process their raw dMRI data, perform tractography, parcellate the brain according to chosen atlases such as [[desikan-killiany-atlas]] or [[glasser-atlas]], and generate connectivity matrices that define the anatomical pathways simulated in TVB.

The software integrates well with other tools in the TVB ecosystem. Output from MRtrix3 can be converted to formats compatible with [[the-virtual-brain]] through adapters or direct format conversion. Additionally, MRtrix3 output complements other tractography packages like [[dsi-studio]] and [[camino]], allowing researchers to compare connectivity estimates or combine approaches. The resulting structural connectomes feed directly into TVB's neural mass simulations, where the connectivity weights modulate signal propagation between brain regions during simulated dynamics.

## Key Papers

- Tournier JD, Calamante F, Connelly A. Robust determination of the fibre orientation distribution in diffusion MRI using constrained spherical deconvolution. NeuroImage. 2007;36(3):645-660.
- Tournier JD, Smith R, Raffelt D, et al. MRtrix3: Design and implementation of a new toolbox for fibre tractography. NeuroImage. 2019;202:116137.
- Smith RE, Tournier JD, Calamante F, Connelly A. SIFT: Spherical-deconvolution informed filtering of tractograms. NeuroImage. 2013;67:376-386.
- Raffelt D, Tournier JD, Rose S, et al. Apparent Fibre Density: A novel measure for the analysis of diffusion-weighted MR images. NeuroImage. 2012;59(4):3976-3994.

## Related Software

MRtrix3 complements several other tools in the neuroimaging ecosystem. For visualization, outputs can be viewed using [[brainnet-viewer]], [[freesurfer]] with [[freeview]], or [[trackvis]]. For alternative tractography approaches, researchers might consider [[camino]], [[dsi-studio]], or [[dipy]]. MRtrix3 is often used alongside preprocessing suites like [[fsl]] and can integrate with connectomics frameworks including the [[brain-connectivity-toolbox]] and [[brainspace]]. For whole-brain modeling workflows, MRtrix3-derived connectomes may be combined with tools like [[tvb-multiscale]] for simulations at different scales of neural organization.
