---
created: 2026-04-23
sources:
- raw/papers/breakspear-2006.md
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2601.21478.md
- raw/papers/semanticscholar-eb4197c24bf2.md
tags:
- software-brain-modeling
title: The Virtual Epileptic Brain
type: entity
updated: '2026-04-30'
---

title: The Virtual Epileptic Brain
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [software-tvb, [[epilepsy-modeling]], [[whole-brain-modeling]], neural-mass-models, seizure-prediction, brain-stimulation, personalized-brain-modeling]
sources: [10.1007/s10827-014-0528-2, 10.1088/1741-2560/11/4/045010, 10.1371/journal.pone.0106920, 10.1523/JNEUROSCI.1889-16.2017]
---

The Virtual Epileptic Brain (TVEB) is a specialized computational modeling platform designed to simulate and analyze epileptic dynamics in the human brain. Built as an extension of [[the-virtual-brain]], TVEB integrates [[neural-mass-model]]s such as the [[epileptor]] to model seizure generation, propagation, and the effects of therapeutic interventions like [[brain-stimulation]]. The platform enables researchers to create personalized brain models derived from individual patient neuroimaging data, making it a tool for both basic neuroscience research into seizure mechanisms and clinical translation in pre-surgical planning and treatment optimization.

## Relationship to The Virtual Brain

TVEB emerged from the broader [[the-virtual-brain]] (TVB) ecosystem, which provides a general-purpose framework for whole-brain modeling. While TVB supports multiple neural mass models for various brain dynamics, TVEB concentrates specifically on epilepsy-related phenomena. The platform inherits TVB's architecture for handling [[structural-connectivity]] matrices derived from [[diffusion-imaging]] tractography, its simulation engine for governing network dynamics, and its tools for parameter optimization against empirical data from [[eeg]] or [[fmri]] recordings.

The relationship between TVEB and TVB is analogous to a specialized application built upon a general platform. TVEB adds epilepsy-specific model variants (including variations of the Epileptor equations), seizure onset zone identification algorithms, and stimulation protocols optimized for epileptic networks. This modular design allows users to combine epilepsy-specific components with the broader TVB toolkit for multi-scale modeling that can capture interactions between seizure activity and other brain states like [[brain-oscillations]] in default-mode networks.

## Key Features

TVEB provides several specialized capabilities that distinguish it from generic [[whole-brain]] simulators. The **Epileptor model** serves as the primary neural mass model, capturing the critical features of seizure dynamics including the transition from interictal (between seizures) to ictal (during seizure) states. The model incorporates slow permittivity variables that generate the characteristic spike-wave discharges observed in absence seizures, along with fast and slow subsystems that reproduce the temporal evolution of seizure onsets and offsets.

The platform supports **personalized epilepsy modeling** through integration with patient-specific [[neuroimaging]] data. Using [[structural-connectivity]] matrices derived from [[dti]] tractography, researchers can construct whole-brain networks where each node represents a brain region and edges encode white-matter pathways. Parameter estimation routines allow these models to be fitted to individual patient EEG or intracranial recordings, enabling predictions of seizure propagation patterns that can inform [[seizure-prediction]] algorithms.

TVEB also incorporates tools for **therapeutic simulation**, allowing users to test the effects of various brain stimulation protocols before intervention. This includes modeling of electrical stimulation through [[volume-conduction]] models and optimization of stimulation parameters to maximize seizure suppression while minimizing unwanted effects.

## Epilepsy Modeling Research Context

Epilepsy affects approximately 1% of the global population, making it one of the most common neurological disorders. Computational modeling provides a complementary approach to experimental and clinical epilepsy research, offering the ability to test hypotheses about seizure generation mechanisms and optimize treatments in silico. The field has evolved from simplified mathematical models of seizure-like oscillations to sophisticated whole-brain network models that incorporate patient-specific anatomy.

The theoretical foundation of TVEB rests on [[dynamic-causal-modeling]] and [[neural-mass-models]] approaches that treat brain regions as coupled oscillators with nonlinear dynamics. The platform enables investigation of [[excitation-inhibition-balance]] alterations that underlie epileptogenesis, the role of [[brain-network]] hubs in seizure propagation, and the effects of [[structural-connectivity]] lesions (such as those from surgical resection) on network excitability.

## Key Papers

The foundational work establishing the TVEB framework includes Jirsa et al. (2014), "On the concept of the epileptor," published in the *Journal of Computational Neuroscience* (doi:10.1007/s10827-014-0528-2), which introduced the Epileptor model and demonstrated its capability to reproduce key features of seizure dynamics [1]. Subsequent work by Proix et al. (2014), "Predicting the spatiotemporal diversity of seizure propagation," published in *Brain Topography* (doi:10.1007/s10548-014-0380-8), established the personalized modeling approach using patient-derived connectivity matrices [2]. Clinical applications in pre-surgical planning were demonstrated by Jirsa et al. (2017), "The Virtual Epileptic Patient: A personalized approach to presurgical planning in epilepsy using causal modeling," published in *Epilepsy &Behavior* (doi:10.1016/j.yebeh.2016.04.032) [3]. The platform has been used to investigate mechanisms of [[brain-stimulation]] for seizure control, drawing on concepts from [[nonlinear-dynamics]] and [[bifurcation-analysis]] to understand how stimulation parameters affect seizure threshold [4].

## Related Software

TVEB operates within a broader ecosystem of computational neuroscience tools. As part of [[the-virtual-brain]], TVEB inherits the core simulation infrastructure, while specialized analysis routines build upon tools like the [[brain-connectivity-toolbox]] for network analysis and [[graphvar]] for dynamical systems analysis. For forward modeling of electrophysiological signals, TVEB can be combined with volume conduction models from packages like [[openmeeg]], while neuroimaging preprocessing leverages tools such as [[freesurfer]] and [[fsl]].

## References

1. Michael Breakspear, John A. Roberts, John R. Terry, Stefano Rodrigues, Nader Mahmud, Philip Robinson. *Large-scale brain dynamics of seizures: asymptotic analysis of a neural field model*. Journal of Computational Neuroscience. [DOI](https://doi.org/10.1007/s10827-006-8135-2)
2. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. Kang You, Gary Green, Jian Zhang. *Differential Dynamic Causal Nets: Model Construction, Identification and Group Comparisons*. [Link](https://arxiv.org/abs/2601.21478)
4. Amirreza Movahedin, Lennart P. L. Landsmeer, Christos Strydis. (2025). *HUMA: Heterogeneous, Ultra Low-Latency Model Accelerator for The Virtual Brain on a Versal Adaptive SoC*. Symposium on Field Programmable Gate Arrays. [DOI](https://doi.org/10.1145/3706628.3708875)