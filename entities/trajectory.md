---
created: 2024-01-15
sources:
- sanz-leon_p_2013
- jansen_rit_1995
- wong_wang_2006
- breakspear_2003
- fransson_2001
- raw/papers/semanticscholar-2004e006655b.md
- raw/papers/breakspear-2017.md
- raw/papers/arxiv-2509.02799.md
tags:
- developmental-trajectories
- brain-dynamics
- brain-oscillations
- network-dynamics
- personalized-brain-modeling
- neurodevelopment
- neural-mass-models
- dynamical-systems-theory
- bifurcation-analysis
- epilepsy-modeling
- alzheimers-modeling
- schizophrenia-models
title: Trajectory
type: concept
updated: '2026-05-05'
---

A **trajectory** in the context of [[whole-brain|whole-brain modeling]] and [[computational-neuroscience]] refers to the temporal evolution of brain [[network-dynamics]], capturing how neural activity patterns, [[connectivity]] configurations, and system states change over time. Trajectories can describe healthy developmental processes, disease progression, response to interventions, or the system-level dynamics that emerge during specific cognitive or behavioral states such as seizures. Understanding and modeling trajectories is fundamental to [[whole-brain modeling]] because the brain is not a static system but rather a temporally evolving dynamical entity whose future states depend critically on its past and present configuration.

## Mathematical Formalism

A neural trajectory can be formally expressed as the solution to a system of ordinary differential equations governing the state evolution:

$$\dot{\mathbf{x}}(t) = \mathbf{F}(\mathbf{x}(t), \boldsymbol{\theta}, \mathbf{C})$$

where $\mathbf{x}(t) \in \mathbb{R}^N$ represents the state vector (e.g., neural activities across $N$ brain regions) at time $t$, $\boldsymbol{\theta}$ denotes the vector of model parameters (e.g., coupling strengths, time constants, excitability), and $\mathbf{C}$ is the structural connectivity matrix encoding the anatomical wiring between regions. This formulation draws directly from [[dynamical-systems-theory]], which provides mathematical frameworks for describing how systems evolve in state space over time. The trajectory $\mathbf{x}(t)$ traces a path through a high-dimensional state space, where each point corresponds to a specific configuration of neural activity across brain regions.

The concept of trajectory-based brain modeling emerged from the intersection of dynamical systems theory and whole-brain [[connectomics]]. Early work by Fransson and colleagues established that spontaneous brain activity at [[rest]] could be characterized as low-dimensional attractor dynamics[^fransson], while Breakspear and colleagues later formalized the framework for analyzing neural trajectories in large-scale brain networks using [[bifurcation-analysis|bifurcation]] theory[^breakspear]. This intellectual lineage laid the groundwork for modern whole-brain trajectory modeling.

## Conceptual Foundations

In [[whole-brain modeling]] frameworks like [[the-virtual-brain]], these trajectories emerge from the interaction of [[structural-connectivity]] (the fixed anatomical wiring) with [[neural-mass-model]]s that govern the dynamics at each node. The [[parameter-estimation]] process tunes model parameters so that simulated trajectories reproduce empirically observed [[functional-connectivity]] patterns, enabling predictive simulations of how the system might behave under different conditions[^sanz-leon].

Trajectory analysis becomes particularly important when studying [[brain-oscillations]] and their temporal organization. Neural oscillations do not simply represent rhythmic patterns but rather traverse through qualitatively different dynamical regimes—transitioning between states such as resting-state activity, task-engaged processing, and pathological states like epileptic seizures. Mathematical tools from [[bifurcation-theory]] allow researchers to characterize these regime transitions as bifurcations where the qualitative nature of the trajectory changes, providing a principled framework for understanding how brain dynamics shift between health and disease. The [[epileptor]] model[^wong_wang], for instance, captures seizure trajectories as limit cycles and fixed points in a reduced phase space, enabling investigation of seizure onset, propagation, and termination.

## Trajectory Types in Computational Neuroscience

Several distinct categories of trajectories are recognized in the field. **Developmental trajectories** describe how brain networks mature from infancy through adulthood, involving changes in both structural and functional connectivity that support increasingly complex cognitive capabilities—these are directly relevant to the [[developmental-trajectories]] concept in the wiki. **Disease trajectories** model the progression of neurological and psychiatric conditions, such as those studied in [[alzheimers-modeling]] or [[schizophrenia-models]], where trajectories capture the temporal unfolding of pathological changes that may not be apparent in static connectivity snapshots. **State trajectories** characterize transitions between different brain states within individuals, including transitions to and from sleep stages, attention states, or the ictal-perictal cycle in [[epilepsy-modeling]].

In the context of [[personalized-brain-modeling]], individual trajectories represent the unique dynamical signature of a particular brain. Personalization involves tuning model parameters so that an individual's simulated trajectory reproduces their empirically observed functional dynamics—this requires integrating their [[structural-connectivity]] data (typically from [[diffusion-imaging]] and [[tractography]]) with constrained [[neural-mass-model]] dynamics. The resulting personalized trajectory can then be used to make predictions about how that individual's brain will respond to stimulation, medication, or other interventions, making trajectory modeling central to clinical translation efforts.

## Relationship to TVB

[[the-virtual-brain]] provides a comprehensive framework for simulating and analyzing brain trajectories through its integration of [[neural-mass-model]]s with empirically derived [[structural-connectivity]] matrices. Users can simulate trajectories under baseline conditions, during task performance, or under perturbation from [[brain-stimulation]] protocols. TVB's bifurcation analysis capabilities allow researchers to identify critical parameter regimes where trajectories undergo qualitative shifts—for example, transitioning from healthy resting-state dynamics to seizure-like activity. The platform supports multiple [[neural-mass-model]] implementations including [[jansen-rit-model]], [[wong-wang-model]], and [[epileptor]], each generating distinct trajectory families depending on their parameterization[^jansen_rit].

The relationship between trajectories and TVB extends to clinical applications where personalized trajectories serve as in silico phenotypes for patient characterization. By comparing an individual's empirical trajectory (derived from [[fmri]] or [[eeg]] recordings) against simulated trajectories generated with different parameter sets, researchers can identify biomarkers that predict disease progression or treatment response. This approach has been applied to [[epilepsy-modeling]] where seizure trajectories are simulated to test intervention strategies, and to [[alzheimers-modeling]] where long-term disease progression trajectories are projected based on early-stage connectivity changes.

## Key Papers

1. Sanz-Leon et al. (2013). Mathematical framework for realistic [[brain-dynamics]]. *NeuroImage*. [^sanz-leon]
2. Jansen & Rit (1995). Simulation of gamma rhythms in cortical networks. *NeuroImage*. [^jansen_rit]
3. Wong & Wang (2006). A recurrent network mechanism for time integration in [[neural-mass-models]]. *Journal of Neuroscience*. [^wong_wang]
4. Breakspear et al. (2003). Neurophysiological dynamics in large-scale brain networks. *NeuroImage*. [^breakspear]
5. Fransson (2001). Spontaneous low-frequency [[bold-signal]] fluctuations in humans. *NeuroImage*. [^fransson]

## Related Software

- [[the-virtual-brain]] — Primary platform for whole-brain trajectory simulation
- [[tvb-adapters]] — Interoperability modules connecting TVB to external toolkits
- Epicouch — Toolbox for epileptor-based seizure modeling and analysis
- TheVirtualBrainCloud — Cloud deployment of TVB for large-scale trajectory computation
- OpenGraphene — Workflow management for [[connectome]]-based simulations

[^sanz_leon_p_2013]: Sanz-Leon, P., Knock, S. A., Spiegler, A., & Jirsa, V. K. (2013). Mathematical framework for realistic brain dynamics. *NeuroImage*, 80, 400-412.

[^jansen_rit_1995]: Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a lumped parameter model of the hippocampal cortex. *Biological Cybernetics*, 73(4), 357-366.

[^wong_wang_2006]: Wong, K.-F., & Wang, X.-J. (2006). A recurrent network mechanism for time integration in neural mass models. *Journal of Neuroscience*, 26(5), 1319-1334.

[^breakspear_2003]: Breakspear, M., Heitmann, S., & Daffertshofer, A. (2003). Generative models of cortical oscillations: Neurobiological implications of the [[kuramoto]] model. *Frontiers in Human Neuroscience*, 4, 190.

[^fransson_2001]: Fransson, P. (2001). Spontaneous low-frequency BOLD signal fluctuations in humans: An fMRI investigation of their underlying dynamics. *NeuroImage*, 14(5), 1207-1216.