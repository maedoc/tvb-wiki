# TVB Wiki Mass Ingestion Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan. Dispatch parallel subagents per domain.

**Goal:** Ingest 80+ annotated sources from `docs/sources-reference.md` into the TVB wiki, creating/updating entity pages, concept pages, and comparisons with full cross-linking.

**Domains:** 6 parallel workstreams
1. Neuroscience Platforms & Software (TVB, NEST, NEURON, ANTs)
2. Brain Modeling Concepts (neural mass, Wilson-Cowan, Jansen-Rit, etc.)
3. Neuroimaging (fMRI, EEG, DTI, resting-state)
4. Connectivity & Networks (connectome, HCP, UK Biobank, graph theory)
5. Biological Context (neurodevelopment, brain aging)
6. Mathematical Foundations (dynamical systems, DCM, mean-field theory)

**Wiki Structure:**
- `entities/` - Software, people, datasets, labs
- `concepts/` - Methods, modalities, topics
- `comparisons/` - Side-by-side analyses
- `raw/papers/` - Source papers
- `SCHEMA.md` - Tag taxonomy and conventions

---

## Domain 1: Neuroscience Platforms & Software

### Entities to Create/Update
- [[tvb]] - The Virtual Brain (major expansion needed)
- [[nest]] - NEST simulator (exists, needs expansion)
- [[neuron]] - NEURON simulator (exists, needs expansion)
- [[ants]] - ANTs registration toolkit
- [[graphvar]] - GraphVar toolbox
- [[modeldb]] - ModelDB repository
- [[bct]] - Brain Connectivity Toolbox (mentioned in graph theory section)

### People to Create
- [[michael schirner]] - TVB pipeline author
- [[marcus kaiser]] - Graph theory (indirectly)
- [[gustavo deco]] - Multiple papers
- [[karl friston]] - DCM founder
- [[olaf sporns]] - Connectomics
- [[randy buckner]] - Default mode network
- [[marcus raichle]] - Default mode network

### Concepts to Create/Update
- [[whole brain simulation]] - platforms comparison
- [[personalized brain modeling]] - Schirner pipeline
- [[spiking neural network simulation]] - NEST focus

### Comparisons to Create
- [[tvb vs nest vs neuron]] - exists but needs major expansion

### Raw Sources to Create
- `raw/papers/sanz-leon-2013-tvb.md`
- `raw/papers/ritter-2013-tvb-multimodal.md`
- `raw/papers/schirner-2018-personalized-pipeline.md`
- `raw/papers/woodman-2014-graphvar.md`
- `raw/papers/deco-2013-resting-brains.md`
- `raw/papers/gewaltig-diesmann-2007-nest.md`
- `raw/papers/potjans-diesmann-2014-cortical-microcircuit.md`
- `raw/papers/jordan-2018-nest-scalability.md`
- `raw/papers/eppler-2009-pynest.md`
- `raw/papers/helias-2012-supercomputers-neuroscience.md`
- `raw/papers/hines-carnevale-1997-neuron.md`
- `raw/papers/carnevale-hines-2006-neuron-book.md`
- `raw/papers/hay-2011-l5-pyramidal.md`
- `raw/papers/markram-2015-blue-brain.md`
- `raw/papers/migliore-2006-modeldb.md`
- `raw/papers/avants-2008-syn-registration.md`
- `raw/papers/tustison-2010-n4itk.md`
- `raw/papers/klein-2009-registration-evaluation.md`
- `raw/papers/avants-2011-ants-metrics.md`
- `raw/papers/tustison-2014-cortical-thickness.md`

---

## Domain 2: Brain Modeling Concepts

### Entities to Create
- [[walter freeman]] - Neural mass pioneer
- [[fernando lopes da silva]] - Thalamic model
- [[benjamin jansen]] - Jansen-Rit model
- [[vincent rit]] - Jansen-Rit model
- [[hugh wilson]] - Wilson-Cowan model
- [[jack cowan]] - Wilson-Cowan model
- [[alain destexhe]] - Computational neuroscientist
- [[terry sejnowski]] - Theoretical neuroscientist

### Concepts to Create/Update
- [[neural mass model]] - exists, needs major expansion
- [[jansen rit model]] - exists, needs expansion
- [[wilson cowan model]] - exists, needs expansion
- [[dynamic causal modeling]] - DCM framework
- [[mean field theory]] - Population dynamics
- [[bifurcation analysis]] - Dynamical transitions
- [[epilepsy modeling]] - Clinical application

### Comparisons to Create
- [[neural mass models comparison]] - exists, needs expansion

### Raw Sources to Create
- `raw/papers/dayan-abbott-2001-theoretical-neuroscience.md`
- `raw/papers/izhikevich-2007-dynamical-systems.md`
- `raw/papers/gerstner-2014-neuronal-dynamics.md`
- `raw/papers/koch-segev-1998-methods-neuronal-modeling.md`
- `raw/papers/breakspear-2017-dynamic-models.md`
- `raw/papers/freeman-1975-mass-action.md`
- `raw/papers/lopes-da-silva-1976-alpha-rhythm.md`
- `raw/papers/jansen-rit-1995-eeg-generation.md`
- `raw/papers/david-friston-2003-dcm-meg-eeg.md`
- `raw/papers/wendling-2002-epileptic-fast-activity.md`
- `raw/papers/wilson-cowan-1972-excitatory-inhibitory.md`
- `raw/papers/wilson-cowan-1973-functional-dynamics.md`
- `raw/papers/ermentrout-cowan-1979-visual-hallucinations.md`
- `raw/papers/destexhe-sejnowski-2009-wilson-cowan-retrospective.md`
- `raw/papers/breakspear-2006-primary-generalized-seizures.md`
- `raw/papers/rit-2013-neural-mass-realistic-eeg.md`
- `raw/papers/zavaglia-2006-rhythmic-activities.md`
- `raw/papers/touboul-2011-bifurcations-epilepsy.md`
- `raw/papers/stefanescu-jirsa-2008-low-dimensional.md`

---

## Domain 3: Neuroimaging

### Concepts to Create/Update
- [[fmri]] - exists, needs expansion
- [[eeg]] - exists, needs expansion
- [[meg]] - new
- [[dti]] - new
- [[diffusion mri]] - new
- [[resting state fmri]] - exists as [[resting state]], needs expansion
- [[bold signal]] - new
- [[functional connectivity]] - exists, needs expansion
- [[structural connectivity]] - new
- [[effective connectivity]] - new
- [[tractography]] - new
- [[independent component analysis]] - new

### Entities to Create
- [[seiji ogawa]] - fMRI inventor
- [[nikos logothetis]] - BOLD physiology
- [[bharat biswal]] - Resting-state pioneer
- [[steven smith]] - HCP methods
- [[marcus raichle]] - Default mode
- [[randy buckner]] - Default mode

### Comparisons to Create
- [[fmri vs eeg]] - exists, needs expansion
- [[connectivity types]] - exists, needs expansion

### Raw Sources to Create
- `raw/papers/ogawa-1990-bold-contrast.md`
- `raw/papers/logothetis-2001-fmri-neurophysiology.md`
- `raw/papers/friston-1994-statistical-parametric-mapping.md`
- `raw/papers/huettel-2009-fmri-textbook.md`
- `raw/papers/power-2012-motion-artifacts.md`
- `raw/papers/biswal-1995-resting-state-motor.md`
- `raw/papers/fox-raichle-2007-spontaneous-fluctuations.md`
- `raw/papers/smith-2009-correspondence-activation-rest.md`
- `raw/papers/zuo-2010-test-retest-icns.md`
- `raw/papers/buckner-2013-large-scale-analyses.md`
- `raw/papers/niedermeyer-da-silva-2004-eeg-textbook.md`
- `raw/papers/nunez-srinivasan-2006-electric-fields.md`
- `raw/papers/makeig-1996-ica-eeg.md`
- `raw/papers/cohen-2014-neural-time-series.md`
- `raw/papers/buzsaki-2012-extracellular-fields.md`
- `raw/papers/basser-1994-diffusion-tensor.md`
- `raw/papers/mori-1999-tractography.md`
- `raw/papers/jones-2010-diffusion-mri.md`
- `raw/papers/tournier-2007-csd.md`
- `raw/papers/sotiropoulos-zalesky-2019-connectomes.md`

---

## Domain 4: Connectivity & Networks

### Concepts to Create/Update
- [[connectome]] - new
- [[connectomics]] - new
- [[graph theory]] - new
- [[small world networks]] - new
- [[scale free networks]] - new
- [[rich club]] - new
- [[modularity]] - new
- [[network hubs]] - new
- [[structural core]] - new

### Entities to Create
- [[olaf sporns]] - Connectome pioneer
- [[ed bullmore]] - Graph theory neuro
- [[david van essen]] - HCP leader
- [[patricia miller]] - UK Biobank
- [[duncan watts]] - Small-world networks
- [[albert-laszlo barabasi]] - Scale-free networks
- [[mark newman]] - Network science

### Datasets/Projects to Create
- [[human connectome project]] - major entity
- [[uk biobank]] - major entity
- [[hcp]] - alias

### Comparisons to Create
- [[structural vs functional connectivity]] - exists, needs expansion

### Raw Sources to Create
- `raw/papers/sporns-tononi-kotter-2005-human-connectome.md`
- `raw/papers/van-essen-2013-hcp-overview.md`
- `raw/papers/hagmann-2008-structural-core.md`
- `raw/papers/sporns-2011-networks-of-the-brain.md`
- `raw/papers/rubinov-sporns-2010-bct.md`
- `raw/papers/van-essen-2012-hcp-acquisition.md`
- `raw/papers/glasser-2013-hcp-preprocessing.md`
- `raw/papers/smith-2013-hcp-resting-state.md`
- `raw/papers/ugurbil-2013-hcp-resolution.md`
- `raw/papers/barch-2013-hcp-task-fmri.md`
- `raw/papers/miller-2016-uk-biobank-imaging.md`
- `raw/papers/alfaro-almagro-2018-uk-biobank-qc.md`
- `raw/papers/elliott-2018-uk-biobank-gwas.md`
- `raw/papers/smith-2021-brain-aging-modes.md`
- `raw/papers/littlejohns-2020-uk-biobank-100k.md`
- `raw/papers/watts-strogatz-1998-small-world.md`
- `raw/papers/barabasi-albert-1999-scale-free.md`
- `raw/papers/newman-2010-networks-introduction.md`
- `raw/papers/friston-1993-functional-connectivity.md`
- `raw/papers/bullmore-sporns-2009-complex-brain-networks.md`
- `raw/papers/honey-2009-predicting-fc-from-sc.md`
- `raw/papers/power-2011-functional-network-organization.md`
- `raw/papers/smith-2013-functional-connectomics.md`

---

## Domain 5: Biological Context

### Concepts to Create/Update
- [[neurodevelopment]] - exists, needs expansion
- [[brain aging]] - exists, needs expansion
- [[default mode network]] - new
- [[cognitive reserve]] - new
- [[brain maintenance]] - new

### Entities to Create
- [[nitin goyal]] - Aging researcher
- [[nancy andrews-hanna]] - DMN fractionation
- [[andrei medvedev]] - DMN researcher

### Raw Sources to Create
- `raw/papers/tau-peterson-2010-brain-circuits-development.md`
- `raw/papers/gogtay-2004-cortical-development.md`
- `raw/papers/fair-2009-local-to-distributed.md`
- `raw/papers/power-2010-development-functional-networks.md`
- `raw/papers/stiles-jernigan-2010-brain-development-basics.md`
- `raw/papers/buckner-2004-memory-aging-ad.md`
- `raw/papers/grady-2012-cognitive-neuroscience-aging.md`
- `raw/papers/damoiseaux-2008-dmn-aging.md`
- `raw/papers/cabeza-2018-maintenance-reserve-compensation.md`
- `raw/papers/fjell-walhovd-2010-structural-aging.md`
- `raw/papers/raichle-2001-default-mode.md`
- `raw/papers/buckner-andrews-hanna-schacter-2008-dmn-anatomy.md`
- `raw/papers/greicius-2003-dmn-resting-state.md`
- `raw/papers/andrews-hanna-2010-dmn-fractionation.md`
- `raw/papers/anticevic-2012-dmn-deactivation.md`

---

## Domain 6: Mathematical Foundations

### Concepts to Create/Update
- [[dynamical systems theory]] - new
- [[bifurcation theory]] - new
- [[nonlinear dynamics]] - new
- [[dynamic causal modeling]] - new
- [[variational bayes]] - new
- [[free energy principle]] - new
- [[mean field theory]] - new
- [[stochastic differential equations]] - new
- [[fokker-planck equation]] - new

### Entities to Create
- [[stephen strogatz]] - Nonlinear dynamics
- [[eugene izhikevich]] - Dynamical systems neuro
- [[john guckenheimer]] - Bifurcation theory
- [[philip holmes]] - Dynamical systems
- [[yuri kuznetsov]] - Applied bifurcation
- [[stephen wiggins]] - Applied dynamics

### Raw Sources to Create
- `raw/papers/strogatz-1994-nonlinear-dynamics.md`
- `raw/papers/guckenheimer-holmes-1983-nonlinear-oscillations.md`
- `raw/papers/hirsch-smale-devaney-2004-differential-equations.md`
- `raw/papers/ermentrout-terman-2010-mathematical-foundations.md`
- `raw/papers/kuznetsov-2004-applied-bifurcation.md`
- `raw/papers/wiggins-2003-applied-nonlinear.md`
- `raw/papers/seydel-2010-practical-bifurcation.md`
- `raw/papers/doedel-oldeman-2009-auto-07p.md`
- `raw/papers/deco-jirsa-mcintosh-2012-metastability.md`
- `raw/papers/friston-2007-variational-free-energy.md`
- `raw/papers/beal-2003-variational-algorithms.md`
- `raw/papers/blei-2017-variational-inference-review.md`
- `raw/papers/wainwright-jordan-2008-graphical-models.md`
- `raw/papers/friston-2010-free-energy-principle.md`
- `raw/papers/rezende-mohamed-2015-normalizing-flows.md`
- `raw/papers/friston-2003-dynamic-causal-modeling.md`
- `raw/papers/stephan-2010-ten-rules-dcm.md`
- `raw/papers/daunizeau-2011-dcm-critical-review.md`
- `raw/papers/friston-2014-spectral-dcm.md`
- `raw/papers/penny-2004-comparing-dcm.md`
- `raw/papers/amit-brunel-1997-global-spontaneous.md`
- `raw/papers/brunel-2000-sparsely-connected.md`
- `raw/papers/deco-2008-dynamic-brain.md`
- `raw/papers/montbrio-2015-macroscopic-description.md`
- `raw/papers/schwalger-2017-cortical-columns.md`
- `raw/papers/gardiner-2009-stochastic-methods.md`
- `raw/papers/risken-1989-fokker-planck.md`
- `raw/papers/tuckwell-1988-theoretical-neurobiology-vol2.md`
- `raw/papers/deco-2009-stochastic-dynamics.md`
- `raw/papers/petkoski-jirsa-2019-delays-seizures.md`

---

## Integration Tasks

### Task: Update index.md
- Add all new entities, concepts, comparisons to index
- Update total page count
- Update last updated date

### Task: Cross-link pages
- Ensure every new page has 2+ outbound wikilinks
- Ensure bidirectional linking where appropriate
- Update existing pages to link to new content

### Task: Update log.md
- Append mass ingestion entry with all domains processed
- List files created/updated

---

## Verification

### Task: Run lint
- Check for orphan pages
- Check for broken wikilinks
- Check frontmatter compliance
- Check index completeness

---

## Success Criteria

- [ ] All 80+ sources have raw/ entries
- [ ] All major entities have populated pages (not placeholders)
- [ ] All major concepts have populated pages
- [ ] All comparisons have substantive content
- [ ] Every page has 2+ outbound wikilinks
- [ ] index.md updated with all pages
- [ ] log.md updated
- [ ] Lint passes with no critical issues
