# ProcRoute: Process-Scoped Authorization of Split-Tunnel Routes

**arXiv ID**: 2604.16080
**Published**: 2026-04-17
**Updated**: 2026-04-17
**Authors**: Arul Thileeban Sagayam
**Categories**: cs.CR
**URL**: https://arxiv.org/abs/2604.16080
**PDF**: https://arxiv.org/pdf/2604.16080
**Source**: arXiv

## Abstract

In most split-tunnel VPN/ZTNA deployments, installing an internal route authorizes the entire device, not a specific application, to use it. An unprivileged malicious process can therefore reach internal services by reusing routes intended for corporate applications. We present ProcRoute, a system that restricts internal-route access to explicitly authorized applications. ProcRoute models route access as an access-control problem: application identities are principals, destination prefixes with port and protocol constraints are resources, and a total, default-deny decision function mediates every connect() and UDP sendmsg() to an internal destination. Processes without a grant retain external access but are denied internal routes under our threat model. We describe ProcRoute's formal model, a Linux prototype built on cgroup v2 and eBPF socket-address hooks, and two complementary evaluations. In a two-machine WireGuard deployment, ProcRoute matches the WireGuard baseline and 13% faster than an nftables cgroup-matching configuration, with a p50 connect latency of 93 $μ$s (+3.6 $μ$s over baseline), flat policy scaling to 5,000 prefixes, and sub-millisecond revocation. Single-machine loopback microbenchmarks confirm low hook overhead: 2.7 $μ$s on the internal-allow path, 82/82 unauthorized pivot attempts blocked, and zero transient allows across 1.2 million connection attempts during policy reload.
