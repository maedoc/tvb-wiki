---
title: COINS
created: 2024-01-15
updated: 2026-05-04
type: entity
tags: [software-brain-modeling, database-neuroinformatics, neuroimaging, data-sharing, hipaa-compliant, multi-site-studies]
sources: [raw/papers/scott-2011.md, raw/articles/coins-website.md]
---

# COINS

## Overview

COINS (Collaborative Informatics and Neuroimaging Suite) is a comprehensive, web-based data management platform developed at the Mind Research Network (MRN) in Albuquerque, New Mexico. Designed to address the growing challenges of neuroimaging data storage, retrieval, and sharing, COINS provides an end-to-end solution for managing large-scale, heterogeneous neuroscience research data across multiple institutions. The system integrates study management, neuroimaging data acquisition, neuropsychological assessment collection, radiology review workflows, and secure data sharing capabilities into a unified HIPAA-compliant architecture. COINS represents one of the earliest large-scale institutional implementations of a neuroinformatics repository, predating many contemporary data sharing initiatives and serving as a model for multi-site collaborative research infrastructure.

The platform emerged from the recognition that as neuroimaging research expanded in scope—incorporating multiple imaging modalities, longitudinal assessments, and multi-site collaborations—researchers required sophisticated but accessible tools to manage the exponential growth in data volume and complexity. Traditional approaches using disconnected databases and manual workflows proved inadequate for modern multi-center studies. COINS was designed to fill this gap by providing a unified system that could handle the complete data lifecycle from participant enrollment through data analysis and sharing.

## Key Features

### Data Acquisition and Management

COINS employs an automated DICOM receiver that collects and archives MR imaging data directly from scanners, requiring no manual intervention. The system performs automated integrity checks to ensure that inaccurate or incomplete data are not stored; problematic scans are routed to a temporary location until resolution. This automated pipeline significantly reduces the administrative burden on research staff while improving data quality through real-time validation against participant enrollment records.

The Assessment Manager (ASMT) component provides web-based tools for collecting neuropsychological and clinical assessment data. COINS implements a dual-entry system for data collected on paper, wherein twoindependent data entry operators input the same form, and the system automatically identifies and resolves discrepancies. This approach dramatically reduces data entry errors and ensures high data quality for downstream analyses. The system also supports offline data entry through a browser cache, enabling data collection in environments with unreliable internet connectivity—a critical feature for research conducted in community settings or developing regions.

### Study and Participant Tracking

COINS provides flexible study management tools that accommodate the diverse organizational structures of neuroscience research. Each study can define custom participant types (e.g., control, patient, screened failure), track enrollment against IRB-approved targets, and manage visit schedules across multiple sessions. The system integrates IRB compliance management, automatically notifying principal investigators when study approvals approach expiration and preventing enrollment in expired studies. This feature has proven essential for maintaining regulatory compliance across large, long-duration investigations.

The participant management system includes sophisticated repeat-subject identification capabilities. When a new participant enters the system, COINS performs fuzzy matching on name and address to identify potential duplicates while maintaining privacy controls. This enables longitudinal tracking of participants across multiple studies without compromising confidentiality, supporting richer metadata about individual developmental trajectories or disease progressions.

### Security and Privacy

As a platform handling human subjects research data, COINS implements comprehensive security features compliant with HIPAA regulations. The system separates personally identifiable information (PII) from research data, enabling granular access controls that can be configured at the study level. COINS supports PHI unlinking—a critical capability for studies approaching completion—allowing researchers to sever the connection between participant identifiers and their research data while preserving the anonymized assessment and imaging data for continued analysis and sharing.

Access controls are role-based, with different permission levels for principal investigators, research coordinators, radiologists, and external collaborators. Audit trails track all data access and modifications, providing accountability and supporting regulatory compliance. The platform also includes automated data quality control checks that flag potential issues such as missing required fields, out-of-range values, or inconsistent imaging metadata.

### Data Sharing Infrastructure

COINS includes a robust data exchange framework that facilitates secure sharing of de-identified data among investigators. The "click-to-share" interface allows researchers to rapidly share datasets with collaborators at other institutions, either through direct data transfer or through a mediated access model where collaborators request access to shared resources. The system has hosted several prominent multi-site datasets, including the Autism Brain Imaging Data Exchange (ABIDE) comprising over 1,000 datasets from 15 sites, and the Consortium for Reliability and Reproducibility (CoRR), which has become a benchmark dataset for assessing neuroimaging reliability.

## Relationship to TVB

COINS relates to [[the-virtual-brain]] primarily through its role in generating and managing the neuroimaging data that feed whole-brain connectome models. TVB requires structural and functional connectivity data—typically derived from [[diffusion-imaging]] (DTI) and resting-state [[fmri]] scans—as primary inputs for simulation. COINS, as a data management platform, can store and organize exactly these imaging modalities, along with the parcellation schemes and phenotypic information needed to configure TVB simulations.

The structural connectivity matrices used in TVB modeling are commonly derived from [[dti]] tractography pipelines, and the quality of these matrices depends critically on the acquisition and preprocessing of the raw diffusion data. COINS' DICOM receiver and quality control workflows help ensure that diffusion imaging data maintain the integrity needed for tractography. For functional connectivity, COINS supports the storage and management of [[fmri]] time series that can be used to derive seed-based or data-driven connectivity patterns, informing TVB's functional connectivity constraints.

Furthermore, COINS' multi-site data sharing capabilities position it as infrastructure that could aggregate the large datasets needed for population-level TVB modeling. As personalized brain modeling increasingly requires large samples to parameterize and validate models, platforms like COINS that enable data pooling across institutions become valuable. The phenotypic and clinical assessment data managed by COINS—including cognitive measures, clinical ratings, and demographic information—are precisely the covariates needed to stratify patient populations for TVB modeling applications in conditions such as [[epilepsy-modeling]] or [[schizophrenia-models]].

## Key Papers

The seminal publication describing COINS appeared in Frontiers in Neuroinformatics: Scott et al. (2011) "COINS: An Innovative Informatics and Neuroimaging Tool Suite Built for Large Heterogeneous Datasets." This paper detailed the system architecture, compared functionality with the widely-used [[xnat]] platform, and discussed the challenges of multi-site data sharing in neuroimaging. The authors emphasized COINS' approach to integrating heterogeneous data types—including MRI, [[meg]], and [[eeg]] imaging alongside clinical assessments—as a distinguishing feature.

The system was subsequently used to demonstrate data sharing at scale through initiatives including SchizConnect, a large-scale schizophrenia neuroimaging data mediation project, and theABIDE dataset. These collaborations established COINS as a viable infrastructure for psychiatric neuroimaging consortia, demonstrating its capacity to support the complex metadata requirements and data governance models characteristic of multi-site clinical studies.

## Scale and Adoption

As of the most recent documentation, COINS manages over 71,000 participants across 970 studies, with more than 78,000 scan sessions and 2 million clinical assessments in its repositories. The system has been deployed at multiple research institutions including the Mind Research Network, the Nathan Kline Institute, University of Colorado Boulder, and the Olin Neuropsychiatry Research Center. This broad adoption demonstrates the platform's ability to scale from single-lab studies to enterprise-level multi-site initiatives while maintaining usability for diverse user populations.