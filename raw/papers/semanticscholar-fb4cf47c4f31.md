# EPISeg: Automated segmentation of the spinal cord on echo planar images using open-access multi-center data

**Source**: semantic-scholar
**ID**: fb4cf47c4f31f489911b7fa1a45149238e0f9abd
**DOI**: 10.1162/IMAG.a.98
**URL**: https://www.semanticscholar.org/paper/fb4cf47c4f31f489911b7fa1a45149238e0f9abd
**Date**: 2025-09-09
**Year**: 2025
**Authors**: Rohan Banerjee, M. Kaptan, Alexandra Tinnermann, Ali Khatibi, Alice Dabbagh, C. Büchel, Christian W Kündig, C. S. Law, Dario Pfyffer, D. Lythgoe, Dimitra Tsivaka, D. Van de Ville, Falk Eippert, Fauziyya Muhammad, Gary H. Glover, Gergely Dávid, Grace Haynes, Jan Haaker, Jonathan C. W. Brooks, J. Finsterbusch, K. Martucci, K. Hemmerling, Mahdi Mobarak-Abadi, M. Hoggarth, M. Howard, Molly G. Bright, Nawal Kinany, O. Kowalczyk, Patrick Freund, Robert L. Barry, S. Mackey, Shahabeddin Vahdat, Simon Schading, Stephen B McMahon, Todd Parish, Véronique Marchand-Pauvert, Yufen Chen, Z. Smith, K. Weber II, B. De Leener, Julien Cohen-Adad
**Venue**: Imaging neuroscience
**Citations**: 3

## Abstract

Abstract Functional magnetic resonance imaging (fMRI) of the spinal cord is relevant for studying sensation, movement, and autonomic function. Preprocessing of spinal cord fMRI data involves segmentation of the spinal cord on gradient-echo echo planar imaging (EPI) images. Current automated segmentation methods do not work well on these data, due to the low spatial resolution, susceptibility artifacts causing distortions and signal drop-out, ghosting, and motion-related artifacts. Consequently, this segmentation task demands a considerable amount of manual effort which takes time and is prone to user bias. In this work, we (i) gathered a multi-center dataset of spinal cord gradient-echo EPI with ground-truth segmentations and shared it on OpenNeuro https://openneuro.org/datasets/ds005143/versions/1.3.1 and (ii) developed a deep learning-based model, EPISeg, for the automatic segmentation of the spinal cord on gradient-echo EPI data. We observe a significant improvement in terms of segmentation quality compared with other available spinal cord segmentation models. Our model is resilient to different acquisition protocols as well as commonly observed artifacts in fMRI data. The training code is available at https://github.com/sct-pipeline/fmri-segmentation/, and the model has been integrated into the Spinal Cord Toolbox as a command-line tool.
