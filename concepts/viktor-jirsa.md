---
affiliation: Aix-Marseille Université
created: 2026-04-20
sources:
- raw/papers/deco-2013.md
- raw/papers/semanticscholar-7c3337c880fd.md
tags:
- people-researcher
- whole-brain-modeling
- neural-mass-models
- the-virtual-brain
- computational-neuroscience
- epilepsy-modeling
- connectivity
title: Viktor Jirsa
type: entity
updated: '2026-05-06'
---

Viktor Jirsa is a computational neuroscientist whose research focuses on large-scale brain modeling, neural mass models, and the development of [[whole-brain]] simulation frameworks. He is a professor at Aix-Marseille Université and leads the Systems Neuroscience team at the Institut de Neurosciences des Systèmes. He is best known for co-founding [[the-virtual-brain]], a software platform for personalized brain modeling, and for developing the Epileptor model—a seminal computational model of epileptic seizures that has become a cornerstone of computational epilepsy research.

## Biography

Viktor Jirsa received his doctoral training in theoretical physics at the University of Tübingen before transitioning to [[computational-neuroscience]]. His early work focused on [[nonlinear-dynamics]] and the application of dynamical systems theory to neural modeling. He joined Aix-Marseille Université, where he established a research program bridging theoretical neuroscience with clinical applications in epilepsy. As scientific director of [[the-virtual-brain]], he has overseen the development of one of the most widely adopted whole-brain modeling platforms in the field.

## Research Contributions

Jirsa's work bridges the gap between [[neural-mass-models]] and [[connectomics]], developing mathematical frameworks that capture how large-scale brain connectivity shapes emergent neural dynamics. His research demonstrates that the brain's structural connectivity—the anatomical white-matter pathways mapped via diffusion imaging—imposes constraints on functional dynamics, enabling predictions of resting-state networks, seizure propagation patterns, and the effects of brain stimulation. This work operates at the intersection of [[dynamical-systems-theory]] and neuroimaging, using [[stochastic-differential-equations]] to model noise-driven exploration of brain state spaces [@jirsa2002; @fransson2005].

A significant contribution from Jirsa and collaborators is the concept of the **[[rest|Resting State]] Manifold (RSM)**—a low-dimensional representation of brain states that emerges from the interplay between local dynamics and anatomical [[connectivity]] patterns. This framework was used to explore network degeneracy: the phenomenon whereby different configurations of brain connectivity can generate similar functional outputs. Understanding degeneracy is crucial for interpreting how the brain maintains function despite structural variations or lesions, and it has implications for predicting the outcomes of neurosurgical interventions [@gudibanda_unpublished].

## The Epileptor Model

The Epileptor model, developed by Jirsa and colleagues, represents one of the most influential [[epilepsy-modeling]] frameworks in computational neuroscience. The model consists of a system of coupled differential equations that capture the fast and slow dynamics of seizure onset, propagation, and termination [@jirsa2014]. By embedding the Epileptor in patient-specific [[connectome]] architectures derived from diffusion tensor imaging, researchers can simulate individualized seizure dynamics and explore therapeutic interventions such as targeted stimulation or surgical resection. The Epileptor has been integrated into [[the-virtual-brain]] as a canonical model for clinical translation.

## Impact on Whole-Brain Modeling

Jirsa's collaboration with [[gustavo-deco]] established a theoretical framework (see [[deco-2013]]) demonstrating that noise-driven fluctuations around stable fixed points in structured brain networks can reproduce empirically observed [[resting-state]] [[functional-connectivity]] patterns. This work provided computational validation for the hypothesis that the resting brain continuously explores a repertoire of functional states, many of which overlap with task-evoked activation patterns—a perspective that has profoundly influenced contemporary theories of intrinsic brain activity.

The software ecosystem developed under Jirsa's leadership, primarily [[the-virtual-brain]], enables researchers to construct personalized brain models from individual neuroimaging data. These models integrate [[structural-connectivity]] matrices (typically derived from [[diffusion-imaging]] and tractography) with neural mass models to generate simulated brain dynamics that can be compared against empirical fMRI, EEG, or MEG recordings. This framework has applications in [[personalized-brain-modeling]], preoperative planning, and basic research into the principles governing brain organization.

## Relationship to TVB

Viktor Jirsa is the scientific director and co-founder of [[the-virtual-brain]], one of the most widely used [[whole-brain-modeling]] software platforms in computational neuroscience. TVB implements several neural mass models originally developed or adapted by Jirsa's group, including the [[epileptor]] for seizure modeling and variants of the [[jansen-rit-model]] for generic whole-brain simulations. The platform's connectivity pipeline can ingest [[diffusion-imaging]] data processed with tools like [[mrtrix3-connectome]] or [[dipy]] to construct patient-specific structural connectivity matrices, which then serve as the anatomical scaffold for simulations. Jirsa's research directly informs TVB's model repertoire, parameter estimation routines, and the theoretical framework connecting structural and functional brain dynamics.

## References

1. Deco et al. (2013). *Resting brains never rest: computational insights into potential cognitive architectures*. Trends in Neurosciences. [DOI](](https://doi.org/10.1016/j.tins.2013.09.002))
2. Kashyap Gudibanda, J. Fousek, S. Petkoski, V. Jirsa. (2026). *The role of connectivity for the degeneracy of the brain’s resting state dynamics*. Journal of Computational Neuroscience. [DOI](](https://doi.org/10.1007/s10827-025-00919-0))