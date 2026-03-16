---
layout: post
title: 'SHA-2 vs. SHAKE in SLH-DSA: Choosing the Right Engine for Your Post-Quantum
  Signatures'
date: 2025-12-18 12:19:36
categories:
- tech
- quantum
original_url: https://insightginie.com/sha-2-vs-shake-in-slh-dsa-choosing-the-right-engine-for-your-post-quantum-signatures
---



When the National Institute of Standards and Technology (NIST) finalized **FIPS 205**, establishing **SLH-DSA** as the standard for stateless hash-based digital signatures, they did not provide a single, monolithic algorithm. Instead, they provided a framework with choices.

Beyond the decisions regarding signature size (Small vs. Fast) and security levels (128, 192, 256), there is a fundamental architectural decision every implementer must make: **The Hash Function.**

FIPS 205 explicitly defines two distinct “flavors” of SLH-DSA based on the core cryptographic engine used:

1. **SLH-DSA-SHA2** (relying on the SHA-2 family)
2. **SLH-DSA-SHAKE** (relying on the SHA-3/Keccak family)

For SLH-DSA, the hash function is not just a utility; it is the entire security model. Unlike RSA or Elliptic Curve cryptography, which rely on number theory, SLH-DSA is built entirely out of hashes. Therefore, the choice between SHA-2 and SHAKE influences performance, hardware compatibility, and implementation complexity.

This article dissects the roles of these two hash families within SLH-DSA to help you select the right engine for your post-quantum infrastructure.

The “Security-Only” Assumption
