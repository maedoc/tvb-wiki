# NETSCOPE: Information-Theory Based Network Discovery and Analysis

**Source**: semantic-scholar
**ID**: d3293216a636b37252744d919c66dd750683ad59
**DOI**: 10.1101/2022.04.18.488630
**URL**: https://www.semanticscholar.org/paper/d3293216a636b37252744d919c66dd750683ad59
**Date**: 2026-03-27
**Year**: 2026
**Authors**: Tido Bergmans, Tousif Jamal, Aya Rezeika, Chih-Chia Hsing, T. Celikel
**Venue**: bioRxiv
**Citations**: 0

## Abstract

Biological systems are naturally described as networks, spanning molecular interactions, cellular circuits, and brain-wide functional connectivity. Despite the ubiquity of network data, workflows for inferring network structure and then applying comparable graph analyses across modalities remain fragmented. We present NETSCOPE, an open-source, multi-platform toolbox for information-theoretic network inference and analysis. NETSCOPE estimates pairwise statistical dependence with mutual information (MI), derives weighted adjacency matrices, removes likely spurious edges using shuffle-based thresholds, and prunes indirect connections using the data processing inequality (DPI). A key feature is the conversion of MI-based similarity into a metric space via (normalized) variation of information (VI), enabling weighted shortest-path and centrality analyses that require distance-like edge weights. We validate the toolbox on synthetic data with known ground-truth topology and by reconstructing published molecular networks in Saccharomyces cerevisiae. We further demonstrate cross-domain use cases in single-cell transcriptomic networks, cell-level anatomical maps, EEG connectivity, and resting-state fMRI. NETSCOPE runs in Python and MATLAB/Octave, and is compatible with Jupyter/Colab workflows.
