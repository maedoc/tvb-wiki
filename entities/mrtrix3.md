---
title: MRtrix3
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-dti, software-visualization, diffusion-imaging, tractography, structural-connectivity, neuroimaging-dti, software-tvb]
sources: [tournier2007, smith2012, jeurissen2014, dhollander2019, mrrix3docs]
---

MRtrix3 is a software package for reconstruction, analysis, and visualization of diffusion MRI data, with a particular emphasis on fiber tractography and structural connectivity mapping. Developed by the Brain Research Institute at the University of Melbourne [@mrrix3docs], MRtrix3 provides a comprehensive suite of command-line tools for processing diffusion-weighted images, generating streamlines, and constructing connectomes. It has become one of the primary tools in the neuroimaging community for extracting quantitative structural connectivity matrices that serve as the anatomical foundation for whole-brain modeling workflows.

## Overview

MRtrix3 originated as an evolution of the earlier MRtrix package, designed specifically to address the computational challenges of modern diffusion imaging datasets. The software implements state-of-the-art algorithms for constrained spherical deconvolution (CSD) [@tournier2007], which enables robust fiber orientation estimation even in regions where multiple fiber populations cross—situations that confounded earlier diffusion tensor imaging approaches. The package operates entirely through command-line interfaces, making it highly suitable for batch processing and integration into automated neuroimaging pipelines. Its modular architecture allows users to construct custom processing workflows by chaining together individual tools for different stages of the analysis, from raw DWI preprocessing to final connectome generation.

## Key Features

The core strength of MRtrix3 lies in its implementation of advanced diffusion models and tractography algorithms. **Constrained Spherical Deconvolution** (CSD) decomposes the diffusion signal into fiber orientation density functions (fODFs), accurately representing complex fiber geometries including crossing, branching, and kissing fibers that are prevalent throughout the white matter. This represents a significant advancement over diffusion tensor imaging, which can only resolve a single fiber direction per voxel and fails completely in regions of fiber crossing [@jeurissen2014].

For tractography, MRtrix3 implements **probabilistic streamline tracking** that samples from the fODF to generate thousands of possible fiber paths through the brain. The algorithm includes anatomical constraints such as maximum angle thresholds and termini criteria to ensure physically plausible streamlines. Users can apply spherical deconvolution-based filtering (SDF) to improve tractography accuracy by excluding streamlines that deviate from the dominant fiber orientation at each point.

The software also provides tools for **connectome construction**, including parcellation-based connectivity matrices, edge-wise statistical analysis, and network visualization. The connectome workflow integrates seamlessly with standard brain atlases such as the Desikan-Killiany atlas, Schaefer atlas, and Glasser atlas, allowing users to generate connectivity matrices at multiple parcel resolutions.

## Technical Processing Pipeline

A typical MRtrix3 workflow for structural connectivity analysis proceeds through several stages. First, diffusion data are preprocessed to correct for motion, eddy currents, and bias fields using tools such as `mrdegibbs`, `mrgrid`, and `dwibiascorrect`. Next, the response function is estimated from white matter voxels using the Dhollander algorithm [@dhollander2019], after which constrained spherical deconvolution is performed to compute fiber orientation density functions. Tractography is then executed using `tckgen` with user-specified parameters for minimum fiber length, angular threshold, and streamline count.

The resulting streamlines can be filtered using the **SIFT (Spherical-deconvolution Informed Filtering of Tractograms)** algorithm [@smith2012], which applies a mathematical model to remove spurious fibers and ensure that the final tractogram represents anatomically plausible connections. Finally, `tck2connectome` maps streamlines onto a parcellation template to generate a weighted connectivity matrix representing the number or density of connections between brain regions.

## Relationship to TVB

MRtrix3 plays a crucial role in The Virtual Brain ecosystem as one of the primary tools for generating **structural connectivity matrices** that define the anatomical infrastructure of TVB models. The structural connectivity matrix—typically a weighted adjacency matrix where entries represent the number or strength of white matter tracts between brain regions—provides the skeletal topology upon which whole-brain dynamics unfold. TVB requires this connectivity data to configure the coupling between brain regions in simulations of epilepsy, resting-state dynamics, and brain stimulation.

The typical integration involves exporting parcellated connectivity matrices from MRtrix3 in formats compatible with TVB's connectivity reader. Several TVB adapters and pipelines have been developed to streamline this conversion, including integration with the Connectome Mapper 3 and custom scripts that map MRtrix3 output to TVB's internal data structures. Users constructing personalized brain models from individual diffusion MRI scans routinely employ MRtrix3 for tractography before importing the resulting connectivity matrix into TVB for simulation.

## Related Software

MRtrix3 frequently operates alongside other diffusion imaging tools in complete neuroimaging workflows. The **FSL** package provides alternative preprocessing routines and statistical tools for diffusion analysis, while **DSi Studio** and **DSI Tutor** offer different tractography implementations. For visualization, **mrview** (MRtrix3's built-in viewer) integrates with **FSLeyes** and the **Connectome Workbench** for interactive exploration of tractograms and connectivity data. The **Brain Connectivity Toolbox** (BCTPY) provides network analysis algorithms that complement MRtrix3's connectome construction capabilities, enabling users to compute graph-theoretic metrics such as modularity, efficiency, and hub identification on structural connectivity networks derived from MRtrix3 tractography.

## Key Papers

- Tournier, J.-D., Calamante, F., & Connelly, A. (2007). Robust determination of the fibre orientation distribution in diffusion MRI: Non-negativity constrained super-resolved spherical deconvolution. *NeuroImage*, 35(4), 1459-1472.
- Smith, R.E., Tournier, J.-D., Calamante, F., & Connelly, A. (2012). Anatomically-constrained tractography: Improved diffusion MRI streamlines tractography through effective use of anatomical information. *NeuroImage*, 62(3), 1924-1938.
- Jeurissen, B., Tournier, J.-D., Dhollander, T., Connelly, A., & Sijbers, J. (2014). Multi-tissue constrained spherical deconvolution for improved analysis of multi-shell diffusion MRI. *Neuroimage*, 164, 127-143.
- Dhollander, T., Raffelt, D., & Connelly, A. (2016). Unsupervised 3-tissue response function estimation from single-shell or multi-shell diffusion MR data without a dedicated atlas. *Proceedings of the ISMRM*, 24, 4307.
- Dhollander, T., Mito, R., Raffelt, D., & Connelly, A. (2019). Improved white matter response function estimation for 3-tissue spherical deconvolution. *Proceedings of the ISMRM*, 27, 5554.
