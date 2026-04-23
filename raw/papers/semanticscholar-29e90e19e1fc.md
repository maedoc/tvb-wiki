# A transformer network for high-throughput materials characterization with x-ray photoelectron spectroscopy

**Source**: semantic-scholar
**ID**: 29e90e19e1fc3f504710dedd25c96881fd734b9d
**DOI**: 10.1063/5.0296600
**URL**: https://www.semanticscholar.org/paper/29e90e19e1fc3f504710dedd25c96881fd734b9d
**Date**: 2025-10-16
**Year**: 2025
**Authors**: Florian Simperl, Wolfgang S. M. Werner
**Venue**: Journal of Applied Physics
**Citations**: 1

## Abstract

The rapid increase of x-ray photoelectron spectroscopy (XPS) as a reliable surface sensitive materials characterization instrument at large-scale synchrotron facilities and emerging autonomous labs calls for a standardized, low-latency, and reproducible quantitative analysis workflow. The notoriously time-consuming and challenging task of spectra interpretation is addressed by combining XPS spectra simulation based on the partial intensity approach with modern data science techniques. We train a transformer neural network on a standardized, open-access XPS survey-spectra repository generated with the NIST Standard Reference Database 100 Simulation of Electron Spectra for Surface Analysis (SESSA). Running SESSA in parallel on the Austrian Scientific Computing infrastructure, we simulate more than 8×106 survey spectra for 7587 synthesizable inorganic and organic bulk compounds under an AlKα excitation source and the magic-angle geometry. We apply experimentally informed data augmentations to account for varying experimentally observed noise, peak broadening, and chemical shifts. The model infers elemental composition from survey spectra correctly for 85% of compounds in the test set (90% when excluding hydrogen). Over 80% of predicted elemental atomic concentrations deviate by less than 20% from ground truth, meeting typical experimental quantification thresholds. We report the full training and hyperparameter tuning workflow and describe benefits relative to conventional peak fitting as the fully trained model retrieves instantaneously the material information without any preprocessing steps. The workflow is adaptable to customized experimental input parameters, establishing a foundation for high-throughput, standardized, and ultimately autonomous quantitative XPS analysis.
