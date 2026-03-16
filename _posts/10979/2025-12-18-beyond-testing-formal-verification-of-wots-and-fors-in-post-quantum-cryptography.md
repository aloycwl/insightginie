---
layout: post
title: "Beyond Testing: Formal Verification of WOTS+ and FORS in Post-Quantum Cryptography"
date: 2025-12-18T13:12:55
categories: [10979]
original_url: https://insightginie.com/beyond-testing-formal-verification-of-wots-and-fors-in-post-quantum-cryptography
---

In the domain of high-assurance security, “it works on my machine” is not an acceptable standard. As the world transitions to Post-Quantum Cryptography (PQC), specifically adopting the **SLH-DSA** (FIPS 205) standard, the complexity of cryptographic implementations has skyrocketed.

Unlike RSA, which relies on elegant number theory, SLH-DSA is a complex machine built of moving parts: tweakable hash functions, massive hypertree structures, and intricate indexing logic. The two most critical components—**WOTS+** (Winternitz One-Time Signature Plus) and **FORS** (Forest of Random Subsets)—rely heavily on iterative hash chains.

A single off-by-one error in a loop, a misinterpreted endianness in an index, or a misplaced bitmask can render the entire signature scheme insecure. Standard unit testing might catch obvious bugs, but it cannot prove the absence of vulnerabilities.

This is where **Formal Verification** enters the engineering lifecycle. By treating code as a mathematical theorem, we can prove—with absolute certainty—that the logic of WOTS+ and FORS adheres strictly to the specification.

The Limits of Unit Testing in Hash-Based Cryptography
-----------------------------------------------------

To understand the necessity of formal verification, one must first appreciate the nature of the algorithms involved.

**WOTS+** involves generating chains of hashes. To sign a message, the algorithm iterates a hash function

```
ww
```

 times. To verify, the receiver completes the chain. If the implementation iterates 15 times instead of 16 due to a loop counter error, the verification fails—or worse, it succeeds but creates a security gap.

**FORS** involves mapping a message digest to specific leaves in a forest of Merkle trees. This requires complex bit-shifting and index calculation.

Standard unit testing relies on inputs and outputs. You feed the function a known input and check if the output matches a test vector. However, the state space of SLH-DSA is effectively infinite. You cannot test every possible hash chain combination. Unit tests prove the presence of bugs, not their absence. In a standard intended to protect global infrastructure for the next 50 years, this statistical confidence is insufficient.

What is Formal Verification?
----------------------------

Formal verification differs from testing in that it does not run the code; it analyzes the logic. Using proof assistants (like Coq or EasyCrypt) or verified programming languages (like F\*), engineers define a **Specification** (what the code *should* do) and an **Implementation** (what the code *actually* does).

The verification tool then attempts to mathematically prove that the Implementation is functionally equivalent to the Specification for *all possible inputs*.

If the proof holds, the code is correct. It is not “probably” correct; it is mathematically proven to be bug-free regarding the properties defined in the spec.

Verifying the WOTS+ Logic
-------------------------

The primary challenge in verifying WOTS+ is the **Hash Chain**.

In formal logic, a hash chain is a recursive function. The verification goal is to prove **Termination** and **Functional Correctness**.

1. **Termination:** We must prove that the loop counting the hash iterations will always finish and never enter an infinite state.
2. **Chain Integrity:** We must prove that Hash\_Chain(x, len) equals Hash(Hash\_Chain(x, len-1)).

Formal verification tools allow us to define the “Tweakable Hash Function” as an abstract axiom. We don’t necessarily need to prove that SHA-256 is secure (that is a cryptanalytic problem); we need to prove that the WOTS+ code calls the hash function the correct number of times, with the correct “Tweak” (address coordinates).

By modeling the Address Structure (ADRS) in the formal language, we can prove that every single hash operation in the WOTS+ chain uses a unique coordinate. This mathematically guarantees that **Domain Separation** is enforced, preventing multi-target attacks at the code level.

Verifying the FORS Logic
------------------------

FORS presents a different challenge: **Index Calculation**.

In FORS, the security depends on correctly interpreting parts of the message digest as indices to select tree leaves. A common implementation error in C or Go involves integer overflow or incorrect bit-masking when converting these bytes into array indices.

Formal verification tackles this via **Type Safety** and **Bound Checking**.

* **Dependent Types:** In languages like F\*, we can define a type Index that is mathematically constrained to be an integer between 0 and k-1.
* **Proof of Bounds:** The compiler will refuse to compile the code unless you can prove that the bit-manipulation logic used to derive the index will *always* result in a value within the valid range.

This eliminates an entire class of “buffer overflow” and “out of bounds read” vulnerabilities before the code is ever deployed. Furthermore, formal proofs can verify the **Merkle Tree authentication path**. We can prove that the algorithm correctly computes the root of the FORS tree from the revealed leaves and the authentication path, ensuring the verification logic is sound.

The Role of EasyCrypt and F\*
-----------------------------

Two tools have emerged as champions in the formal verification of PQC standards:

1. **EasyCrypt:** This tool is designed specifically for cryptographic proofs. It allows cryptographers to prove the “game-based security” of the algorithm. For SLH-DSA, EasyCrypt was used to prove that if the underlying hash function is secure, then the WOTS+ and FORS constructions maintain that security (EU-CMA: Existential Unforgeability under Chosen Message Attacks).
2. *F (F-Star):*\* This is a programming language aimed at program verification. The **HACL**\* (High-Assurance Cryptographic Library) project uses F\* to write the code for algorithms like SHA-256 and Ed25519, which then transpiles to C. This generated C code is proven to be memory-safe and functionally correct. Applying this to SLH-DSA implementation ensures the resulting library is free from memory leaks and logic errors.

The Business Case for Formally Verified Crypto
----------------------------------------------

For CTOs and CISOs, “Formal Verification” often sounds like expensive academic overhead. However, in the context of FIPS 205, it is a risk management strategy.

* **Supply Chain Security:** A formally verified library (like those emerging from the HACL\* project or verified implementations in Rust) provides a higher assurance level than a standard OpenSSL implementation.
* **Compliance:** High-security sectors (Defense, Aerospace, Automotive) often require ISO 26262 or DO-178C certification. Formally verified artifacts significantly drastically reduce the cost of achieving these certifications.
* **Future-Proofing:** PQC migration is expensive. Deploying a library that is proven correct avoids the nightmare scenario of patching a fundamental logic bug in the WOTS+ implementation five years from now across millions of IoT devices.

Conclusion
----------

Trusting Post-Quantum Cryptography requires more than trusting the math; we must trust the code that implements the math. WOTS+ and FORS are elegant, robust structures, but they are fragile in the face of implementation errors.

Formal verification bridges the gap between the blackboard and the binary. By subjecting the hash chains of SLH-DSA to rigorous mathematical proofs, we move beyond the uncertainty of testing and establish a foundation of absolute correctness. As we build the security infrastructure of the future, formal verification is not just a luxury—it is a prerequisite for genuine digital trust.