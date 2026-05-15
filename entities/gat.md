---
created: 2026-05-13
sources:
- raw/papers/hosseini-2012-gat.md
tags:
- software-brain-modeling
- graph-theory
- connectomics
- structural-connectivity
- functional-connectivity
- network-dynamics
- resting-state
title: GAT (Graph Analysis Toolbox)
type: entity
updated: '2026-05-15'
---

# GAT (Graph Analysis Toolbox)

The **Graph Analysis Toolbox** (GAT) is a MATLAB-based software package that provides a graphical user interface for performing graph-theoretical analyses on structural and functional [[brain-network]] data. Built as a GUI wrapper around the core algorithms of the [[brain-connectivity-toolbox]], GAT was designed to make [[graph-theory]]-based network analysis accessible to researchers and clinicians who lack programming expertise, while still offering the statistical rigor required for between-group comparisons in clinical neuroscience.

## Motivation and Context

The rapid growth of [[connectomics]] created a methodological bottleneck: the [[brain-connectivity-toolbox]] provided a rich set of graph-theoretic algorithms, but using them required writing custom MATLAB scripts — a barrier for many clinically oriented researchers studying neurological and psychiatric populations. GAT addressed this gap by wrapping the BCT's core metrics in an interactive point-and-click interface that guides users through the full analysis pipeline: network construction from connectivity matrices, thresholding, computation of global and nodal [[graph-theory]] metrics, statistical comparison between groups, and visualization of results. This workflow standardization also improved reproducibility across studies by reducing ad-hoc scripting decisions.

The toolbox has been applied across a range of clinical and cognitive studies, including investigations of [[alzheimers-modeling]], traumatic brain injury, [[neurodevelopment]], and [[resting-state]] alterations in psychiatric disorders. By lowering the technical barrier to entry, GAT broadened the community of researchers capable of performing systematic [[network-dynamics]] analyses on brain [[connectivity]] data derived from [[fmri]], [[dti]], and [[diffusion-imaging]] based tractography.

## Key Features

- **Full GUI workflow**: All operations — from loading connectivity matrices to exporting publication-ready figures — are performed through dialogue windows, eliminating the need for custom code.
- **Comprehensive network metrics**: Global measures include [[small-world-networks]] indices (clustering coefficient, characteristic path length), global and local efficiency, assortativity, and [[modularity]]. Nodal measures include degree, betweenness centrality, clustering coefficient, and participation coefficient.
- **Flexible thresholding**: Supports absolute, proportional, and density-based thresholding strategies, with options for generating both binary and weighted [[graph-theory]] representations.
- **Between-group statistics**: Implements non-parametric permutation tests with correction for multiple comparisons across network densities, enabling robust comparison of network topology between patient and control groups.
- **Network visualization**: Produces spring-embedded layouts of thresholded graphs, circular [[connectome]] ring plots, and regionally mapped nodal metric visualizations.

## Technical Architecture

GAT is structured as a multi-tab MATLAB GUI that sequences the analysis pipeline. Users first load one or more connectivity matrices — either structural (from [[diffusion-imaging]] tractography) or functional (from [[resting-state]] [[fmri]] or [[eeg]]/[[meg]] coherence analysis). The toolbox applies a user-selected thresholding procedure to convert continuous connectivity values into a sparse graph, computes a battery of global and nodal metrics across a range of network densities, and then performs between-group comparisons using permutation-based significance testing. Results are displayed within the GUI and can be exported as figures or as spreadsheet-compatible tables.

## Relationship to TVB

GAT occupies a preprocessing and validation role within the [[whole-brain-modeling]] ecosystem centered on [[the-virtual-brain]]. The structural connectivity matrices analyzed by GAT — typically derived from [[dti]] tractography — are the same type of data that serves as the anatomical scaffold for [[tvb-library]] simulations. Researchers can use GAT to characterize the topological properties of an empirical [[structural-connectivity]] network (e.g., its [[small-world-networks]] organization, hub distribution, and [[modularity]]) before using that matrix as input to a [[neural-mass-model]] simulation in TVB. Conversely, GAT can be applied to compare the [[graph-theory]] properties of simulated functional connectivity (output by TVB) against empirical [[functional-connectivity]] patterns, providing a quantitative framework for model validation. This bidirectional relationship makes GAT a practical companion tool for TVB workflows, particularly in studies where network-level phenotypes are used to distinguish clinical populations or track disease progression.

## Comparison with Related Tools

| Feature | GAT | [[GraphVar]] | [[brain-connectivity-toolbox]] |
|---|---|---|---|
| Interface | MATLAB GUI | MATLAB GUI | MATLAB command-line API |
| Statistical comparisons | Permutation-based, across densities | GLM-based, with covariates | Manual (user-implemented) |
| Learning curve | Low | Low | Moderate–high |
| Extensibility | Limited | Moderate (modular) | High (direct function access) |
| Primary use case | Group-difference studies | Brain-behavior correlations | Custom analysis pipelines |

GAT prioritizes simplicity and guided workflows for group-comparison designs, while [[graphvar]] extends the GUI paradigm to brain-behavior correlation analyses with more flexible statistical modeling. The [[brain-connectivity-toolbox]] remains the foundation for both GUI tools, offering the greatest algorithmic depth for users comfortable with programmatic control.

## See Also

- [[brain-connectivity-toolbox]] — the core algorithmic library that GAT wraps
- [[graphvar]] — a more recent GUI toolbox extending GAT's approach to brain-behavior correlations
- [[graph-theory]] — mathematical framework for analyzing brain networks
- [[structural-connectivity]] — anatomical networks analyzed by GAT's graph metrics
- [[functional-connectivity]] — statistical dependencies between brain regions quantified by GAT
- [[small-world-networks]] — a key topological property measured by GAT's global metrics
- [[modularity]] — community structure metric computed by GAT
- [[network-dynamics]] — how brain network topology relates to neural dynamics
- [[connectomics]] — the broader field within which GAT operates
- [[the-virtual-brain]] — [[whole-brain]] simulation platform that uses GAT-analyzable connectivity data

## References

1. (authors unknown). *GAT: A Graph-Theoretical Analysis Toolbox for Analyzing Between-Group Differences in Large-Scale Structural and Functional Brain Networks*.