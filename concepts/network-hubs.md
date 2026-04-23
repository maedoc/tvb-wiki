---
created: 2026-04-20
sources:
- raw/papers/sporns-2011.md
- raw/papers/bullmore-sporns-2009.md
- raw/papers/hagmann-2008.md
- raw/papers/power-2010.md
tags:
- network-dynamics
- connectomics
title: Network Hubs
type: concept
updated: '2026-04-24'
---

# Network Hubs

Highly connected nodes in brain networks that play crucial roles in information integration and communication.

## Definition

Hubs are nodes with significantly higher connectivity than average. In brain networks, they serve as critical points for information flow and integration across the network.

## Types of Hubs

### By Connectivity Pattern
- **Connector Hubs**: Connect different modules (high betweenness)
- **Provincial Hubs**: Connect nodes within the same module (high local connectivity)

### By Degree
- **Degree Hubs**: Nodes with highest number of connections
- **Strength Hubs**: Nodes with highest connection weights

## Brain Network Hubs

### Cortical Hubs
- **Posterior cingulate/precuneus**: Default mode network hub
- **Medial prefrontal cortex**: Default mode network hub
- **Lateral parietal cortex**: Attention network hub
- **Insular cortex**: Salience network hub

### Subcortical Hubs
- **Thalamus**: Relay hub for cortical communication
- **Hippocampus**: Memory network hub
- **Striatum**: Basal ganglia hub

## Measures of Hubness

### Degree Centrality
- Number of connections
- Simplest hub measure

### Betweenness Centrality
- Number of shortest paths passing through node
- Identifies connector hubs

### Participation Coefficient
- Distribution of connections across modules
- High = connector hub, Low = provincial hub

## Functional Importance

### Information Integration
- Hubs facilitate communication between distant regions
- Critical for global brain function

### Metabolic Cost
- Hubs consume more energy
- Vascular density correlates with connectivity

### Vulnerability
- Hub damage has disproportionate effects
- Targeted in many neurological diseases

## Clinical Relevance

### Disease
- **Alzheimer's**: Hub regions affected early
- **Schizophrenia**: Altered hub organization
- **Epilepsy**: Seizures may propagate through hubs

### Therapeutics
- Potential targets for brain stimulation
- Important for surgical planning

## Related Concepts
- [[rich-club]] – Hub interconnectivity
- [[structural-core]] – Dense hub network
- [[scale-free-networks]] – Hub distribution
- betweenness-centrality – Path-based hubness
- [[connectome]] – Complete connectivity