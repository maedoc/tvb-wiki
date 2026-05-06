# A co-simulation framework for biosensor modeling and real-time signal processing: integration of COMSOL and CODIS+

**Source**: semantic-scholar
**ID**: 0a3211f3b862d64ffb06e47752f268469db4d307
**DOI**: 10.7717/peerj-cs.3372
**URL**: https://www.semanticscholar.org/paper/0a3211f3b862d64ffb06e47752f268469db4d307
**Date**: 2025-11-18
**Year**: 2025
**Authors**: S. A. Alshaya, Ahmed Hadded, M. Amar, Mossaad Ben Ayed
**Venue**: PeerJ Computer Science
**Citations**: 0

## Abstract

The accurate and efficient simulation of biosensors is essential for applications in healthcare, environmental monitoring, and diagnostics. This study presents a co-simulation framework integrating COMSOL Multiphysics and Continuous DIscrete Simulation (CODIS+), enabling a synchronized and multi-domain simulation approach to enhance the accuracy and execution time estimation of biosensor systems. The proposed framework leverages COMSOL for high-fidelity multiphysics modeling of biosensor behavior and CODIS+ for real-time signal processing, incorporating a 1D Convolutional Neural Network (CNN) for advanced noise reduction. Furthermore, Worst-Case Execution Time (WCET) estimation is implemented to ensure predictable real-time performance, relying on profiling tools within SystemC and CODIS+. Unlike traditional standalone simulations, the proposed framework eliminates iterative feedback between control and physical modeling, optimizing computational efficiency while maintaining high detection accuracy. A high-fidelity COMSOL model is used as the reference for validation due to the absence of experimental data, ensuring a reliable benchmark for performance evaluation. The framework achieves a low Execution Time Error (ETE) of approximately 4%, validating the precision of execution time estimation and ensuring computational predictability. Performance evaluation is conducted using Root Mean Square Error (RMSE) and Signal-to-Noise Ratio (SNR) metrics. The proposed approach achieves a significant reduction in RMSE (from 7.8 to 2.1) and outperforms traditional noise reduction techniques in terms of SNR improvement, demonstrating its effectiveness in preserving biosensor signal integrity. These results confirm that integrating physics-based modeling with AI-driven noise filtering enhances both biosensor signal accuracy and real-time feasibility. The validation presented in this study is based solely on simulation and profiling results; hardware-level testing is planned for future work. The proposed co-simulation framework presents a scalable and reliable solution for optimizing biosensor design and real-time signal processing, ensuring its applicability in critical biomedical and environmental monitoring applications. It underscores the extensibility, modularity, and reusability of our integration approach, allowing other COMSOL models and CODIS+ functionalities to be easily incorporated and customized.
