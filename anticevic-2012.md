---
title: "Anticevic 2012"
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [schizophrenia-models, neural-mass-models, excitation-inhibition-balance, computational-psychiatry, nmda-receptor, default-mode-network, brain-dynamics, whole-brain-modeling, dynamic-causal-modeling]
sources: [raw/papers/anticevic-2012.md]
---

Anticevic et al. (2012) established a mechanistic link between glutamate synaptic dysfunction and large-scale brain network organization in [[schizophrenia-models]]. The study demonstrated that NMDA receptor antagonism disrupts the reciprocal relationship between the [[default-mode-network]] (DMN) and task-positive systems during working memory, providing computational evidence that these effects arise from cortical disinhibition.

## Background and Motivation

The human brain exhibits intrinsic functional organization into dynamically anticorrelated networks: the DMN, which is active during rest and internally directed cognition, and the task-positive network (fronto-parietal system), which engages during goal-directed cognitive operations. This anticorrelation is a fundamental property of spontaneous brain activity measured via [[resting-state-fmri]], yet the synaptic mechanisms maintaining this balance remained unknown. Understanding these mechanisms is critical because both networks are profoundly disrupted in [[schizophrenia-models]], where patients exhibit failure to deactivate the DMN during cognitive tasks alongside reduced task-positive activation.

Prior research had established that sub-anesthetic doses of ketamine, a non-competitive [[nmda-receptor]] antagonist, transiently induce symptoms resembling schizophrenia in healthy volunteers. However, the mechanistic link between ketamine's effects on glutamatergic neurotransmission and the large-scale network alterations observed in schizophrenia remained unclear.

## Experimental Approach

The study combined pharmacological [[fmri]] in healthy volunteers with biophysically computational modeling. Participants performed a spatial working memory task during ketamine infusion, allowing measurement of both task-evoked activations and the dynamics between large-scale networks. The key manipulation examined how NMDA receptor blockade altered the functional competition between the DMN and fronto-parietal systems.

## Key Findings

Ketamine administration produced three major effects. First, it attenuated task-related activation in prefrontal and parietal cortex during working memory encoding and delay periods. Second, it dramatically reduced DMN suppression during task performance—the DMN typically deactivates during goal-directed cognition, but ketamine prevented this deactivation. Third, task-based functional connectivity between the fronto-parietal and DMN systems became significantly less negative under ketamine, indicating disruption of the normal anticorrelation.

Computational modeling established the mechanism: ketamine's effects were reproduced by reducing NMDA conductance preferentially onto GABAergic interneurons (gE-I), implementing cortical disinhibition. This "disinhibition" hypothesis holds that NMDA receptors are more abundant on inhibitory interneurons, so blockade preferentially reduces inhibition onto pyramidal cells, creating a net increase in excitation-inhibition ratio.

## Relationship to Schizophrenia

The findings provide a translational framework for understanding [[schizophrenia-models]] pathophysiology. Both ketamine administration and schizophrenia produce failure of DMN suppression during working memory, impaired cognitive performance, and elevated negative symptoms. The computational model predicts that restoring excitation-inhibition balance—rather than simply enhancing or reducing global activity—may be the critical intervention for normalizing brain dynamics.

## Relationship to Other Concepts

This work connects to multiple [[whole-brain]] modeling approaches. It predates and informs the [[wong-wang-model]] framework for understanding excitation-inhibition balance in working memory circuits. The findings align with the [[dynamic-causal-modeling]] paradigm for understanding changes in effective connectivity. The emphasis on NMDA receptor function connects to broader work on [[excitation-inhibition-balance]] in cortical microcircuits and its disruption in psychiatric disorders.

The methodology exemplifies computational psychiatry approaches, where biophysically realistic models test mechanistic hypotheses about synaptic dysfunction and generate predictions for neuroimaging findings. This framework has been extended to study thalamocortical dysconnectivity in schizophrenia, as reviewed in subsequent work by the same group.

## Technical Details

The computational model employed two modules: a task-activated recurrent network capable of working memory maintenance and a task-deactivated module representing DMN dynamics. Long-range connections implemented reciprocal inhibition between modules. Reducing gE-I (NMDA conductance onto interneurons) produced the experimental pattern, while reducing recurrent excitation (gE-E) produced qualitatively different predictions not matching empirical observations—all interneurons expressed higher NR2C subunit sensitivity to ketamine.

## Implications for Treatment

The model suggests that successful pharmacological interventions must restore excitation-inhibition balance rather than broadly stimulating or depressing neural activity. This principle has guided subsequent development of treatments targeting GABAergic function or specific NMDA receptor subtypes in schizophrenia.

## Open Questions

Several questions remain: whether these mechanisms generalize to other cognitive domains beyond working memory, how chronic illness differs from acute pharmacological challenge, and whether the model can predict individual differences in treatment response.