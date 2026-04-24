---
title: Free Energy Principle
created: 2026-04-20
updated: 2026-04-24
type: concept
tags: [variational-bayes, dynamic-causal-modeling, free-energy-principle, bayesian-brain, dynamical-systems-theory, neural-mass-models, whole-brain-modeling]
sources: [raw/papers/friston-2010-fep.md, raw/papers/friston-2007.md]
---

## Definition

The Free Energy Principle (FEP) is a theoretical framework in neuroscience and cognitive science that proposes all self-organizing biological systems minimize variational free energy. This mathematical quantity serves as a bound on surprise (the negative log probability of sensory observations), providing a unifying account of perception, action, and learning in the brain. Originally formalized by Karl Friston and collaborators in the early 2000s, the FEP extends principles from statistical physics and variational Bayes to explain how neural systems maintain their integrity in the face of a fundamentally unpredictable environment.

## Motivation and Context

The free energy principle emerge from a fundamental puzzle in theoretical neuroscience: how does the brain, a physical system embedded in a complex and ever-changing world, maintain stable functional states despite receiving ambiguous and incomplete sensory information? Traditional models of neural processing treated perception as a passive feedforward process of feature extraction, while motor control was seen as a separate reactive system. The FEP offers a unifying alternative by reframing both perception and action as complementary solutions to the same variational optimization problem.

The conceptual foundation rests on the observation that biological systems are far-from-equilibrium steady states that must resist dissolution into thermal equilibrium—essentially, they must maintain organized patterns of activity against the tendency toward entropy increase. This requirement of homeostasis creates an imperative for any adaptive system: it must minimize surprise by actively inferring the causes of its sensory inputs and selecting actions that verify its predictions. The mathematical elegance of the FEP lies in showing that this seemingly disparate set of behaviors all follow from a single variational principle, much as thermodynamics follows from the minimization of free energy in physical systems.

## Mathematical Framework

### Variational Free Energy

The central quantity in the FEP is variational free energy, defined mathematically as:

**F = ⟨E⟩_q - H(q)**

where ⟨E⟩_q denotes the expected energy under a variational posterior distribution q over hidden states, and H(q) is the entropy of that distribution. The expected energy is typically formulated as the negative log evidence of sensory data under a generative model, while the entropy term encourages the variational distribution to spread broadly over likely states.

The key inequality characterizing the framework is:

**F ≥ -ln p(y)**

This shows that variational free energy always bounds surprise (the negative log probability of observations y under the generative model). Because surprise cannot be directly minimized (it requires knowledge of the true underlying causes), the brain instead minimizes its upper bound—variational free energy—which is tractable to compute. This minimization is mathematically equivalent to performing Bayesian inference, where the variational distribution approximates the true posterior over hidden causes.

### Generative Models

The brain is hypothesized to maintain internal generative models that predict sensory input from underlying hidden causes. These models formalize the relationship between unobservable neural variables (such as stimulus features or motor intentions) and observable sensory data (visual, auditory, somatosensory signals). The process of perception corresponds to inverting this generative model—inferring the hidden causes that most likely produced the observed sensory evidence. This inference proceeds by minimizing variational free energy throughupdates to neural firing rates that represent beliefs about hidden states.

## Core Concepts

### Perception as Inference

The brain under the FEP is conceptualized as an inference machine that continuously updates beliefs about the hidden causes of sensory input. Rather than passively receiving sensory data and extracting features, neural systems actively construct and refine internal models that generate predictions about what the senses should observe. The mismatch between these predictions and actual sensory input—prediction error—drives belief updating through mechanisms that can be understood as gradient descent on variational free energy.

This framework provides a principled account of phenomena ranging from perceptual filling-in and bistable perception to the NMDA receptor-dependent plasticity that underlies learning. When prediction errors are large, the system updates its model parameters (learning) as well as its current beliefs (perception). When predictions accurately track sensory input, the system enters a stable state where prediction errors are minimized.

### Active Inference

Active inference extends the perceptual inference framework to include action. If perception is the minimization of surprise through inference, then action is the minimization of expected future surprise through behavior. The key insight is that actions change the world, and therefore change sensory input. A system can reduce expected surprise by moving its sensors to confirm predictions (active perception) or by acting to bring about expected sensory outcomes.

Mathematically, active inference involves selecting actions that minimize expected free energy over a temporal horizon. This creates a natural account of exploration-exploitation tradeoffs: the system must balance the desire to confirm existing predictions (exploitation) with the need to reduce uncertainty about the model itself (exploration). These imperatives are unified in the single objective of free energy minimization.

### Self-Organization and Self-Evidence

A crucial insight of the FEP is that biological systems maintain themselves far from thermodynamic equilibrium by resisting dispersion—the tendency to spread out over available states. This can be understood as maintaining a low-entropy distribution over physiological states that constitutes the "self." Under the FEP, the imperative to maintain the self is identical to the imperative to minimize surprise; both reduce to variational free energy minimization. This provides a bridge from abstract information-theoretic principles to concrete neurobiological mechanisms of homeostasis and allostasis.

## Relationship to Dynamic Causal Modeling

The FEP provides the theoretical foundation for [[dynamic causal modeling]] (DCM), a popular framework for analyzing neuroimaging data. DCM implements the principles of free energy minimization in the context of neural mass models, where populations of neurons are treated as computational units with dynamics governed by differential equations. The process of model inversion—fitting a DCM to empirical fMRI, EEG, or MEG data—corresponds to minimizing variational free energy to find the posterior distribution over model parameters.

This connection was developed in several key papers, notably Friston et al. (2007) which established the variational Bayesian framework for DCM parameter estimation using the Laplace approximation. The subsequent 2010 review article positioned the FEP as a unifying brain theory that subsumes DCM as a specific implementation. Neural mass models such as the [[Jansen-Rit model]] serve as generative models within this framework, where the model parameters encode synaptic gains and connectivity strengths that determine predicted brain dynamics.

## Relationship to Related Frameworks

The FEP intersects with several other theoretical frameworks in neuroscience and cognitive science. The Bayesian brain hypothesis, which proposes that the brain performs probabilistic inference, is a direct consequence of free energy minimization—when the variational posterior equals the true posterior, free energy minimization reduces to exact Bayesian inference. The [[variational Bayes]] method provides the mathematical machinery for tractable approximate inference in high-dimensional systems.

The framework draws heavily on [[mean-field theory]] from statistical physics, which provides the approximation schemes that make hierarchical inference computationally feasible. Similarly, the use of [[Fokker-Planck equation]] descriptions of neural population dynamics allows the formalization of belief updating in continuous time. These connections to [[dynamical systems theory]] enable analysis of bifurcations and stability in brain models, revealing how qualitative changes in perception and behavior arise from transitions in the underlying dynamics.

## Applications and Implications

The FEP has been applied to diverse domains including computational psychiatry, where it provides a framework for understanding aberrant perception and delusions as maladaptive inference; reinforcement learning, where active inference offers an alternative to reward-based optimization; and whole-brain modeling, where the principle guides the optimization of large-scale connectome-based models such as those implemented in [[the-virtual-brain]]. The framework has also been extended to developmental neuroscience, providing a principled account of how infants learn structure from sensorimotor experience.

## Criticisms and Debates

Despite its mathematical elegance, the FEP has faced several criticisms. Some researchers argue that the principle is too general—it appears to explain everything but makes few specific, testable predictions. Others question whether the variational free energy minimization formalism truly captures the mechanistic constraints faced by real neural tissue, or whether it is merely a useful metaphor. The computational complexity of performing exact variational inference in hierarchical models remains a practical challenge. Additionally, the relationship between the FEP and other theoretical frameworks (such as predictive processing, which shares many assumptions) remains a subject of ongoing debate and clarification in the literature.

## Related Concepts

- [[dynamic-causal-modeling]] — Implementation of FEP for neuroimaging
- [[variational-bayes]] — Mathematical method for approximate inference
- [[neural-mass-model]] — Generative models in DCM
- [[mean-field-theory]] — Statistical approximation
- [[fokker-planck-equation]] — Description of belief dynamics
- [[dynamical-systems-theory]] — Mathematical analysis framework
- [[whole-brain]] — Large-scale modeling context
- [[brain-dynamics-toolbox]] — Software implementation
