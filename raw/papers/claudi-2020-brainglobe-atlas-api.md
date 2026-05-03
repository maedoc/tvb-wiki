---
bibliotype: article
created: '2024-12-01'
date: 2020
firstname: Federico
journal: Journal of Open Source Software
lastname: Claudi
pages: ''
papertitle: 'BrainGlobe Atlas API: a common interface for neuroanatomical atlases'
source: doi.org/10.21105/joss.02668
tags:
- atlas
- neuroanatomy
- python
- visualization
title: 'Claudi et al. (2020) BrainGlobe Atlas API'
volume: '5'
year: '2020'
---

# BrainGlobe Atlas API: a common interface for neuroanatomical atlases

## Abstract

Many excellent brain atlases exist for different species. Some of them have an API (application programming interface) to allow users to interact with the data programmatically (e.g. the excellent Allen Mouse Brain Atlas), but many do not, and there is no consistent way to process data from multiple sources. The BrainGlobe Atlas API deals with this problem by providing a common interface for programmers to download and process data from multiple sources.

## Introduction

Brain atlases are essential tools for neuroscience research, providing standardized anatomical frameworks for interpreting experimental data. However, the diversity of atlas formats, coordinate systems, and access methods creates significant barriers to reproducible analysis. Researchers often need to write custom code to work with each atlas, making it difficult to compare results across studies or integrate data from different sources.

The BrainGlobe Atlas API addresses these challenges by providing a unified Python interface for accessing neuroanatomical atlases. The API defines a common data format that all atlases conform to, enabling researchers to work with multiple atlases using a consistent set of commands.

## Atlas Format

Each BrainGlobe atlas consists of data files in a common format:
- A "reference" image of a brain (`.tiff`)
- An "annotation" image, with each brain region defined by a unique pixel value (`.tiff`)
- Meshes defining the surface of each brain region (`.obj`)
- A mapping of brain region pixel value to region name, and structure hierarchy (`.json`)
- Metadata defining the shape, orientation etc. of the data, and other info such as animal species and authors (`.json`)

## Available Atlases

A number of atlases are available through the API, including:
- Allen Mouse Brain Atlas (10, 25, 50, and 100 micron resolutions)
- Allen Human Brain Atlas (500 micron)
- Max Planck Zebrafish Brain Atlas (1 micron)
- Enhanced and Unified Mouse Brain Atlas
- Waxholm Space atlas of the Sprague Dawley rat brain
- And many more...

## Citation

If you find the BrainGlobe Atlas API useful, please cite the paper in your work:

Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W. and Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. Journal of Open Source Software, 5(54), 2668, https://doi.org/10.21105/joss.02668