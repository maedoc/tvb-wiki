---
created: 2026-04-27
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/breakspear-2017.md
tags:
- the-virtual-brain
title: The Virtual Brain
type: concept
updated: '2026-05-07'
---

[[tvb|The Virtual Brain]] (TVB) is an open-source neuroinformatics platform for simulating large-scale primate brain [[network-dynamics]]. It enables researchers to construct personalized [[whole-brain]] models by combining empirical structural [[connectivity]] data—typically derived from [[diffusion-mri]] [[tractography]]—with biologically realistic [[neural-mass-models]]. TVB provides forward models for electroencephalography (EEG), magnetoencephalography (MEG), and functional magnetic resonance imaging (fMRI), allowing simulated brain activity to be compared directly against empirical [[neuroimaging]] recordings. The platform has become a cornerstone tool in [[computational-neuroscience]] for studying [[brain-dynamics]], disease mechanisms, and individualized virtual brain models (Sanz Leon et al., 2013).

## Motivation and Historical Context

Contemporary brain function is understood to emerge from the interaction of large numbers of neurons across multiple spatial and temporal scales. While traditional neural simulations focus on the microscopic level (individual neurons and synapses) or mesoscopic level (neural masses representing cortical columns), these approaches often lose perspective on the global dynamics of the entire brain. Simultaneously, the assessment of global cortical dynamics across imaging modalities—in human patients and research subjects—has expanded dramatically over recent decades. There existed a strong need for an efficient, flexible platform capable of simulating macroscopic brain dynamics at the whole-brain scale, enabling researchers to integrate diverse neuroimaging data streams and explore the mechanistic basis of brain function and dysfunction (Breakspear, 2017).

The Virtual Brain emerged to address this gap. Developed by an international consortium led by [[viktor-jirsa]] and collaborators, TVB represents a paradigm shift from small-scale neural modeling to whole-[[brain-network]] simulation (Sanz Leon et al., 2013). The platform was designed to bridge the gap between computational modelers and clinical researchers, providing a unified environment where neuroimaging data could be transformed into personalized computational models capable of reproducing individual patterns of brain activity.

## Platform Architecture

TVB employs a modular architecture that separates scientific computation from user interaction. At its core lies the simulation engine, written in Python, which solves large systems of coupled differential equations representing the dynamics of interconnected brain regions. Each region is modeled using a neural mass model—typically variants of the [[jansen-rit-model]] ([[jansen-rit]]) or the [[epileptor]] model for epilepsy studies—which captures the average activity of neuronal populations within that region (Sanz Leon et al., 2013).

The structural connectivity matrix, derived from diffusion tensor imaging (DTI) or high-angular-resolution [[diffusion-imaging]] (HARDI) tractography, defines the coupling between regions (Ritter et al., 2013). This matrix represents the density and strength of [[white-matter]] tracts connecting different brain areas, providing the anatomical skeleton upon which dynamic activity unfolds. Time delays arising from finite conduction velocities are explicitly modeled, creating the characteristic wave-like patterns of brain activity observed in empirical data.

TVB provides multiple user interfaces to accommodate different use cases. A web-based HTML5/JavaScript interface with WebGL visualization enables remote access through a client-server configuration, allowing users to run simulations without local installation. For advanced modeling and customization, a Python scripting interface provides direct access to the scientific kernel, enabling integration with other libraries in the Python scientific ecosystem.

## Forward Modeling and Data Integration

One of TVB's key strengths lies in its ability to generate synthetic neuroimaging signals from underlying neural dynamics. The forward modeling pipeline transforms region-level neural activity into observable signals corresponding to different modalities. For [[neuroimaging-eeg]] and [[neuroimaging-meg]], the platform implements volume conduction models that account for the conductive properties of the head tissue to compute scalp potentials and magnetic fields. For [[neuroimaging-fmri]], a hemodynamic model—typically based on the Balloon model—transforms the fast neural dynamics into the slower blood-oxygen-level-dependent (BOLD) signal measured by fMRI (Ritter et al., 2013).

This multimodal forward modeling capability enables direct comparison between simulated and empirical data. Researchers can fit model parameters to individual subject data by minimizing the discrepancy between simulated and observed [[functional-connectivity]] patterns, [[resting-state]] networks, or event-related responses (Ritter et al., 2013). This personalization framework has proven particularly valuable for clinical applications, where individual variations in brain structure may underlie differences in disease progression and treatment response.

## Relationship to Other Tools

TVB occupies a unique position in the ecosystem of neural simulation software. Unlike [[brian]] or [[brian2]], which focus on detailed single-neuron and small-network simulations, or [[nest]] and [[neuron]], which emphasize large-scale spiking network simulations, TVB operates at the macroscopic whole-brain level using neural mass approximations. This abstraction enables simulation of the entire brain at tractable computational cost while retaining biologically meaningful dynamics.

TVB complements [[dynamic-causal-modeling]] (DCM) approaches, which also integrate neuroimaging data with computational models but typically operate on much smaller sets of regions (10–50) using [[variational-bayes]] inference. TVB's whole-brain approach enables exploration of network-level phenomena such as [[brain-oscillations]], criticality, and traveling waves that emerge from the interaction of distributed brain regions (Breakspear, 2017).

The platform integrates with data management tools such as [[datalad]] and the broader [[bids]] ecosystem for handling neuroimaging datasets. For visualization, TVB interfaces with tools like [[brainnet-viewer]] and the [[brain-connectivity-toolbox]] to enable rich display of connectivity matrices and simulation results. TVB also works well with preprocessing pipelines from [[Brainsuite]] for cortical surface analysis, and can be deployed within containerized environments via [[datalad-containers]] for reproducible workflows (Sanz Leon et al., 2013).

## Applications and Clinical Translation

TVB has been applied extensively in computational psychiatry and neurology research. Personalized whole-brain models have been used to study [[epilepsy-modeling]], where the [[epileptor]] model can capture seizure dynamics and evaluate stimulation interventions. The platform supports investigation of [[schizophrenia-models]] and [[alzheimers-modeling]] by exploring how structural connectivity alterations propagate through large-scale networks to produce functional abnormalities.

The [[personalized-brain-modeling]] framework enables the construction of virtual patient models from individual neuroimaging data. This approach holds promise for clinical translation, potentially allowing clinicians to simulate the effects of stimulation interventions (e.g., transcranial magnetic stimulation or deep brain stimulation) before surgical planning, or to predict disease progression based on individual connectome profiles. By combining [[structural-connectivity]] information with dynamic models, TVB provides a mechanistic bridge between anatomical structure and functional dynamics that is essential for understanding both healthy brain function and the pathophysiology of neurological disorders. Integration with clinical platforms such as [[clinica]] enables seamless processing of clinical neuroimaging data into TVB-compatible formats.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
3. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4)