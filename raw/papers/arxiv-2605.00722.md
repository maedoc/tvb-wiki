# Exploring the Limits of End-to-End Feature-Affinity Propagation for Single-Point Supervised Infrared Small Target Detection

**Source**: arxiv
**ID**: 2605.00722
**URL**: https://arxiv.org/abs/2605.00722
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Qiancheng Zhou, Wenhua Zhang
**Categories**: cs.CV

## Abstract

Single-point supervised infrared small target detection (IRSTD) drastically reduces dense annotation costs. Current state-of-the-art (SOTA) methods achieve high precision by recovering mask supervision through explicit, offline pseudo-label construction, such as multi-stage active learning and physics-driven mask generation. In this paper, we study a minimalist alternative: generating point-to-mask supervision online through in-batch, point-anchored feature-affinity propagation. We instantiate this paradigm as GSACP, an end-to-end testbed that directly supervises the detector using hard-margin feature affinity gated by local image priors, entirely eliminating external label-evolution loops.   This compact design, however, exposes an optimization bottleneck. Because the affinity target is generated from the same feature representation being optimized, training forms a self-referential loop. We theoretically formalize this as \emph{Self-Referential Propagation Drift}, a representation-supervision entanglement that can sharpen true boundaries or distort the feature space to satisfy its own targets. To systematically isolate these failure modes, we apply a protocolized single-variable ablation procedure spanning local EMA teacher decoupling, hard-background contrastive separation, and adaptive support geometry.   On the SIRST3 dataset, GSACP-Final establishes a new ultra-low false-alarm operating regime, achieving a highly competitive $0.6674$ mIoU while demonstrating a $38\% relative reduction in false-positive artifacts ($\mathrm{Fa}$) compared with PAL. By systematically deconstructing the end-to-end paradigm, we map its performance boundaries and show that in-batch feature propagation provides a compact alternative for deployment scenarios where false-alarm suppression is paramount.
