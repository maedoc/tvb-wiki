---
title: SpiNNaker
created: 2023-01-15
updated: 2026-04-30
type: entity
tags: [spiking-neural-networks, neuromorphic-computing, computational-neuroscience]
sources: [Furber et al., 2014, Davison et al., 2009, Rhodes et al., 2020, Muller et al., 2022]
---

# SpiNNaker

## Overview

SpiNNaker (Spiking Neural Network Architecture) is a massively parallel, brain-inspired neuromorphic computing platform developed at the University of Manchester, UK. The system comprises over one million low-power ARM processor cores interconnected via a specialized multicast network, enabling the real-time simulation of large-scale spiking neural networks at the scale of a mouse brain—approximately 1% of the human brain when using moderately complex neuron models such as the cortical microcircuit model developed by the Human Brain Project [Furber et al., 2014](#references). Conceived in the early 2000s by Professor Steve Furber and his team, SpiNNaker represents one of the largest neuromorphic computing installations in the world and serves as a unique research instrument for computational neuroscientists, roboticists, and researchers exploring brain-inspired artificial intelligence.

## Key Features

The architectural innovation of SpiNNaker lies in its brain-inspired communication fabric. Unlike conventional supercomputers that rely on high-bandwidth point-to-point connections, SpiNNaker employs a specialized multicast network capable of broadcasting small data packets—representing individual neural spikes—to many destinations simultaneously [Furber et al., 2014](#references). Each packet explicitly carries the source neuron identifier and implicitly the spike timing, enabling event-driven computation that closely mimics the asynchronous communication patterns observed in biological neural tissue. This design allows the system to handle the massive combinatorial explosion of synaptic connectivity that characterizes large-scale brain models, where each neuron may connect to thousands of others.

The system features approximately one million ARM968 processors arranged in 1200 boards, with each processor capable of modeling several hundred neurons and several million synapses. This architecture achieves real-time simulation speeds for whole-brain scale models that would otherwise require much larger and more power-hungry traditional supercomputers. SpiNNaker supports the PyNN standard application programming interface, allowing researchers to write neural network models once and execute them across different neuromorphic backends [Davison et al., 2009](#references), promoting code reuse and collaboration within the computational neuroscience community.

## Relationship to TVB

While SpiNNaker and [[the-virtual-brain]] (TVB) serve complementary roles in computational neuroscience, they occupy distinct positions in the modeling hierarchy. TVB operates as a whole-brain simulation platform that typically runs on conventional clusters or cloud infrastructure, emphasizing the integration of large-scale connectome data with neural mass models to generate simulated neuroimaging signals (fMRI, EEG, MEG). In contrast, SpiNNaker focuses on lower-level spiking neural network simulations with greater biological fidelity, simulating individual neurons and synapses in real time. That said, both platforms share the common goal of understanding brain dynamics through large-scale simulation, and researchers have explored interfacing TVB's population-level dynamics with SpiNNaker's neuron-level resolution for multi-scale modeling approaches. Additionally, both tools are accessible through the [[ebrains]] infrastructure, which provides unified access to European brain research resources [Muller et al., 2022](#references).

## Key Papers

The foundational reference for SpiNNaker is the IEEE Proceedings article "The SpiNNaker Project" (Furber et al., 2014), which describes the machine's architecture, programming model, and early applications. This paper established SpiNNaker's reputation as a transformative tool for real-time brain simulation and has been cited extensively in both the neuromorphic computing and computational neuroscience literature. Subsequent work has demonstrated the system's capabilities in modeling various brain phenomena, including cortical microcircuits, cerebellar networks, and basal ganglia circuits relevant to Parkinson's disease. The Human Brain Project featured SpiNNaker as a core technology within its neuromorphic computing portfolio [Rhodes et al., 2020](#references), and the system now operates as a community resource under the EBRAINS infrastructure.

## Comparison with Other Neuromorphic Platforms

SpiNNaker occupies a distinct niche in the landscape of neuromorphic computing systems. Unlike BrainScaleS (developed at Heidelberg University), which uses analog circuits to emulate neuronal dynamics at speeds approximately 10,000 times faster than biological real-time, SpiNNaker prioritizes exact real-time operation that aligns with biological timing—a property particularly valuable for closed-loop robotics and brain-machine interface applications. In contrast, Intel's Loihi and IBM's TrueNorth take a more radical approach, using purely digital, event-based silicon that achieves extreme energy efficiency but with more abstract neuron models. SpiNNaker's advantage lies in its flexibility: researchers can implement nearly arbitrary neuron and synapse dynamics in software running on general-purpose ARM cores, making it well-suited for exploring diverse neural coding schemes and plasticity rules without hardware redesign.

## Limitations

Despite its architectural innovations, SpiNNaker has several practical limitations that researchers must consider. Power consumption scales with the number of active cores, and while individual ARM processors are energy-efficient, a machine with one million cores still requires substantial electrical power and cooling infrastructure—the current installation consumes on the order of tens of kilowatts. Finite on-chip memory (approximately 64 KB per processor) constrains the complexity of synaptic models that can be implemented, particularly for models with sophisticated multi-component dynamics or conductance-based synapses. Finally, achieving real-time performance depends heavily on model complexity: simple rate-based or leaky integrate-and-fire neurons can simulate at brain scale, but more biologically detailed models (with dendritic compartments, multiple ion channels, or STDP learning rules) may require significantly more processing time and cannot always achieve true real-time operation without compromising model fidelity.

## Software Ecosystem

SpiNNaker's software stack provides comprehensive tools for developing and deploying spiking neural network models. The system supports the [[pynn]] interface, enabling users to define neural models using a standardized API that abstracts away hardware-specific details [Davison et al., 2009](#references). Both SpiNNaker and [[nest]] support the PyNN standard, meaning that models written in PyNN can target either backend for execution—though NEST simulations run on conventional CPUs, not directly on SpiNNaker hardware. Supporting applications include tools for robotic control where real-time neural processing enables responsive behaviors in autonomous systems. The platform has also been used to explore novel learning algorithms for event-based machine learning, with potential applications in energy-efficient AI for mobile and embedded systems.

## Related Software

The broader ecosystem of neuromorphic and spiking neural network tools complements SpiNNaker in important ways. [[neuromorphic-computing]] encompasses the broader field of brain-inspired hardware, while [[spiking-neural-networks]] provides the theoretical foundation for the models simulated on SpiNNaker. For [[whole-brain-modeling]], researchers often combine SpiNNaker with platforms like [[the-virtual-brain]] to achieve multi-scale simulations that bridge neuron-level and population-level dynamics. The [[computational-neuroscience]] community benefits from interoperability between SpiNNaker, [[nest]] (a popular CPU-based simulator), and [[brian]] (a flexible Python-based spiking network simulator), all of which support the PyNN API [Davison et al., 2009](#references). These tools are increasingly accessible through [[ebrains]], which provides a unified research infrastructure for the European brain research community.

## References

- Furber, S. B., Galluppi, F., Temple, S., & Plana, L. A. (2014). The SpiNNaker Project. *Proceedings of the IEEE*, 102(5), 652-665. DOI: 10.1109/JPROC.2014.2304638
- Davison, A. P., Brüderle, D., Eppler, J. M., Kremkow, J., Muller, E., Pecevski, D., ... & Schemmel, J. (2009). PyNN: A common interface for neuronal network simulators. *Frontiers in Neuroinformatics*, 2, 11. DOI: 10.3389/neuro.11.011.2008
- Rhodes, O., Bogdan, P. A., Brenninkmeijer, C., Callender, S., Davidson, M., Fellows, P., ... & Furber, S. B. (2020). spynnaker: A Spiking Neural Network Modelling Framework in Python. *Frontiers in Neuroscience*, 14, 617. DOI: 10.3389/fnins.2020.00617
- Muller, E., Bouvier, M., Dzack, M., Wierenga, K., Grässler, A., Sadr, S., ... & Heppt, J. (2022). EBRAINS: A European Research Infrastructure for Brain Research and Brain-Inspired Intelligence. arXiv preprint arXiv:2206.14498.