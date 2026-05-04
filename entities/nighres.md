---
created: 2025-01-15
sources:
- 10.1093/gigascience/giy082
- 10.1016/j.neuroimage.2013.03.078
- 10.1016/j.neuroimage.2014.03.032
- 10.1016/j.neuroimage.2015.10.001
- raw/papers/huntenburg-2018.md
tags:
- software-neuroimaging
- neuroimaging-mri
- laminar-imaging
- cortical-analysis
- software-python
- parcellation
- software-dipy
- software-ants
title: Nighres
type: software
updated: '2026-05-04'
---

## Overview

Nighres is an open-source Python library designed for high-resolution neuroimaging data processing, with a particular focus on laminar and subcortical structure analysis. The name derives from "NIGh RESolution," reflecting its primary purpose of extracting fine-grained structural information from high-resolution magnetic resonance imaging (MRI) scans. The library provides automated segmentation and [[parcellation]] tools that complement broader neuroimaging processing workflows, enabling researchers to probe mesoscale brain anatomy that is obscured in conventional resolution data [[1]].

## Motivation and Context

Traditional neuroimaging analysis pipelines often operate on voxel sizes of 1–2 mm, which provides adequate sensitivity for [[whole-brain]] analyses but sacrifices anatomical detail at the laminar and sublaminar levels. Cortical layer analysis requires voxel sizes on the order of 0.5–0.7 mm, achieved with specialized protocols like MP2RAGE or multi-shell [[diffusion-imaging]] [[2]]. However, processing these high-resolution datasets introduces substantial computational challenges and requires specialized algorithms that account for partial volume effects, variable Rician noise profiles, and the complex geometry of cortical laminae [[3]].

Nighres emerged to address this gap, providing validated implementations of algorithms specifically designed for laminar analysis that had previously been available only as disparate MATLAB scripts or commercial solutions. By wrapping these methods in a Python library with a unified API, Nighres enables reproducible, large-scale studies of cortical architecture in both research and clinical contexts. The library fits within a broader ecosystem of [[neuroimaging]] tools—particularly [[ANTs]] for registration, [[pysurfer]] for surface-based analysis, and [[dipy]] for diffusion processing—while offering functionality that these general-purpose packages do not provide.

## Key Features

Nighres implements several core algorithms for high-resolution brain analysis. **Laminar segmentation** employs intensity profiles and boundary detection methods to segment the cortex into multiple depth levels (typically 4–20 layers depending on resolution), using either Bayesian probability estimation or active contour approaches. The library includes implementations of the equivolumetric layering method, which accounts for cortical curvature to produce anatomically meaningful depth estimates [[4]]. This approach is distinct from histological layer identification—Nighres generates a coordinate system for measuring cortical depth rather than directly identifying cytoarchitectonic Brodmann areas.

**Subcortical segmentation** extends classical atlas-based approaches with refined boundary detection for structures like the hippocampus, thalamus, and basal ganglia. These routines are particularly valuable for [[whole-brain modeling]] applications where precise definitions of subcortical nuclei are required for accurate [[neural-mass]] model placement.

**Probabilistic parcellation** tools generate cortical parcellations that respect laminar boundaries, producing "layer-specific" atlases rather than the conventional surface-based parcels. This feature supports analyses of laminar [[functional-connectivity]] and [[effective-connectivity]] that distinguish between feedforward and feedback connections based on their laminar signatures [[5]].

The library maintains compatibility with standard neuroimaging formats ([[nifti]], [[cifti]]) and integrates with [[BIDS]]-compliant processing pipelines through [[nipype]] interfaces.

## Relationship to TVB

Nighres provides anatomical precision that complements [[whole-brain modeling]] frameworks like [[The Virtual Brain]] (TVB). TVB requires detailed structural descriptions—including regional volumes, cortical thickness, and connectivity estimates—to configure [[neural-mass models]] and map them onto individual subject anatomy. Nighres-derived laminar boundaries and subcortical segmentations can inform TVB's anatomical priors, particularly for models targeting the detailed cortical microcircuitry that mediates [[brain-oscillations]] and [[resting-state]] dynamics.

In practice, a typical TVB preprocessing pipeline might use Nighres to extract high-resolution cortical and subcortical segmentations from a subject's MP2RAGE or HCP-style acquisition, then pass these geometric constraints to TVB's cortical mesh generation and region definition modules.

## Related Software

Nighres operates within a broader ecosystem of [[neuroimaging]] processing tools:

- [[ANTs]] provides the registration and normalization foundation that Nighres builds upon
- [[pysurfer]] remains the gold standard for automated cortical reconstruction and is often run in parallel with Nighres
- [[dipy]] handles [[diffusion-mri]] processing including [[tractography]]
- [[nilearn]] offers machine-learning utilities for brain decoding that integrate with Nighres outputs
- [[BrainVISA]] provides related morphometry tools in the French neuroimaging tradition
- The [[Human [[connectome]] Project]] protocols and the [[HCP-dataset]] provide the high-resolution acquisitions that Nighres excels at processing
- **LAYNII** provides complementary tools for laminar fMRI analysis, particularly suited for handling partial brain coverage [[6]]

## Key Algorithms and Technical Details

The core Nighres laminar segmentation algorithm operates by modeling the cortical column as a series of nested surfaces. Given an intensity profile $I(x,y,z)$ through the cortical ribbon, the algorithm seeks surfaces at positions $\mathbf{s}_1, \mathbf{s}_2, \ldots, \mathbf{s}_N$ corresponding to layer boundaries. This is formulated as a maximum a posteriori estimation problem:

$$\arg\max_{\mathbf{s}} P(\mathbf{s}|I) \propto P(I|\mathbf{s}) P(\mathbf{s})$$

where the likelihood term $P(I|\mathbf{s})$ models the expected intensity gradient at each boundary, and the prior $P(\mathbf{s})$ enforces smoothness constraints and laminar ordering. Boundary detection employs a combination of intensity gradient magnitude and second-derivative (Laplacian) analysis, with the Laplacian-of-Gaussian approach particularly effective for identifying the often-subtle intensity transitions between layers. The algorithm outputs both hard segmentations (deterministic layer boundaries) and probabilistic tissue maps that quantify uncertainty at each voxel—critical for interpreting results in the presence of partial volume mixing that is inevitable at laminar resolutions [[7]].

The equivolumetric layering approach, originally developed by Waehnert et al. [[4]], accounts for the fact that histological layer thickness varies with cortical curvature. Rather than using equidistant spacing between layers (which would produce artifacts in highly folded regions), the equivolumetric model preserves the relative volume of each cortical segment, providing a more accurate representation of intracortical organization.

## Open Questions and Limitations

Several challenges remain in the field that Nighres partially addresses but does not fully resolve. **Validation against ground truth** remains difficult because histological references are available for only a small number of brains, and the tissue fixation process introduces shrinkage artifacts that complicate quantitative comparison [[8]]. **Cross-scanner robustness** is an active concern: algorithms optimized for 7T MP2RAGE data may degrade when applied to 3T acquisitions or alternative contrast weightings. **Inter-subject variability** in laminar architecture is substantial, yet most atlases currently provide only population-average templates rather than informative priors for individual subjects.

Future development directions include integration with [[Bayesian]] inference frameworks for more principled uncertainty quantification, incorporation of [[machine-learning]] approaches (particularly deep learning for boundary detection), and extensions to handle [[functional-connectivity]] at laminar resolution using concurrent [[fMRI]] and [[MEG]] acquisitions.

## Key Papers

1. Huntenburg JM, Steele CJ, Bazin P-L (2018) Nighres: processing tools for high-resolution neuroimaging. GigaScience 7: giy082. https://doi.org/10.1093/gigascience/giy082 [[1]]

2. Bazin PL, Weiss M, Dinse J, et al. (2014) A computational framework for ultra-high resolution cortical segmentation at 7Tesla. NeuroImage 93(2): 201-209. https://doi.org/10.1016/j.neuroimage.2013.03.077 [[3]]

3. Waehnert MD, Dinse J, Weiss M, et al. (2014) Anatomically motivated modeling of cortical laminae. NeuroImage 93(2): 210-220. https://doi.org/10.1016/j.neuroimage.2013.03.078 [[4]]

4. Waehnert MD, Dinse J, Schäfer A, et al. (2016) A subject-specific framework for in vivo myeloarchitectonic analysis using high resolution quantitative MRI. NeuroImage 125: 94-107. https://doi.org/10.1016/j.neuroimage.2015.10.001 [[7]]

5. Keuken MC, Bazin PL, Crown L, et al. (2014) Quantifying inter-individual anatomical variability in the subcortex using 7T structural MRI. NeuroImage 94: 40-46. https://doi.org/10.1016/j.neuroimage.2014.03.032 [[8]]

## References

[[1]] Huntenburg JM, Steele CJ, Bazin P-L (2018) Nighres: processing tools for high-resolution neuroimaging. GigaScience 7: giy082. https://doi.org/10.1093/gigascience/giy082

[[2]] Marques JP, Kober T, Krueger G, et al. (2010) MP2RAGE, a self bias-field corrected sequence for improved segmentation and T1-mapping at high field. NeuroImage 49(2): 1271-81. https://doi.org/10.1016/j.neuroimage.2009.10.002

[[3]] Bazin PL, Weiss M, Dinse J, et al. (2014) A computational framework for ultra-high resolution cortical segmentation at 7Tesla. NeuroImage 93(2): 201-209. https://doi.org/10.1016/j.neuroimage.2013.03.077

[[4]] Waehnert MD, Dinse J, Weiss M, et al. (2014) Anatomically motivated modeling of cortical laminae. NeuroImage 93(2): 210-220. https://doi.org/10.1016/j.neuroimage.2013.03.078

[[5]] Huber L, Handwerker DA, Jangraw DC, et al. (2017) High-resolution CBV-fMRI allows mapping of laminar activity and [[connectivity]] of cortical input and output in human M1. [[neuron]] 96(6): 1253-1263. https://doi.org/10.1016/j.neuron.2017.11.005

[[6]] Hubers L, Polimeni JR, Urlins L (2021) LAYNII software for laminar fMRI. https://github.com/layerfMRI/LAYNII

[[7]] Waehnert MD, Dinse J, Schäfer A, et al. (2016) A subject-specific framework for in vivo myeloarchitectonic analysis using high resolution quantitative MRI. NeuroImage 125: 94-107. https://doi.org/10.1016/j.neuroimage.2015.10.001

[[8]] Keuken MC, Bazin PL, Crown L, et al. (2014) Quantifying inter-individual anatomical variability in the subcortex using 7T structural MRI. NeuroImage 94: 40-46. https://doi.org/10.1016/j.neuroimage.2014.03.032