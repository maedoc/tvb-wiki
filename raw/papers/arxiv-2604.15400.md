# Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation

**arXiv ID**: 2604.15400
**Published**: 2026-04-16
**Updated**: 2026-04-16
**Authors**: G. Aytug Akarlar
**Categories**: cs.LG, cs.AI, cs.CL
**URL**: https://arxiv.org/abs/2604.15400
**PDF**: https://arxiv.org/pdf/2604.15400
**Source**: arXiv

## Abstract

We present causal evidence that hallucination in autoregressive language models is an early trajectory commitment governed by asymmetric attractor dynamics. Using same-prompt bifurcation, in which we repeatedly sample identical inputs to observe spontaneous divergence, we isolate trajectory dynamics from prompt-level confounds. On Qwen2.5-1.5B across 61 prompts spanning six categories, 27 prompts (44.3%) bifurcate with factual and hallucinated trajectories diverging at the first generated token (KL = 0 at step 0, KL > 1.0 at step 1). Activation patching across 28 layers reveals a pronounced causal asymmetry: injecting a hallucinated activation into a correct trajectory corrupts output in 87.5% of trials (layer 20), while the reverse recovers only 33.3% (layer 24); both exceed the 10.4% baseline (p = 0.025) and 12.5% random-patch control. Window patching shows correction requires sustained multi-step intervention, whereas corruption needs only a single perturbation. Probing the prompt encoding itself, step-0 residual states predict per-prompt hallucination rate at Pearson r = 0.776 at layer 15 (p < 0.001 against a 1000-permutation null); unsupervised clustering identifies five regime-like groups (eta^2 = 0.55) whose saddle-adjacent cluster concentrates 12 of the 13 bifurcating false-premise prompts, indicating that the basin structure is organized around regime commitments fixed at prompt encoding. These findings characterize hallucination as a locally stable attractor basin: entry is probabilistic and rapid, exit demands coordinated intervention across layers and steps, and the relevant basins are selected by clusterable regimes already discernible at step 0.
