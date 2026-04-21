# Topology Matters: A Cautionary Case Study of Graph SSL on Neuro-Inspired Benchmarks

**arXiv ID**: 2602.03217
**Published**: 2026-02-03
**Updated**: 2026-02-03
**Authors**: May Kristine Jonson Carlon, Su Myat Noe, Haojiong Wang, Yasuo Kuniyoshi
**Categories**: cs.LG, cs.AI
**URL**: https://arxiv.org/abs/2602.03217
**PDF**: https://arxiv.org/pdf/2602.03217
**Source**: arXiv

## Abstract

Understanding how local interactions give rise to global brain organization requires models that can represent information across multiple scales. We introduce a hierarchical self-supervised learning (SSL) framework that jointly learns node-, edge-, and graph-level embeddings, inspired by multimodal neuroimaging. We construct a controllable synthetic benchmark mimicking the topological properties of connectomes. Our four-stage evaluation protocol reveals a critical failure: the invariance-based SSL model is fundamentally misaligned with the benchmark's topological properties and is catastrophically outperformed by classical, topology-aware heuristics. Ablations confirm an objective mismatch: SSL objectives designed to be invariant to topological perturbations learn to ignore the very community structure that classical methods exploit. Our results expose a fundamental pitfall in applying generic graph SSL to connectome-like data. We present this framework as a cautionary case study, highlighting the need for new, topology-aware SSL objectives for neuro-AI research that explicitly reward the preservation of structure (e.g., modularity or motifs).
