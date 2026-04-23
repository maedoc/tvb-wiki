# Accurate Open-Loop Control of a Soft Continuum Robot Through Visually Learned Latent Representations

**Source**: arxiv
**ID**: 2603.19655
**URL**: https://arxiv.org/abs/2603.19655
**Date**: 2026-03-20
**Year**: 2026
**Authors**: Henrik Krauss, Johann Licher, Naoya Takeishi, Annika Raatz, Takehisa Yairi
**Categories**: cs.RO, eess.SY

## Abstract

This work addresses open-loop control of a soft continuum robot (SCR) from video-learned latent dynamics. Visual Oscillator Networks (VONs) from previous work are used, that provide mechanistically interpretable 2D oscillator latents through an attention broadcast decoder (ABCD). Open-loop, single-shooting optimal control is performed in latent space to track image-specified waypoints without camera feedback. An interactive SCR live simulator enables design of static, dynamic, and extrapolated targets and maps them to model-specific latent waypoints. On a two-segment pneumatic SCR, Koopman, MLP, and oscillator dynamics, each with and without ABCD, are evaluated on setpoint and dynamic trajectories. ABCD-based models consistently reduce image-space tracking error. The VON and ABCD-based Koopman models attains the lowest MSEs. Using an ablation study, we demonstrate that several architecture choices and training settings contribute to the open-loop control performance. Simulation stress tests further confirm static holding, stable extrapolated equilibria, and plausible relaxation to the rest state. To the best of our knowledge, this is the first demonstration that interpretable, video-learned latent dynamics enable reliable long-horizon open-loop control of an SCR.
