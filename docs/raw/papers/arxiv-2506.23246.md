# Quantum physics-informed neural networks for Maxwell’s equations: circuit design, “black hole” barren plateaus mitigation, and GPU acceleration

**Source**: semantic-scholar
**ID**: fb865ddcd54c288e81534bab8e19b44dc93f4f2c
**DOI**: 10.1007/s42484-026-00365-w
**URL**: https://www.semanticscholar.org/paper/fb865ddcd54c288e81534bab8e19b44dc93f4f2c
**Date**: 2025-06-29
**Year**: 2025
**Authors**: Ziv Chen, Gal G. Shaviner, Hemanth Chandravamsi, Shimon Pisnoy, Steven H. Frankel, Uzi Pereg
**Venue**: Quantum Machine Intelligence
**Citations**: 4

## Abstract

Physics-Informed Neural Networks (PINNs) have emerged as a promising approach for solving partial differential equations (PDEs) by embedding the governing physics into the loss function associated with a deep neural network. In this work, a Quantum Physics-Informed Neural Network (QPINN) framework is proposed to solve two-dimensional (2D) time-dependent Maxwell’s equations. Our approach utilizes a parametrized quantum circuit (PQC) in conjunction with the classical neural network architecture and enforces physical laws, including a global energy conservation principle, during training. A quantum simulation library, TorQ - Tensor Operations for Research in Quantum systems, was developed to efficiently compute circuit outputs and derivatives by leveraging GPU acceleration based on PyTorch, enabling end-to-end training of the QPINN. The method was evaluated on two 2D electromagnetic wave propagation problems: one in free space (vacuum) and the other has an added dielectric medium. Multiple quantum circuit ansätze, input scales, and an added loss term were compared in a thorough ablation study. Furthermore, recent techniques to enhance PINN convergence, including random Fourier feature embeddings and adaptive time weighting, have been incorporated. Our results demonstrate that the QPINN achieves accuracy comparable to, and even greater than, the classical PINN baseline, while using a significantly smaller number of trainable parameters. This study also demonstrates that adding an energy conservation term to the loss stabilizes training and improves the physical fidelity of the solution in the lossless free-space case. This added term helps mitigate a new kind of barren plateau (BP) related phenomenon - “black hole” (BH) loss landscape for the quantum experiments in that scenario. By optimizing the quantum-circuit ansatz and embedding energy-conservation constraints, our QPINN achieves up to a \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$19\%$$\end{document} higher accuracy on 2D Maxwell benchmark problems compared to a classical PINN.
