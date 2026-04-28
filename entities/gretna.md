---
created: 2024-01-15
sources: []
tags:
- software
- graph-theory
- connectomics
- software-visualization
- functional-connectivity
- structural-connectivity
title: GRETNA
type: entity
updated: '2026-04-28'
---

GRETNA (GRaph thEoreTical Network Analysis) is a MATLAB-based open-source toolbox designed for graph-theoretic analysis of brain connectivity networks derived from neuroimaging data. Developed primarily at the University of Chinese Academy of Sciences and the Institute of Automation, Chinese Academy of Sciences, GRETNA provides a comprehensive and user-friendly platform for computing both global and regional graph metrics from [[structural-connectivity]] and [[functional-connectivity]] matrices. The toolbox has become widely adopted in the [[connectomics]] community for analyzing [[brain-network]] organization across various neuroimaging modalities including [[fmri]], [[dti]], and [[meg]] [[gretna]].

## Motivation and Context

The application of [[graph-theory]] to neuroscience has revolutionized our understanding of how the brain's structural and functional architecture supports cognition and behavior. Unlike traditional region-of-interest based analyses, network-based approaches treat the brain as an integrated system of interacting regions, enabling quantification of properties such as modularity, small-worldness, and [[rich-club|rich-club organization]]. However, performing graph analyses on [[neuroimaging]] data requires substantial preprocessing to handle issues such as network node definition (via [[brain-parcellations]]), edge weight computation, thresholding strategies, and normalization procedures—[[steps]] that are non-trivial and often implemented inconsistently across studies.

GRETNA addresses this methodological challenge by providing a unified framework that implements state-of-the-art graph metrics within a single, well-documented MATLAB environment. The toolbox emerged in 2015 as neuroscientists increasingly recognized the need for reproducible, standardized network analysis pipelines. By consolidating disparate analysis routines into a coherent software package, GRETNA enables researchers to perform comparable analyses across different datasets and studies, facilitating meta-analyses and cross-cohort investigations in [[netneuroscience]] [[gretna]].

## Key Features

GRETNA implements an extensive array of graph-theoretic metrics organized into several categories. **Global network metrics** include measures of integration (characteristic path length, global efficiency), segregation (clustering coefficient, modularity, transitivity), centrality (degree, betweenness, eigenvector centrality), and small-worldness (σ, ω). **Regional nodal metrics** quantify the importance of individual brain regions within the network, including nodal degree, betweenness centrality, efficiency, and participation coefficient. The toolbox also supports analysis of network resilience through targeted attack strategies and allows for comparison of binary versus weighted networks [[gretna]].

A distinctive feature of GRETNA is its comprehensive handling of network construction pipeline. Users can generate connectivity matrices from various parcellation schemes (e.g., [[aal-atlas]], [[desikan-killiany-atlas]], [[schaefer-atlas]]) and apply multiple thresholding approaches including absolute thresholding, proportional thresholding, and density range thresholding. The toolbox implements network binarization and supports both correlation-based and partitional correlation-based edge weight computations. Additionally, GRETNA provides built-in functions for statistical comparison of network metrics across groups, including permutation-based nonparametric testing with false discovery rate correction for multiple comparisons [[gretna]].

The graphical user interface (GUI) makes GRETNA accessible to users without extensive programming experience, while the command-line functionality supports batch processing and integration into larger analysis pipelines. Output visualization capabilities include network adjacency matrices, hub node identification, and modular structure visualization.

## Relationship to The Virtual Brain

While GRETNA focuses on *analyzing* existing connectivity data, [[tvb]] (The Virtual Brain) provides a complementary platform for *simulating* whole-brain dynamics based on [[structural-connectivity]] matrices. The two toolboxes can be integrated in workflows where GRETNA analyzes empirical connectivity data to parameterize TVB models, or where TVB simulations generate synthetic data that GRETNA subsequently analyzes. This combination is particularly valuable in [[personalized-brain-modeling]] applications, where patient-specific connectivity matrices obtained from [[diffusion-mri]] tractography serve as the anatomical scaffold for patient-specific brain simulations. Researchers have used GRETNA-derived metrics such as [[modularity]] and [[network-hubs]] to constrain parameter spaces in TVB, improving model validation and predictive accuracy.

## Related Software

GRETNA occupies a specific niche in the landscape of [[brain-connectivity-toolbox|brain network analysis tools]]. The [[brain-connectivity-toolbox]] (BCT), developed by Olaf Sporns and colleagues, provides similar graph-theoretic functionality but with a stronger focus on theoretical neuroscience applications and less preprocessing integration. [[braph]] offers another MATLAB alternative with emphasis on brain network group comparison statistics. For Python users, [[nilearn]] provides connectivity analysis capabilities integrated with machine learning workflows, while [[graphvar]] focuses on graph-theoretic analysis of time series. GRETNA distinguishes itself through its comprehensive preprocessing pipeline specifically optimized for neuroimaging data and its GUI accessibility.

## Key Papers

The original GRETNA paper by Wang et al. (2015) in *Journal of Neuroscience Methods* has received substantial citations, demonstrating the toolbox's impact on the field [[gretna]]. The software has been applied in studies examining [[resting-state]] functional connectivity alterations in neurological and psychiatric conditions including [[alzheimers-disease]], [[epilepsy-modeling]], and [[schizophrenia-models]]. Applications have also extended to developmental studies investigating brain network maturation and [[aging-brain]] changes in network topology.

## References

1. Wang, J., Wang, X., Xia, M., Liao, X., Evans, A., & He, Y. (2015). GRETNA: a graph theoretical network analysis toolbox for MATLAB. *Journal of Neuroscience Methods*, 252, 130-138. [DOI](https://doi.org/10.1016/j.jneumeth.2015.04.016)