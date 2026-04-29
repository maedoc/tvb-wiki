# MA-SGNN: A Multi-view Adaptive Spiking Graph Neural Network for Event-based Tactile Recognition

**Source**: semantic-scholar
**ID**: 98853e663cf722bc580d6d81f2dac2388ce6a0af
**DOI**: 10.1109/BIBM66473.2025.11355976
**URL**: https://www.semanticscholar.org/paper/98853e663cf722bc580d6d81f2dac2388ce6a0af
**Date**: 2025-12-15
**Year**: 2025
**Authors**: W. Chi, Yingxue Zhang, Xiaolu Zhang, Mingyuan Ma, Jin Xu
**Venue**: IEEE International Conference on Bioinformatics and Biomedicine
**Citations**: 0

## Abstract

Real-time tactile perception with biological fidelity is critical for biomedical applications such as neural prosthetics and robotic surgeries, where sub-millisecond latency and micron-scale spatial resolution are essential. Event-based tactile sensors, inspired by mechanoreceptors, offer ultra-low latency and high energy efficiency but pose challenges for learning robust spatiotemporal representations under data scarcity and task variability. Current Spiking Graph Neural Networks (SGNNs) suffer from rigid spatial modeling and high computational costs, limiting deployment on edge devices. We propose MA-SGNN (Multi-view Adaptive SGNN), a lightweight brain-inspired framework emulating the biological tactile pathway: sensory encoding, feature extraction, and perceptual integration. MA-SGNN introduces: (1) a bio-hybrid spike encoder using Leaky Integrate-and- Fire neurons to capture temporal dynamics and extract biologically plausible features; (2) a multi-view adaptive graph constructor modeling structural and semantic taxel correlations via dynamic graphs; and (3) a spatiotemporal aggregator for efficient graph feature fusion. Evaluated on Ev-Objects and Ev-Containers benchmarks, MA-SGNN achieves competitive accuracy while reducing inference time by 59x and 90x versus state-of-the-art models. With only 10% training data, it maintains robust performance, dropping just 13.19%-significantly outperforming baselines. These results establish that MA-SGNN offers a biologically plausible and efficient solution for practical tactile intelligence.
