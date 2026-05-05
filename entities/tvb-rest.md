---
created: 2025-01-15
sources:
- raw/papers/Sanz-LeonEtAl-2015.md
tags:
- software-tvb
- rest
- api
- the-virtual-brain
- whole-brain-modeling
title: TVB-REST
type: entity
updated: '2026-05-05'
---

TVB-[[rest]] is the application programming interface (API) layer of [[tvb|The Virtual Brain]] that enables programmatic interaction with the TVB simulation engine via HTTP requests. As a RESTful web service, TVB-REST allows researchers to remotely launch brain simulations, retrieve results, manage datasets, and integrate TVB functionality into custom workflows without requiring direct Python execution on the local machine [@Sanz-LeonEtAl-2015]. This architectural choice positions TVB as not merely a desktop application but as a cloud-ready [[neuroimaging]] platform capable of supporting distributed [[whole-brain|whole-brain modeling]] workflows across institutional research environments.

## Motivation and Context

The development of TVB-REST emerged from the growing need to integrate [[whole-brain-modeling|whole-brain]] simulations into larger neuroimaging analysis pipelines and to support collaborative research workflows where multiple users require simultaneous access to computational resources. Traditional desktop installations of TVB require the full Python environment with all dependencies, which can be cumbersome for users who primarily need to run simulations or access results without engaging with the underlying implementation details. Furthermore, high-performance computing clusters often lack graphical user interfaces, making the TVB GUI impractical in such environments. TVB-REST addresses these limitations by exposing TVB's core functionality through a standardized web API, enabling headless operation and seamless integration with workflow management systems such as [[snakemake]] and containerized execution platforms like [[docker]] and [[apptainer]].

The API also facilitates the construction of service-oriented architectures where TVB serves as one component within a larger neuroinformatic pipeline. For instance, researchers can use TVB-REST to generate simulated [[resting-state|resting-state]] [[bold-signal|BOLD signals]] from [[structural-connectivity|structural connectivity]] data, which can then be compared against empirically acquired fMRI data for model validation or parameter estimation [@Sanz-LeonEtAl-2015]. This modular approach to whole-brain modeling aligns with broader trends in computational neuroscience toward reproducible, containerized analysis workflows.

## Key Features

TVB-REST provides a comprehensive set of endpoints that mirror the core functionality of the TVB library. The simulation endpoint allows users to configure and launch whole-brain simulations by specifying the [[neural-mass-model|neural mass model]] (such as the [[jansen-rit-model|Jansen-Rit]] or [[wong-wang-model|Wong-Wang]] models), the structural [[connectivity]] matrix, stimulation parameters, and simulation duration [@Sanz-LeonEtAl-2015]. Upon submission, the API returns a job identifier that can be used to poll for completion status and retrieve results once the simulation finishes.

Data management endpoints enable users to upload custom [[connectivity]] datasets in standard formats (ZIP archives containing connectivity matrices and metadata), list available datasets in the associated TVB storage, and delete unwanted data. The API also provides access to TVB's built-in analysis operations, including functional connectivity estimation using correlation or coherence measures, [[graph-theory|graph-theoretic]] network metrics, and temporal stability analysis. Result retrieval supports multiple output formats, with the ability to return time series, connectivity matrices, or derived metrics in formats compatible with external visualization tools such as [[connectome-workbench]] or [[brainnet-viewer]].

## Relationship to TVB

TVB-REST operates as a thin wrapper around the [[tvb-library]], exposing its Python-based simulation and analysis capabilities through HTTP. The [[tvb-library]] provides the core computational engine implementing various [[neural-mass-models]], the mathematical formalisms governing large-scale brain network dynamics, and the data structures for representing brain connectivity. TVB-REST translates REST requests into appropriate library calls, manages the execution context (including [[docker]] containerization when deployed in isolated environments), and serializes results back to clients. This architecture ensures that API users obtain functionally identical results to those produced by the TVB GUI or direct Python scripts using the library [@Sanz-LeonEtAl-2015].

The deployment of TVB-REST forms the backbone of TVB's cloud-based offerings and supports the [[personalized-brain-modeling]] workflow wherein individual subject connectivity data is used to generate personalized brain simulations. Researchers can submit connectivity data from diverse sources—including [[dti|DTI]] tractography pipelines or the [[hcp-dataset|Human Connectome Project]]—through the API, obtain simulated [[bold-signal|BOLD signals]] or [[eeg|EEG]]/[[meg|MEG]] forward solutions, and compare these against empirical measurements to refine model parameters. This integration of TVB-REST with clinical applications such as [[epilepsy-modeling]] demonstrates its utility in translational research contexts where simulation-driven insights inform patient-specific interventions [@JirsaEtAl-2017].

## Technical Considerations

Deploying TVB-REST requires a server environment with sufficient computational resources to run whole-brain simulations, which can demand substantial CPU or GPU capacity depending on model complexity and simulation duration. The API supports asynchronous execution patterns wherein long-running simulations are queued and executed in background processes, with clients polling for completion. Authentication and authorization mechanisms ensure that multi-user deployments maintain data isolation between researchers. The API communicates using JSON for request/response payloads, and standard HTTP status codes indicate success or error conditions. Client libraries exist for several programming languages, facilitating integration into existing analysis codebases.

## Key Papers

- [@Sanz-LeonEtAl-2015] — [[the-virtual-brain]]: a academic software platform for modeling and simulation of whole-[[brain-dynamics]]
- [@JirsaEtAl-2017] — Performance of Virtual Brain in clinical contexts — The epilepsy use case

## Related Software

- [[tvb-library|TVB Library]] — Core simulation engine
- [[tvb|TVB]] — Complete software ecosystem
- [[nest|NEST]] — Neural simulation tool compatible with TVB
- [[brain-dynamics-toolbox|Brain Dynamics Toolbox]] — Alternative whole-brain simulation framework
- [[pynest|PyNEST]] — Python interface to NEST