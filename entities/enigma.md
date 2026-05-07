---
created: 2024-01-15
sources:
- Stein JL et al. Nature Genetics 2012
- van Erp TGM et al. Molecular Psychiatry 2016
- Schmaal L et al. Molecular Psychiatry 2016
- Hibar DP et al. Molecular Psychiatry 2017
- Hoogman M et al. Lancet Psychiatry 2017
- Boedhoe PS et al. American Journal of Psychiatry 2017
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-57c27f9f72e9.md
- raw/papers/ritter-2013.md
tags:
- neuroimaging-fmri
- neuroimaging-dti
- database-hcp
- database-uk-biobank
- connectomics
- structural-connectivity
- functional-connectivity
- whole-brain-modeling
- personalized-brain-modeling
- dataset
title: ENIGMA
type: entity
updated: '2026-05-07'
---

ENIGMA (Enhancing [[neuroimaging]] Genetics through Meta-Analysis) is an international consortium that brings together neuroimaging researchers from dozens of institutions worldwide to perform large-scale collaborative studies on brain structure and function. Founded in 2009 by Professor Paul Thompson of the University of Southern California (USC) and colleagues, ENIGMA pioneered the use of mega-analyses (combining individual participant data rather than summary statistics) to achieve statistical power previously impossible in single-site studies. The consortium has grown to include over 800 investigators across more than 340 institutions in 35 countries, with working groups focused on schizophrenia, major depressive disorder (MDD), bipolar disorder, ADHD, autism, obsessive-compulsive disorder (OCD), and healthy [[aging]]. This distributed approach to neuroimaging research has become a template for open science collaboration in the field.

## ENIGMA-Schizophrenia

The ENIGMA-Schizophrenia Working Group represents one of the largest collaborative efforts in psychiatric neuroimaging, pooling MRI data from over 4,500 patients with schizophrenia across multiple international cohorts. In a landmark meta-analysis published in 2016, the consortium identified consistent reductions in hippocampal volume (Cohen's d = 0.37) and thalamic volume (Cohen's d = 0.31) among schizophrenia patients compared to healthy controls, with effect sizes that were remarkably consistent across sites from diverse geographic regions. The study demonstrated that despite the heterogeneity inherent in psychiatric diagnoses, reliable neurobiological signatures could be detected when sufficient statistical power was achieved through international collaboration.

## ENIGMA-Major Depressive Disorder

The ENIGMA-MDD working group published the world's largest structural MRI study of major depressive disorder, analyzing data from over 10,000 individuals. The study revealed that MDD patients showed significant reductions in hippocampal volume (Cohen's d = 0.24) compared to healthy controls, with the strongest effects observed in patients with recurrent or chronic depression. Notably, the effect sizes were more modest than those seen in schizophrenia, highlighting the need for large sample sizes to detect the subtler brain structure alterations associated with mood disorders.

## ENIGMA-Bipolar Disorder

The ENIGMA-Bipolar Disorder Working Group identified distinct patterns of subcortical brain alterations that differentiated bipolar disorder from schizophrenia and major depression. In a study of over 4,000 individuals, the consortium found reduced thalamic volumes (Cohen's d = 0.32) and amygdala volumes (Cohen's d = 0.24) in bipolar disorder patients, with some overlap in hippocampal volume reductions seen across all three major psychiatric disorders. This cross-disorder approach has proven invaluable for understanding both shared and unique neurobiological mechanisms across diagnostic categories.

## ENIGMA-ADHD and ENIGMA-OCD

Additional disease-focused working groups have extended the ENIGMA model to attention-deficit/hyperactivity disorder (ADHD) and obsessive-compulsive disorder (OCD). The ENIGMA-ADHD study, one of the largest neuroimaging studies of ADHD to date, revealed reduced volumes in the amygdala (Cohen's d = 0.28) and caudate nucleus (Cohen's d = 0.21) in affected individuals. The ENIGMA-OCD consortium identified altered volumes in the thalamus and pallidum, demonstrating that even disorders with putatively different neurobiological origins show consistent brain structure changes when analyzed across large, harmonized datasets.

## Motivation and Scientific Context

Before ENIGMA, neuroimaging genetic studies were severely underpowered, typically involving dozens or hundreds of participants from single sites. Effect sizes for common genetic variants on brain structure are typically small (Cohen's d < 0.3), requiring sample sizes in the thousands to detect reliable associations. ENIGMA addressed this problem by establishing standardized processing protocols using [[freesurfer]] for cortical reconstruction and [[fsl]] for subcortical segmentation, enabling meaningful meta-analyses across heterogeneous scanner platforms and acquisition protocols. The consortium developed the ENIGMA consortium analysis protocol, which has become a de facto standard for multi-site neuroimaging studies and is now implemented in pipelines like [[ciftify]] for reproducible analysis. By pooling data across sites, ENIGMA studies can identify subtle but reliable brain structure alterations in patient populations that would be invisible in underpowered single-site experiments.

## Key Datasets and Outputs

ENIGMA has produced several landmark datasets and analytical resources that are widely used in the [[whole-brain|whole-brain modeling]] community. The ENIGMA cortical thickness and surface area normative maps provide quantitative estimates of regional brain structure differences across the lifespan and in clinical populations. These effect size maps, expressed as standardized z-scores relative to healthy controls, have been published for schizophrenia (over 4,500 patients), bipolar disorder (over 4,300 patients), major depression (over 10,000 subjects), ADHD (over 3,200 subjects), and OCD (over 3,500 subjects), creating a curated resource for disease biomarker discovery. ENIGMA also maintains public genome-wide association study (GWAS) results through the ENIGMA-Vis interactive portal, allowing researchers to query the effects of specific genetic variants on brain structure measures. All harmonized protocols and analysis pipelines are freely available through the ENIGMA website (enigma.ini.usc.edu), enabling other research groups to implement standardized processing workflows.

## Relationship to TVB

ENIGMA-derived effect size maps provide group-average empirical constraints that can be translated into [[the-virtual-brain]] lesion or [[structural-connectivity]] perturbation models. When ENIGMA reports reduced cortical thickness in specific regions for a given disorder (e.g., frontal lobe thinning in schizophrenia), these z-score maps can inform the parameter initialization of [[neural-mass-model]] simulations in TVB, allowing researchers to simulate the functional consequences of ENIGMA-identified structural changes. For example, [[epilepsy-modeling]] studies have used ENIGMA-derived atrophy patterns to initialize patient-specific TVB simulations showing altered seizure propagation due to structural lesions. Similarly, [[alzheimers-disease]] studies have mapped ENIGMA hippocampal atrophy findings onto TVB connectome models to predict downstream effects on resting-state [[functional-connectivity]]. The consortium's standardized processing output (processed via [[freesurfer]] and [[fsl]]) can also be directly integrated into TVB's anatomical connectivity pipelines, enabling construction of personalized brain models using ENIGMA-harmonized data from [[hcp-dataset]] and [[uk-biobank]] cohorts. This integration represents a key pathway for translating population-level neuroimaging findings into testable predictions about brain dynamics in individual patients.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Xinyu Wang, Sicheng Chen, Yanrong Chen, Xinian Zuo, Jingping Zhao, Yufeng Zang, Chao-Gan Yan. (2025). *The academic impact of open data: Bibliometric evidence from the DIRECT consortium and the [[rest]]-meta-MDD database*. China Scientific Data. [DOI](https://doi.org/10.11922/11-6035.csd.2025.0033.zh)
3. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain [[connectivity]]. [DOI](https://doi.org/10.1089/brain.2012.0120)