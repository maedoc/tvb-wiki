---
created: 2026-04-20
sources:
- raw/papers/niedermeyer-silva-2004.md
- raw/papers/nunez-srinivasan-2006.md
- raw/papers/makeig-1996.md
- raw/papers/cohen-2014.md
- raw/papers/arxiv-2511.09243.md
- raw/papers/arxiv-2512.07842.md
- raw/papers/semanticscholar-cc2129666e15.md
- raw/papers/arxiv-2411.16449.md
- raw/papers/arxiv-2603.29903.md
- raw/papers/arxiv-2604.01889.md
- raw/papers/zuo-2010.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/arxiv-2509.21770.md
tags:
- neuroimaging-eeg
- brain-oscillations
title: EEG
type: concept
updated: '2026-04-27'
---

# EEG

Electroencephalography (EEG) is a non-invasive method for recording electrical activity of the brain via electrodes placed on the scalp. It provides millisecond-resolution measurements of neural dynamics.

## Definition

EEG measures summed electrical activity from populations of neurons, primarily reflecting synchronous postsynaptic potentials in pyramidal cells oriented perpendicular to the cortical surface. The signal is attenuated and blurred by volume conduction through the brain, CSF, skull, and scalp.

## Characteristics

| Feature | Typical Value |
|---------|---------------|
| Temporal resolution | 1-10 ms |
| Spatial resolution | ~1-10 cm (scalp) |
| Frequency range | 0.1-100 Hz |
| Amplitude | 10-100 μV |

## Frequency Bands

- **Delta (0.5-4 Hz)**: Deep sleep, unconsciousness
- **Theta (4-8 Hz)**: Drowsiness, memory, meditation
- **Alpha (8-13 Hz)**: Relaxed wakefulness, visual cortex
- **Beta (13-30 Hz)**: Active thinking, motor planning
- **Gamma (30-100 Hz)**: Conscious perception, binding

## Role in Whole-Brain Modeling

EEG is a primary output measure for [[neural-mass-model]] validation:

1. **Forward problem**: Model-generated LFPs are transformed to scalp potentials via volume-conduction equations
2. **Frequency content**: Models must reproduce empirical power spectra and oscillatory patterns
3. **Connectivity**: Phase relationships and coherence between regions provide validation targets

[[neural-mass-model]]s like [[jansen-rit]] and [[wilson-cowan]] explicitly generate EEG-like signals from population firing rates.

## Analysis Methods

- **Time-frequency analysis**: Wavelets, Hilbert transform (cohen-2014)
- **[[source-localization]]**: Estimating intracranial sources from scalp data
- **[[ica|Independent Component Analysis]] (ICA)**: Separating mixed signals (makeig-1996)
- **Connectivity analysis**: Phase locking, coherence, Granger causality

## Comparison with Other Modalities

| Modality | Temporal | Spatial | Signal Source |
|------------|----------|---------|---------------|
| EEG | ~1 ms | ~1 cm | Electrical potentials |
| MEG | ~1 ms | ~0.5 cm | Magnetic fields |
| fMRI | ~1 s | ~3 mm | Hemodynamic response |

## Related Concepts
- [[meg]] – Magnetic counterpart with better spatial resolution
- [[fmri]] – Complementary hemodynamic measure
- [[neural-mass-model]] – Generate EEG-like outputs
- volume-conduction – Physics of signal spread
- source-localization – Estimating brain sources
- brain-oscillations – Rhythmic neural activity

## References

1. (authors unknown). *Electroencephalography: Basic Principles, Clinical Applications, and Related Fields*.
2. (authors unknown). *Electric Fields of the Brain: The Neurophysics of EEG*.
3. (authors unknown). *Independent component analysis of electroencephalographic data*.
4. (authors unknown). *Analyzing Neural Time Series Data: Theory and Practice*.
5. Helena Bordini de Lucas, Leonardo Dalla Porta, [[alain-destexhe]], Maria V. Sanchez-Vives, Osvaldo A. Rosso, Cláudio R. Mirasso, Fernanda Selingardi Matias. (2025). *Characterizing sleep stages through the complexity-entropy plane in human intracranial data and in a [[whole-brain-modeling|[[whole-brain]] model]]*. [Link](https://arxiv.org/abs/2511.09243)
6. Daniele Avitabile, Gabriel J. Lord, Khadija Meddouni. *State and Parameter Estimation for a Neural Model of Local Field Potentials*. [Link](https://arxiv.org/abs/2512.07842)
7. Gianluca Gaglioti, L. Porta, M. Colombo, Simone Russo, Thierry Nieus, G. Deco, M. Corbetta, S. Sarasso, M. V. Sanchez-Vives, M. Massimini. (2026). *Slow wave generation and propagation in a model of brain lesions*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2026.121817)
8. Huda Mahdi, Jan Sieber, [[krasimira-tsaneva-atanasova]]. *Alpha-Delta Transitions in Cortical Rhythms as grazing bifurcations*. [Link](https://arxiv.org/abs/2411.16449)
9. Breno C. Bispo, Stefania Sardellitti, Juliano B. Lima, Fernando A. N. Santos. (2026). *Multimodal Higher-Order Brain Networks: A Topological Signal Processing Perspective*. [Link](https://arxiv.org/abs/2603.29903)
10. Chenghao Yue, Zhiyuan Ma, Zhongye Xia, Xinche Zhang, Yisi Zhang, Xinke Shen, Sen Song. *LI-DSN: A Layer-wise Interactive Dual-Stream Network for EEG Decoding*. [Link](https://arxiv.org/abs/2604.01889)
11. (authors unknown). *The organization of the human cerebellum estimated by intrinsic [[functional-connectivity]]*.
12. Potjans & Diesmann (2014). *The cell-type specific cortical microcircuit: relating structure and activity*. Cerebral Cortex. [DOI](https://doi.org/10.1093/cercor/bhs358)
13. Sadman Saumik Islam, Bruna Dalcin Baldasso, Davide Cattaneo, Xianta Jiang, Michelle Ploughman. (2025). *Machine Learning and AI Applied to fNIRS Data Reveals Novel Brain Activity Biomarkers in Stable Subclinical Multiple Sclerosis*. [Link](https://arxiv.org/abs/2509.21770)