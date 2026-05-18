---
title: RABIES
created: 2026-04-20
updated: 2026-05-18
type: entity
tags: [software-brain-modeling, connectomics, structural-connectivity, neuroimaging-dti, whole-brain-modeling, diffusion-imaging, tractography, software-tvb]
sources: [raw/papers/ritter-2013.md, raw/papers/sanz-leon-2013.md, raw/papers/huntenburg-2018.md]
---

RABIES (Robust Astute Segmentation of Images) is an open-source [[neuroimaging]] software for automated segmentation of brain structures from magnetic resonance imaging data. The software produces tissue classifications and region-of-interest maps, which serve as anatomical foundations for constructing [[connectome]]-based [[whole-brain-modeling]] simulations. By providing reproducible, automated segmentation, RABIES addresses a fundamental bottleneck in translating raw neuroimaging acquisitions into the parcellated structural data that large-scale brain network models require.

## Motivation and Context

Whole-brain modeling platforms such as [[the-virtual-brain]] depend critically on the quality of anatomical input data. Empirical [[structural-connectivity]] matrices define the coupling weights between neural populations in simulated brain networks, typically derived from [[diffusion-imaging]] and [[tractography]] applied to individual subjects [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The construction of these matrices requires an earlier segmentation step: brain voxels must be partitioned into anatomically meaningful regions before tractography-based connectivity can be estimated. [[raw/papers/ritter-2013.md|Ritter et al. (2013)]] demonstrated that subject-specific structural connectivity derived from diffusion imaging can parameterize personalized brain models capable of reproducing individual [[resting-state]] [[functional-connectivity]] patterns. The fidelity of such personalized models is therefore constrained by the accuracy and consistency of the underlying segmentations. Automated tools reduce operator-dependent variability in this preprocessing stage, making it feasible to construct large cohorts of personalized virtual brain models with systematically comparable anatomical foundations.

The segmentation challenge intensifies in clinical and [[aging]] populations, where pathological changes such as [[white-matter]] hyperintensities, atrophy, or surgical lesions can confound algorithms that assume normative tissue intensity distributions. Specialized robust segmentation approaches become essential for extending [[personalized-brain-modeling]] to disease contexts, including [[epilepsy-modeling]] and [[alzheimers-disease]].

## Relationship to TVB

RABIES is not natively integrated into the TVB platform as a preprocessing adapter, but its outputs — parcellated brain regions and tissue-class maps — are directly relevant to the TVB modeling pipeline. [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]] established that TVB constructs whole-[[brain-network]] models by combining empirical structural connectivity from diffusion MRI tractography with [[neural-mass-models]] to simulate population-level [[network-dynamics]]. In personalized modeling workflows, segmentation quality propagates through every subsequent stage: structural connectivity estimates depend on the spatial extent of each region, and forward models for simulated [[neuroimaging-fmri]] signals rely on accurate tissue masks [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. Automated, reproducible segmentation therefore supports the broader goal of constructing subject-specific virtual brains that can be compared across individuals and cohorts with confidence that differences in model behavior reflect genuine neurobiological variation rather than preprocessing inconsistencies.

## Related Tools

RABIES occupies a methodological niche alongside tools that translate raw MRI data into segmented formats for whole-brain simulators. The [[nighres]] package provides complementary high-resolution segmentation capabilities, including the MGDM (Multi-Atlas Multi-Cloud Decomposition) algorithm for tissue classification and the CRUISE (Cortical Reconstruction Using Implicit Surface Evolution) method for extracting topologically correct cortical surfaces [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]]. While Nighres targets laminar-resolution analysis and depth-dependent cortical profiling, RABIES addresses the related challenge of robust, automated segmentation across heterogeneous clinical and population-level datasets. Both tools output data in formats compatible with [[connectivity]] analysis packages and TVB model construction workflows.
