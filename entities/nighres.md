---
title: Nighres
created: 2025-01-15
updated: 2026-05-01
type: software
tags: [software-neuroimaging, neuroimaging-mri, laminar-imaging, cortical-analysis, software-python, parcellation, software-dipy, software-ants]
sources: [Marques2010, HCP2013, Weiner2014, Schiffer2017, Bazin2011, Greve2013]
---

## Overview

Nighres is an open-source Python library designed for high-resolution neuroimaging data processing, with a particular focus on laminar and subcortical structure analysis. The name derives from "NIGh RESolution," reflecting its primary purpose of extracting fine-grained structural information from high-resolution magnetic resonance imaging (MRI) scans. The library provides automated segmentation and parcellation tools that complement broader neuroimaging processing workflows, enabling researchers to probe mesoscale brain anatomy that is obscured in conventional resolution data.

## Motivation and Context

Traditional neuroimaging analysis pipelines often operate on voxel sizes of 1–2 mm, which provides adequate sensitivity for whole-brain analyses but sacrifices anatomical detail at the laminar and sublaminar levels. Cortical layer analysis requires voxel sizes on the order of 0.5–0.7 mm, achieved with specialized protocols like MP2RAGE or multi-shell diffusion imaging [@Marques2010]. However, processing these high-resolution datasets introduces substantial computational challenges and requires specialized algorithms that account for partial volume effects, variable Rician noise profiles, and the complex geometry of cortical laminae.

Nighres emerged to address this gap, providing validated implementations of algorithms specifically designed for laminar analysis that had previously been available only as disparate MATLAB scripts or commercial solutions. By wrapping these methods in a Python library with a unified API, Nighres enables reproducible, large-scale studies of cortical architecture in both research and clinical contexts. The library fits within a broader ecosystem of [[neuroimaging]] tools—particularly [[ANTs]] for registration, [[FreeSurfer]] for surface-based analysis, and [[dipy]] for diffusion processing—while offering functionality that these general-purpose packages do not provide.

## Key Features

Nighres implements several core algorithms for high-resolution brain analysis. **Laminar segmentation** employs intensity profiles and boundary detection methods to identify cortical depth levels from the pial surface to the [[white-matter]] boundary, producing anywhere from 3 to 10+ equally-spaced layers depending on the chosen parameterization. Unlike histological Brodmann areas which represent cytoarchitectonically distinct regions with known functional properties, Nighres segments geometric depth levels—equivolumetric or equidistant surfaces—useful for modeling the systematic variation in receptor density, myelin content, and connectional patterns across cortical thickness [@Bazin2011; @Weiner2014]. The library includes implementations of depth-based layering methods using Bayesian probability estimation and active contour approaches.

**Subcortical segmentation** extends classical atlas-based approaches with refined boundary detection for structures like the hippocampus, thalamus, and basal ganglia. These routines are particularly valuable for [[whole-brain modeling]] applications where precise definitions of subcortical nuclei are required for accurate [[neural-mass]] model placement.

**Probabilistic parcellation** tools generate cortical parcellations that respect laminar boundaries, producing "layer-specific" atlases rather than the conventional surface-based parcels. This feature supports analyses of laminar [[functional-connectivity]] and [[effective-connectivity]] that distinguish between feedforward and feedback connections based on their laminar signatures.

The library maintains compatibility with standard neuroimaging formats (NIfTI, CIFTI) and integrates with [[BIDS]]-compliant processing pipelines through [[nipype]] interfaces.

## Relationship to TVB

Nighres provides anatomical precision that complements [[whole-brain modeling]] frameworks like [[The Virtual Brain]] (TVB). TVB requires detailed structural descriptions—including regional volumes, cortical thickness, and connectivity estimates—to configure [[neural-mass models]] and map them onto individual subject anatomy. Nighres-derived laminar boundaries and subcortical segmentations can inform TVB's anatomical priors, particularly for models targeting the detailed cortical microcircuitry that mediates [[brain-oscillations]] and [[resting-state]] dynamics.

In practice, a typical TVB preprocessing pipeline might use Nighres to extract high-resolution cortical and subcortical segmentations from a subject's MP2RAGE or HCP-style acquisition, then pass these geometric constraints to TVB's cortical mesh generation and region definition modules.

## Related Software

Nighres operates within a broader ecosystem of [[neuroimaging]] processing tools:

- [[ANTs]] provides the registration and normalization foundation that Nighres builds upon [@Avants2009]
- [[FreeSurfer]] remains the gold standard for automated cortical reconstruction and is often run in parallel with Nighres
- [[dipy]] handles diffusion MRI processing including tractography
- [[nilearn]] offers machine-learning utilities for brain decoding that integrate with Nighres outputs
- [[BrainVISA]] provides related morphometry tools in the French neuroimaging tradition
- The [[Human Connectome Project]] protocols and the [[HCP-dataset]] provide the high-resolution acquisitions that Nighres excels at processing, particularly the 0.7 mm HCP "Myelin" acquisitions that are well-suited for laminar analysis [@Glasser2013]

## Key Algorithms and Technical Details

The core Nighres laminar segmentation algorithm operates by modeling the cortical column as a series of nested surfaces. Given an intensity profile $I(x,y,z)$ through the cortical ribbon, the algorithm seeks surfaces at positions $\mathbf{s}_1, \mathbf{s}_2, \ldots, \mathbf{s}_N$ corresponding to layer boundaries. This is formulated as a maximum a posteriori estimation problem:

$$\arg\max_{\mathbf{s}} P(\mathbf{s}|I) \propto P(I|\mathbf{s}) P(\mathbf{s})$$

where the likelihood term $P(I|\mathbf{s})$ models the expected intensity gradient at each boundary, and the prior $P(\mathbf{s})$ enforces smoothness constraints and laminar ordering. Boundary detection employs a combination of intensity gradient magnitude and second-derivative (Laplacian) analysis, with the Laplacian-of-Gaussian approach particularly effective for identifying the often-subtle intensity transitions between layers. The algorithm outputs both hard segmentations (deterministic layer boundaries) and probabilistic tissue maps that quantify uncertainty at each voxel—critical for interpreting results in the presence of partial volume mixing that is inevitable at laminar resolutions.

## Open Questions and Limitations

Several challenges remain in the field that Nighres partially addresses but does not fully resolve. **Validation against ground truth** remains difficult because histological references are available for only a small number of brains, and the tissue fixation process introduces shrinkage artifacts that complicate quantitative comparison [@Greve2013]. **Cross-scanner robustness** is an active concern: algorithms optimized for 7T MP2RAGE data may degrade when applied to 3T acquisitions or alternative contrast weightings. **Inter-subject variability** in laminar architecture is substantial, yet most atlases currently provide only population-average templates rather than informative priors for individual subjects.

Future development directions include integration with [[Bayesian]] inference frameworks for more principled uncertainty quantification, incorporation of [[machine-learning]] approaches (particularly deep learning for boundary detection), and extensions to handle [[functional-connectivity]] at laminar resolution using concurrent [[fMRI]] and [[MEG]] acquisitions.

## Key Papers

The following publications form the foundation for Nighres and its underlying methodology:

1. **Marques, J.P., et al. (2010)**. MP2RAGE: a self-bipolarizing sequence for fast and accurate T1 mapping at 7T. *Magnetic Resonance in Medicine*, 64(6), 1554-1568. [@Marques2010]

2. **Glasser, M.F., et al. (2013)**. The Human Connectome Project's neuroimaging approach. *Nature Neuroscience*, 16(9), 1213-1221. [@HCP2013]

3. **Weiner, K.S., et al. (2014)**. The modular architecture of the cerebral cortex. *Brain Structure and Function*, 219(1), 147-164. [@Weiner2014]

4. **Schiffer, C., et al. (2017)**. Nighres: a toolbox for high-resolution neuroimaging. *Frontiers in Neuroinformatics*, 11, 47. [@Schiffer2017]

5. **Bazin, P.L., et al. (2011)**. A computational framework for ultra-high resolution cortical segmentation at 7 Tesla. *Proceedings of the 17th Annual Meeting of the Organization for Human Brain Mapping*. [@Bazin2011]

6. **Greve, D.N., et al. (2013)**. Multi-modal correspondence between MRI and histology in the JHU cadaver study. *NeuroImage*, 66, 144-151. [@Greve2013]

---

## References

[@Marques2010]: Marques, J.P., et al. (2010). MP2RAGE: a self-bipolarizing sequence for fast and accurate T1 mapping at 7T. *Magnetic Resonance in Medicine*, 64(6), 1554-1568.

[@HCP2013]: Glasser, M.F., et al. (2013). The Human Connectome Project's neuroimaging approach. *Nature Neuroscience*, 16(9), 1213-1221.

[@Weiner2014]: Weiner, K.S., et al. (2014). The modular architecture of the cerebral cortex. *Brain Structure and Function*, 219(1), 147-164.

[@Schiffer2017]: Schiffer, C., et al. (2017). Nighres: a toolbox for high-resolution neuroimaging. *Frontiers in Neuroinformatics*, 11, 47.

[@Bazin2011]: Bazin, P.L., et al. (2011). A computational framework for ultra-high resolution cortical segmentation at 7 Tesla. *Proceedings of the 17th Annual Meeting of the Organization for Human Brain Mapping*.

[@Greve2013]: Greve, D.N., et al. (2013). Multi-modal correspondence between MRI and histology in the JHU cadaver study. *NeuroImage*, 66, 144-151.

[@Avants2009]: Avants, B.B., et al. (2009). Symmetric diffeomorphic image registration with cross-correlation: evaluating automated labeling of elderly, neurodegenerative, and adult brains. *IEEE Transactions on Medical Imaging*, 28(2), 254-269.