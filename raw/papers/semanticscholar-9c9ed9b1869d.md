# Data simulator for real-time condition evaluation in manufacturing systems: evaluation in a testbench

**Source**: semantic-scholar
**ID**: 9c9ed9b1869d146ea5d62b833cb8efa791d5bfd9
**DOI**: 10.1784/cm2025.4f4
**URL**: https://www.semanticscholar.org/paper/9c9ed9b1869d146ea5d62b833cb8efa791d5bfd9
**Date**: 2025-01-01
**Year**: 2025
**Authors**: Ilaria Pietrangeli, G. Mazzuto, A. G. González, Rafael Espadas, Eneko Carrascal, Jokin Cuesta
**Venue**: Proceedings of the International Conference on Condition Monitoring and Asset Management
**Citations**: 0

## Abstract

Ensuring that a machine operates optimally is crucial for guaranteeing safety, efficiency, process stability, and high-quality outcomes in manufacturing. Therefore, monitoring and evaluating machine behaviour to detect and, eventually, promptly correct any anomalies during operation
 is increasingly essential. In this context, a Condition Evaluation tool (CE) has been designed to extract a model of normal machine behaviour using various techniques, including Artificial Intelligence (AI) algorithms and statistical methods, based on cyclic system data. In this study, data
 were collected from a testbench designed to evaluate bushing wear in a crank-slider mechanism. A Python-based Real Time Data Simulator (RTDS) was developed to preprocess these data, resample or adjust signal speed as needed, and transmit them in real time to a MongoDB (MDB) database. The CE
 tool reads the data from MDB as if from a live process, enabling near real-time condition evaluation. The system was tested using two different algorithms—statistical and AIbased (Convolutional Neural Network, CNN). Results show that while the statistical model offers more stable outputs,
 the CNN model demonstrates higher sensitivity to subtle system variations, making it more effective for detecting early-stage anomalies. However, training was limited to a reduced dataset due to hardware constraints, which may affect model generalizability and long-term reliability. Overall,
 the combined CE and RTDS framework enables dynamic, flexible, and modular real-time condition evaluation, supporting predictive maintenance and decision-making processes in manufacturing.
