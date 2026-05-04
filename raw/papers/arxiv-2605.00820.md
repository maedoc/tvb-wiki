# HyCOP: Hybrid Composition Operators for Interpretable Learning of PDEs

**Source**: arxiv
**ID**: 2605.00820
**URL**: https://arxiv.org/abs/2605.00820
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Jinpai Zhao, Nishant Panda, Yen Ting Lin, Eirik Valseth, Diane Oyen, Clint Dawson
**Categories**: cs.CE, cs.LG, math.NA

## Abstract

We introduce HyCOP, a modular framework that learns parametric PDE solution operators by composing simple modules (advection, diffusion, learned closures, boundary handling) in a query-conditioned way. Rather than learning a monolithic map, HyCOP learns a policy over short programs - which module to apply and for how long - conditioned on regime features and state statistics. Modules may be numerical sub-solvers or learned components, enabling hybrid surrogates evaluated at arbitrary query times without autoregressive rollout. Across diverse PDE benchmarks, HyCOP produces interpretable programs, delivers order-of-magnitude OOD improvements over monolithic neural operators, and supports modular transfer through dictionary updates (e.g., boundary swaps, residual enrichment). Our theory characterizes expressivity and gives an error decomposition that separates composition error from module error and doubles as a process-level diagnostic.
