---
layout: post
title: "Mastering FORS: The &#8216;Few-Time&#8217; Secret Behind SLH-DSA Message Signing"
date: 2025-12-18T12:17:42
categories: [10979]
original_url: https://insightginie.com/mastering-fors-the-few-time-secret-behind-slh-dsa-message-signing
---

In the architecture of **SLH-DSA** (Stateless Hash-Based Digital Signature Algorithm), defined by NIST in **FIPS 205**, there is a clear division of labor. The heavy lifting of the infrastructure—building the massive Hypertree and linking layers together—is handled by **WOTS+** (Winternitz One-Time Signature Plus). But when it comes time to actually sign the user's message, a different, more specialized tool is deployed.

That tool is **FORS**: The **Forest of Random Subsets**.

While WOTS+ is rigid and strictly “one-time,” FORS is a “few-time” signature scheme (FTS). It represents the evolution of hash-based cryptography from theoretical rigidity to practical flexibility. It serves as the frontline interface between the user's data and the cryptographic superstructure of SLH-DSA.

To understand why SLH-DSA is secure against quantum attacks, we must understand how FORS randomizes the signing process to prevent attackers from learning the signer's secrets.

The Problem with “One-Time” Signing
-----------------------------------

To appreciate the genius of FORS, we must first look at the limitation of WOTS+.

WOTS+ is excellent for signing the root of a Merkle tree because the data being signed (a root hash) is random and unpredictable. However, WOTS+ keys must **never** be reused. If you use a WOTS+ key twice, the security falls apart instantly.

In a stateless environment like SLH-DSA, we index keys based on the message hash. If we used WOTS+ to sign the message directly, and an attacker could find a way to manipulate the index selection or if a collision occurred, the WOTS+ key might be exposed.

We needed a scheme that is more resilient—one that degrades gracefully rather than failing catastrophically if parts of the key are exposed. This is where the concept of the **Few-Time Signature (FTS)** enters the picture.

What is FORS?
-------------

FORS stands for **Forest of Random Subsets**. As the name implies, it does not rely on a single Merkle tree, but rather a collection (a forest) of smaller trees.

It is an improvement on an earlier scheme called **HORST** (Hash to Obtain Random Subset Tree), which was used in the original SPHINCS design. NIST and the submission team refined this into FORS for the finalized SPHINCS+ (and now SLH-DSA) standard.

### The “Few-Time” Property

A “Few-Time” signature means that a key pair can be used to sign a message a handful of times before the security level drops below an acceptable threshold. It relies on the statistical probability that revealing a *subset* of the private key for Message A does not reveal enough information to forge a signature for Message B.

How FORS Works: The Mechanics
-----------------------------

The mechanism of FORS is a game of probability and indices. Here is the step-by-step process of how it secures a message.

### 1. The Structure (The Forest)

A FORS public key is not a single value initially; it is the set of root nodes of

```
kk
```

 distinct Merkle trees.

* Imagine you have `kk` small binary trees.
* Each tree has `tt` leaves.
* Each leaf contains a secret random value (part of the private key).

To create the master FORS public key, the roots of these

```
kk
```

 trees are hashed together.

### 2. Processing the Message

When a user wants to sign a message digest (M), the algorithm treats the digest not as a blob of data, but as a set of instructions—specifically, a set of indices.

The message digest is split into

```
kk
```

 segments. Each segment is interpreted as an integer that points to a specific leaf in one of the trees.

* Segment 1 selects a leaf in Tree 1.
* Segment 2 selects a leaf in Tree 2.
* …and so on, up to Tree `kk`.

### 3. The Reveal (The Signature)

The signature consists of the secret values located at those specific leaves, along with the **authentication path** (the sibling nodes) required to verify them up to the root of their respective trees.

Essentially, the signer says: *“I am not showing you my whole private key. I am only showing you the specific subset of secret values that your message digest pointed to.”*

Why “Random Subsets” Secure the System
--------------------------------------

The security of FORS relies on the difficulty of the **Subset Sum** problem (conceptually) and statistical improbability.

If I sign Message A, I reveal one leaf from each of the

```
kk
```

 trees.  
If I sign Message B, I reveal a *different* set of leaves.

An attacker wants to forge a signature for Message C. To do this, they need to know the secret values for the specific leaves that Message C points to.

If the attacker has seen the signatures for Message A and Message B, they know some of the leaves. However, unless Message C points to the *exact same combination* of leaves that have already been revealed, the attacker cannot forge the signature.

Because the trees have many leaves, and the message digest acts as a randomizer, the probability of an attacker collecting enough revealed leaves to forge a new message is astronomically low.

FORS vs. WOTS+: The Comparison
------------------------------

Understanding the distinction between these two primitives is vital for SLH-DSA implementation.

|  |  |  |
| --- | --- | --- |
| Feature | WOTS+ (Winternitz) | FORS (Forest of Random Subsets) |
| **Primary Role** | Infrastructure. Signs the roots of sub-trees within the Hypertree. | Interface. Signs the actual message digest provided by the user. |
| **Type** | One-Time Signature (OTS). Strict single use. | Few-Time Signature (FTS). Resilient to limited overlap. |
| **Structure** | Hash Chains. | Collection of small Merkle Trees. |
| **Signature Content** | Intermediate hash values from chains. | Secret leaf values + Merkle authentication paths. |

The Integration into SLH-DSA
----------------------------

In the full SLH-DSA protocol, FORS is located at the very bottom of the hierarchy.

1. **The User Message:** The user provides a message.
2. **FORS Signing:** A FORS instance is generated based on the message digest. The message is signed using FORS, producing a FORS public key (the hash of the forest roots).
3. **WOTS+ Linking:** That FORS public key is then signed by a WOTS+ key located at the bottom of the Hypertree.
4. **The Chain:** The signature path continues up the Hypertree to the global public key.

This layered approach ensures that even if the random selection in FORS is slightly imperfect, the overarching Hypertree structure (secured by WOTS+) isolates the instance. The FORS key is ephemeral; it exists essentially to capture that specific message safely.

Conclusion
----------

FORS is the unsung hero of FIPS 205. While the Hypertree provides the infinite scalability required for a stateless signature scheme, FORS provides the necessary agility to handle arbitrary message digests.

By utilizing the “Forest of Random Subsets,” SLH-DSA transforms the rigid constraints of hash-based cryptography into a flexible, secure system. It allows the signer to selectively reveal just enough information to prove authenticity without ever compromising the integrity of the private key. For security architects, understanding FORS is the key to understanding why SLH-DSA is capable of withstanding the quantum computing threats of tomorrow.