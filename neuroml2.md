---
title: NeuroML2
created: 2026-05-04
updated: 2026-05-04
type: entity
tags: [software-neuroml, neural-mass-models, spiking-neural-networks, software-tvb, software-nest, software-brian, software-neuron, open-source-brain, neuroml, neurodamus, interoperability, standardization]
sources: [Cannon2014, Gleeson2010, Gleeson2019, NeuroMLDocs]
---

NeuroML2 (Neural Modeling Language, version 2) is a standardized, XML-based description language for constructing, validating, and exchanging computational models of neurons and neural networks. Developed as an evolution of the original NeuroML specification [[neuroml]], NeuroML2 began development in 2011, with early beta versions released starting in 2013 and a key specification paper published in 2014 [@Cannon2014]. The language provides a declarative framework for specifying biophysically detailed neuron models—including multicompartmental membranes, ion channel dynamics, and synaptic connections—as well as network architectures with defined connectivity patterns. By encoding model structure in a platform-independent format, NeuroML2 facilitates interoperability between different simulation engines and enables reproducible computational neuroscience.

## Motivation and Context

The computational neuroscience field historically suffered from fragmentation: models developed in one simulator (e.g., [[neuron]] or [[nest]]) could not be directly executed in another without substantial manual translation. This lack of interchangeability hindered model reuse, verification, and collaboration. NeuroML2 emerged to address this bottleneck by providing a vendor-neutral specification that captures the essential mathematics and topology of neural models independent of implementation details [@Gleeson2010]. The language builds upon earlier standardization efforts, notably LEMS (Low Entropy Model Specification), which provides a core set of dynamical system primitives [@Cannon2014]. Today, NeuroML2 serves as a bridge between the [[spiking-neural-networks]] community and tool-specific ecosystems, supporting both detailed biophysical models and [[neural-mass-model]] abstractions.

## Key Features

NeuroML2 supports several tiers of model complexity. At the cellular level, the language can define arbitrary neuron morphologies with segment-by-segment membrane properties, ion channel implementations (e.g., Hodgkin-Huxley-type channels), and synaptic mechanisms with plasticity rules. At the network level, NeuroML2 specifies populations of cells, their spatial arrangements, and connection rules that may be probabilistic, distance-dependent, or explicitly defined [@Cannon2014]. The specification includes built-in support for common neuroscience experimental paradigms such as current injection, spike trains, and fixed-weight or plastic synapses.

A distinguishing characteristic of NeuroML2 is its emphasis on validation: compliant models must satisfy schema constraints and, where applicable, produce numerically consistent results across compliant simulators. The NeuroML website provides a curated database of example models, and several tools—including pyNeuroML, jNeuroML, and the NeuroML editor—enable model construction, validation, and export to target simulators. The language also defines extensions for specific use cases, such as NeuroML-LEMS for abstract network models and MorphML (embedded within NeuroML) for morphological specifications.

## Relationship to TVB

Within the [[the-virtual-brain]] ecosystem, NeuroML2 plays an emerging but important role in model interoperability. While TVB operates primarily at the [[whole-brain-modeling]] level using [[neural-mass-model]] abstractions (such as the [[epileptor]] or [[jansen-rit-model]]), NeuroML2 provides a pathway for importing detailed single-neuron or microcircuit models into TVB's multiscale framework. The [[tvb-nest]] adapter enables co-simulation between TVB and [[nest]], and NeuroML2 serves as the interoperability layer for exchanging cell and synapse specifications between these platforms. Users seeking to bridge detailed [[spiking-neural-networks]] models with TVB's large-scale [[brain-dynamics]] simulations can leverage NeuroML2 as a standardized interchange format, facilitating integration with tools like [[neurodamus]] (the NEURON-based backend used in some large-scale projects).

## Relationship to Other Standards

NeuroML2 intersects with several other neuroscience modeling standards. Unlike PyNN, which provides a Python API for simulator interoperability, NeuroML2 is a declarative XML format that can be parsed and instantiated by multiple backends [@Cannon2014]. It shares philosophical goals with [[neuroml]] (its predecessor) and the newer SONATA format from the Blue Brain Project, though each targets somewhat different scopes and communities. The Brain Modeling ToolKit and [[bmtk]] also support NeuroML2 reading capabilities, expanding the ecosystem of compatible simulators. Compared to raw model definitions in [[brian2genn]] or C++-based simulators, NeuroML2 prioritizes human readability and toolchain integration over performance optimization.

## Key Papers

- **Cannon et al. (2014)** — "LEMS: A language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2" — Frontiers in Neuroinformatics [@Cannon2014]
- **Gleeson et al. (2010)** — "NeuroML: A language for describing data driven models of neurons and networks with a high degree of biological detail" — PLoS Computational Biology [@Gleeson2010]
- **Gleeson et al. (2019)** — "Open Source Brain: A collaborative community for sharing, visualization, and analyzing computational neuroscience models" — Neuron [@Gleeson2019]

## References

- Cannon, R. C., Gleeson, P., Crook, S., Ganapathy, G., Marin, B., Piasini, E., & Silver, R. A. (2014). LEMS: A language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2. Frontiers in Neuroinformatics, 8, 79. https://doi.org/10.3389/fninf.2014.00079
- Gleeson, P., Crook, S., Cannon, R. C., Hines, M. L., Billings, G. O., Farinella, M., ... & Silver, R. A. (2010). NeuroML: A language for describing data driven models of neurons and networks with a high degree of biological detail. PLoS Computational Biology, 6(6), e1003376. https://doi.org/10.1371/journal.pcbi.1003376
- Gleeson, P., Piasini, E., Crook, S., Harrington, E., Stevanson, I., & Silver, R. A. (2019). The Open Source Brain: A collaborative community for sharing, visualization, and analyzing computational neuroscience models. Neuron, 104(2), 240-256. https://doi.org/10.1016/j.neuron.2019.07.019