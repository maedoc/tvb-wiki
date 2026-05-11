# HyDRASim: A Versatile and Cycle-Accurate Simulator for Hybrid DRAM PIM-CPU Systems

**Source**: semantic-scholar
**ID**: 64b5470fa5d9bfdafa1fce846c08a9e77f04fca5
**DOI**: 10.1109/MASCOTS67699.2025.11283206
**URL**: https://www.semanticscholar.org/paper/64b5470fa5d9bfdafa1fce846c08a9e77f04fca5
**Date**: 2025-10-21
**Year**: 2025
**Authors**: Jihoon Jang, Inseong Hwang, Hyun Kim
**Venue**: IEEE/ACM International Symposium on Modeling, Analysis, and Simulation On Computer and Telecommunication Systems
**Citations**: 0

## Abstract

Recent advancements in deep neural networks (DNNs) have exacerbated the data movement bottleneck inherent in traditional von Neumann architectures. Processing-in-memory (PIM) has emerged as a promising paradigm by integrating computation within memory to alleviate this challenge. However, the lack of versatile and cycle-accurate simulation frameworks significantly limits the evaluation and optimization of diverse PIM designs. Existing in-house PIM simulators tend to be narrowly tailored to specific architectures, lacking generality and extensibility across hybrid computing environments. In this paper, we introduce HyDRASim, a cycle-accurate and extensible PIM-CPU simulator designed to support a wide range of PIM architectural features. HyDRASim integrates ZSim for detailed CPU modeling with DRAMSim3 for accurate memory modeling to enable flexible simulation across CPU-only, PIM-only, and PIM-CPU hybrid configurations. Validation experiments using GEMV workloads of varying sizes demonstrate that HyDRASim achieves cycle-level fidelity, with average latency and power errors of just $5.92 \%$ and $5.61 \%$, respectively, compared to established in-house baselines. Furthermore, system-level performance evaluations with diverse DNN workloads reveal that transformer-based models achieve $2.21 \times$ greater acceleration compared to convolutional neural networks under hybrid configurations modeled with HyDRASim. These results establish HyDRASim as a reliable and powerful tool for accurately modeling, evaluating, and optimizing emerging PIM-CPU hybrid architectures, providing critical insights into the future of memory-centric system design. We open-source HyDRASim at https://github.com/IDSL-SeoulTech/HyDRASim
