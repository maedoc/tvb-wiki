---
title: "DyNet: The Dynamic Computation Graph Library"
created: 2026-05-12
updated: 2026-05-12
type: source
tags: [software-neural-network, machine-learning, library, dynamic-computation-graphs]
authors:
  - Graham Neubig
  - Chris Dyer
  - Yoav Goldberg
  - Andreas Zeldovich
  - Jaime García González
  - Dzmitry Bahdanau
year: 2017
venue: "arXiv preprint arXiv:1702.07014"
doi: "https://doi.org/10.48550/arXiv.1702.07014"
bibtex: |
  @article{neubig2017dynet,
    title={DyNet: The Dynamic Computation Graph Library},
    author={Graham Neubig and Chris Dyer and Yoav Goldberg and Andreas Zeldovich and Jaime Guzm{\'a}n Garc{\'i}a and Dzmitry Bahdanau},
    journal={arXiv preprint arXiv:1702.07014},
    year={2017},
    doi={https://doi.org/10.48550/arXiv.1702.07014},
  }
---

# DyNet: The Dynamic Computation Graph Library

**Authors**: Graham Neubig, Chris Dyer, Yoav Goldberg, Andreas Zeldovich, Jaime García González, Dzmitry Bahdanau  
**Published**: 2017  
**arXiv**: [arXiv:1702.07014](https://arxiv.org/abs/1702.07014)  
**DOI**: 10.48550/arXiv.1702.07014

## Summary

DyNet is a neural network library designed for models that require dynamic computation graphs—neural network architectures where the network structure can vary depending on the input at runtime. Unlike static graph frameworks where the computational structure is fixed once defined, DyNet allows researchers to build network architectures where the connections and operations can change dynamically based on each input sample. This is particularly suited for tree-structured networks, recursive neural networks, and variable-length sequence processing tasks commonly encountered in natural language processing.

## Key Contributions

- Dynamic computation graph framework enabling input-dependent network architectures
- C++ implementation with Python bindings for computational efficiency
- Support for recursive neural networks, tree-structured models, and variable-length sequences
- Lazy computation graph construction for memory efficiency
- Explicit memory management with fine-grained control over computational resources

## Related Concepts

- [[neural-network]]
- [[machine-learning]]
- [[deep-learning]]
- [[natural-language-processing]]