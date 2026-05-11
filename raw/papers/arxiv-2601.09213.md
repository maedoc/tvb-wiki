# SpikeVAEDiff: Neural Spike-based Natural Visual Scene Reconstruction via VD-VAE and Versatile Diffusion

**Source**: semantic-scholar
**ID**: d11d08399ca03820301d6bab955ca4c63b53a33a
**DOI**: 10.48550/arXiv.2601.09213
**URL**: https://www.semanticscholar.org/paper/d11d08399ca03820301d6bab955ca4c63b53a33a
**Date**: 2026-01-14
**Year**: 2026
**Authors**: Jialuo Li, Taiyan Zhou
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Reconstructing natural visual scenes from neural activity is a key challenge in neuroscience and computer vision. We present SpikeVAEDiff, a novel two-stage framework that combines a Very Deep Variational Autoencoder (VDVAE) and the Versatile Diffusion model to generate high-resolution and semantically meaningful image reconstructions from neural spike data. In the first stage, VDVAE produces low-resolution preliminary reconstructions by mapping neural spike signals to latent representations. In the second stage, regression models map neural spike signals to CLIP-Vision and CLIP-Text features, enabling Versatile Diffusion to refine the images via image-to-image generation. We evaluate our approach on the Allen Visual Coding-Neuropixels dataset and analyze different brain regions. Our results show that the VISI region exhibits the most prominent activation and plays a key role in reconstruction quality. We present both successful and unsuccessful reconstruction examples, reflecting the challenges of decoding neural activity. Compared with fMRI-based approaches, spike data provides superior temporal and spatial resolution. We further validate the effectiveness of the VDVAE model and conduct ablation studies demonstrating that data from specific brain regions significantly enhances reconstruction performance.
