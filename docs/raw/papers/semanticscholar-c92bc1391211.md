# NeuroClean: A Benchmarking and Optimization Framework for EEG Preprocessing in Semantic Brain-to-Text Decoding

**Source**: semantic-scholar
**ID**: c92bc1391211a9fe9af7d37eff4a0197e491b823
**DOI**: 10.1109/CINS67018.2025.11412037
**URL**: https://www.semanticscholar.org/paper/c92bc1391211a9fe9af7d37eff4a0197e491b823
**Date**: 2025-11-25
**Year**: 2025
**Authors**: P. Pawar, Nilima Kulkarni
**Venue**: 2025 3rd International Conference on Computational Intelligence and Network Systems (CINS)
**Citations**: 0

## Abstract

Brain-to-text systems are rapidly emerging at the intersection of neuroscience, brain–computer interfaces (BCIs), and artificial intelligence, aiming to decode neural signals into coherent text. While advances in LLMs and EEG decoding models have shown early promise, the preprocessing of raw EEG signals remains an underexplored but critical bottleneck. Most current systems reuse pipelines from ERP or motor imagery tasks, which are poorly suited for extracting semantic content from naturalistic thought processes.We introduce NeuroClean, a modular benchmarking environment purpose-built for optimizing EEG preprocessing in semantic brain-to-text decoding. We systematically evaluate combinations of filtering, artifact removal, referencing, and epoching methods across multiple datasets, including both stimulus-driven and resting-state EEG. We use both signal-quality metrics (e.g., SNR, entropy) and semantic readiness metrics, such as alignment with sentence embeddings from LLMs and classification accuracy in thought-tagging tasks. Our results show that traditional pipelines optimized for motor-control BCI underperform when applied to language decoding tasks. Notably, wavelet-based denoising, adaptive artifact rejection, and Laplacian referencing yield significant improvements in semantic fidelity of the resulting EEG features.NeuroClean fills a critical gap by offering a reproducible, extensible preprocessing benchmarking toolkit, paving the way for more robust EEG-to-text pipelines. We conclude by recommending best practices and providing open-source code to support future work in cognitive decoding and brain-aligned generative AI systems.Implementation-level validation has been performed through systematic design analysis on benchmark EEG corpora such as ZuCo and BCI-IV with a focus on establishing reproducible baselines for future experimental benchmarking. The present study outlines a conceptual yet implementation-ready framework, all modules have been defined with implementation-ready specifications, and the framework will serve as the baseline for empirical benchmarking in subsequent experimental validation phases.
