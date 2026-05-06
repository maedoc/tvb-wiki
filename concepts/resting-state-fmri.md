---
created: 2025-01-15
sources:
- biswal-1995
- greicius-2004
- fox-2007
- buckner-2008
- van-den-heuvel-2010
- bullmore-2009
- menon-2013
- smith-2009
- powers-2014
- zhang-2016
- hutchison-2013
- raichle-2001
tags:
- resting-state
- neuroimaging-fmri
- functional-connectivity
- brain-network
- resting-state-fmri
- default-mode-network
- intrinsic-connectivity-networks
title: Resting-State fMRI
type: concept
updated: '2026-05-06'
---

[[resting-state|Resting-state fMRI]] (rs-[[fmri]]) is a [[neuroimaging]] technique that measures spontaneous low-frequency fluctuations (< 0.1 Hz) in the blood-oxygen-level-dependent ([[bold-signal|BOLD]]) signal while a subject lies quietly in the scanner without performing any explicit task [[biswal-1995]]. Unlike task-based fMRI, which probes evoked responses to external stimuli or internal cognitive operations, resting-state fMRI captures the brain's intrinsic organization—the architecture of coherent [[spontaneous-activity]] that emerges in the absence of goal-directed behavior.

## Motivation and Historical Context

The seminal work of [[biswal-1995]] demonstrated that spontaneous fluctuations in the motor cortex during rest show remarkable temporal correlation between homologous regions in opposite hemispheres, establishing that these fluctuations contain meaningful structure rather than simply reflecting scanner noise or physiological artifacts. This discovery built upon earlier observations of slow hemodynamic oscillations and was later extended by [[greicius-2004]] who identified the [[default-mode-network]]—a set of brain regions showing high metabolic demand at rest but suppressed during task performance [[raichle-2001]]. The default-mode network includes the medial prefrontal cortex, posterior cingulate cortex, and angular gyrus, and is thought to support internal mentation, self-referential processing, and memory consolidation [[buckner-2008]].

Resting-state fMRI quickly became a cornerstone of functional connectivity analysis because it provides a standardized, replicable measurement that does not require sophisticated task design or subject training. This simplicity has made rs-fMRI particularly valuable for clinical applications, developmental studies, and large-scale consortia such as the [[human-connectome-project]] (over 1,200 resting-state scans) and [[uk-biobank]] (over 40,000 resting-state scans), which have acquired thousands of resting-state scans from diverse populations [[smith-2009]].

## Technical Basis of Functional Connectivity

Functional connectivity in rs-fMRI is defined as the temporal correlation between BOLD time series from distinct brain regions [[fox-2007]]. The raw BOLD signal reflects a convolution of underlying neural activity with the [[hemodynamic-response-function]], which acts as a low-pass filter and introduces a temporal delay of approximately 2–6 seconds between neural events and the measured signal [[hutchison-2013]]. Preprocessing typically includes motion correction, slice timing correction, spatial smoothing, band-pass filtering (commonly 0.01–0.1 Hz), and regression of nuisance parameters such as global signal, white matter signals, and cerebrospinal fluid signals [[power-2014]].

Several analysis approaches extract connectivity patterns from rs-fMRI data. Seed-based correlation analysis defines a region of interest a priori and computes correlation maps with all other voxels or parcels. Independent component analysis (ICA) decomposes the data into spatially independent components, some of which correspond to known functional networks such as the [[default-mode-network]], salience network, and fronto-parietal control network [[smith-2009]]. Graph-theoretical approaches model the brain as a network of nodes (regions) and edges (pairwise correlations), enabling quantification of global topology properties including modularity, small-worldness, and rich-club organization [[bullmore-2009]], [[van-den-heuvel-2010]].

## Relationship to Whole-Brain Modeling

Resting-state functional connectivity matrices derived from rs-fMRI serve as primary inputs for [[whole-brain-modeling]] frameworks such as [[the-virtual-brain]]. In this workflow, an empirical connectivity matrix—typically obtained from correlation or partial correlation of rs-fMRI time courses—defines the structural coupling strength between brain regions in a neural mass model. The [[wong-wang-model]] and [[jansen-rit-model]] are commonly used neural mass formulations that can reproduce key features of empirical resting-state dynamics, including the emergence of frequency-specific connectivity patterns and simulated BOLD signals.

The integration of rs-fMRI with [[structural-connectivity]] from diffusion tensor imaging (DTI) or probabilistic tractography enables hybrid modeling approaches that combine anatomical wiring with functional coupling. This combination is particularly powerful for clinical applications in [[epilepsy-modeling]] and [[alzheimers-modeling]], where empirical functional connectivity changes can be compared against model predictions to identify pathological mechanisms.

## Resting-State Versus Task-Based fMRI

A key distinction in functional neuroimaging is between [[resting-state-vs-task-fmri]] paradigms. While task-based fMRI provides superior temporal resolution for mapping brain function to specific cognitive operations, resting-state fMRI offers a standardized, reproducible approach that can be applied across clinical populations regardless of task performance ability. Resting-state paradigms are particularly advantageous for studies of consciousness, sedation, and developmental populations where task compliance is limited.

## Current Applications and Open Questions

Resting-state fMRI has revealed altered [[connectivity]] patterns in numerous neurological and psychiatric conditions, including Alzheimer's disease [[zhang-2016]], schizophrenia [[menon-2013]], major depression, and epilepsy. Biomarkers derived from resting-state connectivity show promise for differential diagnosis, treatment response prediction, and longitudinal disease monitoring. For example, connectivity changes in the default-mode network have been associated with treatment response in depression and schizophrenia, while altered interhemispheric synchronization patterns serve as biomarkers for early detection of epileptogenic zones.

However, several open questions remain regarding the physiological interpretation of functional connectivity—correlation does not imply direct anatomical connection, and the relationship between slow BOLD fluctuations and faster neural oscillations (as measured by [[eeg]] or [[meg]]) remains incompletely understood. Methodological considerations such as global signal regression, motion artifact mitigation, and test-retest reliability continue to be active areas of investigation, with reproducibility initiatives highlighting both the power and limitations of current approaches [[power-2014]].

Recent methodological developments address these limitations, including the development of [[dynamical-causal-modeling]] approaches that enable causal inference about effective connectivity, and hybrid [[neuroimaging-eeg]]/[[neuroimaging-meg]] studies that directly compare hemodynamic and electrophysiological resting-state networks. The field continues to advance toward standardized acquisition protocols, improved preprocessing pipelines (see [[fmriprep]]), and robust biomarker validation through large-scale reproducibility initiatives.