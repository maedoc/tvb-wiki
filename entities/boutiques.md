---
title: Boutiques
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-modeling, software-visualization, reproducibility, computational-neuroscience, bids, neuroml]
sources: [https://boutiques.github.io/, https://github.com/boutiques/boutiques, https://incf.org/]
---

## Overview

Boutiques is a JSON-based framework and software tool for describing, discovering, and executing neuroscience computational tools in a standardized, reproducible manner. Developed through the McGill Centre for Integrative Neuroscience (MCIN) with support from the International Neuroinformatics Coordinating Facility (INCF), Boutiques provides a unified schema—the Boutiques Descriptor—that captures the essential characteristics of neuroscience software including input parameters, output files, computational requirements, and execution patterns. The system enables researchers to discover tools via Zenodo-based registries and the CBRAIN platform, generate command-line interfaces automatically, and execute tools consistently across different computing environments through semantic descriptions rather than platform-specific configurations.

## Motivation and Context

The landscape of neuroscience software suffers from significant heterogeneity in how tools are described, installed, and executed. Different research groups develop tools using varying programming languages, dependency management systems, and interface conventions, making it notoriously difficult to reproduce computational workflows or integrate tools from different labs into a coherent pipeline. Before Boutiques, there was no standardized way to capture what a neuroscience tool does, what it requires, and how to run it in a machine-readable format that could be consumed by workflow managers, containerization systems, or reproducibility platforms.

Boutiques emerged from the recognition that reproducibility in computational neuroscience requires more than just sharing code—it requires sharing executable specifications of computational processes. The Boutiques schema addresses this gap by providing a formal specification that describes tools in terms of their conceptual function (what they compute), their input-output contract (what inputs they accept and what outputs they produce), and their runtime environment (what computational resources they require). This semantic description layer enables higher-level tools to reason about neuroscience software in terms of its computational semantics rather than its implementation details, facilitating automated pipeline construction, cloud-based execution, and reproducible scientific workflows.

## Technical Specification

The Boutiques Descriptor uses JSON Schema to define tool characteristics with several key structural components. The `command-line` field specifies how parameters are translated into actual command invocations, using template syntax that maps input parameters to command-line arguments. The `inputs` section defines each parameter with type information (string, number, boolean, or file), optionality, default values, and semantic constraints such as minimum/maximum values or valid value lists. The `output-files` section specifies what files the tool produces, including optionality and wildcard patterns for variable output names.

A distinctive feature of Boutiques is its support for **container invocation** through the `container-image` field, which specifies Docker or Singularity images that provide the tool's runtime environment. This enables Boutiques to execute tools reproducibly by bundling both the tool code and its dependencies into a portable container. The schema also includes `groups` for organizing related parameters, `mutex` constraints for mutually exclusive parameter combinations, and `suggested-resources` for specifying computational requirements like CPU cores, memory, and GPU requirements.

## Relationship to TVB and Other Tools

Boutiques maintains close relationships with several major neuroimaging and computational neuroscience platforms. The Human Connectome Project (HCP) pipelines were among the first large-scale datasets to adopt Boutiques descriptors for their preprocessing workflows, enabling standardized execution of the HCP's sophisticated image processing pipelines. Similarly, tools from the NiPy ecosystem (which includes nipype and related processing tools), as well as the nilearn library for statistical learning on neuroimaging data, have been described using the Boutiques schema.

For The Virtual Brain (TVB), Boutiques provides a standardization pathway that could enable TVB simulations to be incorporated into larger neuroimaging pipelines with standardized input-output handling. The relationship is bidirectional: TVB's sophisticated whole-brain modeling capabilities could be described as Boutiques tools, while Boutiques-enabled workflow systems could invoke TVB simulations as part of automated parameter sweeps or validation studies. More broadly, Boutiques complements other standardization efforts in the field, including NeuroML for neural model specification and BIDS for neuroimaging data organization, forming a comprehensive stack for reproducible computational neuroscience.

## Key Features

The Boutiques system offers several features that distinguish it from alternative tool description frameworks. First, the **Boutiques Application Publishing System (BApps)** provides a web-based platform where researchers can publish their tool descriptors, making them discoverable to the community through searchable catalogs. Second, the **Boutiques Invocat** tool enables direct execution of Boutiques-described tools locally or on cloud infrastructure, automatically handling container provisioning and parameter validation. Third, the schema supports **tool versioning** through the `tool-version` field, enabling researchers to track how tool specifications evolve over time and maintain reproducibility through explicit version pinning.

The descriptor format also includes a **validation framework** that checks descriptors for correctness before publication, ensuring that published tools meet community standards for completeness and correctness. Integration with the Brain Imaging Data Structure (BIDS) means that Boutiques tools can be designed to operate directly on BIDS-organized datasets, reducing the data preparation burden for researchers and enabling streamlined preprocessing workflows. Additionally, Boutiques supports **parameter sweeps** through the `exec-phys` field, which can invoke tools repeatedly with different parameter values, facilitating automated sensitivity analyses and parameter optimization studies common in computational neuroscience research.

## Related Software

Boutiques exists within a broader ecosystem of neuroscience software standardization tools. It complements PyNEST and NEURON by providing a description layer above these simulators, enabling standardized invocation of simulations built with these tools. The framework intersects with CIVET and related preprocessing pipelines by enabling standardized execution of cortical reconstruction workflows. Researchers using MATLAB-based tools can benefit from Boutiques containerization to distribute complex dependency stacks, while the JSON-based schema integrates naturally with Python-centric tools like Dipy and MNE-Python.

## External Resources

- Official Boutiques documentation: https://boutiques.github.io/
- BApps tool registry: https://app.boutiquesandbox.org/
- Boutiques GitHub repository: https://github.com/boutiques/boutiques