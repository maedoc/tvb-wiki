---
title: DeepLabCut
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-brian, software-neuron, software-nest, software-tvb]
sources: []
---

DeepLabCut is an open-source deep learning software package for markerless pose estimation in animals. Originally developed for tracking rodent whisker and forelimb movements, the tool has evolved into a general-purpose pose estimation framework widely adopted across neuroscience, ethology, and biomechanics research. The software enables researchers to annotate discrete body parts in video frames and train convolutional neural networks to automatically track these keypoints across entire recordings, replacing traditional marker-based motion capture systems that require physical markers glued to the subject.

## Technical Foundation

DeepLabCut employs a transfer learning approach, initializing convolutional neural networks with weights pre-trained on ImageNet before fine-tuning on user-provided labeled frames. The original implementation utilized ResNet-50 architectures, while newer versions incorporate more efficient architectures such as EfficientNet-B00. The training process requires only a small subset of manually annotated frames—typically 20-200 frames per body part—making the method practical for individual research labs. Once trained, the network can process video data at speeds exceeding 100 frames per second on modern GPUs, enabling real-time analysis for many experimental paradigms.

The software architecture separates data management, network training, and inference into distinct modules. Users interact primarily through configuration files that specify video sources, body part definitions, and training hyperparameters. The deeplabcut package provides both a command-line interface and Python API, facilitating integration with existing analysis pipelines.

## Applications in Neuroscience

Within the neuroscience domain, DeepLabCut serves as a critical tool for quantifying behavior in animal models. Applications include measuring gait parameters in Parkinson's disease models, tracking whisker movements during tactile perception tasks, quantifying social interactions in autism-related behavioral assays, and measuring forelimb trajectories in reaching tasks. The ability to extract precise spatiotemporal kinematic data has made DeepLabCut particularly valuable for correlating behavioral events with neural recordings obtained through [[electrophysiology]] or [[neuroimaging]] modalities.

The pose estimation output can be combined with downstream analyses including spectral decomposition of movement trajectories to identify [[brain-oscillations]] locked to specific motor actions, or used as regressors in [[fmri]] or [[eeg]] analysis to identify brain regions active during particular behaviors. Researchers studying [[epilepsy-modeling]] have used the tool to characterize seizure-associated movements and correlate these with electrophysiological biomarkers.

## Relationship to TVB and Whole-Brain Modeling

DeepLabCut occupies a distinct niche relative to [[the-virtual-brain]] and [[whole-brain-modeling]] frameworks. While TVB focuses on simulating large-scale neural dynamics across brain regions using [[neural-mass-models]] or [[dynamic-causal-modeling]], DeepLabCut provides behavioral data that can inform these models. Movement kinematics extracted from DeepLabCut analysis can serve as constraints or validation data for models of motor cortex, or provide timing signals for analyzing [[functional-connectivity]] patterns during goal-directed behaviors. The integration typically flows in one direction: behavioral measurements from DeepLabCut inform parameter selection or validation in computational brain models.

## Key Papers

The foundational paper introducing DeepLabCut appeared in Nature Neuroscience (Mathis et al., 2018) and demonstrated the method's accuracy across diverse species including mice, Drosophila, and horses. A subsequent technical paper (Mathis et al., 2020) provided the software toolkit documentation and demonstrated multi-animal tracking capabilities. The method has seen rapid adoption, with the core software now downloaded over 2 million times, and it has spawned an ecosystem of related tools including DeepLabCut-Live for real-time feedback applications, and extensions for 3D pose estimation when combined with multiple camera views.

## Related Software

DeepLabCut belongs to a family of pose estimation tools used in similar contexts. [[suite2p]] provides integrated spike sorting and pose estimation for two-photon imaging data. SLEAP (SuperLearner for Animal Pose) offers an alternative approach to markerless pose estimation. For traditional marker-based approaches, OptiTrack systems remain common in well-equipped laboratories. Research seeking to link behavioral measurements with neural dynamics may also employ [[brian2]] or [[neuron]] for neural simulation, or integrate with [[fieldtrip]] for analysis.

## Limitations and Considerations

Users should be aware of several limitations when deploying DeepLabCut. The quality of pose estimation depends critically on the representativeness and accuracy of manual annotations; poorly distributed training data leads to systematic errors. Occluded body parts require either specialized multi-animal tracking algorithms or careful experimental design to minimize ambiguities. The computational requirements for training can be substantial, typically requiring GPUs with 8GB or more of VRAM. Additionally, while the network generalizes reasonably across video conditions similar to training data, performance degrades for novel backgrounds or lighting conditions, necessitating targeted retraining or data augmentation strategies.