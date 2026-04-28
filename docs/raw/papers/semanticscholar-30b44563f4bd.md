# The neural analysis toolkit unifies semi-analytical techniques to simplify, understand, and simulate dendrites

**Source**: semantic-scholar
**ID**: 30b44563f4bdb1b2c74cd2c13cbcc113a502dde7
**DOI**: 10.1101/2025.06.26.661734
**URL**: https://www.semanticscholar.org/paper/30b44563f4bdb1b2c74cd2c13cbcc113a502dde7
**Date**: 2025-06-27
**Year**: 2025
**Authors**: W. Wybo
**Venue**: bioRxiv
**Citations**: 0

## Abstract

While simulating compartmental dynamics in response to various input patterns is the prevalent technique for understanding dendritic computation, a great deal can be learned from classical analytical methods that provide solutions for the dendritic voltage. For example, such solutions are needed to simplify spatially extended neuron models, to understand frequency-dependent response properties, to elucidate the interaction between synaptic inputs, and hence to reveal the effective compartmentalization of dendrites into functional subunits. Nevertheless, these methods have not been implemented in modern software tools. This works describes the NEural Analysis Toolkit (NEAT), a Python toolbox that implements classical algorithms to compute response properties of spatially extended neuron models, and that leverages these algorithms to simplify them. Packaged with this are a range of useful utilities to plot morphologies and spatial quantities defined on the morphology, to distribute locations on the morphology, and to select parts of the morphology to e.g. apply morphological ablations or alter the membrane properties. The resulting models can be exported to NEURON and NEST, two commonly used simulators, the former focused on detailed single neuron model simulations, and the latter geared towards distributed network simulations. As a consequence, this toolbox provides a missing link between single neuron computation and large-scale network analysis, substantially facilitating the study of the role of dendritic computation in shaping emergent network dynamics. NEAT is available through pip under the name ‘nest-neat’, or from its source code (https://github.com/nest/NEAT), which is provided under the GNU General Public License. Furthermore, support for NEAT is provided on its GitHub page and through the NEST user mailing list (users@nest-simulator.org).
