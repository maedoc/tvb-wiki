# Articraft: An Agentic System for Scalable Articulated 3D Asset Generation

**Source**: arxiv
**ID**: 2605.15187
**URL**: https://arxiv.org/abs/2605.15187
**Date**: 2026-05-14
**Year**: 2026
**Authors**: Matt Zhou, Ruining Li, Xiaoyang Lyu, Zhaomou Song, Zhening Huang, Chuanxia Zheng, Christian Rupprecht, Andrea Vedaldi, Shangzhe Wu
**Categories**: cs.CV, cs.GR, cs.RO

## Abstract

A bottleneck in learning to understand articulated 3D objects is the lack of large and diverse datasets. In this paper, we propose to leverage large language models (LLMs) to close this gap and generate articulated assets at scale. We reduce the problem of generating an articulated 3D asset to that of writing a program that builds it. We then introduce a new agentic system, Articraft, that writes such programs automatically. We design a programmatic interface and harness to help the LLM do so effectively. The LLM writes code against a domain-specific SDK for defining parts, composing geometry, specifying joints, and writing tests to validate the resulting assets. The harness exposes a restricted workspace and interface to the LLM, validates the resulting assets, and returns structured feedback. In this way, the LLM is not distracted by details such as authoring a URDF file or managing a complex software environment. We show that this produces higher-quality assets than both state-of-the-art articulated-asset generators and general-purpose coding agents. Using Articraft, we build Articraft-10K, a curated dataset of over 10K articulated assets spanning 245 categories, and show its utility both for training models of articulated assets and in downstream applications such as robotics simulation and virtual reality.
