# Wiki Log

## 2026-04-24

- Improved page: [[BrainVoyager]] – Neuroimaging analysis and visualization platform
  - Complete rewrite from placeholder to full entity page (~800 words)
  - Tags: software-brain-modeling, software-visualization, neuroimaging-fmri, resting-state, task-based
  - Established 10+ wikilinks to TVB, ANTs, 3D-Slicer, FreeSurfer, FSL, SPM, structural-connectivity, functional-connectivity, dynamic-causal-modeling, parameter-estimation
  - Documented cortex-based alignment (CBA), real-time fMRI (rt-fMRI), and multi-subject analysis capabilities
  - Detailed TVB relationship: preprocessing companion for connectivity matrix generation, cortical surface export, and empirical validation
  - Comparison table showing complementary roles: BrainVoyager for empirical analysis, TVB for mechanistic modeling
  - Key papers: Goebel et al. (2006) on cortex-based alignment, Sorger et al. (2009) on rt-fMRI neurofeedback
  - Integration pathway: BrainVoyager → structural connectivity, surface meshes, parcellations → TVB simulation

- Improved page: [[PsyNeuLink]] – Graph-based cognitive neuroscience modeling framework
  - Complete rewrite from placeholder to full entity page (~700 words)
  - Tags: software-brain-modeling, whole-brain-modeling, neural-mass-models, functional-connectivity, neuroimaging-fmri
  - Established 10+ wikilinks to TVB, hybrid-architecture, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, functional-connectivity, computational-psychiatry, neural-mass-model, NEST, Brian, ANNarchy, PyTorch, TensorFlow, NeuroML
  - Documented graph-based architecture, dual-level representation (mechanism/composition), ML integration
  - Detailed TVB relationship: complementary focus—TVB for whole-brain dynamics, PsyNeuLink for cognitive tasks; outlined integration pathway
  - Key papers: Cohen & Asthana (2017) foundational paper, Cohen et al. (2020) JOSS software paper, Radulescu et al. (2021) on DL integration
  - Added to [[entities/index.md]] under Software Platforms section

- Improved page: [[PRoNTo]] – Pattern Recognition for Neuroimaging Toolbox
  - Complete rewrite from placeholder to full entity page (~700 words)
  - Tags: software-brain-modeling, neuroimaging-fmri, functional-connectivity, whole-brain-modeling
  - Established 10+ wikilinks to TVB, SPM, Nilearn, PyMVPA, CONN, GIFT, connectome, brain-network, fMRI, EEG, structural-connectivity
  - Documented MATLAB-based machine learning for neuroimaging: SVM, Gaussian Processes, MVPA classification
  - Detailed TVB relationship: complementary workflow—PRoNTo classifies empirical data, TVB simulates mechanisms; bidirectional validation
  - Key papers: Schrouff et al. (2013) foundational Neuroinformatics paper, Schrouff & Mourão-Miranda (2019) handbook chapter
  - Integration notes: seamless SPM import, searchlight and ROI analysis, cross-validation frameworks

- Improved page: [[FastSurfer]] – Deep learning-based neuroimaging pipeline for cortical surface reconstruction
  - Complete rewrite from placeholder to full entity page (~700 words)
  - Tags: software-brain-modeling, neuroimaging-processing, structural-connectivity, neuroimaging-fmri, tractography
  - Established 10+ wikilinks to TVB, FreeSurfer, ANTs, FSL, MRtrix3, NiftyReg, Desikan-Killiany Atlas, Destrieux Atlas
  - Documented deep learning segmentation with 3D U-Net, GPU-accelerated surface reconstruction
  - Detailed TVB relationship: surface mesh generation, regional parcellations, structural connectivity integration
  - Key papers: Henschel et al. (2020) introducing FastSurferCNN, Kügler et al. (2022) on FastSurferVINN resolution independence
  - Highlighted 1000× speedup over FreeSurfer recon-all with maintained accuracy

- Improved page: [[3D Slicer]] – Open-source medical image computing platform
  - Complete rewrite from placeholder to full entity page (~700 words)
  - Tags: software-brain-modeling, software-visualization, neuroimaging-dti, neuroimaging-fmri, structural-connectivity, tractography
  - Established 15+ wikilinks to TVB, FreeSurfer, FSL, MRtrix3, ANTs, HCP Pipelines, BIDS, DTI, MRI, tractography, connectome, parcellation
  - Documented multi-modal visualization, DICOM integration, SlicerDMRI extension
  - Detailed TVB relationship: preprocessing companion for atlas registration, parcellation, tractography QC, surface export
  - Comparison table showing complementary roles with TVB
  - Key papers: Pieper et al. (2006), Norton et al. (2017), Fedorov et al. (2012)
  - Added to [[entities/index.md]] under Software Platforms section

- Improved page: [[CARLsim]] – GPU-accelerated spiking neural network simulator
  - Complete rewrite from placeholder to full entity page (~800 words)
  - Tags: software-brain-modeling, spiking-neural-networks, software-nest, whole-brain-modeling
  - Established 15+ wikilinks to TVB, NEST, NEURON, Brian, ANNarchy, Izhikevich neuron model, spiking neural networks, neuromorphic computing, whole brain, brain network, synaptic plasticity
  - Documented GPU-accelerated SNN simulation with CUDA support
  - Detailed relationship to TVB: complementary approaches (spiking vs neural mass, GPU vs CPU)
  - Comparison table with NEST highlighting different scalability approaches
  - Key papers: Nageswaran et al. (2009), Beyeler et al. (2015), Richert et al. (2021)
  - Technical specifications: neuron models, plasticity rules, multi-GPU support



- Improved page: [[NiftyReg]] – Medical image registration library
  - Complete rewrite from placeholder to full entity page (~750 words)
  - Tags: software-brain-modeling, neuroimaging-processing, structural-connectivity, diffusion-imaging, tractography
  - Established 10+ wikilinks to TVB, ANTs, FSL, SPM, FreeSurfer, MRtrix3, NiftyNet, Desikan-Killiany Atlas, AAL Atlas
  - Documented rigid/affine/FFD registration algorithms, GPU acceleration, and bending energy regularization
  - Detailed TVB relationship for atlas registration, structural connectivity generation, and DTI preprocessing
  - Key papers: Modat et al. (2010) symmetric block-matching, GPU-accelerated FFD

- Improved page: [[HCP Pipelines]] – Neuroimaging preprocessing pipelines
  - Complete rewrite from placeholder to full entity page (~650 words)
  - Tags: software-brain-modeling, database-hcp, structural-connectivity, functional-connectivity, neuroimaging-fmri, neuroimaging-dti, connectomics, tractography
  - Established 10+ wikilinks to TVB, Human Connectome Project, FSL, FreeSurfer, MRtrix3, ANTs, DataLad
  - Documented structural, functional, and diffusion preprocessing stages
  - Detailed TVB relationship for connectome-based simulation workflows
  - Key papers: Glasser et al. (2013), Smith et al. (2013), Van Essen et al. (2013)

- Created page: [[DataLad]] – Distributed data management system
  - Complete entity page from placeholder (~750 words)
  - Tags: software-brain-modeling, structural-connectivity, functional-connectivity, neuroimaging-dti, neuroimaging-fmri, reproducibility, database-hcp
  - Established 12+ wikilinks to TVB, git-annex, BIDS, OpenNeuro, HCP, UK Biobank, neuroimaging tools
  - Documented git-annex integration, provenance tracking, nested datasets
  - Relationship to TVB: connectome dataset management, reproducible simulation studies, data sharing
  - Key papers: Halchenko et al. (2023), Hanke et al. (2021)
  - Added to [[index.md]] under Software Platforms section

## 2026-04-23

- Improved page: [[ANNarchy]] – Artificial Neural Network architecture for hybrid networks
  - Complete rewrite from placeholder to full entity page (~700 words)
  - Added tags: software-brain-modeling, software-nest, neural-mass-models, spiking-neural-networks, whole-brain-modeling
  - Established 10+ wikilinks to TVB, NEST, Brian, Neuron, Elephant, CUDA, structural-connectivity
  - Documented hybrid rate/spiking simulation capabilities
  - Comparison table of TVB vs ANNarchy showing complementary roles
  - Covered C++/CUDA code generation, GPU acceleration, and neuroimaging prediction tools
  - Key papers: Vitay et al. (2015), Dinkelbach et al. (2015), Hamker et al. (2017)

- Created page: [[Elephant]] – NeuralEnsemble electrophysiology analysis toolkit
  - Full entity page with 600+ words
  - Added tags: software-brain-modeling, neuroimaging-eeg, neuroimaging-meg, neural-mass-models, spiking-neural-networks
  - Minimum 5 wikilinks established
  - Covers spike train analysis, LFP processing, connectivity measures
  - Documented TVB integration pathway
- Added Elephant to [[index.md]] under Entities section
- Updated page: [[NeuroVault]] – Complete rewrite with sourced content
  - 550+ words of technical content with citations
  - 0 placeholders remaining
  - 10+ wikilinks to existing pages ([[fmri]], [[diffusion-mri]], [[functional-connectivity]], [[tvb]], [[openneuro]], etc.)
  - All tags validated against taxonomy
  - Sections: Overview, Key Features, Relationship to TVB, Community, Related Software, Key Papers, References

- Improved page: [[MOOSE]] – Multiscale Object-Oriented Simulation Environment
  - Updated from placeholder to full entity page (~700 words)
  - Added tags: neural-mass-models, spiking-neural-networks, whole-brain-modeling
  - Established 7+ wikilinks to TVB, NEST, Neuron, concepts
  - Documented multiscale capabilities and biochemical-electrical-network integration
  - Added comparison table vs TVB showing complementary roles
  - Listed key papers including Bhalla (2011), Dudani & Bhalla (2018)

## [2026-04-23 15:55] Improve: 2 pages improved (moose, neurovault)

- Improved page: [[TVB-Multiscale]] – TVB-NEST co-simulation framework
  - Updated from placeholder to full entity page (~550 words)
  - Added tags: software-tvb, software-nest, whole-brain-modeling, spiking-neural-networks, mean-field-theory, epilepsy-modeling
  - Established 8+ wikilinks to TVB, NEST, concepts (mean-field theory, spiking networks, epilepsy modeling)
  - Documented bidirectional scale translation, MPI intercommunication, hybrid network architecture
  - Covered applications in epilepsy modeling and validation of mean-field reductions
  - Added key papers including Arbor-TVB co-simulation reference
  - All placeholders replaced with sourced content

## [2026-04-23 16:07] DeepResearch: 26 papers added via focused research

## [2026-04-23 16:07] Audit: 514 issues (26 broken links, 90 orphans, 63 placeholders)

## [2026-04-23 16:07] Librarian: index rebuilt, 352 asymmetric links noted

- Improved page: [[Root]] – CERN data analysis framework
  - Complete rewrite from placeholder to full entity page (~750 words)
  - Comprehensive coverage of ROOT's I/O, statistics, and visualization features
  - Documented neuroscience applications: fMRI analysis, Monte Carlo simulations, connectivity matrices
  - Established relationship to TVB for large simulation database management
  - Added 8+ wikilinks: [[TVB]], [[NEST]], [[NEURON]], [[neuroimaging-fmri]], [[whole-brain-modeling]], etc.
  - Tags validated: software-brain-modeling, software-visualization
  - Key papers cited: Brun & Rademakers (1997) foundational publication

## [2026-04-23 16:29] Ingest: 1 new papers, 0 stubs created

## [2026-04-23 16:40] DeepResearch: 18 papers added via focused research

## [2026-04-23 16:40] Audit: 459 issues (40 broken links, 86 orphans, 59 placeholders)

## [2026-04-23 16:40] Librarian: index rebuilt, 384 asymmetric links noted

## [2026-04-23 17:16] Ingest: 45 new papers, 1 stubs created

## [2026-04-23 17:24] Improve: 2 pages improved (c-pac, mrtrix3-connectome)

## [2026-04-23 17:36] DeepResearch: 25 papers added via focused research

## [2026-04-23 17:36] Audit: 649 issues (35 broken links, 114 orphans, 96 placeholders)

## [2026-04-23 17:36] Librarian: index rebuilt, 458 asymmetric links noted

## [2026-04-23 18:26] Improve: 1 pages improved (fooof)

## [2026-04-23 21:38] Linter: 36 broken links, 112 orphans, 154 stale, 97 empty

## [2026-04-23 23:42] Linter: 36 broken links, 112 orphans, 154 stale, 97 empty

## [2026-04-24 00:31] Matcher: 69 pages got 306 new sources

## [2026-04-24 00:40] Improve: 3 pages improved (bionet, afni, steps)

## [2026-04-24 00:48] Audit: 612 issues (42 broken links, 111 orphans, 92 placeholders)

## [2026-04-24 01:07] Repair: 142 issues fixed (27 source refs, 115 index, 0 frontmatter, 0 wikilinks, 0 orphans)

## [2026-04-24 01:07] Librarian: catalog rebuilt, 476 asymmetric links noted

## [2026-04-24 01:07] Linter: 42 broken links, 111 orphans, 130 stale, 94 empty

## [2026-04-24 01:12] SoftwareMapper: 39 pages created

## [2026-04-24 01:56] Matcher: 13 pages got 45 new sources

## [2026-04-24 01:59] Improve: 3 pages improved (neuronunit, datalad, sciunit)

## [2026-04-24 03:18] Matcher: 8 pages got 28 new sources

## [2026-04-24 03:22] Improve: 3 pages improved (voxelmorph, hcp-pipelines, lfp-lib)

## [2026-04-24 04:38] Matcher: 9 pages got 37 new sources

## [2026-04-24 04:42] Improve: 3 pages improved (nipype, carlsim, niftyreg)

## [2026-04-24 06:08] Matcher: 10 pages got 34 new sources

## [2026-04-24 06:15] Improve: 3 pages improved (3d-slicer, pronto, fastsurfer)

## [2026-04-24 07:39] Matcher: 8 pages got 20 new sources

## [2026-04-24 07:45] Improve: 3 pages improved (niftynet, psyneulink, brainvoyager)
