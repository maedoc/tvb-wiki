---
title: NeuroElectro
created: 2026-04-20
updated: 2026-05-12
type: entity
tags: [dataset, neural-mass-models, parameter-estimation, spiking-neural-networks, whole-brain-modeling]
sources: []
---

NeuroElectro is a curated database and web resource that extracts, organizes, and summarizes published electrophysiological properties of diverse neuron types from the neuroscience literature. It employs a semi-automated pipeline combining text mining of journal articles with expert manual curation to populate a structured repository of cellular biophysical measurements. By centralizing data that were previously scattered across thousands of publications with heterogeneous reporting conventions, NeuroElectro provides a critical empirical bridge between experimental cellular neuroscience, [[computational-neuroscience]], and computational modeling frameworks including [[neuronunit]], [[the-virtual-brain]], and large-scale [[spiking-neural-networks]] simulations.

## Motivation and Context

Before NeuroElectro, electrophysiologists and computational modelers who wished to compare intrinsic properties across neuron types or constrain [[parameter-estimation]] for simulations faced a fragmented literature in which measurements of resting membrane potential, input resistance, or spike threshold were reported using inconsistent terminologies and buried within diverse journal formats. Large-scale neuroinformatics projects had already demonstrated the value of aggregating specialized data: [[the-virtual-brain]] offers platforms for [[whole-brain-modeling]], tools such as [[software-nest]] provide simulation engines for [[spiking-neural-networks]], and resources like ModelDB archive computational models. However, a comparable centralized repository for raw electrophysiological values was lacking. NeuroElectro fills this gap by systematically harvesting tabular biophysical data from journal articles, thereby reducing the manual search burden and enabling meta-analyses that link cellular physiology to system-level [[network-dynamics]].

## Technical Approach

The extraction workflow begins with full-text articles in machine-readable HTML or XML, screened algorithmically for relevant electrophysiological terminology. Candidate data tables are parsed using fuzzy string matching against a domain-specific lexicon that maps synonyms to canonical concepts—for example, mapping variants of "resting membrane potential" to a single entity. Identified measurements are mapped to neuron types using the NeuroLex ontology, and machine-assisted assignments are subsequently validated by human curators. Normalization is applied where possible to account for protocol differences, such as variations in recording temperature or electrode compensation. The resulting dataset is stored in a relational database and exposed through both an interactive web interface and a RESTful API capable of returning structured data for programmatic access.

## Relationship to Related Resources

NeuroElectro occupies a complementary position in the neuroinformatics ecosystem. While [[the-virtual-brain]] and [[software-nest]] focus on simulating [[network-dynamics]] at the mesoscopic or microscopic scale, NeuroElectro supplies the empirical biophysical parameters required to ground those simulations in published experimental data. It parallels the mission of [[neuronunit]], which provides a validation framework for neuroscience models; indeed, NeuroElectro’s curated values can serve as reference datasets against which single-neuron or population models are tested. The project also shares methodological kinship with [[neuroimaging]] literature-mining initiatives, though it operates on structured data tables rather than activation coordinates or [[functional-connectivity]] maps.

## Biological Grounding for Modelers

The quantities archived by NeuroElectro correspond directly to the biophysical variables that underlie both detailed compartmental models and reduced [[neural-mass-models]]. Resting membrane potential reflects the aggregate leak conductance of a cell population; input resistance and membrane time constant determine how synaptic inputs are temporally integrated; spike threshold, width, and amplitude encode the kinetics of voltage-gated sodium and potassium currents; and afterhyperpolarization characteristics reveal the influence of calcium-dependent potassium conductances. By tabulating these properties across genetically and anatomically identified neuron classes, NeuroElectro captures the intrinsic heterogeneity that [[whole-brain-modeling]] frameworks must average or parameterize when assigning node properties in large-scale graphs.

## Relationship to TVB

Although NeuroElectro operates at the single-cell scale, it interfaces directly with [[the-virtual-brain]] workflows by supplying empirically grounded estimates for parameters that are otherwise free variables in neural mass formulations. TVB population models abstract millions of neurons into mean-field variables, yet their effective time constants, firing thresholds, and gain functions can be anchored to distributions of cellular properties measured in vitro. As TVB expands toward multi-scale architectures that couple large-scale connectivity with local circuit detail, databases such as NeuroElectro become essential for setting physiologically plausible ranges in both [[neural-mass-models]] and hybrid schemes that embed [[spiking-neural-networks]] within connectome-based simulations.
