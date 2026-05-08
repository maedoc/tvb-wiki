# Control Invariant Sets for Neural Network Dynamical Systems and Recursive Feasibility in Model Predictive Control

**Source**: semantic-scholar
**ID**: 16141455e127eee4a7280a4b78bfbcc863781dfd
**DOI**: 10.48550/arXiv.2505.11546
**URL**: https://www.semanticscholar.org/paper/16141455e127eee4a7280a4b78bfbcc863781dfd
**Date**: 2025-05-15
**Year**: 2025
**Authors**: Xiao Li, Tianhao Wei, Changliu Liu, Anouck Girard, I. Kolmanovsky
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Neural networks are powerful tools for data-driven modeling of complex dynamical systems, enhancing predictive capability for control applications. However, their inherent nonlinearity and black-box nature challenge control designs that prioritize rigorous safety and recursive feasibility guarantees. This paper presents algorithmic methods for synthesizing control invariant sets specifically tailored to neural network based dynamical models. These algorithms employ set recursion, ensuring termination after a finite number of iterations and generating subsets in which closed-loop dynamics are forward invariant, thus guaranteeing perpetual operational safety. Additionally, we propose model predictive control designs that integrate these control invariant sets into mixed-integer optimization, with guaranteed adherence to safety constraints and recursive feasibility at the computational level. We also present a comprehensive theoretical analysis examining the properties and guarantees of the proposed methods. Numerical simulations in an autonomous driving scenario demonstrate the methods' effectiveness in synthesizing control-invariant sets offline and implementing model predictive control online, ensuring safety and recursive feasibility.
