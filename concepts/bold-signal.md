---
created: 2026-04-20
sources:
- raw/papers/ogawa-1990.md
- raw/papers/logothetis-2001.md
- raw/papers/arxiv-2512.24901.md
- raw/papers/arxiv-2604.03619.md
- raw/papers/semanticscholar-cc2129666e15.md
- raw/papers/semanticscholar-f52da2a6cbf2.md
- raw/papers/arxiv-2603.13598.md
tags:
- neuroimaging-fmri
- neurovascular-coupling
title: BOLD Signal
type: concept
updated: '2026-04-27'
---

# BOLD Signal

The Blood Oxygenation Level Dependent (BOLD) signal is the contrast mechanism underlying functional MRI, reflecting changes in blood oxygenation that accompany neural activity.

## Definition

Discovered by [[seiji-ogawa]] in 1990, the BOLD effect arises because deoxygenated hemoglobin is paramagnetic, creating local magnetic field inhomogeneities that affect MRI signal. Neural activity triggers a hemodynamic response that changes local blood oxygenation.

## Neurovascular Coupling

The chain from neural activity to BOLD:

1. **Neural activity** → Increased metabolic demand
2. **Vasodilation** → Increased cerebral blood flow (CBF)
3. **Overcompensation** → CBF increase exceeds oxygen consumption
4. **Oxygenation change** → Decreased deoxyhemoglobin
5. **Signal increase** → Reduced T2* decay, brighter MRI signal

## Neural Correlates

[[nikos-logothetis]] demonstrated that BOLD correlates most strongly with:
- **Local Field Potentials (LFPs)** – Input and local processing
- Less with multi-unit spiking activity

This informs how [[neural-mass-model]] outputs should be coupled to BOLD predictions.

## Hemodynamic Response Function (HRF)

The BOLD response to a brief neural event:
- **Delay**: ~1-2 seconds
- **Peak**: ~4-6 seconds
- **Undershoot**: Small dip after peak
- **Duration**: ~15-20 seconds total

## Role in Whole-Brain Modeling

1. **Forward model**: Neural activity → BOLD conversion
2. **Balloon model**: Biophysical model of hemodynamics
3. **Validation**: Compare simulated and empirical BOLD

## Related Concepts
- [[fmri]] – Imaging modality using BOLD
- neurovascular-coupling – Link between activity and hemodynamics
- hemodynamic-response-function – BOLD time course
- [[neural-mass-model]] – Generate activity for BOLD conversion

## References

1. (authors unknown). *Brain magnetic resonance imaging with contrast dependent on blood oxygenation*.
2. (authors unknown). *Neurophysiological investigation of the basis of the fMRI signal*.
3. Debasis Maji, Arghya Banerjee, Debaditya Barman. *Spectral Graph Neural Networks for Cognitive Task Classification in fMRI Connectomes*. [Link](https://arxiv.org/abs/2512.24901)
4. Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon. (2026). *Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?*. [Link](https://arxiv.org/abs/2604.03619)
5. Gianluca Gaglioti, L. Porta, M. Colombo, Simone Russo, Thierry Nieus, G. Deco, M. Corbetta, S. Sarasso, M. V. Sanchez-Vives, M. Massimini. (2026). *Slow wave generation and propagation in a model of brain lesions*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2026.121817)
6. Timo Hofsähs, Marius Pille, Lucas Kern, Anuja Negi, J. Meier, Petra Ritter. (2026). *The Virtual Brain links transcranial magnetic stimulation evoked potentials and inhibitory neurotransmitter changes in major depressive disorder*. bioRxiv. [DOI](https://doi.org/10.1101/2024.11.25.622620)
7. Kun Jiang, Can Liao, Sujin Jiang, Haidong Lin, Jixin Hou, Tianming Liu, Gang Li, Taotao Wu, Yiqi Mao, Ellen Kuhl, Xianqiao Wang, Xianyan Chen. *Tau-induced atrophy drives functional connectivity disruption in Alzheimer's disease*. [Link](https://arxiv.org/abs/2603.13598)