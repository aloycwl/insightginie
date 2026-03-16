---
layout: post
title: "SLH-DSA vs. XMSS and LMS: The Battle of Stateless vs. Stateful Hash-Based Signatures"
date: 2025-12-18T12:10:43
categories: [10979]
original_url: https://insightginie.com/slh-dsa-vs-xmss-and-lms-the-battle-of-stateless-vs-stateful-hash-based-signatures
---

In the race to secure the internet against the impending threat of quantum computing, hash-based cryptography has emerged as the most conservative and mathematically sound “insurance policy.” Unlike lattice-based algorithms, which rely on relatively newer mathematical assumptions, hash-based signatures depend only on the security of cryptographic hash functions—a concept we have understood and tested for decades.

However, not all hash-based signatures are created equal. The National Institute of Standards and Technology (NIST) has standardized two distinct categories: **Stateful** (XMSS and LMS) and **Stateless** (SLH-DSA).

For Chief Information Security Officers (CISOs) and developers, distinguishing between these two is not just a matter of semantics; it is a critical architectural decision. Choosing the wrong one could either cripple your application’s performance or introduce a catastrophic security vulnerability known as “state exhaustion.”

This article dissects the technical mechanics, risks, and ideal use cases for SLH-DSA compared to its stateful predecessors, XMSS and LMS.

The Foundation: Merkle Trees and One-Time Signatures
----------------------------------------------------

To understand the difference between stateful and stateless, one must understand the foundation they share. Both approaches utilize Merkle Trees and One-Time Signature (OTS) schemes (like Winternitz OTS).

In these schemes, a private key can effectively sign a message only once. If a private key is used to sign two different messages, an attacker can analyze the signatures to forge new ones, completely breaking the system. To solve this, we use a tree structure where many one-time keys are generated, and a “Master” public key allows you to verify them all.

The divergence occurs in how the system ensures a one-time key is never reused.

The Stateful Contenders: XMSS and LMS
-------------------------------------

**XMSS (eXtended Merkle Signature Scheme)** and **LMS (Leighton-Micali Signature)** were the first to arrive on the scene. NIST addressed these in Special Publication 800-208.

### How They Work

These algorithms are “stateful” because the signer must maintain a dynamic record—or state—of exactly which one-time keys have been used. Think of it like a checkbook with numbered checks. You must remember that you have already written check #101 so that you don’t try to write check #101 again for a different transaction.

The system relies on an index (a counter) that increments with every signature.

### The Performance Advantage

The primary benefit of XMSS and LMS is efficiency. Because the path through the Merkle tree is deterministic and pre-calculated, the resulting signatures are relatively small (approx. 2-3 KB) and the verification process is incredibly fast.

### The “Foot-Gun” Risk

The fatal flaw of stateful signatures is their fragility in modern computing environments. If the state is ever mishandled, the security model collapses.

* **Backups:** If you back up a server acting as a signer, restore it a week later, and the server reuses an index that was consumed after the backup was taken, the key is compromised.
* **Cloning:** If a virtual machine (VM) holding the key is cloned to scale up an application, both VMs might try to sign using the same index.
* **Multi-threading:** Complex locking mechanisms are required to ensure two threads don’t grab the same index simultaneously.

Because of these risks, NIST SP 800-208 strictly limits the use of XMSS and LMS to environments where state management can be strictly controlled, such as hardware security modules (HSMs) or smart cards.

The Stateless Evolution: SLH-DSA (FIPS 205)
-------------------------------------------

**SLH-DSA** (Stateless Hash-Based Digital Signature Algorithm), derived from the SPHINCS+ submission, is defined in the newly released FIPS 205. It was designed specifically to eliminate the state management dangers of XMSS and LMS.

### How It Works

SLH-DSA achieves “statelessness” by using a massive Hypertree structure—a tree of trees. Instead of remembering an index, the algorithm randomly selects a leaf in the tree to generate a signature.

Because the total number of keys in the Hypertree is astronomically large (e.g.,

```
264264
```

), the statistical probability of randomly selecting the same key twice is negligible—so low that it is considered impossible in practice. This allows the signer to be purely a function of the message and the private key, with no memory of past actions required.

### The Trade-Off: Size and Speed

Security always comes at a cost. To ensure that collision probability remains zero, the SLH-DSA structure must be immense.

* **Signature Size:** SLH-DSA signatures are significantly larger than XMSS or LMS, ranging from 8 KB to 41 KB depending on the parameter set.
* **Performance:** The signing process is computationally heavier because it involves generating parts of the tree on the fly.

Critical Comparison: Head-to-Head
---------------------------------

### 1. Implementation Safety

* **XMSS/LMS:** Extremely dangerous in general-purpose computing. Requires strict state management. A single restore-from-backup can destroy the root of trust.
* **SLH-DSA:** “Plug and play” safety. It behaves like traditional signatures (RSA/ECDSA). You can clone keys, restore backups, and run in distributed environments without fear of key compromise.

### 2. Signature Size and Bandwidth

* **XMSS/LMS:** Efficient. Suitable for constrained bandwidth environments.
* **SLH-DSA:** Heavy. A 41 KB signature can cause packet fragmentation in networking protocols or exceed limits in certain database fields.

### 3. Verification Speed

* **XMSS/LMS:** Very fast verification, making them suitable for secure boot processes where startup time is critical.
* **SLH-DSA:** Slower verification, though still generally acceptable for most application layers.

Ideal Use Cases
---------------

Understanding the distinction leads to very clear implementation paths for organizations adopting Post-Quantum Cryptography.

### When to use XMSS / LMS:

These should be reserved for **niche, high-control environments** where signature size is the bottleneck and state can be guaranteed.

* **Firmware Signing:** The vendor signs the firmware in a secure clean room (strictly controlling the state) and the device (IoT, satellite, car ECU) verifies it. The device benefits from the small signature and fast verification.
* **Smart Cards:** Where the key never leaves the physical silicon, and the counter is managed by the hardware itself.

### When to use SLH-DSA:

This is the **general-purpose** standard for the internet.

* **Software Supply Chain:** Signing software releases distributed across mirrors.
* **TLS and PKI:** Acting as a root CA or intermediate CA where the key must exist on servers that might be clustered or backed up.
* **Document Signing:** Legal contracts and email signatures where the signer is a user on a laptop or cloud service.

Conclusion
----------

NIST has provided two tools for two different jobs. XMSS and LMS are precision scalpels—sharp, efficient, but dangerous if mishandled. SLH-DSA is the hammer—heavier and blunter, but reliable and safe for general construction.

For 95% of organizations and use cases, **SLH-DSA (FIPS 205)** is the correct choice. The operational risk of managing state in a cloud-native, virtualized world far outweighs the bandwidth savings offered by stateful schemes. While the signature sizes of SLH-DSA present engineering challenges, they provide the peace of mind that your quantum-resistant migration won’t fail due to a simple server backup error.