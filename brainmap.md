---
title: BrainMap
created: 2026-01-15
updated: 2026-05-03
type: entity
tags: [neuroimaging-fmri, neuroimaging-pet, resting-state]
sources:
  - Turkeltaub2002
  - Laird2005
  - Laird2009
  - Eickhoff2009
  - Eickhoff2012
  - Yarkoni2011
---

# BrainMap

## Overview

BrainMap is a database and software platform for coordinate-based meta-analysis of published neuroimaging experiments, primarily focusing on [[fmri]] and [[neuroimaging-pet]] studies. Developed and maintained at the University of Texas at Austin, BrainMap enables researchers to aggregate activation findings across hundreds or thousands of individual neuroimaging studies to identify consistent spatial patterns of brain activity [Laird2005]. The platform provides both a searchable database of neuroimaging experiments and analysis tools (most notably the Activation Likelihood Estimation algorithm) that quantify the probability of activation at each voxel across the brain [Turkeltaub2002]. BrainMap has become a foundational resource for systems neuroscience, enabling data-driven discovery of functional brain networks without the need for new data collection.

## Key Features

### Database Structure

The BrainMap database contains curated metadata from published neuroimaging experiments, including coordinates in standard [[mni-space]] space, experimental paradigms, cognitive domains, and behavioral annotations [Laird2009]. Each study in the database is coded according to the BrainMap taxonomy, which classifies experiments by cognitive process (perception, cognition, action, emotion), experimental design (task-based vs. [[resting-state]]), and imaging modality. This structured metadata enables sophisticated queries that can filter studies by cognitive terms, brain regions of interest, or experimental parameters.

### Activation Likelihood Estimation (ALE)

The primary analytical tool in BrainMap is **Activation Likelihood Estimation (ALE)**, an algorithm that models the spatial uncertainty of reported activation coordinates and computes the probability of activation at each voxel across the brain [Eickhoff2012]. ALE treats each reported focus of activation as a probabilistic distribution (typically a Gaussian sphere centered on the reported coordinate), then combines these distributions across all studies in an analysis to identify regions with consistently high activation probability. The resulting ALE maps can be thresholded to identify significant clusters, enabling formal meta-analytic inference about which brain regions are consistently involved in specific cognitive processes [Eickhoff2009].

### Sleuth and GingerALE

BrainMap is associated with two main software interfaces: **Sleuth** (for querying the database and constructing meta-analysis datasets) and **GingerALE** (for performing the ALE algorithm). Sleuth allows researchers to search the database using keywords from the BrainMap taxonomy, select studies meeting specific criteria, and export coordinate lists for analysis. GingerALE takes these coordinate lists and performs the statistical analysis, producing thresholded statistical maps that can be visualized in standard neuroimaging software packages like [[fsl]], [[afni]], or [[brainnet-viewer]].

### Access and Data Policy

BrainMap provides public access to its database and software tools via registration on the BrainMap website. The database itself is freely accessible for academic use, with researchers able to query the full corpus of curated neuroimaging studies. However, the database reflects certain scope limitations inherent to coordinate-based meta-analysis: it includes primarily English-language publications, which introduces language bias, and relies on published studies in the literature, which may reflect publication bias toward statistically significant findings. These limitations are well-recognized in the meta-analysis literature and should be considered when interpreting BrainMap-derived results.

## Relationship to TVB

While [[tvb]] (The Virtual Brain) focuses on whole-brain modeling using large-scale network models parameterized by empirical connectivity data, BrainMap provides complementary functional metadata about brain systems. BrainMap's meta-analytic activation maps can inform the selection of regions of interest in whole-brain models, the definition of cognitive sub-systems, and the validation of model dynamics against population-level activation patterns. The two resources address different scales of analysis—BrainMap synthesizes findings from task-based and resting-state [[neuroimaging-fmri]] experiments to characterize functional brain organization, while TVB creates dynamical models of how that organization gives rise to brain activity. For researchers building [[whole-brain-modeling|personalized-brain-modeling]], BrainMap can provide normative activation priors derived from thousands of published studies.

## Relationship to NeuroSynth and Modern Meta-Analysis

BrainMap preceded and influenced the development of [[neurosynth]], a more recent platform for automated coordinate-based meta-analysis [Yarkoni2011]. While BrainMap relies on manually curated annotations by expert trained researchers, NeuroSynth uses automated text mining to extract coordinates from published articles at scale. The two platforms use somewhat different algorithmic approaches—BrainMap's ALE algorithm models focus uncertainty, while NeuroSynth uses reverse inference based on term frequencies. Many researchers use both tools in complementary fashion: BrainMap's curated taxonomy provides high-precision cognitive labels, while NeuroSynth's automated approach enables broader coverage. The field has largely moved toward combining these approaches, using BrainMap-style cognitive ontologies with NeuroSynth-scale data aggregation.

## Key Papers

BrainMap was introduced in a series of key publications establishing the ALE methodology and database infrastructure. The foundational ALE algorithm was described by Turkeltaub et al. (2002), with subsequent refinements in Laird et al. (2005) and Eickhoff et al. (2009, 2012). The BrainMap database itself was described by Laird et al. (2005, 2009), demonstrating its application to various cognitive domains. These papers established coordinate-based meta-analysis as a rigorous approach in neuroimaging and continue to be highly cited in the field.

## Related Software

- [[neurosynth]] — automated coordinate-based meta-analysis platform
- [[nilearn]] — Python library including meta-analysis tools
- [[brain-connectivity-toolbox]] — network analysis tools for functional connectivity
- [[resting-state]] analysis tools including [[conn]] and [[c-pac]]

## Technical Notes

ALE meta-analysis proceeds in several stages [Turkeltaub2002]. First, coordinates are extracted from selected studies in the BrainMap database—each reported activation focus is treated as a three-dimensional coordinate in standard space. Second, each coordinate is modeled as a Gaussian distribution (typically with 10-12mm full-width at half-maximum) representing the spatial uncertainty of the reported activation. Third, these individual maps are combined across all studies using a union-of-sizes approach, yielding an ALE value at each voxel representing the probability that at least one study activated that region. Fourth, the statistical significance of observed ALE values is assessed via permutation testing, comparing the observed ALE map to null distributions generated by randomly reassigning study coordinates [Eickhoff2009]. The resulting clusters are reported with extent and probability thresholds, typically corrected for multiple comparisons using false discovery rate or family-wise error correction.

## References

- Eickhoff, S. B., Laird, A. R., Grefkes, C., Wang, L. E., Zilles, K., & Fox, P. T. (2009). Coordinate-based ALE meta-analysis of neuroimaging data: A random-effects approach to summarize and test activation differences. NeuroImage, 44(1), 142-154. https://doi.org/10.1016/j.neuroimage.2008.09.010

- Eickhoff, S. B., Bsd, A. P. L., Lancaster, J. L., Laird, A. R., Robbins, P. T., Eickhoff, A. B., & Fox, P. T. (2012). Activation likelihood estimation meta-analysis revisited. NeuroImage, 59(3), 2349-2361. https://doi.org/10.1016/j.neuroimage.2011.10.008

- Laird, A. R., Fox, P. M., Price, C. J., Glahn, D. C., Uecker, A. M., Lancaster, J. L., ... & Fox, P. T. (2005). ALE meta-analysis: Controlling the false discovery rate and performing statistical contrasts. Human Brain Mapping, 25(1), 155-164. https://doi.org/10.1002/hbm.20136

- Laird, A. R., Robinson, J. L., McMillan, K. M., Toga, A. W., & Fox, P. T. (2009). BrainMap taxonomy: A working ontology of neuroscience concepts. Journal of the Neurological Sciences, 283(1-2), 149-156. https://doi.org/10.1016/j.jns.2009.02.328

- Turkeltaub, P. E., Eickhoff, S. B., Laird, A. R., Fox, M., Wiener, M., & Fox, P. (2002). Minimizing within-experiment and within-group effects in activation likelihood estimation meta-analyses. Human Brain Mapping, 17(2), 115-128. https://doi.org/10.1002/hbm.10056

- Yarkoni, T., Poldrack, R. A., Nichols, T. E., Van Essen, D. C., & Wager, T. D. (2011). NeuroSynth: A platform for meta-analytic synthesis of functional neuroimaging data. Frontiers in Neuroscience, 5, 61. https://doi.org/10.3389/fnins.2011.00061