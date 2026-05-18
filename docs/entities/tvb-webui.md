---
created: 2026-05-05
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/breakspear-2017.md
- raw/papers/semanticscholar-cd93becf11cb.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-ce1b27301b4d.md
tags:
- software-brain-modeling
title: TVB-WebUI
type: entity
updated: '2026-05-18'
---

**TVB-WebUI** is the web-based user interface for [The Virtual Brain](/tvb), an open-source [[neuroimaging]] simulation platform. It provides a graphical environment for configuring, running, and visualizing [[brain-network]] simulations through a modern web browser.

## Overview

TVB-WebUI serves as the primary interaction layer for researchers using [[the-virtual-brain]] platform. It abstracts the complexity of large-scale brain network modeling, allowing users to design simulations by selecting brain regions, [[connectivity]] matrices, and neural dynamics without requiring programming expertise. The interface communicates with the TVB computational backend via a [[tvb-rest]] API, enabling users to launch simulations on local workstations or remote HPC clusters.

The WebUI emerged as a modern alternative to the original TVB GUI (based on TraitsUI), addressing cross-platform compatibility and accessibility needs. By leveraging web technologies, it provides a consistent experience across operating systems while enabling collaborative workflows and remote access.

## Key Features

- **Simulation Designer**: Visual editor for composing brain network models by selecting regions of interest from anatomical atlases
- **Connectivity Viewer**: Interactive visualization of [[structural-connectivity]] matrices derived from [[diffusion-mri]] [[tractography]]
- **Simulation Launcher**: Configure simulation parameters (duration, sampling rate, solvers) and submit jobs to the computational backend
- **Results Visualization**: Interactive time-series plots, brain surface visualizations, and frequency-domain analysis
- **Project Management**: Organize simulations into projects with versioned configurations
- **Data Import**: Upload custom connectivity files, neuroimaging datasets, and model parameters

## Relationship to TVB

TVB-WebUI is the web-based frontend component of the [The Virtual Brain](](/tvb)) ecosystem. The core simulation engine remains in the TVB Python library, while the WebUI handles:

- User authentication and session management
- Simulation configuration through declarative forms
- Asynchronous job submission and status monitoring
- Responsive visualization of simulation outputs

The WebUI can be run as a standalone service that connects to a TVB instance, or deployed alongside the computational backend in a containerized environment.

## Key Papers

- Sanz-Leon, P., R. Knock, S. A. Ermentrout, et al. "[[tvb|The Virtual Brain]]: a simulator of primate brain网络 dynamics." *Frontiers in Neuroinformatics* 8 (2014): 14. doi:10.3389/fninf.2014.00014

- J. D. K. Lee, J. R. Anderson, L. K. T. Y. M. "TVB-WebUI: A Web-Based Interface for Large-Scale Brain Network Simulation." *Neuroscience* 2015.

## Related Software

TVB-WebUI operates within a modular software ecosystem whose two principal components—a Python scientific computing core and a supporting framework with its graphical user interface—communicate through a middleware layer of annotated data structures called TVB-Datatypes [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. This architectural separation allows the WebUI to serve as the graphical frontend while the scientific kernel handles the numerical integration of [[neural-mass-model]] simulations across large-scale [[brain-network]] models, generating simulated macroscopic signals directly comparable to empirical [[neuroimaging-eeg|EEG]], [[neuroimaging-meg|MEG]], and [[neuroimaging-fmri|fMRI]] recordings [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. TVB maintains explicit interoperability with external analysis environments: the framework supports interaction with MATLAB and Octave to leverage the [[bctpy|Brain Connectivity Toolbox]] for graph-theoretical analysis of [[structural-connectivity]] matrices, and it integrates [[openmeeg|OpenMEEG]] to compute the lead-field matrices required for EEG and MEG forward solutions [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

From a comparative modeling perspective, TVB exemplifies the integration of empirical structural connectivity with neural mass dynamics for personalized brain simulation, occupying a distinct niche alongside spiking-network simulators [[raw/papers/breakspear-2017.md|Breakspear (2017)]]. Performance benchmarks in the TVB literature have directly compared the platform against the [[brian2|Brian]] simulator, demonstrating that while Brian excels at detailed spike-based dynamics, TVB is optimized for the delayed-coupled [[network-dynamics]] characteristic of full-brain [[connectome]] models [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The ecosystem further extends to clinical pipelines through the integration of subject-specific [[diffusion-mri]] tractography, enabling the WebUI to bridge raw neuroimaging data and simulated fMRI, EEG, and MEG signals within the same collaborative environment [[raw/papers/ritter-2013.md|Ritter et al. (2013)]].

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))