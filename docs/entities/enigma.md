---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-57c27f9f72e9.md
- raw/papers/sanz-leon-2013.md
- raw/papers/elliott-2018.md
tags:
- database
- connectomics
- neuroimaging
- neuroimaging-dti
- neuroimaging-mri
- structural-connectivity
- brain-parcellations
- brain-network
- schizophrenia-models
- epilepsy-modeling
- resting-state
- reproducibility
- people-paul-thompson
title: ENIGMA
type: entity
updated: '2026-05-01'
---

## Overview

ENIGMA (Enhancing Neuro Imaging Genetics through Meta Analysis) is an international consortium of researchers established in 2009 that combines [[neuroimaging]] data from hundreds of labs worldwide to identify robust brain biomarkers for psychiatric and neurological disorders. The consortium pioneered large-scale collaborative neuroimaging research, developing standardized image processing protocols that enable meta-analysis across diverse populations and scanning sites. ENIGMA's approach addresses a fundamental challenge in neuroimaging: the limited statistical power of individual studies to detect small but consistent effects in brain structure and function.

## Key Features

ENIGMA has developed widely-adopted protocols for processing magnetic resonance imaging (MRI) data, including diffusion tensor imaging (DTI) and structural MRI, ensuring consistency across sites. The ENIGMA-DTI protocol, detailed in the consortium's foundational methods paper (Thompson et al., 2014), became a de facto standard for [[white-matter]] analysis in neuroimaging research. These standardized processing pipelines enable unprecedented cross-site harmonization and have been adopted by hundreds of laboratories globally.

The consortium established specialized working groups focusing on specific disorders, including schizophrenia, Alzheimer's disease, major depression, bipolar disorder, epilepsy, and autism. Each working group conducts analyses combining individual-level data from participating sites when data-sharing agreements permit, using mega-analysis approaches, while also employing traditional meta-analytic techniques on summary statistics when full data sharing is not possible. This flexible methodology yields greater statistical power than individual site studies alone.

ENIGMA integrates neuroimaging with genome-wide association studies (GWAS), identifying genetic variants linked to brain structure and function. The consortium's GWAS work revealed that many common genetic variants affecting brain measures are shared across psychiatric conditions, informing the emerging framework of [[computational-psychiatry]].

ENIGMA researchers developed machine learning classifiers that combine multimodal neuroimaging features to predict disease status and clinical outcomes. These models trained on ENIGMA datasets demonstrated transferability across populations, addressing long-standing concerns about neuroimaging biomarker [[reproducibility]].

## Relationship to TVB

ENIGMA provides high-quality, harmonized neuroimaging datasets that serve as essential inputs for [[whole-brain|whole-brain modeling]] efforts in [[the-virtual-brain]] (TVB). ENIGMA's [[structural-connectivity]] matrices, derived from [[diffusion-imaging]] across large cohorts, are frequently used to construct [[personalized-brain-modeling|personalized brain]] network models. The consortium's normative data on brain structure variations across age groups also informs TVB's aging brain modeling efforts, enabling simulation of age-related changes in [[brain-dynamics]].

## Historical Context

ENIGMA emerged from the recognition that neuroimaging studies typically comprise small samples with limited statistical power to detect subtle effect sizes characteristic of psychiatric and neurological conditions. The consortium's founding principal investigator Paul Thompson at the University of Southern California led an effort to aggregate data from dozens of sites, initially focusing on schizophrenia and later expanding to numerous other disorders. This collaborative model preceded similar efforts in other fields and demonstrated the feasibility of open-science neuroimaging consortia.

## Key Achievements

The consortium produced landmark findings including the identification of reduced [[fractional-anisotropy]] (FA) in schizophrenia patients across 20 sites globally, establishing that white matter alterations represent a reproducible neurobiological signature. ENIGMA's analyses of nearly 50,000 individuals identified robust age-related changes in brain structure, while their GWAS work identified specific genetic loci influencing white matter integrity. The consortium also pioneered the "ENIGMA Toolbox" providing standardized processing pipelines now deployed across hundreds of labs.

## Related Concepts

ENIGMA's work connects to several key domains within the wiki: the consortium's standardized processing pipelines represent standard practices in neuroimaging quality control; its disease working groups advance personalized brain modeling through identification of biomarkers; and its emphasis on open data sharing supports reproducibility standard practices. The consortium's approach to combining data across sites parallels efforts in the [[mrtrix3-connectome]] and [[uk-biobank]] to create large-scale neuroimaging resources.