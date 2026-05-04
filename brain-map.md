title: Brain Map
created: 2024-01-15
updated: 2026-05-04
type: concept
tags: [connectomics, structural-connectivity, functional-connectivity, brain-parcellations, neuroimaging, whole-brain-modeling, parcellation]
sources: [[doi:10.1016/j.neuroimage.2020.116923], [doi:10.1002/hbm.25247], [doi:10.1016/j.neuroimage.2021.117987], [doi:10.1002/hbm.23821], [doi:10.1073/pnas.0601607103]]
---

A brain map in the context of whole-brain modeling refers to a computational representation of the brain's regional structure and connectivity. It comprises two essential components: a parcellation scheme that divides the brain into discrete regions (nodes), and a connectivity matrix that characterizes the structural or functional connections between those regions (edges). Brain maps serve as the foundational anatomical scaffold upon which [[whole-brain-modeling|whole-brain simulations]] are constructed, providing the bridge between empirical neuroimaging data and computational models of neural dynamics.

## Historical Context

The concept of brain mapping traces its origins to the early 20th century, when neuroanatomist Korbinian Brodmann published his influential cytoarchitectonic map of the cerebral cortex in 1909, dividing the cortex into 52 distinct regions based on cellular composition (Brodmann, 1909). These "Brodmann areas" represent the earliest systematic parcellation scheme and remain foundational in modern neuroscience. The evolution from post-mortem histological analysis to in vivo neuroimaging-based parcellation represents a major methodological shift, enabled by MRI technology in the 1980s-1990s. Modern brain maps leverage high-resolution diffusion-weighted imaging to derive structural connectivity non-invasively, and resting-state fMRI to characterize functional networks, building upon the conceptual foundation established by early cytoarchitectonic maps while dramatically expanding spatial resolution and coverage (Glasser et al., 2016; Yeh et al., 2021).

## Definition and Components

A brain map consists of three primary elements that together define the topology of a [[brain-network]]. First, the **parcellation scheme** partitions the cerebral cortex (and often subcortical structures) into a set of mutually exclusive regions, typically ranging from 68 to 500+ regions depending on the resolution desired (Eickhoff et al., 2018). Second, the **structural connectivity** matrix encodes the strength of white matter pathways between regions, usually derived from diffusion tensor imaging (DTI) or more advanced diffusion models via [[tractography]] (Yeh et al., 2021). Third, the **functional connectivity** matrix captures statistical dependencies between regional time series, commonly extracted from resting-state [[fmri]] or [[meg]] data (Biswal et al., 2010). While structural connectivity reflects anatomical wiring, functional connectivity reflects coherent neural activity and can be mediated by indirect pathways not directly visible in anatomical data.

## Types of Brain Maps

Brain maps can be categorized by their modality of origin and the type of connectivity they represent. **Structural brain maps** derive from diffusion-weighted MRI and provide anatomically grounded connectivity matrices representing white matter fiber tracts. These maps capture the physical pathways through which neural signals propagate, making them essential for models of signal transmission and seizure spread. **Functional brain maps** emerge from statistical analysis of neuroimaging time series, capturing correlations in BOLD signal (for fMRI) or electromagnetic activity (for EEG/MEG) between brain regions. **Effective connectivity** maps, often derived from [[dynamic-causal-modeling]] or Granger causality, attempt to infer directional causal relationships between regions rather than mere correlations (Friston, 2011).

The choice of parcellation scheme significantly impacts whole-brain model behavior. Established cortical parcellations include the [[desikan-killiany-atlas]] (68 regions), [[yeo-atlas]] (7 and 17 network parcellations), and [[glasser-atlas]] (360 regions). The [[aal-atlas]] (Automated Anatomical Labeling) is a widely-used tool that provides comprehensive coverage of both cortical and subcortical structures, offering labels for 116 regions (90 cortical and subcortical, plus 26 cerebellar) (Tzourio-Mazoyer et al., 2002). More recent efforts provide finer-grained subcortical parcellations, such as the Brainnetome atlas, which divides subcortical structures into 246 regions (Fan et al., 2016). Higher-resolution parcellations capture finer-grained network structure but increase computational demands and may introduce noise from imperfect region assignment.

## Relationship to TVB

In The Virtual Brain ([[the-virtual-brain]]), brain maps constitute the mandatory anatomical substrate for all simulations. The TVB workflow accepts brain maps in multiple formats, with the most common being:
- **Connectivity matrices**: CSV or MATLAB files specifying connection weights between all region pairs
- **Surface meshes**: GIFTI or FreeSurfer surfaces defining regional boundaries
- **Region labels**: Text files mapping region indices to anatomical labels

TVB provides built-in support for several standard brain parcellations and integrates with tools like [[connectome-workbench]] for visualizing connectivity data. The [[tvb-library]] implements brain map readers that handle various file formats, performing necessary validation and normalization. Brain maps from the [[hcp-dataset]] and [[uk-biobank]] are frequently used in TVB research due to their high-quality diffusion and functional imaging data.

## Key Features

The quality and utility of a brain map for whole-brain modeling depends on several factors. **Parcellation resolution** determines the granularity of network analysis, with trade-offs between anatomical fidelity and computational tractability. **Connectivity weight normalization** ensures that connection strengths fall within biologically plausible ranges for the chosen [[neural-mass-model]]. **Edge density** refers to the proportion of non-zero connections; sparse brain maps may better reflect the relatively sparse cortical wiring, while dense matrices capture all statistically significant correlations. **Weight distribution** properties, including the presence of strong hub regions and modular structure, critically influence model dynamics such as synchronization patterns and criticality (Bullmore & Sporns, 2009).

## Related Software

Several software tools are specifically designed for constructing and analyzing brain maps. [[brain-connectivity-toolbox]] (BCT) provides MATLAB functions for calculating network metrics. [[bctpy]] offers a Python implementation of these metrics. [[brainsmash]] generates surrogate brain maps for statistical comparison. [[brainstat]] performs statistical inference on brain map data. [[nilearn-datasets]] provides programmatic access to standard brain map datasets.

## Related Concepts

Brain maps are closely related to [[connectome]] representations and [[structural-connectivity]] analysis. They provide the anatomical foundation for [[whole-brain-simulators]] and are essential inputs for [[parameter-estimation]] in personalized brain models. [[Brain-parcellations]] represent the regional division schemes used within brain maps, while [[parcellation]] describes the general methodology of dividing continuous neural data into discrete units.

## References

Biswal, B., Yetkin, F. Z., Haughton, V. M., & Hyde, J. S. (2010). Functional connectivity in the motor cortex of resting human brain using echo-planar MRI. *Magnetic Resonance in Medicine*, 34(4), 537-541.

Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde in ihren Prinzipien dargestellt auf Grund des Zellenbaues*. J.A. Barth.

Bullmore, E., & Sporns, O. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186-198.

Eickhoff, S. B., Yeo, B. T. T., & Genon, S. (2018). Imaging-based parcellations of the human brain. *Nature Reviews Neuroscience*, 19(11), 672-686.

Fan, L., Li, H., Zhuo, J., Zhang, Y., Wang, J., Chen, L., ... & Liu, S. (2016). The Human Brainnetome Atlas: A new brain atlas based on connectional architecture. *Cerebral Cortex*, 26(8), 3508-3526.

Friston, K. J. (2011). Functional and effective connectivity: a review. *Brain Connectivity*, 1(1), 3-36.

Glasser, M. F., Coalson, T. S., Robinson, E. C., Hacker, C. D., Harwell, J., Yacoub, E., ... & Van Essen, D. C. (2016). A multi-modal parcellation of human cerebral cortex. *Nature*, 536(7615), 171-178.

Tzourio-Mazoyer, N., Landeau, B., Papathanassiou, D., Crivello, F., Etard, O., Delcroix, N., ... & Joliot, M. (2002). Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. *NeuroImage*, 15(1), 273-289.

Yeh, C. H., Smith, R. E., Liang, X., Descoteaux, M., & Connelly, A. (2021). Reconstruction of the human connectome using diffusion imaging and tractography. *NeuroImage*, 232, 117987.