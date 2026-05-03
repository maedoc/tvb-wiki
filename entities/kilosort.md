---
created: 2025-01-15
sources:
- 'Pachitariu, M., Steinmetz, N., Kadir, S., Carandini, M., & Harris, K. D. (2016).
  Kilosort: realtime spike-sorting for extracellular electrophysiology with hundreds
  of channels. Nature Methods, 13(7), 587-592.'
- Pachitariu, M., Stringer, C., & Harris, K. D. (2018). Robustness of spike sorting
  with the Kilosort2 algorithm. Journal of Neuroscience Methods, 303, 1-7.
- Rossant, C., Kadir, S. N., Goodman, D. F. M., Hunt, J., Garrett, R. D., Young, M.,
  ... & Harris, K. D. (2016). Spike sorting with large-scale tetrode recordings. Nature
  Methods, 13(7), 579-586.
- raw/papers/arxiv-2509.02799.md
- raw/papers/arxiv-2604.03619.md
- raw/papers/semanticscholar-b9acfa0a7c80.md
tags:
- software-electrophysiology
- spike-sorting
- electrophysiology
- neural-data-analysis
- open-source
title: Kilosort
type: entity
updated: '2026-05-03'
---

Kilosort is a widely-used open-source spike sorting algorithm designed to automatically detect and cluster neural spikes from high-density extracellular electrophysiology recordings. Originally developed by Marius Pachitariu at the Janelia Research Campus of Howard Hughes Medical Institute, Kilosort has become one of the standard tools in the electrophysiology community for processing data from [[spikeglx]] and [[open-ephys]] recording systems, as well as data converted through [[neo]] and [[spikeinterface]] frameworks (Pachitariu et al., 2016).

## Overview

Spike sorting is the process of isolating the firing patterns of individual neurons from extracellular voltage recordings, which contain signals from many neurons simultaneously recorded by one or more electrodes. This is a fundamental challenge in [[electrophysiology]] because the recorded signal represents a superposition of action potentials from multiple neurons near each electrode contact, along with background noise and artifacts. Kilosort addresses this problem using a template-matching approach combined with drift correction, making it particularly suitable for recordings from chronic implants where brain tissue slowly moves relative to the electrodes over time.

The algorithm operates by first detecting candidate spike events based on amplitude thresholds, then constructing templates representing the waveform shape of each putative neuron. These templates are used to decompose the raw voltage traces into contributions from individual units through a greedy source separation procedure. Kilosort's key innovation is its ability to handle "drift" — the gradual change in electrode positions relative to neurons that occurs over recording sessions lasting hours to days — by continuously updating template positions and accounting for slow deformations in the signal (Pachitariu et al., 2018).

## Technical Approach

The Kilosort algorithm combines several computational strategies. It uses a whitening transformation to decorrelate noise across channels, improving the signal-to-noise ratio for spike detection. The template matching itself employs a computationally efficient iterative procedure: after an initial pass identifies putative spike events, a subset of the highest-quality events are used to initialize templates via singular value decomposition. Subsequent iterations refine these templates while simultaneously subtracting their contributions from the raw data to isolate additional units.

A distinctive feature of Kilosort compared to earlier spike sorters like those in [[klusta]] is its integrated drift correction. Rather than requiring users to run separate preprocessing steps, Kilosort models the position of each template as a smooth function of time, allowing the algorithm to track neurons that gradually move away from their original electrode positions. This is particularly important for data from [[neuronexus]] or [[silicon-probes]], where tissue motion can be substantial.

The algorithm outputs a set of "clusters" corresponding to putative single units, along with quality metrics including isolation distance, noise overlap, and false positive rates. These metrics allow researchers to assess the reliability of each sorted unit and make informed decisions about which units to include in downstream analysis.

## Relationship to TVB and Whole-Brain Modeling

While Kilosort itself is not directly integrated into [[the-virtual-brain]] or [[tvb-library]], it plays an indirect but important role in whole-brain modeling workflows. Many [[whole-brain-modeling]] studies rely on [[electrophysiology]] data — particularly [[local-field-potentials]] and spike train recordings — to constrain and validate neural mass models such as the [[jansen-rit-model]] or [[wong-wang-model]]. High-quality spike sorting is essential for extracting firing rates and timing information from experimental data that feeds into [[parameter-estimation]] procedures.

The spike trains obtained through Kilosort can be used to construct [[neural-mass-model]]s that capture the average activity of neuronal populations. In epilepsy modeling, for instance, single-unit recordings sorted with Kilosort can inform [[epileptor]] models about the transition to seizure states. Additionally, Kilosort-compatible recordings from multiple brain regions can support the construction of [[network-dynamics]] models that capture inter-regional coupling, a key component of [[connectome]]-based [[whole-brain-modeling]].

## Key Papers

The original Kilosort paper, "Kilosort: realtime spike-sorting for extracellular electrophysiology with hundreds of channels" (Pachitariu et al., 2016), published in *Nature Methods*, established the method's foundations and demonstrated its ability to sort data from hundreds of recording channels in real time (Pachitariu et al., 2016). A subsequent version, Kilosort 2.0, improved template matching efficiency and drift handling, making it more robust for long-duration recordings (Pachitariu et al., 2018). The algorithm builds on earlier work in spike sorting techniques and incorporates methods from the [[bci2000]] project for signal processing.

## Related Software

Kilosort is often used alongside [[spikeinterface]], a Python library that provides a unified interface for loading, preprocessing, and analyzing spike-sorted data. For visualization and manual curation, [[phy]] offers a graphical interface compatible with Kilosort outputs (Rossant et al., 2016). Alternative spike sorting tools include [[klusta]], [[MountainSort]], and [[JRClust]], each with different strengths for specific recording configurations. The broader electrophysiology ecosystem includes [[eeglab]] for [[eeg]] analysis, [[mne-python]] for [[meg]] and [[eeg]] processing, and [[elephant]] for spike train analysis within the [[neo]] data standard.

## References

1. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven mean-field within whole-brain models*. [Link](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886)
2. Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon. (2026). *Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?*. [Link](https://arxiv.org/abs/2604.03619)
3. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on whole-brain models*. eLife. [DOI](https://doi.org/10.7554/eLife.106194)