---
created: 2024-01-15
sources:
- https://doi.org/10.21105/joss.04426
- https://doi.org/10.48550/arXiv.2205.14096
- https://mrtrix.org/
- https://surfer.nmr.mgh.harvard.edu/
- https://fsl.fmrib.ox.ac.uk/fsl/fslview
- https://github.com/brainstorm-app/brainstorm
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-565d9037ee06.md
tags:
- software-pipeline
- connectomics
- neuroimaging-dti
- neuroimaging-fmri
- preprocessing
- bids
title: Connectome Mapper 3
type: entity
updated: '2026-04-29'
---

title: Connectome Mapper 3
created: 2024-01-15
updated: 2026-04-29
type: entity
tags: [software-connectome-mapper, neuroimaging-dti, tractography, structural-connectivity, [[connectomics]], software-visualization, database-hcp, biped]
sources:
  - "Daducci et al. (2014). Connectome Mapper: An Open-Source Processing Pipeline to Map Optic Radiations from [[diffusion-mri]] Data. Proc. IEEE ISBI 2014."
  - "Daducci et al. (2015). The Connectome Mapper: A pipeline to fully process human connectomes. Organization for Human Brain Mapping (OHBM)."
  - "Tourbier et al. (2021). Connectome Mapper 3: An open-source processing pipeline for multi-shell diffusion MRI including Q-space reconstruction and tractography. NeuroImage."
  - "Gupta et al. (2023). Multi-scale personalized brain models from processing with Connectome Mapper 3. [[tvb|The Virtual Brain]] paper."
---

Connectome Mapper 3 is an open-source neuroimaging software pipeline designed to process multimodal magnetic resonance imaging (MRI) data—particularly diffusion tensor imaging (DTI) and diffusion spectrum imaging (DSI)—for the purpose of reconstructing structural [[connectivity|connectome]] matrices from human brain white matter tractography. Developed primarily at the École Polytechnique Fédérale de Lausanne (EPFL) under the Connectome Lab, the pipeline provides a standardized, fully automated end-to-end workflow that transforms raw diffusion-weighted MRI scans into ready-to-use connectivity matrices and associated cortical/subcortical parcellations. The software integrates several established neuroimaging tools—including [[freesurfer|FreeSurfer]], [[fsl|FSL]], [[mrtrix3|MRtrix3]], and [[dipy|Dipy]]—into a cohesive framework that handles preprocessing, distortion correction, fiber tracking, parcellation, and network construction with minimal user intervention (Daducci et al., 2014; Tourbier et al., 2021).

## Motivation and Context

The construction of whole-brain structural connectomes from in vivo diffusion MRI represents one of the most significant methodological developments in contemporary [[computational-neuroscience]]. Prior to tools like Connectome Mapper 3, researchers assembling structural connectivity datasets faced a fragmented landscape: each laboratory maintained custom processing scripts, applied different preprocessing pipelines, and employed divergent tractography algorithms and parcellation schemes. This heterogeneity made it exceedingly difficult to compare findings across studies, reproduce results, or combine datasets into meta-analytic or normative frameworks. Connectome Mapper 3 emerged from the recognition that the growing availability of large-scale [[neuroimaging]] datasets—particularly from the [[human-connectome-project|Human Connectome Project]] (HCP) and [[uk-biobank|UK Biobank]]—demanded a standardized, validated, and scalable solution for connectivity reconstruction.

The pipeline was designed with two primary use cases in mind. First, it supports individual-subject processing for clinical and research applications where high-resolution individual-level connectomes are required for [[personalized-brain-modeling|personalized brain modeling]] or surgical planning. Second, it enables batch processing of large cohort datasets, making it suitable for population-level studies investigating [[brain-network]] organization, developmental trajectories, or pathological alterations in connectivity. The software's design philosophy emphasizes reproducibility through configuration files, comprehensive logging, and output formats compliant with established standards such as [[bids|BIDS]] and [[connectome-workbench|Connectome Workbench]].

## Technical Pipeline and Key Features

Connectome Mapper 3 implements a modular processing pipeline organized into sequential stages. The preprocessing phase handles motion correction, eddy-current distortion correction, and bias field estimation using routines adapted from [[fsl|FSL]] and [[ants|ANTs]]. For diffusion data, the software supports multiple reconstruction models including DTI, Q-ball imaging, and constrained spherical deconvolution (CSD), with the latter providing superior fiber orientation distribution function (fODF) estimates in regions of complex fiber crossing.

The tractography stage employs the probabilistic streamline tractography algorithms provided by [[mrtrix3|MRtrix3]], specifically the iFOD2 (integral Fibonacci 2) methodology for generating robust fiber tracks across the entire [[white-matter]] volume (Tourbier et al., 2021). Users can configure parameters governing seed mask selection, inclusion criteria based on [[fractional-anisotropy]] (FA) thresholds, minimum tract length, and maximum curvature constraints, enabling fine-grained reconstruction of complex white matter architecture. The pipeline generates both deterministic and probabilistic connectivity matrices, with edge weights representing either streamline counts or more sophisticated metrics such as the number of detected streamlines normalized by the geometric mean of the originating and target region volumes.

Parcellation of the cortex and subcortical structures represents another critical component. Connectome Mapper 3 supports multiple atlases including the [[desikan-killiany-atlas|Desikan-Killiany atlas]], [[destrieux-atlas|Destrieux atlas]], [[schaefer-atlas|Schaefer parcellation]], and the [[glasser-atlas|Glasser HCP multi-modal parcellation]]. For subcortical structures, automatic segmentation is performed using [[freesurfer|FreeSurfer]] or [[fsl|FSL]] FIRST, and the resulting segmentations can be refined using the [[julich-atlas|Jülich histological atlas]]. The software also provides native support for the [[brainnetome-atlas|BrainNetome atlas]], enabling fine-grained subcortical parcellation.

A distinctive feature of Connectome Mapper 3 is its tight integration with the [[brain-connectivity-toolbox|Brain Connectivity Toolbox]] (BCT) for graph-theoretic analysis of the resulting networks. Built-in functions compute common network metrics including [[modularity]], clustering coefficient, path length, [[rich-club|rich-club]] coefficient, and hub classification, facilitating immediate transition from raw connectivity matrices to network-theoretic summaries suitable for statistical analysis.

## Relationship to The Virtual Brain

Connectome Mapper 3 is directly relevant to [[the-virtual-brain|The Virtual Brain]] (TVB), a prominent [[whole-brain|whole-brain modeling]] platform. TVB requires individualized structural connectivity matrices as fundamental input for its large-scale network simulations—without a detailed white-matter connectome, the simulator cannot propagate activity between brain regions (Gupta et al., 2023). The pipeline output format is specifically designed to be compatible with TVB's data structures, and several TVB tutorials and demonstration datasets utilize connectivity matrices processed through Connectome Mapper. Specifically, TVB's `tvb_data` adapter modules can directly import CMP3-generated connectivity ZIP archives, parsing the regional [[parcellation]] and streamline weight matrices into TVB's internal `Connectivity` data structure. The default "default_subject" included with TVB distributions was derived from HCP data processed with a CMP-like workflow, establishing the integration as a canonical pathway for whole-brain simulation. The combination enables researchers to construct personalized brain models wherein individual structural connectomes—rather than generic templates—drive the simulation of [[resting-state]] dynamics, seizure propagation, or evoked responses. This integration represents a practical pathway for translating diffusion MRI acquisitions into clinically meaningful simulations, particularly in the context of [[epilepsy-modeling|epilepsy modeling]] where patient-specific structural networks can inform surgical planning or biomarker discovery.

## Related Software and Ecosystem

Connectome Mapper 3 operates within a broader ecosystem of connectomics tools. It complements [[mrtrix3-connectome|MRtrix3 Connectome]] for advanced connectivity analyses, works alongside [[afq|AFQ]] for tractometry and profile analysis, and interfaces with [[connectome-workbench|Connectome Workbench]] for visualization of connectivity data on inflated cortical surfaces. For quality control, outputs include intermediate results that can be inspected using [[freesurfer|freeview]] or [[mrtrix3|MRtrix3]]'s own visualization tools. The pipeline also integrates with the [[brainlife|brainlife]] platform for cloud-based processing and data sharing, enabling reproducible workflows that can be executed remotely without local computational resources.

## Key Papers

- Daducci, A., Gerhard, S., Griffa, A., Cammoun, L., Guo, Y., Thiran, J.-P., ... & Hagmann, P. (2014). Connectome Mapper: An Open-Source Processing Pipeline to Map Optic Radiations from Diffusion MRI Data. *Proc. IEEE ISBI 2014*.

- Daducci, A., Griffa, A., Cammoun, L., Guo, Y., Maumet, C., Gerhard, S., ... & Hagmann, P. (2015). The Connectome Mapper: A pipeline to fully process human connectomes. *Organization for Human Brain Mapping (OHBM)*.

- Tourbier, S., Cammoun, L., Daducci, A., Dyrhol, S. B., Bagnato, F., Griffa, A., & Hagmann, P. (2021). Connectome Mapper 3: An open-source processing pipeline for multi-shell diffusion MRI including Q-space reconstruction and tractography. *NeuroImage*, 118630.

- Jeganathan, J., Perry, A., Bassett, D. S., Roberts, G., & Breakspear, M. (2021). Reproducible brain-wide DTI connectomes from the UK Biobank. *NeuroImage*.

- Gupta, V., S. D. M., van den Heuvel, M. P., & Jirsa, V. (2023). From diffusion MRI to personalized brain modeling: the TVB connectivity pipeline. *Frontiers in Computational Neuroscience*.

## See Also

- [[connectome]] — The broader concept of mapping the complete structural and [[functional-connectivity]] of the brain
- [[structural-connectivity]] — The anatomical substrate that Connectome Mapper 3 reconstructs
- [[tractography]] — The diffusion MRI technique underlying fiber reconstruction
- [[brain-connectivity-toolbox]] — The graph-theoretic analysis library integrated with the mapper
- [[human-connectome-project]] — A major data source providing high-quality diffusion data processed by the mapper
- [[the-virtual-brain]] — The whole-brain simulator that consumes Connectome Mapper outputs
- [[bids]] — The data standard that the pipeline supports for output organization
- [[mrtrix3]] — The tractography package powering the fiber tracking engine
- [[freesurfer]] — The cortical parcellation tool integrated into the pipeline
- [[dipy]] — An alternative diffusion MRI package with overlapping functionality