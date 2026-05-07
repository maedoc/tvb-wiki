---
created: 2026-04-20
sources:
- raw/papers/jansen-rit-1995.md
- raw/papers/rit-2013.md
- raw/papers/arxiv-2411.16449.md
tags:
- neural-mass-models
- neuroimaging-eeg
- neuroimaging-meg
- whole-brain-modeling
- bifurcation-analysis
- dynamical-systems-theory
- brain-oscillations
- computational-neuroscience
title: Jansen-Rit Model
type: concept
updated: '2026-05-07'
---

The [[jansen-rit|Jansen-Rit model]] is a [[neural-mass-models|neural mass model]] of a cortical column that generates realistic electroencephalogram (EEG) and magnetoencephalography (MEG) signals through the interaction of three neuronal populations. Originally developed by Benjamin H. Jansen and Vincent G. Rit in their seminal 1995 paper [@jansen-rit-1995], the model has become the default neural mass implementation in [[the-virtual-brain|TVB]] for [[whole-brain]] simulations [@rit-2013] and serves as a foundational framework for studying [[brain-oscillations]], evoked potentials, and pathological dynamics in disorders such as epilepsy.

## Model Architecture

The Jansen-Rit model represents a single cortical column containing three distinct neuronal populations that are mathematically coupled to produce macroscopic electrical activity. The first population consists of pyramidal cells, which receive excitatory input from interneurons and project to both interneuron populations as well as to distant cortical columns via long-range connections. Pyramidal cells constitute the primary source of the EEG/MEG signal because their aligned dendritic shafts produce measurable extracellular currents.

The second population comprises excitatory interneurons (glutamatergic), which receive synaptic input from the pyramidal population and provide feedback excitation. The third population consists of inhibitory interneurons (GABAergic), which similarly receive from pyramidal cells but impose negative feedback through GABAergic inhibition. This three-population architecture creates a recurrent loop where excitation and inhibition interact to generate oscillatory dynamics.

Each population is characterized by a static nonlinear activation function (typically sigmoidal) applied to the membrane potential, along with post-synaptic response functions that model the temporal dynamics of synaptic transmission. The original 1995 formulation used alpha-shaped impulse response functions [@jansen-rit-1995], which produce physiologically realistic oscillation frequencies in the alpha (8–12 Hz) and beta (13–30 Hz) bands under appropriate parameter regimes.

## Mathematical Formulation

The model dynamics are expressed as a system of second-order differential equations describing the evolution of postsynaptic potentials (PSPs) for each population. The standard formulation distinguishes between excitatory and inhibitory synaptic dynamics using separate time constants and amplitudes.

For each population $i \in \{pyramidal, excitatory, inhibitory\}$, the average membrane potential $v_i$ evolves according to a second-order system that can be written as two coupled first-order equations:

$$\frac{dv_i}{dt} = y_i$$

$$\frac{dy_i}{dt} = A \left( \frac{1}{\tau_e} + \frac{1}{\tau_i} \right) \left( \sum_{j} C_{ij} S(v_j) - \frac{v_i}{\tau_e} - \frac{y_i}{A} \right)$$

where $S(v)$ is the sigmoidal activation function:

$$S(v) = \frac{1}{1 + e^{r(v_0 - v)}}$$

In this formulation, $A$ is the amplitude parameter (typically $A = 2.5$ mV for excitatory PSPs and $A = -2.5$ mV for inhibitory PSPs), $\tau_e$ and $\tau_i$ are the excitatory and inhibitory time constants (typically $\tau_e = 10$ ms and $\tau_i = 20$ ms), $C_{ij}$ are [[connectivity]] constants representing the number of synapses from population $j$ to population $i$, $v_0$ is the threshold potential (typically $v_0 = 6$ mV), and $r$ is the slope of the sigmoid (typically $r = 0.56$ mV$^{-1}$).

The connectivity matrix for the three-population architecture is typically parameterized as follows: $C_{pyramidal \leftarrow excitatory} = 108$, $C_{pyramidal \leftarrow inhibitory} = 33.75$, $C_{excitatory \leftarrow pyramidal} = 108$, $C_{inhibitory \leftarrow pyramidal} = 108$, and $C_{self} = 1$ for each population.

The nonlinearity introduced by the sigmoid function creates the bistable dynamics that underlie transitions between resting states and oscillatory regimes. A critical feature of the model is its sensitivity to parameter variations. Small changes in the balance between excitation and inhibition can shift the system from steady-state dynamics through alpha oscillations to slower delta-range rhythms. Recent [[bifurcation-analysis]] [@arxiv-2411.16449] has shown that alpha-to-delta transitions occur via discontinuity-induced grazing bifurcations, where the minimum of the pyramidal cell output equals the threshold for switching off the excitatory interneuron population.

## Relationship to Other Neural Mass Models

The Jansen-Rit model extends earlier work by Lopes da Silva and colleagues, who developed thalamic models of alpha rhythm generation [@lopes-da-silva-1974]. While Lopes da Silva's approach emphasized thalamocortical loops, Jansen and Rit focused specifically on the cortical column as a self-contained oscillatory unit, making the model more directly applicable to whole-brain simulations where multiple cortical regions are coupled via anatomical [[structural-connectivity|structural connectivity]].

Compared to other [[neural-mass-models]] such as the [[wong-wang-model|Wong-Wang model]] or the [[wilson-cowan-model|Wilson-Cowan model]], the Jansen-Rit architecture provides more detailed mesoscopic dynamics with separate excitatory and inhibitory populations. This granularity enables more precise modeling of excitation-inhibition balance and makes the model particularly suitable for studying the effects of pharmacological agents or pathological conditions that differentially affect inhibitory versus excitatory transmission.

## Applications and Extensions

The model has been extended in numerous directions since its introduction. Multi-column implementations couple multiple Jansen-Rit units via delay-distance-dependent connectivity matrices derived from [[diffusion-imaging|diffusion MRI]] [[tractography]], forming the basis of large-scale whole-brain models in TVB [@rit-2013]. These coupled systems can reproduce [[resting-state]] networks and simulate how lesions or stimulation affects global [[brain-dynamics]].

Extensions to sleep modeling [@weigenand-2014] have demonstrated that the model can generate K-complexes and slow-wave oscillations characteristic of NREM sleep through a Hopf bifurcation mechanism. The model also serves as the foundation for the [[epileptor]] model of seizure dynamics, which embeds Jansen-Rit-like dynamics within a larger framework capable of reproducing ictal and interictal activity.

Pharmacological applications have explored how anesthetic agents affect the balance between excitation and inhibition, with the model successfully reproducing the characteristic spectral shifts observed under different anesthetic regimes. Studies using the model have also investigated the mechanisms underlying event-related potentials such as P300 and auditory evoked responses.

## Relationship to The Virtual Brain

The Jansen-Rit model is the default neural mass model in [[the-virtual-brain|TVB]] for EEG and MEG forward simulations. When users import structural connectivity matrices from DTI tractography and configure cortical brain regions, TVB instantiates one Jansen-Rit model per region, coupling them according to the anatomical weights. The model's relatively low computational cost (compared to spiking network simulations) enables whole-brain simulations at the scale of the human [[connectome]], making it ideal for clinical applications including presurgical mapping and personalized medicine.

The TVB implementation includes the full set of parameters from the original formulation, with default values tuned to produce alpha-band oscillations in the resting state. Users can modify synaptic gains ($A$), time constants ($\tau_e$, $\tau_i$), connectivity strengths ($C_{ij}$), and sigmoid parameters ($v_0$, $r$) to explore how changes in [[excitation-inhibition-balance]] affect [[network-dynamics]].

## Open Questions

Despite its widespread use, the Jansen-Rit model leaves several questions unresolved. The three-population architecture, while more detailed than single-population models, still abstracts away the heterogeneity of cortical [[neuron]] types. Recent work suggests that incorporating more realistic cellular diversity may be necessary to capture certain oscillation types, particularly gamma rhythms that require precise timing between specific interneuron subclasses.

[[parameter-estimation]] for personalized models remains challenging, as the model's many parameters cannot be uniquely determined from macroscopic signals alone. [[bayesian]] approaches and [[variational-bayes|variational inference]] methods are active areas of research for constraining model parameters using empirical EEG or [[fmri]] data. The relationship between the model's abstract "population" variables and underlying cellular mechanisms continues to be refined as more detailed models become computationally tractable.

## References

1. Benjamin H. Jansen, Vincent G. Rit. *Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns*. Biological Cybernetics. [DOI](](https://doi.org/10.1007/BF00199471))
2. Vincent G. Rit, Benjamin H. Jansen. *A neural mass model for the generation of electroencephalograms*. Critical Reviews in Biomedical Engineering.
3. Huda Mahdi, Jan Sieber, Krasimira Tsaneva-Atanasova. *Alpha-Delta Transitions in Cortical Rhythms as grazing bifurcations*. [Link](](https://arxiv.org/abs/2411.16449))