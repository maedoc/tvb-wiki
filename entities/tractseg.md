---
title: TractSeg
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [software-tractography, software-mrtrix3, diffusion-imaging, structural-connectivity, white-matter, tractography]
sources:
  - https://doi.org/10.1016/j.neuroimage.2018.07.070
  - https://arxiv.org/abs/1805.07103
  - https://arxiv.org/abs/1806.05580
  - https://www.sciencedirect.com/science/article/pii/S136184151930101X
  - https://www.humanconnectomeproject.org/
---

TractSeg is an open-source software tool for the automated segmentation of white matter tracts from diffusion magnetic resonance imaging (dMRI) data. Developed by **Jakob Wasserthal**, **Peter Neher**, and colleagues at the German Cancer Research Center (DKFZ), it employs machine learning techniques, specifically convolutional neural networks, to identify and extract major white matter fiber bundles in the brain. The tool produces binary segmentation masks for each identified tract, which can then be used to generate region-of-interest (ROI) masks for tractography analysis or to construct structural connectivity matrices for whole-brain modeling applications.

## Overview

TractSeg was developed to address a major bottleneck in connectome analysis: the time-consuming and operator-dependent process of manually defining white matter tracts. Traditionally, researchers had to manually delineate tract ROIs based on anatomical landmarks, a process that could take hours per subject and introduced significant inter-rater variability. TractSeg automates this process by implementing a fully convolutional neural network trained on the Human Connectome Project (HCP) dataset[^1], enabling reproducible and objective tract segmentation across large cohorts.

The software operates on processed fiber orientation distribution functions (FODs) obtained from constrained spherical deconvolution (CSD) of diffusion MRI data. It segments 72 major white matter tracts, including association tracts (such as the arcuate fasciculus, uncinate fasciculus, and inferior fronto-occipital fasciculus), projection tracts (such as the corticospinal tract and thalamic radiations), and commissural tracts (such as the corpus callosum divisions)[^2]. Each tract is represented as a three-dimensional binary mask that can be used directly for further analysis or as input to other neuroimaging tools.

## Key Features

TractSeg offers several features that make it particularly valuable for computational neuroscience and connectomics research. First, the tool provides fully automated tract segmentation without requiring manual placement of waypoint or exclusion masks, significantly reducing preprocessing time. Second, the machine learning approach ensures consistency across subjects and datasets, eliminating the inter-rater variability inherent in manual segmentation. Third, TractSeg outputs both the tract masks and the extracted tractograms, allowing researchers to examine the resulting fiber populations directly.

The software integrates tightly with the MRtrix3 ecosystem, leveraging its robust preprocessing pipelines for diffusion data and advanced tractography algorithms. TractSeg can operate on either single-shell or multi-shell diffusion data and is compatible with standard preprocessing pipelines including eddy current correction and motion correction. The output format follows NIfTI conventions, ensuring compatibility with a wide range of neuroimaging software including [[FSL]], [[AFNI]], [[3D-Slicer]], and [[ITK-SNAP]].

An important feature of TractSeg is its ability to generate tract probability maps, which represent the likelihood of each voxel belonging to a particular tract across the population. These probability maps can be used to create probabilistic tractography seeds or to study tract morphology and variability across groups. Additionally, TractSeg provides confidence maps that indicate the segmentation certainty for each voxel, allowing researchers to identify potentially problematic segmentations.

## Relationship to TVB

TractSeg plays a significant role in the [[the-virtual-brain]] (TVB) ecosystem by providing high-quality structural connectivity data essential for whole-brain modeling. In TVB, the structural connectome forms the anatomical scaffolding upon which neural mass models are simulated, and the quality of this structural foundation directly influences the fidelity of simulated brain dynamics. TractSeg's automated segmentation enables researchers to generate consistent structural connectivity matrices efficiently, supporting personalized brain modeling pipelines.

The segmented white matter tracts from TractSeg can be used to define the regions of interest for tracking fiber pathways between cortical and subcortical regions. These pathways form the structural connections that mediate signal propagation between brain areas in TVB simulations. The tool's ability to produce segmentation masks for 72 tracts provides coverage of the major fiber systems commonly used in whole-brain connectome construction. Combined with TVB's [[neural-mass-models]] and [[dynamic-causal-modeling]] frameworks, TractSeg-derived connectomes enable researchers to investigate how structural alterations in white matter pathways contribute to changes in functional brain dynamics observed in conditions such as epilepsy, schizophrenia, and Alzheimer's disease.

## Limitations

Users should be aware of several limitations when using TractSeg. First, the neural network was trained on high-quality HCP data, which employs specialized acquisition protocols (including multi-shell diffusion encoding at 1.25mm isotropic resolution)[^3]. Performance may degrade when applying TractSeg to data acquired with different protocols, particularly those with lower spatial resolution or different b-values. Second, certain small tracts such as the Commissure Anterior (CA) and Fornix (FX) may be incomplete or missing in segmentations for non-HCP data, particularly at lower resolutions. The developers recommend using the `--super_resolution` flag to upsample input data to 1.25mm resolution for improved results. Third, TractSeg requires input data to be in MNI space orientation, which may necessitate additional registration steps for datasets with different orientations. Finally, while the 72-tract segmentation provides comprehensive coverage of major fiber bundles, some specialized or species-specific tracts may not be included in the default model.

## Key Papers

- **Wasserthal, J., Neher, P., & Maier-Hein, K. H. (2018).** TractSeg - Fast and accurate white matter tract segmentation. *NeuroImage*, 175, 414-424. https://doi.org/10.1016/j.neuroimage.2018.07.070
- **Wasserthal, J., Neher, P., & Maier-Hein, K. H. (2018).** Tract orientation mapping for bundle-specific tractography. *MICCAI 2018*.
- **Wasserthal, J., et al. (2019).** Combined tract segmentation and orientation mapping for bundle-specific tractography. *Medical Image Analysis*, 54, 28-41. https://doi.org/10.1016/j.media.2019.03.001

## Related Software

TractSeg operates within a broader ecosystem of diffusion MRI and tractography tools. Related software includes [[MRtrix3]] and [[MRTrix3-Connectome]], which provide the underlying preprocessing and tractography capabilities; [[AFQ]], another automated tractography segmentation tool that uses a different approach based on waypoint masks; [[Dipy]], a comprehensive diffusion MRI analysis library; and [[DSI-Studio]], which offers alternative tractography algorithms and visualization capabilities. Additionally, tract segmentation outputs can be visualized using tools such as [[BrainNet-Viewer]], [[Connectome-Workbench]] (specifically its [[SUMA]] surface module), or [[MRIcron]]. The structural connectivity matrices generated from TractSeg can be analyzed using the [[Brain-Connectivity-Toolbox]] or [[BRAPH]] for graph-theoretic network analysis, and can serve as input to whole-brain simulators including TVB, [[The-Virtual-Epileptic-Brain]], and other [[whole-brain-modeling]] platforms.

## References

[^1]: Sotiropoulos, S. N., et al. (2013). Advances in diffusion MRI acquisition and processing in the Human Connectome Project. *NeuroImage*, 80, 125-143. https://doi.org/10.1016/j.neuroimage.2013.05.057

[^2]: Wasserthal, J., Neher, P., & Maier-Hein, K. H. (2018). TractSeg - Fast and accurate white matter tract segmentation. *NeuroImage*, 175, 414-424. https://doi.org/10.1016/j.neuroimage.2018.07.070

[^3]: Van Essen, D. C., et al. (2012). The Human Connectome Project: a data acquisition perspective. *NeuroImage*, 62(4), 2222-2231. https://doi.org/10.1016/j.neuroimage.2012.02.018