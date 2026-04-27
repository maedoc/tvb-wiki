# Fluid flow and mass transport along a microchannel with physics-informed neural networks

**Source**: semantic-scholar
**ID**: 98d58b992da8c231eac53376c15333fa536307fe
**DOI**: 10.3389/fmech.2025.1651334
**URL**: https://www.semanticscholar.org/paper/98d58b992da8c231eac53376c15333fa536307fe
**Date**: 2026-01-21
**Year**: 2026
**Authors**: Mehmet Melih Tatlisoz, Cetin Canpolat
**Venue**: Frontiers of Mechanical Engineering
**Citations**: 0

## Abstract


 
 In the present study, fluid and mass transport along a microchannel are aimed to be solved using physics-informed neural networks (PINN), which is an emerging solution method for partial differential equations (PDEs). For verification purposes, the same cases under identical conditions are modeled with a solver for finite element analysis (FEA), COMSOL Multiphysics.
 
 
 
 
 Continuity, Navier-Stokes, and Nernst-Planck Equations, which characterize momentum and mass conservation, are solved simultaneously by PINN as well as COMSOL Multiphysics. The problems are defined as steady or time-dependent with varying Reynolds numbers in the interval of 5 × 10
 −6
 ≤ Re ≤ 5 × 10
 −2
 . The fluid is flowed by either pressure-driven or electrokinetically-driven. PDEs are nondimensionalized by scaling the quantities for PINN solving on the purpose of alleviating the computational burden. In contrast to usual approach, where the pressure scale is viscosity multiplied by the velocity scale divided by the length scale, pressure scale is determined as its maximum value.
 
 
 
 
 
 Calculation errors of PINN solver are observed as reasonably low, such as 3.04 × 10
 −5
 , 4.76 × 10
 −3
 , 3.60 × 10
 −4
 , 6.02 × 10
 −3
 for steady pressure-driven flow, time-dependent pressure-driven flow, steady electroosmotic flow, and time-dependent electroosmotic flow, respectively. To reduce the error margin at these values, pressure scale must be defined as the maximum pressure value. Therefore, the results of the FEA solver exhibit excellent overlap with the data obtained from PINN. For PINN, species concentrations of 0.52–1.75–2.71–3.36 mol/m
 3
 are accumulated at the outlet under pressure-driven flow for time points 50–100–150–200 seconds, respectively. Under electrokinetic flow, species concentrations are varied as 0.72–1.93–2.83–3.46 mol/m
 3
 for the same time points, respectively. In consideration of FEA, species concentrations are calculated as 0.52–1.75–2.71–3.39 mol/m
 3
 and 0.55–1.85–2.84–3.52 mol/m
 3
 under similar conditions for pressure-driven and electroosmotic flows, respectively.
 
 
 
 
 Both Navier-Stokes and Nernst-Planck Equations can be solved with PINN in a single model, regardless of the flow generation method and the time dependency of the model. Because nearly identical calculations are carried out by the FEA solver. As a result, PINN is a notable alternative for simultaneous modeling of the flow and mass transport under pressure-driven and electrokinetic conditions for microfluidic applications.

