---
title: Fractional Anisotropy
created: 2026-04-20
updated: 2026-05-09
type: concept
tags: [diffusion-imaging, neuroimaging-dti, structural-connectivity, white-matter, connectomics]
sources: [raw/papers/smith-2013-connectomics.md, raw/papers/friston-1993.md]
---

Fractional anisotropy (FA) is a scalar measure derived from diffusion tensor imaging (DTI) that quantifies the degree of directional preference in water diffusion within neural tissue. Mathematically, FA is computed from the eigenvalues of the diffusion tensor (λ₁, λ₂, λ₃) and ranges from 0 to 1, where 0 indicates isotropic diffusion (equal in all directions, as would occur in freely diffusing water) and 1 indicates totally anisotropic diffusion (restricted to a single axis). This measure serves as one of the most widely used indices of white matter integrity in neuroimaging research, providing a window into the microstructural organization of neural pathways that is otherwise invisible to conventional anatomical MRI.

## Motivation and Context

The development of diffusion tensor imaging in the 1990s revolutionized our ability to visualize white matter architecture in vivo [[neuroimaging]]. Prior to DTI, assessing white matter integrity required post-mortem histological examination, limiting both sample sizes and longitudinal research designs. FA emerged as a quantitative summary metric that could be computed from DTI data to characterize the coherence and organization of white matter tracts across the entire brain.

In whole-brain modeling contexts, FA values are commonly used to weight structural connectivity matrices, where higher FA indicates stronger and more reliable structural connections between brain regions. This weighting scheme reflects the empirical observation that tracts with higher anisotropy tend to support more robust functional integration between distant cortical areas, as measured by [[resting-state]] functional connectivity [[connectomics]].

The significance of FA extends beyond basic neuroanatomy into clinical and cognitive neuroscience applications. Reduced FA has been documented in numerous neurological and psychiatric conditions, including multiple sclerosis [[lems]], stroke, schizophrenia [[schizophrenia-models]], and Alzheimer's disease [[alzheimers-disease]], making it a valuable biomarker for disease progression and treatment response. In the context of [[whole-brain modeling]], FA-weighted structural connectivity serves as the anatomical substrate from which [[brain-network]] dynamics emerge, enabling researchers to simulate how structural damage (reflected in lowered FA) might propagate through large-scale brain networks to produce functional deficits [[connectomics]].

## Technical Foundation

The diffusion tensor is a 3×3 symmetric matrix that characterizes the Gaussian diffusion profile at each voxel. In anisotropic tissue such as white matter, the tensor has three orthogonal eigenvectors with corresponding eigenvalues that describe the principal directions and magnitudes of diffusion. FA is computed from these eigenvalues using the formula:

$$FA = \sqrt{\frac{1}{2}} \frac{\sqrt{(\lambda_1 - \lambda_2)^2 + (\lambda_2 - \lambda_3)^2 + (\lambda_1 - \lambda_3)^2}}{\sqrt{\lambda_1^2 + \lambda_2^2 + \lambda_3^2}}$$

This formula normalizes the deviation from isotropic diffusion relative to the overall diffusion magnitude. When λ₁ = λ₂ = λ₃ (isotropic diffusion), the numerator becomes zero and FA = 0. When λ₂ and λ₃ approach zero while λ₁ remains non-zero (highly anisotropic diffusion), the numerator approaches the denominator and FA approaches 1.

## Relationship to Structural Connectivity

In [[whole-brain modeling]], FA plays a critical role in constructing [[structural-connectivity]] matrices that define the anatomical wiring between brain regions. [[Tractography]] algorithms, which reconstruct white matter tracts from diffusion MRI data, generate streamlines representing hypothesized axonal pathways. Each streamline can be weighted by the FA values along its trajectory to create weighted connectivity matrices. These weighted matrices form the structural foundation upon which [[brain-dynamics]] simulations proceed, whether using [[neural-mass-models]] such as [[jansen-rit-model]] or [[wong-wang-model]], or more detailed [[spiking-neural-networks]] implementations.

The use of FA-weighted tractography reflects a fundamental assumption in connectomics: that stronger structural connections support more reliable information transfer between brain regions. While this assumption has proven empirically useful, it represents a simplification. FA captures only the degree of directional coherence and cannot distinguish between different underlying biological substrates—changes in FA could reflect alterations in axonal density, myelin thickness, fiber diameter, or fiber organization [[dti-vs-hardi-vs-noddi]].

## Biological Interpretation and Limitations

Interpreting FA requires awareness of its limitations as a summary metric. Because FA conflates multiple microstructural features into a single value, two voxels with identical FA may have vastly different biological properties. For example, a voxel with tightly packed, highly aligned axons may produce the same FA as one with fewer but more coherently oriented fibers, making interpretation ambiguous without additional context [[dti-vs-hardi-vs-noddi]].

### Crossing Fibers and Partial Volume Effects

One of the most significant limitations of FA is its inability to resolve crossing fibers. In regions where multiple fiber populations intersect atangles less than the angular resolution of standard DTI (typically 30-45°), FA values are artificially lowered because the diffusion tensor can only capture a single principal direction. This leads to systematic underestimation of white matter integrity in complex fiber architectures such as the centrum semiovale, where projection, association, and callosal fibers intermingle. Partial volume effects compound this issue: voxels containing mixtures of different tissue types (such as gray matter adjacent to white matter, or cerebrospinal fluid) yield intermediate FA values that may not accurately represent either tissue type.

### Axonal Density vs. Myelination

FA cannot distinguish between changes in axonal density and changes in myelin content, as both factors increase directional coherence. This ambiguity limits the interpretability of FA changes in developmental studies, aging research [[aging-brain]], and disease contexts where demyelination and axonal loss may occur in parallel or isolation. Researchers interested in dissociating these microstructural contributions must turn to advanced diffusion models that provide separate indices.

## Alternative Diffusion Metrics

FA is often reported alongside other tensor-derived metrics that provide complementary information. Mean diffusivity (MD) measures the average magnitude of diffusion independent of direction, and is elevated in conditions involving tissue loss or increased extracellular space. Radial diffusivity (RD) reflects diffusion perpendicular to the principal axis and is particularly sensitive to myelin integrity, with elevated RD commonly interpreted as demyelination. Axial diffusivity (AD) captures diffusion along the principal axis and has been linked to axonal damage in some contexts [[dti-vs-hardi-vs-noddi]].

Beyond DTI, advanced diffusion models offer more specific indices. High-angular-resolution diffusion imaging (HARDI) and diffusion spectrum imaging (DSI) can resolve multiple fiber populations per voxel, enabling more accurate tractography in crossing fiber regions. Neurite orientation dispersion and density imaging (NODDI) provides separate estimates of neurite density (intra-neurite compartment) and orientation dispersion (extra-neurite compartment), offering clearer biological interpretation than FA alone [[dti-vs-hardi-vs-noddi]].

In the context of [[aging-brain]] research, FA shows characteristic decreases in specific white matter tracts with advancing age, reflecting demyelination and axonal loss. The relationship between FA and cognitive function is complex: while higher FA in certain tracts predicts better performance on tasks requiring speeded information processing, the association is not uniform across all cognitive domains or brain regions. This nuance highlights the importance of combining [[structural-connectivity]] analyses with [[functional-connectivity]] assessments when investigating the neural basis of cognition [[connectomics]].

## Relationship to Whole-Brain Modeling

Within the TVB ecosystem, FA-weighted structural connectivity matrices are imported from external [[diffusion-imaging]] preprocessing pipelines (such as [[mrtrix3-connectome]] or [[connectome-workbench]]) to initialize [[whole-brain]] simulations. The default TVB workflow treats FA as a proxy for connection strength, though users can select alternative weighting schemes or import custom structural connectivity data. Given that TVB simulates [[brain-dynamics]] at the level of [[brain-network]] activity, the anatomical fidelity of the structural connectivity substrate—reflected in large part by FA-derived weights—directly influences the accuracy of simulated functional dynamics. Improving FA estimation through advanced [[diffusion-mri]] acquisition and analysis techniques thus remains an active area of methodological development in the [[computational-neuroscience]] community [[karl-j-friston]].

## See Also

- [[diffusion-imaging]] – Overview of diffusion MRI techniques
- [[neuroimaging|diffusion-tensor-imaging]] – DTI methodology and applications
- [[dti-vs-hardi-vs-noddi]] – Comparison of diffusion modeling approaches
- [[structural-connectivity]] – Anatomical brain wiring
- [[tractography]] – White matter tract reconstruction
- [[connectomics]] – Brain connectivity research
- [[aging-brain]] – Age-related white matter changes
- [[brain-network]] – Network-based brain analysis
- [[whole-brain-modeling]] – Large-scale brain simulation

## References

1. Smith, S. M., Vidaurre, D., et al. (2013). Functional Connectomics from Resting-State fMRI. *Trends in Cognitive Sciences*. [[connectomics]]

2. Friston, K. J., Frith, C. D., Liddle, P. F., & Frackowiak, R. S. J. (1993). Functional Connectivity: The Principal-Component Analysis of Large (PET and fMRI) Data Sets. *Journal of Cerebral Blood Flow & Metabolism*. [[karl-j-friston]]

3. Basser, P. J., & Pierpaoli, C. (1996). Microstructural and physiological features of tissues elucidated by quantitative-diffusion-tensor MRI. *Journal of Magnetic Resonance Series B*, 111(3), 209-219.