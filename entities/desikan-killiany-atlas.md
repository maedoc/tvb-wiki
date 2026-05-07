---
created: '2026-05-03'
sources:
- raw/papers/semanticscholar-66f887e82e89.md
tags: []
title: Desikan Killiany Atlas
type: entity
updated: '2026-05-07'
---

The Desikan-Killiany Atlas is a widely used cortical [[parcellation]] scheme that divides the human cerebral cortex into anatomically defined regions based on magnetic resonance imaging (MRI). Developed by Rahul Desikan, Robert Killiany, and colleagues, this atlas provides a standardized framework for quantifying regional brain structure and function in both healthy and clinical populations [[desikan-killiany-atlas]]. The atlas is characterized by its use of easily identifiable anatomical landmarks—primarily sulcal patterns—that allow for reasonably consistent manual delineation across brains, making it particularly suitable for automated segmentation pipelines that require robust anatomical priors.

## Historical Context and Motivation

The development of the Desikan-Killiany Atlas emerged from a critical need in the neuroimaging community: the absence of a reliable, anatomically validated cortical parcellation scheme that could be applied across different research studies and imaging modalities. Prior to its introduction, researchers often relied on manually defined regions of interest that varied considerably between laboratories, making cross-study comparisons extremely difficult. The atlas was first described in a landmark 2006 paper by Desikan et al. in *NeuroImage* [[desikan-killiany-atlas]], where the authors demonstrated that automated segmentation using this parcellation could achieve high accuracy when compared to expert manual tracings.

The Desikan-Killiany Atlas divides each cerebral hemisphere into 34 cortical regions, yielding a total of 68 regions across both hemispheres. The parcellation is primarily based on sulcal anatomy, with key boundaries defined by major sulci including the central sulcus, lateral sulcus (Sylvian fissure), cingulate sulcus, and superior frontal sulcus [[desikan-killiany-atlas]]. Each region is labeled with a descriptive name that reflects its anatomical location—for example, the "caudal middle frontal gyrus", "pars opercularis", and "isthmus of the cingulate gyrus."

## Technical Description

The Desikan-Killiany Atlas divides each cerebral hemisphere into 34 cortical regions, yielding a total of 68 regions across both hemispheres. The parcellation is primarily based on sulcal anatomy, with key boundaries defined by major sulci including the central sulcus, lateral sulcus (Sylvian fissure), cingulate sulcus, and superior frontal sulcus [[desikan-killiany-atlas]]. Each region is labeled with a descriptive name that reflects its anatomical location—for example, the "caudal middle frontal gyrus", "pars opercularis", and "isthmus of the cingulate gyrus."

The atlas is implemented in the [[FreeSurfer]] software package [[anticevic-2012]], which uses a probabilistic atlas combined by Bayesian segmentation to automatically label voxels in a patient's native MRI space. This automation was novel for its time, as it reduced the enormous labor required for manual segmentation while improving [[reproducibility]] across studies. The FreeSurfer implementation also provides confidence maps that indicate the reliability of the segmentation for each voxel, allowing researchers to mask out uncertain regions in subsequent analyses.

In the context of whole-brain modeling, the Desikan-Killiany Atlas serves as a critical node definition scheme for constructing [[structural connectivity|connectomes]]. When building models in [[The Virtual Brain]] (TVB), the cortical regions defined by this parcellation typically form the nodes of the network, while the edges are defined by [[structural connectivity]] matrices derived from matrices derived from [[neuroimaging]] (DTI) or probabilistic tractography Jeurissen et al., 2014. The relatively coarse granularity of 68 regions makes it computationally tractable for large-scale simulations while retaining sufficient anatomical detail to capture major cortical divisions.

The atlas is frequently used in TVB workflows for both epilepsy modeling and resting-state dynamics simulations. In particular, the distinction between frontal, parietal, temporal, and occipital lobes provided by the Desikan-Killiany parcellation allows researchers to examine how regional heterogeneity in brain dynamics emerges from the underlying [[structural connectivity]]. For studies requiring finer-grained parcellations, researchers often migrate to the [[Schaefer Atlas]] (which provides 100–1000 regions) [[schaefer-atlas]] or the [[Glasser Atlas]] (which provides 360 regions) [[glasser-atlas]], but the Desikan-Killiany remains popular for comparative analyses with historical datasets.

## Key Papers and Validation

The original validation study demonstrated high inter-rater reliability (intraclass correlation coefficients > 0.9) for manual delineation and strong correspondence between automated and manual segmentations [[desikan-killiany-atlas]]. Subsequent studies have validated the atlas in diverse populations including children, elderly individuals, and clinical groups with neurological and psychiatric conditions [[anticevic-2012]]. The atlas has been particularly influential in studies of [[alzheimers-disease|Alzheimer's disease]], where regional cortical thinning in areas such as the entorhinal cortex and superior temporal gyrus—both defined in this parcellation—has been shown to be a sensitive biomarker for early neurodegeneration.

## Related Atlases and Software

The Desikan-Killiany Atlas shares conceptual territory with several other widely used cortical parcellations. The [[Destrieux Atlas]], also available in [[FreeSurfer]], provides a finer-grained parcellation based on the same anatomical principles [[destrieux-atlas]]. The [[Glasser Atlas]], developed using a combination of myelin mapping and task-based fMRI, offers 360 functionally and anatomically defined regions [[glasser-atlas]]. For researchers working with TVB, the choice of atlas involves a tradeoff between granularity and computational efficiency—the Desikan-Killiany Atlas at 68 regions represents a reasonable middle ground.

The atlas is supported by numerous software packages including [[FreeSurfer]], [[fsl-melodic]] [[anticevic-2012]], and can be imported into connectivity analysis tools such as the [[Brain Connectivity Toolbox]] (bctpy) Rubinov & Sporns, 2010, Gretna, and the Connectome Workbench. Visualization of Desikan-Killiany parcellations is supported in [[BrainNet Viewer]], [[Connectome Workbench]], and [[FreeSurfer]].

## Limitations and Open Questions

Despite its widespread adoption, the Desikan-Killiany Atlas has notable limitations that continue to motivate the development of alternative parcellations. First, the anatomical boundaries do not necessarily correspond to functional boundaries—the same cortical region may subserve different cognitive functions depending on context. Second, the 68-region granularity may be too coarse to capture fine-scale network organization revealed by high-resolution [[functional-connectivity]]. Third, the atlas was developed primarily from healthy young adult brains, and its applicability to pediatric or geriatric populations requires careful validation. Future directions include the development of age-appropriate atlases and the integration of multiple modalities (anatomical, functional, and [[connectivity]]-based) into unified parcellation schemes.

## References

1. Federica Franza, M. Cirillo, M. Silvestro, F. Trojsi, Antonio Russo, Fabrizio Esposito, M. A. Pirozzi. (2025). *Impact of [[brain-parcellation]] on MRI-derived Neurovascular Coupling Estimates Across Large-Scale Functional Networks*. 2025 IEEE International Conference on Metrology for eXtended Reality, Artificial Intelligence and Neural Engineering (MetroXRAINE). [DOI](](https://doi.org/10.1109/MetroXRAINE66377.2025.11340209))