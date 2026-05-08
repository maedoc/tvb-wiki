# Characterizing continuous and discrete hybrid latent spaces for structural connectomes

**Source**: semantic-scholar
**ID**: 70409a1c38a8724baddff74319980c34cf0cc2da
**DOI**: 10.1117/12.3086529
**URL**: https://www.semanticscholar.org/paper/70409a1c38a8724baddff74319980c34cf0cc2da
**Date**: 2025-11-20
**Year**: 2025
**Authors**: Gaurav Rudravaram, Lianrui Zuo, Adam M. Saunders, Michael E. Kim, Praitayini Kanakaraj, N. Newlin, Aravind R. Krishnan, Elyssa M. McMaster, Chloe Cho, Susan M. Resnick, L. Beason-Held, D. Archer, Timothy J. Hohman, Daniel Moyer, Bennett A. Landman
**Venue**: Medical Imaging
**Citations**: 0

## Abstract

Structural connectomes are detailed graphs that map how different brain regions are physically connected, offering critical insight into aging, cognition, and neurodegenerative diseases. However, these connectomes are high-dimensional and densely interconnected, which makes them difficult to interpret and analyze at scale. While low-dimensional spaces like PCA and autoencoders are often used to capture major sources of variation, their latent spaces are generally continuous and cannot fully reflect the mixed nature of variability in connectomes---which often include both continuous (e.g., connectivity strength) and discrete factors (e.g., imaging site). Motivated by this, we propose a variational autoencoder (VAE) with a hybrid latent space that jointly models the discrete and continuous components. We analyze a large dataset of 5,761 connectomes from 6 Alzheimer’s disease studies with 10 unique acquisition protocols. Each connectome represents a single scan from a unique subject (3579 females, 2182 males), aged 22 to 102, with 4338 cognitively normal, 809 with mild cognitive impairment (MCI), and 614 with Alzheimer’s disease (AD). Each connectome contains 121 brain regions defined by the BrainCOLOR atlas. We train our hybrid VAE in an unsupervised way and study what each component captures. We find that the discrete space is particularly effective at capturing subtle site-related differences, achieving an Adjusted Rand Index (ARI) of 0.65 with site labels, significantly outperforming traditional methods like PCA and standard VAE followed by clustering (p << 0.05). These results demonstrate that the hybrid latent space can disentangle distinct sources of variability in connectomes in an unsupervised manner, offering potential for large-scale connectome analysis.
