# The Wrath of KAN: Enabling Fast, Accurate, and Transparent Emulation of the Global 21 cm Cosmology Signal

**Source**: semantic-scholar
**ID**: e63f169b4a208824c8f1c377031ce8d8dce71882
**DOI**: 10.3847/1538-4357/adfc49
**URL**: https://www.semanticscholar.org/paper/e63f169b4a208824c8f1c377031ce8d8dce71882
**Date**: 2025-08-15
**Year**: 2025
**Authors**: J. Dorigo Jones, B. Reyes, D. Rapetti, S. Bahauddin, J. Burns, D. W. Barker
**Venue**: Astrophysical Journal
**Citations**: 2

## Abstract

Based on the Kolmogorov–Arnold network (KAN), we present a novel emulator of the global 21 cm cosmology signal, 21cmKAN, that provides extremely fast training speed while achieving nearly equivalent accuracy to the most accurate emulator to date, 21cmLSTM. The combination of enhanced speed and accuracy facilitated by 21cmKAN enables rapid and highly accurate physical parameter estimation analyses of multiple 21 cm models, which is needed to fully characterize the complex feature space across models and produce robust constraints on the early Universe. Rather than using static functions to model complex relationships like traditional fully connected neural networks do, KANs learn expressive transformations that can perform significantly better for low-dimensional physical problems. 21cmKAN predicts a given signal for two well-known models in the community in 3.7 ms on average and trains about 75 times faster than 21cmLSTM, when utilizing the same typical GPU. In addition, 21cmKAN is able to achieve these speeds because of its learnable, data-driven transformations and its relatively small number of trainable parameters compared to a memory-based emulator. We show that 21cmKAN required less than 30 minutes to train and fit these simulated signals and obtain unbiased posterior distributions. We find that the transparent architecture of 21cmKAN allows us to conveniently interpret and further validate its emulation results in terms of the sensitivity of the 21 cm signal to each physical parameter. This work demonstrates the effectiveness of KANs and their ability to more quickly and accurately mimic expensive physical simulations in comparison to other types of neural networks.
