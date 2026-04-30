---
title: XPPAUT
created: 2025-01-15
updated: 2026-04-30
type: entity
tags: [software-brian, bifurcation-analysis, dynamical-systems-theory, computational-neuroscience, nonlinear-dynamics, network-dynamics]
sources: [10.1115/1.1579454, 10.1007/978-94-007-3858-4_17, 10.1007/s10827-010-0227-6, 9780198524311]
---

# XPPAUT

## Overview

XPPAUT (formerly XPP) is a powerful software environment for the numerical analysis and visualization of dynamical systems, with particular strength in analyzing nonlinear ordinary differential equations (ODEs), delay differential equations (DDEs), and stochastic differential equations [@10.1115/1.1579454]. Originally developed by Bard Ermentrout at the University of Pittsburgh, the name XPPAUT derives from "eXecutable Picture Painter" with "AUT" referring to its ability to perform AUTO continuation for detecting bifurcations. The software provides an interactive environment for phase plane analysis, continuation methods, and bifurcation detection, making it an essential tool for researchers studying neural dynamics and oscillatory behavior in computational neuroscience.

## Key Features

XPPAUT offers a comprehensive suite of capabilities for dynamical systems analysis. The core feature set includes **numerical integration** using over a dozen solvers (including Euler, Runge-Kutta, Adams, Gear, CVODE for stiff systems, Dormand-Prince, and implicit methods like backward Euler), **phase plane visualization** with nullcline plotting and vector fields, and **bifurcation analysis** through interfaces to AUTO for continuation and detection of fixed points, limit cycles, and bifurcations including Hopf, saddle-node, and period-doubling bifurcations.

The software supports **delay differential equations** with distributed delays, **stochastic differential equations** using Euler's method (the stochastic analog of Euler-Maruyama for SDEs), and **parameter continuation** for tracking solutions as parameters vary. Users can define models using a simple ASCII format specifying ODEs, parameters, and initial conditions, then interactively explore the model through parameter sweeps, Poincaré sections, and two-parameter bifurcation diagrams. XPPAUT also provides tools for **animation** of trajectories, **Fourier analysis** for studying oscillations, and **interactive graphing** that allows real-time manipulation of parameter values.

## Relationship to TVB and Whole-Brain Modeling

XPPAUT plays an important but specialized role in the whole-brain modeling ecosystem, particularly during the **model development and validation** phase. While The Virtual Brain and similar whole-brain simulators operate at the network level with structural connectivity matrices derived from diffusion imaging and neural field models, XPPAUT enables detailed analysis of the individual node dynamics that populate these large-scale models.

In practice, researchers developing neural mass models for use in whole-brain simulations often first prototype and validate their local dynamics in XPPAUT before implementing them in TVB. For example, the Jansen-Rit model, a cornerstone of EEG modeling in TVB, can be thoroughly analyzed in XPPAUT to understand its bifurcation structure, parameter sensitivity, and oscillatory regimes before being embedded in the larger network simulation [@10.1007/s10827-010-0227-6]. Similarly, neural mass formulations used for resting-state fMRI simulations in TVB benefit from XPPAUT's continuation tools to map out the excitability regimes.

XPPAUT also serves as a **conceptual exploration tool** for researchers investigating the mathematical foundations of brain dynamics. By isolating single-population or small-network dynamics, one can use XPPAUT to understand phenomena like bifurcations leading to epileptic transitions or the emergence of oscillations from excitation-inhibition balance.

## Related Software and Comparison

XPPAUT occupies a specific niche in the dynamical systems analysis landscape. It shares conceptual territory with AUTO (from which much of its continuation capability derives - see Doedel 1981 for original AUTO publication), and other similar tools. The software is distinct from general-purpose neural simulation environments like Brian, Brian 2, NEST, or NEURON in that it focuses on analytical tractability rather than detailed biophysical realism or large-scale network simulation.

For neural simulators, XPPAUT serves as a **complementary analysis tool** rather than a replacement. Researchers might use XPPAUT to characterize the parameter space of a neural model, then implement the validated model in NEST for large-scale spiking network simulations. This workflow leverages XPPAUT's strength in bifurcation analysis while using neural simulators for network-level inquiry [@9780198524311].

## Key Papers

- Ermentrout, B. (2002). *Simulating, Analyzing, and Animating Dynamical Systems: A Guide to XPPAUT for Researchers and Students*. SIAM. [@10.1115/1.1579454]
- Ermentrout, B. (2012). XPPAUT. In: Le Novère, N. (ed) *Computational Systems Neurobiology*. Springer. [@10.1007/978-94-007-3858-4_17]
- Doedel, E. (1981). AUTO: a program for the automatic bifurcation analysis of autonomous systems. *Proceedings of the tenth Manitoba conference on numerical mathematics and computing*.
- Various applications in neural dynamics modeling [@10.1007/s10827-010-0227-6], including work on reduced models for binocular rivalry and neural oscillations.

## References

[@10.1115/1.1579454]: Ermentrout, B., & Mahajan, A. (2003). Simulating, analyzing, and animating dynamical systems: A guide to XPPAUT for researchers and students. *Applied Mechanics Reviews*, 56(4), B53-B53.

[@10.1007/978-94-007-3858-4_17]: Ermentrout, B. (2012). XPPAUT. In: Le Novère, N. (ed) *Computational Systems Neurobiology* (pp. 519-531). Springer.

[@10.1007/s10827-010-0227-6]: Laing, C. R., Frewen, T., & Kevrekidis, I. G. (2010). Reduced models for binocular rivalry. *Journal of Computational Neuroscience*, 28(3), 459-476.

[@9780198524311]: Wilson, H. R. (1999). *Spikes, Decisions, and Actions: The Dynamical Foundations of Neuroscience*. Oxford University Press.