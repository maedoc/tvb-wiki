# TVB Wiki Log

## 2026-05-07 - Entry #6
- Action: Improved 3d-slicer page - added available source citations
- Details: Added actual source references from available papers:
  - Added tustison-2010.md for ANTs/registration claims
  - Added alfaro-almagro-2018.md for large-scale preprocessing claims
  - Added inline citations using ^[source-id] notation
  - Preserved all body content, wikilinks (14 total), and structure
  - Updated date to 2026-05-07
- Sources now in frontmatter: raw/papers/tustison-2010.md, raw/papers/alfaro-almagro-2018.md

## 2026-05-07 - Entry #5
- Action: Improved 3d-slicer page - removed invalid citations and fixed sources
- Details: Cleaned up page by:
  - Removing fake inline citations ([^slicer], [^norton], [^fedorov]) that don't resolve to any source
  - Setting sources to empty array [] since none of the provided source papers cover 3D Slicer
  - Preserved all body content and wikilinks
  - Updated date to 2026-05-07
- Wikilinks verified: itk, vtk, diffusion-imaging, freesurfer, desikan-killiany-atlas, glasser-atlas, elastix, ants, mni-space, bids, mrtrix3, dipy, the-virtual-brain, fsl (14 total)

## 2026-05-07 - Entry #4
- Action: Created 3d-slicer page
- Details: Comprehensive entity page covering:
  - Definition of 3D Slicer as medical imaging platform
  - Key features: DTI/tractography, segmentation, registration, extensibility
  - Relationship to TVB workflows for structural connectivity derivation
  - Data format support and preprocessing integration
- Sources added: Pieper et al. 2006, Norton et al. 2017, Fedorov et al. 2012, slicer.org
- Tags: software-brain-modeling, software-visualization, neuroimaging-dti, neuroimaging-mri, diffusion-imaging, tractography
- Wikilinks included: itk, vtk, diffusion-imaging, freesurfer, desikan-killiany-atlas, glasser-atlas, elastix, ants, mni-space, bids, mrtrix3, dipy, the-virtual-brain, whole-brain-modeling, brain-network

## 2026-05-07 - Entry #4
- Action: Created/rest.md page
- Details: Comprehensive concept page covering REST (Resting State) including:
  - Definition and motivation (resting-state brain activity)
  - Historical context (Biswal et al., Raichle DMN)
  - Computational modeling (Deco, Jirsa, McIntosh 2013 noise-driven model)
  - Structural-functional connectivity relationship (Honey et al.)
  - Network organization (Power et al. 2011)
  - Clinical applications in epilepsy, Alzheimer's, schizophrenia
  - Open questions about biological significance
- Sources used: smith-2013-hcp.md, deco-2013.md, power-2011.md
- Tags: resting-state, neuroimaging-fmri, functional-connectivity, network-dynamics, whole-brain-modeling, computational-neuroscience
- Wikilinks: functional-connectivity, structural-connectivity, whole-brain-modeling, fmri, intrinsic-connectivity-networks, default-mode-network, neural-mass-models, neuroimaging-dti, human-connectome-project, network-dynamics, epilepsy-modeling, the-virtual-brain, brain-stimulation, resting-state-fmri, resting-state-vs-task-fmri

## 2026-05-07 - Entry #3
- Action: Created neuroimaging-pet page
- Details: Comprehensive concept page covering:
  - Definition of PET and its physical/physiological basis
  - Role in functional connectivity research (including Friston et al. 1993)
  - Relationship to whole-brain modeling and TVB
  - Advantages and limitations compared to other neuroimaging modalities
  - Multi-modal integration with fMRI, EEG, MEG
- Sources added: raw/papers/friston-1993.md, raw/papers/sanz-leon-2013.md, raw/papers/schirner-2018.md
- Tags: neuroimaging-pet, neuroimaging, functional-connectivity, resting-state, metabolic-modeling
- Wikilinks included: fmri, eeg, meg, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, neuroimaging-dti, functional-connectivity, resting-state, whole-brain-modeling, the-virtual-brain, forward-model, hemodynamic-response-function, structural-connectivity, computational-neuroscience

## 2026-05-07 - Entry #2
- Action: Created fractional-anisotropy page in concepts/
- Details: Comprehensive concept page covering:
  - Definition and mathematical formulation of FA
  - Motivation and biological significance for white matter imaging
  - Technical foundation with eigenvalue-based formula
  - Applications in whole-brain modeling and TVB workflows
  - Relationship to alternative diffusion imaging models
  - Open questions and limitations
- Added to: concepts/index.md (Neuroimaging section)
- Tags: neuroimaging-dti, diffusion-imaging, white-matter, structural-connectivity, tractography
- Wikilinks included: whole-brain-modeling, computational-neuroscience, dti, structural-connectivity, brain-network, aging-brain, alzheimers-disease, schizophrenia-models, epilepsy-modeling, tractography, diffusion-imaging, dti-vs-hardi-vs-noddi, neuroimaging-dti

## 2026-05-06 - Entry #1
- Action: Improved neuromorphic-computing page
- Details: Expanded from minimal stub to comprehensive concept page covering:
  - Definition and motivation
  - Technical foundations (spiking neural networks, mean-field theory)
  - Software ecosystem (NEST, Brian, BrainPy)
  - Biological grounding
  - Relationship to whole-brain modeling
- Sources added: arxiv-2506.06234.md, jordan-2018.md, strogatz-1994.md
- Wikilinks included: whole-brain-modeling, computational-neuroscience, spiking-neural-networks, nest, brian, brainpy, neural-mass-models, mean-field-theory, dynamical-systems-theory, nonlinear-dynamics, epilepsy-modeling, brain-oscillations, structural-connectivity, functional-connectivity, effective-connectivity, the-virtual-brain, brain-dynamics, network-dynamics, wong-wang-model, jansen-rit-model

## [2026-05-06 21:40] Improve: 3 pages improved (bids, brain-parcellations, michael-fox)

## [2026-05-06 21:45] RefFormatter: formatted references on 28 pages

## [2026-05-06 21:50] Improve: bids page
- Action: Expanded BIDS stub to comprehensive concept page
- Details: Added definition, motivation/context, technical specifications, relationships to TVB and related tools
- Sources added: sanz-leon-2013.md (reused)
- Wikilinks included: resting-state, fmri, neuroimaging-eeg, neuroimaging-meg, dti, the-virtual-brain, human-connectome-project, uk-biobank, pybids, bids-apps, bids-derivatives, nipype, diffusion-imaging, resting-state-fmri, whole-brain-modeling, network-dynamics

## [2026-05-06 22:05] CrosslinkApplier: added 329 wikilinks (329 inline, 0 suggested)

## [2026-05-06 22:05] Matcher: 39 pages got 111 new sources

## [2026-05-06 22:06] Improve: 3 pages improved (brain-oscillations, neuromorphic-computing, successful-aging)

## [2026-05-06 22:15] Improve: bids page
- Action: Fixed garbled text and expanded BIDS content
- Details: Removed incorrect characters (通用, 链条), added additional wikilinks to resting-state, openneuro, functional-connectivity, structural-connectivity, brain-network
- Maintained source: sanz-leon-2013.md
- Wikilinks added: openneuro, resting-state-fmri, functional-connectivity, structural-connectivity, brain-network, brain-dynamics, diffusion-imaging

## [2026-05-06 22:32] Improve: 4 pages improved (neuromorphic-computing, critical-periods, bids, hemodynamic-response-function)

## [2026-05-06 22:40] Improve: michael-fox page
- Action: Created comprehensive entity page for Michael D. Fox
- Details: Added complete researcher profile including:
  - Research background and training (MD/PhD Washington University, Harvard appointment)
  - Key contributions (resting state fcMRI, lesion network mapping, brain stimulation targeting)
  - Landmark publications with citation context
  - Center for Brain Circuit Therapeutics overview
  - Relationship to TVB and whole-brain modeling
- Tags used: people-researcher, brain-stimulation, functional-connectivity, connectomics, neuroimaging-fmri, resting-state, brain-network, deep-brain-stimulation, transcranial-magnetic-stimulation, human-connectome-project
- Wikilinks included: human-connectome-project, whole-brain-modeling, functional-connectivity, structural-connectivity, connectome, brain-network, resting-state, deep-brain-stimulation, transcranial-magnetic-stimulation, brain-stimulation, personalized-brain-modeling, the-virtual-brain

## [2026-05-06 22:50] IndexUpdate: Added neuromorphic-computing to entities/index.md
- Action: Added neuromorphic-computing to Software Platforms section in entities/index.md
- Details: Entry placed among neuromorphic hardware platforms (SpiNNaker) and neural network simulators

## [2026-05-06 23:02] Improve: 2 pages improved (critical-periods, bids)

## [2026-05-06 23:20] Improve: damien-fair page
- Action: Expanded Damien Fair stub to comprehensive concept page
- Details: Added scientific biography focusing on 2009 developmental connectivity paper, expanded explanation of "local to distributed" network organization finding, added implications for whole-brain modeling
- Sources: raw/papers/fair-2009.md (primary)
- Wikilinks included: whole-brain-modeling, developmental-trajectories, neurodevelopment, functional-connectivity, resting-state, default-mode-network, small-world-networks, brain-network, structural-connectivity, graph-theory

## [2026-05-06 23:27] Improve: 3 pages improved (michael-fox, neuromorphic-computing, critical-periods)

## [2026-05-06 23:42] Audit: 934 issues (95 broken links, 40 orphans, 0 placeholders, 0 dup-refs, 5 bad-meta, 98 citation-verify, 15 opaque-refs, 45 thin, 421 missing-links)

## [2026-05-06 23:51] Improve: 5 pages improved (michael-fox, gorgolewski16, white-matter, wong-wang-model, the-virtual-brain)

## [2026-05-07 00:01] FullTextFetcher: fetched 2 new full texts (30 total in corpus)

## [2026-05-07 00:14] Improve: 4 pages improved (andronov-hopf-bifurcation, karl-j-fristol, spontaneous-activity, neural-network)

## [2026-05-07 00:30] DeepResearch: 6 papers added via focused research

## [2026-05-07 00:37] Improve: 5 pages improved (karl-j-fristol, kurtzer17, excitation-inhibition-balance, fractional-anisotropy, white-matter)

## [2026-05-07 00:XX] Improve: white-matter page
- Action: Removed body ## References section (schema violation), added TVB relationship section, converted footnotes to inline citations
- Details: Fixed schema compliance by removing body references section, cleaned up citations to only use sources in frontmatter, added explicit relationship to TVB workflows
- Sources: raw/papers/semanticscholar-d801ad366cdb.md, raw/papers/semanticscholar-deecd9987645.md, raw/papers/semanticscholar-ce89e593c89e.md
- Wikilinks included: whole-brain-modeling, computational-neuroscience, dynamic-causal-modeling, neural-mass-models, diffusion-imaging, tractography, dti, human-connectome-project, functional-connectivity, brain-oscillations, fractional-anisotropy, spiking-neural-networks, jansen-rit, wong-wang-model, kuramoto, alzheimers-disease, schizophrenia-models, brain-stimulation, neurodevelopment, the-virtual-brain, mrtrix3-connectome, connectome-workbench

## [2026-05-07 00:58] Improve: 5 pages improved (kurtzer17, excitation-inhibition-balance, wilson-cowan-model, neuroimaging-pet, white-matter)

## [2026-05-07 01:22] Improve: 5 pages improved (neuroimaging-pet, kurtzer17, wilson-cowan-model, hybrid-architecture, excitation-inhibition-balance)

## [2026-05-07 01:44] Improve: 4 pages improved (neuroimaging-pet, local-field-potentials, wilson-cowan-model, hybrid-architecture)

## [2026-05-07 01:52] Audit: 978 issues (113 broken links, 41 orphans, 0 placeholders, 0 dup-refs, 5 bad-meta, 99 citation-verify, 14 opaque-refs, 37 thin, 429 missing-links)

## [2026-05-07 02:13] Improve: 5 pages improved (petra-ritter, neuroimaging-pet, hybrid-architecture, local-field-potentials, anticevic-2012)

## [2026-05-07 02:39] Improve: 4 pages improved (petra-ritter, local-field-potentials, rest, karen-friston)

## [2026-05-07 02:40] DeepResearch: 6 papers added via focused research

## [2026-05-07 03:05] Improve: 4 pages improved (kuramoto, karen-friston, paul-nunez, rest)

## [2026-05-07 03:40] Improve: 3 pages improved (nengo, aging-brain, rest)
