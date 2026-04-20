---
title: Scale-Free Networks
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [network-dynamics, connectomics]
sources: [raw/papers/barabasi-albert-1999.md, raw/papers/bullmore-sporns-2009.md]
---

# Scale-Free Networks

Networks with power-law degree distributions, characterized by the presence of hubs.

## Definition

Scale-free networks exhibit a power-law degree distribution:
- P(k) ~ k^(-γ)
- Most nodes have few connections
- A few nodes (hubs) have many connections
- Degree distribution follows a straight line on log-log plots

## Key Properties

### Power-Law Distribution
- **Exponent (γ)**: Typically 2 < γ < 3 for real networks
- **No characteristic scale**: Unlike random networks
- **Heavy tail**: High-degree nodes much more likely than in random networks

### Preferential Attachment
albert-laszlo barabasi|Barabási and Albert (1999) proposed the mechanism:
- New nodes preferentially attach to high-degree nodes
- "Rich get richer" principle
- Generates power-law distributions

## Brain Networks

### Evidence
Brain networks show scale-free properties:
- Hub regions with many connections
- Power-law-like degree distributions
- Presence of connector hubs

### Important Caveats
- Strict power laws may not hold
- Often better described as "heavy-tailed"
- Truncated power laws common in physical networks

### Hub Organization
- **Connector Hubs**: Link different modules
- **Provincial Hubs**: Connect within modules
- **Rich-Club**: Hubs connect to other hubs

## Implications

### Robustness
- Resilient to random node removal
- Vulnerable to targeted hub removal

### Dynamics
- Hubs influence network dynamics
- Important for information spreading
- Target for therapeutic interventions

## Related Concepts
- [[network-hubs]] – Highly connected nodes
- [[rich-club]] – Hub interconnectivity
- preferential-attachment – Growth mechanism
- [[graph-theory]] – Mathematical framework
- [[brain-network]] – Network organization
