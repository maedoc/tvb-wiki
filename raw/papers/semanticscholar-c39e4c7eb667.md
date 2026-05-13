# Streamline tractography of the fetal brain in utero with machine learning

**Source**: semantic-scholar
**ID**: c39e4c7eb667b46c19ad1da35bf04ed357b690ad
**DOI**: 10.1162/imag_a_00537
**URL**: https://www.semanticscholar.org/paper/c39e4c7eb667b46c19ad1da35bf04ed357b690ad
**Date**: 2025-04-09
**Year**: 2025
**Authors**: Weide Liu, Camilo Calixto, Simon K. Warfield, Davood Karimi
**Venue**: Imaging neuroscience
**Citations**: 0

## Abstract

Abstract Diffusion-weighted magnetic resonance imaging (dMRI) is the only non-invasive tool for studying white matter tracts and structural connectivity of the brain. These assessments rely heavily on tractography techniques, which reconstruct virtual streamlines representing white matter fibers. Much effort has been devoted to improving tractography methodology for adult brains, while tractography of the fetal brain has been largely neglected. Fetal tractography faces unique difficulties due to low dMRI signal quality, immature and rapidly developing brain structures, and paucity of reference data. To address these challenges, this work presents a machine learning model, based on a deep neural network, for fetal tractography. The model input consists of five different sources of information: (1) Voxel-wise fiber orientation, inferred from a diffusion tensor fit to the dMRI signal; (2) Directions of recent propagation steps; (3) Global spatial information, encoded as normalized distances to keypoints in the brain cortex; (4) Tissue segmentation information; and (5) Prior information about the expected local fiber orientations supplied with an atlas. In order to mitigate the local tensor estimation error, a large spatial context around the current point in the diffusion tensor image is encoded using convolutional and attention neural network modules. Moreover, the diffusion tensor information at a hypothetical next point is included in the model input. Filtering rules based on anatomically constrained tractography are applied to prune implausible streamlines. We trained the model on manually-refined whole-brain fetal tractograms and validated the trained model on an independent set of 11 test subjects with gestational ages between 23 and 36 weeks. Results show that our proposed method achieves superior performance across all evaluated tracts. Qualitative assessments on independent data from the Developing Human Connectome Project demonstrated the generalizability of our method. The new method can significantly advance the capabilities of dMRI for studying normal and abnormal brain development in utero.
