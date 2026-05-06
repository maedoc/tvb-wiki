---
created: 2024-01-15
sources:
- das2011
- bids2016
- mcgill-loris-web
- hcp-database
- raw/papers/huntenburg-2018.md
- raw/papers/sanz-leon-2013.md
- raw/papers/Renton2024.md
tags:
- software-bids
- database-hcp
- data-management
- neuroimaging
- software
title: LORIS
type: entity
updated: '2026-05-06'
---

LORIS (Longitudinal Online Research Infrastructure System) is a free, open-source web-based data management platform designed specifically for large-scale, multi-site [[neuroimaging]] and behavioral research studies. Originally developed at the Montreal Neurological Institute and Hospital (McGill University) [@das2011], LORIS provides an integrated solution for organizing, storing, validating, and distributing complex neuroimaging datasets collected over extended time periods. The system manages the complete lifecycle of research data from the moment it is acquired at scanner sites through processing, quality control, analysis, and eventual sharing with the broader scientific community.

## Motivation and Context

The explosive growth of large neuroimaging consortia—such as the [[human-[[connectome]]-project]] (HCP), the [[uk-biobank]], and the Adolescent Brain Cognitive Development (ABCD) study—created an acute need for infrastructure capable of handling petabytes of imaging data alongside correspondingly vast behavioral, genetic, and clinical datasets. Traditional approaches of storing data on hard drives and managing metadata in spreadsheets simply did not scale to studies involving tens of thousands of participants scanned multiple times across dozens of sites. LORIS emerged to address this challenge by providing a centralized, secure repository with built-in tools for data validation and quality assurance, automated metadata extraction from DICOM headers, role-based access control for multi-site collaborations, and seamless integration with popular neuroimaging analysis pipelines.

The platform proved particularly influential in standardizing data management practices in the neuroimaging community. By enforcing consistent naming conventions, tracking data provenance through every stage of processing, and providing searchable databases of acquisition parameters and participant phenotypes, LORIS helped establish best practices that later influenced the development of the [[bids]] (Brain Imaging Data Structure) specification [@bids2016]. Today, the system continues to serve as the backbone data repository for numerous major neuroimaging initiatives worldwide.

## Technical Architecture

LORIS is built on a modular architecture combining a MySQL database backend, PHP-based server-side logic, and a JavaScript-rich front-end interface. The database schema organizes data around several core entities: imaging datasets (organized by candidate, session, and scan type), behavioral instruments (questionnaires, cognitive tests, clinical ratings), and processing pipelines (automated workflows that transform raw DICOM files into analysis-ready [[nifti]] volumes). Each entity maintains rigorous metadata including acquisition hardware, sequence parameters, processing software versions, and quality control ratings—information essential for [[reproducibility]] and for accounting for batch effects in multi-site analyses.

The system exposes a RESTful API that enables programmatic interaction with the database, allowing external tools to query for specific datasets, upload new acquisitions, or retrieve processed outputs. This API underlies integrations with Python libraries such as [[pybids]] and frameworks like [[nipype]] that orchestrate complex neuroimaging workflows. LORIS also implements the BIDS validator, ensuring that any data exported from the system conforms to the BIDS specification—a critical feature for facilitating data sharing and enabling reproducible analysis across laboratories.

A central strength of LORIS lies in its support for longitudinal study designs, which are pervasive in developmental neuroscience, [[aging]] research, and clinical trials. The system tracks participants across multiple imaging sessions, automatically linking behavioral assessments to the corresponding brain scans and maintaining the temporal context essential for analyzing disease progression or [[developmental-trajectories]]. Integrated versioning allows researchers to track how their datasets evolve as processing pipelines are updated or quality control decisions are revised.

## Relationship to TVB

While LORIS is fundamentally a data management infrastructure rather than a simulation or analysis tool, it plays an important supporting role in [[whole-brain-modeling]] workflows that rely on high-quality, well-curated neuroimaging datasets. Projects using [[the-virtual-brain]] to construct [[personalized-brain-modeling|personalized brain]] models require [[structural-connectivity]] matrices derived from diffusion imaging data, along with corresponding anatomical parcellations and functional timeseries. These datasets often originate from large-scale studies that use LORIS as their primary repository.

The integration between LORIS and TVB typically proceeds in one of two ways. First, researchers may export preprocessed connectivity data directly from a LORIS instance—either through the web interface or programmatically via the API—as input for TVB's connectivity simulator. Second, investigators conducting longitudinal studies can leverage LORIS's temporal tracking capabilities to manage the multiple imaging sessions required for estimating time-varying connectivity patterns that inform personalized models of brain dynamics. The system's ability to maintain provenance metadata also helps ensure that the structural connectomes used in TVB simulations are derived from explicitly documented processing pipelines, facilitating reproducibility and rigorous model validation.

## Key Features

LORIS offers a comprehensive suite of features tailored to the unique demands of neuroimaging research. The platform provides automated data ingestion from DICOM files, with intelligent parsing of headers to populate metadata fields without manual entry. Built-in quality control workflows allow imaging scientists to review scans, flag artifacts, and document issues directly within the interface, creating a complete audit trail of data quality decisions. The instrument builder enables researchers to deploy custom behavioral assessments alongside standardized clinical batteries, while the imaging browser provides visualization tools for inspecting raw and processed volumes.

The permission system supports granular role-based access controls essential for multi-site consortia, enabling different institutions to maintain ownership of their own data while sharing selected datasets with collaborators. Imaging series can be flagged for specific processing pipelines—automatic execution of preprocessing steps frees researchers from manual file handling. Finally, LORIS supports data exports in multiple formats, including raw DICOM, [[bids]]-compliant directory structures, and custom tabular formats suitable for statistical analysis.

## Key Papers

- **Das et al. (2011)**: "LORIS: a web-based data management, archiving and sharing system" — The original publication describing the LORIS system architecture and core functionality.
- **Das et al. (2016)**: "The Longitudinal Online Research Infrastructure System (LORIS)" (NeuroImage) — An updated description of LORIS features and its role in large-scale neuroimaging consortia.

## See Also

- [[TVB]] — The Virtual Brain simulation platform
- [[bids]] — Brain Imaging Data Structure specification
- [[human-connectome-project]] — HCP database and infrastructure
- [[nipype]] — Neuroimaging analysis pipeline framework

## Related Software

LORIS interacts with a rich ecosystem of neuroimaging tools. The [[human-connectome-project]] and its associated [[database-hcp]] rely on LORIS for data hosting. For analysis, researchers often pair LORIS with [[nilearn]] for statistical modeling and visualization, [[dipy]] for diffusion data processing, and [[mrtrix3-connectome]] for advanced connectivity reconstruction. Data exported from LORIS can be processed using [[freesurfer]] for cortical reconstruction or [[fsl]] for general-purpose neuroimaging analysis. The integration with [[datalad]] enables version-controlled data distribution, while [[connectome-workbench]] provides visualization tools for viewing processed neuroimaging results.

---

**References**

[@bids2016]: Gorgolewski et al. (2016). "The Brain Imaging Data Structure (BIDS): Towards a standardized tool for organizing neuroimaging data." *NeuroImage*, 124, 1064-1073.

[@das2011]: Das et al. (2011). "LORIS: a web-based data management, archiving and sharing system." *Frontiers in Neuroinformatics*. Conference abstract.

[@hcp-database]: Human Connectome Project. LORIS database documentation. https://www.humanconnectome.org/

[@mcgill-loris-web]: LORIS Official Website. Montreal Neurological Institute. https://loris.ca/