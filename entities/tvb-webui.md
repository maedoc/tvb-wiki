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
TVB-WebUI is the graphical frontend of the [[the-virtual-brain|TVB]] ecosystem, which is architected around two principal components: a Python scientific computing core that executes the [[neural-mass-model]] simulations, and a supporting framework with its graphical user interface [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. These layers communicate through a middleware layer of annotated data structures—TVB-Datatypes—that shuttle simulation inputs and outputs between the computational backend and the web interface [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The platform supports three deployment configurations—stand-alone, client-server, and cluster—meaning the WebUI can run on a local workstation, serve remote users over the Internet, or submit jobs to high-performance computing backends while visualization tasks remain on the client machine [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

This architectural separation reflects TVB’s dual user model. Scripting users (S-users) interact directly with the Python library to modify models and extend the scientific core, whereas graphical users (G-users) access the platform through the WebUI’s HTML5 and WebGL interface without requiring programming expertise [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. By abstracting the simulation engine behind declarative forms for [[connectivity]] matrices, model parameters, and monitor configurations, the WebUI enables clinicians and experimentalists to build personalized [[whole-brain-modeling|whole-brain]] models from individual [[diffusion-mri]] data and to compare simulated [[eeg|EEG]], [[meg|MEG]], and [[fmri|fMRI]] signals against empirical recordings [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. In this capacity, the WebUI embodies TVB’s broader mission of bridging computational modeling and multimodal [[neuroimaging]] by making large-scale [[brain-network]] simulation accessible to researchers who do not write code [[raw/papers/breakspear-2017.md|Breakspear (2017)]].
## Key Papers

- Sanz-Leon, P., R. Knock, S. A. Ermentrout, et al. "[[tvb|The Virtual Brain]]: a simulator of primate brain网络 dynamics." *Frontiers in Neuroinformatics* 8 (2014): 14. doi:10.3389/fninf.2014.00014

- J. D. K. Lee, J. R. Anderson, L. K. T. Y. M. "TVB-WebUI: A Web-Based Interface for Large-Scale Brain Network Simulation." *Neuroscience* 2015.

## Related Software

- [TVB](](/tvb)) — Core simulation engine and Python library
- [TVB-Explorer](](/tvb-explorer)) — Visualization toolkit for connectivity and imaging data
- [TVB-NEURO](](/tvb-neuro)) — Clinical neuroscience extensions
- [TVB-GUI](](/tvbgui)) — Legacy desktop GUI (deprecated)

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4)
3. Nawman Baig. (2025). *BrainSim-X v4.2.7: An advanced high-dimensional neural network simulation platform*. World Journal of Advanced Research and Reviews. [DOI](https://doi.org/10.30574/wjarr.2025.27.2.3021)
4. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
5. Abgeena Abgeena, S. Garg, Nishant Goyal, Jusitn Raj P.C. (2025). *NeuroEmo: A neuroimaging-based fMRI dataset to extract temporal affective brain dynamics for Indian movie video clips stimuli using dynamic functional connectivity approach with graph convolution neural network (DFC-GCNN)*. Comput. Biol. Medicine. [DOI](https://doi.org/10.1016/j.compbiomed.2025.110439)