---
layout: post
title: "The Cryptographic Size Showdown: RSA &amp; ECDSA vs. ML-DSA &amp; SLH-DSA"
date: 2025-12-18T12:13:33
categories: [10979]
original_url: https://insightginie.com/the-cryptographic-size-showdown-rsa-ecdsa-vs-ml-dsa-slh-dsa
---

For decades, the internet has run on a “lightweight” trust model. We have grown accustomed to digital signatures that are barely a blip on the network radar. Elliptic Curve Cryptography (ECDSA), the current gold standard, operates with keys and signatures so small that they are effectively negligible in terms of bandwidth and storage.

However, the transition to Post-Quantum Cryptography (PQC) is about to change the mathematics of overhead.

As organizations prepare to adopt NIST’s newly finalized standards—**ML-DSA** (FIPS 204, formerly Dilithium) and **SLH-DSA** (FIPS 205, formerly SPHINCS+)—they are encountering a rude awakening: quantum resistance comes with a massive weight penalty.

Understanding the disparity in key sizes and signature lengths between the “old world” (RSA/ECDSA) and the “new world” (ML-DSA/SLH-DSA) is essential for engineers planning the migration. This is not just a security upgrade; it is a data engineering challenge.

The Benchmark: The “Old World” Efficiency
-----------------------------------------

To understand the impact of PQC, we must first establish the baseline. Most of the modern internet currently runs on **RSA-2048** or **ECDSA (P-256)**.

### ECDSA (Elliptic Curve Digital Signature Algorithm)

ECDSA is the reigning champion of efficiency.

* **Public Key:** ~64 bytes
* **Signature:** ~64 bytes

This efficiency is why ECDSA is ubiquitous in mobile applications, IoT devices, and TLS handshakes. It fits easily inside a single TCP packet with ample room to spare.

### RSA (Rivest–Shamir–Adleman)

RSA is the older workhorse. While its keys are larger, its signatures are still manageable.

* **Public Key (2048-bit):** ~256 bytes
* **Signature:** ~256 bytes

Even with RSA, the overhead is minimal. A 256-byte signature does not cause fragmentation issues or noticeable latency in handshake protocols.

The New General Purpose: ML-DSA (FIPS 204)
------------------------------------------

**ML-DSA**, based on structured lattices (CRYSTALS-Dilithium), is NIST’s primary recommendation for general-purpose digital signatures. It is intended to be the direct replacement for RSA and ECDSA in most protocols, including TLS.

While it strikes a balance between security and performance, it introduces a significant jump in size.

**At Security Category 3 (ML-DSA-65):**

* **Public Key:** ~1,952 bytes (1.9 KB)
* **Signature:** ~3,293 bytes (3.3 KB)

**The Impact:**  
Compared to ECDSA, an ML-DSA signature is roughly **50 times larger**. While 3.3 KB is manageable for broadband connections, it creates challenges. A typical Ethernet Maximum Transmission Unit (MTU) is 1,500 bytes. This means a single ML-DSA signature will span multiple packets, increasing the probability of packet loss and retransmission delays during a handshake.

The Heavyweight: SLH-DSA (FIPS 205)
-----------------------------------

**SLH-DSA**, based on stateless hash-based cryptography (SPHINCS+), is the conservative backup. It trades performance for the assurance of well-understood hash security.

The size profile of SLH-DSA is unique: it has surprisingly small public keys but undeniably massive signatures.

**At Security Category 1 (SLH-DSA-SHA2-128s):**

* **Public Key:** ~32 bytes
* **Signature:** ~7,856 bytes (7.8 KB)

**At Security Category 5 (SLH-DSA-SHA2-256f):**

* **Public Key:** ~64 bytes
* **Signature:** ~41,000 bytes (41 KB)

**The Impact:**  
The disparity here is shocking. The public key is actually smaller than ECDSA, which is excellent for distribution. However, the signature size ranges from **8 KB to 41 KB**.  
To put this in perspective, a single 41 KB signature is larger than the entire average webpage from the early 2000s. In a protocol exchange, this guarantees significant fragmentation, potentially requiring dozens of packets just to transmit the signature.

Comparative Data Analysis
-------------------------

The following breakdown illustrates the stark differences at a comparable security level (aiming for roughly AES-128 or NIST Level 1 equivalent where applicable):

|  |  |  |  |
| --- | --- | --- | --- |
| Algorithm | Public Key Size | Signature Size | Size Multiplier (vs ECDSA) |
| **ECDSA (P-256)** | 64 bytes | 64 bytes | 1x |
| **RSA-3072** | 384 bytes | 384 bytes | 6x |
| **ML-DSA-44** | 1,312 bytes | 2,420 bytes | ~37x |
| **SLH-DSA-128s** | 32 bytes | 7,856 bytes | ~122x |
| **SLH-DSA-128f** | 32 bytes | 17,088 bytes | ~267x |

*Note: ML-DSA-44 and SLH-DSA-128 are the “Category 1” PQC entries.*

Engineering Implications
------------------------

The migration to PQC is not a simple “find and replace” operation. The size differences impose strictly physical constraints on your infrastructure.

### 1. Network Fragmentation and DoS Risks

Because both ML-DSA and SLH-DSA signatures exceed the standard 1500-byte MTU, fragmentation is inevitable.

* **Latency:** Reassembling fragmented packets takes time, adding latency to TLS establishment.
* **Amplification Attacks:** Large signatures can be exploited for Denial of Service (DoS) attacks. If a server can be tricked into sending a 40 KB signature in response to a small request, the network can be flooded.

### 2. Database Schema Limits

Many legacy systems store digital signatures in database columns defined with strict character limits (e.g., VARCHAR(2048)). Attempting to shove an 8 KB or 40 KB SLH-DSA signature into these fields will result in truncation or application crashes. Database schemas will need to be audited and migrated to BLOB or larger text types.

### 3. Certificate Sizes

X.509 certificates contain both the public key and the signature from the issuing CA.

* In an **ML-DSA** chain, the certificate size balloons because both the key and signature are kilobytes long.
* In an **SLH-DSA** chain, while the public key inside the certificate is small, the signature *on* the certificate is huge.  
  This increases the size of the certificate chain sent during a handshake, further consuming bandwidth.

Conclusion: Choosing the Right Tool
-----------------------------------

The comparative data makes one thing clear: **ECDSA has spoiled us.**

As we move forward, ML-DSA (FIPS 204) is the only viable option for general-purpose web traffic. Its 2.4 KB signature is a bitter pill to swallow compared to ECDSA’s 64 bytes, but it is engineered to be just small enough to work within current protocols.

SLH-DSA (FIPS 205), with its massive signatures, effectively disqualifies itself from high-frequency, low-latency applications like mobile web browsing. However, its small public key size makes it an interesting candidate for scenarios where the key must be distributed widely (like in a firmware root of trust), but the signature is verified only occasionally.

In the post-quantum era, “efficiency” is no longer about minimal bits; it is about minimal disruption. Understanding these size constraints is the first step in ensuring your PQC migration doesn’t grind your network to a halt.