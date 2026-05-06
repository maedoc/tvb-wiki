---
created: 2026-05-05
sources:
- https://www.thevirtualbrain.org
- https://github.com/thevirtualbrain/tvb-webui
tags:
- software-brain-modeling
title: TVB-WebUI
type: entity
updated: '2026-05-06'
---

**TVB-WebUI** is the web-based user interface for [The Virtual Brain](/tvb), an open-source [[neuroimaging]] simulation platform. It provides a graphical environment for configuring, running, and visualizing [[brain-network]] simulations through a modern web browser.

## Overview

TVB-WebUI serves as the primary interaction layer for researchers using [[the-virtual-brain]] platform. It abstracts the complexity of large-scale brain network modeling, allowing users to design simulations by selecting brain regions, [[connectivity]] matrices, and neural dynamics without requiring programming expertise. The interface communicates with the TVB computational backend via a [[rest]] API, enabling users to launch simulations on local workstations or remote HPC clusters.

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

- [TVB](](/tvb)) — Core simulation engine and Python library
- [TVB-Explorer](](/tvb-explorer)) — Visualization toolkit for connectivity and imaging data
- [TVB-NEURO](](/tvb-neuro)) — Clinical neuroscience extensions
- [TVB-GUI](](/tvbgui)) — Legacy desktop GUI (deprecated)