# Scaling Up Resonate-and-Fire Networks for Fast Deep Learning

**Source**: semantic-scholar
**ID**: 97f309923fd601b70bf3340a8d268e3f6a77a627
**DOI**: 10.48550/arXiv.2504.00719
**URL**: https://www.semanticscholar.org/paper/97f309923fd601b70bf3340a8d268e3f6a77a627
**Date**: 2025-04-01
**Year**: 2025
**Authors**: T. Huber, Jules Lecomte, Borislav Polovnikov, A. V. Arnim
**Venue**: ECCV Workshops
**Citations**: 5

## Abstract

Spiking neural networks (SNNs) present a promising computing paradigm for neuromorphic processing of event-based sensor data. The resonate-and-fire (RF) neuron, in particular, appeals through its biological plausibility, complex dynamics, yet computational simplicity. Despite theoretically predicted benefits, challenges in parameter initialization and efficient learning inhibited the implementation of RF networks, constraining their use to a single layer. In this paper, we address these shortcomings by deriving the RF neuron as a structured state space model (SSM) from the HiPPO framework. We introduce S5-RF, a new SSM layer comprised of RF neurons based on the S5 model, that features a generic initialization scheme and fast training within a deep architecture. S5-RF scales for the first time a RF network to a deep SNN with up to four layers and achieves with 78.8% a new state-of-the-art result for recurrent SNNs on the Spiking Speech Commands dataset in under three hours of training time. Moreover, compared to the reference SNNs that solve our benchmarking tasks, it achieves similar performance with much fewer spiking operations. Our code is publicly available at https://github.com/ThomasEHuber/s5-rf.
