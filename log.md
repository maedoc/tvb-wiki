# Wiki Action Log

## 2026-05-06
- Improved [[abide]] page - added technical depth on parameter-estimation workflows relevant to TVB personalized-brain-modeling

## 2026-05-06
- Created [[izhikevich-neuron-model]] page - comprehensive content about the Izhikevich spiking neuron model
- Defined mathematical formulation with equations and parameter explanations
- Covered biological plasticity and diverse firing regimes (tonic/phasic spiking, bursting, Class 1/2 excitability)
- Added relationship to other neuron models (integrate-and-fire, Hodgkin-Huxley, FitzHugh-Nagumo, AdEx)
- Included computational implementations in NEST, Brian2, NEURON
- Added applications in whole-brain modeling and epilepsy
- Added 8+ wikilinks connecting to spiking-neural-networks, computational-neuroscience, neural-mass-models, nest, brian2, neuron, whole-brain-modeling, epileptor, adaptive-exponential-integrate-and-fire, hodgkin-huxley-model, fitzhugh-nagumo-model, brain-oscillations
- Added discussion of community-detection algorithms and network-dynamics theory in findings section
- Added effective-connectivity and dynamic-causal-modeling discussion for directed information flow hypotheses
- Enhanced connections to neural-mass-models, personalized-brain-modeling, and TVB workflows
- All wikilinks verified against current page inventory
- Date already at 2026-05-06 ✓

## 2026-05-06
- Fixed [[abide]] page - removed invalid "dataset" tag from frontmatter (not in taxonomy)
- Tags corrected to valid taxonomy entries: [neuroimaging-fmri, resting-state, neurodevelopment]
- Date already at 2026-05-06 ✓
- Added ABIDE entry to [[entities/index.md]] under Research Projects & Datasets section
- Verified all wikilinks in the page content are correct and resolve to existing pages
- Page content includes comprehensive coverage of ABIDE dataset, its role in ASD neuroimaging research, and Relationship to TVB section
- All 35+ wikilinks verified against current page inventory

## 2026-05-06
- Improved [[cfflib]] page - replaced placeholder with comprehensive content about Connectome File Format Library
- Added sections on overview, motivation/context, key features (supported data types: CNetwork, CSurface, CVolume, CTrack, CTimeseries, CData)
- Included relationship to TVB explaining cfflib's role in organizing connectivity data as input for whole-brain simulations
- Added 10+ wikilinks connecting to the-virtual-brain, connectome, connectomics, whole-brain-modeling, human-connectome-project, neural-mass-model, nibabel, dipy, brain-connectivity-toolkit, hcp-dataset, structural-connectivity, functional-connectivity, diffusion-mri, tractography
- Updated frontmatter with taxonomy-compliant tags and sources

## 2026-05-06
- Improved [[nitrc]] page - fixed frontmatter tags (removed invalid "database" and "software" tags, kept taxonomy-compliant tags)
- Fixed all wikilinks to proper [[format]] - added links to neuroimaging, whole-brain-modeling, connectomics, diffusion-mri, resting-state, network-dynamics, computational-neuroscience, personalized-brain-modeling
- Removed "Key Papers" section from body (sources are only in YAML frontmatter)
- Added expanded content in Relationship to TVB section emphasizing NITRC's role in providing tools for connectivity matrix generation used in whole-brain simulations
- Added expanded content in Relationship to Other Resources connecting NITRC to brainlife, BIDS, datalad, neuromorpho-toolkit, human-connectome-project, ABIDE
- All wikilinks verified against current page inventory
- Updated tags to: [neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, neuroimaging-dti, reproducibility, software-bct, software-fsl, software-spm]

## 2026-05-06
- Improved [[rockpool]] page - replaced placeholder with comprehensive content about ROCKPOOL neural simulation framework
- Added sections on overview, key features (reservoir computing, parameter estimation, neural mass models), technical implementation
- Included relationship to TVB explaining ROCKPOOL-TVB integration for whole-brain modeling
- Added 15+ wikilinks connecting to the-virtual-brain, nest, brian, jansen-rit, wilson-cowan, structural-connectivity, diffusion-imaging, functional-connectivity, whole-brain-modeling, neural-mass-models, spiking-neural-networks, brainpy, annarchy, network-dynamics, personalized-brain-modeling, dynamic-causal-modeling, human-connectome-project, tensor_flow, pytorch
- Updated frontmatter with proper tags (software-neural-simulators, reservoir-computing, recurrent-neural-networks, spiking-neural-networks, python, whole-brain-modeling, network-dynamics)

## 2026-05-06
- Improved [[abide]] page - fixed frontmatter tags (removed incorrect database-hcp tag), added [[bids]] and [[graph-theory]] wikilinks
- Tags now correctly set to [neuroimaging-fmri, resting-state, neurodevelopment]
- Added wikilink for graph-theory in analysis methods section
- Added wikilink for BIDS in data access section
- All wikilinks verified against current page inventory

## 2026-05-06
- Created [[brica2]] page - comprehensive content about Brain-inspired Computing Architecture version 2
- Added sections on overview, key features (C++ core, pybind11 bindings, message-passing architecture)
- Included relationship to TVB explaining complementary purposes (TVB for clinical modeling, BriCA2 for cognitive architecture)
- Added 12+ wikilinks connecting to neural-mass-models, tvb, nest, brian, pynest, neuroml, brainpy, spiking-neural-networks, network-dynamics, structural-connectivity
- Updated frontmatter with proper tags and date
- Improved [[neuroml2]] page - fixed frontmatter tags (replaced invalid open-source-brain with software-brain-modeling), removed invalid source references, removed body citation markers and Key Papers section
- Fixed all tags to use only taxonomy-compliant tags
- Included proper relationship to TVB via [[tvb-nest]] module
- Retained comprehensive technical content about NeuroML2 features, LEMS foundation, and interoperability
- Content includes: XML-based specification, cellular/network level modeling, validation emphasis, Relationship to Other Standards section
- 18+ wikilinks connecting to related software and concepts (neuron, nest, neuroml, spiking-neural-networks, neural-mass-model, etc.)
- Improved [[brainpy]] page - replaced placeholder with comprehensive content about BrainPy brain dynamics programming framework
- Added sections on overview, key features (JAX-based JIT compilation, spiking neural networks, neural mass models, bifurcation analysis)
- Included relationship to TVB explaining complementary purposes (TVB for whole-brain neural mass, BrainPy for detailed SNN and multi-scale modeling)
- Added 12+ wikilinks connecting to the-virtual-brain, nest, brian2, bmtk, bindsnet, pynest, jax, neural-mass-models, spiking-neural-networks, whole-brain-modeling, jansen-rit-model, wong-wang-model, wilson-cowan-model
- Updated frontmatter with proper tags (software-brain-modeling, spiking-neural-networks, neural-mass-models, python, jax) and sources (eLife paper, documentation)
- Content includes: technical architecture, ecosystem (BrainX, brainpy-state), use cases (E-I balanced networks, decision-making, whole-brain modeling)

## 2026-05-04
- Improved [[coins]] page - replaced placeholder with comprehensive content about COINS (Collaborative Informatics and Neuroimaging Suite)
- Added sections on overview, key features (MICIS, Assessment Manager, DICOM Receiver, Query Builder, Data Exchange), relationship to TVB, key papers
- Included 10+ wikilinks connecting to xnat, abide, bids, fmri, dti, eeg, meg, the-virtual-brain, connectome, structural-connectivity, functional-connectivity
- Added COINS entry to catalog.md in entities section (alphabetical position between Cmtk and Cognitive Reserve)
- Updated frontmatter with proper tags (software-brain-modeling, database, neuroimaging, data-sharing) and 3 source papers
- Content covers: data management, study/subject/scan management, HIPAA compliance, data sharing platform, format support (DICOM, NIfTI)
- Added sections on overview, key features (data acquisition, study management, security, data sharing), relationship to TVB, key papers
- Included 12+ wikilinks connecting to xnat, bids, fmri, dti, eeg, meg, the-virtual-brain, human-connectome-project, abide, brainlife, epilepsy-modeling, schizophrenia-models
- Added COINS entry to entities index under software platforms
- Updated frontmatter with proper tags and sources
- Verified all wikilinks are now valid and present in wiki inventory
- Updated [[limo]] page with comprehensive content about LIMO MEEG toolbox for statistical analysis of EEG/MEG data
- Added technical details about hierarchical linear modeling, robust statistics, and BIDS integration
- Included relationship to TVB and connections to eeglab, fieldtrip, brainstorm, and related software
- Updated [[nnu-net]] page with comprehensive content about nnU-Net deep learning segmentation framework
- Added links to related concepts: [[niftynet]], [[neuroimaging]], [[deep-learning]], etc.
- Included technical details about self-configuring pipeline, architecture variants, and biomedical applications
- Fixed wikilinks to match existing pages - replaced [[pyTorch]] with [[neural-network]], [[ANTs]] with [[ants]]
- Added nnu-net to entities index in correct alphabetical position
- Improved [[hd-bet]] page with full technical content about deep learning-based brain extraction tool
- Added sections on key features, technical considerations, relationship to TVB, and related software
- Included 16 wikilinks connecting to fsl, freesurfer, mrtrix3, hcp-dataset, and other relevant entities
- Updated [[rabies]] page - fixed tags to use only taxonomy-compliant tags (software-brain-modeling, white-matter, alzheimers-modeling, personalized-brain-modeling)
- Replaced invalid wikilinks to non-existent pages (harvard-oxford-atlas, lesion-topology, lesion-gyrus, nilearn, cat12) with valid ones from inventory
- Fixed multiple-sclerosis reference (not in taxonomy) to vascular dementia
## [2026-05-04 13:38] Improve: 5 pages improved (software-fsl, rabies, osi, limo, aomic)
- Created [[neurosift]] entity page with comprehensive content about browser-based NWB visualization tool
- Added sections on overview, key features (NWB, DANDI, OpenNeuro, NIfTI visualization), relationship to TVB, key papers
- Included 10+ wikilinks connecting to neurodata-without-borders, dandi, openneuro, the-virtual-brain, connectome-workbench, functional-connectivity, structural-connectivity, personalized-brain-modeling
- Added to entities index in software platforms section (alphabetical position between NeuroM and neuromaps)
- Updated frontmatter with proper tags (software-visualization, neurodata-without-borders, dandi, openneuro, neuroimaging, visualization-tools)

- Improved [[ccepytools]] page - transformed from placeholder to comprehensive guide to Python brain connectivity tools ecosystem
- Added sections on relationship to TVB, key packages (MNE-Connectivity, GraphVar, Cepy, BCTpy, etc.)
- Included workflow for combining external tools with TVB whole-brain modeling
- Fixed all wikilinks to use valid inventory page names
## [2026-05-04 13:38] RefFormatter: formatted references on 484 pages
- 2026-05-04: Updated AOMIC page - fixed [[epilepsy]] → [[epileptor]] wikilink, improved sources format in frontmatter

## [2026-05-04 13:49] CrosslinkApplier: added 1349 wikilinks (1349 inline, 0 suggested)

## [2026-05-04 13:56] Matcher: 10 pages got 26 new sources

## [2026-05-04 14:05] DeepResearch: 9 papers added via focused research

## 2026-05-06
- Created [[brica2]] page - comprehensive content about Brain-inspired Computing Architecture version 2
- Added sections on overview, key features (C++ core, pybind11 bindings, message-passing architecture)
- Included relationship to TVB explaining complementary purposes (TVB for clinical modeling, BriCA2 for cognitive architecture)
- Added 12+ wikilinks connecting to neural-mass-models, tvb, nest, brian, pynest, neuroml, brainpy, spiking-neural-networks, network-dynamics, structural-connectivity
- Updated frontmatter with proper tags and date

## [2026-05-06] Improve: niftynet
- Fixed duplicate frontmatter (was two YAML blocks concatenated)
- Removed invalid wikilink tag [[connectomics]] from frontmatter
- Removed body References section (sources belong in YAML frontmatter only)
- Fixed all wikilinks to match valid page names: [[TVB]]→[[the-virtual-brain]], [[NiftyReg]]→[[niftyreg]], [[ANTs]]→[[ants]], [[AAL Atlas]]→[[aal-atlas]], [[Desikan-Killiany Atlas]]→[[desikan-killiany-atlas]], etc.
- Updated frontmatter with proper taxonomy tags (software-brain-modeling, software-neuroimaging, deep-learning, tensorflow, etc.)
- Added valid source papers to frontmatter sources list
- Updated date to 2026-05-06
- Expanded content with core methodology section explaining 5-stage pipeline
- Includes 15+ wikilinks to related pages

## [2026-05-04 14:06] Audit: 941 issues (42 broken links, 54 orphans, 20 placeholders, 0 dup-refs, 3 bad-meta, 78 citation-verify, 4 opaque-refs, 75 thin, 421 missing-links)

## [2026-05-04 15:54] Improve: 4 pages improved (nistats, hcp-dataset, aomic, petsurfer)

## [2026-05-04 15:54] RefFormatter: formatted references on 10 pages

## [2026-05-04 16:01] CrosslinkApplier: added 125 wikilinks (125 inline, 0 suggested)
- Improved [[brainsuite]] page - replaced placeholders with comprehensive content about BrainSuite cortical surface extraction software
- Added sections on overview, key features (BSE skull stripping, BFC bias correction, tissue classification, cortical surface extraction, ALE thickness estimation, SVReg, USCBrain atlas, BIDS App)
- Included relationship to TVB section explaining how BrainSuite outputs (cortical surfaces, parcellations, structural connectivity) can feed into TVB whole-brain modeling workflows
- Added key papers (Shattuck & Leahy 2001, Joshi et al. 2022, Kim et al. 2023) and related software connections (connectome-workbench, bids, fmriprep, mrtrix3-connectome)
- Included 12+ wikilinks connecting to the-virtual-brain, structural-connectivity, diffusion-imaging, tractography, neuroimaging, human-connectome-project, hcp-dataset, brain-parcellations, network-dynamics, afni, connectome-workbench, bids
- Updated frontmatter with proper tags (software-brain-modeling, neuroimaging-mri, brain-parcellations, cortical-surface-extraction)
- Updated source paper reference format

## [2026-05-04 16:08] Matcher: 1 pages got 3 new sources

## [2026-05-04 16:21] DeepResearch: 85 papers added via focused research

## [2026-05-04 16:22] Audit: 936 issues (170 broken links, 55 orphans, 19 placeholders, 0 dup-refs, 3 bad-meta, 80 citation-verify, 4 opaque-refs, 74 thin, 330 missing-links)

## [2026-05-04 19:09] Librarian: catalog rebuilt, 6465 asymmetric links noted

## [2026-05-04 19:30] Create: crcns.md - created comprehensive entity page for Collaborative Research in Computational Neuroscience funding program
- Added overview, motivation, program structure, and relationship to TVB
- Included 11 wikilinks connecting to the-virtual-brain, jansen-rit-model, wong-wang-model, epileptor, structural-connectivity, functional-connectivity, parameter-estimation, variational-bayes, free-energy-principle, human-connectome-project, ebrains
- Added crcns entity to entities index under Research Projects & Datasets section

## [2026-05-04 19:09] Linter: 126 broken links, 60 orphans, 42 stale, 40 empty

## [2026-05-04 19:09] RefFormatter: formatted references on 2 pages

## [2026-05-04 19:12] Audit: 945 issues (74 broken links, 60 orphans, 33 placeholders, 0 dup-refs, 3 bad-meta, 80 citation-verify, 4 opaque-refs, 74 thin, 330 missing-links)

## [2026-05-04 19:16] CrosslinkApplier: added 75 wikilinks (75 inline, 0 suggested)

## [2026-05-04 19:20] Improve: 5 pages improved (aomic, itk-snap, fieldtrip, nilearn, rabies)

## [2026-05-04 19:21] Matcher: 9 pages got 17 new sources

## [2026-05-04 19:24] DeepResearch: 17 papers added via focused research

## [2026-05-04 19:26] Improve: 5 pages improved (mrtrix3, coreneuron, brian2, rabies, fieldtrip)

## [2026-05-04 19:33] SoftwareMapper: 25 pages created

## [2026-05-04 19:50] Improve: 5 pages improved (crcns, netpyne, cat12, netneurotools, scot)

## [2026-05-04 19:55] Improve: simbrain.md filled in (neural network simulator content)

## [2026-05-04 20:17] Improve: 5 pages improved (dynasim, spm, brainstorm, crcns, simbrain)

## [2026-05-04 20:53] Improve: 5 pages improved (petsurfer, mrtrix, brainstorm, spinal-cord-toolbox, simbrain)

## [2026-05-04 21:21] Improve: 4 pages improved (dipy, nestml, mrtrix, spinal-cord-toolbox)
- Improved [[tvb-nest]] page - transformed from placeholder into comprehensive entity page covering the TVB-NEST coupling interface
- Added sections on motivation, technical implementation (MPI intercommuncator, bidirectional scale translation)
- Included relationship to TVB and NEST, key applications (epilepsy modeling, validation, pharmacology)
- Added 18+ wikilinks to nest, tvb, neural-mass-models, spiking-neural-networks, mean-field-theory, and other related entities
- Updated frontmatter with 4 sources including sanz-leon-2013, gewaltig-diesmann-2007, arxiv-2505.16861, stefanescu-jirsa-2008

## [2026-05-04 21:39] DeepResearch: 16 papers added via focused research

## [2026-05-04 21:44] Improve: 5 pages improved (dipy, spinal-cord-toolbox, destrieux-atlas, tractoflow, tvb-nest)

## [2026-05-04 21:49] Librarian: catalog rebuilt, 6573 asymmetric links noted

## [2026-05-04 21:49] Linter: 142 broken links, 65 orphans, 37 stale, 27 empty

## [2026-05-04 21:49] RefFormatter: formatted references on 6 pages

## [2026-05-04 21:53] Audit: 1035 issues (141 broken links, 65 orphans, 22 placeholders, 0 dup-refs, 3 bad-meta, 81 citation-verify, 4 opaque-refs, 73 thin, 342 missing-links)

## [2026-05-04 21:56] CrosslinkApplier: added 160 wikilinks (160 inline, 0 suggested)

## [2026-05-04 22:01] Improve: 5 pages improved ( Allen SDK, brain-map, brain-life, trajectory, coins)

## [2026-05-04 22:02] Matcher: 15 pages got 39 new sources

## [2026-05-04 22:07] SoftwareMapper: 18 pages created

## [2026-05-04 22:11] DeepResearch: 123 papers added via focused research

## [2026-05-04 22:14] Improve: 5 pages improved (theano, brain-map, eegsynth, neurosift, brainsuite)
- Improved [[tvb-rest]] page - transformed from placeholder into comprehensive entity page covering the TVB REST API for programmatic whole-brain simulation access
- Added sections on overview, key features (simulation configuration, connectivity/data management, analysis endpoints), relationship to TVB
- Included 12+ wikilinks connecting to the-virtual-brain, tvb-library, tvb-adapters, tvb-nest, tvb-multiscale, rest, structural-connectivity, functional-connectivity, neural-mass-models, jansen-rit-model, wong-wang-model, epileptor, bids, brain-stimulation, diffusion-imaging, tractography, fmri, eeg, meg, brain-oscillations, graph-theory, bifurcation-analysis, connectome, personalized-brain-modeling, fmriprep, dmriprep, mrtrix3-connectome, afq, connectome-workbench, nipype
- Updated frontmatter with proper tags (software-tvb, software-brain-modeling, whole-brain-modeling, api)

## [2026-05-04 22:49] Improve: 5 pages improved (cifti-tools, neurokernel, tvb-rest, lfpykern, brainsuite)

## [2026-05-04 23:10] Improve: 5 pages improved (brain-life, brainsuite, bids-apps, hcp-meg2, neuroml2)

## [2026-05-04 23:20] Repair: 113 issues fixed (27 source refs, 29 index, 2 frontmatter, 37 wikilinks, 8 orphans, 0 dup-refs, 0 opaque-refs, 10 crosslinks)

## [2026-05-05 00:17] DeepResearch: 10 papers added via focused research

## [2026-05-05 02:25] DeepResearch: 28 papers added via focused research

## [2026-05-05 02:54] Audit: 1146 issues (155 broken links, 67 orphans, 20 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 9 opaque-refs, 73 thin, 354 missing-links)

## [2026-05-05 03:49] RefFormatter: formatted references on 16 pages

## [2026-05-05 04:03] CrosslinkApplier: added 241 wikilinks (241 inline, 0 suggested)

## [2026-05-05 04:08] Matcher: 23 pages got 65 new sources

## [2026-05-05 06:52] DeepResearch: 39 papers added via focused research

## [2026-05-05 07:54] Audit: 1127 issues (161 broken links, 62 orphans, 20 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 9 opaque-refs, 73 thin, 354 missing-links)

## [2026-05-05 09:00] DeepResearch: 1 papers added via focused research

## [2026-05-05 09:45] Linter: 161 broken links, 62 orphans, 20 stale, 25 empty

## [2026-05-05 09:46] Librarian: catalog rebuilt, 7119 asymmetric links noted

## [2026-05-05 09:46] RefFormatter: formatted references on 15 pages

## [2026-05-05 09:50] Audit: 988 issues (161 broken links, 62 orphans, 20 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 9 opaque-refs, 73 thin, 354 missing-links)

## [2026-05-05 09:52] SoftwareMapper: 2 pages created

## [2026-05-05 09:53] CrosslinkApplier: added 39 wikilinks (39 inline, 0 suggested)

## [2026-05-05 09:53] Matcher: 1 pages got 3 new sources

## [2026-05-05 09:55] DeepResearch: 1 papers added via focused research

## [2026-05-05 12:06] Repair: 230 issues fixed (95 source refs, 33 index, 5 frontmatter, 73 wikilinks, 9 orphans, 0 dup-refs, 0 opaque-refs, 15 crosslinks)

## [2026-05-05 12:19] DeepResearch: 1 papers added via focused research

## [2026-05-05 14:51] Audit: 948 issues (95 broken links, 54 orphans, 22 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 11 opaque-refs, 73 thin, 352 missing-links)

## [2026-05-05 14:52] DeepResearch: 6 papers added via focused research

## [2026-05-05 15:46] RefFormatter: formatted references on 1 pages

## [2026-05-05 16:01] CrosslinkApplier: added 70 wikilinks (69 inline, 1 suggested)

## [2026-05-05 16:02] Matcher: 10 pages got 28 new sources

## [2026-05-05 17:22] DeepResearch: 10 papers added via focused research

## [2026-05-05 19:52] Audit: 941 issues (98 broken links, 54 orphans, 22 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 11 opaque-refs, 73 thin, 351 missing-links)

## [2026-05-05 21:46] RefFormatter: formatted references on 3 pages

## [2026-05-05 22:09] CrosslinkApplier: added 12 wikilinks (12 inline, 0 suggested)

## [2026-05-05 22:14] Matcher: 4 pages got 12 new sources

## [2026-05-05 23:42] FullTextFetcher: fetched 5 new full texts (6 total in corpus)

## [2026-05-06 00:53] Audit: 941 issues (98 broken links, 54 orphans, 22 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 11 opaque-refs, 73 thin, 351 missing-links)

## [2026-05-06 04:19] Matcher: 1 pages got 3 new sources

## [2026-05-06 05:54] Audit: 941 issues (98 broken links, 54 orphans, 22 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 11 opaque-refs, 73 thin, 351 missing-links)

## [2026-05-06 07:16] Linter: 98 broken links, 54 orphans, 22 stale, 27 empty

## [2026-05-06 07:16] Librarian: catalog rebuilt, 7162 asymmetric links noted

## [2026-05-06 07:17] SoftwareMapper: 3 pages created

## [2026-05-06 08:30] Improve: Improved [[hrf]] page
- Replaced placeholder with comprehensive content about Hemodynamic Response Function
- Added sections on overview, mathematical models (double gamma function), HRF variability, fMRI analysis, relationship to TVB
- Included 10+ wikilinks connecting to the-virtual-brain, jansen-rit-model, wong-wang-model, bold-model, neuroimaging-fmri, functional-connectivity, effective-connectivity, dynamic-causal-modeling, brain-oscillations, whole-brain-modeling, personalized-brain-modeling
- Updated frontmatter: changed type from entity to concept, added proper tags (neuroimaging-fmri, neural-mass-models, dynamical-systems-theory, brain-dynamics), added 2 source papers
- Content covers: neurovascular coupling, canonical HRF models, gamma function mathematics, HRF estimation and deconvolution, TVB forward modeling

## [2026-05-06 07:20] FullTextFetcher: fetched 2 new full texts (8 total in corpus)

## [2026-05-06 07:20] Audit: 894 issues (98 broken links, 54 orphans, 22 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 10 opaque-refs, 73 thin, 352 missing-links)
- Updated neuroml2.md: Added wikilinks, enhanced technical content, removed redundant References section, updated date

## [2026-05-06 07:24] CrosslinkApplier: added 20 wikilinks (20 inline, 0 suggested)

## [2026-05-06 07:25] DeepResearch: 8 papers added via focused research

## [2026-05-06 07:36] Improve: 5 pages improved (abide, tvb-webui, niftynet, neuroml2, hrf)

## [2026-05-06 08:06] Improve: 3 pages improved (hnn, nifti, neuroml2)
- Improved [[nitrc-ce]] page - fixed frontmatter source citation error (wrong initiative name), removed unrelated TVB paper from sources
- Fixed invalid wikilinks (removed [[FSL]], [[trackvis]], [[fsleyes]], [[nilearn]] which don't exist in inventory)
- Corrected wikilinks to valid pages: [[camino]], [[afq]], [[brain-connectivity-toolbox]], [[dipy]]
- Added more technical content about containerized neuroimaging workflows and reproducibility
- Enhanced relationship to TVB section with details on connectivity matrix preprocessing and personalized brain modeling
- Added content about datalad-containers integration for version-controlled analysis workflows
- Updated tags to only include taxonomy-compliant tags

## [2026-05-06 08:40] Repair: 77 issues fixed (20 source refs, 23 index, 3 frontmatter, 18 wikilinks, 6 orphans, 0 dup-refs, 1 opaque-refs, 6 crosslinks)

## [2026-05-06 08:43] Improve: 3 pages improved (eegnet, hcp-dataset, abide)

## [2026-05-06 08:59] LinkRepair: fixed 763 files (3 wikilink-in-URL, 763 abs-path)

## [2026-05-06 09:08] Linter: 82 broken links, 48 orphans, 28 stale, 22 empty

## [2026-05-06 09:08] Librarian: catalog rebuilt, 7254 asymmetric links noted

## [2026-05-06 09:08] LinkRepair: fixed 5 files (0 wikilink-in-URL, 5 abs-path)

## [2026-05-06 09:08] RefFormatter: formatted references on 4 pages

## [2026-05-06 09:11] Ingest: 2 new papers, 0 stubs created

## [2026-05-06 09:12] Audit: 909 issues (82 broken links, 48 orphans, 17 placeholders, 0 dup-refs, 5 bad-meta, 85 citation-verify, 11 opaque-refs, 72 thin, 358 missing-links)

## [2026-05-06 09:16] CrosslinkApplier: added 107 wikilinks (107 inline, 0 suggested)

## [2026-05-06 09:21] DeepResearch: 2 papers added via focused research

## [2026-05-06 09:23] Matcher: 14 pages got 36 new sources

## [2026-05-06 09:24] Improve: 4 pages improved (rockpool, sinabs, dcan-tools, nitrc)

## [2026-05-06 09:27] SoftwareMapper: 1 pages created

## [2026-05-06 10:02] Improve: 2 pages improved (calamity-atlas, abcbids)

## [2026-05-06 10:32] Improve: 2 pages improved (niftynet, cfflib)

## [2026-05-06 11:04] Repair: 99 issues fixed (0 source refs, 21 index, 3 frontmatter, 62 wikilinks, 6 orphans, 0 dup-refs, 0 opaque-refs, 7 crosslinks)

## [2026-05-06 11:05] Improve: 2 pages improved (calamity-atlas, nitrc)

## [2026-05-06 11:30] DeepResearch: 1 papers added via focused research

## [2026-05-06] Improved [[cfflib]] page - replaced placeholder with comprehensive content about Connectome File Format Library
- Added sections on overview, technical architecture, supported data types (CMetadata, CNetwork, CSurface, CVolume, CTrack, CTimeserie, CData, CScript, CImagestack)
- Included relationship to TVB explaining complementary data management approaches (CFF container vs TVB's HDF5 format)
- Added 10+ wikilinks connecting to the-virtual-brain, connectivity, surface, time-series, whole-brain-modeling, connectomics, structural-connectivity, brain-network, graph-theory, small-world-networks, scale-free-networks, modularity, parameter-estimation, personalized-brain-modeling, diffusion-imaging, tractography, connectome-workbench, cifti-tools, mrtrix3-connectome, trackvis, camino
- Updated frontmatter with proper tags from taxonomy (connectomics, structural-connectivity, brain-network, computational-neuroscience, python) and date

## [2026-05-06 11:41] Improve: 2 pages improved (niftynet, calamity-atlas)
2026-05-06: Updated abide.md - Added source raw/datasets/abide-dataset.md to sources frontmatter

## [2026-05-06 12:12] Improve: 4 pages improved (neuroml, dmriprep, dandi, nitrc)

## [2026-05-06 12:45] Improve: 4 pages improved (brian2, nilearn, c302, neuroml)

## [2026-05-06 13:18] Improve: 4 pages improved (nipal, neurodamus, eden, c302)

## [2026-05-06 13:43] DeepResearch: 5 papers added via focused research

## [2026-05-06 13:50] Improve: 3 pages improved (loris, amico, neuroquery)

## [2026-05-06 14:13] Audit: 1025 issues (120 broken links, 46 orphans, 2 placeholders, 0 dup-refs, 5 bad-meta, 88 citation-verify, 14 opaque-refs, 72 thin, 385 missing-links)
2026-05-06: Improved abide.md - added dataset tag to frontmatter

## [2026-05-06 14:27] Improve: 4 pages improved (connectivity, principal-component-analysis, neuroharmonize, abide)

## [2026-05-06 14:56] Improve: 5 pages improved (neuroharmonize, connectivity, consciousness-models, nipal, adaptive-exponential-integrate-and-fire)

## [2026-05-06 15:08] RefFormatter: formatted references on 15 pages

## 2026-05-06
- Improved [[consciousness-models]] page - replaced minimal stub with comprehensive content on consciousness models in whole-brain modeling
- Added sections on theoretical foundations, critical synchronization and brain states, degeneracy and resting state manifold
- Integrated four source papers: hierarchical Kuramoto model (Myrov 2026), resting brain dynamics (Deco 2013), data-driven mean-field (Breyton 2025), network degeneracy (Gudibanda 2026)
- Added 12+ wikilinks connecting to whole-brain-modeling, computational-neuroscience, mean-field-theory, resting-state, functional-connectivity, structural-connectivity, brain-oscillations, dynamic-causal-modeling, bifurcation-theory, network-dynamics, rich-club, the-virtual-brain
- Updated frontmatter with taxonomy-compliant tags and date 2026-05-06

## [2026-05-06 15:22] Improve: 5 pages improved (fitzhugh-nagumo-model, izhikevich-neuron-model, nipal, consciousness-models, connectivity)

## [2026-05-06 15:25] CrosslinkApplier: added 583 wikilinks (583 inline, 0 suggested)

## [2026-05-06 15:29] Matcher: 43 pages got 114 new sources

## [2026-05-06 15:38] Improve: 5 pages improved (consciousness-models, community-detection, brainstorm, izhikevich-neuron-model, fitzhugh-nagumo-model)

## [2026-05-06 15:45] Librarian: catalog rebuilt, 8198 asymmetric links noted

## [2026-05-06 15:45] Linter: 78 broken links, 45 orphans, 18 stale, 9 empty

## [2026-05-06 15:45] RefFormatter: formatted references on 25 pages
