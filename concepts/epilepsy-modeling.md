---
created: 2026-04-20
sources:
- raw/papers/wendling-2002.md
- raw/papers/breakspear-2006.md
- raw/papers/touboul-2011.md
- raw/papers/breakspear-2017.md
- raw/papers/semanticscholar-7733d5476149.md
- raw/papers/semanticscholar-26be4473893d.md
- raw/papers/arxiv-2601.21478.md
- raw/papers/semanticscholar-cc2129666e15.md
- raw/papers/arxiv-2603.25991.md
tags:
- epilepsy-modeling
- neural-mass-models
- bifurcation-analysis
- brain-oscillations
title: Epilepsy Modeling
type: concept
updated: '2026-04-23'
---

# Epilepsy Modeling

Computational modeling of epilepsy uses neural mass models and dynamical systems theory to understand seizure generation, propagation, and termination. These models bridge clinical observations with underlying neurophysiology.

## Overview

Epilepsy modeling aims to:
- Understand mechanisms of seizure onset and offset
- Predict seizure occurrence and spread
- Design stimulation protocols for seizure control
- Personalize treatment through patient-specific models

## Seizure Dynamics as Bifurcations

### Core Insight

Seizures are viewed as transitions between dynamical regimes through bifurcations—qualitative changes in system behavior as parameters vary.

### Key Bifurcations in Seizure Models

| Bifurcation | Seizure Type | Characteristics |
|-------------|--------------|-----------------|
| Saddle-Node on Invariant Circle (SNIC) | Tonic onset | Gradual frequency increase |
| Andronov-Hopf | Spike-wave | Sudden onset with fixed frequency |
| Saddle-Homoclinic | Tonic-clonic | High-frequency onset |
| Torus | Absence | 3 Hz spike-wave |

## Neural Mass Models for Epilepsy

### Jansen-Rit Extensions

The standard Jansen-Rit model produces seizure-like activity when:
- Excitation/inhibition ratio increases
- Inhibitory time constants change
- External input increases

Parameter changes create bifurcations to high-amplitude oscillatory states.

### Wendling Model (4-population)

Critical extension for epilepsy modeling:
- Population 1: Pyramidal cells
- Population 2: Excitatory interneurons
- Population 3: Slow inhibitory interneurons (GABA-B)
- Population 4: Fast inhibitory interneurons (GABA-A)

**Key feature**: Separate fast and slow inhibition captures:
- Interictal spikes (fast inhibition dominant)
- Fast activity during seizures (fast inhibition blocked)
- Slow spike-wave (slow inhibition dominant)

### Breakspear Spatial Model

Extension to large-scale networks:
- Spatially distributed Jansen-Rit columns
- Coupled via anatomical connectivity
- Captures seizure propagation across cortex

## Seizure Types Modeled

### Focal Seizures

**Mechanism**: Local parameter changes trigger activity that spreads via network connections.

Model features:
- Heterogeneous excitability across regions
- Seizure focus with lowered threshold
- Propagation determined by connectivity

### Generalized Seizures

**Mechanism**: Global parameter changes affect entire network simultaneously.

Types:
- **Absence (petit mal)**: 3 Hz spike-wave via torus bifurcation
- **Tonic-clonic**: SNIC bifurcation with rapid onset

### Status Epilepticus

**Mechanism**: Sustained high excitability preventing normal return to baseline.

Modeled as:
- Stable high-amplitude limit cycle
- Bistability with seizure state as attractor

## Parameter Sensitivity and Personalization

### Critical Parameters

| Parameter | Effect | Variability |
|-----------|--------|-------------|
| Excitatory gain | Threshold for seizures | Patient-specific |
| Inhibitory gain | Seizure termination | May be reduced in epilepsy |
| Time constants | Oscillation frequency | Pathological changes |
| Connectivity | Propagation patterns | Individual anatomy |

### Patient-Specific Modeling

**Approach in TVB**:
1. Individual structural connectivity (DTI tractography)
2. Personalized neural mass parameters
3. Simulation of seizure dynamics
4. Validation against clinical EEG/ECoG

## Clinical Applications

### Seizure Prediction

**Challenge**: Identifying pre-ictal state from inter-ictal recordings.

**Model-based approaches**:
- Tracking slow parameter changes
- Detecting approach to bifurcation
- Machine learning on model features

### Surgical Planning

**Application**: Identifying optimal resection zones.

**Model contribution**:
- Simulating effect of removing regions
- Predicting post-surgical seizure freedom
- Identifying hidden epileptic networks

### Stimulation Protocols

**Closed-loop control**:
- Detect seizure onset from model state
- Deliver targeted stimulation
- Push system away from seizure attractor

## Theoretical Insights

### Seizure Threshold

The concept of a "seizure threshold" maps to bifurcation boundaries in parameter space:
- Below threshold: Stable resting state
- At threshold: Bifurcation to oscillatory state
- Above threshold: Sustained seizure activity

### Multistability

Some models exhibit:
- **Resting state**: Low activity fixed point
- **Inter-ictal**: Small oscillations or noise
- **Ictal**: High-amplitude limit cycle

Explains why identical stimuli may or may not trigger seizures.

### Network Effects

Seizure dynamics depend on:
- Local excitability (node properties)
- Network connectivity (edge properties)
- Time delays (propagation speed)

## Limitations

1. **Simplified neurons**: No ion channel detail
2. **Fixed connectivity**: No plasticity during seizure
3. **Parameter identifiability**: Many parameter combinations give similar dynamics
4. **Validation**: Difficult to measure all parameters in vivo

## Related Concepts

- [[neural mass model]] – Model framework
- [[Jansen-Rit]] – Base model for extensions
- [[bifurcation analysis]] – Mathematical foundation
- [[whole brain]] – Large-scale seizure propagation
- [[eeg]] – Clinical validation signal