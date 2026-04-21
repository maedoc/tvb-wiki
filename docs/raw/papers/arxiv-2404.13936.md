# A bound preserving cut discontinuous Galerkin method for one dimensional hyperbolic conservation laws

**arXiv ID**: 2404.13936
**Published**: 2024-04-22
**Updated**: 2024-06-05
**Authors**: Pei Fu, Gunilla Kreiss, Sara Zahedi
**Categories**: math.NA
**URL**: https://arxiv.org/abs/2404.13936
**PDF**: https://arxiv.org/pdf/2404.13936
**Source**: arXiv

## Abstract

In this paper we present a family of high order cut finite element methods with bound preserving properties for hyperbolic conservation laws in one space dimension. The methods are based on the discontinuous Galerkin framework and use a regular background mesh, where interior boundaries are allowed to cut through the mesh arbitrarily. Our methods include ghost penalty stabilization to handle small cut elements and a new reconstruction of the approximation on macro-elements, which are local patches consisting of cut and un-cut neighboring elements that are connected by stabilization. We show that the reconstructed solution retains conservation and order of convergence.   Our lowest-order scheme results in a piecewise constant solution that satisfies a maximum principle for scalar hyperbolic conservation laws.   When the lowest order scheme is applied to the Euler equations, the scheme is positivity preserving in the sense that positivity of pressure and density are retained. For the high-order schemes, suitable bound preserving limiters are applied to the reconstructed solution on macro-elements. In the scalar case, a maximum principle limiter is applied, which ensures that the limited approximation satisfies the maximum principle. Correspondingly, we use a positivity preserving limiter for the Euler equations and show that our scheme is positivity preserving. In the presence of shocks, additional limiting is needed to avoid oscillations, hence we apply a standard TVB limiter to the reconstructed solution. The time step restrictions are of the same order as for the corresponding discontinuous Galerkin methods on the background mesh. Numerical computations illustrate accuracy, bound preservation, and shock capturing capabilities of the proposed schemes.
