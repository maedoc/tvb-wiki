---
created: 2026-05-13
sources: []
tags:
- software-brain-modeling
- neural-mass-models
- dynamical-systems-theory
- mean-field-theory
- whole-brain-modeling
- parameter-estimation
- bifurcation-analysis
title: PyRates
type: entity
updated: '2026-05-13'
---

# PyRates

PyRates is an open-source Python framework for defining, simulating, and analyzing dynamical systems models of neural population activity. Developed by Richard Gast, Daniel Rose, and colleagues, PyRates provides a template-based model specification language that allows researchers to compose complex [[neural-mass-models]] from reusable building blocks—individual differential equations representing synaptic currents, firing rate functions, and coupling operators—and then simulate the resulting system via multiple numerical backends. The framework is designed to bridge the gap between mathematically flexible model prototyping and computationally efficient large-scale simulation, making it directly relevant to [[whole-brain-modeling]] workflows in platforms such as [[the-virtual-brain]].

## Motivation and Design Philosophy

[[computational-neuroscience]] has long faced a recurring tension: researchers need the freedom to modify model equations rapidly during exploratory phases, but they also require the computational performance to simulate those models at the scale of [[whole-brain]] networks. Traditional simulators have typically optimized for one of these poles. [[NEST]] and [[NEURON]] provide efficient simulation engines but use relatively fixed model libraries, while general-purpose scientific programming requires re-deriving and re-coding equations for every model variant. PyRates was designed to resolve this tension through an equation-oriented, operator-based architecture. Models are specified via human-readable YAML templates that encode individual differential equation terms as named operators, which can then be composed into circuits—directed graphs of interconnected neural populations spanning multiple brain regions. This design enables rapid model construction without sacrificing the ability to scale simulations across parameter spaces and network architectures.

The framework's name reflects its scope: PyRates operates at the level of **rate-based** neural population models, where the primary state variables are mean firing rates or average membrane potentials of large neuronal ensembles. This mesoscopic scale—above the resolution of individual [[spiking-neural-networks]] but below macroscopic [[brain-parcellations]]—is the natural domain of neural mass modeling, making PyRates a natural companion to TVB's whole-brain simulation engine.

## Template-Based Model Construction

The core innovation of PyRates lies in its template system. Rather than writing monolithic Python classes for each model, users define individual mathematical operators in YAML templates. For example, a generic excitatory synaptic operator might be defined as a differential equation for the postsynaptic current with parameters for time constant, reversal potential, and maximal conductance. These operator templates can then be instantiated with specific parameter values and assembled into neural population models. A single population template might combine an excitatory synapse operator, an inhibitory synapse operator, and a firing rate function (e.g., a sigmoidal or logistic transfer function) to produce a complete [[wilson-cowan]]-style node. Multiple population templates can then be wired together into circuits representing coupled brain regions.

This composability has two major advantages. First, it dramatically reduces code duplication: a single validated operator can be reused across dozens of model variants. Second, it enforces a clean separation between model structure and numerical implementation. The same YAML specification can be compiled for different backends—NumPy for prototyping, [[tensorflow]] for GPU acceleration, or even TVB's native backend for integration into whole-brain pipelines—without modifying the model definition. The template system also supports inheritance, allowing new models to extend and override parameters from parent templates, which is particularly valuable for systematic exploration of model families across [[parameter-estimation]] studies.

## Backend Architecture and Simulation

PyRates achieves computational flexibility through a multi-backend compilation step. After a circuit is defined in YAML, the framework's frontend parses the templates, resolves operator compositions, and generates an intermediate representation of the full dynamical system—a set of coupled ordinary differential equations augmented by algebraic expressions for derived quantities. This intermediate representation is then translated into executable code for the selected backend. The NumPy backend uses SciPy's ODE integrators and is suitable for single-node or small-network prototyping. The TensorFlow backend enables GPU-accelerated simulation of larger networks and facilitates gradient-based [[parameter-estimation]] via automatic differentiation. For whole-brain applications, PyRates can export models in a format directly consumable by TVB, allowing the same neural mass model used in exploratory single-region analysis to be deployed across a full [[structural-connectivity]] matrix.

The framework also provides built-in support for parameter sweeps and [[bifurcation-analysis]], enabling researchers to map the dynamical regimes of a model as a function of key parameters—identifying transitions between fixed points, oscillations, and chaotic activity. This is achieved through automated construction of parameter grids and parallel execution across the grid, which is particularly important when characterizing [[nonlinear-dynamics]] in models destined for large-scale simulation.

## Relationship to TVB

PyRates has a direct and growing relationship with [[the-virtual-brain]]. The frameworks operate at complementary levels of the whole-brain modeling stack. TVB provides the neuroinformatics infrastructure—structural connectivity from [[diffusion-imaging]] and [[tractography]], forward models for [[fmri]] and [[eeg]]/[[meg]], and simulation orchestration across large brain networks. PyRates provides the model specification layer—the tools to define, test, and parametrize the neural mass models that TVB places on each network node. Models developed and validated in PyRates can be exported to TVB's native format, enabling a workflow in which a researcher prototypes a novel neural mass model in PyRates (exploring its bifurcation structure and tuning parameters against local field potential or firing rate data), then deploys that same model across a connectome-scale brain network in TVB to predict [[resting-state]] [[functional-connectivity]] patterns.

This interoperability addresses a critical bottleneck in [[whole-brain-modeling]]: the difficulty of introducing new, biologically motivated neural mass models into large-scale simulations. Historically, whole-brain models have relied on a small set of canonical equations—[[jansen-rit]], [[wong-wang-model|Reduced Wong–Wang]], and generic oscillator models—because implementing a new model directly in TVB's backend required significant software engineering effort. PyRates lowers this barrier by acting as a model factory, enabling computational neuroscientists to specify novel population dynamics in a high-level declarative language and then materialize them for use in TVB's simulation engine. Recent developments have focused on tighter integration, including automated conversion of PyRates circuits into TVB's model representation format and the ability to use PyRates-generated model metadata for TVB's parameter exploration interfaces.

## Relationship to Other Frameworks

PyRates occupies a distinct and complementary niche within the broader landscape of neural simulation tools. Compared to [[brian2]], which targets the microscale of individual spiking neurons and synapses with an equation-based specification language, PyRates operates at the mesoscale of neural populations and rate models. Compared to [[dipde]], which implements population density methods for integrate-and-fire neurons, PyRates focuses on mean-field and neural mass formalisms where population activity is summarized by firing rate variables rather than voltage distributions. Compared to [[neurolib]], another Python-based whole-brain modeling library, PyRates emphasizes model specification and backend flexibility, whereas neurolib focuses on simulation orchestration and fitting to empirical neuroimaging data. These tools are increasingly interoperable, and a researcher working on multiscale brain modeling might use PyRates for model definition, neurolib for simulation management, and TVB for large-scale connectome-based simulation within a unified workflow.

## Key Features

- **Template-based model definition**: YAML templates for reusable differential equation operators, enabling composition, inheritance, and rapid model prototyping
- **Circuit construction**: Directed graphs of neural population nodes with flexible coupling schemes, suitable for modeling both local microcircuits and distributed brain networks
- **Multi-backend compilation**: Support for NumPy (prototyping), TensorFlow (GPU acceleration and automatic differentiation), and TVB-native export for whole-brain simulation
- **Parameter sweeps and bifurcation analysis**: Automated grid construction and parallel execution for mapping dynamical regimes and identifying critical transitions in model behavior
- **TVB integration**: Direct export of PyRates-defined models into TVB-compatible formats, enabling novel neural mass models to be deployed across [[connectome]]-scale simulations

## Related Software

- [[the-virtual-brain]] — Whole-brain simulation platform that consumes PyRates-defined models
- [[brian2]] — Microscale spiking [[neural-network]] simulator with similar equation-based philosophy
- [[dipde]] — Population density simulator for integrate-and-fire populations
- [[neurolib]] — Python whole-brain modeling library with emphasis on empirical fitting
- [[tvb-library]] — Core TVB library containing reference neural mass model implementations
- [[nest]] — Large-scale point-neuron simulator for spiking networks