---
created: 2026-04-20
sources:
- raw/papers/ritter-2013.md
- raw/papers/sanz-leon-2013.md
- raw/papers/huntenburg-2018.md
tags:
- software-brain-modeling
- structural-connectivity
- neuroimaging-dti
- connectomics
- reproducibility
title: RABIES
type: entity
updated: '2026-05-13'
---

RABIES (Robust Astute Segmentation of Images) is an open-source [[neuroimaging]] software tool for automated segmentation of brain structures from magnetic resonance imaging (MRI) data. The software produces tissue classifications and region-of-interest maps in standard [[nifti]] format, which can serve as the anatomical foundation for constructing [[connectome]]-based [[whole-brain-modeling]] simulations. By providing reproducible, automated segmentation, RABIES addresses a fundamental bottleneck in translating raw neuroimaging acquisitions into the parcellated structural data that large-scale brain network models require.

## Motivation and Context

Whole-brain modeling platforms such as [[the-virtual-brain]] (TVB) depend critically on the quality of anatomical input data. Empirical [[structural-connectivity]] matrices, which define the coupling weights between neural populations in a simulated brain network, are typically derived from [[diffusion-imaging]] and [[tractography]] applied to individual subjects [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The construction of these matrices requires an earlier segmentation step: brain voxels must be partitioned into anatomically meaningful regions before tractography-based connectivity can be estimated. Ritter et al. (2013) demonstrated that subject-specific structural connectivity derived from diffusion imaging can parameterize personalized brain models capable of reproducing individual [[resting-state]] [[functional-connectivity]] patterns [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. The fidelity of such personalized models is therefore constrained by the accuracy and consistency of the underlying segmentations. Automated tools like RABIES reduce operator-dependent variability in this preprocessing stage, making it feasible to construct large cohorts of personalized virtual brain models with systematically comparable anatomical foundations.

The challenge is compounded in clinical and [[aging]] populations, where pathology — such as [[white-matter]] hyperintensities, atrophy, or surgical lesions — can confound segmentation algorithms that assume normative tissue intensity distributions. Specialized segmentation approaches that are robust to atypical anatomy become essential for extending [[personalized-brain-modeling]] to disease contexts, including [[epilepsy-modeling]] and [[alzheimers-disease]].

## Relationship to TVB

RABIES is not natively integrated into the TVB platform as a preprocessing adapter, but its outputs — parcellated brain regions and tissue-class maps — are directly relevant to the TVB modeling pipeline. Sanz Leon et al. (2013) established that TVB constructs whole-[[brain-network]] models by combining empirical structural connectivity from [[diffusion-mri]] tractography with [[neural-mass-models]] to simulate population-level dynamics [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The connectome that serves as the model's coupling matrix must be assembled from segmented, parcellated brain regions, a step for which tools like RABIES supply the necessary anatomical priors.

In personalized modeling workflows, the quality of individual segmentations propagates through every subsequent stage: [[parcellation]] boundaries determine which voxels contribute to each regional timeseries, structural connectivity estimates depend on the spatial extent of each region, and forward models for simulated [[neuroimaging-fmri]] signals rely on accurate gray-matter masks [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. Automated, reproducible segmentation therefore supports the broader goal of constructing subject-specific virtual brains that can be compared across individuals and cohorts with confidence that differences in model behavior reflect genuine neurobiological variation rather than preprocessing inconsistencies.

## Related Software

RABIES occupies a methodological niche alongside other tools that translate raw MRI data into the segmented, parcellated formats used by [[whole-brain]] simulators. The [[nighres]] package provides complementary capabilities for high-resolution segmentation and cortical reconstruction, including the MGDM (Multi-Atlas Multi-Cloud Decomposition) algorithm for tissue classification and the CRUISE (Cortical Reconstruction Using Implicit Surface Evolution) method for extracting topologically correct cortical surfaces [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]]. While Nighres targets laminar-resolution analysis and depth-dependent cortical profiling, RABIES addresses a related challenge for clinical and population-level studies where automated, robust segmentation across heterogeneous datasets is the primary requirement. Both tools output data in formats compatible with [[connectivity]] analysis packages and TVB's model construction workflows.