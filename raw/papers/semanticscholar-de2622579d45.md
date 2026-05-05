# Decoupling model descriptions from execution: a modular paradigm for extensible neurosimulation with EDEN

**Source**: semantic-scholar
**ID**: de2622579d4537f419dbb458c192f4a3b459bd4d
**DOI**: 10.3389/fninf.2025.1572782
**URL**: https://www.semanticscholar.org/paper/de2622579d4537f419dbb458c192f4a3b459bd4d
**Date**: 2025-08-07
**Year**: 2025
**Authors**: Sotirios Panagiotou, Rene Miedema, Dimitrios Soudris, Christos Strydis
**Venue**: Frontiers Neuroinformatics
**Citations**: 0

## Abstract

Computational-neuroscience simulators have traditionally been constrained by tightly coupled simulation engines and modeling languages, limiting their flexibility and scalability. Retrofitting these platforms to accommodate new backends is often costly, and sharing models across simulators remains cumbersome. This paper puts forward an alternative approach based on the EDEN neural simulator, which introduces a modular stack that decouples abstract model descriptions from execution. This architecture enhances flexibility and extensibility by enabling seamless integration of multiple backends, including hardware accelerators, without extensive reprogramming. Through the use of NeuroML, simulation developers can focus on high-performance execution, while model users benefit from improved portability without the need to implement custom simulation engines. Additionally, the proposed method for incorporating arbitrary simulation platforms—from model-optimized code kernels to custom hardware devices—as backends offers a more sustainable and adaptable framework for the computational-neuroscience community. The effectiveness of EDEN's approach is demonstrated by integrating two distinct backends: flexHH, an FPGA-based accelerator for extended Hodgkin-Huxley networks, and SpiNNaker, the well-known, neuromorphic platform for large-scale spiking neural networks. Experimental results show that EDEN integrates the different backends with minimal effort while maintaining competitive performance, reaffirming it as a robust, extensible platform that advances the design paradigm for neural simulators by achieving high generality, performance, and usability.
