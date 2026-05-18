# Learning-based Segmentation of Diffusion-Weighted MR Images with Arbitrary
 q
 -Space Samplings

**Source**: semantic-scholar
**ID**: d97b37677f41df2b7117c0447bc06d647cbd8a11
**DOI**: 10.1162/imag.a.1183
**URL**: https://www.semanticscholar.org/paper/d97b37677f41df2b7117c0447bc06d647cbd8a11
**Year**: 2026
**Authors**: Christian Ewert, David Kügler, Martin Reuter
**Venue**: Imaging Neuroscience
**Citations**: 0

## Abstract


 Segmenting anatomical regions is a crucial step in many diffusion-weighted MRI (dMRI) workflows, such as region-of-interest analysis or anatomically-constrained tractography, which enable in vivo studies of brain microstructure and connectivity. However, convolutional neural networks (CNNs) – the foundation of most state-of-the-art segmentation models – require structured inputs with a fixed number of channels. This makes them ill-suited for dMRI, where acquisition protocols vary widely in q-space sampling – the number of measurements as well as their directions (b-vectors) and weightings (b-values) – resulting in unstructured data with inconsistent dimensionality across studies. As a consequence, the applicability of CNN-based methods is generally limited to the dataset on which they were trained. To address this, existing methods like DeepAnat and DDParcel rely on diffusion model fits, such as the diffusion tensor, to convert raw data into structured representations compatible with CNNs. While this enables broader applicability, it introduces lossy compression that can degrade performance. In this work, we propose a novel method that combines the geometric deep learning-based reconstruction framework DISCUS with the segmentation network VINN to directly map unstructured dMRI data to anatomical segmentations. Our segmentation approach is the first to achieve robust generalization across heterogeneous acquisition schemes using a single neural network without requiring diffusion model fits. Our approach generates the segmentation in minutes, whereas DeepAnat relies on the external FreeSurfer software, which runs for several hours. Additionally, we demonstrate generally superior segmentation performance of our approach across multiple datasets and acquisition settings with respect to DeepAnat, DDParcel, and SynthSeg.
