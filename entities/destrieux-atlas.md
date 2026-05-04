---
created: 2026-04-20
updated: 2026-05-04
type: entity
tags: [brain-parcellations, neuroimaging, software-freesurfer, structural-connectivity]
sources: [raw/papers/destrieux-2010.md]
---

The Destrieux Atlas is an anatomical parcellation of the human cerebral cortex developed by Bruno Destrieux and colleagues [1], widely used in neuroimaging research and whole-brain modeling applications. The atlas provides a systematic division of the cortical surface into 148 distinct regions (74 per hemisphere) based on anatomical landmarks, particularly the pattern of cortical sulci, making it one of the most detailed sulcal-based parcellations available.

## Background and Development

The Destrieux Atlas was developed to address the need for a standardized, anatomically-driven parcellation scheme that could reliably segment the cerebral cortex into meaningful regions. Unlike purely geometric atlases that divide the cortex based on simple spatial criteria [2], the Destrieux Atlas leverages the robust and reproducible anatomical landmarks formed by cortical sulci—the grooves that separate the distinct convolutions of the brain. Research has demonstrated that sulcal patterns exhibit high consistency across individuals [3], making them reliable anatomical markers for cortical parcellation. The original paper describing the atlas methodology was published in NeuroImage in 2010 [1], establishing it as a foundational tool in the neuroimaging community.

## Anatomical Framework and Regional Nomenclature

The atlas divides each cerebral hemisphere into regions organized by major cortical lobes: frontal, parietal, temporal, occipital, and limbic (including the cingulate cortex) [1]. Each region is assigned both a name and a numerical identifier, enabling automated labeling in FreeSurfer and other neuroimaging pipelines. The parcellation includes both sulcal-based regions (identified by specific sulcal landmarks) and gyral-based regions (identified by their positions relative to major gyri). This dual approach provides flexibility for different research applications, as some analyses benefit from sulcal boundaries while others require gyral divisions [1]. The regional boundary definitions are stored as annotation files that can be overlaid on individual cortical surfaces, allowing automated labeling of any individual's brain scan.

## Integration with FreeSurfer and Neuroimaging Pipelines

The primary tool for generating Destrieux Atlas parcellations is Freesurfer, an open-source suite for processing and analyzing neuroimaging data, particularly T1-weighted structural MRI scans. During the standard FreeSurfer recon-all processing pipeline, the Destrieux Atlas is applied to segment the cortical ribbon into its constituent regions automatically [4]. The resulting parcellation labels can be used for region-of-interest analyses, connectivity computations, and as input to whole-brain modeling frameworks. This integration has made the Destrieux Atlas a standard option in many neuroimaging preprocessing pipelines, alongside other popular atlases like the [[desikan-killiany-atlas]] (34 regions/hemisphere) [5] and the [[glasser-atlas]] (180 regions/hemisphere) [6].

## Use in Whole-Brain Modeling and Connectomics

In the context of [[whole-brain modeling]], the Destrieux Atlas serves as the parcellation scheme that defines the nodes of the brain network. Each parcellated region becomes a neural mass or node in the [[connectome]] model, with [[structural-connectivity]] derived from diffusion imaging and tractography defining the edges between nodes. The 148-region resolution provides a balance between anatomical detail and computational tractability, making it suitable for large-scale simulations in frameworks like [[the-virtual-brain]]. Researchers can extract time series from functional MRI, EEG, or MEG data using these parcellated regions to study [[functional-connectivity]] patterns and compare them against model predictions [7].

## Comparison with Other Cortical Atlases

The Destrieux Atlas represents one of several anatomical parcellation schemes available to neuroimaging researchers. The [[desikan-killiany-atlas]], developed earlier, provides a simpler 34-region parcellation per hemisphere that is more coarse-grained but easier to interpret [5]. The [[glasser-atlas]], developed more recently using a multimodal approach that combines functional and structural information, offers 180 regions per hemisphere with enhanced functional homogeneity [6]. The [[schaefer-atlas]] provides a resting-state functional connectivity gradient-based parcellation with variants ranging from 100 to 1000 regions [8][9]. Each atlas has specific strengths: Destrieux excels at capturing fine-grained anatomical detail through sulcal boundaries, making it particularly suitable for studies focused on structural [[neuroimaging]] and anatomical variability.

## Technical Considerations and Preprocessing

When using the Destrieux Atlas for [[whole-brain]] analyses, researchers must ensure proper registration between the atlas and their target neuroimaging data. The FreeSurfer pipeline applies several preprocessing steps to ensure accuracy, including skull stripping, intensity normalization, and white matter segmentation [4]. Quality control measures such as those implemented in tools like [[mriqc]] are essential to verify parcellation accuracy, particularly when working with clinical populations or data with motion artifacts [10]. The atlas labels are typically stored in CIFTI or GIFTI format for compatibility with modern neuroimaging file standards and can be visualized using tools like [[connectome-workbench]] or Freesurfer's freeview interface [4].

## Relationship to TVB

The Destrieux Atlas connects to [[the-virtual-brain]] workflows primarily through its role in defining cortical regions for whole-brain simulations. TVB accepts structural parcellations in various formats, and the Destrieux Atlas can serve as the basis for constructing brain network models. The connectivity matrices derived from diffusion imaging using this parcellation feed directly into TVB's neural mass models, enabling researchers to simulate large-scale brain dynamics [7]. While TVB also supports other atlases like AAL and Schaefer, the Destrieux Atlas remains a popular choice for researchers requiring anatomically detailed parcellations. The atlas is also related to other tools in the TVB ecosystem, including [[connectome-workbench]] for visualization and various tractography tools in the diffusion imaging pipeline.

## References

1. Destrieux, C., Fischl, B., Dale, A., & Halgren, E. (2010). Automatic parcellation of human cortical gyri and sulci using standard anatomical nomenclature. NeuroImage, 52(4), 1235-1348. [DOI](https://doi.org/10.1016/j.neuroimage.2010.02.041)

2. Fischl, B. (2012). FreeSurfer. NeuroImage, 62(2), 774-781. [DOI](https://doi.org/10.1016/j.neuroimage.2012.01.021)

3. Ono, M., Kubik, S., & Abernathey, C.D. (1990). Atlas of the Cerebral Sulci. Georg Thieme Verlag.

4. FreeSurfer Documentation. (2024). Cortical Parcellation with Destrieux Atlas. [Documentation](https://surfer.nmr.mgh.harvard.edu/fswiki/DestrieuxAtlas)

5. Desikan, R.S., Ségonne, F., Fischl, B., Quinn, B.T., Dickerson, B.C., Blacker, D., ... & Killiany, R.J. (2006). An automated labeling system for subdividing the human cerebral cortex on MRI into and from a probabilistic atlas. NeuroImage, 31(3):968-980. [DOI](https://doi.org/10.1016/j.neuroimage.2006.01.021)

6. Glasser, M.F., Coalson, T.S., Robinson, E.C., Hacker, C.D., Harwell, J., Yacoub, E., ... & Van Essen, D.C. (2016). A multi-modal parcellation of human cerebral cortex. Nature, 536(7615), 171-178. [DOI](https://doi.org/10.1038/nature18933)

7. Deco, G., & Kringelbach, M.L. (2014). Great expectations: Using whole-brain models to understand the dynamics of brain function. NeuroImage, 80, 360-374. [DOI](https://doi.org/10.1016/j.neuroimage.2013.10.041)

8. Schaefer, A., Kong, R., Gordon, E.M., Laumann, T.O., Zuo, X.N., Holmes, A.J., ... & Yeo, B.T. (2018). Local-Global parcellation of the human cerebral cortex from intrinsic functional connectivity. Cerebral Cortex, 28(9), 3095-3114. [DOI](https://doi.org/10.1093/cercor/bhx035)

9. Yeo, B.T., Krienen, F.M., Sepulcre, J., Sabuncu, M.R., Lashkari, D., Hollinshead, M., ... & Buckner, R.L. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. Journal of Neurophysiology, 106(3), 1125-1165. [DOI](https://doi.org/10.1152/jn.00338.2011)

10. Esteban, O., Birman, D., Schaer, M., Koyejo, O.O., Poldrack, R.A., & Gorgolewski, K.J. (2017). MRIQC: Advancing the automatic prediction of MRI quality. PeerJ, 5, e3348. [DOI](https://doi.org/10.7717/peerj.3348)