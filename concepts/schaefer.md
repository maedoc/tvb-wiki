---
created: 2026-04-20
sources:
- raw/papers/arxiv-2510.05325.md
- raw/papers/power-2011.md
- raw/papers/smith-2013-hcp.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-66f887e82e89.md
- raw/papers/anticevic-2012.md
tags:
- brain-parcellation
- functional-connectivity
- resting-state
- neuroimaging-fmri
- database-hcp
- software-tvb
title: Schaefer Parcellation
type: entity
updated: '2026-05-09'
---

The **Schaefer Parcellation** is a widely-used functional [[brain-parcellation]] derived from resting-state [[fmri]] data collected by the [[human-[[connectome]]-project]]. Developed by Alexander Schaefer and colleagues (2018), it provides a systematic division of the human cerebral cortex into spatially contiguous regions of interest, offering a hierarchical organization that has become one of the standard node definitions for [[whole-brain]] [[connectivity]] analyses and computational modeling.

## Motivation and Context

Prior to the Schaefer parcellation, [[brain-parcellations]] were often derived from anatomical landmarks (such as the Desikan-Killiany atlas) or from meta-analytic activations. While anatomical parcellations have clear neuroanatomical grounding, they do not necessarily reflect functional boundaries — the cortex is functionally organized in ways that transect cytoarchitectural borders. The Schaefer parcellation addressed this limitation by using intrinsic [[functional-connectivity]] patterns from large-scale [[resting-state]] fMRI data to define parcels that respect functional networks rather than purely anatomical divisions.

The [[human-[[connectome]]-project]]'s resting-state fMRI dataset was instrumental to this approach. As documented in the HCP resting-state studies (Smith et al., 2013), the HCP protocol acquired high-quality, multi-band fMRI data at 1.2mm resolution across over 200 subjects, enabling identification of functional networks at unprecedented spatial resolution. The Schaefer parcellation leveraged this data to create parcels that correspond to functionally coherent brain regions — areas that show strong temporal correlation in their blood-oxygen-level-dependent ([[bold-signal|BOLD]]) signal during [[rest]].

## Technical Details

The Schaefer parcellation provides parcels at multiple resolutions: 100, 200, 300, 400, 500, 600, 800, and 1000 regions (Schaefer et al., 2018). This hierarchical structure allows researchers to choose an appropriate spatial granularity for their analysis — coarser resolutions (100–200 parcels) are often used for tractable network modeling, while finer resolutions (800–1000 parcels) enable more detailed investigations of sub-network organization.

Each parcel is assigned to one of two network labeling schemes: the Yeo 7-network parcellation or the more fine-grained 17-network parcellation (Yeo et al., 2011). The Yeo networks, derived independently from resting-state connectivity, include major systems such as the [[default-mode-network]], visual network, somatomotor network, dorsal attention network, ventral attention network, limbic network, and frontoparietal control network. This dual assignment means that Schaefer parcels inherit both a spatial definition and a network identity — a powerful feature for comparing functional organization across conditions or subject groups.

The parcellation is surface-based, originally defined on [[freesurfer]]'s fsaverage template. This means the parcels are represented on the cortical sheet rather than in volumetric space, which is particularly appropriate for fMRI data that is naturally 2D on the cortical surface after projection. The surface representation also facilitates integration with other surface-based data types, including MEG/EEG source estimates and [[diffusion-imaging]] [[tractography]].

## Relationship to The Virtual Brain

The Schaefer parcellation is one of the most common [[parcellation]] choices for [[the-virtual-brain]] (TVB) workflows. In TVB, the brain is modeled as a network of coupled [[neural-mass-models]], where each node represents a brain region. The [[schaefer-atlas]] provides ready-made node definitions at multiple resolutions, with 400 and 1000 regions being particularly popular choices for TVB simulations.

The Yeo network assignments associated with each Schaefer parcel complement TVB modeling nicely: researchers can compare model dynamics across Yeo-defined functional systems, examining whether simulated brain activity shows network-specific alterations in epilepsy, schizophrenia, or other disease states. Furthermore, structural and functional connectivity matrices can be directly computed between Schaefer parcels using streamline tractography from diffusion imaging or temporal correlations from fMRI, respectively, producing connectivity matrices that serve as the coupling architecture in TVB network models.

## Comparison to Related Parcellations

The Schaefer parcellation sits within a broader ecosystem of functional parcellations. It differs from purely anatomical atlases like the Desikan-Killiany or Destrieux atlases in that it is data-driven rather than landmark-derived. Compared to the Glasser parcellation (Glasser et al., 2016), which was derived from multi-model (structural, functional, and myelin) MRI data, Schaefer relies purely on intrinsic functional connectivity. The [[glasser-atlas]] provides 360 parcels with potentially finer-grained cytoarchitectural correspondence, while Schaefer offers flexible resolution scaling.

Compared to other functional parcellations like the [[power-atlas]] (Power et al., 2011), Schaefer benefits from the HCP's standardized acquisition protocol and large sample size, providing more stable and reproducible network definitions. The hierarchical nature of Schaefer — with parcels nested within larger networks — also distinguishes it from flat parcellations that offer a single resolution.

## Open Questions and Limitations

Despite its widespread adoption, the Schaefer parcellation has several limitations. First, it is derived from young adult data (primarily ages 22–35) and may not generalize to pediatric or geriatric populations — developmental or [[aging]] studies often require age-appropriate parcellations. Second, the parcellation captures group-averaged connectivity patterns, potentially obscuring individual differences in functional topography that are relevant for [[personalized-brain-modeling]]. Recent work on individual-specific parcellations seeks to address this limitation.

Third, the parcellation is cortical-only; subcortical structures are not included, requiring researchers to combine Schaefer with other atlases (such as the Aseg or hippocampal segmentations from freesurfer) for whole-brain coverage. Finally, the relationship between resting-state connectivity parcels and task-based activation boundaries remains an active area of investigation — parcels defined at rest may not align perfectly with task-evoked activation patterns.

## References

1. V. Kirova, Dzerassa Kadieva, Daniil Vlasenko, Isak B. Blank, Fedor Ratnikov. (2025). *Dynamic Functional Connectivity Features for Brain State Classification: Insights from the [[human-[[connectome]]-project]]*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2510.05325)
2. (authors unknown). *Functional Network Organization of the Human Brain*.
3. (authors unknown). *Resting-State fMRI in the Human Connectome Project*.
4. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
5. Federica Franza, M. Cirillo, M. Silvestro, F. Trojsi, Antonio Russo, Fabrizio Esposito, M. A. Pirozzi. (2025). *Impact of Brain Parcellation on MRI-derived Neurovascular Coupling Estimates Across Large-Scale Functional Networks*. 2025 IEEE International Conference on Metrology for eXtended Reality, Artificial Intelligence and Neural Engineering (MetroXRAINE). [DOI](https://doi.org/10.1109/MetroXRAINE66377.2025.11340209)
6. Anticevic et al. (2012). *Global, regional, and network level changes in schizophrenia: computational modeling of glutamatergic dysfunction and GABAergic deficits in a novel whole-brain framework*. Proceedings of the National Academy of Sciences (PNAS). [DOI](https://doi.org/10.1073/pnas.1114858109)