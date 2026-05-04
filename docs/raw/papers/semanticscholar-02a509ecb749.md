# Cycle-conditional diffusion model for noise correction of diffusion-weighted images using unpaired data

**Source**: semantic-scholar
**ID**: 02a509ecb749f34af6415314475ff06b3d6b3a1d
**DOI**: 10.1016/j.media.2025.103579
**URL**: https://www.semanticscholar.org/paper/02a509ecb749f34af6415314475ff06b3d6b3a1d
**Date**: 2025-04-01
**Year**: 2025
**Authors**: Pengli Zhu, Chaoqiang Liu, Yingji Fu, Nanguang Chen, Anqi Qiu
**Venue**: Medical Image Anal.
**Citations**: 7

## Abstract

Diffusion-weighted imaging (DWI) is a key modality for studying brain microstructure, but its signals are highly susceptible to noise due to the thermal motion of water molecules and interactions with tissue microarchitecture, leading to significant signal attenuation and a low signal-to-noise ratio (SNR). In this paper, we propose a novel approach, a Cycle-Conditional Diffusion Model (Cycle-CDM) using unpaired data learning, aimed at improving DWI quality and reliability through noise correction. Cycle-CDM leverages a cycle-consistent translation architecture to bridge the domain gap between noise-contaminated and noise-free DWIs, enabling the restoration of high-quality images without requiring paired datasets. By utilizing two conditional diffusion models, Cycle-CDM establishes data interrelationships between the two types of DWIs, while incorporating synthesized anatomical priors from the cycle translation process to guide noise removal. In addition, we introduce specific constraints to preserve anatomical fidelity, allowing Cycle-CDM to effectively learn the underlying noise distribution and achieve accurate denoising. Our experiments conducted on simulated datasets, as well as children and adolescents' datasets with strong clinical relevance. Our results demonstrate that Cycle-CDM outperforms comparative methods, such as U-Net, CycleGAN, Pix2Pix, MUNIT and MPPCA, in terms of noise correction performance. We demonstrated that Cycle-CDM can be generalized to DWIs with head motion when they were acquired using different MRI scannsers. Importantly, the denoised DWI data produced by Cycle-CDM exhibit accurate preservation of underlying tissue microstructure, thus substantially improving their medical applicability.
