---
created: 2026-04-20
sources:
- raw/papers/ogawa-1990.md
- raw/papers/logothetis-2001.md
- raw/papers/niedermeyer-silva-2004.md
- raw/papers/nunez-srinivasan-2006.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/arxiv-2603.29903.md
- raw/papers/arxiv-2504.17491.md
- raw/papers/arxiv-2602.03240.md
- raw/papers/arxiv-2511.02457.md
- raw/papers/ritter-2013.md
- raw/papers/arxiv-2602.18715.md
tags:
- comparison
- neuroimaging-fmri
- neuroimaging-eeg
title: fMRI vs EEG for Whole-Brain Modeling
type: comparison
updated: '2026-04-27'
---

# fMRI vs EEG for Whole-Brain Modeling

Comparison of functional MRI and electroencephalography as neuroimaging modalities for whole-brain modeling validation and constraint.

## What is Being Compared

fMRI and EEG are complementary neuroimaging modalities that measure different aspects of brain activity. This comparison evaluates their relative strengths for constraining and validating whole-brain network models.

## Dimensions of Comparison

| Dimension | fMRI | EEG |
|-----------|------|-----|
| **Signal source** | Hemodynamic (BOLD) | Electrical potentials |
| **Temporal resolution** | ~1-3 seconds | ~1 ms |
| **Spatial resolution** | ~3 mm | ~1 cm (scalp) |
| **Directness** | Indirect (neurovascular coupling) | Direct (electrical activity) |
| **Coverage** | Whole brain | Cortical surface |
| **Invasiveness** | Non-invasive | Non-invasive |
| **Cost** | High | Low |
| **Portability** | Fixed scanner | Portable systems |
| **Signal-to-noise** | Moderate | Variable |

## Signal Characteristics

### fMRI
- Measures blood oxygenation changes via [[bold-signal]]
- neurovascular-coupling introduces ~6 second hemodynamic delay
- Correlates with local field potentials (LFPs) per [[nikos-logothetis]]
- Excellent for spatial localization of networks

### EEG
- Measures summed postsynaptic potentials
- Direct reflection of neural activity
- Volume conduction blurs spatial source localization
- Excellent for capturing fast dynamics and oscillations

## Whole-Brain Modeling Applications

### fMRI Strengths
- **Network topology**: Resting-state networks clearly spatially resolved
- **Structural-functional correspondence**: Direct comparison with DTI connectivity
- **Clinical translation**: Widely available for patient studies
- **BOLD simulation**: Well-established forward models (Balloon model)

### EEG Strengths
- **Temporal dynamics**: Captures millisecond-scale oscillations
- **Direct validation**: Neural mass models explicitly generate EEG-like signals
- **Frequency analysis**: Clear bands (alpha, beta, gamma) for model targets
- **Source localization**: Can estimate cortical generators

## Complementary Use

Optimal whole-brain modeling uses both modalities:

1. **fMRI**: Constrains spatial network organization
2. **EEG**: Validates temporal dynamics and oscillations
3. **Multimodal integration**: EEG-informed fMRI or joint modeling

## Synthesis

Neither modality alone is sufficient. fMRI provides the spatial organization that EEG lacks, while EEG provides the temporal resolution that fMRI lacks. Whole-brain models should be validated against both, with fMRI targeting network topology and EEG targeting oscillatory dynamics.

## Related Concepts
- [[fmri]] – Functional MRI
- [[eeg]] – Electroencephalography
- [[meg]] – Magnetic counterpart to EEG
- [[bold-signal]] – fMRI contrast mechanism
- neurovascular-coupling – Link between activity and BOLD
- volume-conduction – EEG signal spread

## References

1. (authors unknown). *Brain magnetic resonance imaging with contrast dependent on blood oxygenation*.
2. (authors unknown). *Neurophysiological investigation of the basis of the fMRI signal*.
3. (authors unknown). *Electroencephalography: Basic Principles, Clinical Applications, and Related Fields*.
4. (authors unknown). *Electric Fields of the Brain: The Neurophysics of EEG*.
5. Sakul Mahat, Sharmistha Guha, Jessica Bernard. (2026). *A Bayesian Framework for Quantifying Association Between Functional and Structural Data in Neuroimaging*. [Link](https://arxiv.org/abs/2603.21067)
6. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
7. Breno C. Bispo, Stefania Sardellitti, Juliano B. Lima, Fernando A. N. Santos. (2026). *Multimodal Higher-Order Brain Networks: A Topological Signal Processing Perspective*. [Link](https://arxiv.org/abs/2603.29903)
8. Cristiana Dimulescu, Ronja Strömsdörfer, Agnes Flöel, Klaus Obermayer. (2025). *On the robustness of the emergent spatiotemporal dynamics in biophysically realistic and phenomenological whole-brain models at multiple network resolutions*. [Link](https://arxiv.org/abs/2504.17491)
9. Chetan Gohil, Oliver M. Cliff, James M. Shine, Ben D. Fulcher, Joseph T. Lizier. (2026). *Estimating measures of information processing during cognitive tasks using functional magnetic resonance imaging*. [Link](https://arxiv.org/abs/2602.03240)
10. Mohaddese Qaremohammadlou, Mohammad Bagher Shamsollahi. (2025). *Investigating Brain Connectivity and Information Flow in Mental Workload Using EEG and fNIRS Integration*. [Link](https://arxiv.org/abs/2511.02457)
11. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)
12. Yifei Sun, James M. Shine, Robert D. Sanders, Robin F. H. Cash, Sharon L. Naismith, Fernando Calamante, Jinglei Lv. (2026). *A Data-Driven Method to Map the Functional Organisation of Human Brain White Matter*. [Link](https://arxiv.org/abs/2602.18715)