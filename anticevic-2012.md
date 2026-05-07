---
title: Anticevic 2012
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [schizophrenia-models, neuroimaging-fmri, computational-neuroscience, neural-mass-models, excitation-inhibition-balance, default-mode-network, resting-state, working-memory, brain-dynamics, cortical-disinhibition]
sources: [raw/papers/deco-2013.md]
---

**Anticevic 2012** refers to a landmark study by Anticevic and colleagues that investigated NMDA receptor function in large-scale anticorrelated neural systems, with implications for understanding both normal cognition and the pathophysiology of schizophrenia. This work represents a seminal bridge between synaptic-level mechanisms and systems-level neuroimaging in [[whole-brain|whole-brain modeling]].

## Overview and Definition

The study, published in the Proceedings of the National Academy of Sciences (PNAS), examined how pharmacological blockade of NMDA receptors—using the dissociative anesthetic ketamine—alters the interaction between two large-scale brain networks that are normally anticorrelated during cognitive tasks: the task-positive network (including fronto-parietal regions) and the [[default-mode-network|default mode network]] (DMN). The authors demonstrated that NMDA receptor antagonism disrupts the normal reciprocal relationship between these systems during working memory performance, providing critical insight into how glutamatergic neurotransmission supports cognition and how its disruption may contribute to psychiatric illness.

## Motivation and Context

Understanding the neural basis of cognitive deficits in schizophrenia has long posed a challenge for neuroscience. While dopamine dysfunction has been historically implicated in schizophrenia, emerging evidence pointed toward glutamatergic mechanisms, particularly NMDA receptor hypofunction, as a potential common pathway. However, the link between synaptic-level hypotheses and the large-scale network abnormalities observed in neuroimaging studies remained unclear.

Anticevic et al. (2012) addressed this gap by combining pharmacological fMRI experiments with biophysically realistic computational modeling. Their approach tested whether the leading hypothesis for ketamine's effects—preferential antagonism of NMDA receptors on GABAergic interneurons, resulting in cortical disinhibition—could explain observed disruptions in whole-brain network dynamics during working memory. This work directly connects to the broader enterprise of [[computational-neuroscience|computational neuroscience]] by using mathematical models to formalize and test hypotheses about disease mechanisms.

## Technical Content

### Experimental Design

The study administered ketamine or placebo to healthy volunteers while they performed a delayed spatial working memory task. Blood-oxygen-level-dependent (BOLD) fMRI was used to measure task-evoked activation and deactivation patterns. The key innovation was examining not only task-positive activations but also task-induced deactivations—specifically, the suppression of the DMN that normally occurs during cognitively demanding tasks.

### Main Findings

Ketamine administration produced several critical effects:

First, the drug significantly impaired working memory accuracy, consistent with the well-established cognitive-impairing effects of NMDA antagonists. Second, ketamine attenuated both task-evoked activation in the fronto-parietal network and task-evoked deactivation in the DMN. Third, and most strikingly, the disruption of DMN suppression during working memory predicted individual differences in ketamine-induced negative symptoms—subjects showing the least DMN suppression exhibited more severe schizophrenia-like symptoms. Fourth, task-based functional connectivity analysis revealed that ketamine disrupted the normal anticorrelation between the fronto-parietal and DMN systems during the delay period of the working memory task.

### Computational Modeling Framework

To test the mechanistic hypothesis, the authors developed a biophysically realistic computational model of working memory based on microcircuit equations from [[mean-field-theory|mean-field theory]]. The model comprised two modules: a task-activated module representing the fronto-parietal working memory circuit, and a task-deactivated module representing the DMN. These modules were connected through long-range net inhibitory projections that implemented the anticorrelation observed empirically.

The key manipulation in the model was reducing NMDA conductance onto inhibitory interneurons (g_E-I), which instantiates the hypothesized mechanism of ketamine action—preferential blockade of NMDA receptors on GABAergic cells. This local disinhibition within the DMN module rendered it less sensitive to suppressive signals from the task-activated module, closely reproducing the experimental BOLD findings.

The model produces predictions that can be captured mathematically. The key equation governing the dynamics involves the balance between excitation (E) and inhibition (I):

$$\tau \frac{du}{dt} = -u + \phi\left( W_{EE} \cdot u - W_{EI} \cdot v + I_{external} \right)$$

where $u$ represents the firing rate of excitatory neurons, $v$ represents inhibitory neurons, $W_{EE}$ and $W_{EI}$ are weight matrices, and $\phi$ is a nonlinear activation function. Reducing g_E-I in this framework tilts the excitation-inhibition balance toward disinhibition.

## Relationship to Other Concepts

This work sits at the intersection of several important research domains in [[whole-brain-modeling|whole-brain modeling]] and computational psychiatry.

The study provides crucial empirical validation for computational models of excitation-inhibition balance that have been subsequently developed in multiple [[neural-mass-models|neural mass models]], including those implemented in [[the-virtual-brain|TVB]] and other simulation platforms. The finding that modest disinhibition (targeting NMDA receptors on interneurons specifically) can reproduce both neural and behavioral effects has informed subsequent work on [[personalized-brain-modeling|personalized brain modeling]] in psychiatric conditions.

The work connects directly to the [[resting-state|resting-state]] fMRI literature by demonstrating how pharmacological challenges can transiently induce patterns of network dysfunction that resemble those observed in schizophrenia. This bridges [[functional-connectivity|functional connectivity]] analyses with synaptic-level mechanisms.

The computational framework draws on [[dynamical-systems-theory|dynamical systems theory]], treating the competition between task-positive and task-negative networks as an attractor dynamics problem. This perspective has been influential in understanding how brain dynamics can transition between functional regimes.

## Implications for Schizophrenia Research

Anticevic et al. (2012) established that the disruption of large-scale network anticorrelation observed in chronic schizophrenia patients may have a mechanistic basis in cortical disinhibition. The study demonstrated that a pharmacological challenge producing transient schizophrenia-like symptoms could quantitatively mimic the fMRI abnormalities seen in patients, suggesting a potential common substrate. This work has been highly influential in the field of [[computational-psychiatry|computational psychiatry]], where similar model-based approaches are now widely used to understand psychiatric pathophysiology.

## Open Questions

Several important questions remain open. The precise synaptic alterations in schizophrenia likely differ from acute ketamine administration in their temporal dynamics and chronicity. It remains unclear whether NMDA receptor hypofunction on interneurons is the primary mechanism in schizophrenia or whether other converging pathways lead to similar network-level phenotypes. Additionally, the relationship between DMN suppression deficits and specific cognitive domains beyond working memory continues to be investigated.

## See Also

- [[schizophrenia-models]]
- [[default-mode-network]]
- [[excitation-inhibition-balance]]
- [[functional-connectivity]]
- [[resting-state-fmri]]
- [[working-memory]]
- [[computational-psychiatry]]
- [[neural-mass-models]]
- [[brain-dynamics]]