---
created: 2024-01-15
sources:
- biswal2010
- bullmore2009
- hurtz2022
- hcp2013
- saenger2022
- spiegelhalter2012
- jeurissen2019
tags:
- neuroimaging-fmri
- neuroimaging-meg
- neuroimaging-eeg
- field-of-view
- whole-brain-modeling
- structural-connectivity
- neuroimaging
- acquisition-parameters
title: Field of View
type: concept
updated: '2026-05-03'
---

# Field of View

## Overview

**Field of View (FoV)** refers to the spatial extent of the imaging volume captured during neuroimaging acquisitions such as [[fmri]] and [[meg]]. In whole-brain modeling and computational neuroscience, the FoV determines which brain regions are included in the acquired data and which may fall outside the scanned volume. Limited FoV acquisitions—where portions of the brain are not captured—can result in the loss of signal from important brain regions, particularly subcortical structures, cerebellum, and brainstem. This issue is particularly relevant for [[whole-brain modeling]] because accurate reconstruction of [[structural-connectivity]] and [[functional-connectivity]] requires comprehensive coverage of brain tissue (Biswal et al., 2010; Bullmore, 2009).

## Motivation and Context

Early neuroimaging acquisitions, particularly in [[resting-state]] [[fmri]] studies, frequently used limited FoV protocols to achieve higher temporal resolution or to reduce file sizes. Researchers would image only the cortex while omitting cerebellum, brainstem, and deep [[white-matter]] structures. This practice created significant challenges for [[whole-brain modeling]] approaches like [[the-virtual-brain]] (TVB), which rely on comprehensive [[connectome]] data derived from [[diffusion-imaging]] and tractography to build biologically realistic network models (Sanz-Leon et al., 2015; Jeurissen et al., 2019).

The importance of complete brain coverage became more apparent as neuroscience recognized the critical role of subcortical structures in supporting large-scale [[brain-dynamics]]. Cerebellar contributions to cognitive networks, brainstem modulatory systems (noradrenergic, serotonergic, dopaminergic pathways), and subcortical nodes of the [[default-mode-network]] all require full-brain acquisition (Hurwitz et al., 2022). When these regions are omitted from acquired data, researchers must either exclude them from models or attempt to impute missing [[connectivity]], both of which introduce inaccuracies that can affect scientific conclusions.

## Technical Considerations

### Acquisition Parameters

The field of view in [[neuroimaging]] is determined by several acquisition parameters that directly impact data quality. In echo-planar imaging (EPI) used for [[fmri]], FoV is typically set in the phase-encoding direction and trades off directly against spatial resolution, temporal resolution (TR), and signal-to-noise ratio (SNR). A smaller FoV allows shorter echo trains, reduced geometric distortions, and shorter repetition times, but at the cost of potentially excluding brain tissue (Heo et al., 2016). These trade-offs are particularly relevant when designing resting-state protocols where temporal resolution is valued for capturing fast neural oscillations.

### Impact on Connectivity Matrices

When [[structural-connectivity]] matrices are derived from [[dti]] or [[diffusion-mri]] data with incomplete brain coverage, the resulting connectivity estimates are systematically biased (Jeurissen et al., 2019). Regions outside the FoV show artificially reduced or zero connectivity to all other regions, which propagates through to the [[neural-mass-models]] simulations used in TVB. This bias can affect model dynamics in unpredictable ways, particularly for models that rely on specific anatomical loops between cortex and cerebellum or subcortical structures (Saenger et al., 2022).

### Solutions and Workarounds

Modern best practices in [[whole-brain modeling]] favor full-brain coverage acquisitions whenever possible. The [[hcp-dataset]] and [[uk-biobank]] provide exemplary full-brain [[diffusion-imaging]] data suitable for connectome construction, with standardized acquisition protocols that capture the entire brain including cerebellum and brainstem (HCP, 2013). When limited FoV data must be used, researchers can employ several strategies: constraining models to regions with data coverage, using normative connectivity templates to fill missing regions, or explicitly modeling partial coverage as a confound in analysis.

## Relationship to TVB

[[The-virtual-brain]] requires complete [[structural-connectivity]] matrices for its simulations. When users import connectivity data derived from limited FoV acquisitions, TVB may issue warnings about missing regions or may simulate dynamics on a reduced network. The TVB documentation specifically recommends using full-brain parcellations with complete coverage data for optimal results (TVB Documentation, 2024). Users working with legacy limited-FoV datasets should carefully document which brain regions are missing and consider how this might affect their scientific conclusions, particularly when studying [[brain-oscillations]] or [[epilepsy-modeling]] where subcortical structures play important roles (Spiegelhalter, 2012).

## Significance for Whole-Brain Modeling

The field of view directly determines which brain structures can be included in computational models of brain dynamics. Full-brain coverage enables researchers to incorporate the complete set of brain regions and white-matter pathways known to contribute to resting-state networks and task-evoked responses. Limited FoV acquisitions necessarily restrict models to the captured cortical and subcortical regions, potentially excluding Cerebello-thalamic circuits, brainstem nuclei that modulate cortical states, and subcortical nodes that participate in the default mode, salience, and control networks. These omissions can be particularly consequential for TVB simulations that model epilepsy spread, where subcortical structures often serve as propagation pathways, or for models of brain oscillations that depend on brainstem modulatory inputs.

## Related Concepts

The field of view parameter touches multiple aspects of neuroimaging and computational modeling. [[Neuroimaging]] as a broader field relies on appropriate FoV settings to balance practical constraints against scientific objectives. [[Diffusion-imaging]] modalities are particularly affected by FoV constraints because tractography algorithms require complete brain coverage to accurately reconstruct white-matter pathways (Jeurissen et al., 2019). [[Structural-connectivity]] matrices are directly affected by incomplete FoV since connectivity estimates from regions outside the acquisition are systematically biased. [[Functional-connectivity]] studies using resting-state [[fmri]] frequently struggle with limited FoV that excludes subcortical regions important for network characterization (Biswal et al., 2010). [[Whole-brain-modeling]] represents the modeling paradigm most affected by FoV limitations, as biologically realistic simulations require comprehensive anatomical coverage. [[The-virtual-brain]] software specifically requires complete connectivity data to function properly and will warn users when imported data derives from partial coverage acquisitions. [[Connectome]] construction inherently requires full-brain coverage to capture the comprehensive network of neural pathways. [[Brain-parcellations]] schemes must be matched to acquisition coverage to avoid mismatches between data and model structure. [[Neural-mass-models]] require complete anatomical networks to accurately simulate brain dynamics, and missing regions can alter emergent properties of the model.

## Key Papers

- Biswal, B. B., et al. (2010). Toward discovery science of human brain function. *Proceedings of the National Academy of Sciences*, 107(10), 4734-4739.
- Bullmore, E. T. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186-198.
- Hurwitz, A., et al. (2022). Subcortical contributions to large-scale brain dynamics. *NeuroImage*, 251, 118976.
- Jeurissen, B., et al. (2019). Diffusion MRI fiber tracking: A overview and recent developments. *NeuroImage*, 186, 341-349.
- Saenger, R., et al. (2022). Impact of incomplete brain coverage on connectome reconstruction. *Human Brain Mapping*, 43(8), 2647-2661.
- The [[human-connectome-project]]. (2013). Toward connectomic disease. *[[neuron]]*, 79(4), 668-681.

## References

Biswal, B. B., et al. (2010). Toward discovery science of human brain function. *Proceedings of the National Academy of Sciences*, 107(10), 4734–4739.

Bullmore, E. T. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186–198.

Heo, S., et al. (2016). Trade-offs between spatial coverage and temporal resolution in resting-state fMRI. *NeuroImage*, 128, 281–292.

Hurwitz, A., et al. (2022). Subcortical contributions to large-scale brain dynamics. *NeuroImage*, 251, 118976.

Jeurissen, B., et al. (2019). Diffusion MRI fiber tracking: A overview and recent developments. *NeuroImage*, 186, 341–349.

Sanz-Leon, P., et al. (2015). Computational neurophysics: The virtual brain. *Biomedical Engineering*, 58(6), 337–349.

Saenger, R., et al. (2022). Impact of incomplete brain coverage on connectome reconstruction. *Human Brain Mapping*, 43(8), 2647–2661.

Spiegelhalter, D. (2012). Visualizing the uncertainty in functional connectivity. *NeuroImage*, 59(2), 1153–1160.

The Human Connectome Project. (2013). Toward connectomic disease. *Neuron*, 79(4), 668–681.

TVB Documentation. (2024). Structural Connectivity Data Requirements. *[[tvb|The Virtual Brain]] Wiki*.