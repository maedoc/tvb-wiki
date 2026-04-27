# Parameter and hidden-state inference in mean-field models from partial observations of finite-size neural networks

**Source**: semantic-scholar
**ID**: 274d3afcf4f54ddb5bd2122157c2ab2a105b41ef
**URL**: https://www.semanticscholar.org/paper/274d3afcf4f54ddb5bd2122157c2ab2a105b41ef
**Date**: 2026-02-10
**Year**: 2026
**Authors**: Irmantas Ratas, Kestutis Pyragas
**Citations**: 0

## Abstract

We study large but finite neural networks that, in the thermodynamic limit, admit an exact low-dimensional mean-field description. We assume that the governing mean-field equations describing macroscopic quantities such as the mean firing rate or mean membrane potential are known, while their parameters are not. Moreover, only a single scalar macroscopic observable from the finite network is assumed to be measurable. Using time-series data of this observable, we infer the unknown parameters of the mean-field equations and reconstruct the dynamics of unobserved (hidden) macroscopic variables. Parameter estimation is carried out using the differential evolution algorithm. To remove the dependence of the loss function on the unknown initial conditions of the hidden variables, we synchronize the mean-field model with the finite network throughout the optimization process. We demonstrate the methodology on two networks of quadratic integrate-and-fire neurons: one exhibiting periodic collective oscillations and another displaying chaotic collective dynamics. In both cases, the parameters are recovered with relative errors below $1\%$ for network sizes exceeding 1000 neurons.
