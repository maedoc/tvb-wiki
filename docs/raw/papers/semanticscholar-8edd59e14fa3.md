# Enhanced Brain Stroke Lesion Segmentation in MRI Using a 2.5D Transformer Backbone U-Net Model

**Source**: semantic-scholar
**ID**: 8edd59e14fa344f0e906c76f07f508d80723647c
**DOI**: 10.3390/brainsci15080778
**URL**: https://www.semanticscholar.org/paper/8edd59e14fa344f0e906c76f07f508d80723647c
**Date**: 2025-07-22
**Year**: 2025
**Authors**: Mahsa Karimzadeh, Hadi Seyedarabi, Ata Jodeiri, Reza Afrouzian
**Venue**: Brain Science
**Citations**: 3

## Abstract

Background/Objectives: Accurate segmentation of brain stroke lesions from MRI images is a critical task in medical image analysis that is essential for timely diagnosis and treatment planning. Methods: This paper presents a novel approach for segmenting brain stroke lesions using a deep learning model based on the U-Net neural network architecture. We enhanced the traditional U-Net by integrating a transformer-based backbone, specifically the Mix Vision Transformer (MiT), and compared its performance against other commonly used backbones such as ResNet and EfficientNet. Additionally, we implemented a 2.5D method, which leverages 2D networks to process three-dimensional data slices, effectively balancing the rich spatial context of 3D methods and the simplicity of 2D methods. The 2.5D approach captures inter-slice dependencies, leading to improved lesion delineation without the computational complexity of full 3D models. Utilizing the 2015 ISLES dataset, which includes MRI images and corresponding lesion masks for 20 patients, we conducted our experiments with 4-fold cross-validation to ensure robustness and reliability. To evaluate the effectiveness of our method, we conducted comparative experiments with several state-of-the-art (SOTA) segmentation models, including CNN-based UNet, nnU-Net, TransUNet, and SwinUNet. Results: Our proposed model outperformed all competing methods in terms of Dice Coefficient and Intersection over Union (IoU), demonstrating its robustness and superiority. Our extensive experiments demonstrate that the proposed U-Net with the MiT Backbone, combined with 2.5D data preparation, achieves superior performance metrics, specifically achieving DICE and IoU scores of 0.8153 ± 0.0101 and 0.7835 ± 0.0079, respectively, outperforming other backbone configurations. Conclusions: These results indicate that the integration of transformer-based backbones and 2.5D techniques offers a significant advancement in the accurate segmentation of brain stroke lesions, paving the way for more reliable and efficient diagnostic tools in clinical settings.
