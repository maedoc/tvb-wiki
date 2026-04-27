# The Cost of Relaxation: Evaluating the Error in Convex Neural Network Verification

**Source**: arxiv
**ID**: 2604.18728
**URL**: https://arxiv.org/abs/2604.18728
**Date**: 2026-04-20
**Year**: 2026
**Authors**: Merkouris Papamichail, Konstantinos Varsos, Giorgos Flouris, João Marques-Silva
**Categories**: cs.LG, cs.AI

## Abstract

Many neural network (NN) verification systems represent the network's input-output relation as a constraint program. Sound and complete, representations involve integer constraints, for simulating the activations. Recent works convexly relax the integer constraints, improving performance, at the cost of soundness. Convex relaxations consider outputs that are unreachable by the original network. We study the worst case divergence between the original network and its convex relaxations; both qualitatively and quantitatively. The relaxations' space forms a lattice, where the top element corresponds to a full relaxation, with every neuron linearized. The bottom element corresponds to the original network. We provide analytical upper and lower bounds for the $\ell_\infty$-distance between the fully relaxed and original outputs. This distance grows exponentially, w.r.t. the network's depth, and linearly w.r.t. the input's radius. The misclassification probability exhibits a step-like behavior, w.r.t. input radius. Our results are supported by experiments on MNIST, Fashion MNIST and random networks.
