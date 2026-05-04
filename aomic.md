---
title: AOMIC
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [dataset, database, neuroimaging, resting-state, functional-connectivity, structural-connectivity]
sources:
  - Snoek et al. 2021 (Scientific Data, 8, 1-23)
  - "https://www.nature.com/articles/s41597-021-00870-6"
---

AOMIC (Amsterdam Open MRI Collection) is a publicly available neuroimaging dataset comprising magnetic resonance imaging (MRI) data collected from healthy volunteers at the University of Amsterdam in the Netherlands. The dataset was established to address the growing need for large-scale, well-characterized neuroimaging data in the connectomics community, providing multimodal MRI scans—including T1-weighted structural, resting-state functional, and diffusion tensor imaging (DTI)—alongside detailed phenotypic information for each participant. First described in detail by Snoek and colleagues in their 2021 Nature Scientific Data publication, AOMIC represents one of several open neuroscience datasets that have emerged to support reproducibility and collaborative research in whole-brain modeling and computational neuroscience [@snoek2021amsterdam].

## Overview and Motivation

The rationale behind AOMIC stems from the broader movement toward open science in neuroimaging, which seeks to democratize access to high-quality MRI data and enable independent replication of findings across laboratories [@nichols2017best]. Prior to the establishment of datasets like AOMIC, researchers often relied on proprietary or fragmented data collections, limiting the scalability of connectome-based analyses and whole-brain modeling efforts. By consolidating MRI data from multiple studies conducted at VU Amsterdam into a standardized format, AOMIC enables researchers to investigate individual differences in brain structure and function, test novel analysis pipelines, and train computational models requiring large sample sizes.

AOMIC aligns with other major open neuroimaging initiatives, including the [[human-connectome-project]] (HCP) [@vanessen2013wu], the [[abide]] dataset, and the [[uk-biobank]] imaging cohort [@miller2016multimodal]. However, AOMIC distinguishes itself through its focus on the Dutch population, inclusion of specific clinical subgroups, and emphasis on providing raw, minimally preprocessed data to facilitate method development. The dataset is distributed in [[bids]] (Brain Imaging Data Structure) format [@gorgolewski2016brain], ensuring compatibility with standard neuroimaging processing workflows and tools such as [[fmriprep]] [@esteban2019fmriprep], [[mrtrix3]] [@tournier2019mrtrix3], and [[dipy]].

## The Three AOMIC Sub-Datasets

AOMIC comprises three distinct datasets, each with its own sample characteristics and imaging protocols. The **ID1000** dataset contains data from 928 participants recruited to be representative of the general Dutch population in terms of educational level, drawn from a limited age range of 19–26 years to minimize the effects of aging on brain-related covariates [@snoek2021amsterdam]. The **PIOP1** (Population Imaging of Psychology 1) dataset includes 216 university students from Amsterdam, while the **PIOP2** dataset comprises 226 university students. Both PIOP datasets were collected between 2015 and 2017, with PIOP2 following after a scanner upgrade at the imaging center.

Each dataset includes T1-weighted structural MRI, diffusion-weighted imaging, and both resting-state and task-based functional MRI. Task paradigms include movie watching (ID1000), working memory, emotion matching, face perception, gender-stroop, emotion anticipation (PIOP1), and stop-signal tasks (PIOP2). Notably, physiological data (cardiac and respiratory traces) were recorded concurrently with fMRI scans, providing valuable information for physiological noise correction [@kasper2017physio].

## Imaging Modalities and Data Structure

The AOMIC collection includes three primary imaging modalities that together enable comprehensive characterization of brain anatomy, functional connectivity, and white-matter microstructure. T1-weighted structural MRI provides high-resolution images of gray matter anatomy, supporting voxel-based morphometry (VBM) and parcellation analyses. Resting-state functional MRI (rs-fMRI) captures low-frequency blood oxygen level-dependent (BOLD) fluctuations in the absence of explicit task demands, enabling the construction of [[functional-connectivity]] matrices that characterize intrinsic brain network organization. Diffusion MRI (dMRI), including DTI and advanced diffusion models, allows reconstruction of white-matter tracts through tractography, supporting analyses of [[structural-connectivity]] and structural network topology.

Each participant in AOMIC undergoes comprehensive phenotyping, including demographic information, cognitive assessments, and in many cases clinical screening. This rich phenotypic characterization includes measures of intelligence (via the Intelligence Structure Test for ID1000 and Raven's Progressive Matrices for PIOP datasets), personality (via the NEO-FFI big five inventory), and behavioral variables related to the specific task paradigms. The dataset has been particularly influential in studies examining the neural basis of individual differences in cognitive performance, the developmental trajectory of brain networks, and the effects of specific genetic variants on brain structure and function.

## Relationship to Whole-Brain Modeling and TVB

AOMIC serves as an important data source for [[whole-brain-modeling]] efforts that aim to simulate large-scale brain dynamics using [[neural-mass-models]] or [[spiking-neural-networks]]. Whole-brain models require empirical connectivity estimates—typically derived from diffusion MRI tractography—as structural priors, alongside neural mass model parameters characterizing the dynamics of individual brain regions. The multimodal nature of AOMIC makes it particularly suitable for constructing personalized brain models wherein individual connectivity patterns inform the structural architecture of the simulation.

In the context of [[tvb]] (The Virtual Brain), AOMIC has been used to generate subject-specific connectomes that serve as the structural basis for clinical simulations, such as those modeling [[epileptor]] or exploring the effects of [[brain-stimulation]]. The availability of both functional and structural connectivity data from the same participants enables validation of whole-brain model predictions against empirical functional connectivity, supporting model-fitting approaches that constrain free parameters using empirical data. This integration of empirical connectivity data with generative whole-brain models represents a key methodological advance in computational neuroscience, enabling in silico experiments that would otherwise be infeasible. The extensive phenotypic characterization included in AOMIC further enables investigations of how individual differences in brain structure and function relate to cognitive and personality measures, providing targets for model validation that extend beyond purely connectivity-based comparisons.

## Software Ecosystem

Processing and analyzing AOMIC data leverages the broader neuroimaging software ecosystem. Standard preprocessing pipelines such as [[fmriprep]] (for functional data) and [[freesurfer]] (for structural segmentation) are commonly applied, with fMRIPrep derivatives provided as part of the dataset itself. Connectivity analysis relies on tools including the [[brain-connectivity-toolbox]] (BCT), [[nilearn]], and [[mne-python]]. For diffusion MRI processing, [[mrtrix3]] and [[dipy]] provide tractography and advanced diffusion modeling capabilities. The [[bids]] format ensures seamless integration across these tools, facilitating reproducible workflows that can be shared and repeated across laboratories.

Data quality has been rigorously assessed using the MRIQC pipeline, with both automated quality metrics and manual visual inspection performed for all modalities. Quality control metrics are publicly available, allowing users to apply custom inclusion criteria based on their specific research questions.

## Conclusion

AOMIC represents a valuable contribution to the open neuroscience ecosystem, providing high-quality multimodal MRI data to support research in connectomics, whole-brain modeling, and computational psychiatry. Its standardized format, comprehensive phenotypic characterization, and integration with the broader BIDS-compliant software ecosystem make it an attractive resource for researchers developing or validating whole-brain models. As the field moves toward larger, more heterogeneous datasets and personalized medicine approaches, resources like AOMIC will continue to play an important role in advancing our understanding of human brain organization and dysfunction.

## Key Papers

- **Snoek, L., van der Miesen, M. M., Beemsterboer, T., Van Der Leij, A., Eigenhuis, A., & Scholte, H. S. (2021)**. *The Amsterdam Open MRI Collection, a set of multimodal MRI datasets for individual difference analyses*. Scientific Data, 8(1), 1-23. doi:10.1038/s41597-021-00870-6

## References

- Snoek, L., van der Miesen, M. M., Beemsterboer, T., Van Der Leij, A., Eigenhuis, A., & Scholte, H. S. (2021). The Amsterdam Open MRI Collection, a set of multimodal MRI datasets for individual difference analyses. *Scientific data*, 8(1), 1-23.
- Nichols, T. E., et al. (2017). Best practices in data analysis and sharing in neuroimaging using MRI. *Nature Neuroscience*, 20(3), 299-303.
- Van Essen, D. C., et al. (2013). The WU-Minn Human Connectome Project: an overview. *Neuroimage*, 80, 62-79.
- Miller, K. L., et al. (2016). Multimodal population brain imaging in the UK Biobank prospective epidemiological study. *Nature Neuroscience*, 19(11), 1523-1536.
- Gorgolewski, K. J., et al. (2016). The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. *Scientific Data*, 3, 160044.
- Esteban, O., et al. (2019). fMRIPrep: a robust preprocessing pipeline for functional MRI. *Nature Methods*, 16(1), 111-116.
- Tournier, J-D., et al. (2019). MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. *Neuroimage*, 202, 116137.
- Kasper, L., et al. (2017). The PhysIO Toolbox for Modeling Physiological Noise in fMRI Data. *Journal of Neuroscience Methods*, 276, 56-72.