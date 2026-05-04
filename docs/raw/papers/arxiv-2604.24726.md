# VEHRON: A Configuration-Driven BEV Simulation Framework for Subsystem-Level Studies

**Source**: arxiv
**ID**: 2604.24726
**URL**: https://arxiv.org/abs/2604.24726
**Date**: 2026-04-27
**Year**: 2026
**Authors**: Subramanyam Natarajan
**Categories**: cs.CE, eess.SY

## Abstract

In practical early-stage battery-electric vehicle studies, analysis workflows may become fragmented across spreadsheets, notebooks, and project-specific scripts, making reuse, audit, and extension harder. VEHRON is an open-source Python framework for a deterministic, traceable workflow built around prescribed-speed longitudinal simulation of battery-electric vehicles using validated YAML configuration, packaged drive-cycle resources, interchangeable subsystem models, and auditable case outputs. VEHRON currently runs as a command-line workflow in which a vehicle definition and a testcase definition are combined to execute a simulation, emit a flat time series, and write a case package containing copied inputs, resolved configuration, summary metadata, and standard plots. Architecturally, VEHRON is organized around a small simulation engine, a shared state bus, a registry of model selections, schema-based configuration loading, and extension points for custom battery and HVAC models loaded from external Python files. VEHRON currently focuses on battery-electric longitudinal simulation with low-order battery, thermal, auxiliary-load, and HVAC models. This paper explains how VEHRON is structured, how it is used, which models it implements, and where its present limits lie. Source code is available at https://github.com/vehron-dev/vehron, with archived release metadata recorded under DOI https://doi.org/10.5281/zenodo.19820111.
