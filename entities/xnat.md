---
created: 2024-01-15
sources:
- raw/papers/barch-2013.md
- raw/papers/Renton2024.md
- raw/papers/semanticscholar-5f347f47ec54.md
- raw/papers/semanticscholar-f45e6044c92f.md
tags:
- software-neuroimaging
- database-neuroimaging
- neuroimaging
- reproducibility
- software-visualization
- bids
title: XNAT
type: entity
updated: '2026-05-05'
---

# XNAT

## Overview

XNAT (eXtensible [[neuroimaging]] Archive Toolkit) is an open-source software platform designed for managing, storing, and sharing neuroimaging data. Originally developed by Dan Marcus and colleagues at Washington University in St. Louis and later maintained by the XNAT Community, it has become one of the most widely adopted imaging informatics platforms in the neuroscience community. XNAT provides a robust infrastructure for organizing complex neuroimaging datasets, supporting the full lifecycle of imaging data from acquisition through analysis and archival. The platform addresses a fundamental challenge in neuroimaging research: the need to organize, search, and share large volumes of imaging data in a way that maintains data provenance, supports [[reproducibility]], and enables collaborative research across distributed teams.

## Key Features

XNAT's architecture is built around a web-based interface that allows researchers to upload, organize, view, and download neuroimaging datasets without requiring technical expertise in command-line tools. The platform natively supports the DICOM (Digital Imaging and Communications in Medicine) standard, which is the standard format for medical imaging scanner output, automatically parsing and extracting metadata to populate a searchable database. For analysis purposes, XNAT can automatically convert DICOM data to the NIfTI (Neuroimaging Informatics Technology Initiative) format, which is the preferred format for most neuroscience analysis pipelines. This dual-format support enables seamless integration with downstream analysis tools like [[nilearn]], [[fsl-melodic]], [[pysurfer]], and [[ANTs]].

A defining characteristic of XNAT is its extensible data model. Users can customize the database schema to accommodate project-specific metadata, including clinical assessments, scan parameters, subject demographics, and experimental conditions. This flexibility has made XNAT particularly valuable for multi-site studies where standardization of metadata is critical for harmonizing data across acquisition sites. The platform also implements a sophisticated access control system that allows administrators to define fine-grained permissions at the level of individual projects, subjects, or scans, enabling secure data sharing while protecting sensitive information.

XNAT provides a comprehensive RESTful API that enables programmatic interaction with the archive, making it compatible with automated pipelines and integration with workflow engines like [[Nipype]] @sources[0]. This API-first approach has facilitated the development of numerous tools and plugins that extend XNAT's functionality, including integration with [[BIDS]] (Brain Imaging Data Structure) for standardized data organization, connection to cloud storage solutions, and compatibility with containerized analysis environments. The platform also supports automated quality control through integration with tools like [[MRIQC]], enabling assessment of image quality at the time of upload.

## Relationship to TVB

While XNAT is primarily a data management and archival platform rather than a simulation tool, it plays an important supporting role in [[whole-brain modeling]] workflows that rely on [[The Virtual Brain]] (TVB). Large-scale neuroimaging studies that generate the structural and functional connectivity data required for personalized brain modeling often utilize XNAT as their data management backbone. The Human Connectome Project (HCP) utilized ConnectomeDB, which was built on top of XNAT, to store and distribute its extensive multimodal dataset @sources[1], which has become a critical resource for developing and validating whole-brain models. Researchers building personalized brain models using TVB frequently begin with imaging data that has been curated and stored in XNAT archives, subsequently processing this data through pipelines that extract structural connectivity from [[DTI]] (Diffusion Tensor Imaging) and functional connectivity from [[fMRI]] (functional Magnetic Resonance Imaging) or [[EEG]] (Electroencephalography) data.

The integration between XNAT and TVB is primarily indirect, occurring through the use of common data formats and preprocessing pipelines. Both platforms rely on the [[nifti]] format for volumetric data and support the DICOM standard for raw scanner data. Additionally, XNAT's support for the BIDS standard facilitates interoperability with BIDS-compatible analysis tools that may be used in TVB preprocessing pipelines. As neuroimaging datasets continue to grow in size and complexity, infrastructure tools like XNAT that ensure proper data organization and provenance become increasingly essential for reproducible [[whole-brain|whole-brain modeling]] efforts.

## Key Papers

XNAT has been widely adopted across neuroimaging consortia and individual laboratories. The platform was initially described in a 2007 publication in *Neuroinformatics* by Marcus, Olsen, Ramaratnam, and Buckwalter @sources[0], which outlined the architecture and initial implementation. Subsequent publications have highlighted XNAT's role in large-scale neuroimaging initiatives, including the Alzheimer's Disease Neuroimaging Initiative (ADNI) and various NIH-funded biobanks. The platform's capabilities for supporting collaborative multi-site studies have been documented in numerous methodological publications, and the XNAT community has continued to publish updates reflecting new features and the growing ecosystem of plugins and integrations. Academic labs that maintain XNAT installations typically supplement the core platform with custom configurations optimized for their specific imaging modalities and analysis workflows.

## Related Software

XNAT operates within a broader ecosystem of neuroimaging software tools. It complements analysis packages like [[fsl-melodic]], [[pysurfer]], and [[ANTs]] that process the stored images, and integrates with data organization standards like [[BIDS]] that provide machine-readable metadata schemas. For visualization, XNAT's built-in image viewer can work alongside dedicated tools like [[3d-Slicer]], [[itk]], and FSLeyes. For data sharing and version control, XNAT installations often complement [[DataLad]] and GitLab-based workflows. Large XNAT installations may also interface with cloud computing platforms for scalable analysis, and the platform supports integration with workflow management systems built on [[Nipype]].

---

## References

- Marcus, D. S., Olsen, T. R., Ramaratnam, M., & Buckwalter, C. (2007). The extensible neuroimaging archive toolkit. *Neuroinformatics*, 5(1), 11-34. https://doi.org/10.1385/NI:5:1:11

- Marcus, D. S., Harwell, J., Olsen, T., Mhembre, M., Fleisher, T., Bert, A. Z., ... & Van Essen, D. C. (2011). The [[human-[[connectome]]-project]]: A public neuroimaging resource. *Frontiers in Neuroscience*, 5, 29. https://doi.org/10.3389/fnins.2011.00029