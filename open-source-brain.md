---
title: Open Source Brain
created: 2024-01-15
updated: 2026-04-27
type: entity
tags: [software-modeldb, open-question, reproducibility, software-neuroml, software-pynn, spiking-neural-networks, computational-neuroscience, database-modeldb]
sources:
  - "[Gleeson et al. 2019] Gleeson, P., Cantarelli, M., Marin, B., et al. (2019). Open Source Brain: A Collaborative Resource for Visualizing, Analyzing, Simulating, and Developing Standardized Models of Neurons and Circuits. Neuron, 103(3), 530-544. https://doi.org/10.1016/j.neuron.2019.05.019"
  - "[ModelDB] Hines, M.L., Morse, T., Migliore, M., Carnevale, N.T., & Shepherd, G.M. (2004). ModelDB: A Database to Support Computational Neuroscience. Journal of Computational Neuroscience, 17(1), 7-11. https://doi.org/10.1023/B:JCNS.0000023869.22017.2e"
  - "[EBRAINS] Amunts, K., et al. (2024). The coming decade of digital brain research. A vision for neuroscience at the intersection of technology and computing. Imaging Neuroscience, 2(1). https://doi.org/10.1162/imag_a_00265"
  - "[NeuroML] Gleeson, P., et al. (2025). The NeuroML ecosystem for standardized multi-scale modeling in neuroscience. eLife, 14. https://doi.org/10.7554/eLife.102621"
  - "[TVB] Sanz-Leon, P., et al. (2015). The Virtual Brain: a modelling platform for brain dynamics. International Journal of Psychophysiology, 86(3), 312. https://doi.org/10.1016/j.ijpsycho.2015.07.015"
---

Open Source Brain (OSB) is an online repository and collaborative platform for sharing, developing, and versioning computational models of neurons and neural circuits. Founded in the early 2010s as part of a broader movement toward open science in neuroscience, OSB provides a centralized hub where researchers can publish neural simulation code in standardized formats, enabling reproducibility, reuse, and collaborative refinement of models [Gleeson et al. 2019]. The platform addresses a fundamental challenge in computational neuroscience: the difficulty of reproducing published models due to inconsistent documentation, proprietary code, and the lack of standardized formats for exchanging neuronal models across different simulators.

The motivation for Open Source Brain emerged from growing concerns about reproducibility in computational neuroscience and the fragmented landscape of neural modeling tools. Historically, neuronal models were shared primarily through supplementary materials in journal articles or through informal channels, making it difficult for other researchers to obtain, understand, and build upon existing work. OSB was conceived as a solution analogous to GitHub but specifically tailored for computational neuroscience, incorporating version control, community features, and integration with standardization initiatives like [[neuroml]] and [[pynn]] [Gleeson et al. 2019]. By providing persistent identifiers, clear licensing, and standardized model descriptions, OSB aims to lower the barrier to model sharing and accelerate the accumulation of reproducible knowledge in the field.

## Key Features

Open Source Brain provides several features designed to support collaborative neural model development. The platform hosts model code in multiple formats, with strong support for [[neuroml]]—a standardized language for describing neuronal models [NeuroML]—and PyNN, a Python interface that allows the same model code to run on multiple simulators including [[neuron-simulator]], [[brian]], and [[nest]]. This multi-simulator capability is particularly valuable because it enables users to verify that models behave consistently across different simulation engines and to compare the performance and numerical accuracy of different implementations [Gleeson et al. 2019].

Models hosted on OSB are typically organized into repositories that include not only the model code but also documentation, example scripts, and metadata describing the model structure, parameters, and original source literature. The platform integrates with version control systems, allowing researchers to track changes, branch variants, and merge improvements from collaborators. Many models on OSB are linked to published papers, creating a direct connection between the archived simulation code and the scientific literature. This integration supports the broader goal of reproducible neuroscience by ensuring that the computational basis of published findings remains accessible and tweakable by the community.

The platform also serves an educational function, providing concrete examples that students and new researchers can study, modify, and extend. By seeing well-documented model implementations, newcomers to computational neuroscience can learn best practices in model construction, documentation, and sharing. The collaborative aspect allows for community-driven improvements, bug fixes, and extensions that would not be possible with traditionally published static code.

## Relationship to TVB

Open Source Brain and [[the-virtual-brain]] (TVB) serve complementary but distinct roles in the computational neuroscience ecosystem. While OSB focuses on models of individual neurons and small circuits—particularly [[spiking-neural-networks]] and neural mass models at the cellular level—TVB operates at the scale of whole-brain modeling, simulating large-scale brain networks composed of multiple brain regions connected by [[structural-connectivity]] derived from diffusion imaging [TVB]. OSB models are typically used to understand the intrinsic dynamics of specific neuronal populations or microcircuits, whereas TVB integrates such local dynamics into a whole-brain framework to study emergent network-level phenomena including [[brain-oscillations]], [[resting-state]] dynamics, and pathological states such as [[epilepsy-modeling]].

The relationship between the two platforms is primarily indirect but conceptually important. Neuronal models developed and shared on OSB can inform the local dynamics used in TVB simulations—researchers may derive neural mass or mean-field approximations from detailed spiking network models found in OSB repositories. Additionally, both platforms share a commitment to open science and reproducibility, and both contribute to the broader EBRAINS infrastructure that aims to integrate European neuroscience resources [EBRAINS]. TVB's emphasis on whole-brain simulation and OSB's focus on cellular-scale modeling represent different levels of analysis that must ultimately be bridged to achieve a complete understanding of brain function. Recent integration work between TVB and NeuroML has begun to enable more seamless translation of cellular-level models from OSB into the large-scale network frameworks used in TVB [TVB][NeuroML].

## Notable Models and Contributions

OSB hosts a diverse collection of neural models spanning multiple levels of complexity. At the single-neuron level, models of [[izhikevich-neuron-model]], Hodgkin-Huxley-type neurons, and adaptive exponential integrate-and-fire neurons provide canonical examples of different neuronal dynamics. At the network level, repositories include models of cortical microcircuits, hippocampal formations, and various sensory systems. The platform has become a canonical destination for researchers seeking published neuronal models for secondary analysis or as building blocks for larger simulations.

The availability of these models has enabled new research directions that depend on systematically comparing across models, testing hypotheses in multiple model implementations, and building larger composite models from vetted components. This modular approach to neural modeling, while still developing, represents a shift in computational neuroscience toward more collaborative and cumulative model development—a shift that OSB has helped enable.

## Related Software and Platforms

Several related tools and platforms share overlapping goals with Open Source Brain. [[modeldb]] is a similar repository for computational neuroscience models, originally developed at Yale and now part of the OpenBrain ecosystem [ModelDB]. [[neuroml]] and [[pynn]] are standardization efforts that OSB heavily leverages—NeuML provides the XML-based language for specifying models [NeuroML], while PyNN provides the simulator-agnostic API. The broader EBRAINS platform integrates OSB with other neuroscience resources including data repositories, simulation engines, and analysis tools [EBRAINS]. For visualization and analysis, tools like [[brain Connectivity Toolbox|bctpy]] and [[graphvar]] complement the model development workflow by providing network analysis capabilities applicable to the outputs of neural simulations.

## Open Questions and Challenges

Despite its contributions, Open Source Brain faces ongoing challenges shared with the broader field of computational model sharing. The effort required to document models comprehensively—specifying all parameters, justifying choices, and ensuring the code runs on current software versions—remains a significant barrier to contributions. Determining appropriate levels of model abstraction for different scientific questions, and clearly communicating these choices to users, continues to require careful curation. The long-term maintenance of archived models also poses challenges, as simulator APIs evolve and dependencies change. Nonetheless, OSB remains a pioneering effort in the movement toward reproducible, collaborative computational neuroscience.

## Key Papers

The following publications represent landmark contributions related to Open Source Brain and its ecosystem:

1. **Gleeson et al. (2019)**: "Open Source Brain: A Collaborative Resource for Visualizing, Analyzing, Simulating, and Developing Standardized Models of Neurons and Circuits" - The foundational paper describing OSB's architecture, features, and role in computational neuroscience [Gleeson et al. 2019].

2. **Hines et al. (2004)**: "ModelDB: A Database to Support Computational Neuroscience" - The seminal paper on ModelDB, establishing the concept of a curated model repository in computational neuroscience [ModelDB].

3. **Gleeson et al. (2025)**: "The NeuroML ecosystem for standardized multi-scale modeling in neuroscience" - Recent review of the NeuroML standardization efforts that underpin OSB's model exchange capabilities [NeuroML].

4. **Amunts et al. (2024)**: "The coming decade of digital brain research" - Describes the broader EBRAINS infrastructure of which OSB is a component [EBRAINS].

5. **Sanz-Leon et al. (2015)**: "The Virtual Brain: a modelling platform for brain dynamics" - Foundational TVB publication describing whole-brain simulation methodology [TVB].

## References

[Gleeson et al. 2019] Gleeson, P., Cantarelli, M., Marin, B., et al. (2019). Open Source Brain: A Collaborative Resource for Visualizing, Analyzing, Simulating, and Developing Standardized Models of Neurons and Circuits. Neuron, 103(3), 530-544. https://doi.org/10.1016/j.neuron.2019.05.019

[ModelDB] Hines, M.L., Morse, T., Migliore, M., Carnevale, N.T., & Shepherd, G.M. (2004). ModelDB: A Database to Support Computational Neuroscience. Journal of Computational Neuroscience, 17(1), 7-11. https://doi.org/10.1023/B:JCNS.0000023869.22017.2e

[EBRAINS] Amunts, K., et al. (2024). The coming decade of digital brain research. A vision for neuroscience at the intersection of technology and computing. Imaging Neuroscience, 2(1). https://doi.org/10.1162/imag_a_00265

[NeuroML] Gleeson, P., et al. (2025). The NeuroML ecosystem for standardized multi-scale modeling in neuroscience. eLife, 14. https://doi.org/10.7554/eLife.102621

[TVB] Sanz-Leon, P., et al. (2015). The Virtual Brain: a modelling platform for brain dynamics. International Journal of Psychophysiology, 86(3), 312. https://doi.org/10.1016/j.ijpsycho.2015.07.015