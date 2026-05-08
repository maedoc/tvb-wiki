# Using transient, effector-specific neural responses to gate decoding for brain–computer interfaces

**Source**: semantic-scholar
**ID**: 6edbd74ce0feb1a8745b332bda17b6c381ffd710
**DOI**: 10.1088/1741-2552/adaa1f
**URL**: https://www.semanticscholar.org/paper/6edbd74ce0feb1a8745b332bda17b6c381ffd710
**Date**: 2025-01-14
**Year**: 2025
**Authors**: B. Dekleva, J. Collinger
**Venue**: Journal of Neural Engineering
**Citations**: 3

## Abstract

Objective. Real-world implementation of brain–computer interfaces (BCIs) for continuous control of devices should ideally rely on fully asynchronous decoding approaches. That is, the decoding algorithm should continuously update its output by estimating the user’s intended actions from real-time neural activity, without the need for any temporal alignment to an external cue. This kind of open-ended temporal flexibility is necessary to achieve naturalistic and intuitive control. However, the relation between cortical activity and behavior is not stationary: neural responses that appear related to a certain aspect of behavior (e.g. grasp force) in one context will exhibit a relationship to something else in another context (e.g. reach speed). This presents a challenge for generalizable decoding, since the applicability of a decoder for a given parameter changes over time. Approach. We developed a method to simplify the problem of continuous decoding that uses transient, end effector-specific neural responses to identify periods of relevant effector engagement. Specifically, we use transient responses in the population response observed at the onset and offset of all hand-related actions to signal the applicability of hand-related feature decoders (e.g. digit movement or force). By using this transient-based gating approach, specific feature decoding models can be simpler (owing to local linearities) and are less sensitive to interference from cross-effector interference such as combined reaching and grasping actions. Main results. The transient-based decoding approach enabled high-quality online decoding of grasp force and individual finger control in multiple behavioral paradigms. The benefits of the gated approach are most evident in tasks that require both hand and arm control, for which standard continuous decoding approaches exhibit high output variability. Significance. The approach proposed here addresses the challenge of decoder generalization across contexts. By limiting decoding to identified periods of effector engagement, this approach can support reliable BCI control in real-world applications. Clinical Trial ID: NCT01894802
