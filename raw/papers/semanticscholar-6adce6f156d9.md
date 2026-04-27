# A Framework for Automatic Synthesis of Neuromorphic Architectures with Heterogeneous Integration of CMOS and Memristors

**Source**: semantic-scholar
**ID**: 6adce6f156d92aaaceef5a69c30ee23df9fcd997
**DOI**: 10.1109/ISCAS56072.2025.11043873
**URL**: https://www.semanticscholar.org/paper/6adce6f156d92aaaceef5a69c30ee23df9fcd997
**Date**: 2025-05-25
**Year**: 2025
**Authors**: Sarah Johari, Arghavan Mohammadhassani, Anup Das
**Venue**: International Symposium on Circuits and Systems
**Citations**: 0

## Abstract

A hybrid CMOS-memristor design can significantly enhance the energy efficiency of neuromorphic systems, particularly those implementing spiking neural networks (SNNs). In such a hybrid design, neurons are implemented using CMOS transistors, while synaptic weights are implemented using memristive devices such as resistive RAM (RRAM). We propose a framework for automatic synthesis of such designs at the SPICE level starting from an SNN model defined in a high-level language such as Python. Given the ubiquity of PyTorch in the machine learning community and for demonstration purposes, the frontend of the proposed framework is integrated with a torch-based SNN simulator for model specification and training. Its backend is integrated with a SPICE simulator, e.g., Synopsys HSPICE. We built an open-source application programming interface (API) to compile an SNN model down to its hybrid implementation as a crossbar-based or layer-based microarchitecture, which can subsequently be simulated to verify the design for a wide range of learning tasks and datasets. We show the capability of this framework to perform circuit-oriented design space exploration.
