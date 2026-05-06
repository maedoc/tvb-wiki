---
created: 2025-01-15
sources:
- https://doi.org/10.5281/zenodo.4571808
- https://bids-apps.neuroimaging.io/
- https://doi.org/10.3389/fninf.2021.00037
- raw/papers/doi-10-1016-j-neuroimage-2015-10-019.md
- raw/papers/doi-10-1038-s41592-018-0235-4.md
- raw/papers/doi-10-1371-journal-pcbi-1005209.md
tags:
- software-bids-apps
- diffusion-imaging
- neuroimaging-dti
- tractography
- structural-connectivity
- software-nipype
- bids-derivatives
- preprocessing
title: dMRIprep
type: entity
updated: '2026-05-06'
---

dMRIprep is a [[bids]]-compatible preprocessing pipeline for diffusion magnetic resonance imaging (dMRI) data, designed to produce analysis-ready derivatives suitable for subsequent [[tractography]] and structural [[connectivity]] analysis. Part of the growing family of [[bids-apps]] that includes the more widely developed [[fmriprep]], dMRIprep aims to automate the complex series of correction steps required to transform raw diffusion-weighted images into clean, motion-corrected outputs suitable for quantitative analysis. The pipeline implements a philosophy of minimal manual intervention while maintaining [[reproducibility]] and transparent reporting of processing steps (Esteban et al., 2019).

## Overview

dMRIprep addresses a fundamental challenge in [[diffusion-mri]] analysis: the raw images acquired on MRI scanners suffer from various artifacts including head motion between volumes, eddy current distortions induced by the rapidly switching diffusion gradients, bias field inhomogeneities inherent to echo-planar imaging, and spatial distortions particularly problematic at air-tissue boundaries (Andersson & Sotiropoulos, 2016). Manually correcting these artifacts is time-consuming, requires substantial expertise, and introduces non-reproducibility across studies. dMRIprep automates this pipeline using established algorithms from the neuroinformatics community while maintaining full provenance tracking through the BIDS (Brain Imaging Data Structure) specification (Gorgolewski et al., 2016).

The pipeline is built on [[nipype]] for workflow orchestration, ensuring modularity and allowing users to swap individual processing components if needed. Internally, it leverages algorithms from [[fsl]] (including eddy and DTIFIT), [[ants]] for registration and bias field correction (Tustison et al., 2010), and [[mr-trix3]] for additional processing steps. All outputs follow the BIDS Derivatives specification, making them immediately compatible with downstream analysis tools including tractography packages, connectivity estimation frameworks, and statistical analysis pipelines.

## Key Preprocessing Steps

The dMRIprep pipeline proceeds through several distinct processing stages, each addressing specific artifacts or preparing data for subsequent analysis. The workflow begins with motion correction, where eddy current-induced distortions cause inter-volume misalignment that must be corrected through rigid body registration to a reference b=0 image. dMRIprep uses boundary-based registration or mutual information-based rigid alignment depending on the data quality and available anatomical information.

Following motion correction, the pipeline applies eddy current correction, which accounts for the differential distortions induced by the large diffusion gradients. This correction is typically performed using FSL's eddy tool, which also models and corrects for residual motion effects and susceptibility distortions when paired with a reversed phase-encoded b=0 image (Andersson et al., 2003). The bias field correction step removes intensity inhomogeneities caused by radiofrequency coil profiles and magnetic field imperfections, improving the accuracy of subsequent quantitative metrics like [[fractional-anisotropy]].

The pipeline includes robust skull stripping using [[hd-bet]] (Koch et al., 2021) or similar tools to isolate brain tissue from surrounding tissue, which is critical for accurate tractography. Finally, diffusion tensor fitting produces scalar maps including fractional anisotropy (FA), mean diffusivity (MD), and principal diffusivity maps that characterize the underlying tissue microstructure.

## Relationship to TVB

dMRIprep plays an important role in [[whole-brain modeling]] workflows that require [[structural connectivity]] matrices derived from [[diffusion-imaging]] data. The pipeline's outputs—particularly the motion-corrected, distortion-corrected diffusion-weighted images and derived tensor metrics—serve as inputs for tractography algorithms that estimate white matter pathways between brain regions.

In TVB workflows, dMRIprep-processed data typically feeds into tractography tools such as [[mr-trix3]]-connectome, MRTrix3, or DIPY (Garyfallidis et al., 2014) to generate streamlines representing white matter connections. These streamlines are then used to construct [[structural connectivity]] matrices where connection weights reflect either streamline counts, fractional anisotropy values, or other microstructural metrics. The resulting connectivity matrices form the anatomical scaffold for [[whole-brain]] simulations in [[the-virtual-brain]], enabling personalized brain models that integrate individual anatomical connectivity.

The BIDS-compliant outputs from dMRIprep ensure compatibility with TVB's data handling utilities and facilitate reproducible preprocessing pipelines across research sites. Given that TVB supports multiple parcellation schemes including [[aal-atlas]], [[desikan-killiany-atlas]], and [[brainnetome-atlas]], dMRIprep's standardized outputs can be readily mapped to any desired brain parcellation for connectivity matrix construction.

## Key Papers

- Andersson, J. L., & Sotiropoulos, S. N. (2016). An integrated approach to correction for off-resonance effects and subject movement in diffusion MR imaging. NeuroImage, 125, 1063-1078. https://doi.org/10.1016/j.neuroimage.2015.10.019
- Esteban, O., Markiewicz, C. J., Poldrack, R. A., & Gorgolewski, K. (2019). fMRIPrep: a robust preprocessing pipeline for functional MRI. Nature Methods, 16(1), 111-114. https://doi.org/10.1038/s41592-018-0235-4
- Gorgolewski, K., Auer, T., Calhoun, V. D., et al. (2016). BIDS apps: Improving ease of use, accessibility, and reproducibility of [[neuroimaging]] data analysis methods. PLOS Computational Biology, 13(3), e1005209. https://doi.org/10.1371/journal.pcbi.1005209

## Limitations and Alternatives

dMRIprep represents an active effort to bring BIDS-app convenience to diffusion MRI preprocessing, but it is important to note its current developmental status and limitations. Unlike its sibling [[fmriprep]], which has undergone extensive validation and widespread community adoption, dMRIprep remains a less mature pipeline with a smaller user base and fewer validation studies.

Users should consider alternative pipelines depending on their specific needs: **QSIPrep** (Quantitative Susceptibility Imaging preprocessing) provides comprehensive diffusion MRI preprocessing with support for multiple reconstruction methods including q-space and mapmap approaches (Cieslak et al., 2021). **[[mrtrix3]]'s own preprocessing pipeline** (Tournier et al., 2019) offers integrated motion correction, intensity normalization, and response function estimation within a unified software ecosystem. **DIPY** (Garyfallidis et al., 2014) provides modular tools for users who prefer custom-built preprocessing workflows with fine-grained control over each step.

The choice between pipelines depends on the specific acquisition protocol, reconstruction methodrequirements, and downstream analysis goals. Researchers are encouraged to validate preprocessing outputs visually and consider reporting preprocessing choices thoroughly in methodological descriptions.

## Related Software

dMRIprep exists within a broader ecosystem of BIDS-apps and diffusion imaging tools. Related preprocessing pipelines include [[fmriprep]] for functional MRI, [[qsiprep]] for quantitative susceptibility imaging, and [[smriprep]] for structural MRI. For tractography specifically, users often combine dMRIprep outputs with [[mr-trix3]], [[dsi-studio]], or [[camino]] to generate streamline reconstructions suitable for connectivity analysis.

Related analysis frameworks include [[tvb-nr]] for network reconstruction, [[connectome-workbench]] for visualization, and [[afq]] for automated fiber quantification.

## References

1. (authors unknown). *An integrated approach to correction for off-resonance effects and subject movement in diffusion MR imaging*.
2. (authors unknown). *fMRIPrep: a robust preprocessing pipeline for functional MRI*.
3. (authors unknown). *BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods*.