---
title: Neurodesk
created: 2024-01-15
updated: 2026-05-01
type: entity
tags: [software-neurodesk, reproducibility, neuroimaging, containerization, software-visualization]
sources:
  - "[Renton et al., 2024. Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging. Nature Methods. doi:10.1038/s41592-023-02145-x](https://doi.org/10.1038/s41592-023-02145-x)"
  - "[Kurtzer et al., 2017. Singularity: Scientific containers for mobility of compute. PLoS ONE. doi:10.1371/journal.pone.0177459](https://doi.org/10.1371/journal.pone.0177459)"
  - "[Renton et al., 2023. Neurodesk: An accessible, flexible, and portable data analysis environment for reproducible neuroimaging. PREPRINT. doi:10.21203/rs.3.rs-2649734/v1](https://doi.org/10.21203/rs.3.rs-2649734/v1)"
---

# Neurodesk

## Overview

Neurodesk is a **containerized neuroimaging analysis platform** that provides standardized, ready-to-use environments for a wide spectrum of neuroimaging processing tools. Developed as a collaborative effort between multiple neuroimaging laboratories (primarily from Australia and Europe), Neurodesk addresses one of the most persistent challenges in the field: the difficulty of installing, configuring, and reproducing complex neuroimaging software stacks. The platform bundles over 100 commonly used neuroimaging tools—including packages for preprocessing (e.g., [[fsl]], [[freesurfer]]), segmentation (e.g., [[ants]], [[cat12]]), and visualization (e.g., [[fsleyes]])—into pre-built, versioned containers that can be run on local workstations, high-performance computing clusters, or cloud environments. This approach eliminates the "dependency hell" that traditionally plagues neuroimaging pipelines and ensures that results can be reproduced across different computational environments.

## Key Features

Neurodesk's architecture centers on **Apptainer (formerly Singularity) containers**, which are chosen specifically because they can be run without root privileges and integrate seamlessly with existing HPC infrastructure. Each tool in the Neurodesk ecosystem is packaged with all its dependencies, ensuring version compatibility and **eliminating conflicts** between different software versions that might coexist on a single system. The platform provides a unified **Jupyter-based interface** that allows users to launch notebooks with pre-configured environments, making it straightforward to combine multiple tools in a single analysis pipeline. Users can browse available tools through the Neurodesk web interface, which provides documentation, version information, and one-click launch capabilities for containers.

A distinguishing feature of Neurodesk is its commitment to **FAIR principles** (Findable, Accessible, Interoperable, Reusable). By containerizing tools with pinned versions, Neurodesk makes it significantly easier to share analysis pipelines and ensure that collaborators or reviewers can exactly replicate the computational environment used to generate published results. The platform also includes **neurodocker** recipes, allowing advanced users to customize containers or build new ones based on Neurodesk templates. Integration with [[datalad]] and [[bids]]-compliant data management workflows enables end-to-end reproducibility from raw data to final statistical results.

## Relationship to TVB

While Neurodesk and [[the-virtual-brain]] (TVB) serve different primary purposes, they are complementary tools in the whole-brain modeling ecosystem. Neurodesk focuses on **neuroimaging preprocessing and analysis**—offering tools for structural [[diffusion-imaging]], [[tractography]], gray matter segmentation, and cortical reconstruction that are essential for generating the anatomical connectomes required as input to whole-brain models. TVB, in contrast, provides a simulation framework for building and running large-scale brain network models using these anatomical connectomes as structural constraints.

In practical workflows, Neurodesk is typically used in the **upstream data processing phase**: a researcher might use Neurodesk containers to preprocess [[dti]] scans, perform tractography using tools like [[mrtrix3]] or [[camino]], generate structural connectivity matrices, and then export these connectomes in TVB-compatible formats (e.g., [[connectome-workbench]] CIFT files or simple CSV matrices). The combination of Neurodesk's reproducible preprocessing pipeline with TVB's simulation capabilities exemplifies modern **personalized brain modeling** workflows, where individual subject anatomical data is used to constrain whole-brain simulations. Several TVB tutorials explicitly reference Neurodesk-style preprocessing steps for preparing individual connectomes.

## Technical Implementation

Neurodesk containers are built using **Apptainer definition files** that specify the base operating system, package manager dependencies, and the specific neuroimaging tools to be installed. The build process pulls from upstream software repositories (e.g., GitHub releases, institutional archives) and pins exact versions to ensure reproducibility. Containers are hosted on Docker Hub and can be pulled directly to any system with Apptainer installed or accessed through cloud instances provided by Neurodesk (offering free computational resources for limited use cases).

The platform maintains **multiple tool versions** simultaneously, allowing users to select older versions for backward compatibility with published pipelines or newer versions for access to latest features. Each tool's entry in the Neurodesk catalog includes metadata such as the original publication citation, official documentation links, and common use cases. This metadata approach draws from the [[bids]] philosophy of standardized organization, enhancing discoverability and facilitating best-practice adoption. The build system uses continuous integration to automatically rebuild containers when upstream dependencies change, ensuring that the neuroimaging ecosystem remains up-to-date without breaking existing pipelines.

## Key Papers

Neurodesk was formally introduced in Renton et al. (2024), published in Nature Methods, describing the architecture and motivation for container-based neuroimaging toolkits. The authors demonstrated that Neurodesk eliminates inter-system variability in neuroimaging analysis pipelines—a critical finding given that prior work showed differences in software dependencies across computing environments could produce materially different results in fMRI processing pipelines. The platform has since been adopted by numerous labs conducting [[resting-state]] fMRI analyses, [[diffusion-mri]] studies, and multi-modal imaging investigations.

An earlier preprint version of the paper (Renton et al., 2023) provided additional methodological details on the reproducibility case study, directly comparing Neurodesk containers against locally installed software across different operating systems.

The underlying container technology, **Apptainer (formerly Singularity)**, was introduced by Kurtzer, Sochat, and Bauer (2017) in PLOS ONE, providing the security model and HPC compatibility that makes Neurodesk feasible on shared research computing infrastructure.

## Related Software

Neurodesk should be compared with several related platforms that address neuroimaging software accessibility. **neurodocker** (which Neurodesk uses internally) provides recipe generation for building custom containers. **CBRAIN** offers a web-based platform for distributed neuroimaging computation, with a different emphasis on cloud-based processing. **XNAT** provides a data management system with embedded processing capabilities, targeting institutional data management rather than tool accessibility. **Brainlife** offers a cloud-native platform similar in spirit to Neurodesk but with a more opinionated workflow system. For the specific use case of whole-brain modeling, Neurodesk's utility lies in its tool diversity—it provides nearly all major packages needed for generating structural and functional connectivity inputs to frameworks like TVB, [[psycneulink]], or [[nest]]-based simulations.

[[apptainer]] | [[bids]] | [[datalad]] | [[freesurfer]] | [[fsl]] | [[nilearn]] | [[reproducibility]] | [[the-virtual-brain]] | [[tractography]] | [[diffusion-imaging]]

## References

- Renton, A. I., Dao, T. T., Johnstone, T., Civier, O., Sullivan, R. P., White, D. J., ... & Bollmann, S. (2024). Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging. *Nature Methods*, 21(5), 804-808. https://doi.org/10.1038/s41592-023-02145-x
- Kurtzer, G. M., Sochat, V., & Bauer, M. W. (2017). Singularity: Scientific containers for mobility of compute. *PLoS ONE*, 12(5), e0177459. https://doi.org/10.1371/journal.pone.0177459
- Renton, A. I., Dao, T. T., Johnstone, T., Civier, O., Sullivan, R. P., White, D. J., ... & Bollmann, S. (2023). Neurodesk: An accessible, flexible, and portable data analysis environment for reproducible neuroimaging. *Research Square*. https://doi.org/10.21203/rs.3.rs-2649734/v1