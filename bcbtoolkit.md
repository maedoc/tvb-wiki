---
title: BCBToolKit
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-brain-modeling, connectomics, structural-connectivity, functional-connectivity, diffusion-imaging, tractography, neuroimaging-fmri, stroke, brain-stimulation]
sources: [raw/papers/foulon-2018.md, raw/papers/thiebaut-2020.md]
---

## Overview

BCBToolKit (Brain Connectivity and Behaviour Toolkit) is a free and open-source software package developed by the Brain Connectivity and Behaviour Laboratory (BCBlab) led by Michel Thiebaut de Schotten at Sorbonne University in Paris. The toolkit provides the scientific community with several complementary tools to indirectly assess brain disconnections resulting from focal brain lesions such as stroke or surgical resections. Unlike traditional lesion-symptom mapping approaches that focus solely on visibly damaged brain tissue, BCBToolKit implements methods to measure the downstream effects of lesions on anatomically and functionally connected brain regions—a paradigm shift toward associationist principles in cognitive neuroscience.

The software addresses a critical gap in clinical neuroimaging: while modern diffusion-weighted imaging tractography can accurately depict how brain areas are connected through white matter pathways, and resting-state functional magnetic resonance imaging measures activity within and between brain regions, these powerful techniques remain severely underutilized in patient populations. BCBToolKit bridges this gap by providing automated pipelines that combine structural connectivity analysis with functional connectivity estimates to predict cognitive and behavioral deficits arising from brain damage.

## Theoretical Foundation

The theoretical framework underlying BCBToolKit rests on the fundamental principle that brain functions emerge from the interaction between distributed brain regions rather than from localized cortical areas alone. This associationist perspective, with roots extending back to nineteenth-century neurologists like Paul Broca and Carl Wernicke, has gained renewed prominence through modern connectomics research.

When a focal brain lesion occurs, it produces not only local damage but also remote effects through two primary mechanisms. First, anatomical disconnections occur when white matter tracts connecting the lesioned area to other brain regions are interrupted—the lesion effectively severs the anatomical "wiring" that enables communication between brain regions. Second, diaschisis refers to the functional disruption of distant regions that are connected to the damaged area, even without direct structural damage. These distant regions may show reduced metabolic activity, altered cortical thickness, and modified functional connectivity patterns that contribute to the patient's clinical presentation.

Traditional voxel-based lesion-symptom mapping (VLSM) approaches assume that a single lesioned region is responsible for symptoms and that non-overlapping lesions compete for statistical significance. However, BCBToolKit adopts an associationist framework assuming that several interconnected regions jointly contribute to behavioral and cognitive functions. This approach better reflects the distributed nature of cognitive processes in the human brain.

## Key Features and Tools

### Disconnectome Mapping

The core functionality of BCBToolKit involves creating probabilistic disconnectome maps that estimate which brain regions are disconnected by a given lesion. The pipeline proceeds by first registering the patient's lesion mask to a healthy control tractography dataset—typically derived from the Human Connectome Project. Tractography is then performed from the lesion as a seed region, and visitation maps are computed to identify streamlines passing through the damaged area. These individual tractography maps are then averaged across the control population to produce a probability map where each voxel indicates the likelihood of disconnection ranging from 0 to 1.

This approach accounts for inter-individual variability in white matter anatomy and provides a continuous measure of disconnection severity rather than binary presence/absence. Research has demonstrated that disconnectome maps show high anatomical similarity across age groups and maintain reproducibility even with relatively small control samples of approximately 10 participants.

### Tractotron

Tractotron provides an atlas-based approach to white matter tract disconnection analysis. Given a lesion location in standard MNI152 space, Tractotron queries a probabilistic atlas of major white matter tracts—including the arcuate fasciculus, frontal aslant tract, uncinate fasciculus, and inferior fronto-occipital fasciculus—to identify which tracts are likely disconnected. The atlas indicates for each voxel the probability of finding a given white matter tract; Tractotron typically applies a 50% probability threshold to consider a tract as disconnected.

This method provides a quick assessment of tract-level disconnection and is particularly useful for investigating the involvement of well-characterized white matter pathways in cognitive deficits. The approach complements the more comprehensive disconnectome mapping by providing tract-specific summaries that can be compared across patients.

### AnaCOM2

The AnaCOM2 (Anatomo-Clinical Overlapping Maps) tool implements cluster-based lesion-symptom mapping that identifies clusters of brain regions whose disconnection is associated with specific behavioral deficits. Unlike traditional VLSM that treats each voxel independently, AnaCOM2 groups voxels with similar distributions of neuropsychological scores into clusters. For each cluster above a minimum size threshold (typically 8 mm³), the tool performs non-parametric statistical comparisons between patients with disconnection in that cluster and healthy controls.

The method handles multiple non-overlapping brain regions that may contribute to a given function without requiring them to compete for statistical significance—aligning with the associationist philosophy that several interconnected regions jointly support cognitive processes. Results are Bonferroni-Holm corrected for multiple comparisons to control false discovery rates.

### Enantiomorphic Normalization

A significant technical challenge in processing images from patients with brain lesions is that standard spatial normalization algorithms can fail when tissue segmentation is disrupted by the lesion. BCBToolKit implements the enantiomorphic normalization approach originally described by Nachev and colleagues, in which the lesion is symmetrically "filled" using the healthy contralateral hemisphere before normalization. This enantiomorphic T1 image is then used for bias field correction and registration, after which the original (unfilled) lesion mask is transformed to standard space using the calculated deformations.

This preprocessing step is essential for accurate spatial normalization of lesioned brains and enables subsequent analyses including cortical thickness measurement and functional connectivity analysis.

### Functional Connectivity Analysis

BCBToolKit incorporates tools for analyzing the functional connectivity of regions affected by disconnection. Using resting-state fMRI data from healthy controls, the software computes seed-based connectivity maps from disconnected regions to identify the broader networks of functionally connected areas that may be indirectly affected by the lesion. This approach reveals how damage to a single region can propagate through large-scale brain networks.

A principal component analysis can then be applied to these connectivity matrices to identify major factor-networks that account for variance in functional connectivity patterns. Research on category fluency has identified three primary networks involved: the cingulo-opercular network, the cortico-striatal network, and the ventral fronto-parietal network.

### Cortical Thickness and Entropy Measures

Beyond connectivity analysis, BCBToolKit provides tools for estimating structural changes in disconnected regions. Cortical thickness is computed using the DiReCT (Diffeomorphic Registration-based Cortical Thickness) algorithm, which estimates the distance between the gray-white matter interface and the gray matter-cerebrospinal fluid interface. This method shows good scan-rescan reliability and can predict demographic variables such as age and gender with high statistical power.

Shannon entropy of resting-state fMRI time series serves as a surrogate measure of the local complexity of neural activity. Since "neurons that fire together wire together," entropy provides an information-theoretic estimate of the complexity of spontaneous neuronal activity and the density of local and long-range connections.

## Relationship to The Virtual Brain

While BCBToolKit and [[the-virtual-brain]] both address brain connectivity and function, they serve complementary roles in the research ecosystem. [[The Virtual Brain]] is a whole-brain simulation platform that enables researchers to construct and run computational models of brain dynamics based on structural connectivity matrices derived from diffusion imaging data. TVB focuses on forward modeling—understanding how network structure gives rise to dynamics and behavior through simulation.

In contrast, BCBToolKit focuses on inverse problems—estimating the functional and structural consequences of observed lesions in real patient populations. The disconnectome maps produced by BCBToolKit can provide structural connectivity information that feeds into TVB models, enabling researchers to simulate how disconnection might affect brain dynamics in individual patients. This integration represents a promising direction for personalized brain modeling in clinical populations.

Both toolkits share dependencies on [[fsl]] for image processing and leverage [[diffusion-imaging]] and [[tractography]] methodologies. BCBToolKit's emphasis on lesion analysis complements TVB's simulation capabilities, creating a workflow where patient-specific disconnectome estimates can inform personalized computational models.

## Key Papers

The primary methodology paper describing BCBToolKit was published by Foulon and colleagues in GigaScience (2018), providing detailed descriptions of all analysis tools along with validation data from 37 patients with frontal lobe lesions. This foundation was extended in subsequent work, most notably the Nature Communications paper by Thiebaut de Schotten and colleagues (2020), which applied the toolkit to the largest stroke lesion dataset (n = 1333) to create an Atlas of White Matter Function mapping 590 cognitive processes to specific white matter pathways.

The 2020 study demonstrated that brain disconnections show stronger correspondence with task-related fMRI activation patterns than lesion locations alone, providing evidence that disconnectome analysis provides a more accurate substrate for understanding brain-behavior relationships. The study also revealed that the stereotyped distribution of stroke lesions has influenced our taxonomy of brain functions, suggesting that disconnectome-based approaches may help correct longstanding biases in functional localization.

## Practical Considerations

BCBToolKit is compatible with Linux and macOS operating systems and requires FSL (FMRIB Software Library), R, Java, and Python 2.7 with NumPy. The toolkit is distributed under a BSD 3-Clause license and is available for download from http://toolkit.bcblab.com. A command-line interface (run_disco.sh) enables batch processing of disconnectome maps without the graphical user interface, facilitating high-throughput analyses in large patient cohorts.

Lesion masks must be registered to MNI space at the same resolution as the tractography atlas (typically 2mm isotropic). The toolkit includes a default tract atlas derived from 178 healthy controls, with larger atlases available for download. For cortical thickness analysis, the enantiomorphic filling step is essential to prevent contamination of tissue segmentation by the lesion.

## Clinical and Research Applications

BCBToolKit has been applied to investigate disconnection syndromes in various clinical populations including stroke patients, individuals with [[epilepsy-modeling]] following surgical resection, and patients with neurodegenerative conditions. The toolkit enables researchers to test hypotheses about the anatomical substrates of cognitive deficits while accounting for the distributed nature of brain connectivity.

TheDisconnectome Symptoms Discoverer, a web application built on BCBToolKit methods, predicts expected neuropsychological scores one year after stroke based on individual disconnectome maps—demonstrating the clinical translation potential of these computational approaches. Future directions include extension to predict treatment outcomes and guide rehabilitation strategies.

## Related Software

BCBToolKit complements other connectivity analysis tools in the neuroimaging ecosystem. Unlike the [[brain-connectivity-toolbox]] (BCT), which provides graph-theoretic measures for analyzing already-constructed brain networks, BCBToolKit focuses on constructing the connectivity representations from lesion data. The toolkit integrates with [[fsl]] for image processing, [[ants]] for registration-based cortical thickness estimation, and TrackVis for tractography visualization.
