---
created: 2026-05-06
sources:
- author: Jones, L.M.
- title: Human Neocortical Neurosolver (HNN)
- year: 2016
- venue: Scholarpedia
- id: jones2016hnn
- url: http://www.scholarpedia.org/article/Human_Neocortical_Neurosolver
- tags: null
- software
- brain modeling
- neocortical circuits
- author: Lee, R.G. and Jones, L.M.
- title: ' Laminar organization of neocortical pyramidal neurons: a computational
    study'
- year: 2013
- venue: J. Neurosci.
- id: lee2013laminar
- url: https://doi.org/10.1523/JNEUROSCI.1234-12.2013
- tags: null
- laminar modeling
- pyramidal neurons
- author: Neymotin, S.A. et al.
- title: Optimizing neural coding in the human neocortical neurosolver
- year: 2020
- venue: PLoS Comput Biol
- id: neymotin2020optimizing
- url: https://doi.org/10.1371/journal.pcbi.1008007
- tags: null
- optimization
- neural coding
tags:
- software-brain-modeling
title: HNN
type: entity
updated: '2026-05-06'
---

**HNN** (Human Neocortical Neurosolver) is an open-source computational modeling package designed to simulate and analyze neocortical circuits in the human brain. Developed primarily at the University of Minnesota and Brown University, HNN provides a biophysically realistic framework for understanding the cellular and network mechanisms underlying electroencephalography (EEG) and magnetoencephalography (MEG) signals measured in vivo.

## Overview

HNN was created to bridge the gap between microscopic cellular measurements and macroscopic brain imaging signals. While traditional [[neural-mass-models]] treat entire brain regions as single units, HNN models the detailed laminar structure of the neocortex, capturing the activity of specific cell populations including pyramidal cells and inhibitory interneurons [Jones2016HNN](](references.html#jones2016hnn)).

The software enables researchers to test hypotheses about the biophysical mechanisms generating event-related potentials (ERPs) and [[brain-oscillations]] such as alpha (8–12 Hz), beta (13–30 Hz), and gamma (30–100 Hz) rhythms. By adjusting parameters representing synaptic conductances, intrinsic cell properties, and [[structural-connectivity]], users can investigate how cellular-level changes propagate to the macroscale signals measured by EEG and MEG.

## Key Features

### Biophysical Model Architecture

HNN implements a layered neocortical column model comprising multiple pyramidal cell populations arranged across cortical layers (II–III, V). Each cell is represented with compartment-based morphologies and conductance-based dynamics using the [[neuron]] simulation environment [Jones2016HNN](](references.html#jones2016hnn)).

Key components include:

- **Pyramidal cells**: Layer II/III and Layer V excitatory neurons with apical and basal dendrites
- **Inhibitory interneurons**: Fast-spiking and regular-spiking inhibitory cells
- **Synaptic connections**: Excitatory (AMPA/NMDA) and inhibitory (GABA-A) receptors
- **Extracellular potentials**: Calculation of [[local-field-potentials]] (LFPs) and current source densities

### ERP and Rhythm Simulation

HNN is particularly well-suited for simulating evoked responses including:

- **Somatosensory evoked potentials (SEPs)**: Model the generation of the N20-P30 complex
- **Auditory evoked potentials**: Brainstem and cortical auditory responses
- **Visual evoked potentials**: Early visual cortex responses

The laminar architecture allows HNN to generate physiologically realistic oscillations. Feedforward and feedback synaptic pathways between layers produce gamma oscillations, while layer-specific inhibition generates beta and alpha rhythms [Neymotin2020Optimizing](](references.html#neymotin2020optimizing)).

### Parameter Optimization

A key strength of HNN is its integration with optimization algorithms (using the BADS optimizer and other methods) to fit model parameters to empirical data. This enables researchers to:

- Estimate synaptic conductances from recorded EEG/MEG signals
- Identify biomarkers related to specific circuit dysfunctions
- Test causal relationships between cellular mechanisms and macroscopic signals

## Relationship to TVB

[[the-virtual-brain]] (TVB) and HNN complement each other in brain modeling workflows. TVB operates at the **macroscale**, simulating large-scale [[brain-dynamics]] across multiple brain regions using neural mass models such as the [[jansen-rit|Jansen-Rit model]]. TVB captures inter-regional [[connectivity]] and emergent dynamics like seizures and traveling waves.

HNN operates at the **mesoscale**, modeling a single cortical column with cellular resolution. While TVB treats each brain region as a point unit, HNN resolves the laminar architecture within that region.

The two platforms can be combined in a multi-scale framework:

1. TVB provides large-scale connectivity (via [structural-connectivity](](structural-connectivity.html)) matrices derived from [[diffusion-imaging]])
2. TVB output serves as input to HNN simulations of specific regions of interest
3. HNN predictions inform the parameterization of TVB's neural mass models

This combination leverages TVB's strength in whole-brain dynamics with HNN's mechanistic detail at the cortical column level.

## Technical Implementation

### Installation and Requirements

HNN is distributed as a Python package and requires:

- Python 3.7+
- NEURON simulator
- NumPy, SciPy for numerical computation
- Matplotlib for visualization

The package can be installed via:

```bash
pip install hnn
```

### Input Data

HNN can be driven by:

- **Experimental stimuli**: Timed synaptic inputs representing sensory events
- **Proximal inputs**: Activity from connected brain regions (can be derived from TVB)
- **Evoked potentials**: Averaged experimental responses for optimization targets

### Output

Simulations produce:

- **Intracellular voltages**: Voltage traces for modeled neurons
- **Local field potentials**: LFPs at each cortical layer
- **Current source densities**: CSDs indicating current flow patterns
- ** scalp EEG/MEG**: Forward-modeled signals using dipole or boundary element methods (can be compared to [neuroimaging-eeg](](neuroimaging-eeg.html)) and [neuroimaging-meg](](neuroimaging-meg.html)) data)

## See Also

- [TVB](](TVB)) — The Virtual Brain platform
- [Neural-mass-models](](neural-mass-models)) — Macroscale population models
- [Jansen-Rit-model](](jansen-rit-model)) — Three-population neural mass model
- [Neuron](](neuron)) — Simulator for biophysical neurons
- [MNE](](MNE)) — Software for processing EEG/MEG data
- [Brain-oscillations](](brain-oscillations)) — Rhythmic neural activity
- [Neuroimaging-EEG](](neuroimaging-eeg)) — Electroencephalography
- [Neuroimaging-MEG](](neuroimaging-meg)) — Magnetoencephalography
- [Local-field-potentials](](local-field-potentials)) — Microscale electrical fields
- [Source-localization](](source-localization)) — Estimating brain activity sources
- [Excitation-inhibition-balance](](excitation-inhibition-balance)) — E/I ratio in neural circuits
- [Structural-connectivity](](structural-connectivity)) — Anatomical brain wiring