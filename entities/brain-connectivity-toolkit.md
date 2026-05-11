---
created: 2026-05-06
sources:
- raw/papers/woodman-2014.md
- raw/papers/rubinov-sporns-2010.md
- raw/papers/mijalkov-2017-braph.md
tags:
- connectivity
- graph-theory
- matlab
- network-science
title: Brain Connectivity Toolbox
type: entity
updated: '2026-05-06'
---
# Brain Connectivity Toolbox

The **Brain [[connectivity]] Toolbox (BCT)** is a comprehensive MATLAB package for graph-theoretic analysis of structural and functional brain networks. It provides hundreds of graph metrics for neuroscientific analysis.

## Overview

BCT implements graph-theoretic measures including:
- Degree, strength, and centrality measures
- Clustering coefficient and transitivity
- Path length, efficiency, and small-worldness
- [[community-detection]] and [[modularity]]
- [[rich-club]] organization
- Assortativity and motifs

## Relationship to TVB

BCT and TVB are complementary tools in the connectivity analysis pipeline:
- TVB generates simulated brain [[network-dynamics]]
- BCT analyzes the topological properties of the networks that TVB simulates
- BCT metrics (e.g., rich club coefficient, modularity) validate TVB [[structural-connectivity]] matrices
- TVB's connectivity module can export to BCT-compatible formats for cross-validation

## Software
The Brain Connectivity Toolbox (BCT) was introduced alongside the landmark review by Rubinov and Sporns (2010) as a comprehensive MATLAB toolbox for graph-theoretic analysis of brain networks [[raw/papers/rubinov-sporns-2010|Rubinov & Sporns (2010)]]. It provides implementations of dozens of network metrics including degree, strength, centrality, clustering coefficient, path length, efficiency, modularity, and rich-club organization — all essential tools for characterizing the topological properties of structural and functional brain connectivity matrices derived from [[neuroimaging-fmri|fMRI]], [[neuroimaging-dti|DTI]], or electrophysiological data. BCT has become one of the most widely cited software packages in computational neuroscience, with the original paper receiving thousands of citations across the connectomics literature[[raw/papers/rubinov-sporns-2010|Rubinov & Sporns (2010)]].

For users preferring Python, the [[bctpy]] package provides a native Python port of the core BCT functionality, enabling integration with the broader Python neuroimaging ecosystem including [[nilearn]] and [[networkx]]. BCT data formats have also been adopted as de facto standards in the field, with tools like [[graphvar]] and [[braph]] offering compatible interfaces for users who prefer graphical workflows [[raw/papers/woodman-2014|Woodman et al. (2014)]]. GraphVar extends BCT's functionality by adding a MATLAB GUI and statistical group comparison tools, making network analysis accessible to researchers without programming expertise. Similarly, BRAPH provides a MATLAB pipeline specifically designed for multimodal brain connectivity analysis supporting [[neuroimaging-fmri|fMRI]], [[neuroimaging-eeg|EEG]], and PET data [[raw/papers/mijalkov-2017-braph|Mijalkov et al. (2017)]].

The BCT software is publicly available from the CONNECTOME lab website at [https://sites.google.com/site/bctnet/](https://sites.google.com/site/bctnet/) [[raw/papers/rubinov-sporns-2010|Rubinov & Sporns (2010)]] and has been continuously maintained, with periodic updates improving compatibility with newer MATLAB versions and expanding the metric repertoire [[raw/papers/woodman-2014|Woodman et al. (2014)]]. The toolkit's design emphasizes reproducibility by providing well-documented, consistent implementations of network measures that have been validated across numerous applications in both clinical and cognitive neuroscience research [[raw/papers/mijalkov-2017-braph|Mijalkov et al. (2017)]].

## Related

- [[connectome]] — structural [[brain-network]] definitions
- [[graph-theory]] — mathematical foundations
- [[the-virtual-brain]] — simulation framework that generates networks for BCT analysis
