---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-913068805e7f.md
- raw/papers/power-2011.md
- raw/papers/semanticscholar-1a3ed92b9f5a.md
tags:
- software-neuroimaging
- neuroimaging-fmri
- cerebellum
- brainstem
- spatial-normalization
- toolkit
- software-spm
title: SUIT
type: software
updated: '2026-05-08'
---

# SUIT (Spatial Unbiased Infratentorial Template)

## Overview
SUIT (Spatial Unbiased Infratentorial Template) is a specialized [[neuroimaging]] software tool developed by Diedrichsen et al. within the SPM (Statistical Parametric Mapping) framework for the accurate spatial normalization and segmentation of the cerebellum and brainstem. Unlike standard [[whole-brain]] normalization algorithms that treat the cerebellum as an afterthought—often yielding suboptimal alignment due to its complex and highly folded cortical structure—SUIT provides a dedicated, anatomically informed processing pipeline specifically optimized for these challenging posterior brain regions.

## Technical Implementation

### Normalization Protocol
SUIT employs a two-stage normalization procedure that first isolates the cerebellum and brainstem from the surrounding cerebral tissue using an anatomically informed mask, then applies a customized deformation algorithm that accounts for the unique geometry and variability of these structures. The process begins with a cerebellar isolation step wherein a probabilistic atlas-based mask is used to separate cerebellar and brainstem voxels from the remainder of the brain, creating a dedicated analysis space. This isolation is critical because standard SPM normalization often fails to adequately capture the considerable inter-individual variability in cerebellar morphology, particularly in the lateral hemispheres where individual differences in the arrangement of the deep cerebellar nuclei and the three-dimensional complexity of the cortical lobules create substantial registration challenges.

The normalization itself follows an isolate-then-normalize approach as described in the original SUIT publications. First, the cerebellum and brainstem are isolated using a probabilistic mask. Second, the isolated structures are normalized to the SUIT template using a customized deformation model with cerebellum-specific regularization parameters that balance flexibility in capturing individual anatomical variation against the need for smooth, physiologically plausible deformations. The resulting deformation fields can be applied in either direction—warping individual cerebellar data into the SUIT template space for group analyses, or inverting the transformations to map group-level results back into native space for region-of-interest analyses.

### Segmentation Capabilities
Beyond spatial normalization, SUIT provides automated segmentation of the cerebellum into its constituent lobules based on the SUIT probabilistic atlas, enabling region-specific analyses that are increasingly important for [[computational-neuroscience]] applications. The segmentation distinguishes between the anterior lobe (lobules I–V), the posterior lobe (lobules VI–X), and the flocculonodular lobe, as well as subdivisions within these major lobular territories.

## Relationship to TVB
SUIT is relevant to [[the-virtual-brain]] (TVB) in several important respects. First, TVB's personalized brain modeling pipeline requires accurate anatomical segmentation of brain regions, and the cerebellar parcellation provided by SUIT can be integrated into TVB's region-based modeling framework to assign distinct neural mass parameters to cerebellar subregions. Second, SUIT's normalization enables the generation of group-level cerebellar templates that can serve as atlases for TVB simulations, facilitating the construction of cerebellum-inclusive whole-brain connectomes from [[structural-connectivity]] data derived from [[diffusion-imaging]] and [[tractography]]. Third, the tool's compatibility with Spm and the broader Nilearn ecosystem means that preprocessed neuroimaging data from common pipelines can be readily imported into TVB for simulation.

## Related Software
- Spm — SUIT is developed within the SPM ecosystem
- [[nilearn]] — Python toolbox that can interface with SUIT outputs
- [[freesurfer]] — alternative cerebellar segmentation tool
- [[the-virtual-brain]] — whole-brain simulator that uses anatomical parcellations
- [[dipy]] — diffusion imaging toolbox for [[tractography]]
- [thecerebellum.com](](http://www.thecerebellum.com/)) — alternative cerebellar tools and atlases
- [CBS Tools](](https://www.nitrc.org/projects/cbs_tools/)) — complementary cerebellar segmentation in CBSTools/Itk Snap

## Key Papers

1. **Diedrichsen, J. (2006).** "A spatial unbiased atlas template of the human cerebellum." *NeuroImage*. First paper describing SUIT methodology.

2. **Diedrichsen, J., & Zotow, E. (2009).** "Probabilistic atlases of the human cerebellum." In *NeuroImage*.

3. **Ewert, S., et al. (2018).** "Neuroanatomical tract segmentation reveals the structural [[connectome]] of the human cerebellum." *Cerebral Cortex*.

## References

1. Siva Venkadesh, Yuhe Tian, Wendy Linn, Jessica Barrios Martinez, Harrison Mansour, J. Cook, David J. Schaeffer, D. Szczupak, Afonso C Silva, Allan Johnson, Fang‐Cheng Yeh. (2025). *A hierarchical framework for cortical and subcortical gray-matter [[parcellation]] across rodents, primates, and humans*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.09.08.675002))
2. (authors unknown). *Functional Network Organization of the Human Brain*.
3. Teppei Matsubara, Abbass Sohrabpur, Seppo Ahlfors, M. Jas, John G. W. Samuelsson, Padmavathi Sundaram, Steven M. Stufflebeam. (2026). *Quantifying Cerebellar Signal Detectability in MEG and EEG in Epilepsy Using Anatomically Informed Source Modeling*. bioRxiv. [DOI](](https://doi.org/10.64898/2026.01.14.699512))