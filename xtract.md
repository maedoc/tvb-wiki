---
title: XTRACT
created: 2025-01-15
updated: 2026-04-30
type: entity
tags: [software-tractography, diffusion-imaging, tractography, fsl, white-matter, software-fsl, structural-connectivity, connectomics, neuroimaging-dti]
sources: [raw/papers/xtract-2020-neuroimage.md, raw/papers/xtract-2022-science-advances.md]
---

## Overview

XTRACT (cross-species tractography) is a command-line software tool developed by the FMRIB (Oxford) group for automated probabilistic tractography that enables standardized extraction of white matter tracts in humans, macaques, and other species. Released as part of [[fsl]] (FMRIB Software Library), XTRACT provides a library of predefined tractography protocols along with the computational infrastructure to run tractography across large cohorts of subjects. The tool was designed to address a critical problem in diffusion MRI-based tractography: the lack of standardized, reproducible methods for extracting anatomically defined white matter pathways across multiple subjects and species. Developed primarily by Shaun Warrington, Saad Jbabdi, and Stamatios N. Sotiropoulos at the University of Nottingham and Oxford, XTRACT represents a significant advance in automated white matter dissection that rivals traditional anatomical dissection approaches while being entirely non-invasive.

The software operates by reading standardized protocol definitions—comprising seed, target, exclusion, and stop masks defined in template space—and applying them to individual subjects' diffusion data through warping operations. Tractography is performed using FSL's [[probtrackx2]] (probabilistic tractography), which models crossing fibers and provides robust uncertainty estimates. XTRACT supports both standard-space and native-space tractography, with GPU acceleration available for computationally intensive workflows. The system generates population-level tract atlases by averaging binarized individual tract reconstructions, making it particularly valuable for large-scale neuroimaging studies such as the [[hcp-dataset]] and [[uk-biobank]].

## Key Features

XTRACT offers several distinguishing features that set it apart from other tractography tools. First, the software includes pre-built protocols for 42 major white matter tracts, covering association fibers (including the arcuate fasciculus, superior longitudinal fasciculus variants, inferior fronto-occipital fasciculus, uncinate fasciculus, and others), projection fibers (corticospinal tract, thalamic radiations, acoustic radiation, optic radiation), limbic fibers (cingulum subsections, fornix), and commissural fibers (corpus callosum segments via forceps major/minor, anterior commissure, middle cerebellar peduncle). These protocols were developed through careful anatomical expertise and validated against known neuroanatomy, with protocols designed to be applicable across both human and macaque brains using homologous mask definitions in their respective template spaces.

Second, XTRACT provides a framework for creating custom tractography protocols. Users can define their own tracts by creating seed, target, exclusion, and stop masks in any standard space (such as [[mni-space]]), making the tool extensible for new research applications. The protocol definition system supports multiple seeding strategies, including standard single-ROI seeding and reverse-seeding (where seed-target pairs are swapped and results combined for improved robustness). Third, the software integrates seamlessly with the broader FSL ecosystem, utilizing [[bedpostx]] for fiber orientation distribution modeling and FNIRT for non-linear registration between standard and native spaces.

Beyond basic tract extraction, XTRACT includes several auxiliary tools that extend its utility. The connectivity blueprint functionality ([xtract_blueprint]) computes a full matrix of cortical-to-tract connectivity, enabling detailed analyses of where each white matter bundle terminates on the cortical surface. This approach has proven particularly valuable for comparative neuroimaging studies examining evolutionary changes in brain connectivity. Additional tools include [xtract_stats] for extracting summary metrics (volume, length, fractional anisotropy) from reconstructed tracts, [xtract_qc] for quality control across cohorts, and [xtract_divergence] for comparing connectivity blueprints across individuals, groups, or species using Kullback-Leibler divergence measures.

The software has demonstrated robustness across varying data quality, having been validated on both high-resolution [[human-connectome-project]] data (1.25mm isotropic resolution,multi-shell diffusion) and more typical clinical-quality [[uk-biobank]] data (2mm isotropic resolution). Inter-subject correlation analyses showed similar tract reproducibility across these very different datasets, indicating that XTRACT protocols are generalizable and not overly dependent on ultra-high-quality data. Furthermore, the protocols preserve individual anatomical variability, as demonstrated through twin studies showing greater tract similarity between monozygotic twins than between unrelated subjects.

## Relationship to TVB

While XTRACT is primarily a tool for extracting white matter tractography from diffusion MRI data, its outputs are directly relevant to [[the-virtual-brain]] (TVB) modeling workflows. TVB constructs whole-brain connectivity matrices using structural connectivity data derived from diffusion imaging and tractography, and XTRACT provides a standardized, reproducible method for generating these tractograms. The tract atlases produced by XTRACT (from HCP and UK Biobank data) can be used as population-level priors for TVB connectome construction, ensuring that the structural connectivity basis for brain network simulations reflects established anatomical knowledge.

In TVB workflows, XTRACT-derived tractography can feed into the construction of [[structural-connectivity]] matrices that form the anatomical scaffold for neural mass model simulations. The connectivity blueprint outputs are particularly relevant for TVB's region-based modeling approach, where understanding the precise cortical termination patterns of major white matter tracts enables more anatomically accurate connectivity weightings. Additionally, XTRACT's cross-species capabilities align with TVB's interest in comparative brain modeling, allowing researchers to construct homologous connectivity matrices across humans and non-human primates for evolutionary studies or translational disease modeling.

## Key Papers

The seminal XTRACT methodology paper appeared in NeuroImage: Warrington et al. (2020) "XTRACT - Standardised protocols for automated tractography in the human and macaque brain" DOI:10.1016/j.neuroimage.2020.116923. This paper established the 42-tract protocol library and demonstrated cross-species applicability using HCP (n=1021) and UK Biobank (n=1000) human data plus macaque ex vivo data (n=6). The authors showed robust tract extraction across data qualities, preservation of lateralization patterns, and individual variability through twin analyses.

A subsequent Science Advances paper extended XTRACT to neonatal brains: Warrington et al. (2022) "Concurrent mapping of brain ontogeny and phylogeny within a common space: Standardized tractography and applications" DOI:10.1126/sciadv.abq2022. This work demonstrated XTRACT protocols for human infants and directly compared developmental (ontogeny) and evolutionary (phylogeny) trajectories in white matter organization using the common framework established for cross-species comparison.

Additional methodological extensions include Assimopoulos et al. (2024) in Brain Structure and Function DOI:10.1007/s00429-024-02760-0, which generalized macaque protocols across multiple template spaces (D99, INIA, NMT, YRK), and Assimopoulos et al. (2024) in eLife DOI:10.7554/eLife.107012, which extended the framework to cortico-subcortical tractography with enhanced subcortical protocols.

## Technical Implementation

The XTRACT workflow begins with preprocessed diffusion MRI data that has undergone eddy current and motion correction (via FSL's eddy), susceptibility distortion correction (via topup), brain extraction (via BET), and crossing fiber modeling (via bedpostx). The bedpostx output provides fiber orientation distribution functions that inform probabilistic tractography, with up to three fiber populations modeled per voxel. Registration to standard space uses FNIRT-generated warp fields that map between native diffusion space and template space (MNI152 for humans, F99 for macaques).

The tractography process itself follows a protocol-specific sequence: standard-space masks (seed, target, exclusion, stop) are inverse-warped into each subject's native diffusion space, where probabilistic streamline tracking proceeds. Streamlines are initiated from seed voxels and propagate according to the orientation distribution functions, with termination occurring when exiting the brain, exceeding curvature thresholds, or entering exclusion/termination masks. For reverse-seeding protocols, tractography runs in both seed→target and target→seed directions, with resulting path distributions combined to improve robustness. Results are normalized by the total number of valid streamlines and can be transformed back to standard space for group-level analysis.

The output format consists of tract-specific density maps (probability distributions of streamline visitation) stored in NIfTI format, with options for outputting at native or standard space resolution. Tract atlases are generated by applying a probability threshold (typically 0.5%) to individual tracts, binarizing the result, and averaging across subjects to produce population percentage coverage maps. The primary output for connectivity blueprint analyses is a cortical surface × tract matrix in CIFTI format, representing the termination pattern of each tract on the cortical sheet.

## Related Software

XTRACT is part of the broader [[fsl]] ecosystem and integrates with several related tools. [[bedpostx]] provides the crossing-fiber diffusion model required for tractography, while [[fsl-anat]] and FNIRT handle registration. Visualization is supported through [[fsleyes]], and the tract atlases integrate with other FSL neuroimaging pipelines. Related tractography tools include [[trackvis]] (DTI Studio), [[dsi-studio]], [[mrtrix3]] (which provides complementary global tractography approaches), and [[dipy]] for Python-based diffusion imaging workflows. For connectivity analysis, XTRACT outputs can be used with [[brain-connectivity-toolbox]] or [[graphvar]] for network-level analyses. The [[connectome-workbench]] tool is useful for visualizing connectivity blueprint outputs in CIFTI format.

## See Also

- [[tractography]]
- [[diffusion-mri]]
- [[structural-connectivity]]
- [[fsl]]
- [[human-connectome-project]]
- [[white-matter]]
- [[probtrackx]]
- [[connectivity]]
- [[brain-atlases]]