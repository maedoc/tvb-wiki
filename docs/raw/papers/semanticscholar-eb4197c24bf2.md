# HUMA: Heterogeneous, Ultra Low-Latency Model Accelerator for The Virtual Brain on a Versal Adaptive SoC

**Source**: semantic-scholar
**ID**: eb4197c24bf208e19c6c741054fe9cd1327f2339
**DOI**: 10.1145/3706628.3708875
**URL**: https://www.semanticscholar.org/paper/eb4197c24bf208e19c6c741054fe9cd1327f2339
**Date**: 2025-02-27
**Year**: 2025
**Authors**: Amirreza Movahedin, Lennart P. L. Landsmeer, Christos Strydis
**Venue**: Symposium on Field Programmable Gate Arrays
**Citations**: 1

## Abstract

Brain modeling can occur at different levels of abstraction, each aimed at a different purpose. The Virtual Brain (TVB) is an open-source platform for constructing and simulating personalized brain-network models, favoring whole-brain macro-scales while reducing micro-level detail. Among other purposes, TVB is used to build patient-specific, digital, brain twins that can be used in different clinical settings, such as the study and treatment of epilepsy. However, fitting patient-specific TVB models requires a large number of successive and time-consuming simulations. By studying the internal structure of TVB, we observed heterogeneous computation needs in its models which could be leveraged to accelerate simulations. In this work, we designed and implemented HUMA, a heterogeneous, ultra low-latency, dataflow architecture on an AMD Versal Adaptive SoC to accelerate TVB fitting to different patient-brain makeups. Our heterogeneous solution runs about 27× faster compared to a modern-day, server-class, 32-core CPU while consuming a fraction of its power. Additionally, it delivers on average about 14× lower latency, 1.7× better power efficiency and an order-of-magnitude lower energy consumption when compared against the high-performance GPU version of TVB. The achieved latency savings reveal a significant potential in model-fitting for individual patients as well as in closed-loop biohybrid experiments.
