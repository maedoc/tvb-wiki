# Probabilistic Upscaling of Hydrodynamics in Geological Fractures Under Uncertainty

**arXiv ID**: 2604.15785
**Published**: 2026-04-17
**Updated**: 2026-04-17
**Authors**: Sarah Perez, Florian Doster, Hannah Menke, Ahmed ElSheikh, Andreas Busch
**Categories**: physics.comp-ph, physics.flu-dyn
**URL**: https://arxiv.org/abs/2604.15785
**PDF**: https://arxiv.org/pdf/2604.15785
**Source**: arXiv

## Abstract

Flow and transport in fractured geological media are strongly controlled by aperture heterogeneity and uncertainty in subsurface characterisation, yet most upscaling approaches rely on deterministic representations of fracture permeability. This study presents a scalable probabilistic workflow that bridges image-based fracture geometry and uncertainty-aware hydraulic predictions across scales. The approach integrates Bayesian correction of aperture-permeability model misspecification, a deep learning surrogate for predicting spatially distributed permeability statistics, and Darcy-scale flow upscaling to propagate uncertainty to effective transmissivity.   The workflow is applied to natural shear fractures from core material in the Little Grand Wash Fault damage zone (Utah) and to simplified geometries derived from the same datasets. The Bayesian component quantifies uncertainty due to measurement errors and imperfect constitutive relations, while a Residual U-Net learns the effects of local heterogeneity and spatial correlation on predicted permeability uncertainty. Together, these components generate ensembles of permeability fields that are subsequently upscaled to probabilistic macroscopic flow responses.   Results show that common empirical aperture-permeability relations are systematically biased for natural fractures, whereas the proposed probabilistic workflow yields uncertainty-aware permeability estimates consistent with physics-based behaviour. The method captures the impact of channelisation, connectivity, and complex 3D void geometries on transmissivity while quantifying the resulting uncertainty bounds. Computational efficiency arises from the proposed hybrid strategy for probabilistic upscaling, which combines physics-informed and data-driven approaches, preserves Stokes-flow consistency and supports uncertainty propagation without repeated high-fidelity simulations.
