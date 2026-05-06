# FTPrimitiveBench: A Benchmark Suite For Logical Computation Under Hardware-Motivated and Biased Noise Models

**Source**: arxiv
**ID**: 2605.04049
**URL**: https://arxiv.org/abs/2605.04049
**Date**: 2026-05-05
**Year**: 2026
**Authors**: Shuwen Kan, Adrian Harkness, Zefan Du, Rod Rofougaran, Sean Garner, Chenxu Liu, Ying Mao, Samuel Stein
**Categories**: quant-ph

## Abstract

Fault-tolerant quantum computing requires understanding how error-correcting codes perform on diverse physical hardware. This is typically assessed via noisy stabilizer simulation of logical circuits at HPC scale, combined with a noise model that yields a logical error rate for the relevant code distances and depths. The uniform depolarizing model is the standard baseline, but its homogeneous assumptions fail to capture the heterogeneity, asymmetries, and correlations of real devices, where Pauli, measurement, and spatio-temporal errors are not weakly coupled. Yet these same structured features create opportunities for joint code-hardware co-design, motivating noise models that more faithfully reflect target hardware while remaining tractable to simulate.   We introduce FTPrimitiveBench, a systematic benchmarking approach for studying how logical primitives interact with hardware-motivated noise. It supports both custom specifications and representative structured noise families: Pauli bias, measurement bias, and spatial or spatio-temporal non-uniformity -- together with generators for core surface-code Clifford primitives: logical memory, lattice surgery, transversal logical Hadamard, and the logical phase gate via lattice surgery. We find that structured noise affects these primitives in qualitatively distinct ways, with outcomes shaped by the interplay between noise model, primitive, and decoder choice. These results extend memory benchmarks to active logical computation, where the interaction between noise structure and primitive implementation matters. By standardizing the link between noise-model specification and primitive construction, FTPrimitiveBench enables reproducible comparative studies of QEC protocols and decoders, supporting hardware-aware co-design of fault-tolerant architectures. Code: https://github.com/ShuwenKan/FTPrimitiveBench.
