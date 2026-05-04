---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-b9acfa0a7c80.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/arxiv-2506.22951.md
tags:
- connectomics
- structural-connectivity
- functional-connectivity
- effective-connectivity
- network-dynamics
- whole-brain-modeling
- graph-theory
- computational-neuroscience
- neural-mass-models
- brain-network
title: Network Neuroscience
type: concept
updated: '2026-05-04'
---

Network neuroscience is an interdisciplinary field that applies graph theory and network science to understand brain structure and function as interconnected systems. Rather than studying individual neurons or brain regions in isolation, network neuroscience treats the brain as a complex network of nodes (neurons, populations, or brain regions) linked by edges (synapses, white matter tracts, or statistical dependencies), enabling analysis of emergent properties such as [[small-world-networks]], [[rich-club]] organization, modularity, and [[network-hubs]] [@doi:10.1038/nrn2576].

## Overview

The field emerged from the convergence of several developments: advances in [[neuroimaging]] that enabled mapping of [[structural-connectivity]] via [[diffusion-imaging]] and [[tractography]]; the availability of large-scale datasets such as the [[human-connectome-project]] and [[uk-biobank]]; and theoretical advances in [[graph-theory]] applied to biological networks. Network neuroscience provides a unifying framework for understanding how the brain's anatomical wiring gives rise to [[functional-connectivity]] patterns measured by [[fmri]], [[eeg]], or [[meg]], and how these patterns support cognition, behavior, and clinical outcomes [@doi:10.1038/nn.4502].

The "toolkit" aspect of network neuroscience refers to the collection of methodological approaches, software packages, and analytical frameworks that researchers use to construct, analyze, and simulate brain networks. Unlike a single software platform, network neuroscience represents a paradigm that spans multiple tools including the [[brain-connectivity-toolbox]], [[bctpy]], [[graph-tool]], [[brainspace]], and [[braph]].

## Core Concepts

### Nodes and Edges

The fundamental representation in network neuroscience is the brain graph, where **nodes** correspond to neural elements (individual neurons, neuronal populations, or anatomically defined brain regions) and **edges** represent the connections between them. The nature of edges defines the type of connectivity being modeled: **structural connectivity** uses white matter tracts reconstructed from [[diffusion-mri]] to represent anatomical links; **functional connectivity** uses statistical dependencies (correlation, coherence, or mutual information) between time series measured by [[neuroimaging]] or electrophysiology; **effective connectivity** attempts to infer causal interactions, often within the framework of [[dynamic-causal-modeling]] [@doi:10.1016/j.neuroimage.2010.02.045].

### Network Metrics

Network neuroscience employs a rich set of quantitative metrics to characterize brain networks. **Topology** measures include degree (number of connections per node), [[modularity]] (the degree to which the network partitions into functional communities), clustering coefficient (the tendency of nodes to form local triangles), path length (the average distance between node pairs), and centrality measures (degree centrality, betweenness, eigenvector) that identify [[network-hubs]] [@doi:10.1523/JNEUROSCI.3689-12.2013]. **Geometry** measures incorporate the spatial position of nodes in anatomical space, examining the tradeoff between wiring economy and topological integration. **Dynamics** on networks study how activity propagates through the structural topology, relevant to models of [[brain-oscillations]], [[epilepsy-modeling]], and [[seizure-prediction]].

### Multi-Scale Organization

A key insight from network neuroscience is that brain networks exhibit hierarchical organization across multiple spatial scales. At the microscale, individual neurons form [[spiking-neural-networks]] with synaptic connectivity. At the mesoscale, cortical columns and microcircuits contain recurrent [[excitation-inhibition-balance]] architectures. At the macroscale, distributed brain regions form [[default-mode-network]] and other large-scale networks observable in [[resting-state]] [[fmri]]. The [[connectome]] concept attempts to provide a complete description of neural connectivity across scales [@doi:10.1038/nn.4502].

## Relationship to Whole-Brain Modeling

Network neuroscience provides the structural foundation for [[whole-brain-modeling]] approaches implemented in software such as [[the-virtual-brain]]. In TVB and similar [[whole-brain-simulators]], the brain's anatomical connectivity matrix (derived from [[diffusion-imaging]] data) serves as the substrate on which [[neural-mass-models]] or [[neural-field-theory]] dynamics are simulated. The [[epileptor]] model, for example, uses a network of brain regions to study seizure propagation, while the [[wong-wang-model]] implements [[neural-mass-models]] with [[excitation-inhibition-balance]] on structural connectomes to generate simulated [[resting-state]] activity.

The relationship is bidirectional: network analysis characterizes empirical brain organization, while [[whole-brain-modeling]] tests hypotheses about how network structure generates functional dynamics. Model validation often proceeds by comparing simulated functional connectivity patterns—computed from model-generated time series—against empirical functional connectivity estimates derived from fMRI or electrophysiological recordings. Parameter fitting in whole-brain models frequently uses network-level metrics (modularity, hub topology, path length) as optimization targets, enabling researchers to infer biologically plausible parameter regimes from observed network architecture. This bidirectional feedback loop between network analysis and brain modeling drives research in [[personalized-brain-modeling]], where individual [[structural-connectivity]] estimates inform patient-specific simulations for clinical applications in [[epilepsy-modeling]] and [[alzheimers-modeling]] [@doi:10.1038/nn.4502].

## Key Software Tools

Several software packages implement network neuroscience methods:

- [[brainsuite]] (BCT): MATLAB toolbox for complex network analysis
- [[bctpy]]: Python implementation of BCT functions
- [[brainspace]]: Python library for mapping [[connectivity]] patterns
- [[braph]]: Graph-theoretic analysis of brain connectivity in MATLAB/Python
- [[graph-tool]]: Efficient Python library for statistical analysis of networks

For network reconstruction from neuroimaging data, researchers use packages like [[mrtrix3-connectome]] (for tractography-based connectivity), [[dipy]] (for [[diffusion-mri]] processing), and nilearn (for functional connectivity matrices). Visualization tools include [[brainnet-viewer]] and [[connectome-workbench]].

## Key Papers

Foundational references in network neuroscience include:

- Bassett & Sporns (2017). "Network neuroscience." *Nature Neuroscience* [@doi:10.1038/nn.4502]
- Bullmore & Sporns (2009). "Complex brain networks: From topological architecture to [[brain-dynamics]]." *Nature Reviews Neuroscience* [@doi:10.1038/nrn2576]
- Rubinov & Sporns (2010). "Complex network measures of brain connectivity: Uses and interpretations." *NeuroImage* [@doi:10.1016/j.neuroimage.2010.02.045]
- van den Heuvel & Sporns (2013). "Network hubs in the human brain." *Journal of Neuroscience* [@doi:10.1523/JNEUROSCI.3689-12.2013]
- Fornito, Zalesky & Bullmore (2016). *Fundamentals of [[brain-network]] Analysis* [@doi:10.1093/brain/awx275]

## Open Questions

Network neuroscience continues to grapple with fundamental questions. The relationship between [[structural-connectivity]] and [[functional-connectivity]] remains incompletely understood—strong structural links do not always produce strong functional coupling, and functional networks can emerge even absent direct structural connections through polysynaptic pathways. The field faces challenges in [[reproducibility]] related to preprocessing choices, parcellation scheme selection, and the interpretation of tractography-derived connectivity. Future directions include integrating multi-modal data across spatial scales, extending network analysis to understand temporal dynamics and [[neurodevelopment]], and applying network-level insights to clinical translation in [[schizophrenia-models]] and [[alzheimers-modeling]] [@doi:10.1093/brain/awx275].

## References

1. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on whole-brain models*. eLife. [DOI](https://doi.org/10.7554/eLife.106194)
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](https://doi.org/10.1101/2025.01.21.633922)
3. Ramiro Plüss, Hernán Villota, Patricio Orio. (2025). *Hemispheric-Specific Coupling Improves Modeling of Functional Connectivity Using Wilson-Cowan Dynamics*. [Link](https://arxiv.org/abs/2506.22951)