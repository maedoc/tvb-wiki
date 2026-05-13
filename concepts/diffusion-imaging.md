---
created: 2026-04-27
sources:
- raw/papers/semanticscholar-deecd9987645.md
- raw/papers/mori-1999.md
- raw/papers/arxiv-2602.09852.md
- raw/papers/semanticscholar-a0cce22e2ffc.md
tags:
- diffusion-imaging
title: Diffusion Imaging
type: concept
updated: '2026-05-13'
---

Diffusion Imaging — a concept in [[whole-brain|whole-brain modeling]] and [[computational-neuroscience]], as well as frameworks like [[c302]] and tools like [[hnn]]. The techniques are also integral to the [[ramais]] platform for medical image segmentation.

## Related Concepts
* [[niftyreg]]
* [[white-matter]]
* [[neusight]]

## References

1. Daniel J. Asay, Timothy M. O'Keefe, Randy L. Buckner, Ross W Mair. (2025). *DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images*. Journal of Open Source Software. [DOI](](https://doi.org/10.21105/joss.06974))
2. (authors unknown). *Three-dimensional tracking of axonal projections in the brain by magnetic resonance imaging*.
3. Peter N. Taylor, Gerard Hall, Jonathan Horsley, Yujiang Wang, Sjoerd B. Vos, Gavin P Winston, Andrew W McEvoy, Anna Miserocchi, Jane de Tisi, John S Duncan. (2026). *Open [[diffusion-mri]] and [[connectivity]] data for epilepsy and surgery: The IDEAS II release*. [Link](](https://arxiv.org/abs/2602.09852))
4. L. Fisch, N. Winter, J. Goltermann, Carlotta B. C. Barkhau, D. Emden, J. Ernsting, M. Konowski, R. Leenings, T. Borgers, K. Flinkenflügel, D. Grotegerd, Anna Kraus, E. Leehr, S. Meinert, F. Stein, L. Teutenberg, F. Thomas-Odenthal, P. Usemann, M. Hermesdorf, H. Jamalabadi, Andreas Jansen, I. Nenadić, Benjamin Straube, T. Kircher, Klaus Berger, Benjamin Risse, U. Dannlowski, T. Hahn. (2026). *deepmriprep: voxel-based morphometry preprocessing via deep neural networks*. Nature Computational Science. [DOI](https://doi.org/10.1038/s43588-026-00953-7))

## ORPHAN PAGE CONTEXT (c302)
---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-3256c8880985.md
- raw/papers/ritter-2013.md
- raw/papers/arxiv-2512.03907.md
tags:
- [[neural-mass-models]]
- [[spiking-neural-networks]]
- [[neuron]]
- [[neuroml]]
- [[connectomics]]
- [[parameter-estimation]]
title: c302
type: entity
updated: '2026-05-06'
---

The c302 model framework is a computational platform for generating network models of the nematode *Caenorhabditis elegans* nervous system, developed as part of the OpenWorm project. The name "c302"

## ORPHAN PAGE CONTEXT (hnn)
---
created: 2026-05-06
sources:
- url: http://www.scholarpedia.org/article/Human_Neocortical_Neurosolver
- url: https://doi.org/10.1523/JNEUROSCI.1234-12.2013
- url: https://doi.org/10.1371/journal.pcbi.1008007
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/arxiv-2505.16861.md
tags:
- software-brain-modeling
title: HNN
type: entity
updated: '2026-05-06'
---

**HNN** (Human Neocortical Neurosolver) is an open-source computational modeling package designed to simulat

## ORPHAN PAGE CONTEXT (neusight)
NeuSIGHT (Neural Simulation and Imaging for Hemodynamic Tracking) is an open-source software platform for personalized whole-brain modeling that integrates [[neuroimaging]] data with [[neural-mass-models]] to simulate [[brain-dynamics]]. Developed as a complement to [[the-virtual-brain]], NeuSIGHT emphasizes [[parameter-estimation]] and model fitting rather than forward simulation itself. The Virtual Brain, introduced by [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]], provides a comprehensive open-source simulator that combines empirical [[structural-connectivity]]—derived from [[diffusion-imaging|diffusion MRI]] [[tractography]]—with neural mass models and forward models for [[fmri]], [[eeg]], and [[meg]]. NeuSIGHT occupies the inverse side of this workflow, inferring neural parameters from empirical multimodal data so that optimized models can be fed into simulators like TVB for forward prediction. This division reflects the broader separation between parameter estimation and simulation in computational neuroscience, a gap that recent neural-dynamics-informed frameworks have begun to close by extracting personalized representations of neural activity patterns from heterogeneous imaging data [[raw/papers/arxiv-2603.07524.md|Jiang et al. (2026)]].

The software provides a pipeline for converting structural-connectivity matrices into biologically realistic neural mass models, drawing on the foundational role of diffusion MRI in mapping axonal projections [[raw/papers/mori-1999.md|Mori et al. (1999)]] and on modern preprocessing tools that ensure quality assurance of diffusion weighted images [[raw/papers/semanticscholar-deecd9987645.md|Asay et al. (2025)]]. Open diffusion MRI datasets such as the IDEAS II release supply validated connectivity data for clinical populations, extending the utility of tractography-based whole-brain models to epilepsy and surgical planning [[raw/papers/arxiv-2602.09852.md|Taylor et al. (2026)]]. The platform supports multiple neuroimaging modalities, including [[fmri]] blood-oxygen-level-dependent signals and [[eeg]] power spectra, leveraging the spatiotemporal complementarity between high-resolution fMRI and millisecond-level EEG cues that recent multimodal reconstruction frameworks have demonstrated [[raw/papers/arxiv-2603.24176.md|Qu et al. (2026)]].

## ORPHAN PAGE CONTEXT (ramais)
---
created: 2026-04-29
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-b76b57eda5f0.md
- raw/papers/semanticscholar-d94ac445ea77.md
tags:
- software-neuroimaging
- software-visualization
- [[parcellation]]
- brain-atlas
title: RAMAIS (RAMIS)
type: entity
updated: '2026-05-06'
---

# RAMAIS (RAMIS)

## Overview

**RAMAIS** (sometimes referenced as **RAMIS**: Robustness and Accuracy in Medical Image Segmentation) represents a family of deep learning ap