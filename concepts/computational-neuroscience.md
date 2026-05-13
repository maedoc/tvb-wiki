---
created: 2026-04-27
sources:
- raw/papers/arxiv-2603.07524.md
- raw/papers/jordan-2018.md
- raw/papers/strogatz-1994.md
- raw/papers/friston-1993.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/arxiv-2601.03796.md
- raw/papers/arxiv-2603.20680.md
- raw/papers/semanticscholar-565d9037ee06.md
tags:
- computational-neuroscience
title: Computational Neuroscience
type: concept
updated: '2026-05-12'
---

Computational neuroscience is the discipline that formalizes brain function as a dynamical system constrained by anatomical structure and the [[connectome]], seeking to bridge biophysical mechanism with observable neural activity patterns. Jiang et al. (2026) emphasize that brain activity is intrinsically a neural dynamic process shaped by anatomical space, producing significant variations in spatial distribution and correlation patterns across heterogeneous scenarios. At the microscopic scale, the field simulates [[spiking-neural-networks]] with synaptic resolution; Jordan et al. (2018) demonstrated that the [[nest]] simulator can weak-scale from laptops to petascale supercomputers, executing networks comprising 10^11 synapses—approaching human cortex scale—through a five-step communication scheme and memory-efficient data structures. At the macroscopic scale, [[neural-mass-model|neural mass models]] and mean-field approximations capture population-level dynamics governed by [[nonlinear-dynamics|nonlinear differential equations]], with Strogatz (1994) supplying the foundational treatment of [[bifurcation-analysis|bifurcation theory]], limit cycles, and strange attractors that underpin the analysis of brain state transitions such as [[epilepsy-modeling|seizure onset]].

The bridge from these computational scales to neuroimaging is established by [[functional-connectivity]], which Friston et al. (1993) originally defined as the temporal correlation between spatially remote neurophysiological events and extracted via principal component analysis of [[neuroimaging-pet|PET]] and [[fmri]] data. Despite this progress, the field has historically treated scales in isolation; Hater et al. (2026) address this limitation with a [[co-simulation]] framework that couples the [[arbor]] spiking simulator with [[the-virtual-brain|TVB]] through an MPI intercommunicator, enabling real-time bidirectional translation between discrete spikes and continuous mean-field activity to model seizure generation and whole-brain propagation. Meanwhile, Jiang et al. (2026) argue that dominant functional network construction methods relying on pre-defined atlases and linear assumptions fail to capture heterogeneous neural dynamics, and propose a neural dynamics-informed pre-trained framework for [[personalized-brain-modeling|personalized brain functional network construction]]. Together, these strands illustrate computational neuroscience as an inherently multiscale endeavor spanning biophysical realism, dynamical systems theory, and clinical neuroimaging.

## Related Concepts
* [[parcellation]]
* [[neural-mass-model]]

## References

1. Hongjie Jiang, Yifei Tang, Shuqiang Wang. *Neural Dynamics-Informed Pre-trained Framework for [[personalized-brain-modeling|Personalized Brain]] Functional Network Construction*. [Link](https://arxiv.org/abs/2603.07524))
2. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2018.00002))
3. (authors unknown). *[[nonlinear-dynamics]] and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*.
4. (authors unknown). *[[functional-connectivity]]: The Principal-Component Analysis of Large (PET and [[fmri]]) Data Sets*.
5. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *[[arbor]]-TVB: a novel multi-scale [[co-simulation]] framework with a case study on neural-level seizure generation and [[whole-brain]] propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161))
6. Christopher Gabaldon, Adria Mulero, Rong Wang, Daniel A. Martin, Sabrina Camargo, Qian-Yuan Tang, Ignacio Cifre, Changsong Zhou, Dante R. Chialvo. (2026). *Data-driven inference of brain dynamical states from the r-spectrum of correlation matrices*. [Link](https://arxiv.org/abs/2601.03796))
7. Jianwei Chen, Zhengyang Miao, Wenjie Cai, Jiaxue Tang, Boxing Liu, Yunfan Zhang, Yuhang Yang, Hao Tang, Carola-Bibiane Schönlieb, Zaixu Cui, Du Lei, Shouliang Qi, Chao Li. (2026). *Hierarchical Multiscale Structure-Function Coupling for Brain [[connectome]] Integration*. [Link](https://arxiv.org/abs/2603.20680))
8. C. Goh, Hao Liu. (2025). *Mapping the Disordered Mind: A Computational Framework for Integrating [[neuroimaging]] and Symptom Data*. Digital Neuropsychiatry. [DOI](https://doi.org/10.64229/zxdytz96))