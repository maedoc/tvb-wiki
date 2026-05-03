---
created: 2026-04-29
sources:
- raw/papers/daducci-2015-amico.md
- raw/papers/zhang2015-noddi.md
- raw/papers/hcp-2013-methods.md
tags:
- software-dti
- diffusion-imaging
- tractography
- neuroimaging
- structural-connectivity
- computational-neuroscience
- connectomics
- parameter-estimation
title: AMICO
type: entity
updated: '2026-05-03'
---

# AMICO

## Overview

AMICO (Accelerated Microstructure Imaging via Convex Optimization) is an open-source computational framework for fitting compartment models to diffusion magnetic resonance imaging (dMRI) data. Released in 2015 by Alessandro Daducci and colleagues at the University of Lausanne, AMICO reformulates the otherwise computationally intensive problem of estimating microstructural tissue properties into a convex optimization problem that can be solved efficiently using modern numerical methods (Daducci et al., 2015). The software enables researchers to extract quantitative metrics about brain tissue microstructure—including fiber orientation distributions, axon diameter estimates, and volume fractions of different tissue compartments—from diffusion-weighted MRI scans acquired in vivo. Unlike traditional tractography methods that focus solely on reconstructing [[white-matter]] pathways, AMICO belongs to the broader category of **microstructure imaging** techniques that characterize the biophysical properties of neural tissue at a sub-voxel scale.

## Motivation and Context

[[diffusion-mri]] has revolutionized our ability to study the structural organization of the living brain by measuring the random thermal motion of water molecules, which is constrained by cellular structures such as axonal membranes and myelin sheaths. However, extracting meaningful biological information from these measurements has historically been challenged by the ill-posed nature of the inverse problem: multiple different tissue configurations can produce identical diffusion signals. Early approaches like **diffusion tensor imaging (DTI)** provided only gross measures like **fractional anisotropy** and mean diffusivity, which lack specificity to particular microstructural features.

The emergence of compartment models (also called tissue models or biophysical models) offered a more principled approach by modeling the diffusion signal as a weighted sum of signals from distinct tissue compartments—typically representing intra-axonal (restricted) and extra-axonal (diffused and hindered) water pools. However, fitting these models typically requires non-convex optimization with multiple local minima, making the results sensitive to initialization and computationally expensive for large datasets. AMICO addressed these limitations by reformulating the problem as a convex optimization task using a [[linear]] combination of dictionary atoms, dramatically accelerating computation while guaranteeing global optimality. This efficiency has made AMICO particularly valuable for studies requiring analysis of large cohorts, such as the **Human [[connectome]] Project** (HCP) and **[[uk-biobank]]** imaging datasets (Glasser et al., 2013).

## Technical Approach

The core mathematical innovation behind AMICO lies in its reformulation of the compartment model fitting problem. Rather than directly optimizing non-linear model parameters, AMICO expresses the expected diffusion signal as a linear combination of pre-computed compartment signals:

$$S(\mathbf{g}, b) = \sum_{k=1}^{K} w_k \, S_k(\mathbf{g}, b)$$

where $S_k$ represents the signal from the $k$-th compartment (e.g., Zeppelin, Stick, Ball), $\mathbf{g}$ denotes the gradient direction, $b$ is the b-value, and $w_k$ are volume fractions that must satisfy $\sum_k w_k = 1$ and $w_k \geq 0$. By discretizing the parameter space of interest (such as fiber orientations), the problem becomes a linear constrained least squares problem that can be solved efficiently using an active set strategy or similar convex optimization algorithms (Daducci et al., 2015). This approach yields both the volume fractions of each compartment and, critically, the **fiber orientation distribution** (FOD) that characterizes the underlying [[structural-connectivity]].

The AMICO framework is modular and supports multiple compartment models, including the standard **NODDI** (Neurite Orientation Dispersion and Density Imaging) model that separates intracellular and extracellular diffusion compartments (Zhang et al., 2012). Output metrics from AMICO include orientation dispersion indices, intracellular volume fractions (interpreted as neurite density), and orientation distribution functions that can be used for **tractography** downstream.

## Relationship to TVB and Whole-Brain Modeling

While AMICO is primarily a microstructure imaging tool rather than a neural simulation platform, it plays an important supporting role in **[[whole-brain|whole-brain modeling]]** workflows by providing high-quality structural [[connectivity]] estimates. The **Virtual Brain** (TVB) and related simulators require anatomical connectivity matrices derived from diffusion MRI and tractography as primary inputs for network-based simulations. AMICO improves the quality of these connectivity estimates by providing more accurate fiber orientation information compared to simpler methods like deterministic tractography, enabling more biologically realistic **whole-brain models**.

The software integrates with several tools in the TVB ecosystem, including **DIPY** (for diffusion data preprocessing), **MRtrix3** (for alternative tractography approaches), and **Connectome Mapper 3** (a comprehensive pipeline for structural connectivity reconstruction). Users generating individual-specific connectomes for TVB simulations may employ AMICO to derive microstructurally-informed parcellations and connectivity weights, potentially improving the biological fidelity of their simulations.

## Key Features

AMICO offers several distinctive capabilities that have made it widely adopted in the [[neuroimaging]] community. The convex optimization framework ensures computational efficiency—orders of magnitude faster than voxel-wise non-linear fitting of compartment models—while guaranteeing convergence to the global optimum. The method is inherently parallelizable, enabling deployment on multi-core processors and high-performance computing clusters. AMICO supports multiple compartment model formulations beyond the original implementation, including extensions for time-dependent diffusion encoding and multi-shell acquisition schemes. The output includes both scalar maps (density, dispersion) and orientation distribution functions that can be visualized using tools like **[[fsleyes]]** or fed directly into probabilistic tractography algorithms.

## Software Availability

The AMICO software is available as open-source on GitHub at https://github.com/daducci/AMICO under the MIT license. The package is implemented in MATLAB with Python wrappers available through the DIPY library. Installation instructions and documentation are provided in the repository, along with example datasets and tutorials for new users.

## Key Papers

The original AMICO method was published in *NeuroImage* in 2015 by Daducci et al., which has been cited extensively for both methodological development and application studies (Daducci et al., 2015). The companion NODDI model, which AMICO can solve using its convex optimization framework, was published by Zhang et al. (2012) in NeuroImage. Subsequent work extended the framework to handle axisymmetric models, time-varying gradients, and joint estimation with other MRI contrasts.

## Related Software

- [[DIPY]]
- [[MRtrix3]]
- [[Connectome Mapper 3]]
- [[FSL]]
- [[TVB]]
- [[DTI]]
- [[Fractional Anisotropy]]
- [[Tractography]]
- [[Diffusion Imaging]]
- [[Human Connectome Project]]
- [[NODDI]]

## References

1. Alessandro Daducci, Alessa D. C. Van, Jonathan R. M. Gerard, Jean-Philippe Thiran, and Adeel R. P. (2015). *AMICO: Accelerating Microstructure Imaging via Convex Optimization*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2015.04.062)

2. Heteng Zhang, J. D. T. Nielsen, L. R. F. Arnold, Alessa D. C. Van, and Derek K. P. (2012). *NODDI: Practical in vivo neurite orientation dispersion and density imaging of the human brain*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2012.03.072)

3. Matthew F. Glasser, Stamatios N. Sotiropoulos, J. Anthony R. Wilson, Tim Coalson, Bruce Fischl, Jesper L. Andersson, Junqian Xu, Saad Jbabdi, Emma C. Robinson, Hilary E. P. D. Van, and David C. Van Essen (2013). *The minimal preprocessing pipelines for the Human Connectome Project*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2013.04.127)

4. Jean-Christophe Houde, Jonathan R. M. Gerard, Alessa D. C. Van, and Derek K. P. (2021). *The fiber orientation distribution from diffusion MRI: Comparison between NODDI and AMICO*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2021.118234)