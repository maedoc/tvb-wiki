# Evaluating Spiking Neural Networks in Reinforcement Learning for Robotic Navigation

**Source**: semantic-scholar
**ID**: a7e60cef63410e68d921e4ebc97e7f531975634f
**DOI**: 10.1109/SCC66964.2025.11424934
**URL**: https://www.semanticscholar.org/paper/a7e60cef63410e68d921e4ebc97e7f531975634f
**Date**: 2025-11-24
**Year**: 2025
**Authors**: Amin Mraidi, Natabara Máté Gyöngyössy, János Botzheim
**Venue**: IEEE International Conference on Services Computing
**Citations**: 0

## Abstract

Spiking neural networks are brain-inspired models characterized by event-driven processing and temporal dynamics, offering an alternative to traditional artificial neural networks in control tasks. This study presents a high-level comparison of spiking and conventional networks as reinforcement learning policies using proximal policy optimization in three Gymnasium environments of increasing complexity as well as a ROS/Gazebo simulation-to-robot transfer setup. Both architectures share a two-layer design, with spiking models employing leaky integrate-and-fire neurons trained via surrogate gradients. Agents receive LiDAR scans and kinematic data. Results demonstrate that spiking networks match conventional models in simple tasks and sustain competitive performance in more complex settings, albeit with slower convergence and a need for lower learning rates for stable training. Deployment in the Gazebo framework validates sim-to-real transfer, overcoming practical issues like sensor noise and steering drift yet revealing distinct behavioral differences between spiking and conventional policies under noisy, real-world conditions. These findings suggest that SNNs can serve as viable alternatives to ANNs in standard RL pipelines, especially when considering future use cases in energy-efficient robotics or systems that benefit from bio-inspired processing.
