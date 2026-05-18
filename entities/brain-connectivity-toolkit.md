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
updated: '2026-05-18'
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
The Brain Connectivity Toolbox (BCT) was introduced alongside the landmark review by Rubinov and Sporns (2010) as a comprehensive MATLAB toolbox for graph-theoretic analysis of brain networks Rubinov & Sporns (2010). It provides implementations of dozens of network metrics including degree, strength, centrality, clustering coefficient, path length, efficiency, modularity, and rich-club organization — all essential tools for characterizing the topological properties of structural and functional brain connectivity matrices derived from [[neuroimaging-fmri|fMRI]], [[neuromorpho-toolkit|DTI]], or electrophysiological data. BCT has become one of the most widely cited software packages in [[computational-neuroscience]], with the original paper receiving thousands of citations across the [[connectomics]] literatureRubinov & Sporns (2010).

For users preferring Python, the [[bctpy]] package provides a native Python port of the core BCT functionality, enabling integration with the broader Python neuroimaging ecosystem including [[nilearn]] and [[network-dynamics]]. BCT data formats have also been adopted as de facto standards in the field, with tools like [[graphvar]] and [[braph]] offering compatible interfaces for users who prefer graphical workflows Woodman et al. (2014). GraphVar extends BCT's functionality by adding a MATLAB GUI and statistical group comparison tools, making network analysis accessible to researchers without programming expertise. Similarly, BRAPH provides a MATLAB pipeline specifically designed for multimodal brain connectivity analysis supporting [[neuroimaging-fmri|fMRI]], [[neuroimaging-eeg|EEG]], and PET data [[braph|Mijalkov et al. (2017)]].

The BCT software is publicly available from the CONNECTOME lab website at [https://sites.google.com/site/bctnet/](](https://sites.google.com/site/bctnet/)) Rubinov & Sporns (2010) and has been continuously maintained, with periodic updates improving compatibility with newer MATLAB versions and expanding the metric repertoire Woodman et al. (2014). The toolkit's design emphasizes [[reproducibility]] by providing well-documented, consistent implementations of network measures that have been validated across numerous applications in both clinical and cognitive neuroscience research [[braph|Mijalkov et al. (2017)]].

## Related
BCT sits at the center of a growing ecosystem of [[connectomics]] tools. The toolbox was introduced alongside the landmark review by [[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]], which established graph-theoretic metrics as standard instruments for analyzing both [[structural-connectivity]] matrices and [[network-dynamics]] patterns in brain connectivity data. Because BCT is implemented in MATLAB, several projects have extended its functionality for broader audiences. [[graphvar|GraphVar]] supplements the core metric library with a graphical user interface and permutation-based statistical testing for group comparisons, making network analysis accessible to researchers without scripting experience [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]]. Similarly, [[braph|BRAPH]] provides a dedicated MATLAB pipeline for multimodal connectivity analysis that integrates BCT-style metrics with support for [[neuroimaging-fmri|fMRI]], [[neuroimaging-eeg|EEG]], and PET data [[raw/papers/mijalkov-2017-braph.md|Mijalkov et al. (2017)]].

The interoperability of these implementations reflects the degree to which BCT's metric definitions have become de facto standards in [[computational-neuroscience]] [[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]]. Whether one uses the original MATLAB toolbox or a GUI wrapper such as GraphVar, the underlying graph measures remain comparable, supporting cross-study [[reproducibility]] [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]]. BRAPH further demonstrates this standardization by adopting the same BCT-style metrics for multimodal brain connectivity analysis across diverse neuroimaging datasets [[raw/papers/mijalkov-2017-braph.md|Mijalkov et al. (2017)]]. This consistency is particularly valuable when validating simulated networks produced by platforms such as [[the-virtual-brain]], where BCT metrics quantify the topological realism of model-generated [[brain-network|brain networks]].

## References

1. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
2. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
3. (authors unknown). *BRAPH: A Pipeline for Brain Connectivity Analysis*.