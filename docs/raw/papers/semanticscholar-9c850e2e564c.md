# High-Accuracy MOSFET Modeling and Characterization Using Neural Networks with Automated SPICE Model Conversion

**Source**: semantic-scholar
**ID**: 9c850e2e564c6d2536164a63606dadedf3f0d382
**DOI**: 10.1109/SDPC68151.2025.11347616
**URL**: https://www.semanticscholar.org/paper/9c850e2e564c6d2536164a63606dadedf3f0d382
**Date**: 2025-11-21
**Year**: 2025
**Authors**: Hanguang Jia, Shilie He, Yaiqong Ding
**Venue**: 2025 IEEE International Conference on Sensing, Diagnostics, Prognostics, and Control
**Citations**: 0

## Abstract

The relentless advancement in power electronic semiconductor technology is outstripping the capabilities of traditional, purely physics-based modeling approaches. Their inherent computational cost and the difficulty in accurately formulating the complex physics of novel devices create significant bottlenecks. This is driving a fundamental shift towards more pragmatic, efficient, and often data-driven or hybrid modeling paradigms to keep pace with design and innovation demands. The future lies in intelligently combining physical understanding with advanced computational methods and machine learning. This paper presents a data-driven method that leverages the universal function approximation capabilities of Neural Networks (NNs) and a Python-based NN-to-SPICE converter for accurate and efficient MOSFET (Metal Oxide Semiconductor Field Effect Transistor) modeling and simulation. This research involved conducting device-level TCAD simulations for a MOSFET, which yielded a comprehensive raw dataset containing millions of data points. A detailed development process of data-driven NN models that demonstrate remarkable fidelity in capturing both DC (I-V) and AC (C-V) characteristics across diverse bias conditions and temperatures is provided. A cornerstone of this research is an automated methodology for converting these highly accurate, trained NN models into SPICE models in the Verilog-A language. This crucial step enables their direct and efficient integration into industry-standard SPICE circuit simulators, bridging the gap between device-level model development and practical EDA workflows. It can be concluded that, under various bias conditions, the NN models demonstrated excellent agreement with the TCAD simulation data. Crucially, the development of such high-fidelity, computationally efficient models is a foundational step for advanced prognostics and health management (PHM). At the device level, they provide a precise baseline for detecting degradation, while their system-level integration enables the simulation of how component aging impacts overall circuit and system reliability. This work offers a transformative pathway towards more agile, precise, and extensible MOSFET modeling paradigms.
