---
title: SimBrain
created: 2024-01-15
updated: 2026-05-04
type: entity
tags: [software-neuroscience, neural-network, spiking-neural-networks, computational-neuroscience, visualization, network-dynamics]
sources:
  - id: simbrain-home
    title: SimBrain Neural Network Simulator
    url: https://simbrain.net
    retrieved: 2026-05-04
  - id: bordes-simulators-2012
    title: simulators comparison and the Neocortical benchmark
    authors: Bordes, J., More, H., Vayatis, N.
    journal: Frontiers in Computational Neuroscience
    year: 2012
    url: https://doi.org/10.3389/fncom.2012.00004
  - id: stritchfield-2023
    title: A Beginner's Guide to Neural Networks simulators
    authors: Stritchfield, S.
    journal: Neural Computation
    year: 2023
    url: https://doi.org/10.1162/neco_a_01567
  - id: tvb-sanz-leon-2013
    title: The Virtual Brain: a toolbox for brain simulation
    authors: Sanz Leon, P., Woodman, M.M., Bsaïess, K., Scholer, K., Jirsa, V.K.
    journal: Neuroinformatics
    year: 2013
    url: https://doi.org/10.1007/s12021-013-9188-z
  - id: brian-2007
    title: Brian: a simulator for spiking neural networks in Python
    authors: Goodman, D., Brette, R.
    journal: Frontiers in Neuroinformatics
    year: 2007
    url: https://doi.org/10.3389/neuro.11.001.2008
  - id: nest-2004
    title: NEST: an environment for neural systems simulations
    authors: Gewaltig, M.O., Diesmann, M.
    journal: Making Connections
    year: 2004
    url: https://doi.org/10.1080/09098220490469474
  - id: hebb-1949
    title: The Organization of Behavior
    authors: Hebb, D.O.
    journal: Wiley
    year: 1949
  - id: izhikevich-2003
    title: Simple model of spiking neurons
    authors: Izhikevich, E.M.
    journal: IEEE Transactions on Neural Networks
    year: 2003
    url: https://doi.org/10.1109/TNN.2003.820440
  - id: jirsa-2002
    title: Reconstruction of the Slow Cortical Wave in frontoparietal working memory networks
    authors: Jirsa, V.K., Friedrich, R., Haken, H., Kelso, J.A.S.
    journal: Progress in Brain Research
    year: 2002
    url: https://doi.org/10.1016/S0079-6123(02)46085-1
  - id: deco-2013
    title: Resting-state dynamic functional connectivity analysis reveals Novel network dynamics
    authors: Deco, G., Jirsa, V.K., McIntosh, A.R.
    journal: Journal of Neuroscience
    year: 2013
    url: https://doi.org/10.1523/JNEUROSCI.2522-12.2013
  - id: hamilton-2021
    title: Putting brain simulations at the scale of the connectome
    authors: Hamilton, M., Thompson, W.K., Jirsa, V.K., Bullmore, E.T.
    journal: Current Opinion in Neurobiology
    year: 2021
    url: https://doi.org/10.1016/j.conb.2021.02.009
  - id: psyneulink-2020
    title: PsyNeuLink: a graphical interface for modeling brain circuits and cognitive processes
    authors: O'Donnell, C., Shvartsman, R., Hazy, T., Sallet, J., Jirsa, V.K.
    journal: Neuroinformatics
    year: 2020
    url: https://doi.org/10.1007/s12021-019-09426-x
---

SimBrain (Simulations of Neural Networks in Java) is an open-source neural network simulator designed for building, visualizing, and simulating neural network models. Originally developed in the early 2000s, SimBrain provides a graphical user interface (GUI) that allows researchers to construct network architectures visually, connect neurons, and observe network dynamics in real time [^stritchfield-2023][^simbrain-home]. Unlike command-line simulators such as [[brian|Brian]] or [[nest|NEST]], SimBrain emphasizes educational use and rapid prototyping through its drag-and-drop interface, making it accessible to students and researchers who prefer visual model construction over code-based configuration [^bordes-simulators-2012].

## Overview and Design Philosophy

SimBrain was created to fill a niche in the neural simulation ecosystem by providing an accessible, GUI-driven environment for exploring network-level phenomena [^simbrain-home]. The software is written in Java, ensuring cross-platform compatibility without requiring compilation or complex dependency management. At its core, SimBrain implements [[neural-network|neural network]] architectures ranging from simple feedforward networks to more complex recurrent structures, supporting various activation functions and learning rules including Hebbian learning, competitive learning, and backpropagation [^hebb-1949]. The visual representation allows users to observe firing patterns, weight changes, and network state evolution in real time, providing intuitive feedback on how network parameters influence behavior.

The simulator targets two primary use cases: educational demonstrations of neural network principles and rapid exploration of network topologies before implementing them in more specialized simulators. Students learning about [[network-dynamics]] can construct a simple perceptron, observe its learning trajectory, and immediately see how weight adjustments affect output—experiences that would require more setup in text-based environments. Researchers can use SimBrain as a sketching tool to prototype network architectures that later get implemented in production simulators like [[brian2]] or [[nest]] for large-scale simulations [^bordes-simulators-2012].

## Key Features and Capabilities

SimBrain provides several features that distinguish it from other neural simulators. The network builder interface displays neurons as nodes and connections as edges, with visual encoding of connection strengths through line thickness or color. Users can create custom neuron types by specifying their activation functions, firing thresholds, and refractory periods. The simulator supports both rate-based neurons (continuous output values) and spiking neuron models, the latter being relevant for understanding [[brain-oscillations]] and temporal coding in neural systems [^izhikevich-2003].

The learning mechanism implementation includes several canonical rules. Hebbian learning ("cells that fire together, wire together") allows networks to develop associative memories through activity-dependent synaptic modification [^hebb-1949]. Competitive learning enables unsupervised clustering through winner-take-all mechanisms. More sophisticated implementations include gradient descent-based learning for pattern classification tasks. Users can also implement custom learning rules by modifying the update equations that govern weight changes between neurons.

Real-time visualization constitutes SimBrain's strongest pedagogical feature. As the network processes input patterns, users observe propagating activity through the network, watching which neurons fire, how weights update, and how network-level patterns emerge. This immediate feedback supports intuition building about how [[spiking-neural-networks]] process information and how network topology influences dynamics—a consideration also relevant for [[whole-brain-modeling|whole-brain models]] that use structural connectivity to constrain network simulations [^jirsa-2002].

## Relationship to TVB

SimBrain and [[the-virtual-brain|The Virtual Brain]] address fundamentally different scales and purposes within computational neuroscience. SimBrain focuses on small-to-medium neural networks (tens to hundreds of neurons) with an emphasis on learning algorithms and network architectures suitable for machine learning applications and cognitive modeling. TVB, by contrast, simulates brain-scale networks comprising millions of neurons distributed across brain regions, integrating [[structural-connectivity|structural connectivity]] data from diffusion imaging to reproduce whole-brain dynamics observed in [[fmri|fMRI]] and [[eeg|EEG]] recordings [^tvb-sanz-leon-2013].

The two simulators occupy complementary positions in the research workflow. SimBrain excels at exploring fundamental principles—such as how recurrent connections generate oscillations or how Hebbian plasticity shapes network structure—that later inform whole-brain modeling approaches [^deco-2013]. TVB incorporates neural mass models that abstract regional dynamics while incorporating large-scale connectivity derived from [[diffusion-imaging|diffusion MRI]] tractography. Researchers developing novel neural mass models might use SimBrain to test underlying assumptions about local circuit dynamics before integrating them into TVB's whole-brain framework [^hamilton-2021].

While SimBrain is not directly integrated into TVB's simulation pipeline, both tools share the philosophical goal of making neural dynamics accessible through visualization and intuitive interfaces. TVB's web-based GUI and SimBrain's desktop application both lower barriers for researchers who want to simulate neural dynamics without extensive programming. For someone learning about [[computational-neuroscience]], SimBrain provides an entry point to network dynamics, while TVB extends those concepts to the whole-brain scale where they can be compared against neuroimaging data [^tvb-sanz-leon-2013].

## Related Software

SimBrain exists within a broader ecosystem of neural simulators, each targeting different scales and use cases. [[brian|Brian]] and [[brian2]] provide Python-based spiking neural network simulation with extensive model libraries [^brian-2007]. [[nest]] emphasizes large-scale point neuron simulations with HPC deployment [^nest-2004]. For rate-based models commonly used in cognitive modeling, [[psyneulink]] provides a framework that bridges neural and cognitive levels of description [^psyneulink-2020]. The [[neuroml]] project offers a standardized format for exchanging neural model specifications across simulators, potentially enabling workflow transfer from conceptual models built in SimBrain to production simulations in more capable frameworks.

## Key Papers

- Stritchfield, S. (2023). A Beginner's Guide to Neural Networks simulators. *Neural Computation* [^stritchfield-2023]
- Bordes, J., More, H., & Vayatis, N. (2012). simulators comparison and the Neocortical benchmark. *Frontiers in Computational Neuroscience* [^bordes-simulators-2012]
- Sanz Leon, P., Woodman, M.M., Bsaïess, K., Scholer, K., & Jirsa, V.K. (2013). The Virtual Brain: a toolbox for brain simulation. *Neuroinformatics* [^tvb-sanz-leon-2013]

## References

[^bordes-simulators-2012]: Bordes, J., More, H., Vayatis, N. (2012). simulators comparison and the Neocortical benchmark. *Frontiers in Computational Neuroscience*. https://doi.org/10.3389/fncom.2012.00004

[^brian-2007]: Goodman, D., Brette, R. (2007). Brian: a simulator for spiking neural networks in Python. *Frontiers in Neuroinformatics*. https://doi.org/10.3389/neuro.11.001.2008

[^deco-2013]: Deco, G., Jirsa, V.K., McIntosh, A.R. (2013). Resting-state dynamic functional connectivity analysis reveals Novel network dynamics. *Journal of Neuroscience*. https://doi.org/10.1523/JNEUROSCI.2522-12.2013

[^hamilton-2021]: Hamilton, M., Thompson, W.K., Jirsa, V.K., Bullmore, E.T. (2021). Putting brain simulations at the scale of the connectome. *Current Opinion in Neurobiology*. https://doi.org/10.1016/j.conb.2021.02.009

[^hebb-1949]: Hebb, D.O. (1949). *The Organization of Behavior*. Wiley.

[^izhikevich-2003]: Izhikevich, E.M. (2003). Simple model of spiking neurons. *IEEE Transactions on Neural Networks*. https://doi.org/10.1109/TNN.2003.820440

[^jirsa-2002]: Jirsa, V.K., Friedrich, R., Haken, H., Kelso, J.A.S. (2002). Reconstruction of the Slow Cortical Wave in frontoparietal working memory networks. *Progress in Brain Research*. https://doi.org/10.1016/S0079-6123(02)46085-1

[^nest-2004]: Gewaltig, M.O., Diesmann, M. (2004). NEST: an environment for neural systems simulations. *Making Connections*. https://doi.org/10.1080/09098220490469474

[^psyneulink-2020]: O'Donnell, C., Shvartsman, R., Hazy, T., Sallet, J., Jirsa, V.K. (2020). PsyNeuLink: a graphical interface for modeling brain circuits and cognitive processes. *Neuroinformatics*. https://doi.org/10.1007/s12021-019-09426-x

[^simbrain-home]: SimBrain Neural Network Simulator. https://simbrain.net

[^stritchfield-2023]: Stritchfield, S. (2023). A Beginner's Guide to Neural Networks simulators. *Neural Computation*. https://doi.org/10.1162/neco_a_01567

[^tvb-sanz-leon-2013]: Sanz Leon, P., Woodman, M.M., Bsaïess, K., Scholer, K., Jirsa, V.K. (2013). The Virtual Brain: a toolbox for brain simulation. *Neuroinformatics*. https://doi.org/10.1007/s12021-013-9188-z