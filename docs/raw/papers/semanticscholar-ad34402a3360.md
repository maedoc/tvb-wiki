# Symmetry-Driven Fault-Tolerant Synchronization in Multi-Robot Systems: Comparative Simulation of Adaptive Neural and Classical Controllers

**Source**: semantic-scholar
**ID**: ad34402a336006336559b35408e792f391cd71a8
**DOI**: 10.3390/sym17040591
**URL**: https://www.semanticscholar.org/paper/ad34402a336006336559b35408e792f391cd71a8
**Date**: 2025-04-13
**Year**: 2025
**Authors**: Claudio Urrea, Pablo Sari
**Venue**: Symmetry
**Citations**: 2

## Abstract

This study presents a framework for designing symmetry-aware cooperative controllers to synchronize two SCARA LS3-B401S robots, ensuring precision, adaptability, and fault tolerance in flexible manufacturing environments. Four control strategies—Proportional–Integral–Derivative (PID), Adaptive Sliding Mode Control (ASMC), Adaptation-Enabled Neural Network (ANN), and Inverse-Dynamics with Disturbance Observer (ID-DO)—were evaluated through high-fidelity MATLAB/Simulink simulations (fixed 1 ms step size, ode4 solver), using dynamic SolidWorks 2022 models validated under realistic perturbations, including ±0.0005 rad sensor noise and ±5% mass variation. Among the strategies, the ANN controller—implemented as an 8-10-4 multi-layer perceptron—achieved the highest performance, consistently reducing trajectory errors by over 99%, maintaining symmetry deviations below 0.001 rad, and recovering from ±0.08 rad disturbances in 0.12 s. Its stabilization time averaged 0.247 s across joints, and energy consumption dropped to 0.01 J/s, representing a 98% improvement over PID. Despite a higher computational load (12.5 MFLOPS, 2.80 ms per iteration), GPU acceleration brought execution times below 1.4 ms, ensuring compliance with industrial 5 ms control cycles. These results establish a scalable foundation for next-generation multi-robot systems, with planned physical validation on SCARA LS3-B401S robots equipped with high-resolution encoders and advanced processors. By leveraging symmetry-driven coordination (S=I), the proposed framework supports resilient, sustainable, and high-precision manufacturing, aligned with the goals of Industry 5.0.
