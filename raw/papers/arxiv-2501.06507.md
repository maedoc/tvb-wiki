# Efficient stochastic simulation of piecewise-deterministic Markov processes and its application to the Morris–Lecar model of neural dynamics

**Source**: semantic-scholar
**ID**: bf35ec8a2c5a981a61c997d96223c30eec0ed422
**DOI**: 10.1007/s00422-025-01004-6
**URL**: https://www.semanticscholar.org/paper/bf35ec8a2c5a981a61c997d96223c30eec0ed422
**Date**: 2025-01-11
**Year**: 2025
**Authors**: A. Pikovsky
**Venue**: Biological cybernetics
**Citations**: 1

## Abstract

Piecewise-deterministic Markov processes combine continuous in time dynamics with jump events, the rates of which generally depend on the continuous variables and thus are not constants. This leads to a problem in a Monte-Carlo simulation of such a system, where, at each step, one must find the time instant of the next event. The latter is determined by an integral equation and usually is rather slow in numerical implementation. We suggest a reformulation of the next event problem as an ordinary differential equation where the independent variable is not the time but the cumulative rate. This reformulation is similar to the Hénon approach to efficiently constructing the Poincaré map in deterministic dynamics. The problem is then reduced to a standard numerical task of solving a system of ordinary differential equations with given initial conditions on a prescribed interval. We illustrate the method with a stochastic Morris–Lecar model of neuron spiking with stochasticity in the opening and closing of voltage-gated ion channels.
