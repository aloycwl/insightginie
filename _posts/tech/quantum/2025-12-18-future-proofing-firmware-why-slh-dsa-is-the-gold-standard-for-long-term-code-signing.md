---
layout: post
title: "Future-Proofing Firmware: Why SLH-DSA is the Gold Standard for Long-Term Code Signing"
date: 2025-12-18T13:14:13
categories: [10979]
original_url: https://insightginie.com/future-proofing-firmware-why-slh-dsa-is-the-gold-standard-for-long-term-code-signing
---

In the frantic race to adopt Post-Quantum Cryptography (PQC), speed often dominates the conversation. When securing web traffic, API calls, or ephemeral messaging, milliseconds matter. This need for speed has propelled lattice-based algorithms, specifically ML-DSA (FIPS 204/Dilithium), to the forefront of the NIST standardization process.

However, not all digital interactions are created equal. There is a critical subset of cybersecurity where speed is irrelevant, and longevity is everything: **Firmware and Code Signing**.

For devices with lifecycles measured in decades—such as automobiles, industrial control systems (ICS), satellites, and smart meters—the cryptographic priorities are inverted. Here, the conservative, battle-tested nature of **SLH-DSA** (FIPS 205) makes it the superior choice. Despite its performance overhead, SLH-DSA is emerging as the “Gold Standard” for securing the roots of trust in long-lived infrastructure.

The “Long-Lived” Dilemma
------------------------

To understand why SLH-DSA wins in this arena, one must first appreciate the unique challenges of embedded security.

When a manufacturer releases a smartphone, they expect to push updates frequently, and the device is likely to be replaced within three to four years. If a cryptographic vulnerability is discovered, it can be patched quickly, or the hardware will naturally cycle out of circulation.

Contrast this with an automotive Electronic Control Unit (ECU) or a satellite in geostationary orbit. These devices are deployed with the expectation that they will operate securely for 15, 20, or even 30 years.

1. **Updates are Infrequent:** Firmware updates might happen once a year, or perhaps only once in the device's lifetime.
2. **Hardware is Static:** The root public keys burned into the silicon (ROM or eFuses) cannot be changed physically.
3. **Risk is Cumulative:** The longer a device exists in the field, the higher the probability that a mathematical breakthrough could weaken the cryptography protecting it.

In this environment, “Performance” is secondary to “Assurance.”

The Conservative Security Argument: Hash vs. Lattice
----------------------------------------------------

NIST standardized two primary signature schemes:

1. **ML-DSA (Lattice-based):** Efficient, small signatures, but based on complex mathematical lattice structures.
2. **SLH-DSA (Hash-based):** Slower, larger signatures, but based purely on hash functions.

For a long-term root of trust, **SLH-DSA is the insurance policy.**

Lattice-based cryptography, while rigorously studied, is relatively new compared to RSA or ECC. There remains a non-zero statistical probability that a cryptanalytic breakthrough—classical or quantum—could find a weakness in the underlying lattice structures in the next 20 years. If you burn an ML-DSA key into the silicon of a fleet of smart meters today, and a lattice vulnerability is found in 2030, that entire fleet becomes a liability.

SLH-DSA, on the other hand, relies on the most well-understood concept in cryptography: the hash function (SHA-2 or SHAKE). We have analyzed hash functions for decades. As long as the hash function remains collision-resistant, SLH-DSA remains secure. It involves no complex “hidden” math. For a device that must remain secure until 2050, betting on the stability of SHA-256 is the safest wager an engineer can make.

Re-evaluating the Performance Trade-offs
----------------------------------------

Critics of SLH-DSA point to its performance metrics as a disqualifier. It is true that SLH-DSA signatures are large (ranging from 8KB to 41KB) and verification is slower than ML-DSA.

However, in the context of firmware signing, these downsides are negligible.

### 1. Bandwidth is Relative

A 41KB signature is massive for a 200-byte text message. It is a rounding error for a 500MB firmware image. When a Tesla downloads a gigabyte over-the-air (OTA) update, the bandwidth cost of a 41KB signature is imperceptible. The overhead does not impact the user experience or the network cost significantly.

### 2. Latency is Irrelevant

If a smart meter takes 200 milliseconds to verify a signature instead of 5 milliseconds, does it matter? No. Firmware updates happen in the background, often while the device is in a maintenance state. The user is not waiting for a page to load. The “fast” verification of ML-DSA solves a problem that firmware updates do not have.

The Silicon Advantage: Small Public Keys
----------------------------------------

While SLH-DSA signatures are large, its **Public Keys** are incredibly small.

* **SLH-DSA-SHA2-128s Public Key:** ~32 bytes.
* **ML-DSA-44 Public Key:** ~1,312 bytes.

This is a massive advantage for hardware engineers. The “Root of Trust” in a device usually lives in a limited amount of One-Time Programmable (OTP) memory, eFuses, or Mask ROM inside the microcontroller.

Embedding 1,312 bytes (ML-DSA) into the eFuses of a cost-constrained IoT chip is expensive and takes up valuable silicon real estate. Embedding 32 bytes (SLH-DSA) is trivial. It allows manufacturers to maintain the same hardware manufacturing processes used for SHA-256 hashes or ECDSA keys, significantly lowering the barrier to adoption for secure boot implementations.

Avoiding the State Management Trap
----------------------------------

It is worth noting that SLH-DSA is **Stateless**. Previous iterations of hash-based signatures (like XMSS and LMS) were “Stateful,” requiring the signer to track exactly how many times a key had been used. If the state was lost (e.g., a backup was restored), the security system collapsed.

For code signing—which often happens in distributed build environments, cloud CI/CD pipelines, and across redundant servers—state management is a nightmare. SLH-DSA eliminates this risk. A developer can sign a firmware release from any authorized server without worrying about synchronizing counters or breaking the key. It provides the security of hash-based logic with the usability of standard RSA/ECDSA.

Conclusion
----------

Cryptographic agility is a luxury that embedded hardware does not possess. Once a device leaves the factory, its root of trust is often set in stone.

For high-frequency, ephemeral transactions, ML-DSA is the correct tool. But for the heavy lifting of securing the software supply chain—verifying the firmware that controls brakes, power grids, and medical devices—conservatism is a virtue.

SLH-DSA offers a trade-off that is perfectly tuned for this use case: it sacrifices signature size (which we have in abundance) to buy long-term mathematical certainty (which is scarce). By choosing FIPS 205 for code signing, organizations are not just complying with standards; they are ensuring that the devices they build today will remain trustworthy in the post-quantum world of tomorrow.