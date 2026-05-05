# Pychop: Emulating Low-Precision Arithmetic in Numerical Methods and Neural Networks

**Source**: semantic-scholar
**ID**: 356d1054c3a49108075ff3ac49c541b775f10ef1
**DOI**: 10.48550/arXiv.2504.07835
**URL**: https://www.semanticscholar.org/paper/356d1054c3a49108075ff3ac49c541b775f10ef1
**Date**: 2025-04-10
**Year**: 2025
**Authors**: Erin Carson, Xinye Chen
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Motivated by the growing demand for low-precision arithmetic in computational science, we exploit lower-precision emulation in Python -- widely regarded as the dominant programming language for numerical analysis and machine learning. Low-precision training has revolutionized deep learning by enabling more efficient computation and reduced memory and energy consumption while maintaining model fidelity. To better enable numerical experimentation with and exploration of low precision computation, we developed the Pychop library, which supports customizable floating-point formats and a comprehensive set of rounding modes in Python, allowing users to benefit from fast, low-precision emulation in numerous applications. Pychop also introduces interfaces for both PyTorch and JAX, enabling efficient low-precision emulation on GPUs for neural network training and inference with unparalleled flexibility. In this paper, we offer a comprehensive exposition of the design, implementation, validation, and practical application of Pychop, establishing it as a foundational tool for advancing efficient mixed-precision algorithms. Furthermore, we present empirical results on low-precision emulation for image classification and object detection using published datasets, illustrating the sensitivity of the use of low precision and offering valuable insights into its impact. Pychop enables in-depth investigations into the effects of numerical precision, facilitates the development of novel hardware accelerators, and integrates seamlessly into existing deep learning workflows. Software and experimental code are publicly available at https://github.com/inEXASCALE/pychop.
