# Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics

**Source**: arxiv
**ID**: 2604.25904
**URL**: https://arxiv.org/abs/2604.25904
**Date**: 2026-04-28
**Year**: 2026
**Authors**: Andre Herz, Daniel Durstewitz, Georgia Koppe
**Categories**: cs.LG, math.DS, stat.ML

## Abstract

Identity teacher forcing (ITF) enables stable training of deterministic recurrent surrogates for chaotic dynamical systems and has been highly effective for dynamical systems reconstruction (DSR) with recurrent neural networks (RNNs), including interpretable almost-linear RNNs (AL-RNNs). However, as an intervention-based prediction loss (and thus a generalized Bayes update), teacher forcing need not match the free-running model's marginal likelihood geometry. We compare the objective-induced curvatures of ITF and marginal likelihood in a probabilistic switching augmentation of AL-RNNs, estimating ambiguity-aware observed information via Louis' identity. In the switching setting studied here, conditioning on a single forced regime path (as ITF does) inflates curvature, while marginal likelihood curvature is reduced by a missing-information correction when multiple switching explanations remain plausible. In Lorenz-63 experiments, windowed evidence fine-tuning improves held-out evidence but can degrade dynamical quantities of interest (QoIs) relative to ITF-pretrained models.
