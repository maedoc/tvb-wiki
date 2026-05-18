---
created: 2026-05-13
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/schirner-2018.md
- raw/papers/basser-1994.md
- raw/papers/mori-1999.md
- raw/papers/jones-2010.md
tags:
- software-tvb
- diffusion-imaging
- neuroimaging-dti
- tractography
- structural-connectivity
- connectomics
- whole-brain-modeling
title: tvb-diffusion
type: entity
updated: '2026-05-15'
---

# tvb-diffusion

## Overview

`tvb-diffusion` is the diffusion imaging integration module of [[tvb|The Virtual Brain]] (TVB) that transforms [[diffusion-mri]] data and [[tractography]] outputs into the [[structural-connectivity]] matrices and conduction delay tables required for whole-brain network simulations. It serves as the anatomical data ingestion layer, converting subject-specific white-matter reconstructions—whether from [[dti|diffusion tensor imaging]], constrained spherical deconvolution, or other orientation models—into the weighted coupling matrices that parameterize [[neural-mass-models]] across the cortical surface [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The module is not a tractography engine itself but rather the bridge between external tractography pipelines and TVB's simulation framework, ingesting streamline counts, [[fractional-anisotropy]] values, or mean diffusivity estimates and packaging them into the normalized, TVB-compatible data structures that drive dynamic models.

## Motivation and Context

Whole-brain modeling imposes a strict architectural requirement: every computational model, from the simplest [[jansen-rit]] oscillator to complex multiscale [[spiking-neural-networks]], must be embedded in an anatomically faithful connectivity scaffold. The [[connectome]]-derived structural backbone determines which brain regions interact, how strongly they are coupled, and the temporal delays imposed by axonal transmission—parameters that collectively constrain emergent dynamics, synchronization patterns, and the repertoire of observable brain states [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. Without a standardized mechanism to ingest diffusion-derived connectivity into simulations, researchers would need to hand-craft connectivity matrices for every model, introducing formatting errors, normalization inconsistencies, and non-reproducible preprocessing steps.

`tvb-diffusion` addresses this integration gap by providing a programmatic pipeline that accepts the outputs of established tractography toolkits—including those built on [[mrtrix3]], [[dipy]], and FSL—and maps them onto user-specified [[parcellation]] schemes. The module performs hemispheric alignment, symmetry enforcement (where appropriate), and weight normalization so that connectivity matrices conform to the expectations of TVB's simulation kernel, [[tvb-library]] [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. This standardization was a core design principle of the TVB platform, which was built to accommodate multiple neural mass models within interchangeable anatomical substrates [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Technical Pipeline

The module's workflow begins with pre-computed tractography results rather than raw DICOM volumes, reflecting a deliberate design choice that keeps TVB decoupled from upstream preprocessing concerns such as eddy-current correction, susceptibility distortion correction, and fiber orientation estimation. Inputs typically include a region-to-region streamline count matrix, optionally supplemented by tract-averaged scalar metrics like FA or mean diffusivity, and a corresponding tract-length matrix encoding the mean physical distance traversed by streamlines connecting each node pair.

Internally, the module executes several transformations. First, it maps the input parcellation labels to the node ordering expected by the model surface, performing reindexing and optional hemisphere flipping. Second, it converts raw streamline counts into normalized connection weights—typically by dividing each row by its sum or by applying a global scaling factor that renders coupling strengths dimensionless and bounded, preventing runaway excitation in the dynamical system. Third, it computes a velocity-scaled delay matrix from the tract-length data, converting millimeters to milliseconds using a user-specified conduction velocity (often in the range of 1–10 m/s). These delays are critical for reproducing biologically plausible propagation patterns, particularly for [[eeg]], [[meg]], and [[fmri]] forward models where millisecond timing determines phase relationships [[raw/papers/ritter-2013.md|Ritter et al. (2013)]].

Weight normalization is a non-trivial step with substantial dynamical consequences. Over-normalized coupling can suppress the non-linear regime transitions that give rise to realistic [[resting-state]] [[functional-connectivity]] patterns, while under-normalized coupling can push the system into seizure-like hypersynchronization. The module supports multiple normalization strategies—global scaling, regional row normalization, and eigenvalue-based rescaling—allowing modelers to select the approach best suited to their specific neural mass dynamics and the noise characteristics of their tractography pipeline [[raw/papers/jones-2010.md|Jones (2010)]].

## Relationship to TVB

`tvb-diffusion` occupies a foundational position within the broader TVB ecosystem, interfacing directly with three other core modules. It feeds normalized connectivity and delay matrices into [[tvb-library]] for simulation execution, it relies on [[tvb-adapters]] to ingest data from diverse external formats, and its outputs can be inspected and interactively adjusted through the [[tvb-webui]] graphical interface. The automated personalization pipeline described by Schirner and colleagues depends on `tvb-diffusion` as the final transformation stage that converts standard tractography outputs into TVB-ready model configurations, enabling batch construction of personalized virtual brains from large cohorts with minimal manual curation [[raw/papers/schirner-2018.md|Schirner et al. (2018)]].

In the broader landscape of [[whole-brain-modeling]] infrastructure, `tvb-diffusion` fills a role analogous to the [[connectivity]] import modules found in other simulators—but with tighter integration into TVB's surface-based cortical geometry and its explicit handling of region-to-region conduction delays, both features derived from the platform's origins in primate brain [[network-dynamics]] [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Key Features

- **Format-agnostic ingestion**: Accepts connectivity matrices in multiple representations—streamline counts, mean FA, probabilistic weights—from any tractography pipeline that outputs region-pair data.
- **Configurable normalization**: Supports row normalization, global scaling, and eigenvalue rescaling strategies, each suited to different dynamical regimes and noise profiles.
- **Delay matrix computation**: Converts tract lengths into millisecond-scale conduction delays using user-defined propagation velocities.
- **Parcellation remapping**: Handles label reindexing and hemispheric alignment for compatibility with multiple parcellation schemes, including the [[aal-atlas]] and [[desikan-killiany-atlas]].
- **Symmetry enforcement**: Optionally symmetrizes tractography-derived matrices, acknowledging the bidirectionality limitation while ensuring compatibility with models that require symmetric coupling [[raw/papers/jones-2010.md|Jones (2010)]].
- **Interactive adjustment**: When used through the web interface, connectivity weights and delays can be tuned interactively, supporting exploratory analysis of how anatomical variations influence dynamics.

## Caveats and Limitations

The module inherits all the limitations of the tractography data it processes. Streamline count is not synaptic strength, tractography cannot distinguish afferent from efferent projections, and false-positive and false-negative connections propagate directly into the simulated dynamics [[raw/papers/jones-2010.md|Jones (2010)]]. Weight normalization amplifies certain features of the raw connectivity while suppressing others; no single normalization scheme is universally optimal. The module does not perform tractography itself, so downstream results are contingent on the quality of the chosen upstream pipeline—[[mrtrix3]], [[dipy]], or an equivalent toolkit [[raw/papers/schirner-2018.md|Schirner et al. (2018)]].

## Related Software

- [[tvb]] — The overarching platform
- [[tvb-library]] — Simulation kernel that consumes the module's outputs
- [[tvb-adapters]] — Interoperability layer that feeds external data into the pipeline
- [[tvb-webui]] — Graphical interface for interactive connectivity adjustment
- [[mrtrix3]] — Comprehensive tractography and connectome construction toolkit
- [[dipy]] — Python library for diffusion MRI analysis and tractography
- [[connectome-mapper-3]] — End-to-end connectome reconstruction pipeline

## Related Concepts

- [[diffusion-mri]] — The imaging modality providing the raw data
- [[dti]] — Diffusion tensor imaging, the foundational reconstruction method [[raw/papers/basser-1994.md|Basser et al. (1994)]]
- [[tractography]] — Fiber tracking algorithms pioneered by [[raw/papers/mori-1999.md|Mori et al. (1999)]]
- [[structural-connectivity]] — The anatomical wiring that constrains models
- [[connectome]] — Complete brain connectivity map
- [[white-matter]] — Myelinated axonal fiber tracts
- [[parcellation]] — Regional brain subdivision schemes
- [[fractional-anisotropy]] — Scalar measure of diffusion directionality
- [[neural-mass-models]] — Population-level dynamics that consume the connectivity
- [[personalized-brain-modeling]] — Subject-specific model construction
- [[functional-connectivity]] — Empirical and simulated correlation patterns
- [[resting-state]] — Spontaneous brain activity regime

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal [[neuroimaging]]*. Brain Connectivity. [DOI](](https://doi.org/10.1089/brain.2012.0120))
3. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](](https://doi.org/10.1016/j.neuroimage.2018.05.040))
4. (authors unknown). *MR diffusion tensor spectroscopy and imaging*.
5. (authors unknown). *Three-dimensional tracking of axonal projections in the brain by magnetic resonance imaging*.
6. (authors unknown). *Challenges and limitations of quantifying brain connectivity in vivo with diffusion MRI*.