---
created: 2026-04-20
sources:
- raw/papers/ogawa-1990.md
- raw/papers/logothetis-2001.md
- raw/papers/friston-1994.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/power-2011.md
- raw/papers/arxiv-2509.24715.md
- raw/papers/arxiv-2602.03240.md
- raw/papers/semanticscholar-e08252ec3941.md
- raw/papers/semanticscholar-d70e1661858c.md
- raw/papers/semanticscholar-6295d2445697.md
tags:
- neuroimaging-fmri
title: fMRI
type: concept
updated: '2026-05-04'
---

# fMRI

**Functional magnetic resonance imaging (fMRI)** is a non-invasive [[neuroimaging]] technique that measures brain activity indirectly by detecting changes in blood oxygenation and cerebral blood flow associated with neural activity. Since its invention in the early 1990s, fMRI has become the dominant method for mapping human brain function, enabling researchers to visualize brain activity during cognitive tasks, sensory processing, and at rest. The technique revolutionized cognitive neuroscience by providing whole-brain coverage with reasonable spatial resolution (2-3 mm) and has become the primary empirical target for validating computational models of [[brain-dynamics]], including [[whole-brain]] models and [[neural-mass-model]] simulations.

## Physical Basis and the BOLD Signal

fMRI relies on the Blood Oxygenation Level Dependent (BOLD) contrast mechanism, discovered by Seiji Ogawa in his landmark 1990 study. The biophysical principle underlying BOLD is elegantly simple: neural activity increases local cerebral blood flow (CBF) disproportionately to oxygen consumption, resulting in an elevated ratio of oxygenated (oxyhemoglobin) to deoxygenated (deoxyhemoglobin) hemoglobin in the capillary bed. Because oxyhemoglobin is diamagnetic while deoxyhemoglobin is paramagnetic, changes in their relative concentration alter the local magnetic field homogeneity, which in turn affects the MRI signal intensity measured by echo-planar imaging sequences.

The [[bold-signal]] is fundamentally an indirect measure of neural activity, mediated by the neurovascular coupling that links neuronal signaling to hemodynamic changes. This coupling involves multiple cellular elements—neurons, astrocytes, and blood vessels—and operates on a timescale of seconds, far slower than the millisecond timescale of neural electrical activity. The [[hemodynamic-response-function]] (HRF) that describes this coupling has a characteristic peak latency of approximately 4-6 seconds following neural activation, with a temporal resolution limited by the repetition time (TR) of the imaging sequence, typically 1-3 seconds for whole-brain acquisitions.

## Analysis Methods

### Statistical Parametric Mapping

The standard framework for analyzing fMRI data was established by [[karl-j-fristol]] and colleagues in their 1994 paper introducing Statistical Parametric Mapping (SPM). This approach applies the general [[linear|linear model]] (GLM) to model the expected hemodynamic response to experimental conditions, typically represented as convolved boxcar functions for block designs or impulse responses for event-related designs. The GLM framework allows for the estimation of model parameters using ordinary least squares, followed by statistical inference on linear contrasts to identify brain regions showing significant activation. Critically, the SPM framework incorporated random field theory corrections for multiple comparisons, addressing the fundamental problem of false positives when testing thousands of voxels across the brain.

### Connectivity Analysis

Beyond task-based activation mapping, fMRI enables the characterization of [[functional-connectivity]]—the statistical dependencies between time series recorded from distinct brain regions. Task-free or "resting-state" fMRI, first demonstrated by Bharat Biswal in 1995, revealed that spatially remote brain regions exhibit coherent spontaneous fluctuations even in the absence of explicit tasks. These correlations define intrinsic connectivity networks, including the [[default-mode-network]], which have become central to understanding brain organization and have been extensively replicated across studies and populations.

## Role in Whole-Brain Modeling

fMRI serves as the primary empirical target for validating [[whole-brain]] models in computational neuroscience. The integration of [[connectome]]-based structural connectivity (typically derived from diffusion tensor imaging or tractography) with [[neural-mass-model]] formulations allows researchers to generate synthetic BOLD time series that can be directly compared with empirical fMRI data. This validation pipeline involves several critical steps: first, the neural mass model (such as the [[jansen-rit]] or [[wong-wang]] models) generates predicted neural activity at each brain region; second, a neurovascular coupling model transforms this neural activity into a simulated BOLD signal; and third, functional connectivity matrices computed from the synthetic time series are compared with empirical resting-state connectivity.

The work of Nikos Logothetis establishing that BOLD correlates most strongly with local field potentials (LFPs) rather than multi-unit spiking activity has been crucial for informing these forward models. This finding implies that [[neural-mass-model]] outputs representing synaptic activity—rather than firing rates—should be used as the basis for BOLD simulation, a principle adopted by platforms such as [[tvb]] (The Virtual Brain) for generating synthetic neuroimaging data.

## Key Limitations

Several methodological challenges affect fMRI interpretation and its use in [[model-validation]]. Head motion artifacts can create spurious correlations in functional [[connectivity]] analyses, particularly in clinical populations. The spatial resolution of fMRI is fundamentally constrained by the vascular architecture, with the point-spread function typically spanning 2-3 mm. The temporal resolution is limited by the hemodynamic response delay and the TR, making fMRI poorly suited for capturing fast neural dynamics that are accessible to [[eeg]] or [[meg]]. Additionally, the BOLD signal reflects a mixture of neuronal contributions—input, processing, and output—with varying weighting across brain regions and cortical layers, complicating straightforward interpretation in terms of specific neural computations.

## Related Concepts

- [[eeg]] – Complementary electrophysiological measure with high temporal resolution
- [[meg]] – Magnetic counterpart to EEG, offering improved spatial localization
- [[bold-signal]] – The underlying contrast mechanism
- [[resting-state]] – Task-free functional connectivity
- [[functional-connectivity]] – Statistical dependencies between regional time series
- [[fmri-vs-eeg|Fmri Vs Eeg]] – Comparison of fMRI and EEG methodologies
- [[connectome]] – [[structural-connectivity]] infrastructure
- [[whole-brain]] – Large-scale brain modeling approaches

## References

1. (authors unknown). *Brain magnetic resonance imaging with contrast dependent on blood oxygenation*.
2. (authors unknown). *Neurophysiological investigation of the basis of the fMRI signal*.
3. (authors unknown). *Statistical parametric maps in functional imaging: A general linear approach*.
4. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
5. (authors unknown). *Functional Network Organization of the Human Brain*.
6. Jiangnan Zhang, Chengyuan Qian, Wenlian Lu, Gustavo Deco, Weiyang Ding, Jianfeng Feng. (2025). *Dark Signals in the Brain: Augment Brain [[network-dynamics]] to the Complex-valued Field*. [Link](https://arxiv.org/abs/2509.24715)
7. Chetan Gohil, Oliver M. Cliff, James M. Shine, Ben D. Fulcher, Joseph T. Lizier. (2026). *Estimating measures of information processing during cognitive tasks using functional magnetic resonance imaging*. [Link](https://arxiv.org/abs/2602.03240)
8. Mennahtullah Mabrouk, Reem Reda, Hana Hisham, Abdelrahman Hazem, Bola Hosny, Hossam Elsawaf, Saif Elaswad, Sameh Sherif. (2025). *A Hybrid Learning Approach for Detection of Autism Spectrum Disorder Using fMRI Data*. 2025 13th International Japan-Africa Conference on Electronics, Communications, and Computations (JAC-ECC). [DOI](https://doi.org/10.1109/JAC-ECC67970.2025.11417627)
9. Xiaoqing Huang, Rishit Puri, Dayu Sun, Yi Zhao, Jie Zhang, Kun Huang, Yijie Wang. (2025). *Functional Connectome Signatures of Patients with Asymptomatic and Typical Alzheimer's*. Alzheimer's & Dementia. [DOI](https://doi.org/10.1002/alz70856_103445)
10. Xiaoyan Wu, Chuang Liang, J. Bustillo, Peter V. Kochunov, Xuyun Wen, Jing Sui, Rongtao Jiang, Xiao Yang, Zening Fu, Daoqiang Zhang, V. Calhoun, S. Qi. (2025). *The Impact of Atlas [[parcellation]] on Functional Connectivity Analysis Across Six Psychiatric Disorders*. Human Brain Mapping. [DOI](https://doi.org/10.1002/hbm.70206)