---
title: Co-Simulation
created: 2026-04-20
updated: 2026-05-11
type: concept
tags: [whole-brain-modeling, neural-mass-models, computational-neuroscience, software-tvb, software-nest, software-brian, software-neuron]
sources: [raw/papers/sanz-leon-2013.md, raw/papers/breakspear-2017.md, raw/papers/ritter-2013.md]
---

**Co-simulation** is a computational strategy that couples multiple simulation engines to model phenomena across different spatial and temporal scales simultaneously. In [[computational-neuroscience]], co-simulation bridges the gap between detailed cellular-level [[spiking-neural-networks]] and population-level [[neural-mass-models]], enabling researchers to investigate how microscale neuronal dynamics give rise to meso- and macroscale brain activity observable in [[neuroimaging]] modalities such as [[eeg]], [[meg]], and [[fmri]].

## Motivation and Rationale

The human brain exhibits rich dynamics across multiple scales of organization, from individual ion channels and synaptic interactions to large-scale [[network-dynamics]] spanning cortical and subcortical regions. Traditional modeling approaches have often focused on either microscale detailed biophysical simulations (thousands of individually modeled neurons) or macroscale neural mass representations (where entire brain regions are reduced to single oscillatory units), but not both simultaneously [[raw/papers/breakspear-2017.md|Breakspear (2017)]].

This separation creates a fundamental limitation: macroscale models cannot capture the mechanistic details of cellular-level processes that underlie pathological states such as epilepsy, while microscale models cannot efficiently simulate the entire brain's structural connectivity. Co-simulation addresses this challenge by allowing researchers to embed detailed spiking network models within selected regions of a whole-brain neural mass framework, creating hybrid models that inherit the computational tractability of population models while retaining biological realism where it matters most [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Technical Framework

The mathematical framework of co-simulation involves coupling distinct dynamical systems through shared state variables. At their interface, the neural mass model provides slow oscillatory dynamics that reflect population-level activity, while the embedded spiking network contributes fast timescale fluctuations and detailed circuit motifs. The coupling is typically implemented through a master-slave architecture, where the whole-brain model advances the slower population dynamics and passes regional activity estimates to the spiking simulator, which then returns refined activity patterns that feed back into the next macrostate update.

Time synchronization represents a critical technical challenge in co-simulation. Neural mass models typically operate on millisecond to second timescales suitable for capturing [[brain-oscillations]], whereas detailed spiking simulations may require microsecond resolution for accurate spike timing. Co-simulation frameworks address this through either temporal averaging (aggregating spiking activity into population rates) or adaptive step-sizing algorithms that dynamically adjust simulation precision based on the regime of activity.

## Implementation in The Virtual Brain

[[the-virtual-brain]] implements co-simulation through specialized adapters that interface its macroscale neural mass models with external spiking simulators. The TVB-NEST interface provides bidirectional coupling between TVB and the Neural Simulation Tool (NEST), allowing whole-brain models to incorporate detailed microcircuit simulations from NEST in specified brain regions while retaining tractable neural mass dynamics across the remainder of the connectome [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Similar interfaces exist for Brian2 and NEURON, providing flexibility in modeling choices.

This architecture enables several important use cases. First, researchers can investigate how specific cortical microcircuit configurations (such as alterations in [[excitation-inhibition-balance]]) propagate through the large-scale brain network to produce observable changes in [[functional-connectivity]] patterns. Second, computational studies of [[epilepsy-modeling]] can embed detailed epileptor-like spiking dynamics in specific regions while observing how these seizures spread through the white-matter [[structural-connectivity]] backbone [[raw/papers/ritter-2013.md|Ritter et al. (2013)]].

## Applications and Significance

The ability to bridge scales through co-simulation has proven particularly valuable for clinical translation. Personalized brain models built in TVB can incorporate patient-specific structural connectivity derived from [[dti]] tractography, and co-simulation allows these models to interrogate how individual variations in microcircuit properties contribute to disease phenotypes. This approach connects naturally to [[personalized-brain-modeling]] workflows where the goal is to predict individual responses to stimulation interventions or pharmacological manipulations.

Beyond clinical applications, co-simulation provides a principled framework for testing hypotheses about scale-crossing mechanisms in brain function. Researchers can systematically vary parameters in the microscale spiking network and observe their effects on macroscale dynamics, creating testable predictions that connect theory to empirical [[neuroimaging]] data. This positions co-simulation as a key enabling technology for the next generation of [[whole-brain-modeling]] studies that aim to move beyond phenomenological descriptions toward mechanistic explanations of brain function.

## Relationship to Related Concepts

Co-simulation is distinct from but related to several other multi-scale modeling approaches. [[neural-mass-model]]s themselves can be derived as moment closures from spiking network equations under specific assumptions, creating a mathematical link between the two levels. However, co-simulation differs from this analytical approach by maintaining explicit coupling between separate simulation engines rather than collapsing one level into the other. Similarly, [[dynamic-causal-modeling]] provides a framework for inferring effective connectivity from neuroimaging data, but typically operates at a single scale; co-simulation offers a complementary forward-modeling approach where hypothesized mechanisms can be instantiated and their predictions compared against empirical observations.
