---
title: Anticevic 2012
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [whole-brain-modeling, computational-neuroscience, schizophrenia-models, excitation-inhibition-balance, neural-mass-models, paper-methods, default-mode-network, brain-dynamics, neuroimaging-fmri]
sources: [raw/papers/deco-2013.md, raw/papers/jordan-2018.md]
---

Anticevic 2012 refers to a influential body of work by Alan Anticevic and colleagues at Yale University, published primarily in two papers: "The role of default network deactivation in cognition and disease" (Trends in Cognitive Sciences, 2012) and "NMDA receptor function in large-scale anti-correlated neural systems with implications for cognition and schizophrenia" (PNAS, 2012). Together, these papers established computational frameworks for linking glutamatergic dysfunction at the synaptic level to whole-brain dynamics observable in neuroimaging, representing foundational work in what later became known as computational psychiatry.

## Motivation and Context

The brain's default-mode network (DMN)—a set of brain regions including medial prefrontal cortex, posterior cingulate cortex, and inferior parietal cortices—exhibits high activity during rest and deactivates during cognitively demanding tasks that require external attention. This reciprocal relationship between the DMN and task-positive networks (such as the fronto-parietal control network) had been documented extensively through resting-state fMRI, but the neurobiological mechanisms governing this anti-correlation remained poorly understood.

Anticevic's 2012 work addressed this gap by combining pharmacological neuroimaging with biophysically realistic computational modeling. The approach was motivated by several converging observations: first, schizophrenia had been characterized as a disorder of dysconnected brain networks; second, postmortem studies had consistently implicated GABAergic interneuron dysfunction in prefrontal cortex; and third, NMDA receptor antagonists like ketamine produced schizophrenia-like symptoms in healthy volunteers, including working memory impairments and altered brain connectivity. Understanding how these molecular-level deficits propagated to systems-level dynamics became the central motivation for this work.

## Computational Framework

The computational models developed in these papers represent extensions of [[Jansen-Rit model]] neural mass formulations that had been previously applied to whole-brain dynamics. The key innovation was parameterizing the models to capture the effects of reduced NMDA receptor conductance preferentially onto GABAergic interneurons—a leading hypothesis for ketamine's mechanism of action. This produces a state of cortical disinhibition where excitatory pyramidal cells receive less feedback inhibition, fundamentally altering the dynamics of local circuits.

The mathematical framework involves two interacting neural mass modules: a task-activated module representing working memory circuitry in prefrontal cortex, and a task-deactivated module representing the DMN. These modules interact through long-range inhibitory projections, creating the anti-correlated dynamics observed empirically. When NMDA conductance onto inhibitory cells is reduced (simulating ketamine effects or GABAergic dysfunction), the task-deactivated module becomes hyperactive and less responsive to suppressive inputs from the task-activated module. This produces a characteristic pattern of findings: reduced task-positive activation combined with failure to suppress the DMN during working memory performance.

The models were validated against empirical fMRI data from ketamine administration experiments, demonstrating that the excitation-inhibition balance parameter could reproduce the pattern of both activation and deactivation abnormalities observed in humans. Critically, the same computational framework could explain findings previously observed in schizophrenia patients, suggesting a shared mechanism of cortical disinhibition.

## Relationship to Whole-Brain Modeling

This work established a template for multi-scale computational modeling that bridges cellular neuroscience and systems-level brain dynamics. The approach demonstrated that [[whole-brain modeling]] frameworks constrained by structural connectivity could serve not merely as descriptive tools but as explanatory frameworks that make specific predictions about the effects of molecular perturbations.

The framework connects to broader developments in whole-brain modeling, particularly work by Deco et al. (2013) on how structured networks constrained by empirical connectivity can reproduce resting-state dynamics through noise-driven fluctuations around stable fixed points. Anticevic's contribution extended these frameworks by explicitly incorporating parameters that could be directly linked to molecular findings from pharmacological and postmortem studies.

For The Virtual Brain and similar whole-brain simulators, this work demonstrated the feasibility of linking molecular-level parameters (such as NMDA receptor conductance) to whole-brain dynamics observable in fMRI. Subsequent work has incorporated more biophysically detailed neural mass formulations, including [[Wong-Wang model]] formulations that capture [[excitation-inhibition balance]] at the level of recurrent neural circuits.

## Implications for Schizophrenia

The most significant contribution of Anticevic 2012 was providing a computational account of how glutamate dysfunction might produce the brain connectivity abnormalities observed in schizophrenia. The finding that ketamine—a pharmacological probe of NMDA receptor function—produces pattern of both task-positive activation deficits and DMN suppression failures that mirrors schizophrenia suggested a mechanistic link between the well-documented GABAergic and glutamatergic abnormalities in the disorder.

This work also highlighted the functional significance of DMN suppression for cognitive performance. The degree of DMN suppression during working memory predicted task accuracy both within and across subjects, and subjects showing the least DMN suppression under ketamine exhibited the most severe ketamine-induced negative symptoms. This established a direct link between the ability to suppress internally-directed cognition and the cognitive impairments characteristic of schizophrenia.

## Subsequent Developments

The computational framework established in Anticevic 2012 has been extended in several directions. Subsequent work by Anticevic and colleagues (2014, 2015) further developed biophysically based models that scale from synaptic level to large-scale brain networks, providing more comprehensive accounts of excitation-inhibition balance alterations in schizophrenia. The approach has also been applied to other psychiatric conditions including bipolar disorder, where distinct patterns of thalamo-cortical connectivity have been identified.

Research using NEST and other spiking neural network simulators has extended these approaches to large-scale simulations with biophysically realistic synapse models, moving beyond neural mass approximations toward more detailed representations of cortical circuitry. The field continues to grapple with questions of parameter estimation—how to constrain models with limited empirical data—and the challenge of linking computational models to clinical outcomes in personalized medicine applications.