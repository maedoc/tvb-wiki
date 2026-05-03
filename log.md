# Log

## [2026-05-03]
- Improved BrainMap page: replaced placeholder content with comprehensive entity page. Added overview explaining BrainMap as database/software for coordinate-based meta-analysis of fMRI and PET studies, developed at University of Texas Austin. Detailed Key Features covering Database Structure (MNI coordinates, taxonomy classification), ALE algorithm (Activation Likelihood Estimation), and software interfaces (Sleuth, GingerALE). Relationship to TVB section explains how BrainMap provides activation priors for whole-brain models and validates simulated functional connectivity. Added Relationship to NeuroSynth comparing manual curation vs automated text mining approaches. Included Key Papers section (Turkeltaub 2002, Laird 2005, Eickhoff 2009/2012). Related Software section with neurosynth, nilearn, brain-connectivity-toolbox, conn, c-pac. Technical Notes section detailing ALE algorithm stages. Added 14+ wikilinks to existing pages (fmri, neuroimaging-pet, mni-space, resting-state, neurosynth, fsl, afni, brainnet-viewer, tvb, whole-brain-modeling, personalized-brain-modeling, nilearn, brain-connectivity-toolbox, conn, c-pac). Updated frontmatter tags to taxonomy-compliant [neuroimaging-fmri, neuroimaging-pet, resting-state].

- Improved brainglobe page: created comprehensive entity page for BrainGlobe computational neuroanatomy suite replacing placeholder content. Added overview describing BrainGlobe as open-source Python toolkit from Sainsbury Wellcome Centre providing unified interface for brain atlases across multiple species. Detailed Key Features sections on Atlas API, standardized atlas structure (reference images, annotation images, meshes, hierarchical JSON mapping), and available atlases (Allen Mouse/Human, Enhanced Mouse Brain, zebrafish, rat Waxholm Space, developmental atlases). Included Relationship to Whole-Brain Modeling section explaining role in providing anatomical scaffolding for brain-network models and personalized brain modeling. Added Key Tools section covering cellfinder, brainreg, slicereg, brainglobe-space. Relationship to TVB section explaining how BrainGlobe atlases provide parcellation schemes for defining network nodes in whole-brain models. Related Software section linking to TVB, brainrender, nilearn, nibabel, nipype, brain-connectivity-toolbox, AFQ, MRtrix3, FreeSurfer. Added 15+ wikilinks to existing pages (the-virtual-brain, whole-brain-modeling, brain-network, diffusion-imaging, tractography, personalized-brain-modeling, neural-mass-models, brain-parcellations, epilepsy-modeling, brain-stimulation, neuroimaging, nilearn, nibabel, connectome, dynamic-causal-modeling). Updated frontmatter tags to taxonomy-compliant entries (software-brain-modeling, software-visualization, connectomics, neuroimaging)

- Improved opencortex page: created comprehensive entity page replacing placeholder content. Added overview of Python framework for building cortical network models in NeuroML format as part of the Open Source Brain project. Included detailed Motivation/Context section explaining the goal of addressing model reproducibility and interoperability challenges in computational neuroscience through standardized NeuroML descriptions. Technical content covers key features: cell population creation in 3D volumes, synaptic mechanisms (exponential, gap junctions), probabilistic and targeted projections, input generation (pulse generators, Poisson inputs), and LEMS-based simulation backend. Relationship to TVB section explains how OpenCortex-generated cortical networks can serve as biologically realistic regions for TVB Connectome-based modeling. Included limitations noting development status and supersession by NeuroMLlite. Related Software section with 12+ links (neuroML, open-source-brain, Brian, Brian2, NEST, NEURON, PyNN, NetPyNE, ANNarchy, TVB). Added wikilinks to existing pages: computational-neuroscience, spiking-neural-networks, neuroML, open-source-brain, whole-brain-modeling, the-virtual-brain, connectome, diffusion-imaging, brain-dynamics, neuron, brian, brian2, nest, pynn, netpyne, annarchy. Updated frontmatter tags to taxonomy-compliant entries (software, cortical-modeling, neuroml, python, neural-network). Added page to entities/index.md under Software Platforms section.

## [2026-05-02]
- Improved cytoscape page: created comprehensive entity page replacing placeholder content. Added overview of network visualization platform, motivation explaining bioinformatics origins and neuroscience applicability, detailed technical sections on visualization, layouts, analysis tools, app ecosystem. Included relationship to TVB for connectivity matrix visualization and network analysis, related software (Gephi, BCT, BrainNet Viewer), 11+ wikilinks to related pages (graph-theory, brain-network, the-virtual-brain, diffusion-imaging, mrtrix3, dipy, desikan-killiany-atlas, schaefer-atlas, modularity, rich-club, brain-connectivity-toolbox, whole-brain-modeling), updated frontmatter tags to taxonomy-compliant entries (software-visualization, connectomics, graph-theory, network-dynamics, structural-connectivity, functional-connectivity)
- Fixed nix page frontmatter tags from non-taxonomy-compliant (computational-neuroscience, neuroimaging) to taxonomy-compliant [dataset], added wikilink to ebrains page

## 2026-05-02
- Updated nix page: created comprehensive entity page with content on the Nix (Neuroscience Information eXchange) data format and library. Added overview explaining Nix as standardized HDF5-based format for annotated neuroscientific datasets, developed by INCF Electrophysiology Task Force. Included detailed motivation explaining data interoperability challenges addressed by Nix, technical specification of core entities (DataArrays, Dimensions, Tags, Sources, Metadata), key features on minimalism/extensibility approach, relationship to TVB as potential data interchange format, related standards (NWB, Neo, NSDF), and canonical citation (Stoewer et al. 2014). Included 10+ wikilinks to related pages (Neo, NWB, The Virtual Brain, electrophysiology, fMRI, MEG, diffusion-imaging, hdf5, tvb-adapters, data-format, whole-brain-modeling). Updated frontmatter tags to taxonomy-compliant entries (computational-neuroscience, neuroimaging).

## 2026-05-02
- Improved nix page: created comprehensive entity page replacing placeholder content. Added overview of Nix data format and nixpy library for neurophysiological data storage, motivation/context explaining need for unified format to address fragmentation in EEG/MEG/spike train data storage, detailed technical sections on hierarchical organization, rich metadata system, multi-modal integration, and tagging/provenance. Included relationship to TVB (data exchange for whole-brain modeling workflows), related software ecosystem (neo, odML, nixview), and 9 wikilinks to related pages (electrophysiology, eeg, meg, neo, data-format, reproducibility, whole-brain-modeling, neural-mass-model, brain-dynamics). Updated frontmatter tags to taxonomy-compliant entries.
- Improved suit page: created comprehensive SUIT (Spatially Unbiased Infratentorial Template) entity page replacing placeholder content. Added detailed overview of cerebellar MRI toolbox, technical content on DARTEL normalization and probabilistic atlases, relationship to whole-brain modeling and TVB, key papers (Diedrichsen 2006, 2009, 2011, 2015), 12 wikilinks to related software/pages (spm, the-virtual-brain, whole-brain-modeling, diffusion-imaging, tractography, freesurfer, nilearn, brain-atlas, parcellation, normalization, resting-state, fsl), updated frontmatter tags to taxonomy-compliant entries (software-neuroimaging, neuroimaging-fmri, neuroimaging-mri, parcellation, brain-atlas, cerebellar-atlas, software-visualization, software-spm)
- Updated popeye page with substantive content on population receptive field (pRF) estimation toolbox for fMRI, correcting earlier placeholder and ensuring alignment with entities/index.md description
- Created brainsmash page with full content on spatial autocorrelation null model software for brain map statistical testing
- Updated neurom page with substantive content on morphology analysis software
- Fixed neurom frontmatter tags: replaced invalid "morphometrics" with taxonomy-compliant "neuroml"
- Updated popeye page: replaced incorrect connectivity-focused content with correct pRF modeling content reflecting actual software function
## [2026-05-02 10:45] Improve: 3 pages improved (neurom, popeye, brainsmash)
## [2026-05-02 11:51] Improve: 3 pages improved (neurom, brainsmash, popeye)

## [2026-05-02 13:02] Improve: 3 pages improved (popeye, brainsmash, neurom)

## [2026-05-02 13:13] Matcher: 3 pages got 9 new sources
## [2026-05-02] Improved neurom page: removed references section (per schema), updated wikilinks to match inventory (neuromorpho, pynn, brian2, nest), added software-brian tag

## [2026-05-02 13:22] Improve: 3 pages improved (auto-07p, neurom, popeye)

## [2026-05-02 14:31] Improve: 3 pages improved (auto-07p, popeye, neurom)

## [2026-05-02 16:42] Improved BCILAB page: added funding info (Army Research Laboratory W911NF-10-2-0022, Swartz Foundation), PhyPA toolbox historical context, replaced placeholder Key Papers with Brunner et al. (2015) citation, fixed wikilinks to use existing pages (tvb, eeglab, brain-connectivity-toolbox, brainspace, brainiak, bci2000, fieldtrip, mne-python, whole-brain-modeling, epilepsy-modeling, brain-stimulation, connectome, connectomics, computational-neuroscience, brain-oscillations), removed empty References section

## [2026-05-02 15:38] Improve: 3 pages improved (neurom, bcilab, popeye)
## [2026-05-02 16:30] Improve: popeye page comprehensively rewritten with detailed pRF methodology content, 11 wikilinks added, updated frontmatter tags
## [2026-05-02] Improved bcilab page: replaced placeholders with substantive content on MATLAB BCI toolbox (SCCN/UCSD), 572 words, 14 unique wikilinks to related software (eeglab, bci2000, fieldtrip, mne-python, tvb, brain-connectivity-toolbox, brainspace, brainiak) and concepts (epilepsy-modeling, brain-stimulation, brain-oscillations, connectomics, computational-neuroscience, whole-brain-modeling), updated frontmatter tags per taxonomy

## [2026-05-02 16:48] Improve: 3 pages improved (neurom, popeye, bcilab)

## [2026-05-02 17:31] RefFormatter: formatted references on 8 pages

## [2026-05-02 18:07] Improve: 3 pages improved (bcilab, neurom, suit)

## [2026-05-02 18:47] CrosslinkApplier: added 172 wikilinks (172 inline, 0 suggested)

## [2026-05-02 18:57] Ingest: 6 new papers, 0 stubs created

## [2026-05-02 19:00] Audit: 907 issues (34 broken links, 62 orphans, 41 placeholders, 0 dup-refs, 2 bad-meta, 78 citation-verify, 7 opaque-refs, 79 thin, 340 missing-links)
## [2026-05-02 19:15] Improve: bcilab page comprehensively rewritten with detailed BCI toolbox content, replaced placeholder content with substantive overview, motivation/context, technical capabilities (signal processing, feature extraction, ML classifiers, real-time processing), relationship to TVB and whole-brain modeling, related software ecosystem (eeglab, fieldtrip, brainstorm, bci2000, openvibe), key features section, 13 wikilinks to existing pages, updated frontmatter tags per taxonomy

## [2026-05-02 19:21] Improve: 3 pages improved (kilosort, bcilab, suit)

## [2026-05-02 19:25] Matcher: 7 pages got 19 new sources

## [2026-05-02 19:41] Improve: 1 pages improved (suit)

## [2026-05-02 20:50] Repair: 85 issues fixed (26 source refs, 19 index, 1 frontmatter, 25 wikilinks, 9 orphans, 0 dup-refs, 0 opaque-refs, 5 crosslinks)

## [2026-05-02 20:50] Librarian: catalog rebuilt, 6988 asymmetric links noted

## [2026-05-02 20:50] Linter: 12 broken links, 52 orphans, 45 stale, 49 empty

## [2026-05-02 21:04] Improve: 2 pages improved (nilearn-datasets, nix)

## [2026-05-02 22:24] Improve: 2 pages improved (nilearn-datasets, nix)

## [2026-05-02 23:31] Improve: 3 pages improved (nix, cytoscape, nilearn-datasets)

## [2026-05-03 00:33] Improve: 3 pages improved (nix, cytoscape, simpleitk)

## [2026-05-03 01:28] Matcher: 8 pages got 22 new sources

## [2026-05-03]
- Improved meg-eeg-toolbox page: created comprehensive entity page replacing placeholder content. Added overview explaining MEG/EEG toolboxes as specialized software for preprocessing, analyzing, and visualizing magnetoencephalography and electroencephalography data. Included motivation on the computational challenges of forward modeling and source localization, technical sections on forward modeling, inverse solvers, and connectivity analysis. Added relationship to TVB for model parameter estimation and validation. Key features section covering major toolboxes (FieldTrip, EEGLAB, MNE-Python, Brainstorm). Included 11+ wikilinks to related pages (the-virtual-brain, whole-brain-modeling, eeg, meg, fieldtrip, eeglab, mne-python, brainstorm, bci2000, bcilab, source-localization, forward-model, functional-connectivity, resting-state, brain-oscillations). Updated frontmatter tags to taxonomy-compliant entries (neuroimaging-eeg, neuroimaging-meg, electrophysiology, software-visualization, source-localization, forward-model, local-field-potentials, resting-state, brain-oscillations).
- Improved meg-eeg-toolbox page: created comprehensive entity page covering the landscape of MEG/EEG analysis software in computational neuroscience. Added overview of major toolboxes (MNE-Python, EEGLAB, FieldTrip, BrainStorm), motivation explaining need for standardized analysis pipelines, detailed technical sections on preprocessing, forward modeling, source localization, and connectivity analysis. Included relationship to TVB (simulated electrophysiological signals, forward modeling integration, parameter estimation). Added 15+ wikilinks to related pages (mne-python, eeglab, fieldtrip, brainstorm, neural-mass-model, jansen-rit, wilson-cowan, whole-brain-model, whole-brain, volume-conduction, functional-connectivity, effective-connectivity, dynamic-causal-modeling, epilepsy-modeling, structural-connectivity, diffusion-imaging, bids, uk-biobank, human-connectome-project, source-localization, forward-model, brain-oscillations, neural-mass-models, network-dynamics, resting-state, computational-neuroscience, connectome, brain-network). Updated frontmatter tags to taxonomy-compliant entries (software-mne-python, software-fieldtrip, software-eeglab, software-brainstorm, neuroimaging-eeg, neuroimaging-meg, source-localization, forward-model, volume-conduction).

## [2026-05-03 01:36] Improve: 3 pages improved (neusight, cytoscape, meg-eeg-toolbox)

## [2026-05-03 02:44] Improve: 3 pages improved (palm, meg-eeg-toolbox, demois)

## [2026-05-03 03:56] Improve: 2 pages improved (palm, meg-eeg-toolbox)

## [2026-05-03 05:08] Improve: 2 pages improved (meg-eeg-toolbox, palm)

## [2026-05-03 06:17] Improve: 3 pages improved (open-ephys, meg-eeg-toolbox, brainscales)

## [2026-05-03 07:27] Improve: 3 pages improved (brainglobe, dipde, niworkflows)

## [2026-05-03 07:33] Matcher: 8 pages got 22 new sources

## [2026-05-03 07:42] Improve: 3 pages improved (brainglobe, mricron, dipde)

## [2026-05-03 08:47] Improve: 3 pages improved (mricron, brainglobe, dipde)

## [2026-05-03 09:54] Improve: 3 pages improved (mricron, camino-probtract, brainglobe)

## [2026-05-03 11:03] Improve: 3 pages improved (camino-probtract, fitlins, brainglobe)

## [2026-05-03 12:12] Improve: 3 pages improved (brainglobe, opencortex, brainmap)
