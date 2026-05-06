---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/van-essen-2012.md
- raw/papers/semanticscholar-eb4197c24bf2.md
- raw/papers/glean-github.md
tags:
- software-visualization
- neuroimaging
- cifti
- human-connectome-project
- brain-atlases
- connectomics
- software-fsl
- database-hcp
title: Connectome Workbench
type: entity
updated: '2026-05-04'
---

## Overview

[[connectome]] Workbench (often abbreviated as "Workbench") is a free, open-source software suite developed by the Human Connectome Project (HCP) for the visualization and analysis of [[neuroimaging]] data, with particular emphasis on surface-based data and CIFTI ([[connectivity]] Informatics Technology Initiative) file formats. Originally released in 2012 alongside the first HCP datasets, Workbench has become a standard tool in the [[connectomics]] community for viewing [[brain-parcellations]], visualizing [[functional-connectivity]] maps, and exploring [[structural-connectivity]] data [1]. The software provides a graphical user interface (wb_view) and command-line tools (wb_command) that enable researchers to perform sophisticated analyses on high-dimensional neuroimaging datasets without requiring programming expertise.

## Motivation and Context

The development of Connectome Workbench was driven by a specific challenge: existing neuroimaging visualization tools were not designed to handle the massive, high-resolution datasets produced by modern acquisition protocols, particularly those from the HCP [2]. Traditional volumetric analysis had limitations when working with surface-based data (e.g., cortical thickness maps, functional activation on the cortical sheet) and the novel CIFTI format, which combines surface-based cortical data with volumetric subcortical structures in a single file. Workbench was engineered specifically to address these needs, providing native support for CIFTI files, GIFTI (Geometry Interface Format) surface meshes, and [[nifti]] volumes within an integrated environment.

The software emerged during a period of rapid growth in [[whole-brain]] connectomics, when researchers increasingly needed to visualize and compare connectivity patterns across hundreds of brain regions. This context positioned Workbench as an essential tool for researchers working with the HCP database and other large-scale neuroimaging initiatives, enabling intuitive exploration of data that would otherwise require custom scripting in Python or MATLAB.

## Key Features

Connectome Workbench provides several core capabilities that distinguish it from other neuroimaging visualization tools. The graphical interface, **wb_view**, supports simultaneous viewing of multiple data types including cortical surfaces, subcortical volumes, and dense connectome matrices. Users can display vertex-wise or ROI-wise data on inflated, flattened, or native cortical surfaces, with flexible colormap controls and transparency settings. The software handles the distinction between left and right hemisphere surfaces and maintains proper anatomical alignment across different brain templates.

The command-line interface, **wb_command**, offers batch-processing capabilities essential for pipeline automation. Common operations include extracting data from CIFTI files by label or surface ROI, computing row-wise statistics on dense timeseries, and resampling data between different mesh resolutions. These commands integrate seamlessly with shell scripts and workflow managers, enabling reproducible preprocessing pipelines.

Workbench also includes built-in support for the Glasser HCP [[parcellation]] (a multimodal parcellation of human cortex based on [[fmri]], myelin mapping, and cortical architecture) [3] and other commonly used brain atlases. Users can overlay parcel boundaries on functional or structural data, facilitating region-of-interest analyses and comparison with theoretical network models from the brain connectivity literature.

## Relationship to The Virtual Brain

Connectome Workbench serves a complementary role to [[The Virtual Brain]] (TVB) in whole-brain modeling workflows. TVB is primarily a simulation platform that generates synthetic neuroimaging data ([[bold-signal|BOLD]] signals, EEG, MEG) from biologically plausible [[neural-mass-models]] operating on structural connectomes. Workbench, by contrast, is a visualization and light-analysis tool for empirical neuroimaging data. In practice, the two tools often appear together: researchers may use Workbench to explore the empirical structural connectivity matrices (derived from [[diffusion-imaging]]) that serve as TVB's anatomical scaffold, then visualize TVB's simulated BOLD output in Workbench for direct comparison with empirical data. Both software packages are freely available and run on Linux, macOS, and Windows platforms, though Workbench's native CIFTI support makes it particularly valuable for analyzing HCP-style datasets that TVB users may import as reference data.

## Related Software

Connectome Workbench operates within a broader ecosystem of neuroimaging visualization tools. [[Freeview]] (the FreeSurfer visualization companion) serves similar purposes for FreeSurfer-processed data, while Fsleyes provides another free alternative for volume and surface visualization. For CIFTI-specific operations, the [[cifti]] format is supported by other packages including Nilearn and Pycortex, though these lack Workbench's full GUI capabilities. The [[human-connectome-project]] maintains Workbench as part of its data processing pipeline, alongside [[hcp-pipelines]] and related tools for minimal preprocessing of diffusion and functional MRI data.

## Key Capabilities Summary

| Feature | Description |
|---------|-------------|
| File formats | CIFTI, GIFTI, NIfTI, annot |
| GUI | wb_view for interactive exploration |
| CLI | wb_command for batch processing |
| Atlases | Glasser, Desikan-Killiany, Destrieux, others |
| Platforms | Linux, macOS, Windows |

## Key Papers

1. Human Connectome Project. (2015). Human Connectome Project. https://www.humanconnectome.org/
2. Van Essen, D. C., Smith, S. M., Barch, D. M., Behrens, T. E., Yacoub, E., & Ugurbil, K. (2013). The Human Connectome Project: A data acquisition perspective. NeuroImage, 62, 2222-2231.
3. Glasser, M. F., Coalson, T. S., Robinson, E. C., Hacker, C. D., Harwell, J., Yacoub, E., ... & Van Essen, D. C. (2016). A multi-modal parcellation of human cerebral cortex. Nature, 536(7615), 171-178.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. (authors unknown). *The Human Connectome Project: A Data Acquisition Perspective*.
3. Amirreza Movahedin, Lennart P. L. Landsmeer, Christos Strydis. (2025). *HUMA: Heterogeneous, Ultra Low-Latency Model Accelerator for The Virtual Brain on a Versal Adaptive SoC*. Symposium on Field Programmable Gate Arrays. [DOI](](https://doi.org/10.1145/3706628.3708875))
4. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.