---
title: Demois
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-tvb, whole-brain-modeling, computational-neuroscience]
sources: [tvb-documentation-2024, tvb-paper-2013, tvb-paper-2022]
---

# Demois

## Overview

**Note:** The entity "Demois" as a standalone demonstration and validation framework within The Virtual Brain (TVB) ecosystem cannot be verified through available documentation, codebase repositories, or official TVB resources. Searches of the TVB documentation, GitHub repositories, and related resources yield no results for a component named "Demois." The TVB ecosystem does include demonstration resources including GUI Demos, Python/IPython Notebook tutorials, and MATLAB demos for showcasing simulation capabilities. The following description reflects what demonstration frameworks in the TVB ecosystem generally provide, based on available evidence.

Demonstration and validation frameworks within The Virtual Brain (TVB) ecosystem serve as essential utilities for showcasing whole-brain computational model capabilities, comparing simulated brain dynamics against empirical neuroimaging data, and supporting reproducible research practices. These frameworks play a crucial role in bridging the gap between theoretical models and experimental observations, enabling researchers to assess the biological plausibility of their simulations.

The development of demonstration and validation tools reflects a broader trend in computational neuroscience toward reproducible research and rigorous model validation[^1]. As whole-brain simulators such as TVB have become increasingly sophisticated, the need for standardized frameworks to showcase model capabilities and verify their outputs against ground-truth data has grown substantially.

## Relationship to TVB

TVB's demonstration resources operate as affiliated components within the TVB software ecosystem, complementing the core simulation engine with dedicated demonstration, validation, and educational utilities. Unlike the main TVB simulator which focuses on executing large-scale brain network models, demonstration frameworks specialize in presenting curated workflows that showcase specific modeling capabilities, validation pipelines, and clinical use cases.

The relationship between TVB's demonstration resources and the core simulator is complementary: demonstration content depends on the TVB simulation kernel for generating brain dynamics but provides additional layers of functionality focused on presentation, validation, and pedagogy. Users can access demonstration workflows directly through TVB's graphical interface, where the distinction between demonstration content and production simulation is seamlessly integrated[^3].

Demonstration resources also contribute to TVB's educational mission by providing reproducible examples that new users can modify and explore. These demonstrations typically include pre-configured connectivity matrices, neural mass models, and parameter sets that produce biologically or clinically meaningful dynamics, such as seizure propagation patterns or resting-state networks[^4].

## Key Features

TVB's demonstration and validation frameworks incorporate several key features designed to support model verification and educational outreach. First, they provide curated example simulations that cover the primary use cases of whole-brain modeling, including epilepsy modeling, stroke recovery prediction, brain stimulation planning, and resting-state dynamics. Each example includes not only the simulation configuration but also explanations of the underlying neuroscience, modeling assumptions, and interpretation guidelines[^4].

Second, these frameworks include validation utilities that compare simulation outputs against empirical data. This may involve computing metrics such as functional connectivity matrices, seizure onset times, or spectral properties of modeled brain activity, and comparing them against corresponding metrics derived from patient-specific neuroimaging data. Such validation workflows are essential for assessing the predictive accuracy of personalized brain models and are increasingly required for clinical translation efforts[^2].

Third, demonstration platforms provide interactive visualization capabilities that allow users to explore simulation results through TVB's web-based interface or exported data formats. These visualizations may include 3D brain renderings showing seizure propagation, time-series displays of regional activity, and statistical summaries of simulation outputs.

## Technical Implementation

From a technical perspective, demonstration frameworks within the TVB ecosystem are implemented as collections of standardized simulation configurations, datasets, and analysis pipelines. These resources are distributed through TVB's data repository (Zenodo) and documentation site, allowing users to download examples and run them locally using their own TVB installation.

The simulation configurations follow TVB's standard format, incorporating:
- Connectivity matrices (often derived from databases like the Human Connectome Project)
- Neural mass model selections (such as the Epileptor for epilepsy modeling or the Reduced Wong-Wang model for resting-state dynamics)
- Appropriate monitor settings for generating the desired output modalities

The validation components leverage TVB's analysis toolkit, which includes functions for computing functional connectivity from simulated time series, analyzing spectral properties, and quantifying spatio-temporal dynamics. These analyses can be compared against empirical data using standard metrics, supporting both qualitative assessment (visual comparison of propagation patterns) and quantitative validation (statistical comparison of connectivity matrices).

## See Also

- [[the-virtual-brain]] — Core whole-brain simulation engine
- [[tvb-library]] — TVB's scientific library for custom model development
- [[epileptor]] — Neural mass model commonly used in demonstration workflows
- [[whole-brain-modeling]] — Field that demonstration platforms support
- [[neural-mass-models]] — Local dynamics models used in demonstrations
- [[structural-connectivity]] — Anatomical connectivity that constrains large-scale dynamics
- [[functional-connectivity]] — Dynamic correlation patterns that demonstrations validate
- [[hcp-dataset]] — Source of empirical connectivity data for demonstrations

## References

[^1]: Sanz Leon, P., Knock, S.A., Woodman, M.M., Domide, L., Mersmann, J., McIntosh, A.R., & Jirsa, V. (2013). The Virtual Brain: a simulator of primate brain network dynamics. Frontiers in Neuroinformatics, 7:10. https://doi.org/10.3389/fninf.2013.00010

[^2]: Schirner, M., Domide, L., et al. (2022). Brain simulation as a cloud service: The Virtual Brain on EBRAINS. NeuroImage. https://doi.org/10.1016/j.neuroimage.2022.118973

[^3]: The Virtual Brain Documentation. (2024). GUI Demos. http://docs.thevirtualbrain.org/demos/Demos.html

[^4]: The Virtual Brain Documentation. (2024). Building Your Own Brain Network Model Tutorial. http://docs.thevirtualbrain.org/tutorials/tutorial_1_BuildingYourOwnBrainNetworkModel.html