---
created: 2021-01-01
sources:
- '[Renton et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10055538/)'
- '[Neurodesk Official Website](https://neurodesk.org/)'
- '[Neurodesk GitHub Repository](https://github.com/NeuroDesk)'
- '[Brainhack Global 2021 Project](https://www.brainhack.org/global2021/project/project_74/)'
- raw/papers/Renton2024.md
tags:
- software-neurodesk
- reproducible-neuroimaging
- containerization
- neuroimaging-pipeline
- cloud-computing
- reproducible-research
title: Neurodesk
type: entity
updated: '2026-05-02'
---

## Overview

**Neurodesk** is a desktop-based, containerized neuroimaging analysis framework that provides a unified graphical interface for running diverse neuroimaging software tools in standardized, reproducible environments. Developed primarily at the University of Queensland's Queensland Brain Institute in Australia, Neurodesk addresses one of the most persistent challenges in computational neuroscience: the complexity of installing, configuring, and maintaining the dozens of software packages required for modern neuroimaging analysis pipelines. The platform wraps popular tools including [[fsl]], [[freesurfer]], [[afni]], [[ants]], [[mrtrix3]], [[dipy]], and many others within docker or singularity containers, presenting users with a simple desktop launcher that handles all dependency management behind the scenes. According to a 2023 paper by Renton and colleagues, Neurodesk's architecture was designed around four guiding principles: Accessibility, Portability, Reproducibility, and Flexibility.[^Renton2023]

## Motivation and Context

The field of neuroimaging has evolved dramatically over the past two decades, with researchers now needing to orchestrate complex pipelines that span multiple software ecosystems—from [[diffusion-imaging]] tractography using [[mrtrix]] or [[dsi-studio]], to [[fmri]] preprocessing with [[fmriprep]] or [[fsl]], to cortical reconstruction using [[freesurfer]] or [[brainsuite]]. Historically, installing and configuring these tools required extensive system administration expertise, as each package had unique library dependencies, version requirements, and configuration quirks that often conflicted with one another. This "dependency hell" created substantial barriers to reproducibility, as the same analysis code could produce different results on different laboratory computers depending on software versions and installation configurations. Research has shown that differences across computing environments can lead to meaningful differences in neuroimaging results due to variations in library versions and floating-point arithmetic implementations.[^Glatard2015]

Neurodesk emerged from the [[reproducibility]] movement in neuroscience to solve these problems through containerization. By packaging each tool in its own isolated environment with precisely specified library versions, Neurodesk ensures that analysis pipelines can be reproduced exactly across different computers and operating systems. The platform addresses the growing need for cloud-compatibility in neuroimaging, as [[neurovault]] and other data repositories increasingly encourage containerized analysis for published results.[^NationalAcademies2019] Unlike cloud-native solutions like [[brainlife]] or [[cbrain]], Neurodesk maintains a desktop-first philosophy that allows researchers to run containers locally without requiring constant cloud connectivity.

## Key Features

The architecture of Neurodesk centers on its **example-driven analysis** philosophy. Rather than requiring users to write complex configuration files or pipeline scripts from scratch, Neurodesk provides example notebooks for common analysis tasks that users can modify for their specific needs. These notebooks demonstrate complete pipelines for tasks such as [[structural-connectivity]] analysis from [[dwi-toolbox]] data, [[resting-state]] [[fmri]] preprocessing, and cortical thickness measurements. The platform leverages jupyter notebooks as the primary interface, allowing users to combine interactive exploration with batch processing in a familiar programming environment.[^NeurodeskOrg]

A distinguishing feature of Neurodesk is its **multi-tool integration** under a single launcher. Users can access tools from different software ecosystems within the same analysis pipeline without manually managing separate installations. For instance, a single notebook can combine [[fsl]] for registration, [[ants]] for diffeomorphic normalization, [[mrtrix3]] for tractography, and [[nilearn]] for connectivity analysis—all running in their respective containers. The platform leverages [[nipype]] in some example notebooks for workflow orchestration, though Neurodesk's core infrastructure (neurocommand/neurodeskapp) handles the container launching and management layer that provides the primary interface for tool execution.[^Renton2023]

Neurodesk supports both **local deployment** (using Docker Desktop on Linux, macOS, or Windows via WSL2) and **cloud deployment** (via Google Cloud Platform, AWS, or Kubernetes clusters). This flexibility allows users to develop pipelines locally on laptop computers and then scale up to high-performance computing resources for processing large [[hcp-dataset]] or [[uk-biobank]] cohorts without code modifications. The platform also includes built-in support for [[bids]] data organization, making it compatible with the dominant standard for neuroimaging datasets. Neurodesk containers are distributed globally via CernVM File System (CVMFS), providing low-latency access to users worldwide.[^Renton2023]

## Relationship to TVB

Neurodesk and [[the-virtual-brain]] (TVB) serve complementary but distinct roles in the computational neuroscience ecosystem. While Neurodesk focuses on preprocessing and extracting features from empirical neuroimaging data (segmentation, registration, tractography, time-series extraction), TVB specializes in constructing and simulating [[whole-brain-modeling]] frameworks that generate dynamics from [[structural-connectivity]] matrices. The two platforms can be integrated in a typical analysis workflow: Neurodesk processes raw [[dti]] or [[fmri]] data to produce [[connectivity]] matrices (either [[structural-connectivity]] from tractography or [[functional-connectivity]] from correlation), which are then exported to TVB for [[neural-mass-model]] simulations and dynamical systems analysis.

This integration pathway reflect a broader trend in which specialized tools are chained together through standardized data formats—Neurodesk outputs [[connectome]] data in formats readable by TVB, including [[gift]] files and connectivity matrices. Researchers studying [[epilepsy-modeling]], [[alzheimers-modeling]], or [[brain-stimulation]] can thus use Neurodesk for empirical data preparation and TVB for mechanistic modeling, combining the strengths of data‑driven and theory‑driven approaches to brain dynamics research.

## Key Papers

- **Renton, A.I.**, Dao, T.T., Johnstone, T., Civier, O., Sullivan, R.P., White, D.J., Lyons, P., Slade, B.M., Abbott, D.F., Amos, T.J., Bollmann, S., Botting, A., Campbell, M.E.J., Chang, J., Close, T.G., Eckstein, K., Egan, G.F., Evas, S., Flandin, G., Garner, K.G., Garrido, M.I., Ghosh, S.S., Grignard, M., Hannan, A.J., Huber, R., Kaczmarzyk, J.R., Kasper, L., Kuhlmann, L., Lou, K., Mantilla‑Ramos, Y.J., Mattingley, J.B., Morris, J., Narayanan, A., Pestilli, F., Puce, A., Ribeiro, F.L., Rogasch, N.C., Rorden, C., Schira, M., Shaw, T.B., Sowman, P.F., Spitz, G., Stewart, A., Ye, X., Zhu, J.D., Hughes, M.E., Narayanan, A., & **Bollmann, S.** (2023). Neurodesk: An accessible, flexible, and portable data analysis environment for reproducible [[neuroimaging]]. *medRxiv*. [^Renton2023]

## Related Software

Neurodesk intersects with several other software ecosystems in the neuroimaging landscape. Containerized alternatives include [[apptainer]] (formerly Singularity) for HPC environments and [[datalad-containers]] for data‑aware pipeline execution. Pure preprocessing pipelines like [[fmriprep]] and [[qsiprep]] provide automated versions of specific analysis steps that Neurodesk users may invoke through the platform. For cloud‑native pipeline orchestration, [[brainlife]] offers a complementary hosted solution, while [[cbrain]] provides HPC‑focused batch processing with a web interface. The underlying pipeline framework draws on [[nipype]] for workflow examples and leverages [[bids]] for data standardization across all tools.

## References

[^Renton2023]: Renton, A.I., Dao, T.T., Johnstone, T., Civier, O., Sullivan, R.P., White, D.J., Lyons, P., Slade, B.M., Abbott, D.F., Amos, T.J., Bollmann, S., Botting, A., Campbell, M.E.J., Chang, J., Close, T.G., Eckstein, K., Egan, G.F., Evas, S., Flandin, G., Garner, K.G., Garrido, M.I., Ghosh, S.S., Grignard, M., Hannan, A.J., Huber, R., Kaczmarzyk, J.R., Kasper, L., Kuhlmann, L., Lou, K., Mantilla‑Ramos, Y.J., Mattingley, J.B., Morris, J., Narayanan, A., Pestilli, F., Puce, A., Ribeiro, F.L., Rogasch, N.C., Rorden, C., Schira, M., Shaw, T.B., Sowman, P.F., Spitz, G., Stewart, A., Ye, X., Zhu, J.D., Hughes, M.E., Narayanan, A., & Bollmann, S. (2023). Neurodesk: An accessible, flexible, and portable data analysis environment for reproducible neuroimaging. *medRxiv*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10055538/

[^Glatard2015]: Glatard, T., Berghi, L.B., Jha, D., & Bergman, L. (2015). Reproducibility of neuroimaging analyses across operating systems. *Frontiers in Neuroinformatics*, 9, 12. https://doi.org/10.3389/fninf.2015.00012

[^NationalAcademies2019]: National Academies of Sciences, Engineering, and Medicine. (2019). *Reproducibility and Replicability in Science*. Washington, DC: The National Academies Press. https://doi.org/10.17226/25303

[^NeurodeskOrg]: Neurodesk Documentation. (2024). https://neurodesk.org/overview