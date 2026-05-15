---
title: PyRates
created: 2025-01-15
updated: 2026-05-13
type: entity
tags: [neural-mass-models, whole-brain-modeling, network-dynamics, dynamical-systems-theory, bifurcation-analysis, parameter-estimation, mean-field-theory, software-brain-modeling]
sources: []
---

## Overview

PyRates (Python Rates) is an open-source Python framework for building, simulating, and analyzing rate‑based neural population models. It provides a graph‑based modeling language that allows users to define networks of coupled [[neural-mass-models|neural masses]] at multiple spatial scales — from local microcircuits to [[whole-brain-modeling|whole‑brain networks]] — and automatically translates those high‑level descriptions into executable dynamical systems code. The framework is particularly notable for its clean separation of model specification from numerical implementation, enabling the same model definition to be solved with different backends (ODE integrators, GPU acceleration, or [[software-tvb|TVB]] interfaces) without rewriting equations.

## Motivation

The landscape of rate‑based neural modeling tools has long been fragmented. Researchers working with [[wilson-cowan-model|Wilson–Cowan]] oscillators, Jansen–Rit circuits, or custom firing‑rate equations typically hand‑code each model variant in MATLAB or Python, a process that is error‑prone and difficult to scale when exploring large parameter spaces or wiring model nodes onto [[structural-connectivity|structural connectomes]]. PyRates was developed to systematize this workflow: define the model once in a declarative format, then reuse it for time‑domain simulation, [[parameter-estimation|parameter sweeps]], [[bifurcation-analysis|bifurcation analysis]], and coupling to empirical [[diffusion-imaging|DTI‑derived connectomes]]. By treating model components as composable graph nodes — analogous to how [[software-nest|NEST]] treats spiking neurons, but operating at the population‑firing‑rate level — PyRates bridges the gap between abstract [[dynamical-systems-theory|dynamical systems theory]] and large‑scale network simulations grounded in human neuroanatomy.

## Key Features

### Graph‑Based Model Definition

Models in PyRates are specified as directed graphs where nodes represent neural populations (or sub‑populations) and edges define coupling between them. Each node carries a set of differential equations drawn from a template library that includes canonical models such as the [[jansen-rit-model|Jansen–Rit]] cortical column, the Wilson–Cowan excitatory–inhibitory circuit, and generic [[mean-field-theory|mean‑field]] formulations. Templates are parameterized using a simple YAML‑based syntax, making it straightforward to swap model equations, alter nonlinearities, or add conduction delays without touching the numerical solver. This modular design encourages systematic comparisons — for instance, evaluating how replacing a sigmoidal transfer function with a quadratic nonlinearity alters the [[bifurcation-theory|bifurcation structure]] of the same network topology.

### Multiple Backends and Auto‑Generated Code

Once a model graph is defined, PyRates compiles it into a computational backend. The default NumPy‑based backend uses just‑in‑time (JIT) compilation to produce efficient ODE right‑hand side functions, while optional backends target PyTorch (for GPU acceleration via CUDA) or TensorFlow (for automatic differentiation). A dedicated TVB backend converts PyRates model specifications into components that can be inserted directly into a [[tvb|The Virtual Brain]] simulation, allowing rate‑based local dynamics to drive whole‑brain [[network-dynamics|network simulations]] on personalized connectomes. This backend architecture means that a model validated on a small circuit with NumPy can be promoted to a full‑brain simulation with structural connectivity without re‑deriving a single equation.

### Bifurcation and Parameter Analysis

PyRates integrates with the numerical continuation library Auto‑07p to perform automated [[bifurcation-analysis|bifurcation analysis]] on any model defined within its graph framework. Users can trace families of fixed points, detect Hopf and saddle‑node bifurcations, and map regions of [[brain-oscillations|oscillatory]] versus quiescent behavior across multi‑dimensional parameter spaces. Combined with built‑in grid‑search and random‑search utilities, this makes PyRates a practical tool for systematically characterizing how network-level dynamics — such as transitions from asynchronous firing to synchronized oscillations — depend on local gains, coupling strengths, and conduction delays.

## Relationship to TVB

PyRates serves as an alternative front‑end for specifying local neural mass dynamics within [[tvb|The Virtual Brain]] ecosystem. While TVB ships with a curated library of built‑in neural mass models (the generic 2D oscillator, the Stefanescu–Jirsa reduced Wong–Wang model, the Montbrió–Pazó–Roxin exact mean‑field formulation), PyRates allows researchers to prototype entirely new rate‑based models and then export them as TVB‑compatible components. This workflow is especially valuable for testing novel model architectures — for example, cortical columns with multiple interacting inhibitory sub‑types — before committing them to full‑brain simulations. The PyRates‑to‑TVB pipeline preserves all parameter structure and coupling topology, and supports delayed interactions through TVB's standard time‑delayed integration scheme, ensuring that custom local dynamics interact correctly with long‑range [[structural-connectivity|structural connectivity]] and empirical BOLD forward models.

## Related Software

- [[tvb|The Virtual Brain]] — whole‑brain simulation platform that can consume PyRates‑generated models
- [[software-nest|NEST]] — spiking neural network simulator; complementary to PyRates's rate‑based approach
- [[software-brian|Brian]] — flexible spiking simulator with a similar philosophy of high‑level model specification
- NeuroML — model description language for neuronal models; PyRates occupies an analogous role at the population level
