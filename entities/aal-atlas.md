---
created: 2026-01-15
sources:
- raw/papers/semanticscholar-e923a3372ab2.md
- raw/papers/arxiv-2603.20348.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/schirner-2018.md
- raw/papers/breakspear-2017.md
- raw/papers/barch-2013.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/semanticscholar-913068805e7f.md
tags:
- structural-connectivity
- neuroimaging-fmri
- software-tvb
- connectomics
- brain-parcellations
title: AAL Atlas
type: entity
updated: '2026-04-30'
---

# AAL Atlas

## Overview
The **AAL (Automated Anatomical Labeling) Atlas** is a widely-used anatomical [[parcellation]] of the human brain into 116 regions, first published in 2002. It was developed by Tzourio-Mazoyer and colleagues to provide a standardized anatomical nomenclature for [[neuroimaging]] studies. The atlas is defined in [[mni-space]] (Montreal Neurological Institute) coordinate space and labels cortical and subcortical structures using anatomical criteria from the MNI single-subject brain template.

## Key Features
The AAL atlas divides the brain into hemispheric regions including:
- **90 cerebral regions** (45 per hemisphere) covering cortical areas (frontal, parietal, temporal, occipital, and insular) as well as subcortical structures including the thalamus, caudate, putamen, pallidum, hippocampus, and amygdala
- **26 cerebellar regions** covering the cerebellum

Each region is assigned a unique numerical label and anatomical name based on anatomical landmarks. The original AAL atlas has been followed by **AAL2** (Fan et al., 2016) and **AAL3** (Rolls et al., 2020), which refined cytoarchitectonic boundaries and expanded subcortical coverage, including improved delineation of the brainstem and cerebellar parcels.

## Role in Connectome-Based Modeling
The AAL atlas is one of the most commonly used [[brain-parcellations]] for defining network nodes in [[whole-brain-modeling]] and [[structural-connectivity]] analyses. When constructing connectomes from [[diffusion-mri]] or [[fmri]] data, researchers use AAL regions as nodes, with edges representing fiber tract counts or functional correlations between regions.

In [[tvb]] (TVB), the AAL atlas serves as a default anatomical parcellation for importing structural [[connectivity]] matrices and projecting activity to anatomical locations.

## Relationship to TVB
The AAL atlas is integrated into [[tvb]] (TVB) as one of the standard anatomical parcellations. TVB utilizes AAL labels for:
- Importing structural connectivity data from [[tractography|diffusion tractography]] pipelines
- Mapping simulated neural activity to anatomical locations for visualization
- Defining stimulation targets in [[brain-stimulation]] protocols
- Reporting region-specific outputs from [[neural-mass-models]] simulations

TVB users can import AAL-based connectivity matrices from sources like the [[hcp-dataset]] or custom [[tractography|diffusion MRI]] processing pipelines.

## Key Papers
- Tzourio-Mazoyer et al. (2002) — Original publication describing the 116-region parcellation
- Fan et al. (2016) — Introduction of AAL2 with refined cytoarchitectonic boundaries
- Rolls et al. (2020) — Introduction of AAL3 with expanded subcortical and cerebellar coverage

## Related Concepts
- [[brain-parcellations]]
- [[structural-connectivity]]
- [[mni-space]]
- [[tvb]]

## Other Brain Atlases
- [[desikan-killiany-atlas]]
- [[schaefer-atlas]]
- [[brainnetome-atlas]]

## References

1. Hong Yu, Xuehuan Liu, Xiao Gao, Yuting Wang, Feize Zheng, Zhiheng Zhou, Gouling Zhan, Weiwei Cui, Xiaowen Zheng, Haiyang Shao, Hao Wang, Qing He, Jun Liu. (2026). *Multimodal [[brain-network]] disruption and structural-functional decoupling in overt hypothyroidism*. Frontiers in Endocrinology. [DOI](https://doi.org/10.3389/fendo.2026.1763670)
2. Jiaxing Xu, Jingying Ma, Xin Lin, Yuxiao Liu, Kai He, Qika Lin, Yiping Ke, Yang Li, Dinggang Shen, Mengling Feng. (2026). *Toward a Multi-View Brain Network Foundation Model: Cross-View Consistency Learning Across Arbitrary Atlases*. [Link](https://arxiv.org/abs/2603.20348)
3. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
4. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
5. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
6. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4)
7. (authors unknown). *Function in the Human [[connectome]]: Task-fMRI and Individual Differences in Behavior*.
8. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
9. Siva Venkadesh, Yuhe Tian, Wendy Linn, Jessica Barrios Martinez, Harrison Mansour, J. Cook, David J. Schaeffer, D. Szczupak, Afonso C Silva, Allan Johnson, Fang‐Cheng Yeh. (2025). *A hierarchical framework for cortical and subcortical gray-matter parcellation across rodents, primates, and humans*. bioRxiv. [DOI](https://doi.org/10.1101/2025.09.08.675002)