---
created: 2026-05-04
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/schirner-2018.md
- raw/papers/arxiv-2503.15830.md
tags:
- software-brain-modeling
- diffusion-imaging
- tractography
- structural-connectivity
- diffusion-mri
title: AMICO
type: entity
updated: '2026-05-06'
---

# AMICO

## Overview

AMICO (Accelerated Microstructure Imaging via Convex Optimization) is an open-source computational framework for solving the [[white-matter]] microstructure estimation problem from diffusion magnetic resonance imaging (dMRI) data. Unlike traditional diffusion tensor imaging (DTI) approaches that assume a single Gaussian diffusion process per voxel, AMICO employs convex optimization to reconstruct fiber orientation distributions (FODs) and extract quantitative microstructure metrics such as fiber density, [[fractional-anisotropy]], and orientation dispersion index. The framework was developed to address the computational bottleneck inherent in modern HARDI (High Angular Resolution [[diffusion-imaging]]) and Q-ball imaging techniques, which traditionally required expensive non-convex optimization routines that could trap in local minima. By reformulating the problem as a convex optimization task, AMICO achieves both computational efficiency and robustness to noise, making it practical for processing large [[neuroimaging]] datasets including those from the [[human-connectome-project]] (HCP).

## Motivation and Context

The fundamental challenge in [[diffusion-mri]] is inferring the underlying white matter microstructure from measurements of water molecule displacement patterns. Water diffuses more freely along axonal fibers than across them, and this anisotropy provides the basis for inferring fiber orientation. However, the inverse problem—going from measured signals to microstructure parameters—is severely ill-posed: multiple fiber configurations can produce identical observed signals. Traditional approaches like DTI assume a single tensor per voxel, which fails in regions where multiple fiber populations cross, branch, or kiss. Advanced techniques like diffusion spectrum imaging (DSI) and Q-ball imaging can resolve multiple fiber orientations but at prohibitive computational cost for large-scale studies.

AMICO emerged from the need to bridge the gap between sophisticated microstructure reconstruction methods and practical neuroimaging pipelines. The original implementation (Daducci et al., 2014) demonstrated that the microstructure problem could be expressed as a [[linear]] combination of dictionary atoms, enabling efficient convex optimization via the ADMM (Alternating Direction Method of Multipliers) algorithm. This breakthrough made it feasible to process whole-brain datasets in minutes rather than hours, democratizing advanced microstructure imaging for research groups without dedicated HPC resources. The framework has since become a standard tool in the [[connectomics]] community, particularly for generating structural [[connectivity]] matrices used in [[whole-brain|whole-brain modeling]] workflows.

## Technical Framework

### Mathematical Formulation

AMICO frames the diffusion signal reconstruction as a linear inverse problem. The measured dMRI signal at each voxel is modeled as a sparse combination of basis signals corresponding to different fiber populations and diffusion compartments. Mathematically, the signal model can be expressed as:

$$S(\mathbf{q}) = \sum_{k=1}^{K} f_k \cdot R_k(\mathbf{q}) + \eta$$

where $S(\mathbf{q})$ is the measured signal at diffusion encoding vector $\mathbf{q}$, $f_k$ are the fiber population coefficients (fiber density), $R_k(\mathbf{q})$ are the response functions for each compartment, and $\eta$ represents noise. The response functions are precomputed from single-fiber calibration data or estimated iteratively.

The key insight driving AMICO is that this sparse coding problem can be solved efficiently using convex optimization when properly formulated. The algorithm minimizes a weighted $\ell_1$ objective:

$$\min_f \| \mathbf{S} - \mathbfDf \|_2^2 + \lambda \| \mathbf{f} \|_1$$

subject to non-negativity constraints on the fiber density coefficients $f_k \geq 0$. This formulation guarantees global optimum convergence unlike earlier non-convex approaches.

### Output Measures

AMICO produces several clinically and scientifically relevant metrics. The fiber orientation distribution function (FOD) provides a continuous representation of fiber directions within each voxel, capturing crossing fibers up to a user-specified maximum number (typically 3-5). From the FOD, AMICO computes:

- **Fiber Density (FD):** Total integrated fiber population magnitude, sensitive to axonal density
- **Fractional Anisotropy (FA):** Standard anisotropy measure derived from the second-order tensor of the FOD
- **Orientation Dispersion Index (ODI):** Measures the angular spread of fiber orientations, capturingaxonal organization

These measures can be thresholded and segmented to produce tractograms and structural connectivity matrices for downstream modeling applications.

## Relationship to TVB

AMICO plays an important role in [[the-virtual-brain]] (TVB) workflows for personalized whole-brain modeling. The TVB pipeline for building subject-specific brain models requires a structural connectivity matrix that encodes the strength of anatomical connections between brain regions. This matrix is typically derived from diffusion MRI tractography, and AMICO serves as one of several options for the underlying microstructure reconstruction.

Users processing their own MRI data can use AMICO to generate fiber orientation distributions, which are then passed to tractography algorithms (e.g., [[MRtrix3]] or [[Camino]]) to reconstruct white matter streamlines. These streamlines are subsequently segmented by a [[brain-parcellations|brain parcellation]] (such as [[Desikan-Killiany atlas]] or [[Schaefer atlas]]) to produce a region-by-region connectivity matrix. This matrix directly constrains the [[whole-brain-modeling|whole-brain]] simulation in TVB, determining which brain areas are coupled and with what coupling strength.

The integration typically follows this pipeline: raw DICOM or [[nifti]] diffusion data → AMICO reconstruction → deterministic or probabilistic tractography → connectivity matrix generation → TVB simulation. Several TVB tutorials and documentation pages reference AMICO as a recommended preprocessing step for data acquired on 3T scanners with multi-shell diffusion protocols. Notably, AMICO output can be combined with [[FreeSurfer]] cortical segmentations to ensure consistent segmentation between structural (T1) and diffusion modalities.

## Key Features

The primary advantage of AMICO lies in its computational efficiency. The original publication demonstrated speedups of 10-100x compared to non-convex alternatives, enabling whole-brain processing in under 10 minutes on standard hardware. The framework is implemented in MATLAB with optional C/MEX acceleration, and Python bindings have been developed by the community. AMICO supports multi-shell acquisition protocols common in modern Connectom scanners, allowing separation of intracellular and extracellular diffusion compartments.

The method is specifically designed for single-shell and multi-shell HARDI data, with optimal performance on b-values between 1000-3000 s/mm². It handles the standard acquisition schemes used in human connectomics projects, including the HCP protocols. Users must provide quality-checked preprocessed diffusion data—AMICO does not include artifact rejection or eddy-current correction, which must be performed separately using tools like [[FSL]] eddy or [[MRtrix3]] preprocessing.

## Alternative Tools

AMICO occupies a specific niche in the diffusion MRI ecosystem. Alternative frameworks include [[MRtrix3]] (which implements constrained spherical deconvolution), [[DTI-TK]] (focused on tensor-based tractography), [[Camino]] (Monte Carlo simulation framework), and [[Dipy]] (comprehensive Python library for diffusion MRI). Compared to these alternatives, AMICO's convex optimization formulation provides theoretical guarantees on solution quality but is less flexible in handling complex acquisition protocols or novel contrast mechanisms.

## Related Software

- [[MRtrix3]] - Alternative framework for fiber orientation distribution estimation
- [[Dipy]] - Python library covering broader diffusion MRI analysis
- [[Camino]] - Diffusion toolkit with Monte Carlo simulation capabilities
- [[DTI-TK]] - Tensor-based toolkit for high-precision tractography
- [[FSL]] - General neuroimaging suite including diffusion tools
- [[FreeSurfer]] - Cortical reconstruction for [[parcellation]]
- [[TVB]] - Whole-brain simulation platform
- [[tractography]] - Parent concept for deterministic and probabilistic fiber tracking
- [[structural-connectivity]] - Connection matrices derived from tractography
- [[connectome]] - Complete structural and functional brain connectivity map

## Key Papers

The original AMICO paper established the convex optimization framework and demonstrated its application to both synthetic and real human data. Subsequent work extended the method to handle multiple diffusion compartments, enabling separate estimation of intracellular (axonal) and extracellular (tissue) diffusion fractions. The method has been validated against histology in animal models and against gold-standard techniques in human studies.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](](https://doi.org/10.1016/j.neuroimage.2018.05.040))
3. Martin Cole, Yang Xiang, Will Consagra, Anuj Srivastava, Xin Qiu, Zhengwu Zhang. (2025). *Alignment of Continuous Brain Connectivity*. [Link](](https://www.semanticscholar.org/paper/e2f5bab42e2d6184495327924fdcb7ce59670424))