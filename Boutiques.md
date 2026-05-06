---
title: Boutiques
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-boutiques, software-bids, software-neurodesk, reproducibility, database-neuroscience-gateway, database-nitrc, database-nitrc-ce, software-tool-descriptors]
sources: ["arXiv:1711.09713", "GigaScience 2018:giy016", "Frontiers Neuroinformatics 2014:CBRAIN", "PLoS Computational Biology 2017:BIDS-apps"]
---

# Boutiques

## Overview

Boutiques is a software framework for describing, packaging, and executing computational neuroscience tools in a standardized, portable, and reproducible manner. Developed primarily at the [[mcGill-university|McGill]] [[montreal-neurological-institute|Neurological Institute]], Boutiques provides a JSON-based descriptor format that captures the command-line interface, input parameters, output files, and computational requirements of neuroscience software tools. The framework enables researchers to invoke tools consistently across different computing environments—whether on local workstations, high-performance clusters, or cloud infrastructure—thereby addressing a fundamental challenge in computational neuroscience: the difficulty of sharing, installing, and reproducing complex neuroimaging pipelines. Boutiques can be considered a domain-specific alternative to broader workflow languages like the Common Workflow Language (CWL) or Workflow Definition Language (WDL), tailored specifically to the needs of the neuroscience community [1].

## Motivation and Context

The computational neuroscience landscape faces a significant reproducibility challenge. Neuroimaging pipelines often involve dozens of software tools, each with its own installation procedures, dependency requirements, parameter conventions, and output formats. A researcher who develops a pipeline on one system frequently encounters difficulties when attempting to run the same pipeline on a different machine or share it with collaborators. Traditional approaches to this problem involved writing comprehensive README files or creating Docker/Singularity containers, but these solutions lack a machine-readable description of tool interfaces [1].

Boutiques emerged from the [[neuroinformatics]] community's need for a standardized way to describe neuroimaging tools. The framework was developed as part of broader efforts to improve reproducibility in neuroscience, complementing initiatives like the [[bids|Brain Imaging Data Structure]] format for data organization and [[datalad]] for data version control. By providing a formal specification for tool descriptors, Boutiques enables automated tool invocation, input validation, and pipeline construction—capabilities that are essential for large-scale [[reproducibility]] studies and collaborative research workflows.

## Technical Specification

A Boutiques descriptor is a JSON Schema-formatted file that captures the complete interface of a command-line tool. The descriptor specifies several key components: the tool's name, version, and description; the list of input parameters with their types, default values, and validation constraints; the list of output files and directories; the command template that specifies how inputs are assembled into the final command line; and optional containerization hints specifying Docker or Singularity image identifiers [1].

The descriptor format supports parameter grouping, dependencies between parameters, and conditional execution paths. For example, a neuroimaging tool might have a parameter group for preprocessing options that only applies when a certain flag is set, or dependencies that require one parameter to be specified before another becomes valid. The Boutiques SDK provides Python utilities for validating descriptors, generating command lines from parameter sets, and invoking tools directly from Python code.

## Key Features

Boutiques descriptors enable several powerful capabilities that serve the reproducibility goals of the neuroscience community. First, the framework provides automatic input validation—before executing a tool, Boutiques verifies that all required parameters are present and conform to their specified types and constraints, catching configuration errors early. Second, descriptors support container invocation seamlessly: a Boutiques descriptor can specify a Docker or Singularity container image, and the framework will automatically pull the image and execute the tool within the container environment, eliminating "it works on my machine" problems [1].

Third, Boutiques integrates with the [[neurodesk]] ecosystem and various [[neuroimaging]] platforms to enable one-click tool invocation from web interfaces. The [[cbrain]] platform, for instance, uses Boutiques descriptors to present users with standardized configuration GUIs for neuroimaging tools [3]. Fourth, the framework supports tool caching and provenance tracking, recording which tool version was executed with which parameters, which is essential for scientific reproducibility. Finally, the Boutiques Zenodo repository hosts a growing collection of community-contributed descriptors for popular neuroscience tools, creating a discoverable registry of standardized tool interfaces.

## Relationship to TVB

Boutiques is relevant to [[the-virtual-brain]] (TVB) in several ways. TVB is a large-scale brain modeling platform that incorporates numerous preprocessing and analysis tools for neuroimaging data, including tools for handling [[structural-connectivity]] data from [[diffusion-imaging]] tractography, [[functional-connectivity]] analysis from [[fmri]] or [[eeg]] data, and various brain parcellation schemes. Packaging TVB's many components and dependencies through Boutiques descriptors would enable more reproducible execution of TVB pipelines and facilitate integration with the broader neuroimaging workflow ecosystem [1].

Additionally, the parameter estimation and optimization routines used in TVB simulations often invoke external tools for connectivity matrix processing or signal analysis. Boutiques descriptors could provide standardized interfaces for these external components, enabling automated pipeline construction and cross-platform execution. The relationship between TVB and Boutiques thus represents an opportunity to enhance the accessibility and reproducibility of whole-brain modeling workflows.

## Key Papers

The original Boutiques framework was described by Glatard et al. (2017) in a preprint that was later published in GigaScience [1][2]. This paper introduced the JSON-based descriptor format, the Boutiques SDK, and documented the framework's integration with several neuroimaging platforms including CBRAIN and VIP. The authors demonstrated Boutiques' utility by describing dozens of neuroinformatics applications and showed how the framework enables automated application integration across computational platforms.

A subsequent paper detailed the integration of Boutiques with the CBRAIN platform, demonstrating how Boutiques descriptors can be used to generate standardized web interfaces for neuroimaging tools and enable parallel execution of complex workflows [3]. This work highlighted how Boutiques addresses the reproducibility challenge in large-scale neuroimaging studies by providing formal, machine-readable descriptions of tool interfaces.

The Boutiques framework has also been discussed in the context of related initiatives. The BIDS Apps paper (Gorgolewski et al., 2017) mentions Boutiques as a complementary framework for tool description and notes that BIDS Apps can be imported into Boutiques descriptors using the `bosh` importer [4]. This interoperability demonstrates how Boutiques serves as a foundational layer for the broader neuroinformatics tool ecosystem.

## Related Software

Boutiques occupies a niche in the neuroinformatics tooling landscape that intersects with several related projects. The [[bids]] specification provides a complementary role—while Boutiques describes software tool interfaces, BIDS standardizes the format and organization of neuroimaging data files, and the two can work together in comprehensive pipelines [4]. [[datalad]] and [[datalad-containers]] provide version-controlled data management with container integration, paralleling Boutiques' container support. The [[nipype]] framework offers workflow composition capabilities that could leverage Boutiques descriptors for tool invocation. Platforms like [[cbrain]] and [[neurodesk]] use Boutiques to provide web-based interfaces for tool execution, making complex neuroimaging software accessible through browser-based interfaces without requiring local installation.

## References

[1] Glatard T, Kiar G, Aumentado-Armstrong T, et al. (2017). Boutiques: a flexible framework for automated application integration in computing platforms. arXiv preprint arXiv:1711.09713.

[2] Glatard T, Kiar G, Aumentado-Armstrong T, et al. (2018). Boutiques: a flexible framework to integrate command-line applications in computing platforms. GigaScience, 7(5):giy016. doi:10.1093/gigascience/giy016

[3] Sherif T, Rioux P, Rousseau ME, et al. (2014). CBRAIN: a web-based, distributed computing platform for collaborative neuroimaging research. Frontiers in Neuroinformatics, 8:54.

[4] Gorgolewski KJ, Alfaro-Almagro F, Auer T, et al. (2017). BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods. PLoS Computational Biology, 13(3):e1005209.