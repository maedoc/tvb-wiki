---
created: 2026-04-20
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/breakspear-2017.md
- raw/papers/ritter-2013.md
tags:
- whole-brain-modeling
- neural-mass-models
- computational-neuroscience
- software-tvb
- software-nest
- software-brian
- software-neuron
title: Co-Simulation
type: concept
updated: '2026-05-15'
---

**Co-simulation** is a computational strategy that couples multiple simulation engines to model phenomena across different spatial and temporal scales simultaneously. In [[computational-neuroscience]], co-simulation bridges the gap between detailed cellular-level [[spiking-neural-networks]] and population-level [[neural-mass-models]], enabling researchers to investigate how microscale neuronal dynamics give rise to meso- and macroscale brain activity observable in [[neuroimaging]] modalities such as [[eeg]], [[meg]], and [[fmri]].

## Motivation and Rationale

The human brain exhibits rich dynamics across multiple scales of organization, from individual ion channels and synaptic interactions to large-scale [[network-dynamics]] spanning cortical and subcortical regions. Traditional modeling approaches have often focused on either microscale detailed biophysical simulations (thousands of individually modeled neurons) or macroscale neural mass representations (where entire brain regions are reduced to single oscillatory units), but not both simultaneously Breakspear (2017).

This separation creates a fundamental limitation: macroscale models cannot capture the mechanistic details of cellular-level processes that underlie pathological states such as epilepsy, while microscale models cannot efficiently simulate the entire brain's structural [[connectivity]]. Co-simulation addresses this challenge by allowing researchers to embed detailed spiking network models within selected regions of a [[whole-brain]] neural mass framework, creating hybrid models that inherit the computational tractability of population models while retaining biological realism where it matters most Sanz Leon et al. (2013).

## Technical Framework

The mathematical framework of co-simulation involves coupling distinct dynamical systems through shared state variables. At their interface, the neural mass model provides slow oscillatory dynamics that reflect population-level activity, while the embedded spiking network contributes fast timescale fluctuations and detailed circuit motifs. The coupling is typically implemented through a master‑slave architecture, where the whole‑brain model advances the slower population dynamics and passes regional activity estimates to the spiking simulator, which then returns refined activity patterns that feed back into the next macrostate update.

Time synchronization represents a critical technical challenge in co‑simulation. Neural mass models typically operate on millisecond to second timescales suitable for capturing [[brain-oscillations]], whereas detailed spiking simulations may require microsecond resolution for accurate spike timing. Co‑simulation frameworks address this through either temporal averaging (aggregating spiking activity into population rates) or adaptive step‑sizing algorithms that dynamically adjust simulation precision based on the regime of activity.

## Implementation in The Virtual Brain

[[the-virtual-brain]] implements co‑simulation through specialized adapters that interface its macroscale neural mass models with external spiking simulators. The TVB‑NEST interface provides bidirectional coupling between TVB and the Neural Simulation Tool (NEST), allowing whole‑brain models to incorporate detailed microcircuit simulations from NEST in specified brain regions while retaining tractable neural mass dynamics across the remainder of the connectome Sanz Leon et al. (2013). Similar interfaces exist for Brian2, NEURON, [[spice]], [[simbrain]], and [[neuromllite]], providing flexibility in modeling choices.

This architecture enables several important use cases. First, researchers can investigate how specific cortical microcircuit configurations (such as alterations in [[excitation-inhibition-balance]]) propagate through the large‑scale brain network to produce observable changes in [[functional-connectivity]] patterns. Second, computational studies of [[epilepsy-modeling]] can embed detailed epileptor‑like spiking dynamics in specific regions while observing how these seizures spread through the white‑matter [[structural-connectivity]] backbone Ritter et al. (2013).

## Applications and Significance

The ability to bridge scales through co‑simulation has proven particularly valuable for clinical translation. Personalized brain models built in TVB can incorporate patient‑specific structural connectivity derived from [[dti]] [[tractography]], and co‑simulation allows these models to interrogate how individual variations in microcircuit properties contribute to disease phenotypes. This approach connects naturally to [[personalized‑brain‑modeling]] workflows where the goal is to predict individual responses to stimulation interventions or pharmacological manipulations. The resulting models can be benchmarked against empirical data using frameworks such as [[brain-score]].

Beyond clinical applications, co‑simulation provides a principled framework for testing hypotheses about scale‑crossing mechanisms in brain function. Researchers can systematically vary parameters in the microscale spiking network and observe their effects on macroscale dynamics, creating testable predictions that connect theory to empirical [[neuroimaging]] data. This positions co‑simulation as a key enabling technology for the next generation of [[whole‑brain‑modeling]] studies that aim to move beyond phenomenological descriptions toward mechanistic explanations of brain function.

## Relationship to Related Concepts

Co‑simulation is distinct from but related to several other multi‑scale modeling approaches. [[neural‑mass‑model]]s themselves can be derived as moment closures from spiking network equations under specific assumptions, creating a mathematical link between the two levels. However, co‑simulation differs from this analytical approach by maintaining explicit coupling between separate simulation engines rather than collapsing one level into the other. Similarly, [[dynamic‑causal‑modeling]] provides a framework for inferring [[effective‑connectivity]] [[trentool]] from neuroimaging data, but typically operates at a single scale; co‑simulation offers a complementary forward‑modeling approach where hypothesized mechanisms can be instantiated and their predictions compared against empirical observations.

## ORPHAN PAGE CONTEXT (simbrain)
---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2505-16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
tags:
- software-neuroscience
- [[neural-network]]
- spiking-neural‑networks
- computational-neuroscience
- visualization
- network‑dynamics
title: SimBrain
type: entity
updated: '2026-05-06'
---

SimBrain (Simulations of Neural Networks in Java) is an open‑source neural network simulator designed for building, visualizing, and simulating neural network models

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate [[brain‑network]] dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010))
2. Michael Breakspear. *Dynamic models of large‑scale brain activity*. Nature Neuroscience (Review). [DOI](https://doi.org/10.1038/s41593-017-0015-4))
3. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120))

## ORPHAN PAGE CONTEXT (brain-score)
---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/semanticscholar-9afbfd2d37be.md
tags:
- [[model-validation]]
- computational-neuroscience
- neural-network
- benchmark
- [[machine-learning]]
title: Brain-Score
type: entity
updated: '2026-05-11'
---

Brain-Score is an open-source benchmarking platform designed to systematically evaluate computational brain models against empirical neural data. The pl

## ORPHAN PAGE CONTEXT (neuromllite)
---
created: 2026-05-13
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
tags:
- software-neuroml
- software-brain-modeling
- spiking-neural-networks
- reproducibility
- connectomics
- whole-brain-modeling
- network-dynamics
title: NeuroMLlite
type: entity
updated: '2026-05-15'
---

NeuroMLlite is a lightweight Python library that enables researchers to define [[computational-neuroscience]] models using native Python syntax and