# Accurate Models of NVIDIA Tensor Cores

**Source**: semantic-scholar
**ID**: 4471f6630fb52087b5018ba49082a303d771cb43
**DOI**: 10.48550/arXiv.2512.07004
**URL**: https://www.semanticscholar.org/paper/4471f6630fb52087b5018ba49082a303d771cb43
**Date**: 2025-12-07
**Year**: 2025
**Authors**: Faizan A. Khattak, M. Mikaitis
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Matrix multiplication is a fundamental operation in both training of neural networks and inference. To accelerate matrix multiplication, Graphical Processing Units (GPUs) provide it implemented in hardware. Due to the increased throughput over the software-based matrix multiplication, the multipliers are increasingly used outside of AI, to accelerate various applications in scientific computing. However, matrix multipliers targeted at AI are at present not compliant with IEEE 754 floating-point arithmetic behaviour, with different vendors offering different numerical features. This leads to non-reproducible results across different generations of GPU architectures, at the matrix multiply-accumulate instruction level. To study numerical characteristics of matrix multipliers -- such as rounding behaviour, accumulator width, normalization points, extra carry bits, and others -- test vectors are typically constructed. Yet, these vectors may or may not distinguish between different hardware models, and due to limited hardware availability, their reliability across many different platforms remains largely untested. We present software models for emulating the inner product behaviour of low- and mixed-precision matrix multipliers in the V100, A100, H100 and B200 data center GPUs in most supported input formats of interest to mixed-precision algorithm developers: 8-, 16-, and 19-bit floating point.
