---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-3256c8880985.md
- raw/papers/izhikevich-2007.md
tags:
- software-brian
- bifurcation-analysis
- dynamical-systems-theory
- computational-neuroscience
- nonlinear-dynamics
- network-dynamics
title: XPPAUT
type: entity
updated: '2026-05-01'
---

# XPPAUT

## Overview

XPPAUT (formerly XPP) is a powerful software environment for the numerical analysis and visualization of dynamical systems, with particular strength in analyzing nonlinear ordinary differential equations (ODEs), delay differential equations (DDEs), and stochastic differential equations. Originally developed by Bard Ermentrout at the University of Pittsburgh, the name XPPAUT derives from "eXecutable Picture Painter" with "AUT" referring to its ability to perform AUTO continuation for detecting bifurcations [[cat12]]. The software provides an interactive environment for phase plane analysis, continuation methods, and bifurcation detection, making it an essential tool for researchers studying [[neural-mass-models|neural mass models]] and [[brain-oscillations|brain oscillations]] in [[computational-neuroscience|computational neuroscience]].

## Key Features

XPPAUT offers a comprehensive suite of capabilities for dynamical systems analysis. The core feature set includes **numerical integration** using a variety of solvers including Euler, Runge-Kutta (4th order), Adams-Bashforth, Gear (stiff/BDF), Backward Euler, CVODE (stiff), Dormand-Prince, and Rosenbrock methods [[cat12]], supporting both stiff and non-stiff systems. The software provides **phase plane visualization** with nullcline plotting and vector fields, and **bifurcation analysis** through interfaces to [[auto-07p|AUTO]] for continuation and detection of fixed points, limit cycles, and bifurcations including Hopf, saddle-node, and period-doubling bifurcations [[homer3]].

The software supports **delay differential equations** with distributed delays, **[[stochastic-differential-equations]]** through stochastic trajectory computation and averaging, and **parameter continuation** for tracking solutions as parameters vary. Users can define models using a simple ASCII format specifying ODEs, parameters, and initial conditions, then interactively explore the model through parameter sweeps, Poincaré sections, and two-parameter bifurcation diagrams. XPPAUT also provides tools for **animation** of trajectories, **Fourier analysis** for studying oscillations, and **interactive graphing** that allows real-time manipulation of parameter values.

## Relationship to TVB and Whole-Brain Modeling

XPPAUT plays an important but specialized role in the [[whole-brain-modeling|whole-brain modeling]] ecosystem, particularly during the **model development and validation** phase. While [[the-virtual-brain|TVB]] and similar [[whole-brain-simulators|whole-brain simulators]] operate at the network level with [[structural-connectivity|structural connectivity]] matrices derived from diffusion imaging and neural field models, XPPAUT enables detailed analysis of the individual node dynamics that populate these large-scale models.

In practice, researchers developing [[neural-mass-models|neural mass models]] for use in whole-brain simulations often first prototype and validate their local dynamics in XPPAUT before implementing them in TVB. For example, the [[jansen-rit-model|Jansen-Rit model]], a cornerstone of [[eeg|EEG]] modeling in TVB, can be thoroughly analyzed in XPPAUT to understand its bifurcation structure, parameter sensitivity, and oscillatory regimes before being embedded in the larger network simulation. Similarly, the [[wong-wang-model|Wong-Wang model]] and its variants, used for resting-state fMRI simulations in TVB, benefit from XPPAUT's continuation tools to map out the excitability regimes.

XPPAUT also serves as a **conceptual exploration tool** for researchers investigating the mathematical foundations of [[brain-dynamics]]. By isolating single-population or small-[[network-dynamics]], one can use XPPAUT to understand phenomena like bifurcations leading to epileptic transitions or the emergence of oscillations from excitation-inhibition balance.

## Related Software and Comparison

XPPAUT occupies a specific niche in the dynamical systems analysis landscape. It shares conceptual territory with [[auto-07p|AUTO]] (from which much of its continuation capability derives) and [[matcont|MATCONT]] (a MATLAB-based alternative). The software is distinct from general-purpose neural simulation environments like [[brian|Brian]], [[brian2|Brian 2]], [[nest|NEST]], or [[neuron|NEURON]] in that it focuses on analytical tractability rather than detailed biophysical realism or large-scale network simulation.

For neural simulators, XPPAUT serves as a **complementary analysis tool** rather than a replacement. Researchers might use XPPAUT to characterize the parameter space of an [[izhikevich-neuron-model]], then implement the validated model in NEST for large-scale spiking network simulations. This workflow leverages XPPAUT's strength in bifurcation analysis while using neural simulators for network-level inquiry.

## Key Papers and Historical Context

XPPAUT emerged from the tradition of dynamical systems software pioneered by Bard Ermentrout and has been central to numerous advances in theoretical neuroscience. The software has been instrumental in characterizing [[wilson-cowan]] dynamics, [[kuramoto]] model phase synchronization, and various neural mass formulations. The definitive reference for XPPAUT is Ermentrout's book "Simulating, Analysing, and Animating Dynamical Systems" published by SIAM. While the software itself predates the modern era of large-scale brain simulation represented by TVB, it remains an essential tool in the modeler's toolkit for understanding the fundamental dynamics that underlie [[whole-brain]] models.

## Related Concepts

- [[bifurcation-analysis|Bifurcation Analysis]]
- [[dynamical-systems-theory|Dynamical Systems Theory]]
- [[neural-mass-models|Neural Mass Models]]
- [[whole-brain-modeling|Whole-Brain Modeling]]
- [[brain-oscillations|Brain Oscillations]]
- [[computational-neuroscience|Computational Neuroscience]]
- [[auto-07p|AUTO]]
- [[matcont|MATCONT]]

## References

1. Ermentrout, B. (2023). XPPAUT Homepage. University of Pittsburgh. https://sites.pitt.edu/~phase/bard/bardware/xpp/xpp.html

2. Ermentrout, B. (2023). XPP - Numerics. XPPAUT Documentation. https://sites.pitt.edu/~phase/bard/bardware/xpp/help/xppnumerics.html

3. Ermentrout, B. (2023). XPP AUTO. XPPAUT Documentation. https://sites.pitt.edu/~phase/bard/bardware/xpp/help/xppauto.html

4. Ermentrout, B. (2002). Simulating, Analysing, and Animating Dynamical Systems. SIAM.

5. Deco, G., Jirsa, V.K., Robinson, P.A., Breakspear, M., & Friston, K. (2008). The dynamic brain: from spiking neurons to neural masses and cortical rhythms. PLoS Computational Biology, 4(8), e1000092.