---
title: Whole-brain modeling
created: 2026-04-20
updated: 2026-04-27
type: concept
tags: [whole-brain-modeling, connectomics, neural-mass-models, network-dynamics, computational-neuroscience, structural-connectivity, functional-connectivity, brain-network, personalized-brain-modeling, dynamical-systems-theory]
sources: [raw/papers/breakspear-2017.md, raw/papers/semanticscholar-ce89e593c89e.md, raw/papers/arxiv-2504.17491.md]
---

# Whole-brain modeling

Whole-brain modeling is a computational neuroscience approach that represents the entire brain as a network of coupled dynamical systems, where each node corresponds to a brain region and connections are derived from empirical [[structural connectivity]] data. This framework enables researchers to investigate how anatomical substrate—measured noninvasive via [[diffusion-mri]] and [[tractography]]—gives rise to functional brain dynamics observable in [[fmri]], [[eeg]], or [[meg]] recordings. By treating the brain as a coupled oscillator network or neural mass model, whole-brain modeling bridges the gap between [[connectome]]-level anatomy and emergent spatiotemporal patterns of activity that subtend cognition, behavior, and clinical dysfunction.

## Conceptual Foundations

The foundational premise of whole-brain modeling is that the brain's large-scale organization can be understood through the interaction of distributed neuronal populations, each governed by local dynamics that couple to peer populations via white-matter pathways. This approach emerged from the convergence of several lines of research: the development of [[neural mass model]] formulations that reduce the dynamics of cortical columns to couple differential equations; advances in diffusion tensor imaging that enabled reconstruction of [[structural connectivity]] matrices; and the application of [[dynamical-systems-theory]] to characterize network-level phenomena such as oscillations, synchronization, and bifurcations.

At its core, a whole-brain model consists of $N$ brain regions (typically $N \approx 68-500$ depending on the [[parcellation]] scheme) where each region's state evolves according to a local dynamical system. These regional dynamics are then coupled through a connectivity matrix $C_{ij}$ encoding the strength or presence of anatomical pathways between regions $i$ and $j$. The mathematical formulation can be expressed as a system of coupled differential equations:

$$\frac{d\mathbf{x}_i}{dt} = \mathbf{F}_i(\mathbf{x}_i) + \sum_{j=1}^{N} C_{ij} \mathbf{G}(\mathbf{x}_j, \mathbf{x}_i)$$

where $\mathbf{x}_i$ is the state vector for region $i$, $\mathbf{F}_i$ characterizes local dynamics, and $\mathbf{G}$ specifies the coupling function. The coupling matrix $C_{ij}$ is typically derived from tractography-based reconstructions of the human [[connectome]], such as those provided by the [[human-connectome-project]] or [[uk-biobank]] datasets.

## Taxonomic Diversity of Whole-brain Models

Whole-brain models span a spectrum of complexity, reflecting different levels of biological realism and computational tractability. At one end lie **neural mass models** such as the [[jansen-rit]] model or its extensions (including the [[wong-wang]] and [[larter-breakspear]] variants), which represent cortical regions as populations of excitatory and inhibitory neurons coupled through mean-field approximations. These models can reproduce key features of [[brain-oscillations]] across frequency bands and have proven valuable for understanding the mechanistic basis of [[functional connectivity]] patterns observed in resting-state [[fmri]].

Phenomenological models such as the [[wilson-cowan]] equation offer a simpler alternative, representing regional dynamics through coupled nonlinear differential equations that capture the interaction between excitation and inhibition without detailed neuronal circuitry. These models are computationally efficient and facilitate analytical treatment of network dynamics, including [[bifurcation-analysis]] that reveals how the system transitions between qualitatively different dynamical regimes.

More biophysically detailed approaches incorporate spiking neuron models (as in the [[epileptor]] model for [[epilepsy-modeling]]) or conductance-based formulations that simulate the flow of ions through specific channel types. The choice of model granularity involves trade-offs between biological fidelity, analytical tractability, and computational cost—concerns that become particularly salient when fitting models to empirical data or exploring parameter spaces for [[parameter-estimation]].

## Hierarchical and Multi-scale Extensions

Recent advances have moved beyond monolithic regional representations to incorporate hierarchical structure within brain regions. The hierarchical [[kuramoto]] model exemplifies this approach, embedding multiple coupled oscillators within each node to capture both local synchronization dynamics and long-distance interareal interactions. This framework has proven particularly valuable for investigating **critical brain dynamics**—the hypothesis that the brain operates near a critical point between order and disorder, thereby optimizing information processing through long-range temporal correlations.

Multi-scale whole-brain modeling also encompasses phenomena such as the **structure-function coupling**, where the relationship between anatomical connectivity and functional connectivity varies across frequency bands and cognitive states. Research using the hierarchical approach has revealed that this coupling peaks at criticality for long-range temporal correlations and cross-correlations, while decaying for phase synchronization measures—patterns that align with empirical observations from resting-state [[meg]] recordings.

## Clinical and Translational Applications

Whole-brain modeling has emerged as a powerful tool for clinical translation, enabling personalized brain modeling that integrates patient-specific structural connectivity data. This approach is particularly developed in the context of [[epilepsy-modeling]], where the [[epileptor]] model and related formalisms can predict seizure propagation patterns and inform surgical planning. Similarly, whole-brain frameworks have been applied to [[schizophrenia-models]] and [[alzheimers-modeling]], investigating how structural alterations propagate through the network to produce observed functional disturbances.

The [[the-virtual-brain]] (TVB) platform represents the most widely adopted software ecosystem for whole-brain simulation, providing an integrated environment for constructing, fitting, and analyzing personalized brain models. TVB supports multiple neural mass formulations, connects to diverse neuroimaging datasets, and includes tools for simulating [[brain-stimulation]] interventions—capabilities that have enabled investigations into optimal targeting for transcranial magnetic stimulation and deep brain stimulation.

## Open Questions and Future Directions

Despite substantial progress, fundamental challenges remain. The relationship between model complexity and explanatory power remains debated: do more biophysically detailed models yield superior predictions, or do phenomenological frameworks capture essential dynamics more parsimoniously? How sensitive are conclusions to [[parcellation]] choice, tractography algorithm, and parameter fitting procedures—and to what extent do observed phenomena reflect genuine biophysical mechanisms versus modeling artifacts? Recent systematic comparisons across [[parcellation]] resolutions suggest that while coarse-grained models can capture dominant dynamical features, fine-scale features may be resolution-dependent.

Future directions include the integration of [[effective-connectivity]] frameworks (including [[dynamic-causal-modeling]]) to distinguish direct anatomical effects from causal functional interactions; incorporation of [[neurodevelopment]] trajectories to model how structural connectivity sculpts functional dynamics across the lifespan; and extension to [[brain-stimulation]] paradigms that combine whole-brain models with biophysical models of current flow. As computational resources expand and [[openneuro]] and related repositories provide increasingly large multimodal datasets, whole-brain modeling is poised to become an indispensable tool for bridging cellular-level neuroscience with systems-level cognition and clinical translation.

## Related Concepts

* [[neural mass model]]
* [[structural connectivity]]
* [[functional connectivity]]
* [[connectome]]
* [[brain-network]]
* [[dynamic causal modeling]]
* [[the-virtual-brain]]
* [[epilepsy modeling]]
* [[bifurcation analysis]]
* [[personalized brain modeling]]