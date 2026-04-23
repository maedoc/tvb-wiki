# Full Feature Spiking Neural Network Simulation on Micro-Controllers for Neuromorphic Applications at the Edge

**Source**: arxiv
**ID**: 2604.16474
**URL**: https://arxiv.org/abs/2604.16474
**Date**: 2026-04-11
**Year**: 2026
**Authors**: L. Niedermeier, J. L. Krichmar
**Categories**: cs.AR, cs.AI, cs.NE

## Abstract

Microcontroller units (MCU), which have an order of magnitude lower Size, Weight and Power (SWaP) than standard computers, makes them suitable for applications at the edge. Neuromorphic computing, which can realize low SWaP, relies on Spiking Neural Networks (SNNs). Until now, software based simulations of SNNs required GPU-based workstations, application classified core processors such as the ARM Cortex-A53, or specialized hardware like Intel's Loihi. In the present work, we demonstrate that the SNN simulator CARLsim can run its full feature set on a MCU RP2350 with 8 MB memory. We accomplished this by utilizing IEEE 16-bit float point numbers, which reduced memory requirements without loss of function. We were able to run the Synfire4 benchmark which comprises 1200 neurons. The accuracy was 97.5% compared to the standard single precision numbers. Furthermore, we show that CARLsim runs a Synfire4 benchmark scaled-down to 186 neurons on a MCU in real-time at only 20 mW. Compared to the smallest application class ARM processor used by Raspberry in their Pi Zero 2 W, our MCU implementation is five times more energy efficient for the SNN itself, and an order of magnitude better when compared to the complete SoC (MCU/CPU + Board).
