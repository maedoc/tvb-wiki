# Improved Source Localization of Auditory Evoked Fields using Reciprocal BEM-FMM

**Source**: semantic-scholar
**ID**: 87fcd15931add607d677bbf6190b9190a0f11002
**DOI**: 10.1101/2025.05.09.653081
**URL**: https://www.semanticscholar.org/paper/87fcd15931add607d677bbf6190b9190a0f11002
**Date**: 2025-05-14
**Year**: 2025
**Authors**: Derek A. Drumm, Guillermo Nuñez Ponasso, A. Linke, G. Noetscher, Burkhard Maess, T. Knösche, J. Haueisen, J. Lewine, Christopher Abbott, S. Makaroff, Zhi-De Deng
**Venue**: bioRxiv
**Citations**: 2

## Abstract

The precise localization of auditory evoked fields (AEFs) from magnetoencephalography (MEG) data is very important for the functional understanding of the auditory cortex in medicine and cognitive neuroscience. The numerical solution of the field equations in the human head using the boundary element method (BEM) is a powerful tool for achieving this. We hypothesized that the spatial resolution of the BEM is crucial for the achievable accuracy. However, in classical BEM (as implemented, e.g., in MNE-Python), very high resolutions are impractical due to the associated prohibitive computational effort. In contrast, our recently introduced reciprocal boundary element fast multipole method (reciprocal BEM-FMM) allows for hitherto unprecedented spatial resolution. In this work, we apply our reciprocal BEM-FMM technique for source estimation to localize AEFs, and we compare our results with the source estimates produced using a 3-layer BEM model (standard BEM) via MNE-Python. We first validate our methodology through comparison of source estimates of simulated N1m components of AEFs using a receiver operating characteristic (ROC) measure. While we obtain ROC measures of about 80% for the standard BEM, reciprocal BEM-FMM reaches about 90%, a significant statistical improvement. We then apply this methodology to analyze the source estimates of experimental data obtained from a cohort of 7 participants subjected to binaural auditory stimulation. Using a dispersion measurement to quantify the focality of localized sources, we find improvements upwards of 30% using reciprocal BEM-FMM over the standard BEM. Analyses from both simulated and experimental data show localization of AEFs using high-resolution reciprocal BEM-FMM is significantly better in terms of accuracy and focality than those estimates of the low-resolution standard BEM. We therefore recommend using the high-resolution reciprocal BEM-FMM to utilize high spatial anatomical precision for the modeling of neural activity.
