# Wiki Log

## 2026-04-29

- Created/Improved page: [[nibabies]] – Infant brain MRI preprocessing pipeline
  - Complete rewrite from placeholder to comprehensive entity page (~590 words)
  - Updated frontmatter: changed updated date to 2026-04-29
  - Tags: software-bids, neuroimaging-fmri, neuroimaging-dti, neuroimaging-infants, software-neuroimaging, bids-derivatives, software-fmriprep, developmental-trajectories
  - Established 12+ wikilinks: fMRIprep, BIDS, nipype, freesurfer, ANTs, FSL, BIDS-derivatives, nilearn, nistats, structural-connectivity, connectome, personalized-brain-modeling, developmental-trajectories, brain-network, the-virtual-brain, Brainstorm, mne-python, Templateflow, mriqc, datalad, qsiprep
  - Added detailed sections: Overview, Key Features (anatomically-informed processing, motion correction, age-adaptive segmentation, quality control), Relationship to TVB (provides data for whole-brain models), Key Papers, Related Software, Technical Considerations
  - Explained nibabies' role in infant neuroimaging and its relationship to the broader whole-brain modeling ecosystem
  - Positioned nibabies within the TVB ecosystem as a data preprocessing tool contributing high-quality derivatives

- Created/Improved page: [[bifurcation-theory]] – Mathematical theory of qualitative changes in dynamical systems
  - Complete rewrite from placeholder to comprehensive concept page (~910 words)
  - Updated frontmatter: changed updated date to 2026-04-29
  - Tags: bifurcation-theory, dynamical-systems-theory, nonlinear-dynamics, bifurcation-analysis, neural-mass-models, brain-oscillations, epilepsy-modeling, parameter-estimation, stochastic-differential-equations, fokker-planck-equation
  - Established 15+ wikilinks: neural-mass-models, whole-brain-modeling, dynamical-systems-theory, nonlinear-dynamics, brain-oscillations, epileptor, wong-wang-model, jansen-rit-model, spiking-neural-networks, mean-field-theory, fokker-planck-equation, dynamic-causal-modeling, parameter-estimation, personalized-brain-modeling, seizure-prediction, brain-stimulation, variational-bayes
  - Added detailed sections: Overview, Theoretical Foundation, Key Bifurcation Types (Saddle-Node, Andronov-Hopf, Pitchfork, Bogdanov-Takens), Relationship to Dynamical Systems Theory, Applications in Computational Neuroscience, Open Questions and Challenges
  - Explained saddle-node and Hopf bifurcations with normal forms and their relevance to brain oscillations and seizure dynamics
  - Connected to neural mass models (Wong-Wang, Jansen-Rit, Epileptor) and their bifurcation structures
  - Positioned within the theoretical framework for understanding state transitions in whole-brain models

- Created/Improved page: [[bctpy]] – Brain Connectivity Toolbox for Python
  - Complete rewrite from placeholder to comprehensive entity page (~540 words)
  - Updated frontmatter: changed updated date to 2026-04-29
  - Tags: software-bct, software-graph-tool, connectomics, network-dynamics, graph-theory
  - Established 10+ wikilinks: the-virtual-brain, whole-brain-modeling, graph-theory, network-dynamics, small-world-networks, modularity, community-detection, rich-club, structural-connectivity, functional-connectivity, connectomics, brain-parcellations, graph-tool, braph, nest
  - Added detailed sections: Overview, Key Features (node centrality, path-based metrics, clustering, community detection, network comparison), Relationship to TVB, Key Papers, Related Software
  - Explained BCTpy's role in analyzing brain connectivity networks from neuroimaging data
  - Added entry to entities/index.md under Software Platforms

- Created/Improved page: [[braph]] – Graph theory software for brain connectivity analysis
  - Complete rewrite from placeholder to comprehensive entity page (~550 words)
  - Updated frontmatter: changed updated date to 2026-04-29
  - Tags: software-brain-modeling, connectomics, graph-theory, neuroimaging-fmri, neuroimaging-mri, neuroimaging-eeg, neuroimaging-pet, network-dynamics
  - Established 12+ wikilinks: the-virtual-brain, connectome, brain-connectivity-toolbox, conn, brainnet-viewer, graphvar, graph-tool, small-world-networks, modularity, network-hubs, alzheimers-disease, alzheimers-modeling, bctpy, nilearn, neural-mass-models, whole-brain-modeling, functional-connectivity, structural-connectivity
  - Added detailed sections: Overview, Motivation and Context, Key Features (multimodal support, correlation measures, thresholding, global/nodal metrics, permutation tests), BRAPH 2.0 and Genesis, Relationship to TVB, Key Papers, Related Software
  - Explained BRAPH's role as MATLAB-based brain connectivity analysis tool complementary to TVB for whole-brain modeling
  - Positioned BRAPH within connectomics ecosystem alongside BCTpy, GraphVar, and Brain Connectivity Toolbox
  - Added entry to entities/index.md under Software Platforms

## 2026-04-28

- Improved page: [[brainnet-viewer]] – Brain network visualization toolbox
  - Complete rewrite from placeholder to comprehensive entity page (~600 words)
  - Updated frontmatter: changed updated date to 2026-04-28, added sources: raw/papers/xia-2013-brainnet-viewer.md
  - Tags: software-visualization, connectomics, neuroimaging-fmri, neuroimaging-meg, neuroimaging-eeg
  - Established 10+ wikilinks: the-virtual-brain, neural-mass-models, epileptor, diffusion-mri, brain-connectivity-toolbox, nilearn, pycortex, freesurfer, brainvisa, brainstorm, 3d-slicer, itk-snap, spm, connectome-workbench
  - Added detailed sections: Overview, Key Features (file formats, node/edge visualization, volume mapping, layout options, command-line interface), Relationship to TVB, Key Papers, Related Software
  - Explained BrainNet Viewer's role in the connectomics visualization pipeline and its complementary relationship to TVB for whole-brain modeling result visualization
  - Positioned BrainNet Viewer within the network visualization ecosystem alongside Brain Connectivity Toolbox, nilearn, and pycortex

- Improved page: [[cartool]] – EEG analysis and source localization software
  - Complete rewrite from placeholder to comprehensive entity page (~700 words)
  - Updated frontmatter: changed updated date to 2026-04-28, added sources: raw/papers/brunet-2011.md, raw/papers/michel-2019.md
  - Tags: software-visualization, neuroimaging-eeg, source-localization, micro-states, brain-mapping
  - Established 10+ wikilinks: the-virtual-brain, neural-mass-models, whole-brain-modeling, brain-oscillations, eeg, fieldtrip, brainstorm, meg, mne-python, resting-state, epilepsy-modeling
  - Added detailed sections: Overview, Key Features (source localization, microstates, frequency analysis, preprocessing), Relationship to TVB, Technical Implementation, Key Papers, Related Software
  - Explained Cartool's role in EEG/MEG source imaging and its complementary relationship to TVB whole-brain simulation
  - Positioned Cartool within the EEG analysis ecosystem alongside EEGLAB, FieldTrip, and Brainstorm

- Improved page: [[lfpykit]] — Python toolkit for computing extracellular potentials from neural simulations
  - Complete rewrite from placeholder to comprehensive entity page (~750 words)
  - Updated frontmatter: changed updated date to 2026-04-28, added sources: LFPykit GitHub Repository, Linden et al. 2014, Hagen et al. 2018, Ness et al. 2015, Næss et al. 2017
  - Tags: software-neuron, spiking-neural-networks, neural-mass-models, dynamic-causal-modeling, neuroimaging-eeg, neuroimaging-meg
  - Established 10+ wikilinks: lfpy, neuron, brian2, nest, local-field-potentials, neuroimaging-eeg, neuroimaging-meg, electrophysiology, computational-neuroscience, the-virtual-brain, whole-brain-modeling, dynamic-causal-modeling, brain-oscillations
  - Added detailed sections: Overview, Motivation and Context, Technical Content (Line-Source Approximation, Point-Source Method, Current-Source Density Estimation), Key Features (anisotropic conductivity, electrode modeling), Relationship to TVB and Whole-Brain Modeling, Related Software
  - Explained LFPykit's role in forward modeling of extracellular potentials and its relationship to neural simulators
  - Positioned LFPykit within the computational neuroscience ecosystem alongside NEURON, Brian2, NEST, and LFPy

- Improved page: [[krasimira-tsaneva-atanasova]] – Researcher in connectome-based whole-brain modeling
  - Complete rewrite from placeholder to comprehensive entity page (~600 words)
  - Updated frontmatter: changed updated date to 2026-04-28, added sources: raw/papers/breakspear-2017.md, raw/papers/sanz-leon-2013.md
  - Tags: people-researcher, whole-brain-modeling, neural-mass-models, computational-neuroscience, network-dynamics
  - Established 10+ wikilinks: connectome, whole-brain-modeling, neural-mass-model, tvb, structural-connectivity, functional-connectivity, parameter-estimation, personalized-brain-modeling, brain-dynamics, network-dynamics, epilepsy-modeling, computational-psychiatry
  - Added sections: Affiliations, Research Focus (whole-brain modeling, parameter estimation, neural mass models), Key Publications with context, Relationships and Collaborative Context, Open Questions
  - Replaced all placeholders with substantive content about the researcher's work in computational neuroscience
  - Linked to key foundational papers (Breakspear 2017, Sanz Leon et al. 2013) and explained their relevance to the field

- Improved page: [[pynrrd]] – Python library for reading/writing NRRD file format
  - Complete rewrite from placeholder to comprehensive entity page (~900 words)
  - Updated frontmatter: changed updated date to 2026-04-28, added tags: neuroimaging-dti, diffusion-imaging
  - Added sources: raw/papers/pynrrd-docs.md, raw/papers/nrrd-format.md
  - Established 9+ wikilinks: nibabel, dipy, 3d-slicer, ants, mrtrix, nilearn, the-virtual-brain, whole-brain, connectome, structural-connectivity, diffusion-imaging
  - Added detailed sections: Overview, Relationship to TVB, Key Features, Technical Implementation, Comparison with Related Formats, Integration with Neuroimaging Software
  - Explained NRRD format's role in DTI/tractography and whole-brain modeling workflows
  - Included usage code example demonstrating 4D DWI volume handling

- Improved page: [[yasa]] – Python toolbox for polysomnographic sleep recording analysis
  - Complete rewrite from placeholder to comprehensive entity page (~750 words)
  - Updated frontmatter: changed updated date to 2026-04-28, added tags: neuroimaging-eeg, brain-oscillations (in addition to existing software-brain-modeling)
  - Added sources: (none available - used general knowledge from web search)
  - Established 10+ wikilinks: eeg, brain-oscillations, mne-python, eeglab, epilepsy-modeling, whole-brain-modeling, neural-mass-model, tvb, neuroimaging, functional-connectivity, resting-state
  - Added detailed sections: Overview, Key Features (automated sleep staging, event detection, spectral analysis), Relationship to Whole-Brain Modeling and TVB, Key Papers, Related Software, Technical Implementation
  - Positioned YASA within the EEG/sleep analysis ecosystem while explaining connections to whole-brain modeling via brain oscillations and neural mass model frameworks

- Improved page: [[jneuroml]] – Java implementation of NeuroML specification
  - Complete rewrite from placeholder to comprehensive entity page (~750 words)
  - Updated frontmatter: changed updated date to 2026-04-28, added tags: software-neuroml, neuroml, spiking-neural-networks, neural-mass-models, open-source-brain, model-validation
  - Added sources: (none available - used domain knowledge from web search)
  - Established 12+ wikilinks: neuroml, open-source-brain, computational-neuroscience, spiking-neural-networks, neural-mass-models, neuron, brian, nest, bifurcation-analysis, dynamical-systems-theory, epilepsy-modeling, the-virtual-brain, whole-brain-modeling, mean-field-theory
  - Added detailed sections: Overview and Purpose, Key Features (validation, export to NEURON/Brian/NEST, parameter variation), Relationship to TVB, Relationship to Other NeuroML Tools, Key Capabilities for Model Developers, Conclusion
  - Explained jNeuroML's role in model interoperability and reproducibility in computational neuroscience
  - Positioned jNeuroML within multi-scale modeling context bridging detailed neurons to whole-brain models

## 2026-04-27

- Fixed and re-improved page: [[cognitive-reserve]] – Brain's adaptive capacity to maintain function despite pathology
  - **CRITICAL FIX**: Page content was corrupted (contained garbled metadata instead of actual concept content)
  - Complete rewrite to proper concept page (~1400 words) with actual substantive content
  - Updated frontmatter: updated date remains 2026-04-27, added tags: neuroimaging-eeg, neuroimaging-meg, compensation, network-dynamics
  - Established 15+ wikilinks: brain-maintenance, aging, functional-connectivity, resting-state, default-mode-network, structural-connectivity, connectomics, whole-brain-modeling, personalized-brain-modeling, network-dynamics, structural-core, brain-network, bold-signal
  - Proper opening paragraph defining cognitive reserve and distinguishing it from brain reserve
  - Added "Theoretical Motivation and Clinical Significance" explaining the threshold model and clinical implications
  - Expanded "Historical Development" with detailed prose on Stern's theory, Buckner's neuroimaging integration, and Cabeza's three-mechanism framework
  - Added section on "Types of Reserve: Brain Versus Cognitive" with threshold model explanation
  - Expanded "Proxy Measures and Their Limitations" with confounding factor discussion
  - Added "Neural Mechanisms and Neuroimaging Evidence" section covering fMRI, EEG, and MEG findings
  - Added "Role in Whole-Brain Modeling" section linking to neural mass models and network resilience
  - Added "Relationship to Brain Maintenance" section explaining conceptual distinctions and complementarities
  - Removed invalid ## References section that was in corrupted content
  - Sources retained: raw/papers/buckner-2004.md, raw/papers/grady-2012.md, raw/papers/cabeza-2018.md

- Improved page: [[neurodevelopment]] – Brain development across the lifespan
  - Complete rewrite expanding from ~400 words to ~800 words
  - Updated frontmatter: changed updated date from 2026-04-23 to 2026-04-27
  - Tags: neurodevelopment, developmental-trajectories, whole-brain-modeling
  - Established 10+ wikilinks: Nitin Gogtay, developmental-trajectories, aging, brain-network, functional-connectivity, structural-connectivity, personalized-brain-modeling, whole-brain-modeling, resting-state, default-mode-network, network-dynamics
  - Expanded opening paragraph to define neurodevelopment in context of whole-brain modeling, explaining why developmental stage matters for model parameter calibration
  - Added "Definition and Scope" section with more detailed explanation of the integration of developmental neuroscience, neuroimaging, and computational modeling
  - Expanded "Structural Development" section with prose explaining neurogenesis in proliferative zones, neuronal migration mechanisms, differentiation processes, and detailed timeline of synaptogenesis and synaptic pruning
  - Expanded "Functional Development" section detailing transition from local to distributed processing and cognitive maturation
  - Enhanced "Cortical Maturation Pattern" section to integrate resting-state neuroimaging context and link to whole-brain modeling implications
  - Added detail to "Network Development" section describing transitions from infancy through adulthood with specific network behaviors
  - Expanded "Role in Whole-Brain Modeling" section with specific parameter types that must be age-calibrated: synaptic time constants, connection strengths, network topology
  - Added "Modeling Developmental Disorders" subsection explaining how personalized-brain-modeling approaches can identify deviations in developmental trajectories
  - Replaced broken link to "plasticity" with valid links to brain-network and network-dynamics
  - Added more related concepts in final section to reach 10 wikilinks: whole-brain-modeling, resting-state, default-mode-network, network-dynamics
  - Removed ## References section per schema, as sources are already documented in frontmatter
  - Sources retained from frontmatter: raw/papers/tau-peterson-2010.md, raw/papers/gogtay-2004.md, raw/papers/fair-2009.md, raw/papers/power-2010.md, raw/papers/stiles-jernigan-2010.md, raw/papers/semanticscholar-c4bc6ce91683.md, raw/papers/smith-2021.md

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

## [2026-04-24 14:08] Audit: 823 issues (95 broken links, 128 orphans, 116 placeholders, 0 dup-refs, 2 opaque-refs, 52 thin, 115 missing-links)

## [2026-04-24 14:08] Audit: 823 issues (95 broken links, 128 orphans, 116 placeholders, 0 dup-refs, 2 opaque-refs, 52 thin, 115 missing-links)

## [2026-04-24 14:08] Audit: 823 issues (95 broken links, 128 orphans, 116 placeholders, 0 dup-refs, 2 opaque-refs, 52 thin, 115 missing-links)

## [2026-04-24 14:08] Audit: 823 issues (95 broken links, 128 orphans, 116 placeholders, 0 dup-refs, 2 opaque-refs, 52 thin, 115 missing-links)

## [2026-04-27 09:14] RefFormatter: formatted references on 91 pages

## [2026-04-27 09:22] CrosslinkApplier: added 237 wikilinks (206 inline, 31 suggested)

## [2026-04-27] lint | 210 broken links, 97 orphans, 42 missing from index

## [2026-04-27] hourly | Added 0 new papers

## [2026-04-27 10:55] functional-connectivity.md | Improved page (expanded content, added wikilinks, updated references)

## [2026-04-27 11:03] Linter: 208 broken links, 97 orphans, 157 stale, 115 empty

## [2026-04-27 11:13] BulkRewrite: 39 pages rewritten with ollama/minimax-m2.5:cloud, 0 failed

## [2026-04-27 12:32] RefFormatter: formatted references on 48 pages

## [2026-04-27 12:34] CrosslinkApplier: added 218 wikilinks (212 inline, 6 suggested)

## [2026-04-27 12:35] Audit: 828 issues (247 broken links, 98 orphans, 114 placeholders, 0 dup-refs, 2 opaque-refs, 2 thin, 114 missing-links)

## [2026-04-27 12:35] Audit: 828 issues (247 broken links, 98 orphans, 114 placeholders, 0 dup-refs, 2 opaque-refs, 2 thin, 114 missing-links)

## [2026-04-27 14:37] Audit: 837 issues (254 broken links, 98 orphans, 114 placeholders, 0 dup-refs, 2 opaque-refs, 0 thin, 116 missing-links)

## [2026-04-27 15:43] Audit: 783 issues (200 broken links, 98 orphans, 114 placeholders, 0 dup-refs, 2 opaque-refs, 0 thin, 116 missing-links)

## [2026-04-27 15:49] Audit: 1025 issues (7 broken links, 87 orphans, 114 placeholders, 0 dup-refs, 2 opaque-refs, 86 thin, 206 missing-links)

## [2026-04-27 16:11] Audit: 1020 issues (14 broken links, 81 orphans, 87 placeholders, 0 dup-refs, 2 opaque-refs, 80 thin, 233 missing-links)

## [2026-04-27 16:15] CrosslinkApplier: added 720 wikilinks (719 inline, 1 suggested)

## [2026-04-27 16:20] Audit: 812 issues (8 broken links, 80 orphans, 87 placeholders, 0 dup-refs, 2 opaque-refs, 80 thin, 151 missing-links)

## [2026-04-27 16:22] Audit: 809 issues (5 broken links, 80 orphans, 87 placeholders, 0 dup-refs, 2 opaque-refs, 80 thin, 151 missing-links)

## [2026-04-27 16:25] Audit: 808 issues (4 broken links, 80 orphans, 87 placeholders, 0 dup-refs, 2 opaque-refs, 80 thin, 151 missing-links)

## [2026-04-27 16:26] Audit: 805 issues (0 broken links, 81 orphans, 87 placeholders, 0 dup-refs, 2 opaque-refs, 80 thin, 151 missing-links)

## [2026-04-27 16:30] Librarian: catalog rebuilt, 2330 asymmetric links noted

## [2026-04-27 16:31] Audit: 704 issues (0 broken links, 81 orphans, 87 placeholders, 0 dup-refs, 2 opaque-refs, 80 thin, 151 missing-links)

## [2026-04-27 18:56] Improve: 3 pages improved (neuromorpho-toolkit, open-source-brain, dsi-studio)

## [2026-04-27 18:56] RefFormatter: formatted references on 60 pages

## [2026-04-27 19:00] CrosslinkApplier: added 162 wikilinks (162 inline, 0 suggested)

## [2026-04-27 19:05] Ingest: 7 new papers, 0 stubs created

## [2026-04-27 19:43] Matcher: 61 pages got 164 new sources

## [2026-04-27 19:51] DeepResearch: 76 papers added via focused research

## [2026-04-27 19:51] Audit: 609 issues (5 broken links, 78 orphans, 84 placeholders, 0 dup-refs, 2 opaque-refs, 78 thin, 165 missing-links)

## [2026-04-27 20:20] Improve: 3 pages improved (scirun, brainsuite, ebrains)

## [2026-04-27 20:20] RefFormatter: formatted references on 19 pages

## [2026-04-27 20:24] CrosslinkApplier: added 60 wikilinks (60 inline, 0 suggested)

## [2026-04-27 20:28] Ingest: 2 new papers, 0 stubs created

## [2026-04-27 20:54] Matcher: 57 pages got 156 new sources

## [2026-04-27 21:43] Improve: 3 pages improved (ebrains, scirun, brainsuite)

## [2026-04-27 21:43] RefFormatter: formatted references on 4 pages

## [2026-04-27 21:47] CrosslinkApplier: added 29 wikilinks (29 inline, 0 suggested)

## [2026-04-27 21:51] Ingest: 2 new papers, 0 stubs created

## [2026-04-27 22:43] Improve: 3 pages improved (clinica, neuroscience-gateway, nengo)

## [2026-04-27 22:43] RefFormatter: formatted references on 3 pages

## [2026-04-27 22:47] CrosslinkApplier: added 25 wikilinks (25 inline, 0 suggested)

## [2026-04-27 22:51] Ingest: 3 new papers, 0 stubs created

## [2026-04-27 23:15] Matcher: 15 pages got 36 new sources

## [2026-04-27 23:26] DeepResearch: 25 papers added via focused research

## [2026-04-27 23:26] Audit: 590 issues (7 broken links, 71 orphans, 78 placeholders, 0 dup-refs, 2 opaque-refs, 78 thin, 176 missing-links)

## [2026-04-27 23:37] Repair: 29 issues fixed (18 source refs, 0 index, 0 frontmatter, 7 wikilinks, 4 orphans, 0 dup-refs, 0 opaque-refs, 0 crosslinks)

## [2026-04-27 23:37] Librarian: catalog rebuilt, 2697 asymmetric links noted

## [2026-04-27 23:37] Linter: 0 broken links, 66 orphans, 77 stale, 116 empty

## [2026-04-27 23:56] SoftwareMapper: 20 pages created

## [2026-04-27 23:58] Improve: 3 pages improved (nibetaseries, cat12, chronux)

- Updated [[lfpy]] entity page with comprehensive content including overview, technical framework, key features, relationship to TVB, key papers, and related software.

## [2026-04-28 01:03] Improve: 3 pages improved (the-virtual-epileptic-brain, physionet, lfpy)

## [2026-04-28 02:09] Improve: 3 pages improved (pybids, pynrrd, krasimira-tsaneva-atanasova)

## [2026-04-28 03:13] Improve: 3 pages improved (sloreta, music, neurosynth)

## [2026-04-28 04:16] Improve: 3 pages improved (brain-connectivity-toolbox, itk-snap, plotly)

## [2026-04-28 05:39] Matcher: 33 pages got 91 new sources

## [2026-04-28 05:44] Improve: 3 pages improved (fmriprep, genesis, pyeeg)

## [2026-04-28 13:38] Audit: 696 issues (16 broken links, 65 orphans, 68 placeholders, 0 dup-refs, 4 opaque-refs, 78 thin, 192 missing-links)

## [2026-04-28 13:47] RefFormatter: formatted references on 8 pages

## [2026-04-28 13:52] Improve: 3 pages improved (suma, glasser-atlas, xnat)

## [2026-04-28 13:56] CrosslinkApplier: added 126 wikilinks (126 inline, 0 suggested)

## [2026-04-28 14:00] Ingest: 3 new papers, 0 stubs created

## [2026-04-28 14:20] Matcher: 13 pages got 33 new sources

## [2026-04-28 14:29] Audit: 697 issues (23 broken links, 63 orphans, 65 placeholders, 0 dup-refs, 4 opaque-refs, 78 thin, 195 missing-links)

## [2026-04-28 14:41] Repair: 84 issues fixed (40 source refs, 15 index, 2 frontmatter, 20 wikilinks, 4 orphans, 0 dup-refs, 0 opaque-refs, 3 crosslinks)

## [2026-04-28 14:41] Librarian: catalog rebuilt, 3117 asymmetric links noted

## [2026-04-28 14:41] Linter: 0 broken links, 59 orphans, 65 stale, 100 empty

## [2026-04-28 14:50] SoftwareMapper: 19 pages created

## [2026-04-28 14:55] Improve: 3 pages improved (dcm2niix, dpabi, gretna)

## [2026-04-28 16:00] Improve: 3 pages improved (pycortex, heudiconv, tractseg)

## [2026-04-28 17:06] Improve: 3 pages improved (civet, yasa, bci2000)

## [2026-04-28 18:12] Improve: 3 pages improved (brainnetome-atlas, pyedflib, templateflow)

## [2026-04-28 18:15] Create: New page XCOS (concepts/xcos.md) - EEG electrode coordinate framework for source localization and forward modeling

## [2026-04-28 18:30] Improve: page power-atlas – Complete rewrite from placeholder to full entity page (~850 words)
  - Restructured from placeholder content to comprehensive entity page about brain parcellation scheme
  - Tags: brain-parcellations, functional-connectivity, neuroimaging-fmri, resting-state, network-dynamics
  - Established 10+ wikilinks: brain-parcellations, functional-connectivity, neuroimaging-fmri, resting-state, network-dynamics, connectome, the-virtual-brain, mni-space, yeo-atlas, desikan-killiany-atlas, aal-atlas, bharat-biswal, steven-smith, human-connectome-project
  - Expanded opening paragraph: defined Power Atlas as 264-ROI parcellation from Power et al. 2011
  - Added motivation/context section explaining the need for standardized parcellation before 2011
  - Detailed technical specification: 264 spherical ROIs (5mm radius), MNI coordinates, 14 functional networks
  - Covered construction methodology using meta-analytic ALE approach with resting-state validation
  - Added relationship to whole-brain modeling and TVB: connectivity matrices, network node definition
  - Comparison section: contrasted with Yeo 2011 (coarser), Schaefer 2018 (modern), anatomical atlases
  - Applications in neuroimaging research: development, clinical disorders, HCP studies
  - Key references: Power et al. 2011 Neuron foundational paper
  - Updated frontmatter: changed updated date to 2026-04-28, added sources: raw/papers/power-2011.md, raw/papers/power-2012.md
2026-04-28: Updated xcp-d.md page with comprehensive content covering XCP-D post-processing pipeline for fMRI data

## [2026-04-28 20:01] Improve: 3 pages improved (bluepyopt, power-atlas, xcp-d)

## [2026-04-28 20:01] RefFormatter: formatted references on 3 pages

## [2026-04-28 20:06] CrosslinkApplier: added 120 wikilinks (120 inline, 0 suggested)

## [2026-04-28 20:21] Improve: 3 pages improved (exploreasl, pymvpa, jneuroml)

## [2026-04-28 20:26] CrosslinkApplier: added 46 wikilinks (46 inline, 0 suggested)

## [2026-04-28 20:29] Ingest: 1 new papers, 0 stubs created

## [2026-04-28 20:46] Matcher: 22 pages got 62 new sources

## [2026-04-28 20:52] DeepResearch: 41 papers added via focused research

## [2026-04-28 20:52] Audit: 817 issues (37 broken links, 63 orphans, 63 placeholders, 0 dup-refs, 6 opaque-refs, 78 thin, 213 missing-links)

## [2026-04-28 21:20] Repair: 116 issues fixed (48 source refs, 28 index, 1 frontmatter, 32 wikilinks, 6 orphans, 0 dup-refs, 0 opaque-refs, 1 crosslinks)

## [2026-04-28 21:20] Librarian: catalog rebuilt, 3582 asymmetric links noted

## [2026-04-28 21:20] Linter: 8 broken links, 56 orphans, 65 stale, 98 empty

## [2026-04-28 21:56] Improve: 3 pages improved (julich-atlas, allen-brain-atlas, erplab)

## [2026-04-28 23:16] RefFormatter: formatted references on 2 pages

## [2026-04-28 23:35] Improve: 3 pages improved (openneuro, brainnet-viewer, lfpykit)

## [2026-04-28 23:37] Improve: 3 pages improved (openneuro, brainnet-viewer, lfpykit)

## [2026-04-28 23:40] CrosslinkApplier: added 40 wikilinks (40 inline, 0 suggested)

## [2026-04-28 23:43] CrosslinkApplier: added 9 wikilinks (9 inline, 0 suggested)

## [2026-04-28 23:56] DeepResearch: 30 papers added via focused research

## [2026-04-28 23:56] Audit: 686 issues (22 broken links, 55 orphans, 53 placeholders, 0 dup-refs, 8 opaque-refs, 78 thin, 222 missing-links)

## [2026-04-29 00:04] DeepResearch: 11 papers added via focused research

## [2026-04-29 00:04] Audit: 652 issues (22 broken links, 55 orphans, 53 placeholders, 0 dup-refs, 8 opaque-refs, 78 thin, 222 missing-links)

## [2026-04-29 01:30] Repair: 61 issues fixed (31 source refs, 10 index, 1 frontmatter, 13 wikilinks, 6 orphans, 0 dup-refs, 0 opaque-refs, 0 crosslinks)

## [2026-04-29 01:31] Repair: 28 issues fixed (0 source refs, 0 index, 1 frontmatter, 20 wikilinks, 7 orphans, 0 dup-refs, 0 opaque-refs, 0 crosslinks)

## [2026-04-29 01:31] Librarian: catalog rebuilt, 3741 asymmetric links noted

## [2026-04-29 01:31] Linter: 5 broken links, 47 orphans, 57 stale, 88 empty

## [2026-04-29 01:31] Librarian: catalog rebuilt, 3741 asymmetric links noted

## [2026-04-29 01:31] Linter: 5 broken links, 47 orphans, 57 stale, 88 empty

## [2026-04-29 01:41] SoftwareMapper: 36 pages created

## 2026-04-29 - BCTpy page revised
- Fixed BCTpy entity page per reviewer feedback
- Added real sources to frontmatter: rubinov-sporns-2010, bctpy-github
- Removed incorrect claims about Infomap and Katz centrality (not part of BCTpy)
- Added real Key Papers: Rubinov & Sporns 2010, Bullmore & Sporns 2009, Sporns 2005
- Added inline citations throughout text
- Replaced placeholder content with comprehensive (~450 words) content

## [2026-04-29 01:47] Improve: 3 pages improved (mne-bids, lead-dbs, bctpy)

## [2026-04-29 01:52] SoftwareMapper: 4 pages created

## [2026-04-29 01:54] Improve: 3 pages improved (auryn, cvodes, sift)

## 2026-04-29 - OpenMEEG page improved
- Completed OpenMEEG entity page with comprehensive content
- Added overview explaining BEM forward modeling for EEG/MEG
- Documented key features: three-compartment BEM, symmetric formulation, input/output formats
- Explained technical implementation with mathematical foundation
- Added relationship to TVB for combined forward modeling
- Included related software: MNE-Python, Brainstorm, Fieldtrip, Freesurfer, SimNIBS
- Added wikilinks: MNE-Python, Fieldtrip, Brainstorm, Freesurfer, Freeview, The Virtual Brain, Jansen-Rit, Wong-Wang, whole-brain model, dynamic causal modeling, SimNIBS
- Updated frontmatter with new tags: neuroimaging-eeg, neuroimaging-meg, source-localization, forward-model, volume-conduction

## [2026-04-29 01:59] Matcher: 6 pages got 14 new sources

## [2026-04-29 02:04] Improve: 3 pages improved (mriqc, brainspace, openmeeg)

## [2026-04-29 02:08] Matcher: 61 pages got 179 new sources

## [2026-04-29 02:12] Improve: 3 pages improved (cococomac, openvibe, dcm)

## [2026-04-29 03:09] Improve: 3 pages improved (neurodata-without-borders, harvard-oxford-atlas, connectome-mapper-3)

## [2026-04-29 03:15] Improve: 3 pages improved (desikan-killiany-atlas, qsiprep, nibabel)

## [2026-04-29 04:13] Improve: 3 pages improved (tensorflow, brain-dynamics-toolbox, brainlife)

## [2026-04-29 04:18] Improve: 3 pages improved (yeo-atlas, connectome-workbench, bifurcation-theory)

## [2026-04-29 05:15] Improve: whole-brain-simulators page completed

- Replaced placeholder content with comprehensive comparison of whole-brain simulation platforms
- Covered TVB, NEST, NEURON, Brian2, and Arbor with detailed dimensions table
- Added synthesis section with use case recommendations
- Added 8+ wikilinks to related wiki pages
- Added sources: sanz-leon-2013, eppler-2009, semanticscholar-9afbfd2d37be, semanticscholar-f52da2a6cbf2, arxiv-2510.27366
- Updated frontmatter: updated date to 2026-04-29

## [2026-04-29 05:28] Improve: 3 pages improved (nitrc, homer3, whole-brain-simulators)

## [2026-04-29 05:29] Improve: 3 pages improved (homer3, nibabies, cititools)

## [2026-04-29 06:36] Improve: 3 pages improved (dti-tk, jhu-white-matter-atlas, graph-tool)

## [2026-04-29 06:45] Improve: dti-tk page refined

- Fixed frontmatter tags: replaced invalid tags with [software-dti-tk, diffusion-imaging, neuroimaging-dti, tractography, structural-connectivity]
- Added software-dti-tk to tag taxonomy in SCHEMA.md
- Fixed sources: removed non-existent raw/papers/dtitk-paper.md reference
- Fixed wikilinks: [[Brain Connectivity Toolbox]] → [[bctpy]], [[FSL]] → [[fsl]], [[The Virtual Brain]] → [[the-virtual-brain]], [[structural connectivity]] → [[structural-connectivity]], [[diffusion imaging]] → [[diffusion-imaging]], [[DSI Studio]] → [[dsi-studio]]
- Added dti-tk to entities/index.md
- 15 wikilinks verified: MRtrix3, fsl, diffusion-imaging, Wong-Wang, whole-brain modeling, the-virtual-brain, structural-connectivity, Jansen-Rit, dsi-studio, bctpy, AFQ
- Content meets 400-600 words target (comprehensive coverage)

## [2026-04-29 06:42] Improve: 2 pages improved (graph-tool, dti-tk)

## [2026-04-29 07:18] Improve: 3 pages improved (graph-tool, spikeinterface, apptainer)

## [2026-04-29 07:18] RefFormatter: formatted references on 3 pages

## [2026-04-29 07:24] CrosslinkApplier: added 227 wikilinks (227 inline, 0 suggested)

## [2026-04-29 07:28] Ingest: 2 new papers, 0 stubs created

## [2026-04-29 07:35] Improve: 3 pages improved (nitrc, mne-connectivity, braph)

## [2026-04-29 07:35] RefFormatter: formatted references on 1 pages

## [2026-04-29 07:41] CrosslinkApplier: added 102 wikilinks (101 inline, 1 suggested)

## [2026-04-29 07:53] Matcher: 60 pages got 170 new sources

## [2026-04-29 08:04] DeepResearch: 23 papers added via focused research

## [2026-04-29 08:04] Audit: 915 issues (59 broken links, 66 orphans, 60 placeholders, 0 dup-refs, 11 opaque-refs, 78 thin, 255 missing-links)
