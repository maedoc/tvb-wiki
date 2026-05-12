---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-eb4197c24bf2.md
- raw/papers/Renton2024.md
tags:
- software-tvb
- whole-brain-modeling
- computational-neuroscience
- software-visualization
- software-modeling
title: TVB-VM
type: entity
updated: '2026-05-12'
---

TVB-VM (The Virtual Brain Virtual Machine) is a pre-configured virtual appliance that packages the complete [[the-virtual-brain]] software stack along with all necessary neuroimaging preprocessing dependencies in a single, ready-to-run environment. Originally developed to lower the barrier to entry for new users, TVB-VM provides a turnkey solution for whole-brain modeling that eliminates the complex software installation process traditionally associated with computational neuroscience toolkits.

## Overview

TVB-VM is distributed as a virtual machine image (in OVA/OVA format) that can be run using standard virtualization software such as VirtualBox, VMware, or libvirt. The virtual appliance includes not only the TVB core libraries and web interface but also a complete suite of neuroimaging tools commonly used in the TVB workflow, including [[freesurfer]] for cortical reconstruction, [[fsl]] for FMRI analysis, [[mrtrix3]] for diffusion tractography, and various other utilities. This integrated approach means researchers can begin conducting whole-brain simulations immediately after booting the virtual machine, without needing to manually configure Python environments, install system dependencies, or manage software compatibility.

The virtual machine runs a Linux-based operating system with a pre-configured desktop environment, allowing users to interact with TVB through both its web-based graphical interface and command-line tools. The appliance is particularly valuable for reproducible research, as all software versions are pinned to known compatible configurations, reducing the "it works on my machine" problems that often plague computational neuroscience studies.

## Key Features

The primary advantage of TVB-VM lies in its comprehensive software bundling. Beyond the core [[tvb]] functionality, the virtual machine includes bidirectional interfaces to connectivity processing tools such as [[dipy]] for diffusion MRI processing, [[bids]] utilities for handling standardized neuroimaging datasets, and various atlas-based parcellation tools. Users can import structural connectivity matrices derived from [[diffusion-imaging]] data and immediately proceed to fitting neural mass models to empirical [[functional-connectivity]] patterns.

The TVB-VM distribution also includes visualization capabilities through [[tvb-webui]], allowing users to view 3D brain network visualizations, time series animations, and bifurcation diagrams directly within the virtual machine. The integrated Jupyter notebook environment enables reproducible analysis workflows, combining simulation code with visualization and statistical analysis in a single document. This is particularly useful for researchers exploring [[parameter-estimation]] techniques or conducting sensitivity analyses on whole-brain models.

## Relationship to TVB

TVB-VM serves as one of several deployment options for [[the-virtual-brain]], complementing the traditional pip-based installation and [[docker]] container approaches. Unlike the standalone Python installation, which requires users to manage their own Python environment and dependencies, TVB-VM provides a completely isolated system where all components are pre-configured to work together. This makes it particularly useful for workshops, tutorials, and educational settings where participants may have varying levels of technical expertise.

The virtual machine approach also facilitates workflow integration with external tools. Researchers can use the bundled neuroimaging software to process their own [[structural-connectivity]] data, import the resulting connectivity matrices into TVB, and then export simulation results for further analysis. This end-to-end capability makes TVB-VM a complete research platform for [[personalized-brain-modeling]] applications, from raw imaging data to fitted computational models.

## Limitations and Considerations

While TVB-VM provides convenience, it carries certain trade-offs relative to other deployment methods. The virtual machine image requires significant disk space and may run slower than native installations on resource-constrained hardware. Updates to TVB or its dependencies require downloading new virtual machine images rather than simple package manager upgrades. For production environments requiring high-performance simulations, many researchers prefer running TVB directly on bare metal or using Docker containers that can be easily rebuilt with updated software versions.

## Related Software

TVB-VM relates to several other software deployment approaches in the TVB ecosystem. The [[tvb-docker]] project provides containerized deployments offering similar convenience with reduced resource overhead. For users preferring native installations, [[tvb-library]] and [[tvb-rest]] provide programmatic APIs. The virtual machine also complements [[tvb-adapters]] by providing the execution environment needed to run simulations with various neural simulator backends including [[nest]] and [[brian2]].

TVB-VM integrates with the broader neuroimaging ecosystem through its bundled tools. [[connectome-workbench]] enables visualization of connectivity data in CIFTI format, while [[freesurfer]] provides the cortical segmentation needed for many TVB parcellation workflows. The combination of these tools within a single environment makes TVB-VM particularly valuable for researchers working across multiple neuroimaging modalities including [[neuroimaging-fmri]], [[neuroimaging-meg]], and [[neuroimaging-eeg]].