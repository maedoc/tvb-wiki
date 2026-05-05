# DeepMultiConnectome: Deep Multi-Task Prediction of Structural Connectomes Directly from Diffusion MRI Tractography

**Source**: semantic-scholar
**ID**: 38f08b0bfcd27e3629e69024683ebac21aa751a4
**DOI**: 10.48550/arXiv.2505.22685
**URL**: https://www.semanticscholar.org/paper/38f08b0bfcd27e3629e69024683ebac21aa751a4
**Date**: 2025-05-27
**Year**: 2025
**Authors**: Marcus J. Vroemen, Yuqian Chen, Yui Lo, Tengfei Xue, Tom Weidong Cai, Fan Zhang, J. Pluim, L. O’Donnell
**Venue**: NeuroImage
**Citations**: 1

## Abstract

Diffusion MRI (dMRI) tractography enables in vivo mapping of brain structural connections, but traditional connectome generation is time-consuming and requires gray matter parcellation, posing challenges for large-scale studies. We introduce DeepMultiConnectome, a deep-learning model that predicts structural connectomes directly from tractography, bypassing the need for gray matter parcellation while supporting multiple parcellation schemes. Using a point-cloud-based neural network with multi-task learning, the model classifies streamlines according to their connected regions across two parcellation schemes, sharing a learned representation. By classifying individual streamlines, our method's output serves as a flexible prerequisite for constructing a wide range of differently weighted connectomes. We train and validate DeepMultiConnectome on tractography from the Human Connectome Project Young Adult dataset (n=1000), labeled with an 84 and 164 region gray matter parcellation scheme. DeepMultiConnectome predicts multiple structural connectomes from a 3-million-streamline tractogram in ∼40 seconds. DeepMultiConnectome is evaluated by comparing predicted connectomes with traditional connectomes generated using the conventional method of labeling streamlines using a gray matter parcellation. The predicted connectomes show high agreement with traditionally generated connectomes across two parcellation schemes and multiple weighting strategies, and largely preserve network properties. Pearson correlations were r = 0.992 and 0.986 for streamline-count-weighted connectomes, r = 0.995 and 0.992 for SIFT2-weighted connectomes, and r = 0.775 and 0.727 for mean-FA-weighted connectomes. Test-retest analysis and downstream predictions of age and cognitive function demonstrate performance and reproducibility comparable to traditionally generated connectomes. Overall, DeepMultiConnectome provides a fast and scalable model for generating subject-specific connectomes across multiple parcellation and weighting schemes.
