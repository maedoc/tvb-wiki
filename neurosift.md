---
title: Neurosift
created: 2026-05-04
updated: 2026-05-05
type: entity
tags: [software-visualization, dandi, openneuro, neuroimaging, visualization-tools]
sources: [raw/papers/joss-06590.md, raw/papers/github-flatiron-neurosift.md]
---

Neurosift is a browser-based visualization platform developed by Jeremy Moreau at the [Flatiron Institute](https://flatironinstitute.org/) that enables interactive exploration of neuroscience data, with particular emphasis on NWB (Neurodata Without Borders) files and cloud-hosted neurophysiology archives [@joss-neurosift]. The platform provides a unified interface for browsing, visualizing, and sharing neuroscientific datasets without requiring local software installation, making it especially valuable for collaborative research workflows and reproducible science [@nwb-format].

## Overview

Neurosift addresses a fundamental challenge in modern neuroscience: the growing volume and complexity of neurophysiology data demands web-based tools that can render diverse data types interactively while maintaining tight integration with established data archives. Unlike traditional desktop visualization applications that require substantial local setup, Neurosift runs entirely in the browser and can stream data directly from remote archives, lowering barriers to exploratory data analysis. The platform supports multiple neuroimaging and neurophysiology data modalities, including extracellular electrophysiology recordings, calcium imaging, behavioral tracking data, and volumetric imaging data such as NIfTI files.

The architecture distinguishes between local and remote access modes. In local mode, users can visualize files directly from their device by installing the Python package via pip and executing simple command-line instructions. Remote mode enables real-time visualization of datasets hosted on cloud archives by passing URL parameters to the web application, allowing researchers to share specific data snapshots with collaborators without transferring large files. This dual-mode design makes Neurosift adaptable to different use cases, from quick local inspection of individual subjects to systematic browsing of entire datasets within a repository.

## Key Features

The visualization capabilities of Neurosift span several categories of neuroscientific data types. For electrophysiology data, the platform renders spike raster plots showing sorted unit activity across recording channels, alongside continuous voltage traces that can be zoomed and scrolled interactively. Behavioral data visualization includes position decode fields tracking animal movement, video annotations overlaid on recording sessions, and spectrograms for audio stimuli or vocalizations. The platform also supports rendering of video data stored within NWB files, enabling correlated visualization of neural activity and behavioral footage.

A distinguishing capability is the deep integration with major neuroscience data archives. Users can browse the contents of [DANDI Archive](dandi.md) directly within Neurosift, navigate through published datasets (dandisets), and open individual NWB files for immediate visualization without downloading the entire archive. Similarly, [OpenNeuro](openneuro.md) datasets can be accessed, providing a pathway for exploring neuroimaging datasets including fMRI and EEG recordings [@openneuro-dataset]. The EMBER Archive is also supported, extending the reach to certain classes of processed and derived data products.

The technical implementation leverages niivue for NIfTI volume rendering, enabling visualization of three-dimensional brain imaging data including anatomical MRI, functional MRI activation maps, and diffusion tensor imaging scalar maps. This integration makes Neurosift applicable not only to the microelectrode recording domain but also to broader neuroimaging contexts, complementing tools like [Connectome Workbench](connectome-workbench.md) for CIFTI/surface data visualization and [BrainNet Viewer](brainnet-viewer.md) for network visualization [@workbench-cifti].

## Relationship to TVB

The relationship between Neurosift and [The Virtual Brain](the-virtual-brain.md) is indirect but potentially valuable for researchers working across the spectrum from empirical data to whole-brain modeling. TVB produces simulation outputs including regional time series, [functional connectivity](functional-connectivity.md) matrices, and [structural connectivity](structural-connectivity.md) surrogates that require visualization for interpretation and validation [@tvb-paper]. While no native integration exists between TVB and Neurosift, the common dependency on standardized data formats creates a potential interoperability pathway.

Specifically, if TVB simulation outputs are exported to NWB format—either through custom export routines or via intermediate tools like the TVB-to-NWB converter—Neurosift could provide browser-based visualization of simulated neural activity, complementing TVB's built-in visualization capabilities. This could prove useful for collaborative projects where team members wish to inspect simulation results without setting up a local TVB instance, or for sharing specific simulation epochs with external collaborators. Additionally, Researchers using TVB to generate synthetic functional connectivity data could leverage Neurosift's integration with empirical archives like DANDI to compare simulated dynamics against real neuroimaging datasets, supporting validation workflows in [personalized brain modeling](personalized-brain-modeling.md).

## Key Papers and Documentation

The primary reference for Neurosift is the Journal of Open Source Software publication by Magland, Soules, Dichter, and Baker (2024), which describes the architecture, feature set, and integration with neurophysiology archives [@joss-neurosift]. The software documentation provides detailed instructions for local installation, web-based usage, and developer contribution guidelines. The live application is hosted at [https://neurosift.app](https://neurosift.app), and the source code is available on GitHub under the Apache 2.0 license, facilitating community contributions and extensions.

## Related Tools and Platforms

Neurosift occupies a niche in the neuroscience visualization landscape alongside several complementary tools. While web-based NWB visualization tools exist, Neurosift's distinguishing strength lies in its tight integration with major data archives and zero-setup browser access [@nwb-format].

## References

- [@joss-neurosift] Magland, J., Soules, C., Dichter, B., & Baker, S. (2024). Neurosift: Browser-based visualization for neurophysiology and neuroimaging data. *Journal of Open Source Software*, 9(99), 6550. https://doi.org/10.21105/joss.06590

- [@nwb-format] Teeters, J. L., Godfrey, K., Young, R., Chaurand, M., Gollub, R., Puetz, T., ... & Helmer, K. (2015). Neurodata Without Borders: Creating a common data format for neurophysiology. *Frontiers in Neuroinformatics*, 9, 9. https://doi.org/10.3389/fninf.2015.00025

- [@openneuro-dataset] Poldrack, R. A., Barch, D. M., Mitchell, J. P., Glasser, M. F., Zhang, S., Andersson, J., ... & Poline, J. B. (2013). An open resource for the analysis of fMRI data. *Frontiers in Neuroinformatics*, 7, 13. https://doi.org/10.3389/fninf.2013.00013

- [@tvb-paper] Sanz Leon, P., Knock, S. A., Woodman, M. M., Domide, L., Mersmann, J., McIntosh, A. R., & Jirsa, V. (2013). The Virtual Brain: A simulator of primate brain network dynamics. *Frontiers in Neuroinformatics*, 7, 10. https://doi.org/10.3389/fninf.2013.00010

- [@workbench-cifti] Marcus, D. S., Harwell, J., Olsen, T., Hodge, M., Glasser, M. F., Prior, F., ... & Van Essen, D. C. (2011). Informatics and data mining tools and strategies for the Human Connectome Project. *Frontiers in Neuroinformatics*, 5, 4. https://doi.org/10.3389/fninf.2011.00004 For cortical surface visualization, particularly of [CIFTI](cifti-tools.md) data from the [Human Connectome Project](human-connectome-project.md), [Connectome Workbench](connectome-workbench.md) remains the dominant tool, though it requires desktop installation unlike Neurosift's browser-based approach [@workbench-cifti].

The choice between these tools depends on the specific data types, workflow requirements, and user preferences regarding local versus cloud-based analysis. Neurosift's strength lies in its zero-setup browser access and tight coupling to archival repositories, making it particularly suitable for quick data inspection, teaching environments, and collaborative sharing scenarios where installing specialized software would be impractical.