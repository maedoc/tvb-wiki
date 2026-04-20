---
title: "Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns"
created: 2026-04-20
updated: 2026-04-20
type: source
tags: [paper-methods, neural-mass-models, eeg, meg, people-researcher]
sources: []
---

# Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns

**Authors**: Benjamin H. Jansen, Vincent G. Rit  
**Published**: 1995  
**Journal**: Biological Cybernetics  
**DOI**: 10.1007/BF00199471

## Summary

Seminal paper introducing the Jansen-Rit model—a neural mass model of a single cortical column capable of generating realistic EEG/VEP signals. Now the default model in TVB for EEG/MEG simulations.

## Key Contributions

- Three-population model: pyramidal cells (excitatory), excitatory interneurons, inhibitory interneurons
- Post-synaptic impulse response functions (alpha-shaped)
- Connection to Lopes da Silva's thalamic model but adapted for cortical columns
- Generation of alpha and beta rhythms through parameter variation

## Model Structure

- Population 1 (pyramidal): receives excitation from interneurons, projects to both
- Population 2 (excitatory interneurons): receives from pyramidal, projects back
- Population 3 (inhibitory interneurons): receives from pyramidal, projects back with GABAergic inhibition

## Related Concepts

- [[Jansen-Rit]]
- [[neural mass model]]
- [[eeg]]
- [[Benjamin Jansen]]
- [[Vincent Rit]]
