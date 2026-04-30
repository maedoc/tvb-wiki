---
title: NIDM-Results
created: 2024-01-15
updated: 2026-04-30
type: entity
tags: [neuroimaging, neuroimaging-fmri, data-standard, software-spm, software-fsl, reproducibility, nidm, neuroimaging-eeg, neuroimaging-meg]
sources: [nidm-wg, prov-ontology, nidm-jsonld, spm-nidm, fsl-nidm]
---

## Overview

NIDM-Results (Neuroimaging Data Model - Results) is a specification that provides a standardized, machine-readable format for representing statistical results from neuroimaging analysis pipelines. It is part of the broader NIDM family of specifications developed to improve data interoperability in neuroscience by defining semantic vocabularies and data structures for neuroimaging experiments. NIDM-Results specifically focuses on encoding the outputs of statistical analysis workflows—including statistical parametric maps, contrast estimates, design matrices, error estimates, and associated metadata—in a way that preserves provenance and enables reproducible science. The specification emerged from the Neuroimaging Data Model (NIDM) working group, which aimed to address the fragmentation of data formats across different neuroimaging software packages like [[SPM]] (Statistical Parametric Mapping), [[FSL]], and other analysis tools. [nidm-wg]

## Motivation and Context

The neuroimaging field has long suffered from format heterogeneity, with each software package using different file format conventions for storing analysis results. For example, [[SPM]] uses NIfTI images with embedded headers, [[FSL]] uses its own conventions, and custom analysis pipelines often generate yet different formats. This heterogeneity makes it extremely difficult to combine results across studies, perform meta-analyses, or even reproduce another lab's analysis pipeline from published results. Researchers often spend considerable time reverse-engineering file formats or writing custom parsers, diverting effort from actual scientific inquiry.

NIDM-Results addresses this problem by providing a unified framework for representing statistical results that preserves both the data values and the computational provenance—the exact sequence of operations that produced each result. By encoding results in NIDM-Results format, researchers can immediately understand not just what the statistical maps show, but how they were generated, what contrast was tested, what preprocessing was applied, and what software version was used. This provenance information is critical for reproducibility and for the emerging field of large-scale neuroimaging meta-analyses, where standardized result representations enable automated aggregation across hundreds of studies.

## Technical Specification

NIDM-Results is structured around a core set of entities that represent the key components of a statistical neuroimaging analysis. The central entity is the **Statistic Map**, which represents a spatially-organized image of statistical values (e.g., t-statistics, F-statistics, or Z-scores) along with metadata specifying what kind of statistic it represents and what the degrees of freedom are. Each statistic map is linked to a **Contrast**, which specifies the linear combination of parameter estimates that was tested—for instance, a difference between two conditions or an effect of a covariate.

The specification captures the full **Design Matrix** that specifies the regression model used in the analysis, including which regressors correspond to experimental conditions, confounds, or nuisance variables. Each column of the design matrix is labeled with a meaningful name (e.g., "stimulus_A", "response_time"), enabling downstream users to understand exactly what each regressor represents. The specification also supports encoding **Error Model** information, including whether spatial autocorrelation was modeled and what assumptions were made about the noise structure.

A key feature of NIDM-Results is its use of **provenance tracking**: the specification builds on the W3C PROV ontology to explicitly represent the data transformation pipeline. Each result entity carries information about what input data was used, what processing steps were applied, and what software produced the output. This allows any consumer of NIDM-Results data to reconstruct the computational history of each result, greatly facilitating both reproducibility checks and automated pipeline comparison. [prov-ontology]

The NIDM-Results specification is serialized using JSON-LD (JavaScript Object Notation for Linked Data), which combines the readability of JSON with the semantic richness of the Resource Description Framework (RDF). This allows NIDM-Results documents to be parsed both by humans (as readable JSON) and by machines (as RDF with formal semantics), enabling automated reasoning and integration with other linked data resources in the neuroimaging ecosystem. [nidm-jsonld]

## Key Features

One of the primary features of NIDM-Results is its **software interoperability**. By providing a common specification adopted by multiple analysis packages, NIDM-Results enables results generated in one software environment to be understood and used in another. Several major neuroimaging tools have implemented NIDM-Results export functionality, including [[SPM]] (via its NIFTI extensions), [[FSL]] (via fslmaths utilities), and [[AFNI]]. This means researchers are not locked into a single software ecosystem for their analyses. [spm-nidm] [fsl-nidm]

Another important feature is **semantic Annotation**. Unlike raw image formats that store only numerical voxel values, NIDM-Results enriches results with human-readable and machine-interpretable labels. Every statistic map, contrast, and regressor carries a unique identifier and descriptive metadata that can be queried programmatically. This supports the development of neuroimaging databases and discovery tools that can automatically categorize and retrieve results based on their experimental contents.

The specification also provides explicit support for **family-wise error (FWE) correction** and multiple comparison correction information. Rather than only providing raw p-value maps, NIDM-Results can encode which correction methods were applied (e.g., Bonferroni, FDR, cluster-wise correction using random field theory) and what thresholds were used, enabling proper statistical interpretation of results.

Additionally, NIDM-Results facilitates **result sharing and reuse** across laboratories by providing a well-documented, vendor-neutral format. Researchers can archive their analysis outputs in NIDM-Results format and share them alongside publications, enabling other groups to build upon existing results without needing access to the original raw data or analysis pipelines.

## Key Papers

The NIDM specifications were developed through an open collaborative process involving the neuroimaging community. The original NIDM-Results specification was published as part of the efforts by the NIDM working group, with key contributions from researchers at INRIA and the University of Oxford. Notable publications include the NIDM-Results specification papers describing the PROV-based provenance model and JSON-LD serialization format. The adoption of NIDM-Results by major software packages like [[SPM]] and [[FSL]] has been documented in the software release notes and associated technical publications.

## Relationship to TVB and Whole-Brain Modeling

While NIDM-Results was primarily developed for traditional mass-univariate analysis workflows common in fMRI research, it has relevance for whole-brain modeling efforts including The Virtual Brain (TVB). In TVB and similar large-scale modeling frameworks, researchers often compare model-generated dynamics to empirical functional connectivity patterns derived from fMRI or other neuroimaging data. NIDM-Results can provide a standardized way to represent these comparison statistics—showing where model predictions match or diverge from empirical observations, what parameter variations produce the best fit, and what regions show significant differences between modeled and observed activity.

Furthermore, as the field moves toward personalized brain modeling where individual structural connectivity from diffusion imaging data informs model parameters, the provenance tracking capabilities of NIDM-Results become valuable for documenting exactly how each personalized model was constructed. This supports the broader goals of the personalized brain modeling literature, where reproducibility and methodological transparency are essential.

## Related Software and Standards

NIDM-Results should be understood in the context of the broader neuroimaging data ecosystem. It complements **BIDS** (Brain Imaging Data Structure), which standardizes the organization of raw neuroimaging data, by providing a specification for analysis outputs. Tools like PyBIDS and Nilearn provide Python interfaces for working with both BIDS-organized data and NIDM-Results documents. The nibabel library provides low-level file I/O for neuroimaging formats and can be used alongside NIDM-Results parsers.

The NIDM family includes related specifications beyond NIDM-Results: **NIDM-Experiment** for representing raw neuroimaging time-series data, **NIDM-Probabilities** for representing probabilistic atlases and parcellations, and **NIDM-fMRI** for task-based fMRI experiment designs. Together, these specifications aim to provide end-to-end interoperability from raw data acquisition through statistical analysis and results publication.

## Open Questions and Limitations

Despite its utility, NIDM-Results adoption has been incremental rather than universal. Some analysis packages still lack native NIDM export capabilities, and many published results in the literature are not available in NIDM-Results format, limiting its usefulness for meta-analysis. Additionally, the JSON-LD serialization, while powerful, can be verbose compared to simple image formats, creating challenges for storage and bandwidth in large-scale studies.

An ongoing question is how to extend NIDM-Results to cover newer analysis paradigms beyond mass-univariate modeling—including multivariate pattern analysis (MVPA), representational similarity analysis (RSA), and the statistical outputs from dynamic causal modeling (DCM) analyses. As these analysis approaches become more common, the NIDM working group continues to develop extensions that can accommodate their specific result structures. The relationship between NIDM-Results and emerging standards like **ODR** (Open Data Repository) also remains an area of active development.

## References

[nidm-wg] Neuroimaging Data Model (NIDM) Working Group. NIDM-Results Specification. https://nidm.nidash.org/

[prov-ontology] W3C PROV Ontology Specification. https://www.w3.org/TR/prov-o/

[nidm-jsonld] NIDM Working Group. NIDM JSON-LD Context and Specification. https://nidm.nidash.org/spec/

[spm-nidm] SPM NIDM-Results Export. Statistical Parametric Mapping Software Documentation. https://www.fil.ion.ucl.ac.uk/spm/

[fsl-nidm] FSL NIDM-Results Export. Oxford University FMRIB Software Library Documentation. https://fsl.fmrib.ox.ac.uk/fsl/