# Silicon Aware Neural Networks

**Source**: arxiv
**ID**: 2604.19334
**URL**: https://arxiv.org/abs/2604.19334
**Date**: 2026-04-21
**Year**: 2026
**Authors**: Sebastian Fieldhouse, Kea-Tiong Tang
**Categories**: cs.CV, eess.IV

## Abstract

Recent work in the machine learning literature has demonstrated that deep learning can train neural networks made of discrete logic gate functions to perform simple image classification tasks at very high speeds on CPU, GPU and FPGA platforms. By virtue of being formed by discrete logic gates, these Differentiable Logic Gate Networks (DLGNs) lend themselves naturally to implementation in custom silicon - in this work we present a method to map DLGNs in a one-to-one fashion to a digital CMOS standard cell library by converting the trained model to a gate-level netlist. We also propose a novel loss function whereby the DLGN can optimize the area, and indirectly power consumption, of the resulting circuit by minimizing the expected area per neuron based on the area of the standard cells in the target standard cell library. Finally, we also show for the first time an implementation of a DLGN as a silicon circuit in simulation, performing layout of a DLGN in the SkyWater 130nm process as a custom hard macro using a Cadence standard cell library and performing post-layout power analysis. We find that our custom macro can perform classification on MNIST with 97% accuracy 41.8 million times a second at a power consumption of 83.88 mW.
