---
created: 2024-01-15
sources:
- raw/papers/ritter-2013.md
- raw/papers/schirner-2018.md
- raw/papers/arxiv-2603.07524.md
- raw/papers/sanz-leon-2013.md
- raw/papers/woodman-2014.md
- raw/papers/arxiv-2506.21155.md
tags:
- personalized-brain-modeling
- whole-brain-modeling
- neural-mass-models
- structural-connectivity
- functional-connectivity
- software-tvb
- neuroimaging-dti
- neuroimaging-fmri
- neuroimaging-eeg
- epilepsy-modeling
- brain-stimulation
- personalized-brain-modeling
title: Personalized Brain Modeling
type: concept
updated: '2026-05-07'
---

Personalized brain modeling (also termed patient-specific brain modeling or virtual brain建模) refers to the construction of subject-specific computational brain models that are parameterized by an individual's unique [[neuroimaging]] data. Unlike generic brain models that represent average anatomical and functional patterns across a population, personalized models capture the distinctive structural architecture and dynamics of a specific individual—including their unique [[white-matter]] pathways, cortical [[parcellation]], and characteristic neural rhythms. This individualization enables clinically relevant simulations that can predict disease progression, treatment outcomes, and personalized neuromodulation protocols with significantly higher fidelity than population-level models.

## Motivation and Clinical Context

The motivation for personalized brain modeling emerges from a fundamental limitation of population-average approaches in clinical neuroscience: the high degree of inter-subject variability in brain anatomy, [[connectivity]], and dynamics. While group-level studies have successfully identified canonical brain networks and biomarkers, they often fail to capture the idiosyncratic features that determine an individual patient's disease [[trajectory]] or treatment response. For example, the pattern of seizure propagation in [[epilepsy-modeling]] depends critically on the specific white matter pathways connecting epileptogenic zones to downstream regions—pathways that vary substantially across individuals and cannot be adequately represented by a template brain.

Personalized brain modeling addresses this problem by transforming individual neuroimaging data into computational model parameters, creating a "digital twin" of the patient's brain that can be simulated in silico. This approach draws on the theoretical framework of [[whole-brain modeling]], which represents the brain as a network of coupled [[neural-mass-model]]s connected by empirical structural connectivity matrices derived from [[diffusion-mri]] tractography. By parameterizing these models with subject-specific data, researchers can generate predictions that account for individual anatomical differences—something thatpurely data-driven analyses of functional neuroimaging cannot achieve without mechanistic modeling.

The clinical imperative is particularly strong in epilepsy, where surgical resection or neuromodulation (e.g., [[brain-stimulation]] via implanted electrodes) requires precise localization of epileptogenic tissue and prediction of postsurgical outcomes. Personalized models allow surgeons to simulate the effects of tissue removal or stimulation before intervention, potentially reducing the risk of unexpected functional deficits. Similar arguments apply to [[brain-stimulation]] protocols for Parkinson's disease, depression, and other disorders where individualized targeting is critical.

## Data Sources and Acquisition

A robust personalized brain modeling pipeline requires multimodal neuroimaging data that capture different aspects of brain structure and function. The primary data sources include:

**Structural MRI** provides the anatomical reference from which cortical and subcortical parcellation is performed. High-resolution T1-weighted images (typically 1 mm isotropic resolution) are used to define the boundaries of brain regions that will serve as nodes in the whole-brain network model. Various atlases—such as [[desikan-killiany-atlas]], [[aal-atlas]], or [[brainnetome-atlas]]—can be used to partition the cortex into anatomically and functionally coherent regions of interest.

**Diffusion-weighted MRI** enables reconstruction of white matter pathways through [[tractography]], yielding the structural connectivity matrix that defines the coupling strength between brain regions. These matrices encode the number or density of tractographic streamlines connecting each pair of regions, providing the anatomical scaffold that constrains model dynamics. The quality of the connectivity matrix depends critically on acquisition parameters (e.g., b-value, number of diffusion directions) and preprocessing Steps (e.g., eddy-current correction, orientation distribution function estimation).

**Functional neuroimaging**—whether [[fmri]] measured at rest ([[resting-state]]) or during task performance, or [[eeg]]/[[meg]] providing high temporal resolution of electromagnetic activity—serves as validation targets for model calibration. The simulated activity generated by the personalized model should reproduce empirically observed functional connectivity patterns, ensuring that the model captures meaningful dynamics rather than artifacts.

## Pipeline and Methodology

The construction of a personalized brain model proceeds through a well-defined sequence of preprocessing and simulation steps, each of which introduces specific methodological considerations:

1. **[[brain-parcellation]]**: The cortical surface is partitioned into between 32 and 200 regions depending on the spatial scale of the model. This step can use anatomical landmarks, functional connectivity parcellations, or hybrid approaches that combine both. The choice of parcellation resolution involves a tradeoff between computational tractability and biological specificity.

2. **Tractography and connectivity estimation**: Fiber tracking algorithms applied to diffusion-weighted data reconstruct streamlines representing white matter pathways. These streamlines are mapped onto the parcellation to produce a weighted connectivity matrix, where each entry represents the number of streamlines, [[fractional-anisotropy]], or other metrics of structural coupling between region pairs. Software packages such as [[mrtrix3]], [[dipy]], or [[dsi-studio]] are commonly used for tractography.

3. **Model parameterization**: Each brain region is equipped with a [[neural-mass-model]] that captures the collective dynamics of neurons in that region. Popular choices include the [[jansen-rit]] model (a neural mass model originally developed for EEG generation), the [[wong-wang]] model (a excitatory-inhibitory population model useful for simulating resting-state fMRI), or the [[epileptor]] model (specifically designed for seizures in epilepsy modeling). The structural connectivity matrix defines the coupling strengths between these regional models.

4. **Simulation and validation**: The parameterized model is simulated to generate predicted brain activity—either [[bold-signal|BOLD]] signals compatible with fMRI or electrophysiological signals compatible with EEG. These simulated signals are compared to empirical functional connectivity matrices derived from the individual's actual neuroimaging data. Parameter optimization (e.g., via gradient descent or evolutionary algorithms) may be employed to minimize the discrepancy between simulated and empirical functional connectivity.

5. **Clinical application**: Once validated, the personalized model can be used for predictive simulations—such as computing seizure propagation patterns in epilepsy, predicting effects of virtual lesions in stroke, or optimizing stimulation electrode placements for deep brain stimulation.

## Key Platforms and Tools

Several software platforms have been developed specifically to support personalized brain modeling workflows:

[[TVB]] (The Virtual Brain) is the most widely used open-source platform for [[whole-brain]] simulation and personalized modeling. TVB provides an integrated environment for data import, connectivity matrix construction, neural mass model selection, parameter optimization, and simulation. It supports multiple [[neural-mass-models]] (including Jansen-Rit, Wong-Wang, and Epileptor) and can generate both fMRI and EEG-compatible outputs. The platform includes a graphical user interface for interactive exploration as well as a Python API for programmatic workflows.

[[ANTs]] (Advanced Normalization Tools) is essential for image registration and preprocessing—particularly for aligning individual anatomical scans to template spaces and performing skull-stripping. ANTs provides sophisticated diffeomorphic registration algorithms that are considered current for neuroimaging preprocessing.

[[GraphVar]] is a MATLAB-based toolbox for graph-theoretic analysis of brain connectivity networks. While not a simulation platform itself, GraphVar provides the connectivity analysis tools needed for validating personalized models by comparing simulated and empirical network metrics (e.g., [[modularity]], [[rich-club]] coefficients, small-world properties).

Additional tools commonly used in personalized modeling pipelines include [[freesurfer]] for cortical parcellation, [[mrtrix3-connectome]] for tractography-based connectivity estimation, and [[nipype]] for workflow orchestration.

## Applications

Personalized brain modeling has found application across a range of clinical and research contexts:

**Epilepsy modeling** represents the most mature clinical application, where personalized models are used to identify seizure onset zones, predict ictal propagation patterns, and guide surgical planning. The [[epileptor]] model within TVB is specifically designed for this purpose, and several studies have demonstrated that personalized models can predict postsurgical seizure freedom with reasonable accuracy.

**Stroke and brain injury** modeling uses personalized models to predict patterns of functional reorganization following focal brain damage. By virtually lesioning specific regions in the model and simulating recovery dynamics, researchers can explore which compensatory pathways might support functional restoration.

**Neurodegenerative disorders** such as [[alzheimers-disease|Alzheimer's disease]] can be modeled by parameterizing model dynamics to reproduce the altered functional connectivity patterns observed in patients. While the pathophysiology of neurodegeneration involves pathological protein accumulation that cannot be fully captured by current neural mass models, personalized models can still provide insight into how [[network-dynamics]] are perturbed by tissue loss.

**Neuromodulation optimization** uses personalized models to simulate the effects of transcranial magnetic stimulation, transcranial direct current stimulation, or implanted electrode stimulation. By modeling the electric field distribution and its effects on neural dynamics, clinicians can optimize stimulation parameters (e.g., frequency, intensity, electrode placement) for individual patients.

**[[aging|Brain aging]]** research leverages personalized models to understand how structural connectivity changes across the lifespan affect functional dynamics. By connecting personalized models to empirical data from the [[uk-biobank]] or [[human-connectome-project]] datasets, researchers can investigate how normal aging alters [[brain-network]] dynamics and what factors predict maintenance or decline.

## Emerging Methods and Future Directions

Recent advances in [[machine-learning]] have begun to influence personalized brain modeling, particularly through deep learning approaches that can learn personalized representations directly from functional data. The Neural Dynamics-Informed Pre-trained Framework proposed by Jiang et al. (arxiv-2603.07524) represents a notable step in this direction, using [[neural-network]] architectures that embed inductive biases about [[brain-dynamics]] to construct personalized functional networks without relying on predefined atlases.

Another frontier is the development of amortized personalization methods that can generate personalized models more efficiently by learning a mapping from empirical data to model parameters through a single forward pass, rather than requiring lengthy optimization procedures. Such approaches could make personalized modeling feasible for large cohort studies or real-time clinical applications.

The integration of [[effective-connectivity]] methods—such as [[dynamic-causal-modeling]]—with whole-brain simulation represents another opportunity for advancing the field, as it would allow models to capture not just correlation patterns but causal dynamical relationships between brain regions.

## Related Concepts

- [[whole-brain modeling]] — The broader framework of which personalized modeling is a part
- [[structural connectivity]] — The anatomical connectivity matrices derived from diffusion MRI
- [[functional connectivity]] — The statistical dependencies between regional time series used for [[model-validation]]
- [[neural-mass-model]] — The regionaldynamical models that form the nodes of whole-brain networks
- [[epilepsy-modeling]] — The primary clinical application of personalized brain models
- [[brain-stimulation]] — Clinical domain where personalized models optimize neuromodulation
- [[TVB]] — Primary software platform for personalized brain simulation
- [[resting-state]] — The empirical functional patterns commonly used for model validation
- [[fmri-vs-eeg|Fmri Vs Eeg]]

## References

1. Ritter et al. (2013). *[[the-virtual-brain]] integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](](https://doi.org/10.1089/brain.2012.0120))
2. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](](https://doi.org/10.1016/j.neuroimage.2018.05.040))
3. Hongjie Jiang, Yifei Tang, Shuqiang Wang. *Neural Dynamics-Informed Pre-trained Framework for Personalized Brain Functional Network Construction*. [Link](](https://arxiv.org/abs/2603.07524))
4. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
5. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))
6. Nina Baldy, Marmaduke M Woodman, Viktor K Jirsa. (2025). *Amortizing personalization in virtual brain twins*. [Link](](https://arxiv.org/abs/2506.21155))