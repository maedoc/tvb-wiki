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
tags:
- structural-connectivity
- neuroimaging-fmri
- software-tvb
- connectomics
- brain-parcellations
title: AAL Atlas
type: entity
updated: '2026-04-24'
---

# AAL Atlas

## Overview
The **AAL (Automated Anatomical Labeling) Atlas** is a widely-used anatomical parcellation of the human brain into 116 regions, first published in 2002. It was developed by Tzourio-Mazoyer and colleagues to provide a standardized anatomical nomenclature for neuroimaging studies. The atlas is defined in [[mni-space]] (Montreal Neurological Institute) coordinate space and labels cortical and subcortical structures using anatomical criteria from the MNI single-subject brain template.

## Key Features
The AAL atlas divides the brain into hemispheric regions including:
- **90 cerebral regions** (45 per hemisphere) covering cortical areas (frontal, parietal, temporal, occipital, and insular) as well as subcortical structures including the thalamus, caudate, putamen, pallidum, hippocampus, and amygdala
- **26 cerebellar regions** covering the cerebellum

Each region is assigned a unique numerical label and anatomical name based on anatomical landmarks. The original AAL atlas has been followed by **AAL2** (Fan et al., 2016) and **AAL3** (Rolls et al., 2020), which refined cytoarchitectonic boundaries and expanded subcortical coverage, including improved delineation of the brainstem and cerebellar parcels.

## Role in Connectome-Based Modeling
The AAL atlas is one of the most commonly used [[brain-parcellations]] for defining network nodes in [[whole-brain-modeling]] and [[structural-connectivity]] analyses. When constructing connectomes from [[diffusion-imaging]] or [[neuroimaging-fmri]] data, researchers use AAL regions as nodes, with edges representing fiber tract counts or functional correlations between regions.

In [[the-virtual-brain]] (TVB), the AAL atlas serves as a default anatomical parcellation for importing structural connectivity matrices and projecting activity to anatomical locations.

## Relationship to TVB
The AAL atlas is integrated into [[the-virtual-brain]] (TVB) as one of the standard anatomical parcellations. TVB utilizes AAL labels for:
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
- [[the-virtual-brain]]

## Other Brain Atlases
- [[desikan-killiany-atlas]]
- [[schaefer-atlas]]
- [[brainnetome-atlas]]

## References
1. Tzourio-Mazoyer N, et al. (2002). Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. *NeuroImage*, 15(1), 273-289.
2. Fan L, et al. (2016). Automated anatomical labeling atlas 2. *NeuroImage*, 124, 1-15.
3. Rolls ET, et al. (2020). Automated anatomical labelling atlas 3. *NeuroImage*, 206, 116132.