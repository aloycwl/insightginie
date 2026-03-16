---
layout: post
title: "Turbocharging SLH-DSA: Optimizing WOTS+ Hash Chains with AVX2 and AVX-512"
date: 2025-12-18T12:25:54
categories: [10979]
original_url: https://insightginie.com/turbocharging-slh-dsa-optimizing-wots-hash-chains-with-avx2-and-avx-512
---

The arrival of FIPS 205 and the standardization of **SLH-DSA** (Stateless Hash-Based Digital Signature Algorithm) has provided the cybersecurity world with a robust safety net against the quantum threat. However, this safety comes with a tangible cost: performance.

Compared to lattice-based alternatives like ML-DSA (Dilithium), SLH-DSA is computationally expensive. The algorithm requires millions of hash operations to generate keys and sign messages. In high-throughput environments—such as TLS termination proxies or certificate authorities—this latency can be a dealbreaker.

The primary bottleneck in SLH-DSA is the **Winternitz One-Time Signature Plus (WOTS+)**. This component requires generating and iterating through thousands of hash chains. Fortunately, modern CPU architectures offer a powerful solution to this specific problem: **SIMD (Single Instruction, Multiple Data)**.

By leveraging vector extensions like **AVX2** and **AVX-512**, developers can parallelize the computation of these hash chains, turning a sluggish sequential process into a high-speed parallel highway. This article explores the engineering strategy behind optimizing WOTS+ using advanced CPU instruction sets.

The WOTS+ Bottleneck: A Game of Thousands of Chains
---------------------------------------------------

To understand why SIMD is necessary, we must look at the workload of a WOTS+ signature.

In the WOTS+ scheme, a signature is not derived from a single mathematical operation (like exponentiation in RSA). Instead, it is derived by taking a secret value and hashing it repeatedly—typically 15 or 16 times—to create a “chain.”

Crucially, a single SLH-DSA signature involves not just one chain, but hundreds of them.

* The **FORS** (Forest of Random Subsets) component uses multiple trees, each containing leaves that are hash chains.
* The **Hypertree** is composed of Merkle trees, where every connection between layers is secured by a WOTS+ instance containing roughly 67 distinct hash chains (for SHA-256 parameter sets).

When a CPU executes this in a standard scalar manner (one operation at a time), it computes Chain A, finishes it, then computes Chain B, and so on. This leaves a massive amount of silicon sitting idle.

The SIMD Approach: Why WOTS+ is the Perfect Candidate
-----------------------------------------------------

**SIMD** allows a processor to perform the same operation on multiple data points simultaneously.

You might think: *“We can’t parallelize a hash chain because step 2 depends on step 1.”* This is correct. You cannot use SIMD to speed up a single chain because of the sequential dependency of the hash output.

**However, you can compute multiple chains at once.**

Because WOTS+ requires the generation of dozens of *independent* chains to form a single signature, it presents an “embarrassingly parallel” workload. Instead of asking the CPU to compute Chain A, then Chain B, then Chain C, and then Chain D, we can use AVX instructions to compute step 1 for Chains A, B, C, and D simultaneously.

Implementing with AVX2 (256-bit Vectorization)
----------------------------------------------

**AVX2** (Advanced Vector Extensions 2) is supported on almost all modern x86\_64 processors (Intel Haswell and later, AMD Ryzen). It features 256-bit wide registers.

### The x4 Strategy

Since a standard SHA-256 state is 256 bits (8 words of 32 bits), mapping it to AVX2 requires a “4-way” implementation (often called x4).

Wait, if the register is 256 bits and the hash state is 256 bits, doesn’t that mean we can only fit one hash?  
Not quite. The internal operations of SHA-256 work on 32-bit words. An AVX2 register can hold **eight 32-bit integers**.

Therefore, we can interleave the data. We take the state variables (

```
a,b,c,…,ha,b,c,…,h
```

) for **8 different hash instances** and load them across the vector registers.

* **Vector Register 1:** Holds variable `aa` for Chains 1 through 8.
* **Vector Register 2:** Holds variable `bb` for Chains 1 through 8.

However, due to the complexity of the message expansion in SHA-256, a **4-way (x4)** implementation is often the sweet spot for AVX2 when managing register pressure and complex rotation logic. This allows the CPU to advance 4 independent WOTS+ chains in the exact same number of clock cycles it would normally take to advance one.

The Heavy Artillery: AVX-512
----------------------------

**AVX-512** doubles the width of the registers to 512 bits. This instruction set is available on Intel Skylake-X, Ice Lake, and newer server-grade Xeon processors, as well as recent AMD EPYC (Genoa) chips.

### The x8 and x16 Strategy

With 512-bit registers, we can drastically scale up the parallelism.

* **SHA-256:** We can comfortably implement an **8-way (x8)** or even **16-way (x16)** parallel hashing engine.
* **SHAKE-256 (Keccak):** Keccak uses 64-bit lanes. AVX-512 allows for highly efficient parallelization of the Keccak permutation, allowing usually 4 or 8 parallel instances depending on the internal lane mapping.

In an AVX-512 implementation of WOTS+, the performance gains are massive. The CPU can process the hash chains for nearly a quarter of a WOTS+ key in a single batch.

### The “Downclocking” Myth

Historically, developers feared AVX-512 because early Intel implementations would drastically downclock the CPU frequency to manage heat, negating the speed benefits. However, on modern processors (Ice Lake, Sapphire Rapids, and AMD Zen 4), this penalty is negligible or non-existent. For cryptographic workloads like SLH-DSA, AVX-512 is now purely a performance win.

The Engineering Challenge: Data Transposition
---------------------------------------------

The difficulty in implementing SIMD for SLH-DSA is not the instruction set itself, but data management.

Standard cryptographic libraries store hash states in **Array of Structures (AoS)** format:  
[Chain1\_State, Chain2\_State, Chain3\_State, …]

SIMD requires **Structure of Arrays (SoA)** format. To process 8 chains at once, you need the first 32 bits of Chain 1 next to the first 32 bits of Chain 2, next to the first 32 bits of Chain 3, etc.

This requires **Transposition**.

1. **Input:** You must gather the inputs for 8 different WOTS+ chains.
2. **Transpose:** You must rearrange the bits so they fit into the vector lanes.
3. **Hash:** Run the AVX rounds.
4. **Transpose Back:** Rearrange the results into standard output formats for the next step of the algorithm.

While transposition adds overhead, the sheer computational cost of the SHA-2 or Keccak rounds is so high that the time saved by parallel execution dwarfs the time lost rearranging the bits.

Real-World Performance Impact
-----------------------------

How much difference does this make?

According to benchmarks from the **Open Quantum Safe (liboqs)** project and optimized implementations in Go (Cloudflare CIRCL) and Rust:

* **Scalar vs. AVX2:** Typically yields a **3x to 3.5x** speedup in key generation and signing.
* **Scalar vs. AVX-512:** Can yield a **5x to 8x** speedup depending on the specific parameter set (SHA2 vs. SHAKE).

Note that this optimization primarily benefits **Key Generation** and **Signing**, where the full WOTS+ public keys must be generated from scratch. **Verification** sees a smaller benefit because the verifier only needs to compute the specific chains revealed in the signature, not the entire tree.

Conclusion
----------

SLH-DSA is often criticized for its speed, but that criticism typically assumes a naive, scalar implementation. When viewed through the lens of vectorization, the algorithm transforms.

Because WOTS+ is composed of many independent, identical tasks, it is the ideal candidate for SIMD optimization. By utilizing AVX2 and AVX-512 to process hash chains in parallel batches, developers can reclaim the CPU cycles lost to post-quantum complexity. As FIPS 205 moves into production, the difference between a sluggish application and a responsive one will likely come down to how well the underlying library exploits these vector instructions.