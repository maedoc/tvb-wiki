---
title: "Anticevic 2012"
created: 2024-01-15
updated: 2026-05-07
type: concept
tags: [paper-review, schizophrenia-models, whole-brain-modeling, neural-mass-models, functional-connectivity, brain-oscillations]
sources: [raw/papers/deco-2013.md]
---

**Anticevic 2012** — formally titled "NMDA receptor function in large-scale anticorrelated neural systems with implications for cognition and schizophrenia" — is a landmark study bridging cellular-level synaptic hypotheses and systems-level neuroimaging observations in [[schizophrenia-models|schizophrenia]] research. Published in *Proceedings of the National Academy of Sciences* (PNAS) by Alan Anticevic, John D. Murray, and colleagues, this work demonstrated how pharmacological manipulation of NMDA receptors disrupts the coordination between large-scale [[brain-dynamics|brain networks]] fundamental to cognitive function.

## Overview

The study addressed a fundamental question in [[computational-psychiatry]]: how do synaptic-level perturbations — specifically, reduced function of NMDA receptors — scale up to produce the [[functional-connectivity|functional connectivity]] alterations and cognitive deficits observed in [[schizophrenia-models|schizophrenia]]? The investigators approached this through a combination of [[fmri|functional MRI]] experiments in healthy human volunteers and [[neural-mass-models|computational neural mass modeling]].

The researchers administered ketamine, a non-competitive NMDA receptor antagonist, to healthy volunteers while they performed a spatial working memory task. Ketamine transiently induces schizophrenia-like symptoms in healthy individuals, making it a powerful pharmacological model for understanding the neurobiological basis of psychosis. Critically, the study focused not just on regional brain activation, but on how ketamine affected the interaction between two large-scale brain systems: the [[default-mode-network|default-mode network]] (DMN) and the task-positive fronto-parietal network.

## Key Findings

### Disruption of Anticorrelated Networks

A fundamental organization principle of the human brain is the presence of dynamically anticorrelated networks: the [[default-mode-network|DMN]] is typically active during rest and deactivates during cognitively demanding tasks, while the task-positive network shows the opposite pattern. The Anticevic 2012 study demonstrated that NMDA receptor blockade with ketamine profoundly disrupted this normal anticorrelation during working memory performance.

Under placebo conditions, robust negative correlation existed between the DMN and task-positive regions during the delay period of the working memory task — reflecting effective competitive inhibition between the two systems. Following ketamine administration, this anticorrelation was significantly reduced, meaning the two systems could no longer operate in opposition. This finding provided direct evidence that glutamate signaling via NMDA receptors is critical for maintaining the competitive relationship between large-scale brain systems.

### Relationship to Cognitive Performance

The degree of ketamine-induced disruption in network anticorrelation predicted individual differences in working memory performance. Participants who showed the greatest reduction in DMN suppression during the task also performed worst on the working memory trials. This links the synaptic-level effect of NMDA blockade directly to behavioral outcome, supporting computational models that propose excitation-inhibition balance as critical for cognition.

### Computational Modeling

A crucial component of the study was the integration of [[neural-mass-models|biophysically realistic computational modeling]]. The authors adapted a microcircuit model of working memory incorporating pyramidal cells and inhibitory interneurons. By simulating selective reduction of NMDA conductance onto inhibitory interneurons — the "disinhibition" hypothesis — the model reproduced the pattern of results observed empirically: both attenuated task-related activation and failure to suppress the DMN.

This modeling work demonstrated how a specific synaptic perturbation (reduced NMDA conductance on GABAergic interneurons) could scale from local microcircuit dysfunction to large-scale network effects measurable with [[fmri|fMRI]]. The model generated specific predictions that were subsequently confirmed empirically, exemplifying the value of computational approaches in [[computational-psychiatry|computational psychiatry]].

## Mechanism: Excitation-Inhibition Imbalance

The findings support a model of **cortical disinhibition** as a key mechanism underlying both the cognitive deficits and network dysfunction in schizophrenia. According to this framework, NMDA receptors on inhibitory interneurons are preferentially sensitive to blockade. When these receptors are compromised, the balance between excitation and inhibition (E/I balance) shifts toward excitation, disrupting the precise coordination of neural activity required for successful cognitive operation.

This [[excitation-inhibition-balance|excitation-inhibition imbalance]] has become one of the leading hypotheses in [[computational-psychiatry|computational psychiatry]], with implications for understanding not just transient pharmacological effects but also the ongoing pathophysiology of schizophrenia.

## Relationship to Whole-Brain Modeling

The Anticevic 2012 paper represents a paradigm for how [[whole-brain-modeling]] approaches can inform understanding of psychiatric conditions. It demonstrated:

1. **Multi-scale integration**: Linking synaptic mechanisms (NMDA receptors), neural microcircuits (pyramidal-interneuron networks), and large-scale brain systems (anticorrelated networks)

2. **Computational validation**: Using [[neural-mass-models|neural mass models]] not just to describe data, but to generate testable predictions that were experimentally verified

3. **Clinical translation**: The ketamine model provides a causal, reversible way to probe mechanisms relevant to schizophrenia, complementing observational studies in patients

4. **Network perspective**: Moving beyond single-region activation to understand how distributed network coordination underlies cognition

This work has influenced subsequent research combining pharmacological neuroimaging with computational modeling to understand other psychiatric conditions and develop targeted treatments. The study's integration of experimental and computational approaches exemplifies the computational psychiatry framework discussed in Deco et al. (2013), which explores how [[brain-dynamics|resting-state brain dynamics]] emerge from the interplay between structural connectivity and neural circuit properties.

## Related Concepts

* [[default-mode-network]] — The task-deactivated network whose suppression was disrupted by ketamine
* [[schizophrenia-models]] — The clinical condition whose pathophysiology the ketamine model recapitulates
* [[excitation-inhibition-balance]] — The synaptic mechanism (E/I ratio) critical for network coordination
* [[neural-mass-models]] — The computational modeling approach used to link synaptic and systems levels
* [[computational-psychiatry]] — The broader field this study exemplifies
* [[brain-dynamics]] — The large-scale network dynamics perturbed by NMDA blockade
* [[functional-connectivity]] — The measure of correlated activity between brain regions disrupted
* [[whole-brain-modeling]] — The framework for simulating large-scale neural dynamics