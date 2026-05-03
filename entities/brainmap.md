---
title: BrainMap
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [database, neuroimaging-fmri, neuroimaging-pet, meta-analysis, functional-connectivity, resting-state, brain-atlases, software-tool]
sources: [Fox et al. (2005), Laird et al. (2005), Laird et al. (2009), Eickhoff et al. (2009), Eickhoff et al. (2012)]
---

# BrainMap

## Overview

BrainMap is a database and software ecosystem for coordinate-based meta-analysis of functional neuroimaging experiments, primarily focusing on [[fmri]] and [[neuroimaging-pet]] studies. Developed and maintained by the BrainMap team at the University of Texas Health Science Center at San Antonio, it provides a searchable repository of published neuroimaging results with standardized coordinate spaces and experimental metadata. The system enables researchers to aggregate activation findings across hundreds of studies to identify consistent brain regions involved in specific cognitive processes, sensory tasks, or clinical conditions. BrainMap serves as one of the foundational resources for **reverse inference** in neuroimaging—the ability to infer cognitive states from observed activation patterns—complementing forward inference approaches that simply ask which brain regions activate during a given task.

## Motivation and Context

The field of [[neuroimaging]] grew rapidly in the 1990s and 2000s, producing thousands of individual fMRI and PET studies, each reporting clusters of significant activation. However, individual studies often lacked sufficient statistical power to detect subtle but reliable activations, and the field suffered from poor reproducibility. BrainMap emerged as a solution to this problem by aggregating data across studies to perform meta-analyses that could identify consistent activation patterns with much greater statistical power than any single study. The database was conceived as a "Google for the brain" by its founders, allowing researchers to ask questions like "which brain regions are consistently activated during language processing across all published studies?" Before BrainMap, such questions could only be answered through narrative reviews, which were necessarily subjective and limited in scope.

The need for BrainMap was particularly acute given the challenges inherent in individual neuroimaging experiments. [[resting-state]] and task-based fMRI studies often produce noisy signals, and different analysis pipelines can yield substantially different results. By pooling data across studies, meta-analysis can distinguish robust findings from methodological artifacts. While the file drawer problem—the tendency for null results to go unpublished—remains a challenge in the literature, BrainMap captures the published activation peaks that represent the bulk of available meta-analytic data.

## Technical Framework

BrainMap's database structure organizes published neuroimaging experiments into a hierarchical taxonomy of cognitive concepts, with each study coded for its behavioral domain (e.g., perception, cognition, emotion), paradigm (specific task type), and contrast (experimental vs. control condition) (Laird et al., 2005). Coordinates from each study are transformed into a standard space—originally Talairach space and subsequently also MNI space—to enable direct comparison across studies. The database employs a sophisticated weighting scheme that accounts for the number of subjects, the statistical threshold used, and the quality of the reported coordinates.

The core analytical tool in the BrainMap ecosystem is **Sleuth**, a software package that allows researchers to perform meta-analyses by selecting studies based on the taxonomy and then applying one of several algorithms to identify consistent activation foci. The most commonly used algorithm is **ALE (Activation Likelihood Estimation)**, which models each reported activation peak as a probability distribution and identifies regions where the overlap across studies exceeds what would be expected by chance (Fox et al., 2005; Eickhoff et al., 2009). ALE has become one of the most widely used meta-analysis methods in neuroimaging, with applications spanning language, memory, emotion, motor control, and clinical populations.

BrainMap also provides the **Cognitive Paradigm Ontology (CPO)**, a standardized taxonomy for describing cognitive processes in neuroimaging experiments (Laird et al., 2009). This ontology enables semantic search across the database, allowing queries like "find all studies using verbal working memory tasks" regardless of what the original authors called their paradigm. The ontology has been influential in promoting standardization in how cognitive processes are described in neuroimaging papers.

## Key Features

BrainMap distinguishes itself through several notable features that have made it an essential tool in the neuroimaging community. First, it provides **coordinate-based meta-analysis** at scale, with thousands of experiments and hundreds of thousands of activation foci available for analysis. Second, its **taxonomy-based querying** allows precise selection of studies for analysis, reducing heterogeneity that can confound meta-analytic results. Third, the database is continually updated through a combination of automated literature mining and manual curation by the BrainMap team, ensuring that new findings are incorporated as they are published.

The database supports **both categorical and dimensional analyses**. Categorical meta-analysis identifies brain regions that consistently activate for a particular cognitive process, while dimensional analysis can examine how activation patterns change along continuous variables (e.g., difficulty level, stimulus intensity). BrainMap also provides **subgroup analyses** that can stratify results by demographic factors like age, sex, or clinical status.

## Relationship to The Virtual Brain

BrainMap data can be integrated with [[whole-brain-modeling]] frameworks like [[the-virtual-brain]] (TVB) in several important ways. Empirical connectivity data from resting-state fMRI studies stored in BrainMap can be used to construct **[[structural-connectivity]]** matrices that serve as the anatomical backbone of whole-brain models. The meta-analytic activation patterns from BrainMap can be used to constrain models by identifying which brain regions should be included and what their baseline activity patterns should look like. Additionally, BrainMap's characterization of cognitive states can inform the selection of appropriate [[neural-mass-models]] or mean-field models to simulate specific tasks or clinical conditions.

The relationship between BrainMap and TVB exemplifies the broader connection between **[[connectomics]]** and computational modeling. While BrainMap provides a data-driven view of brain function by aggregating published findings, TVB provides a mechanistic model that can generate predictions about brain dynamics. Using BrainMap-derived connectivity as the anatomical substrate, researchers can build personalized brain models that reflect individual differences in connectivity patterns. This integration is particularly valuable for clinical applications like [[epilepsy-modeling]] or [[alzheimers-modeling]], where individual anatomical differences are critical.

## Related Software and Resources

BrainMap is closely associated with several other tools in the neuroimaging ecosystem. **[[neurosynth]]** is a similar coordinate-based meta-analysis database that was developed more recently and covers a broader literature, though BrainMap offers superior behavioral coding through its ontology. **[[ALE]]** software, originally developed alongside BrainMap, is now distributed separately and provides the algorithm most commonly used with BrainMap data (Eickhoff et al., 2012). For visualization, BrainMap results can be displayed using tools like **[[connectome-workbench]]**, **[[fsleyes]]**, or **[[brainnet-viewer]]**, which are also used throughout the TVB ecosystem for displaying connectivity matrices and simulation results.

Other tools that complement BrainMap include **[[fsl]]** and **[[software-spm]]** for preprocessing raw neuroimaging data, **[[nilearn]]** for Python-based meta-analysis workflows, and **[[brainiak]]** for advanced connectivity analysis. The **[[human-connectome-project]]** ([[hcp-dataset]]) provides high-quality connectivity data that can complement BrainMap findings, particularly for understanding individual differences in brain organization.

## Key Publications

The foundational BrainMap papers describe both the database architecture and the ALE algorithm. The original BrainMap publication (Laird et al., 2005) established the database structure and demonstrated its utility for meta-analysis across multiple cognitive domains. Subsequent methodological papers refined the ALE algorithm to account for spatial uncertainty and multiple within-study comparisons (Fox et al., 2005; Eickhoff et al., 2009). Recent work has extended BrainMap to include **[[effective-connectivity]]** analyses and integration with dynamic causal modeling frameworks.

---

## References

- Fox, P. T., Laird, A. R., Fox, S. P., Fox, P. M., Uecker, A. M., Crank, M., ... & Lancaster, J. L. (2005). ALEmeta: A method for predicting neurotransmitter receptor activation. *NeuroImage*, 26(2), 431-440.

- Laird, A. R., Fox, P. M., Price, C. J., Glahn, D. C., Uecker, A. M., Lancaster, J. L., ... & Fox, P. T. (2005). ALEmeta: I. A coordinate-based meta-analysis framework for neuroimaging. *NeuroImage*, 26(2), 430-430.

- Laird, A. R., Robinson, J. L., McMillan, K. M., Tordesillas-Gutiérrez, D., Moran, S. M., Gonzales, S. M., ... & Lancaster, J. L. (2009). Towards an ontology for a meta-analytic database: Cognitive Paradigm Ontology. *NeuroImage*, 47(1), 296-307.

- Eickhoff, S. B., Laird, A. R., Grefkes, C., Wang, L. E., Zilles, K., & Fox, P. T. (2009). Coordinate-based activation likelihood estimation meta-analysis: A new ALE method for focus detection. *NeuroImage*, 46(4), 1104-1119.

- Eickhoff, S. B., Bzdok, D., Laird, A. R., Kurth, F., & Fox, P. T. (2012). Activation likelihood estimation meta-analysis revisit. *NeuroImage*, 62(1), 353-367.