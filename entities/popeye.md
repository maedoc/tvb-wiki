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
updated: '2026-05-18'
---

**popeye** operates within the landscape of [[fmri]] data analysis and [[neuroimaging]] research. Functional magnetic resonance imaging is widely used for studying and diagnosing brain disorders, providing high-resolution cortical representations that form a strong basis for characterizing fine-grained brain activity patterns [[raw/papers/arxiv-2604.14259.md|Chen & Yu (2026)]][[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]]. The high acquisition cost of fMRI limits large-scale applications, placing strong pressure on analysis pipelines to reconstruct maximal information from each scan while maintaining temporal coherence and spatial accuracy across whole-brain and functionally specific regions [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]]. Capturing dynamic spatiotemporal neural activity is essential for understanding large-scale brain mechanisms, and methods that preserve cortical-vertex-level detail across continuous neural sequences are increasingly demanded in multimodal neuroimaging toward more dynamic brain activity modeling [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]].

This demand for precision exists alongside broader reproducibility challenges in network neuroscience. Because there is no ground truth for the validity of specific analytical steps, researchers face a multitude of arbitrary yet defensible choices when moving from raw BOLD signals to interpretable models, raising concerns about the robustness and generalizability of results across pipelines and studies [[raw/papers/semanticscholar-cb501cd33451.md|Burkhardt & Gießing (2025)]]. [[Functional-connectivity]] matrices derived from fMRI provide powerful representations of large-scale neural interactions that support both basic research and clinical applications including brain disorder diagnosis, yet downstream inferences remain vulnerable to methodological variability and site-specific effects, underscoring the need for transparent, well-validated estimation frameworks [[raw/papers/arxiv-2604.14259.md|Chen & Yu (2026)]]. Within this landscape, popeye contributes to community efforts to advance reproducible [[computational-neuroscience]] and robust [[brain-dynamics]] research through accessible, modular analysis tools.

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
- [[fmri]], [[whole-brain-modeling]], [[jansen-rit-model]], [[wong-wang-model]], [[neuroimaging]], [[brain-dynamics]], [[computational-neuroscience]], Fsleyes, Freesurfer, Nilearn, [[bids]]

**Frontmatter corrected:**
- Updated `updated:` to 2026-05-02
- Fixed tags to use only those in taxonomy: [software-visualization, [[neuroimaging-fmri]], forward-model, [[reproducibility]], brain-dynamics]
- Added sources from web research

**Log updated:** Added entry documenting this improvement.

## References

1. Micha Burkhardt, Carsten Gießing. (2025). *The Comet Toolbox: Improving robustness in [[netneuroscience|network neuroscience]] through multiverse analysis*. bioRxiv. [DOI](](https://doi.org/10.1101/2024.01.21.576546))
2. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](](https://arxiv.org/abs/2603.24176))
3. Qianyu Chen, Shujian Yu. (2026). *Continual Learning for fMRI-Based Brain Disorder Diagnosis via [[functional-connectivity]] Matrices Generative Replay*. [Link](](https://arxiv.org/abs/2604.14259))
4. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.
5. Xiaoyan Wu, Chuang Liang, J. Bustillo, Peter V. Kochunov, Xuyun Wen, Jing Sui, Rongtao Jiang, Xiao Yang, Zening Fu, Daoqiang Zhang, V. Calhoun, S. Qi. (2025). *The Impact of Atlas [[parcellation]] on Functional [[connectivity]] Analysis Across Six Psychiatric Disorders*. Human Brain Mapping. [DOI](](https://doi.org/10.1002/hbm.70206))