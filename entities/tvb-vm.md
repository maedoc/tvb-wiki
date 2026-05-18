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
updated: '2026-05-13'
---
TVB-VM (The Virtual Brain Virtual Machine) is a pre-configured virtual appliance that packages the complete [[the-virtual-brain]] software stack along with all necessary [[neuroimaging]] preprocessing dependencies in a single, ready-to-run environment. Originally developed to lower the barrier to entry for new users, TVB-VM provides a turnkey solution for [[whole-brain|whole-brain modeling]] that eliminates the complex software installation process traditionally associated with [[computational-neuroscience]] toolkits.

## Overview

TVB-VM is distributed as a virtual machine image (in OVA/OVA format) that can be run using standard virtualization software such as VirtualBox, VMware, or libvirt. The virtual appliance includes not only the TVB core libraries and web interface but also a complete suite of neuroimaging tools commonly used in the TVB workflow, including [[freesurfer]] for cortical reconstruction, [[fsl]] for FMRI analysis, [[mrtrix3]] for diffusion tractography, and various other utilities. This integrated approach means researchers can begin conducting whole-brain simulations immediately after booting the virtual machine, without needing to manually configure Python environments, install system dependencies, or manage software compatibility.

The virtual machine runs a Linux-based operating system with a pre-configured desktop environment, allowing users to interact with TVB through both its web-based graphical interface and command-line tools. The appliance is particularly valuable for reproducible research, as all software versions are pinned to known compatible configurations, reducing the "it works on my machine" problems that often plague computational neuroscience studies.

## Key Features

The primary advantage of TVB-VM lies in its comprehensive software bundling. Beyond the core [[tvb]] functionality, the virtual machine includes bidirectional interfaces to connectivity processing tools such as [[dipy]] for diffusion MRI processing, [[bids]] utilities for handling standardized neuroimaging datasets, and various atlas-based parcellation tools. Users can import structural connectivity matrices derived from [[diffusion-imaging]] data and immediately proceed to fitting neural mass models to empirical [[functional-connectivity]] patterns.

The TVB-VM distribution also includes visualization capabilities through [[tvb-webui]], allowing users to view 3D [[brain-network]] visualizations, time series animations, and [[bifurcation-analysis|bifurcation]] diagrams directly within the virtual machine. The integrated Jupyter notebook environment enables reproducible analysis workflows, combining simulation code with visualization and statistical analysis in a single document. This is particularly useful for researchers exploring [[parameter-estimation]] techniques or conducting sensitivity analyses on whole-brain models.

## Relationship to TVB

TVB-VM serves as one of several deployment options for [[the-virtual-brain]], complementing the traditional pip-based installation and [[tvb]] container approaches. Unlike the standalone Python installation, which requires users to manage their own Python environment and dependencies, TVB-VM provides a completely isolated system where all components are pre-configured to work together. This makes it particularly useful for workshops, tutorials, and educational settings where participants may have varying levels of technical expertise.

The virtual machine approach also facilitates workflow integration with external tools. Researchers can use the bundled neuroimaging software to process their own [[structural-connectivity]] data, import the resulting [[connectivity]] matrices into TVB, and then export simulation results for further analysis. This end-to-end capability makes TVB-VM a complete research platform for [[personalized-brain-modeling]] applications, from raw imaging data to fitted computational models.

## Limitations and Considerations
While TVB-VM addresses the installation heterogeneity that [[raw/papers/Renton2024.md|Renton et al. (2024)]] identify as a reproducibility barrier in neuroimaging—where purpose-built analysis software is challenging to install and may produce different results across computing environments—its virtualized architecture faces fundamental pressure from the computational demands of whole-brain modeling. [[raw/papers/semanticscholar-eb4197c24bf2.md|Movahedin et al. (2025)]] demonstrate that fitting patient-specific [[the-virtual-brain]] models requires a large number of successive and time-consuming simulations, a workload that strains even modern server-class CPUs and high-performance GPU implementations. Their heterogeneous FPGA accelerator achieves approximately 27× speedup over a 32-core CPU and about 14× lower latency than the GPU version of TVB while consuming an order of magnitude less energy, underscoring that every layer of abstraction between the simulation and dedicated hardware compounds the cost of model fitting.

The static, all-in-one bundling strategy that gives TVB-VM its turnkey reliability also contrasts with the modularity that contemporary reproducible platforms have demonstrated. [[raw/papers/Renton2024.md|Renton et al. (2024)]] show that containerized neuroimaging analysis eliminates inter-computer differences while offering browser-accessible virtual desktops alongside command-line tools and notebooks, illustrating how modern deployment can preserve flexibility alongside reproducibility. Because Neurodesk further achieves on-demand software streaming without full downloads through CVMFS [[raw/papers/Renton2024.md|Renton et al. (2024)]], the monolithic image approach of TVB-VM represents a different point in the design space—one that trades incremental updateability for immediate usability. As [[the-virtual-brain]] expands from its original scope of large-scale primate brain network simulation [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]] to clinical applications demanding iterative, time-consuming patient-specific fitting [[raw/papers/semanticscholar-eb4197c24bf2.md|Movahedin et al. (2025)]], this tension between turnkey convenience and the need for computational throughput and modular updates becomes the defining constraint of the virtual appliance.
## Related Software

TVB-VM relates to several other software deployment approaches in the TVB ecosystem. The [[tvb]] project provides containerized deployments offering similar convenience with reduced resource overhead. For users preferring native installations, [[tvb-library]] and [[tvb-rest]] provide programmatic APIs. The virtual machine also complements [[tvb-adapters]] by providing the execution environment needed to run simulations with various neural simulator backends including [[nest]] and [[brian2]].

TVB-VM integrates with the broader neuroimaging ecosystem through its bundled tools. [[connectome-workbench]] enables visualization of connectivity data in CIFTI format, while [[freesurfer]] provides the cortical segmentation needed for many TVB parcellation workflows. The combination of these tools within a single environment makes TVB-VM particularly valuable for researchers working across multiple neuroimaging modalities including [[neuroimaging-fmri]], [[neuroimaging-meg]], and [[neuroimaging-eeg]].
