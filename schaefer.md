---
title: Schaefer Parcellation
created: 2026-04-20
updated: 2026-05-07
type: entity
tags: [brain-parcellation, functional-connectivity, resting-state, neuroimaging-fmri, human-connectome-project]
sources: [raw/papers/smith-2013-hcp.md, raw/papers/power-2011.md]
---

The **Schaefer Parcellation** (also referred to as the Schaefer atlas) is a widely-used functional brain parcellation derived from resting-state functional magnetic resonance imaging (fMRI) data collected by the [[human-connectome-project]] (Schaefer et al., 2018). It provides a hierarchical set of cortical parcels at multiple resolutions ranging from 100 to 1000 regions, with each parcel assigned to either 7-network or 17-network categorical labels originally described by Yeo and colleagues (Yeo et al., 2011). The atlas has become one of the most common node definitions used in [[whole-brain modeling]] workflows, particularly in [[the-virtual-brain]] simulations, owing to its data-driven derivation, hierarchical structure, and network-level annotations that facilitate interpretation of brain dynamics in terms of known functional systems.

## Motivation and Context

The development of the Schaefer parcellation addressed a fundamental challenge in neuroimaging and connectomics: the need for a biologically meaningful, data-driven segmentation of the cerebral cortex into coherent functional units. Prior to this atlas, researchers relied largely on anatomical parcellations (such as the Desikan-Killiany or Destrieux atlases) that were derived from cytoarchitectural or anatomical features but did not necessarily align with [[functional-connectivity]] patterns. Other approaches included random parcelation schemes or investigator-defined regions of interest, which lacked standardization across studies and limited reproducibility. The Human Connectome Project provided an unprecedented dataset of high-quality, multi-modal neuroimaging data from over 1,000 subjects (Smith et al., 2013), enabling the derivation of robust group-level [[resting-state]] functional connectivity estimates that could form the basis of a new parcellation scheme.

The Schaefer atlas was developed to bridge the gap between anatomical segmentation and functional network organization. By using [[intrinsic-connectivity-networks]] derived from group-level [[functional-connectivity]] gradients (Yeo et al., 2011), the atlas captures the spontaneous co-activation patterns that characterize the brain's [[brain-network]] architecture during task-free conditions. This approach ensures that parcels represent regions that are functionally coherent, making them suitable for analyses ranging from seed-based connectivity estimation to graph-theoretical characterization of brain network topology.

## Technical Details

The parcellation algorithm employs a gradient-boundary approach to identify transitions in [[functional-connectivity]] patterns across the cortical surface (Schaefer et al., 2018). Specifically, the method computes similarity matrices based on resting-state fMRI time series (after preprocessing via [[freesurfer]]-based pipelines) and applies a clustering algorithm that respects the boundaries imposed by connectivity gradients. This results in parcels that are internally coherent (high within-parcel connectivity) and distinct from neighboring parcels (low between-parcel connectivity).

The atlas provides eight different resolutions: 100, 200, 300, 400, 500, 600, 800, and 1000 regions. Each resolution is available with either 7-network or 17-network labels, where the networks correspond to functional systems originally described by Yeo et al. (2011) and refined in subsequent analyses. The 7-network scheme includes major systems such as the [[default-mode-network]], salience/ventral attention, dorsal attention, limbic, somatomotor, visual, and frontoparietal control networks. The 17-network scheme provides finer-grained subdivisions of these major systems.

All parcels are mapped to [[freesurfer]]'s fsaverage surface template, enabling compatibility with standard surface-based neuroimaging tools and datasets. This surface-based representation is particularly valuable for visualization and for integration with other surface-based atlases such as the [[glasser-atlas]].

## Relationship to Other Atlases

The Schaefer parcellation is closely related to and often used in conjunction with the [[yeo-atlas]], which provides the network labels assigned to each Schaefer parcel. While the Yeo atlas defines network boundaries at a coarser resolution (seven or seventeen networks) (Yeo et al., 2011), the Schaefer atlas subdivides these networks into spatially contiguous regions (parcels), providing both network-level and region-level granularity. This hierarchical organization permits analyses at multiple spatial scales within the same dataset.

Compared to purely anatomical parcellations like the Desikan-Killiany or Destrieux atlases, the Schaefer parcellation has the advantage of reflecting [[functional-connectivity]] architecture rather than sulcal/gyral anatomy alone. This makes it particularly suitable for studies of [[brain-dynamics]], [[functional-connectivity]], and [[whole-brain-modeling]] where the node definitions should correspond to coherent functional units. The combination of the Schaefer parcels with the Yeo network assignments provides researchers with a principled way to analyze brain organization at multiple levels of granularity—from fine-grained regional boundaries to coarse network-level interpretations.

## Relationship to TVB

The Schaefer atlas is one of the most common [[parcellation]] choices for [[the-virtual-brain]] simulations and related [[whole-brain-modeling]] workflows. In TVB context, the atlas serves several critical functions. First, it provides node definitions: the 400-region and 1000-region resolutions are the most frequently used configurations in TVB models, with each parcel representing a network node in the [[connectivity]] matrix. Second, the Yeo network assignments enable researchers to compare dynamics across major functional systems, facilitating interpretation of model outputs in terms of known brain organization. Third, structural and functional [[connectivity]] matrices are commonly computed between Schaefer parcels using diffusion imaging and resting-state fMRI data from the HCP or other datasets, providing the coupling parameters for TVB simulations.

The integration of Schaefer parcels with TVB typically involves computing [[structural-connectivity]] from DTI/tractography data and [[functional-connectivity]] from resting-state fMRI, both averaged across subjects or applied subject-specifically in [[personalized-brain-modeling]] pipelines. The resulting connectivity matrices define the coupling strength between brain regions in TVB's neural mass models such as [[wong-wang-model]] or [[jansen-rit-model]].

## Open Questions and Limitations

Several limitations and open questions surround the use of the Schaefer parcellation in research. The atlas is derived exclusively from young adult subjects (ages 22–35) in the HCP sample, raising questions about its applicability across the lifespan, including developmental and [[aging-brain]] populations. Some studies have developed age-specific parcellations to address this concern. Additionally, the parcellation is based on group-level connectivity, which may obscure individual differences in functional organization that are relevant for [[personalized-brain-modeling]] approaches. The choice of resolution (100–1000 parcels) involves a trade-off between spatial granularity and computational tractability, with no single resolution being optimal for all analytical goals. Finally, recent work on dynamic functional connectivity (as explored in the HCP dataset) suggests that static parcellations may not fully capture the time-varying nature of [[functional-connectivity]] networks, prompting ongoing research into temporally variable parcel boundaries.

## References

- Schaefer, A., Kong, R., Gordon, E. M., Laumann, T. O., Zuo, X. N., Holmes, A. J., ... & Yeo, B. T. T. (2018). Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. Cerebral Cortex, 28(9), 3095-3114.
- Yeo, B. T., Krienen, F. M., Sepulcre, J., Sabuncu, M. R., Lashkari, D., Hollinshead, M., ... & Buckner, R. L. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. Journal of Neurophysiology, 106(3), 1125-1165.
- Smith, S. M., Vidaurre, D., Glasser, M. F., Woolrich, M., & Van Essen, D. C. (2013). The resting-state paradigm: HCP and beyond. In fMRI: From Spikes to Networks (pp. 93-120).