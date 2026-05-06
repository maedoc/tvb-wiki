# Scalarium: A Unified Scala-based Co-Simulation Framework for Agile Chip Development

**Source**: semantic-scholar
**ID**: 67b06f79dbce439d745a36cdd9e869b8ed9d21d7
**DOI**: 10.1109/ASP-DAC66049.2026.11420730
**URL**: https://www.semanticscholar.org/paper/67b06f79dbce439d745a36cdd9e869b8ed9d21d7
**Date**: 2026-01-19
**Year**: 2026
**Authors**: Yuefeng Zhang, Cheng-Yang Zhang, Wenkai Zhou, Binzhe Yuan, Junsheng Chen, Xiangyu Zhang, Hao Geng, Xin Lou
**Venue**: Asia and South Pacific Design Automation Conference
**Citations**: 0

## Abstract

Modern digital integrated circuit and system design workflows rely on hardware/software co-simulation that often employs multi-language methodologies (e.g., SystemC for modeling and Verilog HDL for implementation), introducing significant overhead from manual interface synchronization, cross-toolchain integration, and loss of high-level abstraction. To address these limitations, we propose Scalarium, a unified Scala-based cosimulation framework that integrates a cycle-driven simulator and SpinalHDL hardware modules within a single Scala environment, eliminating Verilog translation and proprietary DPI/PLI glue code. In particular, we propose: 1) a Scala-based iterative hardware design workflow for large-scale digital chip design; 2) an extensible cycle-driven simulation library for agile system modeling and accurate simulation, leveraging Scala’s expressive syntax and type system and 3) a unified co-simulation platform enabling automatic type-safe hardware/software binding, enabling direct data exchange. Evaluation on a neural rendering accelerator design project demonstrates a $74.8 \times$ simulation speedup over register-transfer level (RTL) with minimal functional deviation (6.5% and performance mismatch (2.4%), attributable to design differences rather than simulator inaccuracy. Scalarium enhances productivity, debuggability, and maintainability while preserving SpinalHDL’s verification advantages.
