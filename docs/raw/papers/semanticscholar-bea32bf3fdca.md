# EEG-Driven Mobile Robot Intelligent Control Using ROS Integration

**Source**: semantic-scholar
**ID**: bea32bf3fdca28fcb94ef089143d95d3f188d727
**DOI**: 10.1109/CSCS66924.2025.00008
**URL**: https://www.semanticscholar.org/paper/bea32bf3fdca28fcb94ef089143d95d3f188d727
**Date**: 2025-05-27
**Year**: 2025
**Authors**: Bianca Ghinoiu, Abigail Pop, L. Vlădăreanu, V. Vlădăreanu, Lingfeng Sang, Ionel Puscasu
**Venue**: Computer Science in Cars Symposium
**Citations**: 0

## Abstract

BCIs (Brain-Computer Interfaces) utilising EEG (Electroencephalography) have reached great potential in recent years, offering possibilities in numerous domains, such as healthcare and rehabilitation, neuroscience, human-computer interaction, robotics, and even military. In this study, a hybrid CNN-LSTM (Convolutional Neural Network-Long Short-Term Memory) model trained on EEG data was used to control a mobile robot via ROS (Robot Operating System). The CNN-LSTM model was evaluated for its classification performance on motor imagery EEG tasks, achieving an accuracy of 85.8% in a cross-subject scenario. The LSTM part of our architecture incorporates two BiLSTM modules to capture temporal dependencies in both forward and backwards directions, while the spatial features are extracted through convolutional layers. The model was trained on a relatively small public dataset containing four classes of movement (right hand, left hand, feet, tongue). Despite the data size, the BiLSTM-based model proved its generalisation capability and feasibility for EEG decoding in real-time robotic control. In real-time, the EEG signals were classified using the best model, and the results were mapped to robot actions. The classification system and the mobile robot communicated through ROS, achieving a low-latency response of about 200 ms after processing the EEG signals. This work showcases how integrating a BiLSTM model positively impacts the performance of a system with limited time-series training data and contributes a practical approach for an EEG-based BCI to control mobile robots.
