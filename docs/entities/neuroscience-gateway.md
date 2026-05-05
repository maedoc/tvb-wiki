---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
tags:
- software-neuron
- software-brian
- computational-neuroscience
- reproducibility
- database-hcp
title: Neuroscience Gateway
type: entity
updated: '2026-05-05'
---

## Overview
The Neuroscience Gateway (NSG) is a web-based computing portal that provides [[computational-neuroscience]] researchers with access to neural simulation software and high-performance computing (HPC) resources through a simple web interface [@nsg-portal]. Developed to address the increasing computational demands of large-scale brain modeling and to lower barriers to entry for researchers without dedicated computing infrastructure, NSG serves as a central access point for running sophisticated neural simulations without requiring local software installation or significant local computational resources.

The project originated from the San Diego Supercomputer Center (SDSC) at UC San Diego, with collaborative development involving Yale University. In 2012, the National Science Foundation (NSF) awarded a collaborative grant (awards DBI 1146949 to UC San Diego and DBI 1146830 to Yale University) to develop the Neuroscience Gateway, which officially launched in early 2013 [@ucsd-news-2012]. The project was led by Amit Majumdar (SDSC) as principal investigator, with Maryann Martone (Neuroscience Information Framework) as co-principal investigator, and Ted Carnevale (Yale) as the Yale principal investigator.

The platform supports multiple simulation engines including [[NEURON]], [[GENESIS]], [[MOOSE]], [[Brian]], [[NEST]], and [[PyNN]], enabling researchers to construct, configure, and execute complex neural models while leveraging remote HPC clusters. As part of the broader Neuroscience Information Framework (NIF) ecosystem, NSG represents a key piece of neuroinformatics infrastructure that promotes reproducibility and accessibility in computational neuroscience research.

## Key Features
The Neuroscience Gateway provides several critical features that distinguish it from local simulation approaches. First, the platform offers a unified web-based interface through which users can submit simulation jobs to remote HPC resources (including SDSC's Comet and Expanse, and other ACCESS/XSEDE resources), eliminating the need for local installation and configuration of potentially complex software packages. This abstraction layer handles job scheduling, resource allocation, and output management, allowing researchers to focus on model design rather than computational infrastructure [@carnevale-2014].

Second, NSG maintains a curated collection of popular neural simulation engines that are pre-configured and tested on the remote computing clusters, ensuring compatibility and optimal performance across different software packages. The NSG team collaborates with developers of neural simulation tools to optimally install, test, and benchmark these applications on compute resources.

Third, the gateway supports both interactive sessions for exploratory modeling and batch processing for large-scale parameter sweeps, accommodating diverse research workflows. Notably, NSG provides bundled job submission support for Brian, enabling parameter sweep studies to be performed by creating a jobs-list file with multiple executable commands.

Fourth, the platform provides access to example models from databases such as [[model-validation]]—users can download models from ModelDB and upload them to NSG for simulation on HPC resources—but direct automated importing from model databases is not a built-in feature.

Fifth, NSG includes tools for managing simulation outputs and results, facilitating data organization and sharing within research groups. Users receive email notifications upon job completion, and results are downloadable as zip archives containing the entire working directory.

## Relationship to TVB
While the Neuroscience Gateway and [[The Virtual Brain]] (TVB) serve complementary roles in computational neuroscience, they address different aspects of the research workflow. TVB is a specialized [[whole-brain|whole-brain modeling]] platform designed for [[connectome]]-based simulations at the network level, integrating [[structural-connectivity]] data with [[neural-mass-models]] to simulate [[brain-dynamics]] at scale. In contrast, NSG provides a more general-purpose computing infrastructure for lower-level neural simulations, including single-neuron models, small network simulations, and detailed biophysical models.

Researchers using TVB may leverage NSG resources for certain computational tasks, particularly when performing parameter optimization or [[parameter-estimation]] procedures that require significant computing power. The distinction reflects the architectural philosophy: TVB provides a specific modeling framework optimized for whole-brain dynamics, while NSG offers flexible access to diverse simulation tools for varied computational neuroscience applications.

## Technical Architecture
The technical architecture of the Neuroscience Gateway consists of several interconnected components that work together to provide seamless access to computational resources. At the frontend, users interact with a web-based portal that allows model upload, parameter specification, and job submission through a graphical interface or programmatic [[rest]] APIs (known as NSG-R). This frontend connects to a job management system that handles queueing, scheduling, and execution of simulation tasks across available HPC resources.

The backend computing clusters are equipped with multiple neural simulation packages compiled and optimized for the specific hardware, ensuring reasonable execution performance. The gateway maintains user workspaces where simulation results are stored and can be accessed after job completion. Additionally, NSG provides configuration files and tutorials for common simulation scenarios, reducing the learning curve for new users. The system supports both the NEURON interpreter format (hoc and mod files) and [[NeuroML]] representations, promoting model interoperability and reuse across platforms.

NSG transparently distributes user jobs to appropriate HPC resources available through XSEDE (now ACCESS). The architecture also supports access to High Throughput Computing (HTC) resources through the Open Science Grid (OSG) and cloud computing resources.

## Related Software
Neuroscience Gateway intersects with several categories of software in the computational neuroscience ecosystem. For neural simulation, it supports multiple engines including [[NEURON]], [[GENESIS]], [[MOOSE]], [[Brian]], [[NEST]], and [[PyNN]]. For model management, it works with [[model-validation]] for model retrieval—users can download models from ModelDB and run them on NSG—and complements [[NeuroMorpho]] for morphological data. For data processing workflows, it complements tools like [[nipype]] that provide preprocessing pipelines for neuroimaging data. For reproducibility, NSG supports containerized workflows where compatible. The gateway also relates to specialized whole-brain simulators including [[The Virtual Brain]], which may be executed on NSG infrastructure for large-scale simulations. Related brain imaging and visualization tools that may be used in conjunction include [[FreeSurfer]], [[FSL]], and [[AFNI]] for MRI analysis, as well as [[BrainNet Viewer]] for visualization of connectivity results.

## Use Cases and Applications
The Neuroscience Gateway enables a wide range of computational neuroscience research applications that would be impractical on standard desktop computers. Large-scale network simulations involving thousands of neurons and millions of synapses can be executed on the HPC resources provided by NSG, enabling investigations of cortical circuit dynamics that are beyond the scope of local computing.

Parameter sweep studies that systematically explore the behavior of neural models across high-dimensional parameter spaces become feasible when parallel computing resources are available through the gateway. Researchers studying specific neural phenomena such as [[synaptic-plasticity]], dendritic integration, or network oscillations can construct detailed biophysical models and run extended simulations to collect sufficient data for analysis.

The platform also supports educational use cases, allowing students to run simulations without requiring access to dedicated computing infrastructure or installation of specialized software. NSG has been used for teaching neuroscience courses and workshops, where students can access simulation resources without needing individual accounts on HPC systems.

Collaborative research projects benefit from the centralized nature of NSG, where shared workspaces facilitate data sharing and [[reproducibility]] across team members. The free access model (for academic and non-profit users) helps democratize computational neuroscience research, particularly benefiting researchers at institutions with limited computational infrastructure.

## Key Papers
The following publications document the development and use of the Neuroscience Gateway:

- Carnevale T, Majumdar A, Sivagnanam S, Yoshimoto K, Astakhov V, Bandrowski A, Martone M (2014). The neuroscience gateway portal: high performance computing made easy. BMC Neuroscience 15(Suppl 1):P101. https://doi.org/10.1186/1471-2202-15-S1-P101

- Sivagnanam S, Majumdar A, Yoshimoto K, Astakhov V, Bandrowski A, Martone M, Carnevale N (2013). Introducing the Neuroscience Gateway. Proceedings of the 5th International Workshop on Science Gateways. CEUR Workshop Proceedings 993.

- Sivagnanam S, Yoshimoto K, Astakhov V, Majumdar A (2018). The Neuroscience Gateway: Enabling Large Scale Modeling and Data Processing in Neuroscience. PEARC '18.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861)
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161)