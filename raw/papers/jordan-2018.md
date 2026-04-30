---
title: "Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers"
created: 2026-04-20
updated: 2026-04-20
type: source
tags: [paper-methods ,software-nest ,spiking-neural-networks ,brain-network ,whole-brain-modeling]
authors:
  - Jakob Jordan
  - Tammo Ippen
  - Moritz Helias
  - Itaru Kitayama
  - Mitsuhisa Sato
  - Jun Igarashi
  - Markus Diesmann
  - Susanne Kunkel
year: 2018
venue: Frontiers in Neuroinformatics
doi: "https://doi.org/10.3389/fninf.2018.00002"
bibtex: |
  @article{jordan2018extremely,
    title={Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers},
    author={"Jakob Jordan and Tammo Ippen and Moritz Helias and Itaru Kitayama and Mitsuhisa Sato and Jun Igarashi and Markus Diesmann and Susanne Kunkel"},
    year={2018},
    journal={Frontiers in Neuroinformatics},
    doi={https://doi.org/10.3389/fninf.2018.00002},
  }
---




# Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers

**Authors**: Jordan et al. (2018)
**Journal**: Frontiers in Neuroinformatics
**DOI**: https://doi.org/10.3389/fninf.2018.00002
**Full text**: https://doi.org/10.3389/fninf.2018.00002

## Summary

Jordan and colleagues describe a highly optimized implementation of NEST that achieves near-perfect weak scaling from consumer laptops to petascale supercomputers with hundreds of thousands of cores. The work demonstrates simulations of spiking networks containing up to 10¹¹ synapses—approaching the scale of a full human cortex—using modern high-performance computing facilities. Key algorithmic advances include a five-step communication scheme and memory-efficient data structures that minimize inter-node communication overhead. This paper establishes a computational pathway toward biologically realistic whole-brain spiking simulations on forthcoming exascale systems.

## Key Contributions

- Near-perfect weak scaling from laptops to petascale supercomputers
- Simulations up to 10¹¹ synapses (approaching human cortex scale)
- Five-step communication scheme
- Memory-efficient data structures
- Pathway toward exascale whole-brain simulations

## Related Entities

- [[NEST]]
- [[spiking neural networks]]
