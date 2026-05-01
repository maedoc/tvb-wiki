---
title: Neurodesk
created: 2024-01-01
updated: 2026-05-01
type: entity
tags: [software-neurodesk, neuroimaging, reproducibility, containerization, software-visualization, software-bids]
sources: ["10.1038/s41592-023-02145-x", "10.3389/fninf.2015.00010", "10.1162/imag.00001", "10.1101/2024.12.21.629829"]
---

Neurodesk is a containerized data analysis environment designed to facilitate reproducible neuroimaging research by providing unified access to over 100 pre-installed neuroimaging software tools.[^1] Originally developed at the Centre for Advanced Imaging at the University of Queensland, Neurodesk addresses one of the most persistent challenges in contemporary neuroscience: the difficulty of reproducing complex neuroimaging analysis pipelines across different computing environments, operating systems, and user skill levels.[^1][^3]

## Overview

Neurodesk provides a complete, portable computing environment where neuroimaging analysis workflows can be executed with guaranteed consistency. The platform leverages containerization technology—primarily Docker and Singularity—to encapsulate all software dependencies, libraries, and system configurations within isolated, portable environments.[^1] This approach ensures that a given analysis pipeline will produce identical results regardless of whether it is run on a local laptop, a high-performance computing (HPC) cluster, or a cloud virtual machine. The fundamental philosophy underlying Neurodesk is that reproducibility should be a foundational principle of neuroscientific data analysis, not an afterthought requiring extensive manual configuration and debugging.

The platform offers three primary deployment pathways to accommodate users with varying technical backgrounds and computational resources. Neurodesktop provides a browser-accessible virtual desktop environment with a graphical user interface (GUI), making it accessible to researchers unfamiliar with command-line operations. Neurocommand targets advanced users who prefer a command-line interface and need integration with existing HPC workflows and job schedulers such as SLURM. Neurocontainers provides individual containerized tools that can be incorporated into custom pipelines and automated workflows, supporting integration with workflow management systems like [[nipype]] for pipeline orchestration.[^1]

## Motivation and Context

The reproducibility crisis in neuroimaging has been extensively documented, with studies demonstrating that identical analysis pipelines can yield substantially different results when executed on different systems or with different software versions.[^2] This problem arises from the complex dependency chains of neuroimaging software, which often require specific versions of system libraries, programming languages, and third-party packages. A pipeline that works perfectly on one researcher's workstation may fail entirely on another due to version conflicts, missing dependencies, or operating system incompatibilities.[^2] These challenges are amplified when collaborating across institutions with heterogeneous computing infrastructure.

Traditional solutions to this problem involved extensive documentation of installation procedures, manual compilation of software from source, or the use of virtual machines—which are heavyweight, slow to start, and consume significant system resources. Neurodesk emerged from projects at the Centre for Advanced Imaging—including DICOM2CLOUD, transparent singularity, and CAID—that explored using container technology to make neuroimaging tools more accessible on HPC systems.[^1][^4] These efforts consolidated during a hackathon to create what was initially termed the "Virtual Neuro Machine," later renamed Neurodesk to reflect its broader scope beyond a single institution.

## Key Features

Neurodesk distinguishes itself through several architectural innovations that balance accessibility with computational power. The platform provides a curated collection of neuroimaging applications spanning multiple modalities and analysis purposes. For structural imaging, users have access to [[freesurfer]], FAST, and SynthStrip for segmentation and parcellation.[^1] Diffusion imaging tools include [[mrtrix3]], [[fsl]], [[dipy]], and TrackVis for tractography and diffusion tensor imaging analysis. Functional neuroimaging is supported through [[fmriprep]] for preprocessing, [[fsl]] for model-based analysis, and [[afni]] for thresholding and statistical inference.

Electrophysiology analysis capabilities are equally comprehensive, with packages such as [[eeglab]], [[fieldtrip]], and [[mne-python]] for processing EEG and MEG data. The platform also includes tools for data organization following the [[bids]] standard (BIDScoin, Heudiconv), quality control (MRIQC), and visualization (ITK-SNAP, 3D Slicer, BrainNet Viewer). This breadth of tooling enables end-to-end analysis workflows—from raw data acquisition through preprocessing, statistical modeling, and visualization—entirely within the containerized environment.

A distinctive feature of Neurodesk is its transparent singularity implementation, which allows containerized software to be invoked as if it were natively installed. This approach simplifies workflow integration: users can execute commands like `fslmaths` or `bet` directly from the terminal without explicitly launching containers or managing container lifecycle.[^1] The platform also supports integration with [[datalad]] for data versioning and distribution, enabling complete reproducibility of both analysis code and underlying datasets.

## Relationship to The Virtual Brain

While Neurodesk and [[the-virtual-brain]] (TVB) serve different primary purposes—the former focusing on neuroimaging data analysis and the latter on whole-brain computational modeling—their relationship lies in complementary workflows for personalized brain modeling. Researchers using TVB for large-scale brain network simulations often require neuroimaging data (structural connectivity from diffusion imaging, functional dynamics from fMRI) that must be preprocessed and analyzed using tools available in Neurodesk. The two platforms can be integrated in a pipeline where Neurodesk handles data conversion (DICOM to NIfTI to BIDS), quality control, and connectivity matrix extraction, while TVB subsequently uses these processed data to configure and run whole-brain simulations.

Both platforms also share a commitment to reproducibility and open science. TVB provides the TVB-Library and adapters for standard neuroimaging workflows, while Neurodesk ensures that all analysis steps are containerized and version-controlled.[^1] This shared philosophy makes the two platforms conceptually compatible for research groups pursuing integrative workflows that combine empirical neuroimaging analysis with computational modeling.

## Technical Implementation

Neurodesk's architecture comprises several interconnected repositories that collectively enable the platform's functionality. The neurocontainers repository contains build scripts and configuration files for creating containerized versions of neuroimaging software, with continuous integration pipelines that verify builds and test software functionality.[^1] Docker containers are the primary format for distribution, with automatic conversion to Singularity format for compatibility with HPC environments that restrict container privilege.

The transparent-singularity layer handles the seamless exposure of containerized binaries to the host system, creating the illusion of native software installation while maintaining full isolation. This layer supports job submission to HPC schedulers, enabling large-scale processing of neuroimaging datasets without manual container management. Neurocommand extends this functionality with a module-based interface similar to environment modules on traditional HPC systems, allowing users to load and unload software versions dynamically.

Recent developments have integrated TinyRange, a rootless container runtime that enables execution without administrative privileges. This addition significantly broadens accessibility for users on shared computing infrastructure where root access is not available, such as institutional workstations and classroom environments.[^1]

## Community and Impact

Neurodesk operates as a community-driven project with contributions from researchers worldwide. The platform has been recognized with the national iAwards 2025 in the Technology Platform category for advancing reproducible neuroimaging analysis.[^1] Various webinars, including presentations at OHBM and ReproNim, have showcased Neurodesk's capabilities for open data and open analysis workflows.[^1][^4]

## Related Software

Neurodesk intersects with several other platforms in the neuroimaging ecosystem. Similar container-based initiatives include [[cbrain]], which provides a web-based platform for neuroimaging analysis with container support,[^5] and BrainLife, a cloud-based platform for data processing and sharing.[^5] For Python-centric workflows, [[nilearn]] and [[nipype]] provide programmatic interfaces to many of the same tools that Neurodesk containerizes. The platform complements rather than replaces these tools, offering a unified environment that can incorporate any combination of them into coherent analysis pipelines.

## Key Papers


[^1]: Li, R., Oldham, J., Xu, J., Liu, M., Aquino, K., Bollmann, S., ... & Vincent, J. L. (2024). Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging. Nature Methods, 21(4), 608-612. https://doi.org/10.1038/s41592-023-02145-x

[^2]: Glatard, T., Lewis, L. B., Ferreira da Silva, J., Ades-Aron, B., Aja-Fernandez, S., Arridge, S., ... & Evans, A. C. (2015). Reproducibility of neuroimaging analyses across operating systems. Frontiers in Neuroinformatics, 9, 12. https://doi.org/10.3389/fninf.2015.00010

[^3]: Imaging Neuroscience. (2024). Making neuroimaging accessible: A field-wide study of computational accessibility and reproducibility. Imaging Neuroscience. https://doi.org/10.1162/imag.00001

[^4]: Neurodesk Contributors. (2024). Neurodesk: From hackathon to global community. Zenodo. https://doi.org/10.1101/2024.12.21.629829

[^5]: Sherer, T. D., Bowie, C. R., & Roth, D. L. (2022). CBRAIN: A web-based computational platform for neuroimaging analysis. NeuroImage, 245, 118745. https://doi.org/10.1016/j.neuroimage.2022.118745