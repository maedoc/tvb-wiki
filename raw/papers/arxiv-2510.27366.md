# A Sensing Whole Brain Zebrafish Foundation Model for Neuron Dynamics and Behavior

**Source**: arxiv
**ID**: 2510.27366
**URL**: https://arxiv.org/abs/2510.27366
**Date**: 2025-10-31
**Year**: 2025
**Authors**: Sam Fatehmanesh Vegas, Matt Thomson, James Gornet, David Prober
**Categories**: q-bio.NC

## Abstract

Neural dynamics underlie behaviors from memory to sleep, yet identifying mechanisms for higher-order phenomena (e.g., social interaction) is experimentally challenging. Existing whole-brain models often fail to scale to single-neuron resolution, omit behavioral readouts, or rely on PCA/conv pipelines that miss long-range, non-linear interactions. We introduce a sparse-attention whole-brain foundation model (SBM) for larval zebrafish that forecasts neuron spike probabilities conditioned on sensory stimuli and links brain state to behavior. SBM factorizes attention across neurons and along time, enabling whole-brain scale and interpretability. On a held-out subject, it achieves mean absolute error <0.02 with calibrated predictions and stable autoregressive rollouts. Coupled to a permutation-invariant behavior head, SBM enables gradient-based synthesis of neural patterns that elicit target behaviors. This framework supports rapid, behavior-grounded exploration of complex neural phenomena.
