---
created: 2026-04-27
sources:
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/semanticscholar-d6e43299345d.md
- raw/papers/sanz-leon-2013.md
tags:
- software-brain-modeling
- software-neuroimaging
- data-format
title: Pynrrd
type: entity
updated: '2026-04-28'
---

# Pynrrd

## Overview

Pynrrd is a pure-Python library for reading and writing NRRD (Nearly Raw Raster Data) files into and from numpy arrays. The NRRD format itself is a flexible container for storing n-dimensional raster data, originally developed as part of the Teem toolkit at the University of Utah. While NRRD is commonly used for diffusion-weighted MRI data, segmentation masks, and other volumetric imaging datasets, it is fundamentally a general-purpose scientific array format—not DTI-specific. The pynrrd library provides a thin Python interface to this format, handling the mechanics of reading and writing without performing any visualization or data processing.

The library provides a simple, intuitive API that abstracts away the complexities of the NRRD file format specification while maintaining full compliance with the format version 5 (NRRD0005). The pynrrd project was initiated in 2010 and has since grown to become a fundamental utility in the [[neuroimaging]] ecosystem, with approximately 125 GitHub stars and active development continuing as of 2025.

## Relationship to Whole-Brain Modeling and TVB

It is important to distinguish between the NRRD format and the pynrrd library when considering relationships to [[whole-brain modeling]] and [[the-virtual-brain]]. The NRRD format's widespread use in [[diffusion-imaging]] and [[tractography]] pipelines makes it relevant to [[connectome]]-based modeling, but pynrrd itself is merely a thin I/O wrapper—it is the NRRD *data format* (not the Python library) that connects to the broader neuroimaging ecosystem.

Tractography outputs—such as fiber orientation distributions, streamline counts, and probabilistic pathway maps—are frequently stored in NRRD format, given the format's native support for arbitrary-dimensional data and its ability to encode gradient directions and measurement frames essential for [[diffusion-mri]] interpretation. Researchers using [[the-virtual-brain]] to simulate brain dynamics based on [[structural-connectivity]] derived from diffusion data may encounter NRRD-format tractography results. The pynrrd library can read these files, but it is the NRRD *format* (and the data it contains) that relates to whole-brain modeling, not the library itself.

Similarly, when working with [[brain-parcellations]] and region-based connectivity matrices, researchers may encounter NRRD-format label maps or segmentation volumes. Pynrrd enables conversion between NRRD volumes and numpy arrays, which can then be processed using libraries like [[nibabel]] or [[nilearn]] for further analysis—but this is a data conversion capability, not a modeling capability.

## Key Features

The pynrrd library offers several distinctive capabilities that make it well-suited for neuroimaging workflows:

**Reading and Writing NRRD Files**: The core functionality revolves around two primary functions—`nrrd.read()` and `nrrd.write()`—which handle bidirectional conversion between NRRD files and numpy arrays. The `read()` function returns a tuple containing the data array and a dictionary of header fields, while `write()` accepts a numpy array and optionally a custom header dictionary.

**Header Parsing and Formatting**: Pynrrd provides comprehensive support for the full range of NRRD header fields, including dimensional information (`dimension`, `sizes`), spatial metadata (`space`, `space directions`, `space origin`, `space units`), axis properties (`kinds`, `labels`, `units`, `spacings`, `thicknesses`), and encoding specifications (`type`, `endian`, `encoding`). The library includes dedicated functions for parsing and formatting both standard fields and custom key-value pairs.

**Index Order Handling**: A critical feature for neuroimaging applications is the `index_order` parameter, which controls whether data is interpreted in C-order (row-major) or Fortran-order (column-major). Given that medical images are typically stored with the fastest-varying axis corresponding to x-coordinates, proper handling of index order is essential for maintaining correct spatial orientation when reading volumetric data.

**Custom Field Support**: The library allows users to define custom field type mappings via the `custom_field_map` parameter, enabling extension of the NRRD format with application-specific metadata. This is particularly relevant for DWI data, where conventions like those established by NAMIC use custom key-value pairs to encode diffusion gradient directions and b-values.

**Detached Header Support**: NRRD files can have either attached headers (header and data in the same file) or detached headers (separate header and data files). Pynrrd handles both configurations transparently, supporting patterns like `data file: S4.%03d` for referencing multiple data files.

**Encoding Options**: The library supports various encoding schemes including raw binary, ASCII text, gzip compression, and bzip2 compression. This flexibility allows researchers to balance storage efficiency against computational overhead when working with large neuroimaging datasets.

## Technical Implementation

The NRRD format's design philosophy emphasizes self-containment and explicit representation of spatial metadata. For diffusion-tensor imaging applications, the format's header fields encode crucial information about the relationship between image coordinates (IJK), scanner coordinates (XYZ), and anatomical coordinate systems (RAS/LPS). This explicit encoding addresses common challenges in DWI processing, including the ambiguity between gradient coordinate frames and image space coordinate frames that frequently complicates analysis of legacy datasets.

The format distinguishes between "domain" axes (along which resampling or blurring makes physical sense) and "range" axes (which represent components of vector or tensor quantities). For instance, a 4D DWI volume would typically have three spatial domain axes and one "list" or "vector" range axis containing the diffusion-weighted measurements. This semantic distinction is preserved in pynrrd's header representation and informs how data is interpreted during reading.

## Comparison with Related Formats

While NRRD is widely used in the ITK/3D Slicer ecosystem, other formats dominate different segments of the neuroimaging landscape. The [[nifti]] format (accessed via [[nibabel]]) is more common for general-purpose fMRI and structural MRI data, offering tight integration with the broader neuroimaging analysis ecosystem including [[fsl]], [[spm]], and [[afni]]. The NIFTI format benefits from a more compact header structure and native support for temporal data, making it preferred for time-series analysis.

For diffusion-specific processing, [[dipy]] provides a higher-level interface to diffusion imaging data that can consume NRRD files through nibabel's IO utilities. However, NRRD's explicit representation of measurement frames and gradient directions remains advantageous when precise knowledge of coordinate transformations is required.

## Integration with Neuroimaging Software

Pynrrd interoperability extends across several major neuroimaging platforms:

- **[[3d-slicer]]**: As the software that popularized NRRD for DWI applications, 3D Slicer can directly read and write NRRD files, enabling workflows that combine Slicer's tractography capabilities with TVB's [[whole-brain]] simulation through pynrrd-mediated data conversion.

- **[[ants]]** (Advanced Normalization Tools): The ANTs suite uses NRRD as an internal representation for many operations, making pynrrd useful for preprocessing pipelines that combine ANTs with custom Python analysis code.

- **[[dipy]]**: While dipy primarily uses NIfTI internally, its tractography outputs can be saved in NRRD format, enabling integration with tools expecting that format.

- **nitk** (when available): ITK's NrrdImageIO class provides C++ NRRD support that mirrors pynrrd's functionality at a lower level, useful for performance-critical preprocessing stages.

## Usage Example

```python
import numpy as np
import nrrd

# Write a sample diffusion volume
data = np.zeros((256, 256, 36, 14))  # 4D DWI volume
header = {
    'kinds': ['space', 'space', 'space', 'list'],
    'space': 'right-anterior-superior',
    'space directions': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [None, None, None]]),
    'spacings': [1.0, 1.0, 2.5, np.nan],
    'units': ['mm', 'mm', 'mm', '']
}
nrrd.write('dwi_volume.nrrd', data, header)

# Read the volume back
read_data, header = nrrd.read('dwi_volume.nrrd')
print(read_data.shape)  # (256, 256, 36, 14)
```

This minimal example demonstrates how pynrrd handles the complete round-trip conversion of volumetric imaging data while preserving critical spatial metadata.

## Related Software

- [[nibabel]] — Python library for neuroimaging file formats (primarily NIfTI)
- [[dipy]] — Diffusion imaging processing and tractography
- [[3d-slicer]] — Medical image computing platform with native NRRD support
- [[ants]] — Advanced Normalization Tools for neuroimaging
- [[mrtrix3]] — MRtrix3 for advanced tractography
- [[nilearn]] — Neuroimaging data visualization and manipulation
