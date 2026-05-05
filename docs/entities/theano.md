---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software-neural-computation
- computational-neuroscience
- deep-learning
- python
- machine-learning
title: Theano
type: entity
updated: '2026-05-05'
---

Theano is a Python library for symbolic mathematical computation that was developed at the Montreal Institute for Learning Algorithms (MILA) at Université de Montréal. Originally released in 2007, Theano enabled researchers to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It was among the first widely adopted frameworks for deep learning research and played a crucial role in advancing the field during the early to mid-2010s before being largely superseded by TensorFlow and PyTorch. Theano's core innovation lay in its ability to perform symbolic differentiation, compile computations into efficient machine code, and leverage Graphics Processing Units (GPUs) for accelerated computation—capabilities that were novel and transformative at the time of its development.

## Key Features

Theano's architecture centered on symbolic computation, where mathematical operations were first expressed as a computational graph before being compiled and executed. This approach allowed for several powerful features that distinguished it from numerical computation libraries like NumPy. First, Theano performed automatic differentiation—given a symbolic expression, it could automatically compute gradients with respect to any variable, which was essential for training neural networks via backpropagation. Second, Theano applied sophisticated optimization passes to the computational graph, including common subexpression elimination, constant folding, and GPU kernel fusion, often producing faster execution than naive implementations. Third, Theano provided transparent GPU acceleration without requiring users to write CUDA code explicitly; computations could be seamlessly moved to GPU devices by changing configuration flags.

The library also introduced innovations in stability optimization. When computing gradients involving exponentials or logarithms, Theano could automatically rewrite expressions to avoid numerical overflow or underflow—a technique sometimes called stability optimization that proved valuable for training deep networks. Theano's expression system supported broadcast operations similar to NumPy, allowing vectorized computations over multi-dimensional tensors. Additionally, Theano's profiling tools that could identify computational bottlenecks in symbolic graphs, helping researchers optimize their models' performance.

## Historical Context and Evolution

Theano emerged from the deep learning renaissance catalyzed by the availability of larger datasets, faster GPUs, and algorithmic advances like dropout and better activation functions. During roughly 2010–2015, Theano was the dominant framework for academic deep learning research in Python, particularly at MILA where researchers like Yoshua Bengio, Ian Goodfellow, and their students made foundational contributions. Notable deep learning architectures first implemented in Theano included early versions of convolutional neural networks, recurrent neural networks with Long Short-Term Memory (LSTM) units, and variational autoencoders.

However, Theano's architecture proved difficult to maintain and extend as the field evolved. The symbolic computational graph, while powerful, imposed a rigid execution model that complicated debugging and dynamic computation. Around 2015–2017, newer frameworks like TensorFlow (released by Google) and PyTorch (released by Facebook) offered more flexible execution models while retaining automatic differentiation capabilities. These alternatives gained rapid adoption, and Theano's development slowed significantly. The final release (Theano 1.0.0) came in 2017, after which MILA announced discontinuation of active development, though the library remains available on GitHub for historical and archival purposes.

## Relationship to The Virtual Brain

The relationship between Theano and [[the-virtual-brain]] (TVB) is primarily historical rather than operational in modern workflows. During TVB's early development phases in the late 2000s and early 2010s, Theano was considered as a potential computational backend for simulating large-scale [[neural-network]] models due to its efficiency at handling numerical arrays and its GPU acceleration capabilities. Theano's symbolic computation capabilities aligned well with certain [[neural-mass-models]] formulations that require solving systems of differential equations numerically. However, no public documentation confirms Theano was ever adopted as TVB's primary computational backend.

Modern TVB installations typically utilize NumPy-based computations for the [[neural-mass-model]] level simulations and may integrate with specialized simulators like [[nest]] for detailed spiking network simulations. The computational requirements of TVB's [[whole-brain]] simulations—which involve solving large systems of coupled differential equations representing brain region interactions—have led the development team to prioritize flexibility over the low-level optimizations that Theano provided. Today, TVB's simulation engine operates primarily through its own custom-written numerical routines rather than depending on legacy deep learning frameworks.

## Related Software

Theano's legacy is visible in several subsequent frameworks that adopted similar approaches. [[tensorflow]], developed at Google Brain, extended Theano's symbolic computation model with a more flexible dataflow graph architecture and broader deployment options. [[pytorch-geometric]], released by Meta AI (formerly Facebook), offered dynamic computational graphs that addressed Theano's rigidity limitations while retaining automatic differentiation. Within computational neuroscience specifically, [[brian2cuda]] and [[nest]] provide dedicated neural simulation environments with their own optimization strategies. [[the-virtual-brain]] represents an alternative approach to whole-brain modeling that prioritizes clinical translation and personalized brain models over raw deep learning acceleration.

Several other Python libraries for numerical computing relate to Theano's domain: numpy provides the foundational array operations that Theano built upon, while scipy offers additional scientific computing routines. The [[neural-mass-models-comparison]] page provides a broader context for evaluating simulation frameworks in whole-brain research. Within the broader ecosystem, [[brain-dynamics-toolbox]] and [[braph]] offer alternative software for analyzing brain connectivity and network dynamics.

## Key Papers

- Al-Rfou, R., Alain, G., Almahairi, A., et al. (2016). "Theano: A Python framework for fast computation of mathematical expressions." *arXiv preprint arXiv:1605.02688*. This is the primary reference describing Theano's architecture, optimization system, and performance characteristics.

- Bastien, F., Lamblin, P., Pascanu, R., et al. (2012). "Theano: new features and speed improvements." *Deep Learning and Unsupervised Feature Learning NIPS 2012 Workshop*.

- LeCun, Y., Bengio, Y., & Hinton, G. (2015). "Deep learning." *Nature*, 521(7553), 436-444. Provides broader context on the deep learning renaissance during which Theano was developed.

- Schweighofer, N., & Doya, K. (2003). "Neural simulators: Lessons from brain modeling." *Neural Networks*, 16(5), 645-653. Context for neural simulation approaches in [[computational-neuroscience]].

- Ritter, P., et al. (2008). "[[tvb|The Virtual Brain]]: a simulator for primate brain [[network-dynamics]]." *Neuroinformatics*, 6(1), 1-8. Original TVB publication documenting its computational architecture.

- Morrison, A., et al. (2008). "Realistic modeling of small-scale neuronal networks." *Neural Networks*, 21(2-3), 257-265. Background on neural mass modeling approaches used in TVB.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)