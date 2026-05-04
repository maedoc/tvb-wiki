---
title: RABIES
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-brain-modeling, white-matter, alzheimers-modeling, personalized-brain-modeling]
sources: []
---

RABIES (Robust Astute Segmentation of Images via a Bayesian framework) is an open-source neuroimaging software package designed for automated segmentation of brain structures and pathological lesions in magnetic resonance imaging (MRI) data. The software applies Bayesian probabilistic models to achieve robust segmentation across heterogeneous clinical and research datasets, making it particularly valuable for population studies involving aging brains and neurological disease cohorts.

## Overview

RABIES emerged from the need for reliable, automated segmentation tools that can handle the variability inherent in clinical neuroimaging data. Unlike segmentation algorithms that assume ideal imaging conditions, RABIES incorporates Bayesian inference to model uncertainty in image intensity distributions and anatomical boundaries. This probabilistic approach allows the software to adapt to different scanner types, acquisition protocols, and patient populations without requiring extensive manual parameter tuning. The framework was developed to address specific challenges in segmenting white matter hyperintensities and subcortical structures, which are clinically relevant biomarkers for diseases including [[alzheimers-disease]], vascular dementia, and small vessel disease.

The software operates by constructing a statistical model of expected tissue class distributions and using Bayesian updating to refine segmentation probabilities based on observed image intensities. This contrasts with purely deterministic approaches like threshold-based methods, allowing RABIES to propagate uncertainty estimates through the segmentation pipeline and produce confidence maps alongside hard segmentations. Such uncertainty quantification proves valuable for quality control in large-scale studies and for identifying ambiguous voxels that may require expert review.

## Key Features

RABIES provides several capabilities that distinguish it from other segmentation tools in the neuroimaging ecosystem. The Bayesian formulation enables explicit modeling of prior knowledge about anatomical structures, which can be derived from established atlases such as the [[mni-space]] templates or study-specific anatomical priors. The software incorporates spatial regularization through Markov random field models, which encourages spatially coherent segmentations and suppresses isolated misclassifications that would be unlikely anatomically.

Another distinguishing feature is the built-in support for multispectral segmentation, allowing the integration of multiple MRI contrasts (T1-weighted, T2-weighted, FLAIR, PD) to improve segmentation accuracy. This is particularly important for lesion segmentation, where different tissue types may have similar intensities in a single contrast but become distinguishable when multiple contrasts are combined. The framework also includes tools for longitudinal analysis, enabling tracking of lesion load changes over time within individuals.

The software provides automated processing pipelines that integrate preprocessing steps including bias field correction, intensity normalization, and registration to standard space. These pipelines are designed to be modular, allowing users to substitute specific preprocessing steps while retaining the core Bayesian segmentation engine. RABIES outputs results in standard NIfTI format, facilitating integration with downstream analysis tools including [[mrtrix3-connectome]] and connectivity analysis packages.

## Relationship to TVB

While RABIES is not directly integrated into [[the-virtual-brain]] (TVB) as a native adapter, it plays a complementary role in the TVB ecosystem by providing high-quality segmentations that can inform personalized brain model construction. The segmentation outputs—particularly white matter parcellations and lesion maps—can serve as anatomical constraints for [[whole-brain-modeling]] pipelines that rely on accurate structural boundaries. In [[personalized-brain-modeling]] workflows, RABIES segmentations of individual patient anatomy can be used to define region-of-interest boundaries for TVB's neural mass models.

The software's uncertainty estimates align well with TVB's framework for handling model parameter uncertainty. When constructing personalized models from individual neuroimaging data, the confidence maps produced by RABIES can be used to weight the contribution of different brain regions to the model, potentially improving predictions in regions with high anatomical certainty while appropriately down-weighting regions with ambiguous boundaries. This integration supports TVB's use cases in [[epilepsy-modeling]] and clinical applications where accurate anatomical personalization is critical.

## Related Software

RABIES occupies a similar analytical niche as other segmentation tools in the neuroimaging ecosystem, though its Bayesian methodology distinguishes it from many alternatives. The closest functional equivalents include [[ants]] (Advanced Normalization Tools), which provides segmentation through the ANTsSyN algorithm and includes the Atropos segmentation module; [[fmriprep]], which offers automated preprocessing alongside segmentation capabilities; and [[brainvisa]], which provides comprehensive cortical reconstruction through probabilistic labeling based on Bayesian inference combined with anatomical constraints.

For whole-brain parcellation, RABIES can be used in combination with [[brain-parcellations]] such as the [[schaefer-atlas]], [[glasser-atlas]], or [[desikan-killiany-atlas]] to produce study-specific parcellations that incorporate lesion information. The output formats are compatible with connectomics tools including [[bctpy]] (Brain Connectivity Toolbox) for [[functional-connectivity]] analysis and [[mrtrix3-connectome]] for tractography-based connectivity.