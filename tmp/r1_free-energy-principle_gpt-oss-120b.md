---
title: Free Energy Principle
created: 2026-04-20
updated: 2026-04-24
type: concept
tags: [free-energy-principle, variational-bayes, dynamic-causal-modeling, whole-brain-modeling, neural-mass-model, neuroimaging-fmri, resting-state, functional-connectivity, structural-connectivity]
sources: [raw/papers/friston-2010-fep.md, raw/papers/friston-2007.md]
---

## Opening Paragraph
The **Free Energy Principle (FEP)** is a theoretical framework that proposes self‑organising biological systems, including the brain, act to minimise a quantity called *variational free energy*. By keeping free energy low, an organism implicitly reduces the surprise (negative log evidence) associated with its sensory inputs, thereby maintaining viable internal states. In practice, this principle unifies perception, action, and learning under a single probabilistic inference scheme.

## Motivation and Context
Neuroscience has long sought a common language linking neural dynamics, behaviour, and cognition. Traditional models treat perception and action as separate processes, often requiring distinct mathematical formalisms. The FEP emerged as a response to this fragmentation, offering a *universal* account of how the brain updates its internal generative model of the world to predict sensory data while simultaneously acting to sample predictable inputs. This unification aligns with the broader ambition of [[dynamic-causal-modeling]] to infer hidden neuronal states from observable data, and it dovetails with the ambitions of large‑scale [[whole-brain]] simulations that aim to reproduce whole‑brain functional patterns such as those observed in [[resting-state]] fMRI.

From a methodological standpoint, the FEP leverages the machinery of Bayesian inference: the brain is treated as a Bayesian agent that maintains probability distributions over hidden causes of its sensations. By minimising variational free energy, the agent maximises model evidence, which is a cornerstone of statistical model selection in neuroimaging, particularly in [[neural-mass-model]] fitting and [[neuroimaging-fmri]] data analysis.

## Technical Content
Variational free energy **F** can be expressed as:

\[
F = \underbrace{\mathbb{E}_{q(\mathbf{x})}[\ln q(\mathbf{x}) - \ln p(\mathbf{y},\mathbf{x})]}_{\text{Complexity – Accuracy decomposition}}
\]

where \( \mathbf{y} \) denotes sensory data, \( \mathbf{x} \) hidden states, \( p(\mathbf{y},\mathbf{x}) \) the joint probability under the generative model, and \( q(\mathbf{x}) \) the approximate posterior. This formulation splits into an *accuracy* term (how well the model explains data) and a *complexity* term (how far the posterior deviates from the prior). Minimising **F** therefore drives the posterior toward the true posterior, implementing a form of *variational Bayes*.

Active inference extends this static formulation to the temporal domain. The brain selects actions \( \mathbf{a} \) that minimise expected free energy:

\[
G(\pi) = \mathbb{E}_{p(\mathbf{o},\mathbf{s}|\pi)}[F(\mathbf{o},\mathbf{s})]
\]

Here \( \pi \) denotes a policy (sequence of actions), \( \mathbf{o} \) predicted outcomes, and \( \mathbf{s} \) future states. By choosing policies that reduce \( G \), the agent balances *exploration* (reducing epistemic uncertainty) and *exploitation* (achieving preferred outcomes). In the context of [[functional-connectivity]] and [[structural-connectivity]] modelling, this translates into selecting network dynamics that best explain observed functional correlations while staying compatible with the underlying anatomical scaffold.

## Relationships to Other Frameworks
The FEP can be viewed as a generalisation of several pre‑existing ideas. Classical [[bayesian-brain]] hypotheses already posited that perception implements Bayesian inference, but they did not prescribe a concrete optimisation target. The FEP fills this gap by identifying variational free energy as that target. Compared to traditional [[dynamic-causal-modeling]], which focuses on parameter estimation for a fixed model structure, the FEP views model structure itself as adaptable through *policy* selection, thereby encompassing both inference and control.

Earlier energy‑based theories, such as the *predictive coding* framework, can be derived as a linearised special case of the FEP when the generative model is assumed Gaussian and the Laplace approximation holds (Friston, 2007). Conversely, more recent *active inference* formulations extend predictive coding by explicitly incorporating action selection, providing a richer description of behaviour that goes beyond passive perception.

## Biological Grounding
The FEP is deliberately agnostic about the specific neural substrate, yet its mathematical ingredients map onto known neurophysiological processes. The *prediction error* signals that drive belief updates correlate with neuronal firing rates observed in hierarchical cortical circuits, while the *precision* weighting of these errors mirrors neuromodulatory gain control (e.g., acetylcholine, norepinephrine). In [[neural-mass-model]] implementations, free‑energy gradients can be expressed as synaptic coupling adjustments that shape the emergent oscillatory repertoire, linking the principle to observable rhythms in electroencephalography and magnetoencephalography.

At the network level, the principle predicts that the brain will preferentially occupy *attractor* states that are both metabolically cheap (low entropy) and informative about the environment. This resonates with findings from resting‑state fMRI where low‑dimensional manifolds capture the majority of functional variance, and with the *repertoire* hypothesis advanced by Deco and colleagues (2013) that spontaneous activity explores a set of metastable configurations akin to those recruited during tasks.

Through the lens of the FEP, seemingly disparate phenomena—from perceptual learning and decision‑making to large‑scale brain dynamics—are interpreted as manifestations of a single optimisation process, offering a parsimonious yet powerful unifying narrative for computational neuroscience.
