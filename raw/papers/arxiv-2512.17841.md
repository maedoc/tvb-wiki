# NeuRehab: A Reinforcement Learning and Spiking Neural Network-Based Rehab Automation Framework

**Source**: semantic-scholar
**ID**: 63dcdfbb417cbcd9dadc7f29fbf29f7b85a20c41
**DOI**: 10.48550/arXiv.2512.17841
**URL**: https://www.semanticscholar.org/paper/63dcdfbb417cbcd9dadc7f29fbf29f7b85a20c41
**Date**: 2025-12-19
**Year**: 2025
**Authors**: Phani Pavan Kambhampati, Chainesh Gautam, Jagan Palaniswamy, Madhav Rao
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Recent advancements in robotic rehabilitation therapy have provided modular exercise systems for post-stroke muscle recovery with basic control schemes. But these systems struggle to adapt to patients'complex and ever-changing behaviour, and to operate within mobile settings, such as heat and power. To aid this, we present NeuRehab: an end-to-end framework consisting of a training and inference pipeline with AI-based automation, co-designed with neuromorphic computing-based control systems that balance action performance, power consumption, and observed latency. The framework consists of 2 partitions. One is designated for the rehabilitation device based on ultra-low power spiking networks deployed on dedicated neuromorphic hardware. The other resides on stationary hardware that can accommodate computationally intensive hardware for fine-tuning on a per-patient basis. By maintaining a communication channel between both the modules and splitting the algorithm components, the power and latency requirements of the movable system have been optimised, while retaining the learning performance advantages of compute- and power-hungry hardware on the stationary machine. As part of the framework, we propose (a) the split machine learning processes for efficiency in architectural utilisation, and (b) task-specific temporal optimisations to lower edge-inference control latency. This paper evaluates the proposed methods on a reference stepper motor-based shoulder exercise. Overall, these methods offer comparable performance uplifts over the State-of-the-art for neuromorphic deployment, while achieving over 60% savings in both power and latency during inference compared to standard implementations.
