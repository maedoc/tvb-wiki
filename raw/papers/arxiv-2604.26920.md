# Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction

**Source**: arxiv
**ID**: 2604.26920
**URL**: https://arxiv.org/abs/2604.26920
**Date**: 2026-04-29
**Year**: 2026
**Authors**: David Novikov, Eilon Vaknin, Narek Tumanyan, Mark Sheinin
**Categories**: cs.CV

## Abstract

The task of capturing and rendering 3D dynamic scenes from 2D images has become increasingly popular in recent years. However, most conventional cameras are bandwidth-limited to 30-60 FPS, restricting these methods to static or slowly evolving scenes. While overcoming bandwidth limitations is difficult for general scenes, recent years have seen a flurry of computational imaging methods that yield high-speed videos using conventional cameras for specific applications (e.g., motion capture and particle image velocimetry). However, most of these methods require modifications to a camera's optics or the addition of mechanically moving components, limiting them to a single-view high-speed capture. Consequently, these methods cannot be readily used to capture a 3D representation of rapid scene motion. In this paper, we propose a novel method to capture and reconstruct a volumetric representation of a high-speed scene using only unaugmented low-speed cameras. Instead of modifying the hardware or optics of each individual camera, we encode high-speed scene dynamics by illuminating the scene with a rapid, sequential color-coded sequence. This results in simultaneous multi-view capture of the scene, where high-speed temporal information is encoded in the spatial intensity and color variations of the captured images. To construct a high-speed volumetric representation of the dynamic scene, we develop a novel dynamic Gaussian Splatting-based approach that decodes the temporal information from the images. We evaluate our approach on simulated scenes and real-world experiments using a multi-camera imaging setup, showing first-of-a-kind high-speed volumetric scene reconstructions.
