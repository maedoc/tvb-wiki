# MarkIt: Training-Free Visual Markers for Precise Video Temporal Grounding

**Source**: arxiv
**ID**: 2604.25886
**URL**: https://arxiv.org/abs/2604.25886
**Date**: 2026-04-28
**Year**: 2026
**Authors**: Pengcheng Fang, Yuxia Chen, Xiaohao Cai
**Categories**: cs.MM

## Abstract

Video temporal grounding (VTG) aims to localize the start and end timestamps of the event described by a given query within an untrimmed video. Despite the strong open-world video understanding and recognition ability of video language large models (Vid-LLMs), outputting precise temporal grounding information remains challenging, since explicit temporal cues are scarce in untrimmed videos, and query-relevant entities are hard to track consistently across the video timeline. In this paper, we present \MarkIt{}, a training-free framework that transforms an input video into a query-conditioned marked video, which empowers Vid-LLMs to generate more reliable temporal localization predictions. The core component of \MarkIt{} is an annotation-free query-to-mask grounding bridge (Q2M-Bridge). Given a natural-language query, it automatically derives a compact set of canonical subject tags through linguistic parsing and normalization, then maps these tags to query-conditioned instance masks using text-conditioned open-vocabulary segmentation. The bridge also embeds lightweight semantic instance markers and a persistent frame index into each frame, effectively transforming long-range temporal reasoning into explicit visual cues for Vid-LLMs. \MarkIt{} adopts an inference-time plug-and-play design, needs no modifications to Vid-LLM weights, and is fully compatible with supervised fine-tuning. Experiments conducted on multiple mainstream moment retrieval and highlight detection benchmarks demonstrate that \MarkIt {} achieves state-of-the-art results, delivering consistent temporal grounding improvements across a wide range of existing models.
