# High-Definition MEG Source Estimation using the Reciprocal Boundary Element Fast Multipole Method

**Source**: semantic-scholar
**ID**: cd05b14603f7e8d2fb9a659827b012cfe8208eb7
**DOI**: 10.1101/2025.03.21.644601
**URL**: https://www.semanticscholar.org/paper/cd05b14603f7e8d2fb9a659827b012cfe8208eb7
**Date**: 2025-03-24
**Year**: 2025
**Authors**: Guillermo Nuñez Ponasso, Derek A. Drumm, Abbie Wang, G. Noetscher, Matti Hämäläinen, T. Knösche, Burkhard Maess, J. Haueisen, S. Makaroff, T. Raij
**Venue**: bioRxiv
**Citations**: 2

## Abstract

Magnetoencephalographic (MEG) source estimation relies on the computation of the gain (lead-field) matrix, which embodies the linear relationship between the amplitudes of the sources and the recorded signals. However, with a realistic forward model, the calculation of the gain matrix in a “direct” fashion is a computationally expensive task because the number of dipolar sources in standard MEG pipelines is often limited to ∼10,000. We propose a fast approach based on the reciprocal relationship between MEG and transcranial magnetic stimulation (TMS). This approach couples naturally with the charge-based boundary element fast multipole method (BEM-FMM), which allows us to efficiently generate gain matrices for high-resolution multi-layer non-nested meshes involving source spaces of up to a ∼1 million dipoles. We evaluate our approach by performing MEG source reconstruction against simulated data (at varying noise levels) obtained from the direct computation of MEG readings from 2000 different dipole positions over the cortical surface of 5 healthy subjects. Additionally, we test our methods with real MEG data from evoked somatosensory fields by right-hand median nerve stimulation in these same 5 subjects. We compare our experimental source reconstruction results against the standard MNE-Python source reconstruction pipeline.
