---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-a324c47ea982.md
- raw/papers/semanticscholar-f45e6044c92f.md
tags:
- software-brian
- software-modeling
- software-tvb
- database-hcp
- database-uk-biobank
- brain-atlas
- compute-infrastructure
- european-infrastructure
- research-infrastructure
title: EBRAINS
type: entity
updated: '2026-04-30'
---

# EBRAINS

## Overview

EBRAINS (European Brain Research Infrastructure) is a distributed research infrastructure established under the European Union's ESFRI (European Strategy Forum on Research Infrastructures) roadmap to advance understanding of the human brain in health and disease[^esfri]. Placed on the ESFRI roadmap in 2018 and formally operationalized as a legal entity in 2021, EBRAINS serves as a pan-European platform that integrates [[neuroimaging]] data, brain atlases, computational modeling tools, and high-performance computing resources into a unified ecosystem for brain research[^about]. The infrastructure emerged from the Human Brain Project's legacy, transforming its research outcomes into a sustainable, community-accessible platform that supports the entire research pipeline from data acquisition to simulation and validation[^hbp]. EBRAINS operates as a member-based organization with nodes distributed across multiple European countries, each contributing specialized expertise in imaging, modeling, or data curation.

## Motivation and Scientific Context

The creation of EBRAINS addresses a fundamental challenge in modern neuroscience: the need to synthesize vast quantities of heterogeneous data—ranging from molecular-level experiments to whole-brain neuroimaging—into coherent computational models that can explain brain function and dysfunction. Prior to EBRAINS, researchers faced significant barriers in accessing standardized datasets, lacked interoperable software frameworks, and had limited opportunities for reproducible computational experiments. The infrastructure was conceived to lower these barriers by providing curated access to large-scale datasets such as the [[human-connectome-project]] (HCP)[^hcp], alongside a growing collection of atlases including the [[julich-atlas]] and [[brainnetome-atlas]]. Beyond data access, EBRAINS enables researchers to run computationally intensive simulations using frameworks like [[the-virtual-brain]] (TVB), [[nest]], and [[brian2]] directly on distributed computing resources, eliminating the need for individual labs to maintain expensive high-performance computing clusters.

## Key Features

**Data Services and Curation:** EBRAINS provides a Data Registry that indexes brain-related datasets with standardized metadata following frameworks like [[bids]] (Brain Imaging Data Structure), enabling researchers to discover and download datasets relevant to their questions. The platform hosts multiple atlases with annotation capabilities, supporting both [[parcellation]]-based and voxel-wise analyses. Quality control tools like [[mriqc]] are integrated to assess dataset quality before downstream analysis.

**Compute Platform:** The Infrastructure offers a Compute Cloud providing Jupyter-based interactive computing environments with pre-installed neuroscience software packages. Users can launch workflows that process neuroimaging data using tools like [[freesurfer]], [[fsl]], and [[afni]], or run large-scale brain simulations on distributed clusters. The platform supports containerized workflows ensuring computational reproducibility.

**Brain Simulation Capabilities:** EBRAINS includes dedicated support for whole-brain modeling through integration with [[the-virtual-brain]], enabling researchers to construct personalized brain models using empirical [[structural-connectivity]] data from [[diffusion-imaging]] and [[tractography]]. The platform also supports neural mass models, mean-field approximations, and detailed spiking neural network simulations through integration with various simulator-specific interfaces.

**Knowledge Graph and Atlas Services:** The infrastructure maintains a Brain Atlas service with hierarchical organization of brain regions, enabling cross-species comparisons and linking genomic, cellular, and systems-level information. The EBRAINS Knowledge Graph provides semantic integration of brain data, allowing queries across experimental modalities.

## Relationship to TVB

EBRAINS maintains a particularly close relationship with [[the-virtual-brain]] (TVB), one of the flagship whole-brain simulation platforms in the field. TVB is natively supported within the EBRAINS compute ecosystem, allowing users to configure and run personalized brain simulations without local software installation. The integration enables TVB workflows to leverage EBRAINS-hosted datasets including structural [[connectome]] data derived from HCP cohorts[^hcp]. Personalization pipelines within TVB can utilize EBRAINS compute resources to estimate model parameters fitting empirical [[functional-connectivity]] patterns, supporting applications in [[epilepsy-modeling]], [[personalized-brain-modeling]], and clinical translation research. This synergy exemplifies EBRAINS's role as an enabling infrastructure for sophisticated computational neuroscience workflows that would otherwise require substantial technical setup.

## Technical Architecture

The EBRAINS architecture comprises several interconnected layers: a data layer hosting curated datasets and atlases; a compute layer providing scalable processing and simulation capabilities; a tools layer offering integrated software packages for analysis, visualization, and modeling; and a services layer exposing programmatic APIs for automated workflows. The infrastructure follows open-science principles, with much of its software stack available as open-source and datasets released under permissive licenses. Interoperability with other major brain initiatives—including the US brain initiative ecosystem and international partners—is maintained through adoption of community standards like [[neuroml]] for model specification and NWB ([[neurodata-without-borders]]) for data formats.

## Related Software and Platforms

EBRAINS integrates with numerous software tools in the computational neuroscience ecosystem. For neuroimaging analysis, the platform supports [[nilearn]] and [[nipype]] for pipeline construction, along with [[mne-python]] for electrophysiology data processing. Simulation platforms including [[neuron]], [[arbor]], and [[carlsim]] are available for detailed neural modeling. Visualization tools like [[brainnet-viewer]] and [[connectome-workbench]] enable exploration of connectomic datasets. The infrastructure also provides access to databases including [[neuromorpho]] for morphological data and [[modeldb]] for computational models.

## External Relationships

As a European research infrastructure, EBRAINS collaborates with numerous institutional partners including national brain initiatives, university medical centers, and [[computational-neuroscience]] laboratories across the continent. The infrastructure maintains relationships with major international brain projects and contributes to international standardization efforts in neuroimaging and computational neuroscience. These partnerships enable data sharing agreements and coordinated research campaigns addressing fundamental questions in brain science.

## Related Concepts

The infrastructure connects to several foundational concepts in modern neuroscience. [[Whole-brain-modeling]] represents a primary use case, where researchers construct computational models of entire brain regions based on empirical connectivity data. [[Connectomics]] provides the structural foundation for many EBRAINS-hosted analyses, particularly studies examining [[structural-connectivity]] and its relationship to [[functional-connectivity]]. The platform supports research in [[dynamic-causal-modeling]] frameworks and enables parameter estimation workflows that fit computational models to empirical neuroimaging data. Applications in [[computational-psychiatry]] leverage EBRAINS resources to investigate biomarkers of brain disorders, while [[brain-stimulation]] researchers use the platform for simulation-based targeting of interventional protocols.

## Key Papers

*The following represents foundational publications related to EBRAINS and its integrated tools. A comprehensive bibliography is maintained on the EBRAINS website.*

- Sanz-Leon, P., et al. (2015). "The virtual brain: a simulator of primate brain [[network-dynamics]]." *NeuroImage*, 111, 385-407.[^tvbp]

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2025). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research*. bioRxiv. [DOI](https://doi.org/10.1101/2025.10.06.680781)
3. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2026). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research.*. Brain Stimulation. [DOI](https://doi.org/10.1016/j.brs.2025.103016)