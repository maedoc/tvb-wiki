---
created: 2026-04-27
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/gewaltig-diesmann-2007.md
tags:
- software-arbor
title: Arbor
type: entity
updated: 2026-05-18
---
Arbor is a high-performance neural simulation library optimized for efficient multi-compartment [[neuron]] models and large-scale [[spiking-neural-networks]] on modern hardware architectures. Originally developed to address the computational demands of biophysically detailed simulations, Arbor spans scales from single-compartment neurons to coordinated populations of cells, offering a microscopic counterpart to macroscopic whole-brain platforms Hater et al. (2025). While [[tvb]] models [[whole-brain-modeling]] dynamics through anatomical [[structural-connectivity]] and regional mean activity Sanz Leon et al. (2013), and [[nest]] specializes in large networks of point neurons with efficient spike communication Gewaltig & Diesmann (2007), Arbor distinguishes itself by emphasizing detailed compartmental resolution and performance portability across heterogeneous computing systems. The library's modular design has enabled direct co-simulation with TVB via an MPI intercommunicator, translating discrete spikes into continuous macroscopic signals for studying [[epilepsy-modeling|seizure onset]] and [[network-dynamics]] propagation Hater et al. (2026). This interoperability positions Arbor as a critical component in multi-scale brain modeling pipelines, where biologically realistic cell populations can substitute abstract [[neural-mass-models|neural-mass]] nodes to bridge microscopic biophysics with whole-brain function.

## Key Features

Arbor is an open-source library purpose-built for simulating biophysically detailed [[neuron]] models, offering a modern alternative to established simulators such as [[neuron|NEURON]] with a deliberate emphasis on contemporary hardware architectures and scalability to large-scale systems [[raw/papers/arxiv-2505.16861.md|Hater et al. (2025)]]. Written in C++ and exposed through an intuitive high-level Python interface, Arbor solves the cable equation over neuronal morphologies, enabling simulations that transcend point-neuron approximations to resolve dendritic computation and spatially extended dynamics. Its numerical core supports bulk-synchronous parallelism, shared-memory execution through a thread-pool and job system, and hardware acceleration of compartmental cells via SIMD vectorization and GPU offload for selected cell types [[raw/papers/arxiv-2505.16861.md|Hater et al. (2025)]].

Beyond single-cell modeling, the framework scales to large [[spiking-neural-networks]] with multi-compartment morphologies while maintaining performance portability across heterogeneous computing platforms, a design that has enabled direct [[co-simulation]] with macroscopic [[whole-brain-modeling]] tools such as [[tvb]] [[raw/papers/semanticscholar-eb704b6f5462.md|Hater et al. (2026)]]. Arbor supports conversion of single-neuron models from [[neuron|NEURON]] and implements a spectrum of [[synaptic-plasticity]] mechanisms, including spike-timing-dependent plasticity, calcium-based synaptic tagging, and structural plasticity, alongside built-in diffusion functionality for intracellular signaling. As a component of the [[ebrains]] research infrastructure, Arbor is distributed through the EBRAINS software catalog and accessible on connected HPC centers, positioning it as a critical building block in multi-scale brain modeling pipelines that couple microscopic biophysics with whole-brain function [[raw/papers/semanticscholar-eb704b6f5462.md|Hater et al. (2026)]].

## Relationship to Whole-Brain Modeling
Whereas [[tvb]] models [[whole-brain-modeling]] dynamics through [[structural-connectivity]] and regional mean activity [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]], it traditionally represents each brain region with abstract [[neural-mass-models]] that average over cellular biophysics. Arbor closes this gap by offering a microscopic counterpart: its populations of multi-compartment [[neuron]] models can replace TVB's lumped nodes, injecting biologically realistic [[spiking-neural-networks]] activity directly into the macroscopic circuit [[raw/papers/arxiv-2505.16861.md|Hater et al. (2025)]]. The two simulators are coupled via an MPI intercommunicator that translates discrete spikes from Arbor into continuous signals for TVB and vice versa, enabling real-time bidirectional interaction during a single simulation [[raw/papers/semanticscholar-eb704b6f5462.md|Hater et al. (2026)]]. Because the framework is fully modular, each scale retains its own model choices—Arbor supplies detailed compartmental resolution while TVB supplies the anatomical [[connectome]]—so researchers can study how local biophysical events, such as [[epilepsy-modeling|seizure onset]], propagate across large-scale [[network-dynamics]] without sacrificing either microscopic fidelity or whole-brain coverage [[raw/papers/semanticscholar-eb704b6f5462.md|Hater et al. (2026)]]. This positions Arbor not merely as a pre-processing or post-processing tool, but as an integral component of multi-scale pipelines in which realistic cell populations substitute for abstract neural-mass nodes [[raw/papers/arxiv-2505.16861.md|Hater et al. (2025)]].
## Related Software
* Antspy
* [[bids]] Validator
* Bidscoin
* [[brainstorm]]
* [[brian]]
* [[music]]
