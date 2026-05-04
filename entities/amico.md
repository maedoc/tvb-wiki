---
created: 2026-04-29
sources:
- raw/papers/semanticscholar-d8b81edc13b4.md
- raw/papers/semanticscholar-c393c4c4a671.md
- raw/papers/semanticscholar-deecd9987645.md
- raw/papers/semanticscholar-d94ac445ea77.md
- raw/papers/semanticscholar-67bfc55dcfc8.md
- raw/papers/arxiv-2503.07263.md
- raw/papers/semanticscholar-2c08584d27f9.md
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
updated: '2026-05-04'
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

1. M. Cottaar, Zhiyu Zheng, Karla L. Miller, Benjamin C. Tendler, Saad Jbabdi. (2025). *Multi-modal Monte Carlo MRI simulator of tissue microstructure*. bioRxiv. [DOI](https://doi.org/10.1162/IMAG.a.1177)
2. Jorge Barrios, Evan Porter, D. Capaldi, T. Upadhaya, William C. Chen, Julian R. Perks, Aditya Apte, M. Aristophanous, Eve LoCastro, Dylan Hsu, Payton H Stone, J. Villanueva-Meyer, Gilmer Valdes, Fei Jiang, Michael Maddalena, A. Ballangrud, K. Prezelski, Hui Lin, Jinger Y. Sun, M. K. Aldin, O. Chau, B. Ziemer, M. Seaberg, P. Sneed, J. Nakamura, L. Boreta, S. Fogh, D. Raleigh, J. Chew, H. Vasudevan, S. Cha, Christopher Hess, Ruben Fragoso, David B. Shultz, L. Pike, S. Hervey-Jumper, Derek S. Tsang, P. Theodosopoulos, Daniel Cooke, Stanley H Benedict, Ke Sheng, Jan Seuntjens, Catherine Coolens, J. Deasy, S. Braunstein, Olivier Morin. (2025). *Multi-institutional atlas of brain metastases informs spatial modeling for precision imaging and personalized therapy*. Nature Communications. [DOI](https://doi.org/10.1038/s41467-025-59584-7)
3. Daniel J. Asay, Timothy M. O'Keefe, Randy L. Buckner, Ross W Mair. (2025). *DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images*. Journal of Open Source Software. [DOI](https://doi.org/10.21105/joss.06974)
4. Maya Iratni, Amirali Abdullah, Mariam Aldhaheri, Omar Elharrouss, Alaa A. Abd-alrazaq, Zahiriddin Rustamov, Nazar Zaki, Rafat Damseh. (2025). *Transformers for Neuroimage Segmentation: Scoping Review*. Journal of Medical Internet Research. [DOI](https://doi.org/10.2196/57723)
5. Benjamin C. Tendler, S. Warrington, M. K. Selim, Wenchuan Wu, G. Adriany, Edward J. Auerbach, Alexander Bratch, Hamza Farooq, Noam Harel, Sarah R. Heilbronner, Saad Jbabdi, Steve Jungst, Christophe Lenglet, A. M. Manea, Steen Moeller, Franco Pestilli, P. Pisharady, K. Ugurbil, Matt Waks, E. Yacoub, S. Sotiropoulos, Karla L. Miller, J. Zimmermann. (2025). *Diffusion-weighted steady-state free precession imaging in the ex vivo macaque brain on a 10.5T human MRI scanner*. bioRxiv. [DOI](https://doi.org/10.64898/2025.12.12.694017)
6. Haolin He, Ce Zhu, Le Zhang, Yipeng Liu, Xiao Xu, Yuqian Chen, L. Zekelman, Jarrett Rushmore, Y. Rathi, N. Makris, L. O’Donnell, Fan Zhang. (2025). *DeepNuParc: A novel deep clustering framework for fine-scale parcellation of brain nuclei using diffusion MRI tractography*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2025.121421)
7. Jon Haitz Legarreta, Zhou Lan, Yuqian Chen, Fan Zhang, Edward H. Yeterian, N. Makris, Jarrett Rushmore, Y. Rathi, L. O’Donnell. (2025). *Towards an Informed Choice of Diffusion MRI Image Contrasts for Cerebellar Segmentation*. bioRxiv. [DOI](https://doi.org/10.1002/hbm.70317)