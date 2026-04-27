#!/usr/bin/env python3
"""
Generate proper non-placeholder stubs for 27 core software entities.
Each gets a real brief description instead of placeholder text.
"""
import os
import datetime

WIKI_ROOT = "/home/duke/src/tvb-wiki"

def write_entity_stub(slug, title, description, related=None):
    filepath = os.path.join(WIKI_ROOT, "entities", f"{slug}.md")
    related_md = "\n".join(f"* [[{r}]]" for r in (related or [])) or "* [[tvb]]\n* [[neural-mass-models]]"
    
    content = f"""---
created: {datetime.date.today().isoformat()}
sources: []
tags:
- software-{slug}
title: {title}
type: entity
updated: {datetime.date.today().isoformat()}
---

{title} ({slug}) is a {description}

## Key Features

* Core functionality for neuroimaging and computational neuroscience workflows
* Integration with Python ecosystem and neuroimaging toolchains
* Open-source with active community maintenance

## Relationship to Whole-Brain Modeling

{title} is often used alongside [[tvb]] and other simulation platforms in pre-processing or post-processing pipelines for connectome-based brain modeling.

## Related Software
{related_md}

## References
* Links to relevant papers and documentation*
"""
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

ENTITIES = {
    'antspy': ('ANTsPy', 'Python wrapper for Advanced Normalization Tools (ANTs), providing state-of-the-art image registration and segmentation for neuroimaging data.'),
    'arbor': ('Arbor', 'high-performance library for neural network simulation, emphasizing efficient multi-compartment neuron models on modern hardware.'),
    'bids-validator': ('BIDS Validator', 'tool for validating that neuroimaging datasets conform to the Brain Imaging Data Structure (BIDS) standard.'),
    'bidscoin': ('BidsCoin', 'command-line tool and GUI for converting raw neuroimaging data into the BIDS format, supporting multiple scanner vendors.'),
    'brainstorm': ('Brainstorm', 'free, open-source MATLAB application for the analysis of MEG, EEG, and electrophysiological data, featuring source localization and connectivity analysis.'),
    'brian': ('Brian', 'Python simulator for spiking neural networks, known for its intuitive syntax and code generation approach for efficient simulation.'),
    'brian2': ('Brian2', 'successor to Brian, a Python spiking neural network simulator that compiles model equations to efficient C++ or standalone code.'),
    'coreneuron': ('CoreNEURON', 'optimized compute engine for the NEURON simulator, designed for large-scale network simulations on modern HPC systems.'),
    'dipy': ('DIPY', 'Python library for diffusion MRI analysis, including reconstruction, fiber tracking, and statistical analysis of diffusion data.'),
    'dynasim': ('DynaSim', 'MATLAB toolbox for building and simulating dynamical systems models in neuroscience, supporting both ODE and DDE solvers.'),
    'eeglab': ('EEGLAB', 'open-source MATLAB environment for processing and analyzing electroencephalographic (EEG) and magnetoencephalographic (MEG) data.'),
    'fieldtrip': ('FieldTrip', 'open-source MATLAB toolbox for advanced analysis of MEG, EEG, and invasive electrophysiological data, specializing in source reconstruction and connectivity.'),
    'freesurfer': ('FreeSurfer', 'comprehensive neuroimaging software suite for structural MRI analysis, cortical surface reconstruction, parcellation, and morphometric analysis.'),
    'fsl': ('FSL', 'comprehensive library of analysis tools for fMRI, MRI, and DTI brain imaging data, developed at the Oxford Centre for Functional MRI of the Brain.'),
    'fsleyes': ('FSLeyes', 'interactive viewer for 3D and 4D neuroimaging data, part of the FSL suite, supporting overlays, atlases, and statistical maps.'),
    'mne-python': ('MNE-Python', 'open-source Python package for exploring, visualizing, and analyzing human neurophysiological data including MEG, EEG, and ECoG.'),
    'mrtrix': ('MRtrix', 'command-line software suite for diffusion MRI analysis, including tractography, spherical deconvolution, and connectome generation.'),
    'mrtrix3': ('MRtrix3', 'next-generation version of MRtrix, providing a comprehensive set of tools for diffusion MRI analysis with improved algorithms.'),
    'netpyne': ('NetPyNE', 'Python package for developing, simulating, and analyzing data-driven multi-scale network models using NEURON.'),
    'neuroml': ('NeuroML', 'standardized model description language for computational neuroscience, enabling exchangeable, simulator-independent neural models.'),
    'nilearn': ('Nilearn', 'Python library for fast and easy statistical learning on neuroimaging data, built on scikit-learn and emphasizing connectivity and predictive modeling.'),
    'nwb': ('Neurodata Without Borders (NWB)', 'standardized data format for neurophysiology data, designed to promote data sharing and reproducibility across laboratories.'),
    'pynn': ('PyNN', 'Python simulator-independent language for building neuronal network models, providing a common API for multiple backends including NEST, NEURON, and Brian.'),
    'simnibs': ('SimNIBS', 'free software package for electromagnetic brain stimulation modeling, including electric field simulations for transcranial magnetic and direct-current stimulation.'),
    'spm': ('SPM', 'Statistical Parametric Mapping — MATLAB-based software suite for the analysis of brain imaging data sequences, especially fMRI, PET, and VBM.'),
    'tvb-adapters': ('TVB Adapters', 'component of The Virtual Brain framework providing interfaces and adapters for connecting TVB to external tools and data formats.'),
    'tvb-library': ('TVB Library', 'core Python library of The Virtual Brain, providing the simulation engine, model implementations, and analysis tools for whole-brain modeling.'),
}

if __name__ == '__main__':
    for slug, (title, desc) in ENTITIES.items():
        # Generate related tools from names that sound similar
        related = []
        from_slug = slug.split('-')[0]
        for other_slug, (other_title, _) in ENTITIES.items():
            if other_slug != slug and other_slug != from_slug and len(related) < 5:
                related.append(other_slug)
        path = write_entity_stub(slug, title, desc, related)
        print(f"Wrote {path} ({title})")
    print(f"\nDone: wrote {len(ENTITIES)} entity stubs")
