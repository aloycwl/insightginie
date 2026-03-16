---
layout: post
title: "SHA-2 vs. SHAKE in SLH-DSA: Choosing the Right Engine for Your Post-Quantum Signatures"
date: 2025-12-18T12:19:36
categories: [10979]
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
------------------------------

To understand why this choice matters, we must reiterate the unique nature of SLH-DSA. In this algorithm, the security of the digital signature is directly reducible to the security of the underlying hash function.

* If the hash function is collision-resistant and preimage-resistant, the signature is secure.
* If the hash function breaks, the signature scheme breaks instantly.

NIST included both SHA-2 and SHAKE to provide **diversity**. If a cryptanalytic breakthrough were to weaken one family (e.g., a new attack on the Merkle-Damgård structure of SHA-2), the industry could pivot to the other (the Sponge construction of SHAKE) without abandoning the SLH-DSA standard entirely.

Contender 1: The SHA-2 Family (SHA-256 / SHA-512)
-------------------------------------------------

**SHA-2** (Secure Hash Algorithm 2) is the veteran of the industry. Designed by the NSA and published in 2001, it is ubiquitous. From TLS certificates to Bitcoin, SHA-2 is the backbone of the current digital economy.

### The Architecture: Merkle-Damgård

SHA-2 utilizes the **Merkle-Damgård** construction. It processes data in fixed-size blocks (512 bits for SHA-256, 1024 bits for SHA-512).

In the context of SLH-DSA, this presents a slight engineering challenge. SLH-DSA requires the ability to process inputs of varying lengths and produce outputs of varying lengths to construct the Hypertree and WOTS+ chains. Because SHA-2 outputs a fixed length (e.g., 32 bytes), implementing it inside SLH-DSA requires additional mechanisms—specifically **HMAC** (Hash-based Message Authentication Code) or **MGF1** (Mask Generation Functions)—to extend the output or randomize the input safely.

### The Hardware Advantage

The primary argument for choosing **SLH-DSA-SHA2** is **Hardware Acceleration**.

Almost all modern processors—from Intel and AMD CPUs in servers to ARM chips in mobile phones—have dedicated instruction sets for SHA-2 (specifically SHA-256).

* **Performance:** On hardware with SHA extensions, SLH-DSA-SHA2 can be incredibly fast. The CPU can process the hashing operations natively, drastically reducing the cycle count for signing and verification.
* **Legacy Support:** Because SHA-2 has been the standard for two decades, virtually every crypto library, hardware security module (HSM), and smart card supports it out of the box.

Contender 2: The SHAKE Family (SHAKE-128 / SHAKE-256)
-----------------------------------------------------

**SHAKE** represents the modern era. It is based on **Keccak**, the winner of the NIST SHA-3 competition. While it is newer, it offers a level of flexibility that older algorithms cannot match.

### The Architecture: The Sponge Construction

SHAKE uses a **Sponge construction**. It “absorbs” data into its state and then “squeezes” it out. Unlike SHA-2, SHAKE is an **XOF (Extendable Output Function)**.

This is a game-changer for SLH-DSA. An XOF allows the developer to request an output of *any* length.

* Need a 32-byte hash for a node? SHAKE can do it.
* Need a 100-byte bitmask? SHAKE can do it without needing complex loops or counter modes.

Because of this, the internal implementation of **SLH-DSA-SHAKE** is cleaner and simpler. It does not require the HMAC wrappers needed for SHA-2. It simply absorbs the input and squeezes the exact number of bytes required for the signature components.

### Software Performance

In pure software implementations (where no dedicated hardware acceleration is available), SHAKE/Keccak is often faster than SHA-2. Its internal permutations are designed to be efficient in software. For generic microcontrollers or older systems lacking SHA extensions, SLH-DSA-SHAKE often wins the race.

The Parameter Sets
------------------

FIPS 205 defines the parameter sets by combining the hash function with the security category.

**For SHA-2:**

* **SLH-DSA-SHA2-128s/f:** Uses SHA-256.
* **SLH-DSA-SHA2-192s/f:** Uses SHA-512 (truncated).
* **SLH-DSA-SHA2-256s/f:** Uses SHA-512.
* *Note: The switch to SHA-512 at higher levels provides a significant speed boost on 64-bit platforms.*

**For SHAKE:**

* **SLH-DSA-SHAKE-128s/f:** Uses SHAKE-128.
* **SLH-DSA-SHAKE-192s/f:** Uses SHAKE-256.
* **SLH-DSA-SHAKE-256s/f:** Uses SHAKE-256.

Choosing the Right Engine: A Decision Matrix
--------------------------------------------

Which one should you implement? The answer depends on your deployment environment.

### Choose SLH-DSA-SHA2 if:

1. **You rely on Hardware Acceleration:** Your servers run modern Intel/AMD/ARM chips with SHA extensions. The performance gain here is undeniable.
2. **You require FIPS 140-2/3 validated modules *now*:** Most existing certified HSMs already have optimized SHA-2 engines.
3. **You prefer the “Tried and True”:** SHA-2 has a longer history of widespread deployment than Keccak.

### Choose SLH-DSA-SHAKE if:

1. **You are running on non-accelerated hardware:** If you are deploying to RISC-V chips or older embedded systems without SHA instructions, SHAKE often performs better in software.
2. **You value code simplicity:** The implementation of SHAKE within the SLH-DSA logic is more elegant and less prone to implementation errors regarding padding and masking.
3. **You want Masking Protection:** The sponge construction of Keccak makes it slightly easier to implement side-channel protections (like masking against power analysis) compared to the HMAC-SHA2 constructions.

Conclusion
----------

Both SHA-2 and SHAKE provide the robust security foundation required for FIPS 205. The “security” difference between them is negligible for practical purposes—both are considered secure against quantum and classical attacks.

The choice, therefore, is one of **optimization**.

If you are building high-throughput server farms to verify signatures, **SLH-DSA-SHA2** is likely your champion due to the ubiquity of hardware instructions. If you are building a clean, modern codebase for diverse IoT devices or prioritizing side-channel resistance, **SLH-DSA-SHAKE** offers the modern flexibility you need.

Ultimately, NIST’s decision to include both ensures that SLH-DSA remains resilient. Whether powered by the veteran Merkle-Damgård or the agile Sponge, the engine of hash-based signatures is ready for the post-quantum road ahead.