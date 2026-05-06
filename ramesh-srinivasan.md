---
title: Ramesh Srinivasan
created: 2026-04-20
updated: 2026-05-06
type: entity
tags: [people-researcher, neuroimaging-eeg, brain-dynamics, neural-mass-models, computational-neuroscience]
sources: [raw/papers/nunez-srinivasan-2006.md]
---

Ramesh Srinivasan is a researcher in computational neuroscience and electrophysiology whose work on the neurophysics of EEG, brain wave dynamics, and the theoretical foundations of brain connectivity has significantly influenced [[whole-brain modeling]] and [[connectomics]].

## Overview

Ramesh Srinivasan is a Professor of Cognitive Sciences with a joint appointment in Biomedical Engineering at the University of California, Irvine. His research focuses on understanding the relationship between brain structure and function as measured by electrophysiological techniques, particularly [[eeg]] and [[meg]]. He is best known for his collaboration with Paul Nunez on the theoretical framework for understanding EEG signals in terms of cortical dynamics and [[brain-dynamics]].

## Scientific Contributions

### Neurophysics of EEG

Srinivasan's work, most notably in the textbook "Electric Fields of the Brain: The Neurophysics of EEG" (Oxford University Press, 2006), co-authored with Paul Nunez, provides a comprehensive theoretical framework for understanding how [[neuroimaging-eeg]] signals arise from cortical activity. This work establishes the physical and physiological basis for interpreting scalp potentials in terms of synaptic action fields in the neocortex, connecting microscopic neural activity to macroscopic measurements.

The framework treats EEG as arising from [[synaptic-plasticity]] and [[neural-mass-model|neural mass]] activity across large-scale cortical networks. This approach is foundational for [[whole-brain modeling]] because it provides the link between the [[structural-connectivity]] measured via [[dti]]/[[diffusion-imaging]] and the [[functional-connectivity]] observed in [[resting-state-fmri]] and EEG recordings.

### Brain Wave Theory

A major focus of Srinivasan's research has been on characterizing brain waves—both traveling waves and standing waves—as fundamental modes of neocortical dynamics. This work extends the [[neural-field-theory]] approach pioneered by [[jansen-rit-model|Jansen and Rit]] and others, providing a mathematical framework for understanding how global brain dynamics emerge from [[cortico-cortical]] interactions.

The theoretical framework predicts that EEG oscillations arise from a combination of:

- **Standing waves**: Resonant oscillations of the [[cortical-sheet]] with characteristic frequencies determined by the geometry and excitability of the cortex
- **Traveling waves**: Propagating disturbances of synaptic activity that traverse the cortex at speeds of approximately 5–10 m/s, reflecting the velocity of signal propagation in long-range [[white-matter]] fibers

This work connects directly to [[brain-oscillations]] research and informs [[neural-mass-models]] used in [[whole-brain-simulators]] like [[the-virtual-brain]].

### Structural-Functional Connectivity

Srinivasan has contributed substantially to understanding the relationship between [[structural-connectivity]] and [[functional-connectivity]] in the brain. His work demonstrates that the brain's dense network of [[cortico-cortical]] axons (approximately 10^10 fibers) creates a "small-world" network architecture that enables both local specialization and global integration of neural activity.

This research is highly relevant to [[connectomics]] and [[personalized-brain-modeling]], as it provides a theoretical basis for understanding how individual differences in [[white-matter]] structure (as measured by [[diffusion-imaging]] and [[tractography]]) relate to differences in brain dynamics and cognitive function.

### Neurocognitive Modeling

More recently, Srinivasan has worked on integrating [[eeg]] with computational models of cognition, particularly [[drift-diffusion model]]s of perceptual decision-making. This work demonstrates how trial-by-trial variability in EEG signals can reveal the latent cognitive processes underlying decision-making, including evidence accumulation rates and visual encoding time.

This approach represents an important bridge between [[computational-psychiatry]] and cognitive neuroscience, potentially enabling more principled integration of brain imaging data with cognitive models.

## Key Publications

- Nunez, P.L. & **Srinivasan, R.** (2006). *Electric Fields of the Brain: The Neurophysics of EEG* (2nd ed.). Oxford University Press.
- Srinivasan, R., Winter, W.R., Ding, J., & Nunez, P.L. (2007). EEG and MEG coherence: measures of functional connectivity at distinct spatial scales of neocortical dynamics. *Journal of Neuroscience Methods*.
- Nunez, M.D., **Srinivasan, R.**, & Vandekerckhove, J. (2015). Individual differences in attention influence perceptual decision making. *Frontiers in Psychology*.

## Relationship to TVB

While Srinivasan's work is not directly developed within The Virtual Brain (TVB) framework, his theoretical contributions to EEG neurophysics and brain wave dynamics provide foundational concepts that inform [[whole-brain-modeling]] approaches. Specifically:

1. **Neural mass models**: The [[neural-mass-model|neural mass]] formulations used in TVB build upon the same theoretical foundations that Srinivasan and Nunez established for relating cortical synaptic activity to scalp EEG.

2. **Connectivity frameworks**: His work on the relationship between [[structural-connectivity]] and [[functional-connectivity]] informs TVB's approach to integrating [[dti]]-derived connectivity matrices with [[neural-dynamics]] simulations.

3. **Brain oscillations**: The emphasis on [[brain-oscillations]] and traveling waves provides a theoretical basis for understanding the rhythms generated by TVB's [[epileptor]] and other [[neural-mass-model]] implementations.

4. **Personalized modeling**: His work on individual differences in brain structure-function relationships supports the [[personalized-brain-modeling]] paradigm that TVB enables.

## Related Concepts

- [[eeg]]
- [[meg]]
- [[neuroimaging-eeg]]
- [[brain-dynamics]]
- [[brain-oscillations]]
- [[neural-mass-models]]
- [[neural-field-theory]]
- [[whole-brain-modeling]]
- [[structural-connectivity]]
- [[functional-connectivity]]
- [[connectome]]
- [[resting-state]]
- [[the-virtual-brain]]
- [[personalized-brain-modeling]]