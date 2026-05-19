---
created: 2026-05-04
sources:
- raw/papers/semanticscholar-de2622579d45.md
- raw/papers/semanticscholar-5c84b271b035.md
- raw/papers/sanz-leon-2013.md
tags:
- software-neuroml
- spiking-neural-networks
- software-tvb
- software-nest
- software-neuron
- software-brain-modeling
- neuroml
- interoperability
- standardization
title: NeuroML2
type: entity
updated: '2026-05-19'
---

NeuroML2 (Neural Modeling Language, version 2) is a standardized, XML-based description language for constructing, validating, and exchanging computational models of neurons and neural networks. Developed as an evolution of the original NeuroML specification [[neuroml]] [cite:Gleeson2010], NeuroML2 began development in 2011, with early beta versions released starting in 2013 and a key specification paper published in 2014 [cite:Cannon2014]. The language provides a declarative framework for specifying biophysically detailed neuron models—including multicompartmental membranes, [[ion-channel]] dynamics, and synaptic connections—as well as network architectures with defined [[connectivity]] patterns. By encoding model structure in a platform-independent format, NeuroML2 facilitates interoperability between different simulation engines and enables reproducible [[computational-neuroscience]].

## Motivation and Context

The computational neuroscience field historically suffered from fragmentation: models developed in one simulator (e.g., [[neuron]] or [[nest]]) could not be directly executed in another without substantial manual translation. This lack of interchangeability hindered model reuse, verification, and collaboration. NeuroML2 emerged to address this bottleneck by providing a vendor-neutral specification that captures the essential mathematics and topology of neural models independent of implementation details [cite:Cannon2014]. The language builds upon earlier standardization efforts, notably LEMS (Low Entropy Model Specification), which provides a core set of dynamical system primitives [cite:LEMSspec]. Today, NeuroML2 serves as a bridge between the [[spiking-neural-networks]] community and tool-specific ecosystems, supporting both detailed biophysical models and [[neural-mass-model]] abstractions.

## Key Features

NeuroML2 supports several tiers of model complexity. At the cellular level, the language can define arbitrary neuron morphologies with segment-by-segment membrane properties, ion channel implementations (e.g., [[hodgkin-huxley-model]]-type channels), and synaptic mechanisms with plasticity rules. The specification includes native support for reduced spiking neuron models including [[izhikevich-neuron-model]] and [[adaptive-exponential-integrate-and-fire]], as well as conductance-based variants [cite:Cannon2014]. At the network level, NeuroML2 specifies populations of cells, their spatial arrangements, and connection rules that may be probabilistic, distance-dependent, or explicitly defined. The specification includes built-in support for common neuroscience experimental paradigms such as current injection, spike trains, and fixed-weight or plastic synapses. Network descriptions in NeuroML2 can specify [[connectome]]-level connectivity patterns suitable for [[brain-network]] analysis.

A distinguishing characteristic of NeuroML2 is its emphasis on validation: compliant models must satisfy schema constraints and, where applicable, produce numerically consistent results across compliant simulators. The NeuroML website provides a curated database of example models, and several tools—including pyNeuroML, [[jneuroml]], and the NeuroML editor—enable model construction, validation, and export to target simulators. The language also defines extensions for specific use cases, such as NeuroML-LEMS for abstract network models. Morphological specifications that were originally handled by the separate MorphML standard are now fully embedded within the NeuroML2 specification itself [cite:Cannon2014].

## Relationship to TVB

Within the [[the-virtual-brain]] ecosystem, NeuroML2 interfaces with TVB through the [[tvb-nest]] module [cite:TVBNESTdocs], facilitating the specification of detailed neuronal microcircuits that can be coupled to TVB's [[whole-brain-modeling]] framework. While TVB's default workflows use reduced [[neural-mass-model]] formulations such as the [[jansen-rit-model]] or [[epileptor]] for large-scale simulations, users can incorporate NeuroML2-defined [[spiking-neural-networks]] to create hybrid models that maintain biophysical detail at the microscale while leveraging TVB's capabilities at the macroscale. This is particularly valuable for [[personalized-brain-modeling]] applications where subject-specific cell types and synaptic properties derived from imaging data need to be integrated [cite:TVBNESTdocs].

## Relationship to Other Standards

NeuroML2 intersects with several other neuroscience modeling standards. Unlike [[pyNN]], which provides a Python API for simulator interoperability, NeuroML2 is a declarative XML format that can be parsed and instantiated by multiple backends. It shares philosophical goals with [[neuroml]] (its predecessor) [cite:Gleeson2010] and the SONATA format from the Blue Brain Project, though each targets somewhat different scopes and communities. The language builds on [[lems]] (Low Entropy Model Specification), which provides the mathematical foundation for defining dynamical systems and is maintained as a related but distinct specification [cite:LEMSspec]. In contrast to [[dynamic-causal-modeling]] approaches used in neuroimaging analysis, NeuroML2 is designed for forward simulation rather than Bayesian inversion of measured signals.

## References

The recent EDEN neural simulator illustrates one practical application of NeuroML-based descriptions in decoupling abstract model specifications from execution backends. [[raw/papers/semanticscholar-de2622579d45.md|Panagiotou et al. (2025)]] describe a modular architecture that enables developers to focus on high-performance simulation while users gain portability without implementing custom engines; by integrating diverse targets including FPGA-based accelerators and the SpiNNaker neuromorphic platform, the work demonstrates how standardized descriptions can support heterogeneous hardware with minimal reprogramming effort. Complementing this domain, the NESTML project offers a domain-specific language for neuron and synapse models paired with a Python-based code generation toolchain. [[raw/papers/semanticscholar-5c84b271b035.md|Linssen et al. (2025)]] emphasize that NESTML supports FAIR principles by making models findable, accessible, interoperable, and reusable across backends such as [[nest]] Simulator and SpiNNaker. At the whole-brain scale, [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]] introduced [[the-virtual-brain]], an open-source platform that combines empirical structural connectivity with [[neural-mass-model]] abstractions and supports forward modeling for [[eeg]], [[meg]], and [[fmri]], enabling [[personalized-brain-modeling]].