---
created: 2026-05-06
sources:
- raw/papers/power-2011.md
- raw/papers/smith-2013-hcp.md
- raw/papers/arxiv-2602.03240.md
- raw/papers/anticevic-2012.md
tags:
- neuroimaging-fmri
- resting-state
- task-fmri
- functional-connectivity
- experimental-design
title: Resting-State vs Task fMRI
type: comparison
updated: '2026-05-07'
---

# Resting-State vs. Task fMRI

[[resting-state]] and task-based [[fmri]] are the two dominant paradigms for studying brain function with [[bold-signal|BOLD]] imaging. They provide complementary information about brain organization and are both critical for constraining and validating [[whole-brain modeling]] approaches like [[the-virtual-brain]].

## Overview

| Feature | Resting-State fMRI | Task fMRI |
|---------|-------------------|-----------|
| **Participant instruction** | "Lie still, don't think of anything in particular" | "Perform the task (e.g., press button when you see X)" |
| **Brain state** | Spontaneous, intrinsic activity | Evoked, stimulus-driven activity |
| **Analysis focus** | Connectivity, network architecture | Activation maps, response amplitudes |
| **Control** | Minimal experimental control | Strong experimental control via block/event design |
| **Reproducibility** | High across sessions (~0.7 test-retest for connectivity) | Moderate (task-dependent) |
| **Scan duration** | Typically 5-10 minutes | Varies (2-30 minutes depending on task) |
| **Clinical utility** | High (no patient cooperation needed) | Moderate (requires task compliance) |

## Resting-State fMRI

Resting-state fMRI measures spontaneous low-frequency fluctuations in the BOLD signal while participants lie awake but perform no explicit task.

**Key findings:**
- Stable, reproducible networks emerge consistently: default mode, salience, frontoparietal, visual, motor, dorsal attention, limbic
- These networks reflect intrinsic functional organization, not task-specific co-activation
- [[connectivity]] strength correlates with [[structural-connectivity]] derived from DTI [[tractography]]
- Individual connectivity fingerprints are highly stable, enabling [[connectome]]-based identification

**Strengths:**
- Minimal participant burden (scalable to clinical populations)
- Reveals intrinsic network architecture without task confounds
- Enables connectivity-based biomarkers for disease
- Data from thousands of subjects publicly available ([[abide]], HCP, [[uk-biobank]])

**Limitations:**
- Cannot localize specific cognitive functions to regions
- Susceptible to head motion, physiological noise, drowsiness
- Interpretation of "[[rest]]" is heterogeneous across subjects
- Cannot dissociate activity from connectivity

**TVB relevance:** Resting-state [[functional-connectivity]] is the primary empirical constraint for TVB simulations. TVB models are optimized to reproduce the correlation structure observed during rest.

## Task fMRI

Task fMRI measures BOLD signal changes evoked by controlled experimental manipulations, enabling localization of brain functions.

**Common designs:**
- **Block designs**: Extended periods of task vs. rest (high power, low temporal precision)
- **Event-related designs**: Brief stimuli separated by jittered inter-stimulus intervals (good for overlapping responses)
- **Mixed designs**: Combining blocked and event-related components

**Key findings:**
- Task-evoked responses are well-localized to specific brain regions
- Cognitive networks show task-dependent reconfiguration
- Activation amplitudes correlate with behavioral performance
- Habituation and adaptation effects reveal dynamic neural coding

**Strengths:**
- Strong causal inference (experimental control)
- Direct mapping of cognitive functions to brain regions
- Can study specific cognitive processes (attention, memory, language, etc.)
- Enables hypothesis-driven neuroscience

**Limitations:**
- Requires task compliance (difficult in clinical populations)
- Task-evoked activity reflects both stimulus-driven and intrinsic dynamics
- Cannot directly measure connectivity without specialized designs
- Practice effects and fatigue confound longitudinal studies

**TVB relevance:** Task fMRI provides empirical constraints on how brain networks reconfigure during cognitive demands. TVB can simulate task-evoked responses by modulating local parameters, and task data validate model predictions.

## Complementary Roles in Whole-Brain Modeling

| Goal | Resting-State Data | Task Data | Combined |
|------|-------------------|-----------|----------|
| Connectivity calibration | ✅ Primary input | ⚠️ Requires specialized designs | ✅ Best |
| Model validation | ✅ Correlation matrix | ✅ Task-evoked trajectories | ✅ Best |
| Individual fingerprinting | ✅ Highly stable | ⚠️ Variable across tasks | ✅ Most stable |
| Clinical biomarker | ✅ Scalable | ⚠️ Compliance issues | ✅ Most robust |
| Cognitive function mapping | ❌ Cannot localize | ✅ Direct mapping | ✅ Best |

## Integration with TVB

The optimal TVB workflow uses both:
1. **Resting-state** provides the baseline connectivity matrix that TVB simulates
2. **Task fMRI** provides the dynamic response patterns TVB must reproduce

By comparing TVB's simulated task responses against empirical task fMRI, researchers can validate and refine model parameters. This two-step approach has been used to:
- Calibrate TVB's structural connectivity weights using resting-state FC
- Validate TVB's ability to reproduce task-evoked BOLD changes
- Discriminate healthy [[aging]] from neurodegeneration via model parameter differences

## Software Ecosystem

- [[fsl]] — FEAT for task analysis, melodic for resting-state ICA
- [[spm]] — GLM for task analysis, DCM for connectivity
- [[nilearn]] — Python-based connectivity and decoding
- [[tvb]] — Simulates resting-state and task dynamics given connectivity

## References

- Biswal et al. (1995) — Original resting-state fMRI connectivity paper
- Raichle et al. (2001) — [[default-mode-network]] discovery
- Deco et al. (2011) — Resting-state connectivity constraining TVB models
- Smith et al. (2013) — Resting-state fMRI in the [[human-connectome-project]]