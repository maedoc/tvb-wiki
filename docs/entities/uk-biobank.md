---
created: 2026-04-20
sources:
- raw/papers/miller-2016.md
- raw/papers/alfaro-almagro-2018.md
- raw/papers/elliott-2018.md
- raw/papers/smith-2021.md
- raw/papers/littlejohns-2020.md
tags:
- database-uk-biobank
- connectomics
- neuroimaging-fmri
- aging-brain
title: UK Biobank
type: entity
updated: '2026-05-19'
---

# UK Biobank

The UK Biobank Imaging Study is the largest brain imaging study ever conducted, designed to acquire multimodal [[neuroimaging-fmri|MRI]] from 100,000 existing UK Biobank participants and merge these scans with the project's extensive phenotypic and genetic data [[raw/papers/miller-2016.md|Miller et al. (2016)]]. The protocol captures [[neuroimaging-fmri|functional MRI]], [[diffusion-mri|diffusion MRI]], and structural scans, enabling population-level investigations of [[brain-network|brain structure]] and [[functional-connectivity|function]] that are impossible in smaller cohorts [[raw/papers/miller-2016.md|Miller et al. (2016)]]. By imaging a broad age range within a single standardized framework, the study creates an unprecedented resource for understanding how the [[aging-brain|brain changes across the lifespan]] at the population level [[raw/papers/miller-2016.md|Miller et al. (2016)]].

To manage this scale, dedicated processing pipelines were developed to automatically preprocess structural, functional, and diffusion data for the full 100,000-participant target, with extensive quality metrics and standardized procedures released alongside the raw images [[raw/papers/alfaro-almagro-2018.md|Alfaro-Almagro et al. (2018)]]. These pipelines established the processing standards for the world's largest brain imaging dataset and have enabled thousands of researchers to use the data reliably [[raw/papers/alfaro-almagro-2018.md|Alfaro-Almagro et al. (2018)]]. Integrating the resulting imaging phenotypes with genome-wide genotyping has already yielded the first large-scale genome-wide association studies of brain imaging traits, identifying novel genetic loci associated with [[structural-connectivity|brain structure]], [[white-matter|white matter integrity]], and [[resting-state|resting-state]] connectivity [[raw/papers/elliott-2018.md|Elliott et al. (2018)]]. This convergence of massive sample size, multimodal [[connectomics]], and genetic depth makes UK Biobank a cornerstone resource for population-level analyses of the [[aging-brain|aging brain]] and [[brain-dynamics|brain dynamics]] [[raw/papers/elliott-2018.md|Elliott et al. (2018)]].

## Overview

UK Biobank is a large-scale biomedical database and research resource containing genetic, health, and imaging data from 500,000 UK participants. The imaging study aims to scan 100,000 participants with multimodal MRI, making it the largest brain imaging study ever conducted.

## History

### Establishment (2006)
- Funded by UK Medical Research Council and Wellcome Trust
- Baseline data collection from 500,000 participants (2006-2010)
- Extensive questionnaire and health data

### Imaging Extension (2014)
- Brain and body MRI added to protocol
- Target: 100,000 participants
- First scans: 2014
- 100,000 milestone: 2020

## Imaging Protocol

### Modalities
- **Structural MRI**: T1, T2 FLAIR, susceptibility-weighted
- **[[neuroimaging-fmri|Functional MRI]]**: [[resting-state|Resting-state fMRI]]
- **[[diffusion-mri]]**: dMRI for [[white-matter]]
- **Body MRI**: Cardiac, abdominal

### Scanner Standardization
- Three identical Siemens Skyra 3T scanners
- Traveling head model for consistency
- Regular calibration and quality checks

### Additional Measures
- **Genetics**: Genome-wide genotyping
- **Health Records**: Linked NHS data
- **Lifestyle**: Questionnaires and physical measures
- **Cognitive Tests**: Brief assessment battery

## Data Processing

### Processing Pipelines
- Automated preprocessing for all modalities
- Standardized quality control procedures
- Public release of processed data
- Extensive documentation

### Quality Control
- Automated artifact detection
- Manual review of problematic scans
- QC metrics for all participants
- Exclusion criteria applied

## Scientific Impact

### Scale
- 100,000+ brain imaging datasets
- Combined with genetics and health data
- Enables unprecedented statistical power
- Population-level neuroscience

### Key Findings
- Brain [[aging]] trajectories across lifespan
- Genetic associations with brain structure
- Risk factors for brain health
- Normative brain templates

### Publications
- 1000+ publications using UK Biobank data
- Open to researchers worldwide
- Rapidly growing literature

## Data Access

### Application Process
- Free for health-related research
- Application via UK Biobank Access Portal
- Ethical approval required
- Data use agreement

### Available Data
- Raw and processed imaging
- Genetic data (imputed genotypes)
- Health outcomes (linked records)
- Lifestyle and cognitive measures

## Comparison with HCP

| Feature | UK Biobank | Human Connectome Project |
|---------|------------|-------------------------|
| **Sample Size** | 100,000+ | 1,200 |
| **Age Range** | 40-69 (imaging) | 22-35 (young adult) |
| **Resolution** | Standard clinical | Ultra-high resolution |
| **Genetics** | Genome-wide | Limited |
| **Health Data** | Extensive | Limited |
| **Focus** | Population health | Precision connectivity |

## Related Concepts
- [[uk-biobank|UK Biobank]] – High-resolution [[connectivity]] study
- population-[[neuroimaging]] – Large-scale imaging
- imaging-genetics – Genetic basis of brain structure
- [[aging-brain]] – Brain aging processes
- neuroimaging-[[fmri]] – Functional MRI
- [[connectomics]] – [[brain-network]] analysis
- big-data-neuroscience – Large-scale data resources

## Key People
[[karla-miller|Karla L. Miller]] leads the UK Biobank imaging study and served as first author of the foundational protocol paper that established the multimodal [[neuroimaging-fmri|MRI]] framework designed for 100,000 participants, integrating structural, functional, and diffusion data with the project's extensive phenotypic and genetic resources [[raw/papers/miller-2016.md|Miller et al. (2016)]]. Her leadership defined the scanner standardization, imaging modalities, and acquisition protocols that demonstrated population-scale [[population-neuroimaging]] could be conducted with sufficient rigor to support genetic and epidemiological analysis [[raw/papers/miller-2016.md|Miller et al. (2016)]]. [[fidel-alfaro-almagro|Fidel Alfaro-Almagro]] co-authored that protocol description and subsequently led the development of automated [[image-processing|processing]] and [[quality-control]] pipelines essential for managing data at this scale [[raw/papers/miller-2016.md|Miller et al. (2016)]][[raw/papers/alfaro-almagro-2018.md|Alfaro-Almagro et al. (2018)]].

[[fidel-alfaro-almagro|Fidel Alfaro-Almagro]] took the lead on the processing infrastructure as first author of the comprehensive pipeline paper, working with [[mark-jenkinson|Mark Jenkinson]] and others to create automated, standardized procedures for structural, functional, and diffusion data that underpinned the public release of processed data and QC metrics [[raw/papers/alfaro-almagro-2018.md|Alfaro-Almagro et al. (2018)]]. These pipelines established the practical foundation that allowed thousands of researchers to analyse UK Biobank imaging data with confidence, directly enabling the first large-scale [[imaging-genetics]] studies by producing reliable phenotypes suitable for [[gwas|genome-wide association analyses]] [[raw/papers/alfaro-almagro-2018.md|Alfaro-Almagro et al. (2018)]][[raw/papers/elliott-2018.md|Elliott et al. (2018)]]. [[lloyd-elliott|Lloyd T. Elliott]], as first author of the inaugural UK Biobank brain imaging GWAS, leveraged these processed data to identify genetic loci associated with [[structural-connectivity|brain structure]], [[white-matter|white matter integrity]], and [[resting-state|resting-state]] connectivity, demonstrating the translational value of the imaging resource when coupled with genome-wide genotyping [[raw/papers/elliott-2018.md|Elliott et al. (2018)]].

## References

1. (authors unknown). *Multimodal Population Brain Imaging in the UK Biobank: Prospective Epidemiological Study*.
2. (authors unknown). *Image Processing and Quality Control for the First 100,000 Brain Imaging Datasets from UK Biobank*.
3. (authors unknown). *Genome-wide Association Studies of Brain Imaging Phenotypes from UK Biobank*.
4. (authors unknown). *UK Biobank Brain Imaging: Structural MRI in a Massive Population Resource*.
5. (authors unknown). *The UK Biobank Imaging Study: 100,000 Participants and Beyond*.
