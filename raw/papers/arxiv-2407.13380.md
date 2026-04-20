# Active flux methods for hyperbolic conservation laws -- flux vector splitting and bound-preservation: Two-dimensional case

**arXiv ID**: 2407.13380
**Published**: 2024-07-18
**Updated**: 2024-11-04
**Authors**: Junming Duan, Wasilij Barsukow, Christian Klingenberg
**Categories**: math.NA
**URL**: https://arxiv.org/abs/2407.13380
**PDF**: https://arxiv.org/pdf/2407.13380
**Source**: arXiv

## Abstract

This paper studies the active flux (AF) methods for two-dimensional hyperbolic conservation laws, focusing on the flux vector splitting (FVS) for the point value update and bound-preserving (BP) limitings, which is an extension of our previous work [J.M. Duan, W. Barsukow, C. Klingenberg, arXiv:2405.02447]. The FVS-based point value update is shown to address the mesh alignment issue that appeared in a quasi-2D Riemann problem along one axis direction on Cartesian meshes. Consequently, the AF methods based on the FVS outperform those using Jacobian splitting, which are prone to transonic and mesh alignment issues. A shock sensor-based limiting is proposed to enhance the convex limiting for the cell average, which can reduce oscillations well. Some benchmark problems are tested to verify the accuracy, BP property, and shock-capturing ability of our BP AF method. Moreover, for the double Mach reflection and forward-facing step problems, the present AF method can capture comparable or better small-scale features compared to the third-order discontinuous Galerkin method with the TVB limiter on the same mesh resolution, while using fewer degrees of freedom, demonstrating the efficiency and potential of our BP AF method for high Mach number flows.
