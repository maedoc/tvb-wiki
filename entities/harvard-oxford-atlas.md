---
title: Harvard-Oxford Atlas
created: 2025-01-15
updated: 2026-04-29
type: entity
tags: [neuroimaging, neuroimaging-fmri, parcellation, software-fsl, brain-parcellations, functional-connectivity, structural-connectivity, connectomics]
sources: [https://fsl.fmrib.ox.ac.uk/fsl/docs/other/datasets.html, https://nilearn.github.io/stable/modules/generated/nilearn.datasets.fetch_atlas_harvard_oxford.html, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1359520/, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1457003/, https://www.sciencedirect.com/science/article/pii/S0920998920305837]
---

# Harvard-Oxford Atlas

## Overview

The Harvard-Oxford Atlas is a widely-used probabilistic brain parcellation that provides detailed anatomical segmentation of the human cerebral cortex and subcortical structures. Developed at the Center for Morphometric Analysis (CMA) at Harvard Medical School and distributed through the FMRIB Software Library (FSL) at the University of Oxford, this atlas has become a standard tool in neuroimaging research for defining regions of interest (ROIs) in [[fmri]] analysis, particularly in studies of [[resting-state]] functional connectivity and task-based activation studies[^1].

The Harvard-Oxford Atlas offers both **probabilistic** and **deterministic** (or categorical) parcellation schemes. The probabilistic version provides, for each voxel, the probability that it belongs to a particular anatomical region, calculated from manual segmentations of multiple individual brains that were then averaged and warped to a standard template. The deterministic version assigns each voxel a single label corresponding to the region with the highest probability. The atlas is distributed as part of the [[fsl]] (FMRIB Software Library) package and is natively defined in [[mni-space]] (Montreal Neurological Institute152 standard space), making it directly compatible with virtually all preprocessing pipelines for neuroimaging data[^1].

The cortical parcellation divides each hemisphere into 48 anatomically-defined regions, including frontal, parietal, temporal, occipital, and limbic lobes, as well as subdivisions such as the superior, middle, and inferior frontal gyri, the precuneus, and the parahippocampal gyrus. The subcortical parcellation includes 21 regions such as the thalamus, caudate nucleus, putamen, pallidum, hippocampus, and amygdala[^1]. A combined cortical-subcortical version is also available, providing comprehensive coverage of the entire brain in a single segmentation scheme.

## Key Features

One of the defining characteristics of the Harvard-Oxford Atlas is its **anatomical specificity**. Unlike purely connectivity-based parcellations (such as those derived from [[clustering]] algorithms applied to [[functional-connectivity]] data), the Harvard-Oxford Atlas regions are defined by clear anatomical boundaries that correspond to established neuroimaging literature and classical neuroanatomy. This makes it particularly valuable for hypothesis-driven research where investigators have *a priori* reasons to expect involvement of specific anatomical structures[^1].

The atlas employs a **probabilistic framework** that accounts for anatomical variability across individuals. The probabilistic maps indicate the proportion of subjects in which a given voxel falls within the boundaries of each region, calculated from 21 healthy male and 16 healthy female subjects (ages 18-50) whose T1-weighted images were individually segmented and affine-registered to MNI152 space using FLIRT[^1]. This approach provides a principled way to handle the well-known anatomical variability across individuals in the human population, a particularly important consideration when working with clinical populations or across diverse samples.

The atlas is available at multiple **spatial resolutions**, including 1mm and 2mm isotropic voxels in MNI space, allowing researchers to choose an appropriate tradeoff between spatial specificity and computational efficiency for their particular application[^2]. The 2mm resolution version is perhaps the most commonly used, as it provides a good balance between the number of voxels per region (ensuring adequate sampling for resting-state analyses) and the total number of regions in the atlas. The 1mm version offers higher spatial precision but requires significantly more computational resources.

## Relationship to The Virtual Brain

The Harvard-Oxford Atlas is highly relevant to [[whole-brain modeling]] and [[the-virtual-brain]] (TVB) workflows in several ways. In TVB, empirical structural connectivity matrices are often derived from diffusion imaging and tractography data, and these matrices are used to define the anatomical skeleton of whole-brain network models. When extracting connectivity data from empirical DWI scans, researchers frequently use the Harvard-Oxford Atlas to define the ROIs from which tractography streams are initiated or terminated, essentially using the atlas regions as nodes in the structural connectivity network[^3].

Beyond structural connectivity, the Harvard-Oxford Atlas can serve as a **source space** for simulating neuroimaging signals in TVB. After running network simulations (typically using neural mass models or reduced models such as the Wong-Wang model), the simulated neural activity can be projected onto the atlas regions to generate synthetic BOLD (Blood-Oxygen-Level-Dependent) signals using the hemodynamic response function model. These synthetic signals can then be compared directly to empirical fMRI data for model validation or parameter optimization[^3].

The atlas also facilitates **comparative model validation** by providing a common parcellation scheme. When comparing whole-brain models parameterized in different ways, or when benchmarking TVB against other whole-brain simulators, using the same atlas ensures that the comparison is fair and that differences are not attributable to discrepancies in region definitions. The TVB ecosystem includes support for the Harvard-Oxford Atlas through its integration with the nilearn library and direct FSL dataset loading capabilities[^3].

## Relationship to Other Atlases

The Harvard-Oxford Atlas is one of several widely-used anatomical parcellations in neuroimaging research. It complements other atlases such as the [[aal-atlas]] (Automated Anatomical Labeling), which provides a similar number of regions but uses a different anatomical parcellation scheme, and the [[desikan-killiany-atlas]], which is a FreeSurfer-derived parcellation based on cortical curvature and sulcal patterns. The related [[destrieux-atlas]] provides an alternative cortical parcellation with finer-grained subdivisions[^4].

The [[glasser-atlas]] represents a newer generation of parcellations that integrate anatomical and functional connectivity information through the Human Connectome Project, while the [[schaefer-atlas]] provides a purely connectivity-based 100- to 1000-region parcellation derived from resting-state data[^4]. The Jülich-Brain cytoarchitectonic atlas offers another probabilistic alternative based on post-mortem histological analysis, providing higher anatomical precision but requiring more complex integration workflows.

In the TVB ecosystem, parcellation choice is an important consideration, and the library supports multiple atlases including variants of the Harvard-Oxford Atlas. Researchers working with TVB should consider the tradeoffs between anatomical specificity, number of regions, and the specific research question when selecting a parcellation scheme.

## Key Papers

The Harvard-Oxford Atlas was constructed using segmentations from the Harvard Center for Morphometric Analysis. The foundational methodology is described in association with multiple studies from this group, including work on insula volume in schizophrenia by Makris et al. (2006) which demonstrates the application of the atlas to psychiatric neuroimaging[^5]. Additional validation comes from pediatric bipolar disorder research by Frazier et al. (2005) using these anatomical segmentations[^6].

The automated labeling system that influenced the Harvard-Oxford cortical parcellation scheme was described by Desikan et al. (2006) in Neuroimage, providing a gyral-based region-of-interest definition method that complements the Harvard-Oxford approach[^7]. Goldstein et al. (2007) further applied these methods to investigate hypothalamic abnormalities in schizophrenia[^8].

A comparative parcellation framework (HOA2.0-ComPaRe) extending the Harvard-Oxford Atlas to human-macaque comparisons was published in Frontiers in Neuroanatomy (2022), demonstrating the lasting impact and continued development of this anatomical framework[^4].

## Related Software

* [[fsl]] — Primary distribution platform for the Harvard-Oxford Atlas
* [[freesurfer]] — Alternative anatomical parcellation workflows
* [[mne-python]] — EEG/MEG analysis that can incorporate anatomical information
* [[nilearn]] — Python toolbox for neuroimaging that includes atlas loading utilities
* [[brainnetome-atlas]] — A further subdivided anatomical parcellation
* [[connectome-workbench]] — Visualization tool compatible with volume-based atlases

## References

[^1]: https://fsl.fmrib.ox.ac.uk/fsl/docs/other/datasets.html
[^2]: https://nilearn.github.io/stable/modules/generated/nilearn.datasets.fetch_atlas_harvard_oxford.html
[^3]: https://docs.thevirtualbrain.org/manuals/UserGuide/UserGuide-UI_Connectivity.html
[^4]: https://www.sciencedirect.com/science/article/pii/S0920998920305837
[^5]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1359520/
[^6]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1457003/
[^7]: https://pubmed.ncbi.nlm.nih.gov/16644248/
[^8]: https://pubmed.ncbi.nlm.nih.gov/17338948/