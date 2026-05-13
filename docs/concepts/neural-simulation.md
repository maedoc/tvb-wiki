---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-b9acfa0a7c80.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/sanz-leon-2013.md
tags:
- neural-simulation
- computational-neuroscience
- spiking-neural-networks
- neural-mass-model
- whole-brain-modeling
title: Neural Simulation
type: concept
updated: '2026-05-13'
---

# Neural Simulation

**Neural simulation** is the computational modeling of brain activity at levels ranging from individual neurons to entire brain networks. It provides a way to formalize theories of brain function, generate testable predictions, and link molecular and cellular mechanisms to behavior and cognition.

## Levels of Simulation

| Scale | Resolution | Examples | Tools |
|-------|-----------|----------|-------|
| Molecular | Ion channels, synapses | Hodgkin–Huxley, Markov models | NEURON, MOOSE |
| Single neuron | Compartmental models | Multi-compartment morphological models | NEURON, Arbor |
| Microcircuit | 10³–10⁵ neurons | Cortical columns, barrel cortex | NEST, Brian2 |
| Mesoscale | 10⁶–10⁸ neurons | Brain regions, area-level dynamics | TVB, ANNarchy |
| Macroscale / Whole brain | 10⁸–10¹¹ neurons | Global brain dynamics, cognition | [[the-virtual-brain|TVB]], TheBrain |

## Relationship to TVB

TVB operates primarily at the **macroscale** level, simulating whole-[[brain-dynamics]] using neural mass and [[mean-field-theory|mean-field]] models:
- TVB can **couple to microscale simulators** ([[nest]], [[nestml]], [[brian2]]) via co-simulation interfaces
- TVB's [[neural-mass-models]] are **derived from** lower-level spiking dynamics using mean-field approximations
- TVB integrates [[structural-connectivity]] data to constrain large-scale network simulations
- TVB generates predictions at the level of [[bold-signal|BOLD]] [[fmri]], EEG, and MEG that can be compared to empirical [[neuroimaging]]

## Related

Neural simulation spans a hierarchy of scales that are tightly coupled in practice. At the macroscale, whole-brain network modeling combines computational models of brain dynamics with individual brain imaging data to coordinate network nodes, advancing understanding of complex brain dynamics and their neurobiological underpinnings [[raw/papers/semanticscholar-b9acfa0a7c80.md|Ziaeemehr et al. (2025)]]. The [[the-virtual-brain|Virtual Brain]] (TVB) is a key platform in this space, integrating empirical [[structural-connectivity]] derived from diffusion MRI tractography with [[neural-mass-model|neural mass models]] to simulate large-scale primate brain network dynamics [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. These population-level approximations make whole-brain simulation computationally tractable while remaining conceptually linked to [[spiking-neural-networks|spiking]] and single-[[neuron]] dynamics. TVB further bridges simulation and empirical neuroscience by providing forward models for [[neuroimaging-eeg|EEG]], [[neuroimaging-meg|MEG]], and [[neuroimaging-fmri|fMRI]], allowing synthetic signals to be compared directly against empirical recordings [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. Despite this progress, a critical need remains for automated model inversion tools that can estimate control and [[bifurcation-analysis|bifurcation]] parameters at large scales, given the varying spatio-temporal resolutions of different [[neuroimaging]] modalities [[raw/papers/semanticscholar-b9acfa0a7c80.md|Ziaeemehr et al. (2025)]]. The Virtual Brain Inference (VBI) toolkit was introduced to fill this gap, providing efficient [[bayesian|Bayesian]] inference and uncertainty quantification to enhance the predictive power of virtual brain models for applications in precision medicine [[raw/papers/semanticscholar-b9acfa0a7c80.md|Ziaeemehr et al. (2025)]]. Taken together, these developments situate whole-brain simulation within the broader field of [[computational-neuroscience|computational neuroscience]], where the interplay between theory, simulation, and data continues to drive the field toward biophysically interpretable models of brain function.

## References

1. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on whole-brain models*. eLife. [DOI](](https://doi.org/10.7554/eLife.106194))
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.01.21.633922))
3. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))