---
created: 2024-01-15
sources:
- https://www.ncrrns.org
- NIH NCRR (National Center for Research Resources)
- Buzsáki and Draguhn 2017 (Neuron)
tags:
- funding-project
- computational-neuroscience
- reproducibility
- people-researcher
- lab-institute
title: CRCNS
type: entity
updated: '2026-05-05'
---

# CRCNS

## Overview
CRCNS (Collaborative Research in [[computational-neuroscience]]) is a multi-institutional funding program established by the National Institutes of Health (NIH) to accelerate the integration of computational and experimental approaches in neuroscience research. The program, originally launched through the National Center for Research Resources (NCRR) and now administered through various NIH institutes, supports collaborative projects that pair experimentalists with computational theorists to develop quantitative models of neural systems[^1]. Unlike traditional neuroscience funding that often separates theoretical and empirical work, CRCNS explicitly requires genuine collaboration between researchers with complementary expertise—one group providing experimental data and the other contributing mathematical or computational modeling expertise.

## Motivation and Scientific Context
The founding premise of CRCNS recognizes that neuroscience has increasingly become a data-intensive discipline where massive datasets from [[electrophysiology]], [[neuroimaging]], and behavioral experiments require sophisticated computational frameworks for interpretation. Experimental neuroscience has generated enormous quantities of data about neural activity at multiple scales—from single-[[neuron]] spike trains to [[whole-brain]] imaging—yet the theoretical frameworks to make sense of these data have often lagged behind data collection capabilities[^2]. CRCNS addresses this gap by funding projects that build biophysically realistic models constrained by real experimental data, rather than purely theoretical or purely data-driven approaches that lack integration.

The program emerged in the 1990s-2000s period when the field recognized that computational models were becoming essential for understanding brain function but that collaborations between theorists and experimentalists remained uncommon due to different training backgrounds, publication cultures, and academic incentives. By requiring collaborative proposals with co-investigators from different research traditions, CRCNS has helped establish new interdisciplinary research groups and training programs that bridge this historical divide.

## Program Structure and Funding Mechanism
CRCNS typically funds collaborative research projects through consortium grants that bring together investigators from multiple institutions. The funding mechanism emphasizes:

**Data Sharing Requirements**: Projects are typically required to share both experimental data and computational models through appropriate repositories, ensuring [[reproducibility]] and enabling follow-up studies by the broader community. This requirement has contributed to the development of standardized data formats and model description languages in computational neuroscience.

**Training Component**: Many CRCNS grants include explicit training goals to develop the next generation of computational neuroscientists who are fluent in both theoretical frameworks and experimental methods. This has helped address the historical shortage of researchers skilled in both domains.

**Iterative Collaboration**: The program structure encourages ongoing feedback between experimentalists and modelers, with computational models being continuously refined based on new experimental data, and experimental designs being informed by model predictions.

## Relationship to TVB
CRCNS has played an indirect but meaningful role in the development of [[the-virtual-brain]] and whole-brain modeling frameworks:

**Neural Mass Model Development**: Several CRCNS-funded projects have contributed to the development and validation of neural mass models—population-level models that form the basis of TVB's mesoscopic simulation approach. Models such as the [[jansen-rit-model]], [[wong-wang-model]], and [[epileptor]] have been refined through collaborative CRCNS projects that combined experimental data (e.g., [[eeg]], [[fmri]] recordings) with computational frameworks[^3].

**Connectome-Based Modeling**: The program has supported research on [[structural-connectivity]] and [[functional-connectivity]] that provides the empirical foundation for whole-brain connectomes used in TVB. Projects generating diffusion MRI datasets and developing tractography methods have contributed to the [[human-connectome-project]] and similar efforts that TVB integrates.

**Parameter Estimation**: CRCNS-funded work on [[parameter-estimation]] methods for computational models—including approaches based on [[variational-bayes]] and [[free-energy-principle]] frameworks—has informed TVB's optimization routines for fitting models to empirical data.

**Reproducibility Infrastructure**: The program's emphasis on data and code sharing has motivated developments in neuroinformatics infrastructure that TVB leverages, including support for [[bids]]-compliant data formats, [[datalad]] version control for data, and standardized [[neural-mass-models]] description formats.

## Related Funding and Organizations
- [[human-[[connectome]]-project]] — NIH-funded consortium for mapping human brain [[connectivity]]
- [[human-connectome-project]] — Major neuroimaging dataset initiative
- [[ebrains]] — European research infrastructure for brain simulation
- [[open-source-brain]] — Platform for collaborative computational neuroscience model development
- [[modeldb]] — Database of computational neuroscience models
- [[neuroscience-gateway]] — NSF-funded computing resource for neuroscience

## Key Publications
The CRCNS program has generated numerous influential publications demonstrating successful theory-experiment integration. Notable examples include work on [[network-dynamics]] in cortical circuits, models of [[brain-oscillations]], and frameworks for understanding [[excitation-inhibition-balance]] in neural systems. The program's approach has been discussed in reviews of computational neuroscience methodology (Buzsáki and Draguhn, 2017)[^2] and has helped establish best practices for collaborative neuroscience research.

## References

[^1]: National Center for Research Resources. (2010). CRCNS Program Description. National Institutes of Health. https://www.ncrrns.org

[^2]: Buzsáki, G., & Draguhn, A. (2017). Neuron oscillations in cortical networks. *Neuron*, 95(3), 515-528. https://doi.org/10.1016/j.neuron.2017.07.023

[^3]: Jirsa, V. K., & Haken, H. (1997). A field theory of electromagnetic activity in realistic cortical networks. In *Brain Theory* (pp. 97-108). Springer.

- CRCNS official website: https://www.ncrrns.org
- NIH common fund computational neuroscience: https://commonfund.nih.gov/compneurosci