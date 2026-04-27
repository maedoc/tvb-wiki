---
created: 2026-04-20
sources:
- raw/papers/sporns-2011.md
- raw/papers/barabasi-albert-1999.md
- raw/papers/smith-2013-connectomics.md
tags:
- connectomics
- network-dynamics
- graph-theory
- structural-connectivity
- functional-connectivity
title: Brain Network
type: concept
updated: '2026-04-27'
---

A brain network represents the brain as a mathematical graph in which neural elements—neurons, cortical columns, or macroscopic brain regions—are abstracted as nodes and the connections between them are abstracted as edges. This representation transforms the complex three-dimensional structure of the brain into a format amenable to the tools of graph theory, enabling quantitative characterization of network topology and dynamics. The nodes are typically derived from neuroimaging parcellation schemes such as the [[desikan-killiany-atlas]] or the [[julich-atlas]], while edges are derived from measurements of structural connectivity via diffusion MRI [[tractography]] or from functional connectivity computed from resting-state [[fmri]], [[eeg]], or [[meg]] data. The resulting graph can be weighted (where edge weights reflect connection strength) or binary (where edges simply indicate presence or absence), directed or undirected, depending on the modality and scientific question at hand.

The motivation for representing the brain as a network emerges from the recognition that cognitive and neurological functions arise from the coordinated activity of distributed brain regions, not from isolated processing in localized areas alone. By mapping the brain as a network, researchers can move beyond describing individual brain regions as isolated units and instead examine the relational structure that enables integration and segregation of information—two fundamental operations that the brain must perform simultaneously. This approach has proven particularly powerful for understanding brain disorders, as many neurological and psychiatric conditions manifest as characteristic alterations in network topology rather than focal lesions. The network perspective also provides a natural framework for linking empirical observations to computational models of [[brain-dynamics]], as the structural [[connectome]] can serve as the anatomical scaffold upon which whole-brain simulations are built.

## Network Analysis Metrics

The mathematical characterization of brain networks relies on a rich set of metrics borrowed from [[graph-theory]]. These metrics quantify topological properties at both the nodal level and the global network level. At the nodal level, common metrics include degree (the number of connections to a node), betweenness centrality (the proportion of shortest paths passing through a node), and clustering coefficient (the tendency of a node's neighbors to connect to each other). Nodes with exceptionally high degree or centrality are termed [[network-hubs]] and often correspond to association cortex regions that integrate information across multiple functional networks. At the global level, metrics such as path length (the average shortest distance between all node pairs), modularity (the degree to which the network divides into tightly coupled communities), and small-worldness (a combination of high clustering and short path length) characterize overall network organization. The [[brain-connectivity-toolbox]] provides standardized implementations of these metrics for the neuroscience community.

## Network Organization Principles

Beyond characterizing empirical brain networks, researchers have developed network models to understand the principles governing brain organization. The scale-free network model, introduced by Barabási and Albert in 1999, demonstrates how networks exhibiting power-law degree distributions emerge through [[preferential-attachment]]—a growth mechanism whereby nodes with more connections attract even more connections over time. This mechanism provides a theoretical account for the presence of highly connected hub regions observed in empirical Brain networks. Complementary to the scale-free model, the [[small-world-networks]] framework captures networks characterized by high clustering among neighboring nodes combined with short path lengths between distant nodes, thereby enabling efficient integration of information across the entire network. Empirical studies have demonstrated that human brain networks exhibit both scale-free and small-world properties, suggesting that the brain's network architecture balances the competing demands of local processing and global integration.

The [[modularity]] of brain networks refers to their organization into distinct functional communities—groups of nodes that are densely interconnected with each other but sparser connections to nodes in other modules. This modular architecture supports functional specialization while permitting inter-module communication through hub nodes and [[rich-club]] phenomena, wherein highly connected hub regions themselves form a densely interconnected subnetwork.

## Relationship to Whole-Brain Modeling

In [[whole-brain]] modeling, the structural network serves as the anatomical substrate for simulating large-scale neural dynamics. Computational frameworks such as [[tvb]] integrate structural connectivity matrices derived from diffusion imaging with [[neural-mass-model]]s to generate realistic brain activity patterns. The coupling between nodes is determined by the structural edges, which can be scaled by parameters representing conduction delays and connection strengths. This approach allows researchers to investigate how structural alterations—such as those observed in [[alzheimers-modeling]] or [[schizophrenia-models]]—impact functional dynamics measured through [[resting-state]] activity. The network representation thus provides the essential bridge between anatomical connectivity and emergent functional connectivity, making it a foundational concept for computational neuroscience and connectomics research.

## References

1. (authors unknown). *Networks of the Brain*.
2. (authors unknown). *Emergence of Scaling in [[random-networks]]*.
3. (authors unknown). *Functional [[connectomics]] from Resting-State fMRI*.