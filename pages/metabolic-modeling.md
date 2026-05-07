---
title: Metabolic Modeling
created: 2025-01-15
updated: 2026-05-07
type: concept
tags: [whole-brain-modeling, computational-neuroscience, neural-mass-models, neuroimaging-fmri, brain-network-dynamics, dynamical-systems-theory]
sources: [raw/papers/semanticscholar-ce89e593c89e.md, raw/papers/semanticscholar-9afbfd2d37be.md, raw/papers/arxiv-2509.02799.md]
---

Metabolic modeling in the context of whole-brain modeling refers to computational frameworks that incorporate the metabolic demands and energy constraints of neural activity into large-scale brain network simulations. This approach recognizes that neural signaling, particularly in the form of synchronized oscillations and network dynamics observed in neuroimaging data, relies on a continuous supply of glucose and oxygen, and that the blood-oxygen-level-dependent (BOLD) signal measured in functional magnetic resonance imaging (fMRI) provides an indirect readout of this metabolic activity [1]. By integrating metabolic constraints into whole-brain models, researchers can more accurately link the biophysical mechanisms of neural mass models to experimentally observed functional connectivity patterns, improve the biological realism of personalized brain digital twins, and develop predictive models of how metabolic dysfunction contributes to neurological and psychiatric disorders.

## Motivation and Context

Traditional whole-brain models, such as those implemented in [[the-virtual-brain]], couple neural mass models at regions defined by a parcellation and constrain these models by empirical structural connectivity derived from diffusion tensor imaging or tractography. While such models successfully reproduce key features of resting-state functional connectivity, including the formation of large-scale networks like the [[default-mode-network]], they often operate without explicit representation of the metabolic substrate that supports neural activity [2]. The BOLD signal upon which fMRI is based emerges from a complex cascade known as the [[hemodynamic-response-function]], which couples neural activity to changes in local cerebral blood flow, volume, and oxygenation through mechanisms including the balloon model and neurovascular coupling. Early work on the [[bold-model]] provided foundational mathematical descriptions of this relationship, but integrating these ideas into whole-brain modeling frameworks remains an active area of development [3].

The motivation for metabolic modeling in whole-brain contexts stems from several converging factors. First, personalized brain models for clinical applications increasingly aim to predict not only neural dynamics but also the metabolic consequences of targeted interventions such as [[brain-stimulation]] or pharmacological treatments. Second, evidence suggests that metabolic constraints may shape the parameter regimes accessible to whole-brain models, particularly regarding critical dynamics and the balance between excitation and inhibition that supports optimal information processing [1]. Third, hierarchical models of brain dynamics, such as the [[kuramoto]] model with multiple levels of coupling, may exhibit different synchronization properties when metabolic limits are incorporated as additional constraints or bifurcation parameters.

## Technical Foundations

Metabolic modeling in whole-brain frameworks draws on several theoretical and computational pillars. The [[fokker-planck-equation]] provides a mathematical framework for describing the evolution of probability distributions over neural state variables, which can be extended to include metabolic variables such as local glucose concentration or oxygen availability as state-dependent parameters. The Fokker-Planck equation takes the general form:

$$\frac{\partial P(x,t)}{\partial t} = -\frac{\partial}{\partial x}[A(x)P(x,t)] + \frac{\partial^2}{\partial x^2}[D(x)P(x,t)]$$

where $P(x,t)$ is the probability distribution over neural state $x$, $A(x)$ represents the drift (deterministic) term, and $D(x)$ is the diffusion coefficient. Extended models may include metabolic variables $m$ such that the drift term becomes $A(x, m)$ and the diffusion becomes $D(x, m)$, capturing how metabolic availability modulates neural dynamics [3].

In neural mass models such as the [[jansen-rit-model]] or [[wong-wang-model]], mean firing rates and synaptic currents can be coupled to dynamic equations describing the evolution of metabolic variables. The Wong-Wang model, for example, describes mean firing rate dynamics through:

$$\frac{dS}{dt} = -\frac{S}{\tau} + (1 - S)H(J S + I_{\mathrm{ext}})$$

where $S$ represents the synaptic gating variable, $\tau$ is the synaptic time constant, $J$ is the recurrent coupling strength, and $H$ is a nonlinear transfer function. Extending such models to include metabolic constraints yields a coupled system where the transfer function parameters become functions of metabolic state [3].

Mean-field approaches, such as those explored in data-driven whole-brain modeling, provide a natural framework for incorporating metabolic constraints because they already bridge the gap between microscopic neuronal activity and macroscopic brain dynamics [3]. The recent work on data-driven mean-field models demonstrates how machine learning techniques can learn macroscopic dynamics directly from simulations of spiking neural networks, potentially allowing metabolic variables to be inferred from observed BOLD signals or other metabolic imaging modalities. Such approaches may enable parameter estimation in whole-brain models that simultaneously constrains both neural and metabolic parameters.

The relationship between structural connectivity and functional connectivity in whole-brain models depends critically on the coupling strength between brain regions and the timescales of neural dynamics. Metabolic constraints may impose additional limitations on coupling strength and timescale, since regions with higher metabolic demand may saturate local energy supplies more quickly, leading to nonlinear effects in functional connectivity patterns. This observation connects metabolic modeling to the study of [[critical-periods]] and [[brain-oscillations]], where the brain operates near critical transitions between ordered and disordered dynamics [1]. Recent theoretical work on hierarchical whole-brain models demonstrates that critical synchronization dynamics emerge from the interplay between local and interareal coupling, and metabolic constraints may provide a physical underpinning for why the brain operates in specific critical regimes [1].

## Integration with Whole-Brain Modeling

The [[the-virtual-brain]] ontology represents an effort to create standardized representations of whole-brain models that can encompass metabolic components alongside neural, synaptic, and connectivity parameters [2]. By providing a common vocabulary and metadata specification, the ontology enables researchers to describe the metabolic assumptions of their models in a machine-readable format, facilitating reproducibility and comparison across studies. This framework supports the integration of personalized metabolic constraints derived from individual patient data, which may be particularly valuable in clinical applications such as [[epilepsy-modeling]] where metabolic dysfunction may contribute to seizure dynamics.

The hierarchical whole-brain modeling approach, which incorporates multiple levels of synchronization from local cortical dynamics to interareal phase synchronization, may benefit from metabolic modeling because different hierarchical levels may operate under different metabolic constraints [1]. Local synchronization within brain regions typically occurs on faster timescales and may be more tightly constrained by local metabolic supply, while interareal synchronization operates on slower timescales and may be more influenced by global metabolic states. This multi-scale perspective connects metabolic modeling to the broader framework of [[network-dynamics]] in the brain.

## Relationship to Related Concepts

Metabolic modeling complements several other concepts in the whole-brain modeling literature. The [[bold-model]] and [[hemodynamic-response-function]] provide the biophysical foundation for relating neural activity to the BOLD signal, and extending these models to whole-brain contexts naturally leads to metabolic considerations. Dynamic causal modeling ([[dynamic-causal-modeling]]) has historically incorporated metabolic-like constraints through its Bayesian parameter estimation framework, though explicit metabolic variables are not typically included as state variables.

The study of [[excitation-inhibition-balance]] in neural mass models is closely related to metabolic modeling, since maintaining excitation-inhibition balance requires metabolic energy, and imbalances may arise from metabolic constraints. Similarly, models of [[brain-stimulation]] increasingly consider metabolic consequences of intervention, since therapeutic effects may operate partially through metabolic mechanisms. The connection to [[k-ion-exchange]] relates to metabolic modeling through the role of ionic pumps that maintain resting membrane potentials, which are direct consumers of metabolic energy.

## Open Questions and Future Directions

Several important questions remain at the intersection of metabolic modeling and whole-brain modeling. How can metabolic constraints be personalized using readily available clinical measurements? What are the bifurcation structures that arise when metabolic limits are incorporated into neural mass models, and how do these compare to the novel bifurcations recently discovered in data-driven mean-field approaches [3]? Can metabolic modeling improve the accuracy of clinical predictions in [[personalized-brain-modeling]] applications?

Future directions include integrating metabolic imaging data such as PET measurements of glucose metabolism into whole-brain model fitting procedures, developing new neural mass models that explicitly include metabolic state variables, and exploring how metabolic constraints shape critical dynamics in large-scale brain networks [1]. The growing availability of multi-modal neuroimaging data, including simultaneous EEG-fMRI and MR spectroscopy, provides new opportunities for constraining metabolic models of whole-brain dynamics.

## References

[1] Myrov, V., Suleimanova, A., Knapič, S., Partanen, P., Vesterinen, M., Liu, W., Palva, S., & Palva, J. M. (2026). Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain. *Proceedings of the National Academy of Sciences of the United States of America*. https://doi.org/10.1073/pnas.2505768123

[2] Martin, L., Bülau, K., Pille, R., Schmitt, R., Hüttl, C., Meier, J., Taher, H., Perdikis, D., Schirner, M., Stefanovski, L., & Ritter, P. (2025). The Virtual Brain Ontology: A Digital Knowledge Framework for Reproducible Brain Network Modeling. *bioRxiv*. https://doi.org/10.1101/2025.11.19.689211

[3] Breyton, M., Sip, V., Woodman, M., Hashemi, M., Petkoski, S., & Jirsa, V. (2025). Data-driven mean-field within whole-brain models. *arXiv*. https://doi.org/10.48550/arXiv.2509.02799