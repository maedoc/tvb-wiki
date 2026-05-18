---
title: ModelDB
created: 2026-05-06
updated: 2026-05-18
type: entity
tags:
- software-modeldb
- reproducibility
- spiking-neural-networks
- whole-brain-modeling
- neural-mass-models
- software-neuron
- software-brian
- software-neuroml
- connectomics
sources:
- raw/papers/migliore-2006.md
---

# ModelDB

**ModelDB** is a curated, web-accessible repository for computational neuroscience models that links published, peer-reviewed research to its corresponding runnable source code. Originally launched with a focus on [[neuron|NEURON]] simulations, the database has since grown into a heterogeneous archive spanning multiple platforms including [[brian2]], [[genesis]], and [[nest]], hosting thousands of models that range from detailed single-neuron biophysics to network-level dynamics and simplified population representations. [[raw/papers/migliore-2006.md|Migliore et al. (2003)]]

The need for ModelDB arose from a growing recognition within the computational neuroscience community that reproducibility depends on whether other researchers can execute, inspect, and extend a model after publication. Before curated repositories became common, model implementations were typically distributed through personal websites or lost entirely after a paper appeared, creating a widening gap between published scientific claims and verifiable code. ModelDB addresses this by requiring that every deposited model be tied directly to its originating peer-reviewed publication, thereby establishing an unbroken provenance chain from citation to executable source. [[raw/papers/migliore-2006.md|Migliore et al. (2003)]] The repository integrates with PubMed and other bibliographic databases so users can navigate between a paper's description of model behavior and the underlying implementation files, while a submission interface designed for non-programmers lowers the barrier for authors to archive their work without requiring expertise in version control or web deployment.

Each model entry carries structured metadata describing the model architecture, parameter sets, and computational requirements, alongside source code that is typically packaged to run with minimal configuration. Over time the collection has expanded to encompass implementations expressed in hoc, Python, C++, and Matlab, reflecting the diverse tooling landscape of the field. The database also integrates with [[open-source-brain]] (OSB) to furnish web-based simulation capabilities, enabling researchers to execute certain models directly in a browser without local installation—an arrangement that supports reproducible modeling independent of any single software stack. [[raw/papers/migliore-2006.md|Migliore et al. (2003)]]

ModelDB occupies a central node in the broader ecosystem of neuroscience simulators and standards. The repository leverages [[neuroml]] as a standardized model description format that promotes interoperability across disparate simulation environments, while its cross-referencing with PubMed establishes a bibliographic layer anchoring validated biophysical implementations within the literature. Detailed circuit models archived in the database demonstrate parameter ranges for equations that are later simplified in population-level formulations, while documented parameters from [[spiking-neural-networks]] constrain the derivation of mean-field approximations used in [[whole-brain-modeling]] simulations. Within the broader [[connectomics]] landscape, ModelDB serves as a foundational layer for comparing large-scale predictions against independently verified network architectures.

For [[the-virtual-brain]] (TVB), ModelDB provides a bridge between microscale biophysics and macroscale [[brain-network]] dynamics. Implementations of the [[jansen-rit-model|Jansen-Rit model]] available through ModelDB establish biophysically grounded parameter ranges that inform TVB's [[neural-mass-models|neural mass model]] formulations, while documented spiking network parameters constrain the derivation of population-level equations employed in TVB simulations. Because ModelDB entries preserve the exact code and parameters from peer-reviewed publications, TVB researchers can validate whole-brain predictions against independently verified network architectures and trace the biophysical origins of the simplified dynamical systems that drive connectome-based simulations.
