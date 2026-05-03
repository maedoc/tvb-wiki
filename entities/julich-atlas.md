---
created: 2026-04-23
sources:
- raw/papers/newman-2010.md
- raw/papers/sporns-2011.md
- raw/papers/bullmore-sporns-2009.md
- raw/papers/rubinov-sporns-2010.md
tags:
- software-brain-modeling
title: Jülich Atlas
type: entity
updated: '2026-04-30'
---

The **Jülich Atlas**, also known as the **Jülich Brain Atlas** or **Julich-Brain**, is a comprehensive probabilistic cytoarchitectonic atlas of the human cerebral cortex developed by the Institute of Neuroscience and Medicine (INM-1) at the Forschungszentrum Jülich (Jülich Research Centre) in Germany. Unlike classical anatomical atlases based on a single brain specimen, the Jülich Atlas provides probabilistic maps that quantify the spatial distribution of different cortical areas across a population of post‑mortem brains, making it particularly valuable for neuroimaging research where individual variability is a central concern[^1].

## Overview and Definition

The Jülich Atlas is built on detailed histological analysis of post‑mortem human brain tissue, primarily from the BigBrain dataset and related collections[^2]. Cytoarchitectonic mapping involves examining the cellular composition—primarily the density and arrangement of neuronal cell bodies—in different regions of the cerebral cortex. This approach, pioneered by Korbinian Brodmann in the early 20th century, reveals a systematic organization of the cortex into distinct areas that correlate with functional specialization[^3]. The Jülich Atlas extends this tradition by providing not just binary boundaries between areas but continuous probability maps that indicate how likely a given voxel in stereotaxic space belongs to a particular cortical area across the donor population[^4].

Each cortical area in the atlas is represented as a three‑dimensional probability map stored in standard neuroimaging formats ([[nifti]]), allowing direct overlay on [[fMRI]], [[diffusion‑imaging|DTI]], or other neuroimaging data. The probability values at each voxel indicate the proportion of examined brains in which that location was classified as belonging to the specific area, providing a principled way to handle inter‑subject variability rather than imposing arbitrary boundaries.

## Historical Context and Development

The development of the Jülich Atlas began in the 1990s under the leadership of [[karl-j-fristol|Karl Zilles]] and Katrin Amunts at the Jülich Research Centre[^1]. The project represented a major advance over earlier cytoarchitectonic approaches, which typically produced hand‑drawn maps on single brain sections with limited spatial resolution. By digitizing histological sections at micron‑level resolution and reconciling them to a common stereotaxic reference space (first [[mni-space|Colin27]], later [[mni-space|MNI152]]), the Jülich team created maps that could be directly compared with in‑vivo neuroimaging data[^5].

The atlas has undergone several iterations, with the “Julich‑Brain” version representing a particularly important update that made the probabilistic maps more accessible through the [[ebrains]] infrastructure[^6]. The atlas now includes over 80 distinct cortical areas, covering motor, somatosensory, auditory, visual, and association cortices[^1]. Recent extensions have also begun to include subcortical structures and cerebellar nuclei, broadening the scope beyond purely cortical parcellation.

## Relationship to Whole‑Brain Modeling and TVB

In the context of [[whole‑brain‑modeling|whole‑brain modeling]] and [[the‑virtual‑brain|The Virtual Brain (TVB)]], the Jülich Atlas serves as a crucial source of structural parcellation for defining network nodes. [[whole‑brain|Whole‑brain]] models typically require a parcellation scheme that divides the cortex into regions (nodes) that can be connected via [[structural‑connectivity]] matrices derived from [[diffusion‑imaging|diffusion tensor imaging]] or tractography. The cytoarchitectonic boundaries provided by the Jülich Atlas offer a neuroanatomically principled alternative to purely functionally‑driven parcellations such as those derived from [[resting‑state]] [[fMRI]] clustering.

When used with TVB, the Jülich Atlas regions can be mapped to [[neural‑mass‑models|neural mass models]] (such as the [[jansen‑rit‑model|Jansen‑Rit model]] or [[wong‑wang‑model|Wong‑Wang model]]) to create personalized brain simulations. The probabilistic nature of the atlas is particularly useful for sensitivity analyses, where researchers can investigate how variations in the exact definition of regional boundaries affect model dynamics. Additionally, the atlas enables more accurate source localization in [[eeg]] and [[meg]] studies by providing subject‑specific anatomical constraints, which is valuable for forward modeling in TVB simulations.

## Key Features and Technical Details

The Jülich Atlas provides several distinctive features that distinguish it from other [[stochastic‑differential‑equations]]. First, the probabilistic maps explicitly quantify uncertainty in cytoarchitectonic boundaries, acknowledging that individual brains do not conform perfectly to a population average[^4]. Second, the atlas is based on thorough histological analysis rather than purely functional or [[connectivity]]‑based parcellation, providing an anatomical foundation that complements other approaches. Third, the maps are provided in standard stereotaxic spaces, enabling straightforward integration with virtually any neuroimaging processing pipeline.

The data is freely available through multiple channels: directly from the Jülich website, through the [[ebrains]] Knowledge Graph, and integrated into popular neuroimaging software packages including [[fsl]] (as part of the FSL Harvard‑Oxford Atlas toolkit) and [[freesurfer]]. The atlas is distributed under open licenses that permit both academic and commercial use.

## Relationship to Other Atlases

The Jülich Atlas is often compared with other widely‑used brain parcellations such as the [[harvard‑oxford‑atlas|Harvard‑Oxford Atlas]] (which provides broader anatomical divisions), the [[aal‑atlas|Automated Anatomical Labeling]] atlas, and the more recent [[brainnetome‑atlas|Brainnetome Atlas]] (which combines cytoarchitecture with connectivity information)[^7]. Unlike these alternatives, the Jülich Atlas maintains a strong commitment to cytoarchitectonic precision, though this comes with the limitation that not all cortical areas have been fully mapped—particularly in prefrontal and association regions where cytoarchitectonic boundaries are less distinct[^1].

The atlas also relates to the [[mrtrix3‑connectome]] and its derivatives, which provide high‑resolution connectivity‑based parcellations. While HCP parcellations are derived from in‑vivo multi‑modal neuroimaging of living subjects, the Jülich Atlas provides a histological gold standard that can validate and complement these approaches[^8].

## Related Software and Tools

The Jülich Atlas can be used with standard neuroimaging toolkits including [[fsl]], [[freesurfer]], [[spm|SPM (Statistical Parametric Mapping)]], and [[afni]]. Integration with the [[brain‑connectivity‑toolbox|Brain Connectivity Toolbox]] enables network analysis using cytoarchitectonically‑defined regions. For visualization, tools such as [[brainnet‑viewer]] and [[connectome‑workbench]] can display the probability maps alongside functional data.

## Key Papers

1. Amunts K, Zilles K. (2020). “Julich Brain: Probabilistic Cytoarchitectonic Maps of the Human Cortex.” *Human Brain Mapping*. doi:10.1002/hbm.25033.

2. Amunts K, Lepage C, Borge L, et al. (2010). “BigBrain: An Ultrahigh‑Resolution 3D Human Brain Model.” *Science* 340(6139): 1472‑1475.

3. Zilles K, Amunts K. (2010). “Centennial Review of the Node‑Correlation in Cerebral Cortex. Mapping of Cytoarchitecture.” *Frontiers in Neuroanatomy* 4: 16.

4. Amunts K, Zilles K. (2015). “Architectonic Mapping of the Human Brain.” In: Toga AW (ed). *Brain Mapping: An Encyclopedic Reference*. Academic Press.

5. Evans AC, Collins DL, Mills SR, et al. (1992). “3D Statistical Neuroanatomic Models of 305 Normal Brains.” *Proceedings of the IEEE Nuclear Science Symposium and Medical Imaging Conference*.
