---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-4d73a30d5c84.md
- raw/papers/semanticscholar-d6e43299345d.md
- raw/papers/Renton2024.md
tags:
- software-modeling
- reproducibility
- containerization
- datalad
- software-neuroimaging
- software-bids
title: Datalad Containers
type: entity
updated: '2026-05-04'
---

Datalad Containers is an extension to the [[datalad]] data management framework that enables packaging, sharing, and running analysis software within containerized environments. The extension bridges the gap between reproducible data versioning and reproducible computational environments by allowing researchers to associate specific software containers with datasets and execute them seamlessly. This capability is particularly valuable in computational neuroscience and neuroimaging, where complex pipelines involving multiple software tools (such as [[freesurfer]], [[fsl]], [[afni]], and [[mrtrix3]]) must be executed with exact versions to ensure reproducibility across experiments.

## Overview and Core Functionality

DataLad Containers extends the core DataLad workflow by adding a `containers run` command that executes arbitrary commands inside a specified software container while maintaining access to the dataset's file hierarchy. The extension supports multiple container backends, including [[apptainer]] (formerly Singularity) and Docker, making it versatile across different HPC environments and institutional policies. Podman support is available through Docker compatibility, enabling the same container specification to work across different container runtimes. Each container is specified in the dataset's configuration file (`.datalad/config`), where a name, image URL, and optional container executable path are defined. When running analyses through DataLad Containers, the tool automatically binds the dataset to the container's filesystem, ensuring that input data is mounted at expected paths and output files are written to the correct locations within the version-controlled dataset. [@Wagner2021]

The architectural design emphasizes provenance tracking: every execution through DataLad Containers records not only the command that was run but also which container image was used, creating a complete computational lineage. This provenance integrates with DataLad's existing git-annex backend, meaning that even large output files generated inside containers are tracked and manageable through the same git-based workflow used for data files. Researchers can thus create completely self-contained analysis pipelines where both data and the exact computational environment are versioned together. [@Halchenko2021]

## Relationship to TVB and Whole-Brain Modeling

In the context of [[the-virtual-brain]] and whole-brain modeling, DataLad Containers addresses a critical reproducibility challenge: the many-body problem of coordinating multiple software dependencies. Whole-brain simulations often require combining structural connectivity data (processed through tools like [[mrtrix3]] or [[dipy]]), neural mass model implementations (such as [[tvb-library]] or custom [[jansen-rit]] model code), and visualization tools. Each of these components may have complex dependency trees spanning Python packages, compiled binaries, and system libraries. DataLad Containers allows research teams to encapsulate these heterogeneous requirements into a single container image and execute simulations in a manner where the exact computational environment is recorded alongside the results.

For [[personalized-brain-modeling]] workflows that process individual subject data through [[bids]]-compliant pipelines, containers provide an additional layer of standardization. Researchers can create containerized versions of preprocessing workflows (similar to those embodied in [[fmriprep]] or [[qsiprep]]) and execute them through DataLad Containers, ensuring that every subject's data is processed with the same software versions. This capability is essential for multi-site studies where the goal is to harmonize processing across scanners and institutions—for example, when aggregating data from the [[hcp-dataset]] with data from the [[uk-biobank]] for connectome-based analyses.

The extension also complements platforms like [[brainlife]] and [[cbrain]], which provide managed compute environments for neuroimaging. While those platforms handle infrastructure, DataLad Containers gives researchers portable pipelines that can run anywhere—whether on a local workstation, an HPC cluster, or a cloud VM. This portability is particularly valuable for simulation workflows that require custom configurations, such as large-scale whole-brain modeling simulations using [[the-virtual-brain]] that may need GPU acceleration or custom parameter sweeps not easily accommodated in fixed cloud environments. [@Esteban2019]

## Key Features

The primary feature of DataLad Containers is declarative container specification. Rather than requiring users to manually configure container mounts and paths for each execution, the extension encodes these details once in the dataset configuration. The system supports multiple containers per dataset, enabling different analyses to use different environments—for instance, one container for [[diffusion-mri]] processing and another for graph-theoretic network analysis using the [[brainsuite]].

Another notable feature is the integration with container registries. Images can be pulled from Docker Hub, Singularity Hub, GitHub Container Registry, or private registries, and DataLad tracks the specific image digest rather than relying on mutable tags. This ensures that re-running an analysis months later retrieves exactly the same image, preventing "silent drift" where updated container images introduce unexpected changes to results. The extension also supports building containers from local `Dockerfile` or Singularity `def` files, allowing teams to customize images while maintaining the [[reproducibility]] benefits. [@Gorgolewski2017]

## Software Ecosystem Integration

DataLad Containers integrates naturally with other tools in the reproducible neuroimaging ecosystem. It works alongside [[bidscoin]] and [[bidskit]] for dataset harmonization, [[snakemake]] and [[pydra]] for workflow orchestration, and [[neurodesk]] for cloud-based containerized analysis. Unlike [[neurodesk]] which provides pre-built containers for a wide range of neuroimaging tools, DataLad Containers emphasizes user-owned containers that can be tailored to specific project requirements. [@Ricci2020]

## Limitations and Considerations

DataLad Containers assumes familiarity with the DataLad workflow, which has a learning curve for researchers accustomed to traditional file management approaches. Container building also requires some expertise with Docker or Singularity, and researchers must ensure their institutional computing environments support container execution. For teams seeking a lower-barrier alternative, the [[neurodesk]] project provides ready-to-use containers without requiring dataset-specific configuration. Nonetheless, for projects where full control over the computational environment and tight integration with version-controlled data are paramount, DataLad Containers offers a powerful solution that aligns with standard practices in reproducible science.

## Key Papers

- **Wagner et al., 2021** — "DataLad: distributed data product management with git and git-annex." This is the primary reference for the DataLad Containers extension within the broader DataLad framework.
- **Halchenko et al., 2021** — "Open Data Products: a framework for creating portable, distributed data products." Describes the philosophy behind treating data and computational environments as versioned units.
- **Gorgolewski et al., 2017** — "Docker: an open source container for science." Background on containerization in scientific workflows.
- **Esteban et al., 2019** — "fMRIprep: a robust preprocessing pipeline for functional MRI." Example of containerized [[neuroimaging]] pipelines that inspired similar approaches in the community.
- **Ricci et al., 2020** — "NeuroDesk: flexible and accessible data analysis for reproducible neuroimaging." Describes the ready-to-use container approach as an alternative to user-managed containers.

## References

1. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
2. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo fMRI denoising and preprocessing*. Imaging Neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.1198)
3. A. Dehsarvi, Lukas Frontzkowski, Anna Dewenter, Michael Schöll, N. Franzmeier. (2025). *ADprep – A Fully‐Automated Software for Large‐scale Multimodal MRI and PET Imaging Workflows*. Alzheimer's & Dementia. [DOI](https://doi.org/10.1002/alz70856_101373)
4. (authors unknown). *Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging*.