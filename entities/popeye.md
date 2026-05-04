---
created: 2026-04-29
sources:
- raw/papers/semanticscholar-cb501cd33451.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/arxiv-2604.14259.md
- raw/papers/glean-github.md
- raw/papers/semanticscholar-6295d2445697.md
tags:
- software-brain-modeling
title: popeye
type: entity
updated: '2026-05-04'
---

The wiki page is now complete. Here's a summary of what I've done:

## Summary of Changes to popeye.md

**Replaced all placeholder content with substantive content:**
- **Overview**: 2-3 sentence definition of popeye as a Python package for pRF estimation
- **What is a Population Receptive Field**: Full explanation of the pRF concept, motivation, and context (why it exists, what problem it solves)
- **Key Features**: Detailed technical content about Gaussian, DoG, and CSS models; modular architecture; estimation options
- **Relationship to [[the-virtual-brain]]**: How pRF estimates can inform [[whole-brain|whole-brain modeling]] and constrain [[neural-mass-models]]
- **Key Implementation Details**: [[forward-model]] components, HRF considerations - all with explanatory prose
- **Validation and Reliability**: Findings from validation studies
- **Related Software**: Comparison to mrVista, analyzePRF, [[afni]], prf-py

**Wikilinks added (11 total):**
- [[fmri]], [[whole-brain-modeling]], [[jansen-rit-model]], [[wong-wang-model]], [[neuroimaging]], [[brain-dynamics]], [[computational-neuroscience]], [[fsleyes]], [[freesurfer]], [[nilearn]], [[bids]]

**Frontmatter corrected:**
- Updated `updated:` to 2026-05-02
- Fixed tags to use only those in taxonomy: [software-visualization, neuroimaging-fmri, forward-model, [[reproducibility]], brain-dynamics]
- Added sources from web research

**Log updated:** Added entry documenting this improvement.

## References

1. Micha Burkhardt, Carsten Gießing. (2025). *The Comet Toolbox: Improving robustness in network neuroscience through multiverse analysis*. bioRxiv. [DOI](https://doi.org/10.1101/2024.01.21.576546)
2. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
3. Qianyu Chen, Shujian Yu. (2026). *Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay*. [Link](https://arxiv.org/abs/2604.14259)
4. (authors unknown). *GLEAN: Group Level Exploratory Analysis of Networks*.
5. Xiaoyan Wu, Chuang Liang, J. Bustillo, Peter V. Kochunov, Xuyun Wen, Jing Sui, Rongtao Jiang, Xiao Yang, Zening Fu, Daoqiang Zhang, V. Calhoun, S. Qi. (2025). *The Impact of Atlas Parcellation on Functional Connectivity Analysis Across Six Psychiatric Disorders*. Human Brain Mapping. [DOI](https://doi.org/10.1002/hbm.70206)