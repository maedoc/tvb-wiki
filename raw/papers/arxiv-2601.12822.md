# MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction

**Source**: semantic-scholar
**ID**: 3f769130125a7f45b359b5b2b316c7c16de03508
**DOI**: 10.48550/arXiv.2601.12822
**URL**: https://www.semanticscholar.org/paper/3f769130125a7f45b359b5b2b316c7c16de03508
**Date**: 2026-01-19
**Year**: 2026
**Authors**: Wenqi Zhang, Yulin Shen, Changyue Jiang, Jiarun Dai, Geng Hong, Xu Pan
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Large foundation models are integrated into Computer Use Agents (CUAs), enabling autonomous interaction with operating systems through graphical user interfaces (GUIs) to perform complex tasks. This autonomy introduces serious security risks: malicious instructions or visual prompt injections can trigger unsafe reasoning and cause harmful system-level actions. Existing defenses, such as detection-based blocking, prevent damage but often abort tasks prematurely, reducing agent utility. In this paper, we present MirrorGuard, a plug-and-play defense framework that uses simulation-based training to improve CUA security in the real world. To reduce the cost of large-scale training in operating systems, we propose a novel neural-symbolic simulation pipeline, which generates realistic, high-risk GUI interaction trajectories entirely in a text-based simulated environment, which captures unsafe reasoning patterns and potential system hazards without executing real operations. In the simulation environment, MirrorGuard learns to intercept and rectify insecure reasoning chains of CUAs before they produce and execute unsafe actions. In real-world testing, extensive evaluations across diverse benchmarks and CUA architectures show that MirrorGuard significantly mitigates security risks. For instance, on the ByteDance UI-TARS system, it reduces the unsafe rate from 66.5% to 13.0% while maintaining a marginal false refusal rate (FRR). In contrast, the state-of-the-art GuardAgent only achieves a reduction to 53.9% and suffers from a 15.4% higher FRR. Our work proves that simulation-derived defenses can provide robust, real-world protection while maintaining the fundamental utility of the agent. Our code and model are publicly available at https://bmz-q-q.github.io/MirrorGuard/.
