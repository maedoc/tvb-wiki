# BAYES-GAIT: A Bayesian Deep Neural Network for Continuous Gait Reference Trajectory Generation Using an Enhanced Loss Function

**Source**: semantic-scholar
**ID**: 9318e52fc6e02c06383cb56394740a1c80c68e05
**DOI**: 10.1109/ACCESS.2026.3668233
**URL**: https://www.semanticscholar.org/paper/9318e52fc6e02c06383cb56394740a1c80c68e05
**Year**: 2026
**Authors**: Bharat Singh, Suchit Patel, Ankit Vijayvargiya, Rajesh Kumar, Naveen Gehlot
**Venue**: IEEE Access
**Citations**: 0

## Abstract

Background: Adaptive gait trajectory prediction is essential to achieve natural and stable locomotion in prosthetic limbs and legged robots, particularly under varied conditions such as changing inclines and walking speeds. Although deep neural networks have shown potential for learning complex joint gait trajectory patterns, conventional deep neural networks often suffer from prediction bias and lack mechanisms for uncertainty estimation, which limits their reliability in dynamic or unseen environments. Methods: This study proposes a Bayesian deep neural network framework for predicting continuous joint trajectories in the sagittal plane across diverse ambulation tasks. The approach integrates Bayesian inference to estimate predictive uncertainty and enhance model generalization. A new hybrid loss function is introduced that combines the standard error of the dataset with variational mean absolute error or mean squared error, allowing the model to leverage low-variance gait segments more effectively during training. The framework is trained and evaluated using a dataset that includes varying walking speeds and inclines. Results: The proposed Bayesian model outperforms traditional state-of-the-art methods, particularly deep neural networks and finite state machine baselines, and shows up to 15% and 25% improvements, respectively, in joint trajectory prediction accuracy. Moreover, the Bayesian deep neural network provides 95% prediction intervals, indicating strong reliability and robustness under uncertain conditions. Significance: By incorporating uncertainty quantification and dataset-driven variance into the learning process, this study offers a more reliable and adaptive approach to gait modeling. These improvements support enhanced gait control in assistive technologies and legged robotic systems operating in variable terrain conditions in the real world.
