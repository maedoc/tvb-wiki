---
created: 2026-04-20
sources:
- raw/papers/van-essen-2013.md
- raw/papers/barch-2013.md
- raw/papers/smith-2013-hcp.md
tags:
- database-hcp
- neuroimaging-fmri
- neuroimaging-dti
- connectomics
- structural-connectivity
- functional-connectivity
- resting-state
- task-based
- dataset
title: HCP Dataset
type: concept
updated: '2026-05-06'
---

The **HCP Dataset** refers to the publicly released [[neuroimaging]] data from the Human Connectome Project (HCP), a landmark initiative to map the structural and functional connectivity of the healthy adult human brain. Unlike its parent initiative (the [[human-connectome-project]]), which encompasses the broader research program, the HCP Dataset specifically denotes the curated collection of multimodal brain imaging scans acquired using standardized protocols and made openly available to the neuroscience community. The dataset comprises structural MRI, task-based functional MRI, resting-state functional MRI, and [[diffusion-imaging]] data from approximately 1200 healthy young adults, representing the largest and most comprehensively characterized neuroimaging repository of its kind when first released [1].

## Motivation and Scientific Context

Prior to the HCP Dataset, whole-brain modeling efforts were constrained by fragmented datasets acquired with heterogeneous protocols across different institutions, making cross-study comparisons difficult and limiting the statistical power of connectivity analyses. The HCP Dataset addressed this by establishing uniform acquisition standards and preprocessing pipelines, enabling researchers to construct [[structural-connectivity]] matrices and [[functional-connectivity]] maps with unprecedented consistency. For [[whole-brain-modeling]] specifically, the dataset provides the empirical foundation upon which [[connectome]]-based simulations can be validated, offering both the anatomical wiring diagrams derived from diffusion imaging and the functional dynamics observed in resting-state and task-evoked fMRI acquisitions.

The impact of this dataset on computational neuroscience has been substantial. Prior to its release, researchers building [[neural-mass-model]]s and [[whole-brain]] simulations often relied on small sample sizes or disparate data sources that limited generalizability. The HCP Dataset's sample of approximately 1200 subjects provides statistical power for robust connectivity analyses and enables population-level characterization of individual differences in brain network architecture [1]. This has been particularly valuable for parameter-estimation in [[personalized-brain-modeling]] workflows, where individual subject connectivity profiles can inform simulation parameters.

## Dataset Contents and Acquisition Protocols

The HCP Dataset incorporates multiple imaging modalities designed to capture complementary aspects of brain organization. Structural MRI acquisitions include T1w and T2w images at high resolution (0.7 mm isotropic) providing detailed anatomical delineation for [[parcellation]] and [[parameter-estimation]] purposes [1]. The high spatial resolution supports accurate delineation of cortical boundaries and subcortical structures, essential for defining regions of interest in whole-brain models.

The diffusion imaging protocol employs multi-shell HARDI (high angular resolution diffusion imaging) with b-values of 1000, 2000, and 3000 s/mm², enabling robust [[tractography]] reconstruction of white-matter pathways and the derivation of [[structural-connectivity]] matrices at resolutions defined by the [[glasser-atlas]] (360 regions) or alternative parcellation schemes [1]. Multi-shell acquisition improves the angular resolution of fiber orientation estimates, particularly in regions with complex crossing fibers, leading to more reliable structural connectivity matrices. This is particularly important for [[whole-brain-modeling]] applications where the quality of anatomical coupling directly influences simulated dynamics.

The multi-shell HARDI data also enables the application of advanced microstructural models such as neurite orientation dispersion and density imaging (NODDI), which can be fit to the acquired diffusion signals to estimate neurite density and orientation dispersion indices [1]. However, it is important to note that NODDI is not part of the official HCP preprocessing pipeline or standard data releases—it is a post-hoc analysis method that researchers can apply to the multi-shell data. Derived metrics from the standard pipeline include [[fractional-anisotropy]] (FA), mean diffusivity (MD), and orientation dispersion (OD), which provide quantitative measures of [[white-matter]] microstructural properties that can be incorporated as edge weights in structural [[connectivity]] matrices [1].

Functional MRI data in the HCP Dataset encompasses both [[resting-state]] and task-based acquisitions. Resting-state fMRI was collected using a multiband echo-planar imaging sequence achieving 2 mm isotropic spatial resolution and 0.72 s temporal resolution [3], capturing spontaneous low-frequency fluctuations in the blood-oxygen-level-dependent signal that reveal [[intrinsic-connectivity-networks]] such as the [[default-mode-network]]. The accelerated temporal resolution enabled by multiband acquisition significantly improves the fidelity of resting-state connectivity estimates by reducing aliasing of high-frequency physiological noise, making the HCP Dataset particularly valuable for studying fast network dynamics that might be obscured in conventional fMRI acquisitions with longer repetition times [3].

The task-[[fmri]] component employs a battery of seven paradigm categories [2] probing emotion processing, gambling decisions, language comprehension and production, motor execution, relational reasoning, social cognition, and working memory, enabling characterization of task-evoked activation patterns and comparison with [[functional-connectivity]] dynamics observed at [[rest]]. This extensive task battery, administered to each participant, provides an unprecedented resource for investigating how brain networks reconfigure between cognitive states—a capability directly relevant to whole-brain models seeking to reproduce task-evoked changes in functional connectivity [2]. The paradigms were designed to maximize reliability and coverage of major cognitive domains, providing a standardized resource for studying task-based [[brain-dynamics]] [2].

## Preprocessing and Derived Data Products

A distinguishing feature of the HCP Dataset is the extensive preprocessing pipeline applied before public release, implementing artifact removal, motion correction, and registration to standard [[mni-space]] coordinates. The HCP preprocessing pipelines (available as [[hcp-pipelines]]) employ sophisticated algorithms for fieldmap unwarping, intensity normalization, and surface projection, substantially reducing the analytical burden on downstream users [1]. Critically, the HCP pipeline performs both volume-based and surface-based preprocessing, with subsequent alignment to a common grayordinate space that combines cortical surface vertices with subcortical volume voxels—this [[cifti]] (Connectivity Informatics Technology Initiative) format has become a de facto standard for representing whole-brain connectivity data.

Derived data products include CIFTI-format dense connectomes representing voxel-wise functional connectivity, grayordinate files combining surface and volume representations, and pre-computed connectivity matrices parcellated according to multiple atlas schemes including the [[glasser-atlas]] (360 regions), [[yeo-atlas]] (7 and 17 networks), and [[desikan-killiany-atlas]] (68 cortical regions) [3]. These refined outputs have become reference datasets for benchmarking [[parcellation]] algorithms, [[community-detection]] methods, and [[graph-theory]] metrics applied to brain networks. The availability of multiple parcellation schemes enables researchers to investigate how choice of spatial resolution affects connectivity estimates—a methodological question directly relevant to whole-brain modeling where the parcellation defines the node resolution of the network model.

The dataset also includes processed derivatives such as task contrast maps, dual-regression ICA components, and timeseries extracted from predefined regions, all deposited in [[bids]] (Brain Imaging Data Structure)-compliant format with appropriate metadata [1]. This standardization facilitates automated analysis workflows and enables reproducible research practices that are essential for methodological comparisons across studies.

## Relationship to The Virtual Brain

The HCP Dataset serves as a critical data source for [[the-virtual-brain]] (TVB) workflows that construct personalized [[bold-model]]s from empirical connectivity data. TVB's [[tvb-adapters]] and connectivity pipeline tools can ingest HCP-derived structural connectivity matrices to define the anatomical coupling between neural populations in simulations of brain dynamics. The resting-state fMRI data enables validation of simulated functional connectivity against empirical patterns, facilitating parameter-optimization routines that tune model parameters to match observed brain states.

Studies employing HCP data within TVB have investigated [[brain-oscillations]], [[epilepsy-modeling]], and personalized approaches to [[personalized-brain-modeling]] where individual subject connectivity profiles inform simulation parameters [1]. The high-fidelity structural connectivity matrices derived from HCP diffusion data provide particularly valuable inputs for TVB simulations, as the multi-shell HARDI protocol enables more accurate tractography reconstruction compared to single-shell acquisitions. The dataset's comprehensive characterization of both structural and functional connectivity enables end-to-end workflows where empirical data informs model construction, simulated dynamics are validated against held-out empirical data, and model parameters are optimized to minimize discrepancies between simulated and observed functional networks.

## Relationship to Other Datasets and Resources

The HCP Dataset intersects numerous concepts in the [[connectomics]] and neuroimaging domains. It provides the empirical basis for [[structural-connectivity]] reconstruction, serves as the source data for [[functional-connectivity]] analyses, and supports both [[resting-state]] and task-based research paradigms. The dataset's multi-modal nature enables integration of diffusion-imaging-derived tractography with fMRI-based functional dynamics, supporting [[effective-connectivity]] analyses and [[dynamic-causal-modeling]] approaches.

Alternative large-scale neuroimaging resources include [[abide]] for autism research and the [[uk-biobank]] for population-level studies, though these differ in demographic composition and acquisition protocols. The HCP Young Adult dataset specifically targets healthy subjects aged 22-35, making it ideal for studying typical brain organization but limiting its applicability to developmental or clinical populations [1]. For researchers requiring pediatric data, the ABCD (Adolescent Brain Cognitive Development) study provides a complementary resource, while the UK Biobank offers longitudinal data on [[aging]] populations. The HCP also released the [[hcp-meg2]] dataset incorporating magnetoencephalography, enabling investigation of fast electrophysiological dynamics that complement the slower [[bold-signal]] captured in fMRI acquisitions [1].

## Known Limitations

While the HCP Dataset represents a landmark resource, users should be aware of several limitations. The sample, while large, is not representative of the general population—it comprises predominantly Caucasian individuals with high socioeconomic status, limiting generalizability of findings to more diverse populations [1]. Additionally, the scanning protocol, while state-of-the-art, employs multiband sequences that introduce unique artifacts (such as SARI and cross-scan contamination) that require specialized handling. The extensive preprocessing applied by the HCP consortium, while reducing burden on users, also limits transparency regarding how raw data has been transformed. Despite these limitations, the HCP Dataset remains one of the most comprehensive and widely used neuroimaging resources for studying human brain connectivity and serves as a foundational dataset for the field of [[computational-neuroscience]].

## References

1. (authors unknown). *The WU-Minn Human Connectome Project: An Overview*.
2. (authors unknown). *Function in the Human Connectome: Task-fMRI and Individual Differences in Behavior*.
3. (authors unknown). *Resting-State fMRI in the Human Connectome Project*.