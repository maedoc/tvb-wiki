# Wiki Log

## 2026-04-24

- Improved page: [[Stochastic Differential Equations]] – Concept page on noise-driven dynamics in neural systems
  - Complete rewrite from sparse bullet-point outline to full concept page (~720 words)
  - Tags: stochastic-differential-equations, neural-mass-models, whole-brain-modeling, dynamical-systems-theory, nonlinear-dynamics, network-dynamics, mean-field-theory, fokker-planck-equation, resting-state, brain-oscillations
  - Established 18+ wikilinks: resting-state, whole-brain, functional-connectivity, tvb, neural-mass-models, fmri, eeg, meg, neural-mass-model, brain-oscillations, structural-connectivity, jansen-rit, wilson-cowan, fokker-planck-equation, bifurcation-analysis, parameter-estimation, dynamical-systems-theory, nonlinear-dynamics, spiking-neural-networks, mean-field-theory
  - Expanded opening paragraph with plain definition of SDEs as probability-distribution evolution equations bridging biophysics and empirical recordings
  - Added motivation/context section explaining tension between deterministic ODE elegance and biological variability in resting-state and whole-brain modeling
  - Replaced list-only Langevin/Itô/Stratonovich notes with prose-integrated mathematical formulation and calculus interpretation
  - Enhanced biological grounding: channel noise, synaptic quantal variability, finite-size effects, and neuromodulatory background input across scales
  - Documented whole-brain applications: TVB stochastic simulations, Jansen-Rit and Wilson-Cowan nodes with noise, Deco et al. resting-state fMRI results
  - Added numerical methods prose: Euler-Maruyama for additive noise, Milstein and stochastic Runge-Kutta for multiplicative noise
  - Strengthened analysis methods section: Fokker-Planck density evolution, moment equations, linear noise approximation, Monte Carlo ensembles
  - Enhanced relationships section linking SDEs to dynamical-systems-theory, nonlinear-dynamics, spiking-neural-networks, mean-field-theory, and fokker-planck-equation
  - Removed ## References section per schema
  - Sources retained: raw/papers/gardiner-2009.md, raw/papers/tuckwell-1988.md, raw/papers/deco-2008-stochastic.md, raw/papers/deco-2009-stochastic.md, raw/papers/arxiv-2603.24176.md, raw/papers/montbrio-pazo-roxin-2015.md

- Improved page: [[Free Energy Principle]] – Variational brain theory and active inference
  - Complete rewrite from sparse bullet-point outline to full concept page (~800 words)
  - Tags: free-energy-principle, variational-bayes, dynamic-causal-modeling, mean-field-theory, effective-connectivity, whole-brain-modeling, neural-mass-models, resting-state, neuroimaging-fmri, neuroimaging-eeg
  - Established 17 wikilinks: dynamic-causal-modeling, variational-bayes, effective-connectivity, fmri, eeg, resting-state, structural-connectivity, tvb, neural-mass-model, whole-brain, functional-connectivity, mean-field-theory, personalized-brain-modeling, epilepsy-modeling, whole-brain-modeling, bifurcation-analysis, stochastic-differential-equations
  - Expanded opening paragraph with plain definition of FEP as unifying perception, action, and learning under approximate Bayesian inference
  - Added motivation/context section explaining intractability of exact inference and FEP roots in Helmholtz/Ashby, with concrete instantiation in DCM for neuroimaging
  - Replaced list-only core concepts with prose-integrated mathematical formulation of variational free energy, ELBO, and Laplace approximation
  - Documented active inference as policy selection minimizing expected free energy with exploration-exploitation balance
  - Enhanced whole-brain modeling connections: TVB neural-mass-model inversion, spectral DCM, mean-field approximations, and resting-state functional-connectivity
  - Added biological grounding: computational psychiatry (precision weighting in schizophrenia), epilepsy-modeling (homeostatic failure), and consciousness theories
  - Strengthened criticisms section: falsifiability concerns, computational complexity in delay-coupled systems, relationship to reinforcement learning/enactive cognition
  - Removed placeholder ## References section per schema
  - Sources retained: raw/papers/friston-2010-fep.md, raw/papers/friston-2007.md, raw/papers/deco-2013.md

- Improved page: [[Variational Bayes]] – Approximate Bayesian inference via optimization
  - Complete rewrite from sparse bullet-point outline to full concept page (~720 words)
  - Tags: variational-bayes, dynamic-causal-modeling, parameter-estimation, free-energy-principle, mean-field-theory, neuroimaging-fmri, neuroimaging-eeg, effective-connectivity, neural-mass-models, whole-brain-modeling
  - Established 14+ wikilinks: dynamic-causal-modeling, spm, neural-mass-models, fmri, eeg, meg, effective-connectivity, free-energy-principle, whole-brain, tvb, mean-field-theory, stochastic-differential-equations, fokker-planck-equation, parameter-estimation
  - Expanded opening paragraph with plain definition contrasting VB to MCMC sampling
  - Added motivation/context section explaining intractability of exact inference in high-dimensional neural models and VB's speed advantage
  - Replaced list-only ELBO/mean-field/Laplace sections with prose-integrated mathematical explanations
  - Documented modern extensions: normalizing flows for flexible posterior approximations (Rezende & Mohamed 2015)
  - Enhanced applications section: DCM/SPM inversion for fMRI/EEG/MEG, parameter estimation in TVB neural-mass-models, group-level random effects
  - Strengthened relationships section linking VB to free-energy-principle, mean-field-theory, stochastic-differential-equations, and fokker-planck-equation
  - Removed placeholder ## References section per schema
  - Sources retained: raw/papers/friston-2007.md, raw/papers/beal-2003.md, raw/papers/blei-kucukelbir-mcauliffe-2017.md, raw/papers/wainwright-jordan-2008.md, raw/papers/rezende-mohamed-2015.md

- Improved page: [[Tractography]] – Concept page on diffusion-MRI-based white matter tract reconstruction
  - Complete rewrite from sparse bullet-point outline to full concept page (~720 words)
  - Tags: tractography, neuroimaging-dti, diffusion-imaging, structural-connectivity, connectomics, whole-brain-modeling, paper-methods, paper-review
  - Established 15 wikilinks: tvb, nest, network-hubs, rich-club, functional-connectivity, epilepsy-modeling, diffusion-mri, structural-connectivity, connectome, dti, whole-brain, effective-connectivity, dynamic-causal-modeling, fmri, eeg
  - Expanded opening paragraph with plain definition of tractography and its role in connectome construction
  - Added motivation/context section tracing history from invasive tracers to Mori et al. (1999) and emphasizing structural connectivity matrix generation
  - Replaced list-only methods section with prose covering deterministic tracking, probabilistic approaches, CSD (Tournier 2007), global optimization, and anatomically constrained tractography
  - Documented role in whole-brain modeling: connection weights, transmission delays, network topology, and relationship to TVB/NEST platforms
  - Enhanced challenges section with Jones (2010) validation critique and Sotiropoulos & Zalesky (2019) connectome construction caveats
  - Added sensitivity analysis implications for model robustness
  - Removed placeholder ## References section per schema
  - Sources retained: raw/papers/mori-1999.md, raw/papers/jones-2010.md, raw/papers/tournier-2007.md, raw/papers/sotiropoulos-zalesky-2019.md

- Improved page: [[Bifurcation Theory]] – Mathematical theory of qualitative transitions in dynamical systems
  - Complete rewrite from sparse bullet-point outline to full concept page (~780 words)
  - Tags: bifurcation-theory, dynamical-systems-theory, nonlinear-dynamics, neural-mass-models, epilepsy-modeling, network-dynamics, brain-oscillations, whole-brain-modeling, parameter-estimation
  - Established 18+ wikilinks: whole-brain-modeling, neural-mass-models, structural-connectivity, wilson-cowan, jansen-rit, brain-oscillations, epilepsy-modeling, epileptor, network-dynamics, functional-connectivity, neural-mass-model, dynamical-systems-theory, nonlinear-dynamics, bifurcation-analysis, tvb, steven-strogatz, john-guckenheimer, philip-holmes, the-virtual-epileptic-brain, parameter-estimation
  - Expanded opening paragraph with plain definition and scope
  - Added motivation/context section explaining why bifurcation theory matters for mapping parameter spaces in brain modeling
  - Replaced list-only local bifurcation section with prose explanation of saddle-node, transcritical, pitchfork, and Hopf bifurcations in neural terms
  - Added global bifurcations and codimension-2 organizing centers with neuroscience relevance
  - Documented numerical continuation (AUTO, MATCONT) and applications to epilepsy modeling and network dynamics
  - Biological grounding section links bifurcation parameters to synaptic coupling, excitation-inhibition balance, and seizure transitions
  - Removed placeholder ## References section per schema
  - Sources retained: raw/papers/strogatz-1994.md, raw/papers/guckenheimer-holmes-1983.md, raw/papers/kuznetsov-2004.md, raw/papers/seydel-2010.md, raw/papers/touboul-2011.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2509.02799.md, raw/papers/hirsch-smale-devaney-2004.md

- Improved page: [[Fokker-Planck Equation]] – Concept page on population-level stochastic dynamics
  - Complete rewrite from sparse bullet-point outline to full concept page (~700 words)
  - Tags: fokker-planck-equation, stochastic-differential-equations, neural-mass-models, mean-field-theory, nonlinear-dynamics, dynamical-systems-theory, whole-brain-modeling
  - Established 12 wikilinks: dynamical-systems-theory, bifurcation-analysis, epileptor, jansen-rit, spiking-neural-networks, mean-field-theory, whole-brain-modeling, epilepsy-modeling, nonlinear-dynamics, neural-mass-model, variational-bayes, dynamic-causal-modeling
  - Opening paragraph defines the equation and its role in computational neuroscience
  - Motivation/context section explains tension between Monte Carlo simulation and population-level analysis
  - Mathematical formulation includes general drift-diffusion PDE with prose explanation of each term
  - Solution methods covered: eigenfunction expansions, matrix continued fractions, spectral methods, finite-difference/finite-element schemes
  - Applications detailed: population density approach, firing-rate derivation from threshold flux, first-passage-time problems
  - Biological grounding: membrane potential statistics, synaptic noise, interspike interval distributions, epilepsy transitions
  - Relationships: contrast with Langevin/SDE trajectory methods, link to mean-field and neural-mass models, dimensionality tradeoffs
  - Sources retained: raw/papers/risken-1989.md, raw/papers/gardiner-2009.md, raw/papers/tuckwell-1988.md

- Improved page: [[Epileptor]] – Composite neural mass model for seizure dynamics
  - Complete rewrite from placeholder/equation list to full concept page (~750 words)
  - Tags: neural-mass-models, epilepsy-modeling, bifurcation-analysis, nonlinear-dynamics, dynamical-systems-theory, whole-brain-modeling, software-tvb, personalized-brain-modeling, structural-connectivity, functional-connectivity, brain-oscillations, brain-stimulation
  - Established 18 wikilinks to epilepsy-modeling, neural-mass-models, structural-connectivity, tvb, the-virtual-epileptic-brain, brain-network, jansen-rit, larter-breakspear, bifurcation-analysis, connectome, dynamical-systems-theory, spiking-neural-networks, oscillator, wilson-cowan, epileptorcodim3, epileptor-rs, functional-connectivity, whole-brain-modeling
  - Documented mathematical formulation with fast-slow subsystem coupling, permittivity variable z, and epileptogenicity parameter x₀
  - Detailed dynamical regimes: interictal, pre-ictal, and ictal states with bifurcation structure (SNIC onset, homoclinic offset)
  - Incorporated clinical applications: Virtual Epileptic Patient, delay-constrained re-entry (Triebkorn et al. 2025), and passivity-based control (Acharya & Nozari 2026)
  - Added biological grounding: mapping x₀ to tissue excitability, z to slow homeostatic processes (extracellular potassium, metabolic buildup)
  - Compared to Jansen-Rit, Wilson-Cowan, and Larter-Breakspear models
  - Added source: raw/papers/breakspear-2006.md for historical neural-field context

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

- Improved page: [[dynamic-causal-modeling]] – Bayesian framework for inferring effective connectivity
  - Restructured and condensed from ~1150 words to ~790 words (target 500–800)
  - Tags validated: dynamic-causal-modeling, effective-connectivity, neural-mass-models, variational-bayes, free-energy-principle, mean-field-theory, stochastic-differential-equations, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, resting-state
  - Established 20+ wikilinks: effective-connectivity, functional-connectivity, neural-mass-models, variational-bayes, spm, fmri, eeg, meg, dti, structural-connectivity, free-energy-principle, nonlinear-dynamics, bold-signal, mean-field-theory, stochastic-differential-equations, resting-state, jansen-rit, wilson-cowan, epilepsy-modeling, tvb
  - Enhanced opening paragraph with plain definition and modality scope
  - Expanded motivation/context: contrasted DCM with descriptive functional-connectivity and structural-connectivity, situated within free-energy-principle and key historical papers (Friston 2003, Stephan 2010, Daunizeau et al. 2011)
  - Streamlined mathematical formulation: neural state equation with A/B/C matrices explained in prose, observation models for fMRI (Balloon/BOLD) and EEG/MEG (forward model)
  - Condensed Bayesian inference section: variational-bayes, variational Laplace, free energy for model comparison, fixed-effects vs random-effects group analysis
  - Merged DCM variants into concise prose: deterministic fMRI DCM, stochastic extensions, EEG/MEG with Jansen-Rit and Wilson-Cowan, spectral DCM for resting-state
  - Added explicit biological grounding: synaptic efficacy, neuromodulation, vascular reactivity, clinical applications in epilepsy-modeling and neurodegeneration
  - Strengthened relationships section: contrast with Granger causality, identifiability limits, complementary role beside TVB population-level modeling
  - Removed redundant subsections and eliminated overlap between variant descriptions
  - Retained sources: friston-2003-dcm.md, stephan-2010.md, daunizeau-david-stephan-2011.md

- Improved page: [[Hopfield Network]] – Recurrent associative memory model
  - Complete rewrite from sparse equation list to full concept page (~720 words)
  - Tags validated: neural-mass-models, dynamical-systems-theory, nonlinear-dynamics, network-dynamics, mean-field-theory
  - Established 11 wikilinks: dynamical-systems-theory, nonlinear-dynamics, mean-field-theory, network-dynamics, wilson-cowan, jansen-rit, neural-mass-model, spiking-neural-networks, free-energy-principle, functional-connectivity, brain-network
  - Expanded opening paragraph with plain definition of content-addressable memory and attractor convergence
  - Added motivation/context section tracing history from cybernetics to statistical mechanics and energy minimization
  - Replaced isolated equations with prose-integrated mathematical formulation explaining symmetry constraint, Lyapunov energy function, and Hebbian learning capacity
  - Documented modern extensions: dynamical mean-field theory, continuous neurons, non-monotonic transfer functions, non-equilibrium retrieval
  - Added relationships section contrasting with Wilson-Cowan, Jansen-Rit, spiking networks, and linking to free-energy principle
  - Enhanced biological grounding: synaptic plasticity, persistent prefrontal activity, asymmetric weight caveats, whole-brain attractor models of resting-state functional connectivity
  - Removed ## References section per schema
  - Sources retained: arxiv-2510.19146.md, arxiv-2512.05252.md, arxiv-2602.09535.md, arxiv-2604.13719.md, semanticscholar-71ffb8153870.md, semanticscholar-c3d9674bec1b.md, semanticscholar-62534125f066.md

## [2026-04-24] Improve: 1 page improved (mean-field-theory)

- Improved page: [[Mean Field Theory]] – Concept page on population-level approximations of large neuronal networks
  - Complete rewrite from sparse bullet-point outline to full concept page (~780 words)
  - Tags validated: mean-field-theory, neural-mass-models, spiking-neural-networks, whole-brain-modeling, dynamical-systems-theory, brain-oscillations, network-dynamics, stochastic-differential-equations, nonlinear-dynamics, bifurcation-analysis
  - Established 18+ wikilinks: spiking-neural-networks, whole-brain-modeling, fmri, eeg, meg, brain-oscillations, network-dynamics, wilson-cowan, neural-mass-models, tvb, bifurcation-analysis, fokker-planck-equation, nest, epilepsy-modeling, structural-connectivity, diffusion-mri, connectome, jansen-rit, dynamic-causal-modeling, variational-bayes, stochastic-differential-equations, nonlinear-dynamics, dynamical-systems-theory
  - Expanded opening paragraph with plain definition bridging microscopic spiking networks and population-level whole-brain models
  - Added motivation/context section explaining the scale gap between billions of neurons and macroscopic neuroimaging signals, with roots in statistical physics
  - Replaced list-only mathematical framework with prose-integrated sections on self-consistency equations, Wilson-Cowan firing-rate dynamics, and exact reductions
  - Documented modern exact reductions: Montbrió-Pazó-Roxin 2015 Ott-Antonsen ansatz for QIF neurons, Schwalger-Deger-Gerstner 2017 population density methods, Stefanescu-Jirsa 2008 heterogeneous network dimension reduction
  - Enhanced dynamical regimes section: asynchronous irregular (Amit & Brunel 1997, Brunel 2000), synchronous regular, and fast oscillatory states with biological grounding in cortical spontaneous activity and seizure transitions
  - Strengthened whole-brain modeling applications: coupling mean field nodes across structural-connectivity matrices, Jansen-Rit for EEG/MEG, Wilson-Cowan, and dynamic-causal-modeling variational-bayes inversion
  - Added limitations section: finite-size effects, correlation structure, strong coupling, spatial heterogeneity, and extensions via stochastic-differential-equations and moment closure
  - Removed ## References section per schema
  - Sources retained: raw/papers/amit-brunel-1997.md, raw/papers/brunel-2000.md, raw/papers/montbrio-pazo-roxin-2015.md, raw/papers/schwalger-deger-gerstner-2017.md, raw/papers/stefanescu-jirsa-2008.md

- Improved page: [[Mean Field Theory]] – Further refinements
  - Renamed "From Microscopic Dynamics to Macroscopic Rates" to "Self-Consistency and Population Averaging" for clarity
  - Added mathematical fixed-point formulation: $r = F[\mathbf{J} \cdot r + I_{\text{ext}}]$ with explanatory prose
  - Added comparison paragraph contrasting classical deterministic transfer functions vs [[fokker-planck-equation]] density propagation
  - Extended Exact Reductions section: Lorentzian firing-rate function interpretation, center manifold theory connection for Stefanescu-Jirsa, and explicit contrast between classical and modern correlation treatments
  - Added [[bifurcation-theory]] wikilink in correlation contrast discussion
  - Expanded Limitations section with TVB-specific challenges: laminar/cell-type diversity within cortical columns, calibration against spiking simulations
  - Added discussion of combined neural + variational mean field approximation hierarchy in [[dynamic-causal-modeling]] and [[variational-bayes]]
  - Total: ~980 words, 25+ wikilinks


## [2026-04-24 14:08] Audit: 823 issues (95 broken links, 128 orphans, 116 placeholders, 0 dup-refs, 2 opaque-refs, 52 thin, 115 missing-links)
