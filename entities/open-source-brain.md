---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software-neuroml
- computational-neuroscience
- neural-mass-models
- spiking-neural-networks
- reproducibility
- database-neuroscience
- software-modeldb
title: Open Source Brain
type: entity
updated: '2026-05-06'
---

Open Source Brain (OSB) is an online platform and community repository for sharing, developing, and distributing [[computational-neuroscience]] models in a standardized, reusable format. Founded in the late 2000s by researchers in Angus Silver's group at University College London (UCL) and collaborators across Europe, OSB addresses a fundamental challenge in computational neuroscience: the proliferation of incompatible, poorly documented model implementations that are difficult to reuse, reproduce, or extend. The platform serves as both a model database analogous to Modeldb and a collaborative development environment where researchers can publish nervous system models ranging from single neuron simulations to whole-[[brain-network]] architectures.

## Motivation and Context

Computational neuroscience has historically suffered from a [[reproducibility]] crisis comparable to that in experimental sciences. When researchers publish computational models in journal articles, they typically provide model code that is tightly coupled to a specific simulator (such as [[neuron]], Brian2, or [[nest]]), written in a custom format, and poorly documented with respect to parameters, initial conditions, and numerical methods. This siloed approach makes it extraordinarily difficult for other laboratories to build upon existing work, to verify published claims, or to compare competing models directly. Open Source Brain emerged as a response to this fragmentation, promoting the use of Neuroml (Neural Open Markup Language) as a simulator-independent standard for specifying neural models. By encoding models in Neuroml, researchers can execute the same mathematical specification across multiple simulator backends, compare implementations for numerical consistency, and archive the canonical form of a model independent of whichever simulator was used for the original publication.

The platform also fills a niche distinct from other model repositories. While Modeldb (hosted at Yale) focuses primarily on archiving published models with minimal curation, OSB emphasizes active community involvement, model validation against multiple simulators, and integration with the broader [[neuromorpho-toolkit]] ecosystem including tools like [[pynest]], PyBrain, and Nengo. OSB models are also exported to the [[ebrains]] infrastructure, providing European neuroscience researchers with a pathway to integrate their computational work into the European Brain Project's data ecosystem.

## Key Features

OSB provides several interconnected features that distinguish it from simple code repositories. First, the platform maintains a curated library of neural models organized by brain region, cell type, and complexity level. Models range from detailed multi-compartment neuron models of cortical pyramidal cells to simplified [[neural-mass-model]] representations of cortical columns suitable for [[whole-brain]] simulations. Second, OSB implements automated test suites that validate model behavior against reference traces — when a model is submitted, the platform runs it on multiple simulators (where supported) and reports whether outputs remain within tolerance of the reference behavior. This validation infrastructure catches implementation errors and ensures that models remain functional as simulator software evolves.

Third, OSB serves as a hosting platform for collaborative model development. Researchers can fork existing models, modify parameters or equations, and submit improved versions for inclusion in the main repository. The platform supports version control through Git, allowing detailed tracking of changes over time. Fourth, OSB provides educational resources including tutorials on converting legacy model code to [[neuroml]] format, documentation of best practices for model annotation, and worked examples demonstrating how to connect OSB models to simulation environments like [[neuron]] and [[brian2]].

## Relationship to The Virtual Brain

While Open Source Brain and [[the-virtual-brain]] (TVB) serve different primary purposes—one focusing on neuron and network model repositories while the other provides an integrated whole-brain simulation platform—they intersect meaningfully in the domain of large-scale brain modeling. Several OSB models, particularly those implementing [[neural-mass-model]] architectures such as the [[jansen-rit-model]] or reduced [[wong-wang-model]] formulations, serve as the mathematical foundations for TVB's regional brain network simulations. TVB's architecture allows users to configure neural mass models at each brain region and couple them via [[structural-connectivity]] matrices derived from [[diffusion-imaging]] data. By providing well-validated neural mass implementations in Neuroml format, OSB contributes directly to the ecosystem that TVB draws upon for whole-brain modeling workflows. Conversely, TVB's emphasis on personalized brain modeling—where individual connectivity patterns inform simulation parameters—has inspired OSB community members to develop models specifically targeting the integration of [[functional-connectivity]] constraints into neural mass representations.

## Related Software

Open Source Brain operates within a broader ecosystem of neuroscience software tools. The platform is closely tied to Neuroml as its primary model specification language and to the [[lems]] (Low-Electrophysiology Model Specification) framework that provides the execution engine for mathematical descriptions. Model curation and validation rely on the [[pynest]] interface for NEST simulations and the Brian2 simulator for Python-based implementations. For visualization and analysis, OSB integrates with tools like [[pymvpa]] for multivariate pattern analysis of simulation outputs and [[connectome-workbench]] for exploring brain parcellations that inform network topology. The platform also maintains interoperability with Brainsuite and [[brainlife]] repositories for sharing full analysis pipelines alongside raw model code.

## Key Papers

The foundational paper describing Open Source Brain was published in *Neuron* (Gleeson et al., 2019), outlining the architecture, validation framework, and growth [[trajectory]] of the model repository. This paper demonstrated OSB's capabilities for browser-based visualization, analysis, and simulation of standardized neuronal models. The original NeuroML specification paper (Gleeson et al., 2010) established the standardized model description language that underlies OSB's interoperability. Subsequent work detailed the integration of OSB with [[ebrains]] and the development of the validation testing infrastructure. The platform has also been referenced in methodological reviews of computational neuroscience tooling, including comparisons between Neuroml and alternative standards such as NineML and [[pynn]] (Davison et al., 2009). Additionally, OSB has been cited in discussions of reproducibility and best practices in computational neuroscience (McDougal et al., 2017), particularly in comparisons with Modeldb for model archiving and reuse.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))