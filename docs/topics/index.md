# Browse by Topic

Explore the wiki organized by research area rather than content type.

---

## :fontawesome-solid-brain: Neuroimaging

Techniques for measuring brain structure and function.

| Modality | Description |
|----------|-------------|
| [fMRI](../concepts/fmri.md) | Functional magnetic resonance imaging |
| [EEG](../concepts/eeg.md) | Electroencephalography |
| [MEG](../concepts/meg.md) | Magnetoencephalography |
| [DTI](../concepts/dti.md) | Diffusion Tensor Imaging |
| [Diffusion MRI](../concepts/diffusion-mri.md) | Structural connectivity from diffusion imaging |
| [BOLD Signal](../concepts/bold-signal.md) | Blood oxygen level-dependent contrast |

**Related:** [Resting-state](../concepts/resting-state.md) | [Tractography](../concepts/tractography.md)

---

## :fontawesome-solid-network-wired: Connectivity & Networks

Brain connectivity concepts and network analysis.

| Concept | Description |
|---------|-------------|
| [Connectome](../concepts/connectome.md) | Complete structural description of brain connectivity |
| [Structural Connectivity](../concepts/structural-connectivity.md) | Physical white matter connections |
| [Functional Connectivity](../concepts/functional-connectivity.md) | Statistical dependencies between regions |
| [Effective Connectivity](../concepts/effective-connectivity.md) | Causal influence between regions |
| [Graph Theory](../concepts/graph-theory.md) | Mathematical framework for network analysis |
| [Modularity](../concepts/modularity.md) | Network community structure |

**Network Properties:** [Small-world](../concepts/small-world-networks.md) | [Scale-free](../concepts/scale-free-networks.md) | [Rich Club](../concepts/rich-club.md) | [Network Hubs](../concepts/network-hubs.md) | [Structural Core](../concepts/structural-core.md)

---

## :fontawesome-solid-calculator: Neural Mass Models

Population-level brain dynamics models.

### Classic Models
| Model | Populations | Primary Use |
|-------|-------------|-------------|
| [Wilson-Cowan](../concepts/wilson-cowan.md) | 2 (E, I) | General firing-rate dynamics |
| [Jansen-Rit](../concepts/jansen-rit.md) | 3 (P, E, I) | EEG/MEG generation |

### TVB Model Library
| Model | Dim | Best For |
|-------|-----|----------|
| [Epileptor](../concepts/epileptor.md) | 6D | Seizure dynamics |
| [Wong-Wang](../concepts/wong-wang.md) | 1D | fMRI/BOLD |
| [Larter-Breakspear](../concepts/larter-breakspear.md) | 3D | Ion channel dynamics |
| [Zerlaut](../concepts/zerlaut.md) | 2D+adapt | Adaptation effects |
| [Stefanescu-Jirsa](../concepts/stefanescu-jirsa.md) | 2D | Reduced seizures |

[See all neural mass models →](../concepts/neural-mass-model.md)

---

## :fontawesome-solid-square-root-variable: Mathematics & Dynamics

Theoretical foundations for brain modeling.

| Area | Key Concepts |
|------|--------------|
| **Dynamical Systems** | [Dynamical Systems Theory](../concepts/dynamical-systems-theory.md) · [Nonlinear Dynamics](../concepts/nonlinear-dynamics.md) · [Bifurcation Theory](../concepts/bifurcation-theory.md) · [Bifurcation Analysis](../concepts/bifurcation-analysis.md) |
| **Stochastic Methods** | [Stochastic Differential Equations](../concepts/stochastic-differential-equations.md) · [Fokker-Planck Equation](../concepts/fokker-planck-equation.md) · [Mean Field Theory](../concepts/mean-field-theory.md) |
| **Bayesian Methods** | [Variational Bayes](../concepts/variational-bayes.md) · [Free Energy Principle](../concepts/free-energy-principle.md) · [Dynamic Causal Modeling](../concepts/dynamic-causal-modeling.md) |

---

## :fontawesome-solid-laptop-code: Software & Tools

Platforms and tools for brain simulation and analysis.

### Simulation Platforms
| Platform | Description |
|----------|-------------|
| [TVB](../entities/tvb.md) | Whole-brain network simulation with neural mass models |
| [NEST](../entities/nest.md) | Spiking neural network simulator |
| [NEURON](../entities/neuron.md) | Multi-compartment neuron modeling |

**Compare:** [TVB vs NEST vs NEURON](../comparisons/tvb-vs-nest-vs-neuron.md)

### Major Datasets
- [Human Connectome Project](../entities/human-connectome-project.md)
- [UK Biobank](../entities/uk-biobank.md)

### Preprocessing Tools
- [ANTs](../entities/ants.md) — Image registration
- [FreeSurfer](../entities/freesurfer.md) — Cortical reconstruction
- [C-PAC](../entities/c-pac.md) — Connectome pipelines

[See all software →](../entities/index.md)

---

## :fontawesome-solid-hospital: Clinical Applications

Computational modeling for clinical neuroscience.

| Application | Description |
|-------------|-------------|
| [Epilepsy Modeling](../concepts/epilepsy-modeling.md) | Seizure dynamics and prediction |
| [Personalized Brain Modeling](../concepts/personalized-brain-modeling.md) | Subject-specific simulations |
| [The Virtual Epileptic Brain](../entities/the-virtual-epileptic-brain.md) | Clinical brain simulation platform |

**Key Models:** [Epileptor](../concepts/epileptor.md) · [EpileptorCodim3](../concepts/epileptorcodim3.md) · [EpileptorRS](../concepts/epileptor-rs.md)

---

## :fontawesome-solid-baby: Development

Brain development across the lifespan.

- [Neurodevelopment](../concepts/neurodevelopment.md) — Processes of nervous system growth
- [Developmental Trajectories](../concepts/developmental-trajectories.md) — Patterns of brain change
- [Default Mode Network](../concepts/default-mode-network.md) — Network development

**Researchers:** [Nitin Gogtay](../entities/nitin-gogtay.md) — Longitudinal cortical development

---

## :fontawesome-solid-person-cane: Aging

Brain aging and cognitive decline.

- [Aging](../concepts/aging.md) — Structural and functional changes
- [Brain Maintenance](../concepts/brain-maintenance.md) — Preserving brain structure
- [Cognitive Reserve](../concepts/cognitive-reserve.md) — Protective factors

**Researchers:** [Nancy Andrews-Hanna](../entities/nancy-andrews-hanna.md) — DMN and aging

---

## Browse by Type Instead

- [**All Concepts**](../concepts/index.md) — 59 theoretical and methodological topics
- [**All Entities**](../entities/index.md) — 124 software, people, and datasets
- [**All Comparisons**](../comparisons/index.md) — Side-by-side analyses
- [**Full Catalog**](../catalog.md) — Complete alphabetical listing
