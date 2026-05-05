# A Convolutional Neural Network to Spiking Neural Network Conversion Framework for Seismic Denoising

**Source**: semantic-scholar
**ID**: 778b24a0c82753cc9a7b3ff2c0c331bc51f32182
**DOI**: 10.1109/ACCESS.2025.3617570
**URL**: https://www.semanticscholar.org/paper/778b24a0c82753cc9a7b3ff2c0c331bc51f32182
**Year**: 2025
**Authors**: Shuna Chen, Zhege Liu, Ziyu Qin, Xinyi Liu, Ya‐juan Xue, Junxing Cao
**Venue**: IEEE Access
**Citations**: 1

## Abstract

This study investigates the application of Spiking Neural Network (SNN) in seismic signal denoising by developing a Convolutional Neural Network (CNN) to SNN conversion framework. We focus on two challenges: optimal spike encoding strategy adaptation for seismic data; and denoising performance preservation during CNN-SNN conversion. Through systematic experiments on the public Marmousi 2 dataset and field data from Sichuan Basin, we demonstrate that SNN can feasibly serve as an alternative to traditional CNN for seismic denoising tasks. Our experiments show that both count-rate encoding (CR) and time-to-first-spike coding (TTFS) can effectively encode seismic data. However, when integrated with the proposed CNN-SNN conversion framework for seismic denoising, CR outperforms TTFS due to structural mismatches between TTFS and the framework in signal representation, temporal control, and weight mapping, which lead to information loss. Our neuron optimization strategy combines soft reset mechanisms with adaptive thresholding, demonstrating enhanced performance that narrows the gap between native CNN and converted SNN implementations. To enable rigorous evaluation, we introduce a baseline alignment scheme ensuring fair comparison between the native CNN and its CNN-SNN converted architecture. This work demonstrates the first successful application of SNN to seismic signal denoising, offering a bio-inspired alternative to conventional CNN while preserving comparable signal-to-noise ratio performance.
