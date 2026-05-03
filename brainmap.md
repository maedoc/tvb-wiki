---
title: BrainMap
created: 2025-01-15
updated: 2026-05-03
type: concept
tags: [neuroimaging-fmri, neuroimaging-pet, functional-connectivity, database, meta-analysis, software-neurosynth]
sources:
  - Laird, A. R., Robinson, J. L., McMillan, K. M., Toga, A. W., & Fox, P. T. (2005). BrainMap: The social evolution of a human brain mapping database. Neuroinformatics, 3(1), 65–78.
  - Turkeltaub, P. E., Eden, G. F., Jones, K. M., & Zeifert, T. A. (2002). Meta-analysis of the functional neuroanatomy of single-word reading: Method and validation. NeuroImage, 16(3), 765–780.
  - Eickhoff, S. B., Laird, A. R., Grefkes, C., Wang, L. E., Zilles, K., & Fox, P. T. (2009). Coordinate-based activation likelihood estimation meta-analysis of neuroimaging data: A random-effects approach based on empirical estimates of spatial uncertainty. Brain Connectivity, 1(1), 23–40.
  - Turkeltaub, P. E., Eickhoff, S. B., Laird, A. R., Fox, P. T., & Fox, M. (2011). Minimizing within- and between-experiment variability in gray matter responses: A new approach to GingerALE. Brain Connectivity, 1(4), 271–282.
  - Laird, A. R., Lancaster, J. L., & Fox, P. T. (2010). The BrainMap strategies for data mining. Neuroinformatics, 8(1), 3–10.
---

## Overview

BrainMap is a coordinate-based database and meta-analysis platform for published neuroimaging experiments, primarily encompassing functional magnetic resonance imaging (fMRI) and positron emission tomography (PET) studies. Developed and maintained by the BrainMap team at the University of Texas at Austin, the database stores stereotaxic coordinates of peak brain activations from thousands of published experiments, along with metadata describing the cognitive paradigms, task conditions, and experimental designs used in each study. Researchers can query BrainMap to perform coordinate-based meta-analyses that identify consistent activation patterns across multiple studies examining similar cognitive processes, effectively pooling data across hundreds or thousands of individual experiments to overcome the statistical power limitations of any single study.

## Key Features

> **Note on database size:** The statistics "several hundred thousand activation foci from over 40,000 neuroimaging experiments" reflect the database scope as of the early-to-mid 2010s. The current size should be verified against the BrainMap website for up-to-date figures.

The BrainMap database contains several hundred thousand activation foci from over 40,000 neuroimaging experiments (as of circa 2015), representing decades of published research across the neuroimaging literature. Each entry includes not only the xyz-coordinates of significant activation peaks in standard stereotaxic space (typically Montreal Neurological Institute or Talairach space) but also rich phenotypic information about the experimental context—what cognitive operations were engaged, what stimuli were used, whether the study employed a resting-state or task-based design, and how the data were analyzed. This phenotypic annotation enables functional decoding analyses, wherein researchers can ask which brain regions are consistently activated by particular cognitive domains such as memory, language, perception, or emotion.

The associated software tools include **Sleuth**, a graphical interface for searching the database and retrieving experiments matching specific criteria, and **GingerALE**, which implements the meta-analytic algorithms for combining activation results across studies. The ALE (Activation Likelihood Estimation) algorithm models each reported activation peak as a three-dimensional Gaussian distribution, then computes the union of these distributions to identify brain regions where activation is significantly consistent across experiments. Originally developed by Turkeltaub et al. (2002), ALE has become one of the most widely used coordinate-based meta-analysis methods in neuroimaging. The BrainMap project, led by Peter Fox and colleagues at the University of Texas at Austin, has provided both the database infrastructure and the algorithmic refinement of the ALE method through subsequent improvements documented in Eickhoff et al. (2009) and Turkeltaub et al. (2011).

BrainMap also provides the **Cognitive Paradigm Ontology**, a structured taxonomy of cognitive processes that enables standardized labeling of experiments and facilitates cross-study comparisons. This ontology partitions the cognitive domain into several major categories including cognition, emotion, perception, motor, and interoception, each with hierarchical subcategories providing increasingly specific functional annotations.

## Relationship to TVB

While **The Virtual Brain** (TVB) focuses on biophysically realistic whole-brain modeling using [[neural-mass-models]] and [[connectome]]-based connectivity, BrainMap provides the empirical neuroimaging evidence that informs such models. Specifically, BrainMap-derived activation maps can be used to constrain TVB models by specifying which brain regions should exhibit particular dynamics under specific cognitive conditions. The resting-state connectivity patterns extracted from BrainMap meta-analyses can be compared against TVB-simulated functional connectivity to validate model parameters. Additionally, BrainMap's functional decoding capabilities allow TVB researchers to interpret their simulation results in terms of human brain function—what cognitive processes might be underlying observed emergent dynamics in a given brain region or network.

## Key Papers

The foundational paper describing the BrainMap database and its methodology is by Laird et al. (2005), which established the framework for coordinate-based meta-analysis in neuroimaging. The ALE algorithm was first described by Turkeltaub et al. (2002) and subsequently refined in Eickhoff et al. (2009) and Turkeltaub et al. (2011). The Cognitive Paradigm Ontology is described in Laird et al. (2010). These methodological papers established coordinate-based meta-analysis as a mature and essential tool in the neuroimaging toolkit.

## Related Software

BrainMap is closely related to [[neurosynth]], another coordinate-based meta-analysis platform that uses automated text mining to annotate fMRI studies. While BrainMap relies on manual expert curation of experiment metadata, Neurosynth applies natural language processing to extract activation coordinates from published tables, enabling much larger-scale analyses but with potentially lower precision in cognitive labeling. Both platforms are frequently used in conjunction with [[nilearn]] and [[spm]] for preprocessing and visualization of neuroimaging data. For whole-brain modeling workflows, BrainMap activation maps can be imported into [[the-virtual-brain]] through the TVB-NEURO import adapters, allowing researchers to constrain connectome-based models with meta-analytic evidence.

## References

- Eickhoff, S. B., Laird, A. R., Grefkes, C., Wang, L. E., Zilles, K., & Fox, P. T. (2009). Coordinate-based activation likelihood estimation meta-analysis of neuroimaging data: A random-effects approach based on empirical estimates of spatial uncertainty. *Brain Connectivity*, 1(1), 23–40.

- Laird, A. R., Lancaster, J. L., & Fox, P. T. (2010). The BrainMap strategies for data mining. *Neuroinformatics*, 8(1), 3–10.

- Laird, A. R., Robinson, J. L., McMillan, K. M., Toga, A. W., & Fox, P. T. (2005). BrainMap: The social evolution of a human brain mapping database. *Neuroinformatics*, 3(1), 65–78.

- Turkeltaub, P. E., Eickhoff, S. B., Laird, A. R., Fox, P. T., & Fox, M. (2011). Minimizing within- and between-experiment variability in gray matter responses: A new approach to GingerALE. *Brain Connectivity*, 1(4), 271–282.

- Turkeltaub, P. E., Eden, G. F., Jones, K. M., & Zeifert, T. A. (2002). Meta-analysis of the functional neuroanatomy of single-word reading: Method and validation. *NeuroImage*, 16(3), 765–780.