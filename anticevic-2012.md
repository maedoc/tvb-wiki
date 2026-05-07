---
title: Anticevic 2012
created: 2026-01-15
updated: 2026-05-07
type: concept
tags: [neural-mass-models, computational-psychiatry, schizophrenia-models, neuroimaging-fmri, excitation-inhibition-balance, default-mode-network, functional-connectivity, whole-brain-modeling]
sources: [raw/papers/anticevic-2012.md]
---

In the context of [[whole-brain]] modeling and [[computational-neuroscience]], Anticevic 2012 refers to a seminal study by Anticevic and colleagues that investigated the relationship between NMDA receptor function and large-scale brain network dynamics, with particular focus on the [[default-mode-network]] (DMN) and task-positive systems. This work provided critical insights into the computational mechanisms underlying cognitive dysfunction in [[schizophrenia-models]] through the lens of excitation-inhibition balance.

## Overview

The study "NMDA receptor function in large-scale anticorrelated neural systems with implications for cognition and schizophrenia" (Anticevic et al., 2012, PNAS) addressed a fundamental question in systems neuroscience: how does glutamatergic neurotransmission via NMDA receptors modulate the dynamic interplay between large-scale brain networks? The human brain exhibits a prominent anticorrelation between the [[default-mode-network]] (DMN)—active during rest and internally directed cognition—and task-positive networks (such as the [[fronto-parietal-control-network]]) engaged during externally directed, goal-oriented tasks. However, the synaptic mechanisms governing this relationship remained poorly understood.

The authors administered ketamine, a non-competitive NMDA receptor antagonist, to healthy volunteers and examined its effects on brain activity during a delayed spatial [[working-memory]] task. Ketamine serves as a pharmacological model of schizophrenia because it transiently induces psychotic-like symptoms and cognitive impairments similar to those observed in the disorder.

## Key Findings

### Disruption of Anticorrelated Systems

The study demonstrated that NMDA receptor blockade via ketamine significantly disrupted the normal reciprocal relationship between the DMN and task-positive networks. Under placebo conditions, task engagement was associated with robust activation of prefrontal and parietal regions coupled with deactivation of DMN regions. However, ketamine attenuated both the activation of task-positive regions and the deactivation of DMN regions, effectively blunting the brain's ability to appropriately switch between network states.

The disruption was not merely additive—it specifically impaired the competition between networks. The authors observed that ketamine reduced the anticorrelation between the fronto-parietal network and the DMN specifically during the working memory delay phase, when cognitive demands were highest. This suggests that NMDA receptor function is critical for maintaining the segregated operation of large-scale brain systems during cognitively demanding tasks.

### Relationship to Behavior and Symptoms

Perhaps most strikingly, the degree of DMN suppression disruption under ketamine predicted individual working memory performance. Participants who showed less DMN deactivation during the task performed worse overall. Furthermore, the extent of this disruption correlated with the severity of transient psychotic symptoms induced by ketamine, suggesting a direct link between large-scale network dysfunction and the phenomenological features of psychosis.

### Computational Modeling Framework

To understand the underlying mechanism, the authors developed a biophysically realistic computational model of [[working-memory]] comprising two modules: a task-activated module representing the fronto-parietal network and a task-deactivated module representing the DMN. These modules were coupled through long-range inhibitory connections, capturing the observed anticorrelation. The model implemented the effects of ketamine as a reduction in NMDA conductance specifically onto GABAergic interneurons—a leading hypothesis for ketamine's mechanism of action.

This model successfully reproduced the empirical findings: reducing excitation-inhibition (E/I) balance via preferential NMDA blockade on interneurons disrupted the task-activated module's ability to suppress the task-deactivated module. The modeling indicated that local disinhibition, rather than impaired long-range connectivity per se, was the primary mechanism driving the observed network-level effects. This computational work exemplifies how [[neural-mass-models]] can bridge synaptic-level hypotheses with systems-level neuroimaging observations.

## Relationship to Schizophrenia

The findings have profound implications for understanding schizophrenia pathophysiology. Multiple studies had documented abnormal DMN function in schizophrenia patients, including reduced task-based deactivation and altered resting-state connectivity. The Anticevic 2012 study demonstrated that these network-level abnormalities could be partially reproduced by transient NMDA receptor blockade in healthy individuals, supporting the hypothesis that [[excitation-inhibition-balance]] disruption is a core mechanism underlying psychotic cognition.

The work established a translational framework linking:
- Synaptic level: NMDA receptor hypofunction on GABAergic interneurons
- Circuit level: Disrupted excitation-inhibition balance in cortical microcircuits  
- Systems level: Failure to suppress DMN during cognitive tasks
- Behavioral level: Working memory impairments and psychotic symptoms

## Related Concepts

The work connects to several key concepts in the [[whole-brain]] modeling literature:

- [[default-mode-network]]: The task-deactivated system whose suppression was disrupted
- [[functional-connectivity]]: The measure used to characterize network relationships
- [[excitation-inhibition-balance]]: The key computational parameter explored
- [[schizophrenia-models]]: The psychiatric condition the pharmacological manipulation mimics
- [[brain-dynamics]]: The systems-level phenomenon under investigation
- [[ketamine]]: The pharmacological probe used to manipulate NMDA function
- [[neural-mass-models]]: The computational framework employed to explain findings
- [[whole-brain]]: The spatial scale at which anticorrelated networks operate
- [[computational-psychiatry]]: The emerging field this work exemplifies
- [[working-memory]]: The cognitive domain most affected

## Impact and Subsequent Work

Anticevic 2012 became a highly influential citation in the field, with subsequent work extending these findings in several directions. Later studies examined similar mechanisms in first-episode and chronic schizophrenia patients, explored the role of different neurotransmitter systems, and developed more sophisticated computational models linking molecular mechanisms to network-level dysfunction. The paper's integration of pharmacological neuroimaging with computational modeling set a methodological standard for translational research in [[computational-neuroscience]] and [[computational-psychiatry]].

The work also motivated research into potential therapeutic approaches targeting excitation-inhibition balance, as the computational models suggested that even small corrections to this parameter could potentially restore normal network dynamics and cognitive function.