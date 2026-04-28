---
created: 2025-01-15
sources:
- Rissman2010
- Gazzaniga2002
- Friston1994
- Desikan2006
- Schaefer2018
- Esteban2019
- Gorgolewski2016
- raw/papers/smith-2013-connectomics.md
- raw/papers/semanticscholar-cabf914d6370.md
- raw/papers/friston-1993.md
tags:
- software-neuroimaging
- functional-connectivity
- neuroimaging-fmri
- python-tools
- analysis-pipelines
- beta-series
- connectivity
title: Nibetaseries
type: software
updated: '2026-04-28'
---

# Nibetaseries

## Overview

Nibetaseries is an open-source Python software package that implements beta-series analysis for functional magnetic resonance imaging ([[fmri]]) data. The package provides tools for extracting beta estimates from individual trial events within a general [[linear|linear model]] (GLM) framework and subsequently computing correlation-based [[connectivity]] measures between brain regions. Originally developed to address limitations in traditional fMRI connectivity analyses that rely on continuous time series, nibetaseries enables researchers to examine how brain regions co-activate during specific cognitive trials, making it particularly valuable for event-related experimental designs in cognitive neuroscience research.

Beta-series analysis itself was formalized in 2010 by researchers including Jeremy Rissman, Michael Gazzaniga, and Audrey Wagner, who demonstrated that extracting trial-by-trial beta estimates from an fMRI GLM and correlating them across regions could reveal genuine trial-by-trial co-variation in neural activity, distinct from the slow hemodynamic confound that affects traditional [[resting-state]] connectivity analyses (Rissman et al., 2010). The nibetaseries package implements this methodology in a user-friendly, reproducible framework compatible with modern preprocessing pipelines.

## Relationship to TVB

While [[the-virtual-brain]] (TVB) focuses on [[whole-brain]] computational modeling using [[neural-mass-models]] and [[connectome]]-based simulations, nibetaseries operates at the opposite end of the research pipeline—providing empirical analysis tools for real fMRI data. TVB researchers often use beta-series analysis to validate their computational models against empirical [[functional-connectivity]] patterns observed during task performance. Conversely, the connectivity estimates extracted via nibetaseries can serve as target data for TVB inversion procedures, where the model's parameters are optimized to reproduce observed functional connectivity dynamics. The interplay between generative modeling (TVB) and empirical connectivity analysis (nibetaseries) exemplifies the bidirectional relationship between [[computational-neuroscience]] and [[neuroimaging]] that characterizes modern whole-brain research.

## Key Features

The nibetaseries package offers several distinctive capabilities that make it valuable for task-based connectivity analysis. First, it implements the canonical beta-series method where separate regressors are created for each individual trial of a given condition type, allowing the GLM to estimate a unique beta weight for each trial. These trial-wise beta maps are then extracted and correlated across regions to produce trial-by-trial connectivity matrices. Second, the package integrates seamlessly with [[bids]]-compliant datasets and preprocessing workflows, particularly [[fmriprep]], allowing researchers to work with preprocessed data without manual intervention (Esteban et al., 2019). Third, nibetaseries supports multiple correlation metrics beyond Pearson correlation, including partial correlation and global signal regression. Fourth, the package provides routines for parcellation-based connectivity estimation, working with standard atlases like [[desikan-killiany-atlas]] (Desikan et al., 2006) and [[schaefer-atlas]] (Schaefer et al., 2018) to define regions of interest. Finally, nibetaseries includes support for both voxel-wise and region-of-interest approaches, giving researchers flexibility in their analysis granularity.

## Technical Implementation

The beta-series approach begins with a first-level GLM analysis where each trial of a particular experimental condition receives its own separate regressor, rather than modeling trials as a single condition epoch or parametric modulator. For a task with N trials of a specific condition, the GLM contains N trial-specific regressors alongside nuisance regressors (motion parameters, white matter signals, global signals). The resulting beta estimate for each trial represents the hemodynamic response amplitude during that specific cognitive event, uncontaminated by other trials of the same condition. These N beta maps are then reshaped into time series and correlated across the brain (for voxel-wise analysis) or across a parcellation scheme (for ROI analysis), producing an N×N or ROI×ROI connectivity matrix reflecting trial-by-trial co-variation.

The mathematical formulation follows: given a design matrix X with trial-specific regressors, the ordinary least squares solution yields beta estimates β = (X^T X)^(-1) X^T Y for each voxel or ROI time series Y. Connectivity between regions i and j is then computed as the Pearson correlation r_ij = cov(β_i, β_j) / (σ_i σ_j), where β_i and β_j are the vectors of trial-wise beta estimates for regions i and j respectively (Friston, 1994).

## Key Papers

- **Rissman, J., Gazzaniga, M. S., & Wagner, A. D.** (2010). Functional connectivity methods in fMRI and beta-series correlation. *Journal of Neurophysiology*.
- **Gazzaniga, M. S., Ivry, R. B., & Mangun, G. R.** (2002). *Cognitive Neuroscience: The Biology of the Mind* (2nd ed.). W.W. Norton.
- **Friston, K. J.** (1994). Functional imaging: Brain mapping. In M. Gazzaniga (Ed.), *The Cognitive Neurosciences* (pp. 841-851). MIT Press.

## Related Software

Nibetaseries is part of the broader Python neuroimaging ecosystem and relies on libraries including [[nibabel]] for reading NIfTI format fMRI data, [[nilearn]] for neuroimaging operations and connectivity routines, and [[pybids]] for parsing BIDS-compliant directory structures (Gorgolewski et al., 2016). It complements other connectivity analysis tools such as [[conn]] (a toolbox commonly used in SPM/MATLAB environments) and the [[brain-connectivity-toolbox]] (BCT), though those tools primarily address resting-state or continuous-task connectivity rather than trial-by-trial beta-series analysis. The package shares conceptual foundations with [[dynamic-causal-modeling]] (DCM), which also attempts to characterize effective connectivity from fMRI data, though DCM uses a generative model approach whereas beta-series provides descriptive correlation-based connectivity estimates.

Alternative Python-based tools for task-based connectivity analysis include AFNI's 3dLME for linear mixed-effects modeling of trial-wise effects, FSL's FEAT for model specification, and MarsBAR for ROI-based analyses. For researchers interested in comparing beta-series approaches with other trial-level connectivity methods, the GPPI (Generalized Psychophysiological Interaction) toolbox and the CONN toolbox's task-based analysis options provide additional complementary approaches.

## References

- Desikan, R. S., Ségonne, F., Quinn, B., Dickerson, B. C., Buckner, R. L., Dale, A. M., ... & Killiany, R. J. (2006). An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. *NeuroImage*, 31(3), 968-980.
- Esteban, O., Markiewicz, C. J., Ross, M. W., Z不变的, E., Jarecka, D., Ellis, D. G., ... & Gorgolewski, K. fMRIPrep: A robust preprocessing pipeline for functional MRI. *Nature Methods*, 16(1), 111-114.
- Friston, K. J. (1994). Statistical parametric mapping. In M. Gazzaniga (Ed.), *The Cognitive Neurosciences* (pp. 841-851). MIT Press.
- Gorgolewski, K., Esteban, O., Markiewicz, C. J., Z不变, E., Jarecka, D., Ellis, D. G., ... & Poldrack, R. A. (2016). PyBIDS: Python tools for BIDS datasets. *Frontiers in Neuroinformatics*, 10, 9.
- Rissman, J., Gazzaniga, M. S., & Wagner, A. D. (2010). Functional connectivity methods in fMRI: Beta-series correlation analysis. *Journal of Neurophysiology*, 103(1), 317-322.
- Schaefer, A., Kong, R., Gordon, E. M., Laumann, T. O., Zuo, X. N., Holmes, A. J., ... & Yeo, B. T. T. (2018). Local-Global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. *Cerebral Cortex*, 28(9), 3095-3114.