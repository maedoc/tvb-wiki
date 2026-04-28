---
created: 2026-04-23
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/woodman-2014.md
- raw/papers/sanz-leon-2013.md
tags:
- software-brain-modeling
title: Brain Connectivity Toolbox
type: entity
updated: '2026-04-28'
---

title: Brain Connectivity Toolbox
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [software-bct, connectomics, graph-theory, network-analysis, functional-connectivity, structural-connectivity, neuroimaging-mri, matlab-toolbox]
sources: [rubinov-sporns-2010, bct-github, betzel-2019-multilayer]
---

The **Brain Connectivity Toolbox** (BCT) is a widely used MATLAB toolbox for the analysis of structural and functional brain networks derived from neuroimaging data. Developed primarily by Mikail Rubinov and Olaf Sporns at Indiana University, with later contributions from Richard Betzel and colleagues, BCT provides a comprehensive set of tools for computing graph-theoretic measures on brain connectomes, enabling researchers to characterize the topological organization of neural networks at multiple scales. The toolbox has become a standard resource in the field of [[connectomics]], with applications spanning [[resting-state]] fMRI analysis, [[diffusion-imaging]] based tractography, and [[whole-brain]] modeling validation.

## Motivation and Clinical Context

The emergence of the Brain Connectivity Toolbox addressed a critical need in [[neuroimaging]] research: the lack of standardized, well-validated software for quantifying network properties in brain data. Before BCT, researchers interested in applying [[graph-theory]] measures to brain networks had to implement algorithms from scratch, leading to inconsistencies in methodology across studies. BCT provides optimized, peer-reviewed implementations of network metrics that enable reproducible analysis of brain connectivity patterns. The toolbox has proven particularly valuable in studying [[brain-network]] alterations in neurological and psychiatric conditions, including [[alzheimers-disease]], [[schizophrenia-models]], and [[epilepsy-modeling]], where disrupted network topology serves as a marker of pathology.

## Key Features and Capabilities

BCT includes implementations of over 100 network analysis algorithms spanning several categories. **Global network metrics** include [[small-world]] measures (clustering coefficient, characteristic path length), network efficiency (global and local), [[modularity]], [[rich-club]] coefficient, and [[structural-core]] identification. **Node-level metrics** include degree, betweenness centrality, [[network-hubs]] identification, and eigenvector centrality. The toolbox also provides tools for **network comparison**, including null model generation (configurable and lattice-watts-strogatz models), network distance measures, and statistical testing via permutation frameworks.

A distinctive feature of BCT is its support for **weighted and directed networks**, allowing analysis beyond simple binary graphs. The toolbox implements algorithms for thresholding strategies (absolute, proportional, and density-capped), as relationship strength between brain regions can vary continuously. BCT also includes specialized functions for **community detection**, implementing algorithms from multiple research groups including Louvain, Infomap, and spectral partitioning methods. For time-varying connectivity analysis, BCT provides tools for analyzing dynamic connectivity patterns extracted from sliding-window analyses of fMRI or MEG data.

## Relationship to TVB and Whole-Brain Modeling

The Brain Connectivity Toolbox plays an important role in the [[whole-brain-modeling]] ecosystem, particularly in the **parameterization and validation** of [[the-virtual-brain]] simulations. When building personalized brain models using [[the-virtual-brain]] or [[tvb-library]], researchers often use BCT to compare simulated functional connectivity patterns against empirical fMRI or MEG data. The toolbox's implementation of graph-theoretic metrics provides objective measures for assessing how well a [[neural-mass-model]] or [[epileptor]] network reproduces the topological features of observed brain networks. Additionally, BCT analysis of empirical structural connectivity (derived from [[diffusion-mri]] tractography) informs the [[structural-connectivity]] matrices that serve as the anatomical scaffold for [[whole-brain]] simulations in TVB. The combination of BCT analysis with [[whole-brain]] simulators represents a powerful approach for studying the relationship between anatomical structure and emergent functional dynamics in the brain.

## Related Software and Ecosystem

While BCT was originally developed for MATLAB, several adaptations and alternatives have emerged in the Python ecosystem. **bctpy** provides Python bindings to the core BCT algorithms, enabling integration with scientific computing stacks using [[numpy]] and [[scipy]]. The [[brainnet-viewer]] software complements BCT by providing visualization capabilities for three-dimensional brain networks. For Python-native analysis, the [[brainspace]] library offers network analysis functionality, while [[nilearn]] provides connectivity-related tools within the Python neuroimaging preprocessing ecosystem. The [[graphvar]] toolbox extends BCT-style network analysis specifically for graph-theoretic approaches to neuroimaging, with additional features for brain-behavior correlation analysis and null model validation for dynamic connectivity metrics.

## Key Papers and Development History

The Brain Connectivity Toolbox was first released in 2009 alongside a seminal review paper by Rubinov and Sporns that established standardized terminology for complex network analysis in neuroscience. The foundational reference for BCT remains the comprehensive NeuroImage paper by Mikail Rubinov and Olaf Sporns, which describes the toolkit's capabilities, algorithms, and theoretical foundations in detail. The toolbox has undergone continuous development, with major updates adding new algorithms for network comparison, null model generation, and modular decomposition. The 2019 update (BCT 2019) added enhanced support for multilayer network analysis and improved computational efficiency for large-scale networks. Researchers using BCT should cite the original Rubinov and Sporns (2010) NeuroImage paper as the primary reference.

## See Also

- [[connectomics]] — the broader field of mapping brain connectivity
- [[graph-theory]] — mathematical framework underlying BCT's network analysis
- [[structural-connectivity]] — anatomical brain networks analyzed using BCT
- [[functional-connectivity]] — statistical dependencies between brain regions
- [[community-detection]] — identifying modular structure in brain networks
- [[network-dynamics]] — how brain network topology relates to neural dynamics
- [[small-world-networks]] — a key topological property of brain networks
- [[rich-club]] — densely connected hub regions in the brain