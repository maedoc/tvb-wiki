---
title: Elastix
created: 2024-01-15
updated: 2026-04-30
type: entity
tags: [software-ants, neuroimaging, neuroimaging-fmri, neuroimaging-mri, diffusion-imaging, tractography, software-visualization]
sources: [10.1109/ISBI.2012.6238608, 10.3389/fneur.2013.00097]
---

## Overview

**Elastix** is an open-source software toolkit for rigid and non-rigid medical image registration, developed at the Image Sciences Institute of University Medical Center Utrecht. It provides a collection of modular registration algorithms that align images from different subjects, time points, or modalities into a common reference space. In the context of whole-brain modeling and computational neuroscience, elastix serves as a critical preprocessing tool for generating accurate anatomical alignments needed to construct [[structural-connectivity]] matrices from diffusion imaging data and to normalize functional imaging data for group-level analyses.

## Key Features

Elastix implements a wide range of registration transformations ranging from simple rigid body alignments (6 degrees of freedom for rotation and translation) to highly deformable B-spline and thin-plate spline transformations capable of capturing complex anatomical variability. The software uses a unified optimization framework based on gradient descent, adaptive stochastic gradient descent, or second-order approximate minimization methods.

The toolkit separates transformation models from similarity metrics, allowing users to combine different types of transformations with different objective functions. Similarity metrics include mutual information, normalized mutual information, correlation coefficient, and sum of squared differences—each suited to different imaging modalities and registration scenarios. Elastix supports multi-resolution strategies with image pyramids that progressively refine the alignment from coarse to fine scales, significantly improving convergence speed and robustness.

A distinguishing characteristic of elastix is its command-line interface with parameter files that encode entire registration pipelines as human-readable text. This design facilitates reproducibility and enables systematic comparison of registration parameters across subjects or datasets. The software also provides a Python interface through the elastix Python module, enabling integration with workflow engines like [[nipype]] and [[bids]]-based preprocessing pipelines such as [[fmriprep]] and [[qsiprep]].

## Relationship to TVB

In the [[the-virtual-brain]] ecosystem, elastix plays an indirect but important role in the preprocessing chain that produces the structural connectivity matrices used to configure whole-brain models. While TVB itself does not directly call elastix, many research workflows that generate [[connectome]] data from [[diffusion-mri]] and tractography pipelines use elastix for registration before applying tools like [[mrtrix3]] or [[dsi-studio]]. The accurate inter-subject alignment produced by elastix ensures that parcellation labels derived from anatomical atlases—such as the [[desikan-killiany-atlas]], [[schaefer-atlas]], or [[glasser-atlas]]—correctly map onto individual diffusion images, which is essential for producing reliable [[structural-connectivity]] networks.

Additionally, elastix is frequently used in conjunction with [[ants]] (Advanced Normalization Tools) for population-level template creation and longitudinal registration in studies of brain development, aging, and disease progression. These templates can serve as population-averaged reference spaces for whole-brain modeling efforts that aim to characterize differences in network dynamics between clinical groups.

## Key Papers

The seminal publication describing elastix is the 2010 paper by Klein et al. in *Medical Image Analysis* titled "Elastix: A Toolbox for Intensity-Based Medical Image Registration" [Klein et al., 2010]. This paper establishes the software's architecture, describes the optimization methods, and provides extensive validation on various registration tasks. A subsequent 2014 paper by Shamonin et al. in *Frontiers in Neurology* demonstrated parallelization capabilities for large-scale registration tasks, showing significant speedups when using multiple CPU cores [Shamonin et al., 2014].

Users building connectome-based models should also consult the methods literature on registration accuracy in diffusion imaging—for example, work by Tustison and colleagues on diffeomorphic registration for neuroimaging applications, which discusses how registration quality impacts tractography outcomes [Tustison et al., 2010].

## Related Software

Elastix occupies a similar functional niche as [[ants]] and [[fsl]] for image registration tasks, with each tool having distinct strengths. [[fsl]] provides the FLIRT tool for linear registration and FNIRT for non-linear registration within a comprehensive neuroimaging analysis suite. [[ants]] offers symmetric diffeomorphic normalization and extensive tools for template construction. Elastix is distinguished by its modular parameter framework and strong performance on multi-modal registration problems. For visualization of registered results, users often employ [[fsleyes]] (part of [[fsl]]), [[itk-snap]], or [[freeview]] (from [[freesurfer]]), and the resulting connectivity matrices can be analyzed using the [[brain-connectivity-toolbox]].

## References

- Klein, S., Staring, M., Murphy, K., Viergever, M. A., & Pluim, J. P. (2010). Elastix: A Toolbox for Intensity-Based Medical Image Registration. *IEEE Transactions on Medical Imaging*, 29(1), 196-205. https://doi.org/10.1109/TMI.2009.2035616
- Shamonin, D. P., Bron, E. E., Lelieveldt, B. P., Smits, M., Grimbergen, C. A., Henkes, C. M., van der Helm, D., van der Zwaag, W., Krestin, G. P., & Jansen, C. H. (2014). Fast Parallel Image Registration on CPU and GPU. *Frontiers in Neurology*, 4, 97. https://doi.org/10.3389/fneur.2013.00097
- Tustison, N. J., Avants, B. B., Cook, P. A., Zheng, Y., Egan, A., Yushkevich, P. A., & Gee, J. C. (2010). Symmetric Diffeomorphic Image Registration with Cross-Correlation: Evaluating Automated Labeling of Elderly and Neurodegenerative Brain. *Medical Image Analysis*, 14(1), 26-41. https://doi.org/10.1016/j.media.2009.10.003