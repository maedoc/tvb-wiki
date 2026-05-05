# NLML: A Deep Neural Network Emulator for the Exact Nonlinear Interactions in a Wind Wave Model

**Source**: semantic-scholar
**ID**: 7e5da7d5d9e91f3ad82d95cb7612705c60e082cb
**DOI**: 10.1029/2025jh000699
**URL**: https://www.semanticscholar.org/paper/7e5da7d5d9e91f3ad82d95cb7612705c60e082cb
**Date**: 2026-01-23
**Year**: 2026
**Authors**: O. Ikuyajolu, Luke P. van Roekel, Steven R. Brus, Erin Thomas
**Venue**: Journal of Geophysical Research
**Citations**: 0

## Abstract


 
 Nonlinear wave interactions describe the resonant energy transfer between wave components, playing a fundamental role in the evolution of ocean wave spectra. Nonlinear wave interactions significantly influence wave growth and development, making them essential for accurate wave modeling. However, resolving the full six‐dimensional Boltzmann integral of the exact nonlinear wave interactions (Webb‐Resio‐Tracy method,
 WRT
 ) is computationally expensive, limiting its application in real‐time operational wave forecasting and for research purposes. Current approximations, such as the Discrete Interaction Approximation (
 DIA
 ), prioritize computational speed over accuracy, resulting in significant errors in wave mean parameters. Here, we introduce
 NLML
 , a machine learning (ML) emulator designed to approximate the exact nonlinear wave interactions within WAVEWATCH III (WW3), with the goal of achieving the accuracy of
 WRT
 while maintaining the stability and computational speed of
 DIA
 . By leveraging GPU capabilities such as half precision inference, we achieved substantial speedups, up to 136 faster than the
 WRT
 and only a modest 1.04 slowdown relative to
 DIA
 , while achieving 2 the accuracy of
 DIA
 in global wave spectral energy and mean wave parameters, with up to 7 higher accuracy in some regions. Unlike previous ML approaches,
 NLML
 maintained inherent stability throughout model integration in a standalone, year‐long WW3 simulation, without requiring additional constraints. Our new ML parameterization bridges the gap between accuracy and efficiency, offering a promising alternative for improving wave modeling in operational settings and research purposes.

