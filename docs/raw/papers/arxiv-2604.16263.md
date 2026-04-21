# Semantic Area Graph Reasoning for Multi-Robot Language-Guided Search

**arXiv ID**: 2604.16263
**Published**: 2026-04-17
**Updated**: 2026-04-17
**Authors**: Ruiyang Wang, Hao-Lun Hsu, Jiwoo Kim, Miroslav Pajic
**Categories**: cs.RO
**URL**: https://arxiv.org/abs/2604.16263
**PDF**: https://arxiv.org/pdf/2604.16263
**Source**: arXiv

## Abstract

Coordinating multi-robot systems (MRS) to search in unknown environments is particularly challenging for tasks that require semantic reasoning beyond geometric exploration. Classical coordination strategies rely on frontier coverage or information gain and cannot incorporate high-level task intent, such as searching for objects associated with specific room types. We propose \textit{Semantic Area Graph Reasoning} (SAGR), a hierarchical framework that enables Large Language Models (LLMs) to coordinate multi-robot exploration and semantic search through a structured semantic-topological abstraction of the environment. SAGR incrementally constructs a semantic area graph from a semantic occupancy map, encoding room instances, connectivity, frontier availability, and robot states into a compact task-relevant representation for LLM reasoning. The LLM performs high-level semantic room assignment based on spatial structure and task context, while deterministic frontier planning and local navigation handle geometric execution within assigned rooms. Experiments on the Habitat-Matterport3D dataset across 100 scenarios show that SAGR remains competitive with state-of-the-art exploration methods while consistently improving semantic target search efficiency, with up to 18.8\% in large environments. These results highlight the value of structured semantic abstractions as an effective interface between LLM-based reasoning and multi-robot coordination in complex indoor environments.
