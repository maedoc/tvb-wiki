---
title: CBRAIN
created: 2025-01-15
updated: 2026-04-29
type: entity
tags: [software-neuroimaging, neuroimaging, data-processing, workflow-automation, high-performance-computing, reproducibility, bids]
sources:
  - Sherif et al., 2014 - CBRAIN: a web-based, distributed computing platform for collaborative neuroimaging research
  - Glatard et al., 2014 - Interoperability between the CBRAIN and VIP web platforms
  - CBRAIN GitHub Wiki - Generic CBRAIN Documentation
---

# CBRAIN

## Overview

CBRAIN is a web-based computational platform designed for large-scale neuroimaging data processing, analysis, and management. Developed at the McGill Centre for Integrative Neuroscience (MCIN) at the Montreal Neurological Institute, McGill University, under the direction of Professor Alan C. Evans—with significant contributions from lead developers Pierre Rioux, Tarek Sherif, Tristan Glatard, Natacha Beck, Nicolas Kassis, and the CBRAIN team—CBRAIN provides a unified graphical interface that allows researchers to run neuroimaging pipelines on remote high-performance computing (HPC) clusters without requiring direct command-line access. The platform serves as a middleman between users and compute resources, enabling the execution of complex neuroimaging workflows—such as those built on [[freesurfer]], [[fsl]], [[spm]], and [[afni]]—through a user-friendly web browser while handling data transfer, job scheduling, and result aggregation automatically [[Sherif et al., 2014]].

## Motivation and Context

The neuroimaging community faces a fundamental infrastructure challenge: modern analysis pipelines require substantial computational resources (hundreds to thousands of CPU hours per subject) that are impractical to run on individual workstations. Simultaneously, many neuroscientists lack the technical expertise to interact directly with HPC systems via command-line interfaces. Traditional solutions like sending data to a central facility for processing created bottlenecks, while manual cluster management consumed significant research time and introduced variability that compromised reproducibility.

CBRAIN emerged to address these challenges by providing a layer of abstraction over heterogeneous computing infrastructure. The platform implements a federated model where multiple institutions can contribute compute resources (clusters, cloud instances) while retaining local control, and users can access these resources through a unified portal. This architecture proved particularly valuable for large consortia projects like the [[human-connectome-project]] (HCP) and [[enigma]], where thousands of subjects required standardized processing across multiple sites [[Sherif et al., 2014]].

## Key Features

### Web-Based Interface

CBRAIN exposes a graphical web interface that allows users to upload neuroimaging datasets (typically in [[bids]] or legacy formats), configure processing parameters, launch jobs, and download results. The interface abstracts the underlying Unix environment, making neuroimaging analysis accessible to clinical researchers and cognitive neuroscientists who might otherwise find HPC access prohibitive.

### Multi-Site Compute Federation

One of CBRAIN's distinctive features is its support for distributed computing resources. Institutions can register their own HPC clusters as CBRAIN compute targets, allowing jobs to run on local infrastructure while the web interface remains centralized. This federated model has been particularly adopted in Canada (through the CBRAIN/HCPTalk initiative) and increasingly in international collaborations. As of recent reporting, CBRAIN connects to six Compute Canada HPC clusters plus international resources, totaling over 80,000 CPU cores [[CBRAIN GitHub Wiki]].

### Tool Integration

CBRAIN bundles and maintains wrappers for dozens of leading neuroimaging tools, including:

- **Structural processing**: [[freesurfer]], [[fsl]]'s BET/FAST, [[ants]]
- **Diffusion imaging**: [[mrtrix3]], [[dipy]], [[fsl]]'s FDT, [[camino]]
- **Functional processing**: [[fsl]]'s FEAT, [[spm]], [[afni]]
- **Connectivity analysis**: [[connectome-workbench]], [[bctpy]]

Each tool wrapper ensures consistent input/output handling and proper integration with CBRAIN's data management system.

### Data Provenance and Reproducibility

Every processing step in CBRAIN is logged with full provenance information, including the exact software version, parameters used, and computational environment. This infrastructure supports rigorous reproducibility by making it possible to exactly replicate any analysis pipeline. Combined with [[bids]] data organization, CBRAIN workflows can be shared and reproduced across sites with minimal effort.

### Batch Processing and Workflow Automation

CBRAIN excels at launching massive batch analyses across hundreds of subjects. Users can configure parameter sweeps, apply processing chains to entire cohort directories, and monitor progress in real-time. For more complex workflows, CBRAIN supports integration with workflow managers like [[snakemake]] and can execute pipelines defined in [[nipype]].

## Relationship to TVB and Whole-Brain Modeling

While CBRAIN is primarily focused on neuroimaging preprocessing rather than biophysical simulation, it plays an increasingly important role in whole-brain modeling workflows. The platform processes [[structural-connectivity]] data derived from [[diffusion-imaging]] and [[tractography]]—essential inputs for connectome-based models in [[the-virtual-brain]] and other [[whole-brain-simulators]]. CBRAIN can generate parcellated connectivity matrices from raw DWI data, producing the structural scaffolds that constrain [[neural-mass-model]] simulations. Additionally, CBRAIN's preprocessing pipelines produce preprocessed [[fmri]] time series used in functional connectivity analyses that inform model parameterization. Researchers building personalized brain models increasingly rely on CBRAIN to handle the data preparation pipeline before feeding processed data into [[tvb]] or similar simulators.

## Related Software

CBRAIN occupies a distinct niche in the neuroimaging software ecosystem, but several related platforms serve overlapping needs:

- **[[LORIS]]**: Also developed at McGill, LORIS focuses more on data hosting and query capabilities for longitudinal studies, while CBRAIN emphasizes processing workflows
- **[[brainlife]]**: A more recent platform offering similar web-based processing with a stronger emphasis on community pipelines and data sharing
- **[[nipype]]**: A Python workflow library that underlies much of CBRAIN's internal processing logic; users seeking programmatic control may prefer direct nipype usage
- **[[bidscoin]]**: A tool for converting raw data to [[bids]] format, often used upstream of CBRAIN workflows

## Technical Architecture

At its core, CBRAIN consists of three interconnected components: a Ruby-on-Rails web application (the user-facing portal), a database for job and data metadata, and a set of "BrainPlugins" that wrap individual software tools. The system uses SSH tunneling to communicate with remote compute servers, submitting jobs through scheduler APIs (SLURM, PBS, SGE) and managing data transfer via dedicated storage systems. Data remains stored at the user's home institution, with CBRAIN only orchestrating the processing—this federated data model addresses many institutional data governance concerns that would otherwise preclude centralized cloud solutions [[Sherif et al., 2014]].

## Open Questions and Limitations

Despite its widespread adoption, CBRAIN faces ongoing challenges. The tool wrapper system requires manual maintenance as software packages evolve, and some legacy wrappers lag behind current version releases. Additionally, the platform's learning curve—while lower than direct HPC usage—remains nontrivial for new users. Some researchers have reported difficulties debugging failed jobs when error messages are abstracted. Future development directions include tighter integration with container technologies like [[apptainer]] for more consistent software environments, and expanded support for real-time processing pipelines needed in clinical applications.

## Key Papers

- Sherif T, Rioux P, Rousseau M-E, Kassis N, Beck N, Adalat R, Das S, Glatard T and Evans AC (2014). CBRAIN: a web-based, distributed computing platform for collaborative neuroimaging research. *Frontiers in Neuroinformatics* 8:54. https://doi.org/10.3389/fninf.2014.00054
- Glatard T, Rousseau M-E, Camarasu-Pop S, Rioux P, Sherif T, Beck N, Adalat R and Evans AC (2014). Interoperability between the CBRAIN and VIP web platforms for neuroimage analysis. *Frontiers in Neuroinformatics*, Conference Abstract: Neuroinformatics 2014. https://doi.org/10.3389/conf.fninf.2014.18.00070

## References

- Sherif, T., Rioux, P., Rousseau, M.-E., Kassis, N., Beck, N., Adalat, R., Das, S., Glatard, T., & Evans, A. C. (2014). CBRAIN: a web-based, distributed computing platform for collaborative neuroimaging research. *Frontiers in Neuroinformatics*, 8, 54. https://doi.org/10.3389/fninf.2014.00054
- Glatard, T., Rousseau, M.-E., Camarasu-Pop, S., Rioux, P., Sherif, T., Beck, N., Adalat, R., & Evans, A. C. (2014). Interoperability between the CBRAIN and VIP web platforms for neuroimage analysis. *Frontiers in Neuroinformatics*. https://doi.org/10.3389/conf.fninf.2014.18.00070
- CBRAIN GitHub Repository. https://github.com/aces/cbrain
- CBRAIN Portal. https://portal.cbrain.mcgill.ca