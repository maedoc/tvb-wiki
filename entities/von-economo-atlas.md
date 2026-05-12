---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/breakspear-2017.md
tags:
- brain-parcellation
- structural-connectivity
- neuroimaging-fmri
- neuroimaging-meg
- parcellation
title: Von Economo Atlas
type: entity
updated: '2026-05-12'
---

The von Economo atlas, also known as the cytoarchitectonic map of the cerebral cortex, is a systematic classification of cortical areas based on their histological characteristics. Developed by the Austrian neuroanatomist Constantin von Economo (1876–1931) in collaboration with Georg N. Koskinas, this atlas represents one of the earliest systematic efforts to parcellate the human cerebral cortex into anatomically and functionally distinct regions. Published in 1925 as "Die Cytoarchitektonik der Hirnrinde des Erwachsenen Menschen," the atlas divides each of the four major lobes into subtypes of cortical architecture, providing a foundation for understanding the relationship between cytoarchitecture and brain function that remains relevant in contemporary [[whole-brain modeling]] and [[connectomics]] research.

## Motivation and Historical Context

Prior to von Economo's work, cortical [[parcellation]] was limited to gross anatomical divisions based on sulcal patterns and crude histological staining methods. The von Economo atlas introduced a systematic approach to classifying cortical areas based on the size, density, and arrangement of neuronal cell bodies observable in Nissl-stained sections. This cytoarchitectonic approach addressed a fundamental problem in neuroscience: the lack of a standardized, reproducible method for dividing the cortex into functionally relevant units. The resulting classification scheme identified seven fundamental cortical types—frontal, parietal, temporal, and occipital polar types, plus orbitofrontal, retrosplenial, and insular types—each characterized by distinct laminar organization profiles.

The atlas gained renewed importance in the era of [[neuroimaging-fmri]] and [[whole-brain-modeling]], as researchers sought to relate macroscopic functional signals to the underlying microscopic cortical architecture. Unlike purely anatomical parcellations based on sulcal landmarks (such as the [[desikan-killiany-atlas]] or [[destrieux-atlas]]), the von Economo atlas provides a biologically grounded segmentation that reflects genuine variations in cortical microstructure. This makes it particularly valuable for [[personalized-brain-modeling]] workflows where the goal is to create patient-specific models that honor individual anatomical variation.

## Key Features and Structure

The von Economo atlas distinguishes cortical areas along two primary dimensions: cortical type and regional subtype. Each of the four lobes contains multiple cytoarchitectonic areas characterized by varying degrees of laminar differentiation, neuronal density, and pyramidal cell size. The frontal cortex encompasses primary motor cortex (area 4), premotor areas, and prefrontal regions with progressively elaborated laminar structure. The parietal lobe includes primary somatosensory cortex (areas 1, 2, 3) and higher-order somatosensory association areas. The temporal lobe contains primary auditory cortex (areas 41, 42) and auditory association cortex, while the occipital lobe is dominated by primary visual cortex (area 17) and visual association areas.

Modern implementations of the von Economo atlas, particularly those derived from the Julich-Brain atlas (formerly the Julich histological atlas), provide high-resolution volumetric labels that can be aligned to [[mni-space]] templates. These digital versions enable integration with [[resting-state-fmri]] analyses, [[diffusion-imaging]] tractography, and [[structural-connectivity]] reconstruction pipelines. The atlas is particularly useful for studying [[network-hubs]] and [[structural-core]] regions, as it identifies areas with distinct cytoarchitectonic profiles that may underlie their functional importance.

## Relationship to TVB

The von Economo atlas is directly relevant to [[the-virtual-brain]] (TVB) workflows in several important ways. First, TVB's cortical surface parcellation capabilities can leverage this atlas to define regions of interest for [[whole-brain modeling]] simulations. When constructing [[brain-network]] models in TVB, users can select the von Economo parcellation to define the nodes of their network, enabling simulations that respect biologically meaningful cortical divisions. Second, the atlas informs TVB's [[structural-connectivity]] matrix generation, as connectivity profiles between regions can be weighted based on the cytoarchitectonic similarity or dissimilarity of their constituent cortices.

The [[brain-dynamics-toolbox]] and related TVB community projects have implemented the von Economo atlas as one of the standard parcellation options, alongside the [[schaefer-atlas]], [[yeo-atlas]], and [[glasser-atlas]]. When used in conjunction with TVB's parameter estimation routines, the atlas enables researchers to investigate how variations in cortical microstructure across regions might influence [[network-dynamics]] and [[brain-oscillations]]. This is particularly relevant for modeling [[epilepsy-modeling]] and [[brain-stimulation]] scenarios where the differential excitability of distinct cytoarchitectonic regions plays a critical role in seizure propagation and stimulation response.

## Related Atlases and Comparative Context

The von Economo atlas occupies a unique position among cortical parcellations by virtue of its histological basis. Contemporary alternatives include the [[glasser-atlas]], which parcels the cortex based on multi-modal neuroimaging data (resting-state connectivity plus task activation), and the [[schaefer-atlas]], which defines regions based on resting-state functional connectivity gradients. The [[aal-atlas]] and its derivatives provide anatomically labeled parcellations widely used in clinical neuroimaging, while the [[brainnetome-atlas]] offers a fine-grained parcellation combining structural and functional connectivity information.

Each parcellation scheme carries distinct advantages and limitations for [[whole-brain-modeling]] applications. The von Economo atlas's primary strength lies in its direct biological grounding—cortical types reflect genuine variations in neuronal composition that influence local dynamics and [[connectivity]]. However, the atlas was developed from a limited sample of adult brains, raising questions about population generalizability. Modern efforts to create probabilistic cytoarchitectonic maps that capture inter-individual variation address this limitation, as implemented in the Julich-Brain atlas and related projects that provide uncertainty estimates for cytoarchitectonic boundaries.

## Open Questions

Despite its historical significance, several challenges remain in applying the von Economo atlas to contemporary computational neuroscience. The correspondence between cytoarchitectonic borders and functional boundaries (as measured via [[resting-state]] or task-based [[neuroimaging-fmri]]) remains an active area of investigation, with some studies finding good alignment and others revealing substantial discrepancies. Additionally, how cytoarchitectonic variation relates to individual differences in cognition, aging, and disease states is poorly characterized, though large-scale datasets like the [[hcp-dataset]] and [[uk-biobank]] offer unprecedented opportunities to address these questions. Integrating the von Economo atlas with TVB's [[personalized-brain-modeling]] frameworks may help bridge the gap between microscopic neuroanatomy and macroscopic brain dynamics in health and disease.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal [[neuroimaging]]*. Brain Connectivity. [DOI](](https://doi.org/10.1089/brain.2012.0120))
3. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](](https://doi.org/10.1038/s41593-017-0015-4))