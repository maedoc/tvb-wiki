---
title: jNeuroML
created: 2025-01-15
updated: 2026-04-28
type: entity
tags: [software-neuroml, neuroml, spiking-neural-networks, computational-neuroscience, java, model-validation, standards, neurodevelopment]
sources:
  - https://github.com/NeuroML/jNeuroML
  - https://docs.neuroml.org/Userdocs/Software/jNeuroML.html
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000815
  - https://www.frontiersin.org/articles/10.3389/fninf.2014.00079/full
  - https://pubmed.ncbi.nlm.nih.gov/20585541/
  - https://pubmed.ncbi.nlm.nih.gov/17873371/
---

# jNeuroML

## Overview

jNeuroML is a Java-based software package that provides both an implementation of the [[neuroml]] specification and a suite of command-line tools for working with NeuroML model descriptions. Developed primarily by [Padraig Gleeson](https://github.com/pgleeson) and the NeuroML community, jNeuroML serves as the reference implementation of the NeuroML specification and provides essential functionality for parsing, validating, simulating, and converting neural models expressed in the NeuroML format. As a cross-platform Java application, it runs on Windows, macOS, and Linux systems, making it accessible to researchers across different computational environments. The software is open-source and available through GitHub, with releases distributed via Maven Central for integration into Java-based projects.

jNeuroML was the first full implementation of the NeuroML specification and has served as the reference implementation for subsequent tools in the NeuroML ecosystem, including [[pyneurotml]] (a Python library providing similar functionality).

## Relationship to NeuroML and the NeuroML Ecosystem

[[neuroml]] (Neural Markup Language) is a standardized XML-based format for describing computational models of neurons, synapses, and neural networks. The language was developed to address the challenge of model interoperability in computational neuroscience—different simulators (such as [[neuron]], [[brian]], and [[nest]]) historically used incompatible formats, making it difficult to reuse and share models across platforms. NeuroML provides a modular, hierarchical structure that can represent individual ion channels, cell models, populations, and full networks at multiple levels of abstraction.

jNeuroML implements the full NeuroML specification and provides several core functions essential to the ecosystem. First, it acts as a **validator**, parsing NeuroML documents and checking them against the schema to ensure compliance with the specification. Second, it serves as a **simulator interface**, capable of running simulations of NeuroML-described networks using its internal simulation engine or by exporting to formats compatible with other simulators. Third, it provides **conversion capabilities**, transforming NeuroML models into formats suitable for other simulation environments, including NEURON (.mod files), [[brian]] (Python scripts), and standalone simulation scripts.

The relationship between jNeuroML and the broader NeuroML ecosystem is complementary to other tools like [[pyneurotml]] (a Python library providing similar functionality) and [[neuroconstruct]] (a graphical environment for building and managing NeuroML models). While neuroconstruct offers a GUI for model construction, jNeuroML focuses on command-line operations and programmatic usage, making it particularly suitable for batch processing, automated testing pipelines, and integration with workflow tools. The Java implementation was historically the first full implementation of the NeuroML specification and has served as a reference for subsequent tools. Development of jNeuroML began in 2012, shortly after the NeuroML v1.x specification was finalized, and it has been maintained in parallel with the evolution of NeuroML v2.x.

## Key Features

jNeuroML offers several distinguishing features that make it valuable for computational neuroscience research. The **LEMS (Lumped Element Model Specification) interpreter** built into jNeuroML provides support for running simulations defined using LEMS, a domain-specific language for describing dynamical systems that is closely integrated with NeuroML. This allows researchers to define and simulate abstract neural models that can be mapped onto specific simulator implementations.

The software includes **network generation capabilities**, supporting the creation of large-scale networks from parameterized specifications. This is particularly useful for researchers building whole-brain models or large-scale network simulations who need to generate connectivity patterns programmatically. jNeuroML can export network specifications to various formats suitable for simulation in [[nest]], [[neuron]], or other established simulators.

Another important feature is **model unit conversion and scaling**, which allows users to transform models between different parameter regimes or export them with different units. This is valuable when adapting models developed for specific brain regions or species to new contexts. The tool also supports **graph generation**, producing visual representations of network architectures defined in NeuroML documents.

jNeuroML can export NeuroML models to multiple simulator formats including NEURON, Brian2, Matlab, MOOSE, NetPyNE, and can even import other formats like SBML into LEMS.

## Relationship to TVB

While jNeuroML and [[the-virtual-brain]] (TVB) serve different primary purposes, they share the broader goal of advancing standardized, reproducible computational neuroscience. TVB is primarily a whole-brain modeling platform that simulates large-scale brain dynamics at the level of brain regions, often using neural mass models or mean-field approaches. In contrast, jNeuroML focuses on detailed single-neuron and small-network models using [[spiking-neural-networks]].

There is potential for integration between these tools: TVB's regional models could be parameterized using insights from detailed [[neuroml]]-based simulations, and jNeuroML could serve as a bridge for incorporating detailed cellular models into larger-scale frameworks. The [[tvb-multiscale]] extension of TVB specifically explores such multi-scale modeling approaches, potentially connecting to detailed network models. Additionally, TVB's use of the [[connectome]] as an essential component shares conceptual ground with NeuroML's network description capabilities.

Recent developments in the NeuroML community, including the creation of database resources like Open Source Brain, have facilitated the sharing of models that could potentially inform whole-brain modeling efforts. The standardized format provided by [[neuroml]] offers a path for exchanging model descriptions between detailed neural simulators and large-scale frameworks like TVB. Multi-scale integration remains an active area of development, with researchers exploring how to bridge the gap between detailed biophysical models and population-level brain simulations.

## Related Software

- [[neuroml]] — The XML-based specification for describing neural models
- [[pyneurotml]] — Python library providing NeuroML functionality
- [[neuroconstruct]] — Graphical environment for building NeuroML models
- [[brian]] — Simulator with NeuroML export capabilities
- [[neuron]] — Simulator supporting NeuroML import/export
- [[nest]] — Simulator with NeuroML support
- [[lfpy]] — Python interface for NEURON simulations
- [[the-virtual-brain]] — Whole-brain modeling platform
- [[tvb-multiscale]] — TVB extension for multi-scale modeling
- [[connectome]] — Brain connectivity representation

## Key Papers

1. **Gleeson et al. (2010)** — "NeuroML: A Language for Describing Data Driven Models of Neurons and Networks with a High Degree of Biological Detail" — The foundational paper describing NeuroML and its implementation in jNeuroML. Published in PLoS Computational Biology. PMID: 20585541.

2. **Crook et al. (2007)** — "MorphML: Level 1 of the NeuroML Standards for Neuronal Morphology Data and Model Specification" — Describes the MorphML component of the NeuroML standards. Published in Neuroinformatics. PMID: 17873371.

3. **Cannon et al. (2014)** — "LEMS: A Language for Expressing Complex Biological Models in Concise and Hierarchical Form and its Use in Underpinning NeuroML 2" — Describes the LEMS language that underlies NeuroML 2. Published in Frontiers in Neuroinformatics.

4. **Gleeson et al. (2007)** — "neuroConstruct: A Tool for Modeling Networks of Neurons in 3D Space" — Describes neuroConstruct, a complementary tool for building NeuroML models. Published in Neuron.

5. **Goddard et al. (2001)** — "Towards NeuroML: Model Description Methods for Collaborative Modelling in Neuroscience" — The original proposal that led to the development of NeuroML. Published in Philosophical Transactions of the Royal Society B. PMID: 11545699.

## References

1. Gleeson P, Crook S, Cannon RC, Hines ML, Billings GO, Farinella M, Morse TM, Davison AP, Ray S, Bhalla US, Barnes SR, Dimitrova YD, Silver RA. (2010). NeuroML: A Language for Describing Data Driven Models of Neurons and Networks with a High Degree of Biological Detail. PLoS Comput Biol 6(6): e1000815. https://doi.org/10.1371/journal.pcbi.1000815

2. Crook S, Gleeson P, Howell F, Svitak J, Silver RA. (2007). MorphML: level 1 of the NeuroML standards for neuronal morphology data and model specification. Neuroinformatics. 5(2):96-104. https://doi.org/10.1007/s12021-007-0003-6

3. Cannon RC, Gleeson P, Crook S, Ganapathy G, Marin B, Piasini E, Silver RA. (2014). LEMS: a language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2. Front Neuroinform. 8:79. https://doi.org/10.3389/fninf.2014.00079

4. Gleeson P, Steuber V, Silver RA. (2007). neuroConstruct: A Tool for Modeling Networks of Neurons in 3D Space. Neuron. 54(2):219-235. https://doi.org/10.1016/j.neuron.2007.03.025

5. Goddard NH, Hucka M, Howell F, Cornelis H, Shankar K, Beeman D. (2001). Towards NeuroML: model description methods for collaborative modelling in neuroscience. Philos Trans R Soc Lond B Biol Sci. 356(1412):1209-1228. https://doi.org/10.1098/rstb.2001.0910