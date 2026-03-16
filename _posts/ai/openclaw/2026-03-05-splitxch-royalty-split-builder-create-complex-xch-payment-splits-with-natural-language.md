---
layout: post
title: "SplitXCH Royalty Split Builder: Create Complex XCH Payment Splits with Natural Language"
date: 2026-03-05T10:41:23
categories: [24854]
original_url: https://insightginie.com/splitxch-royalty-split-builder-create-complex-xch-payment-splits-with-natural-language
---

What is SplitXCH?
-----------------

SplitXCH is a revolutionary tool that creates special Chia blockchain addresses capable of automatically splitting incoming payments among multiple recipients based on configured percentages. When someone sends XCH to a SplitXCH address, the blockchain automatically distributes the funds to all designated recipients without requiring any manual intervention or third-party escrow services.

How SplitXCH Works
------------------

The system parses plain-language split descriptions into structured data, converts percentages to basis points (with a 1.5% platform fee), and builds hierarchical payment splits that can handle complex scenarios with up to 128+ recipients across multiple levels.

### Natural Language Processing

SplitXCH accepts intuitive descriptions like “Split 60/40 between Alice and Bob” or “Team A (Alice 50%, Bob 50%) gets 70%, Charlie gets 30%” and automatically structures them into valid payment configurations.

### Basis Points Calculation

The system converts percentages to basis points (1 basis point = 0.01%) and scales them to a total of 9,850 points, reserving 150 basis points (1.5%) for the platform fee. This ensures precise distribution even with complex splits.

### Nested Split Architecture

For scenarios requiring more than 128 recipients or hierarchical structures, SplitXCH builds splits from the bottom up. It creates leaf-level splits first, then uses their addresses as recipients in parent splits, with each level incurring its own 1.5% fee.

Key Features
------------

### Automatic Payment Distribution

Once configured, SplitXCH addresses automatically distribute any received XCH according to the predefined percentages, eliminating manual accounting and ensuring transparent, trustless transactions.

### Support for Complex Hierarchies

The system handles nested splits, allowing for sophisticated organizational structures like teams within teams, departments with sub-departments, or multi-tiered royalty arrangements.

### Validation and Security

SplitXCH validates all addresses to ensure they start with “xch1” and are valid bech32m format, prevents duplicate addresses within splits, and ensures all points sum to exactly 9,850.

Common Use Cases
----------------

### Royalty Distribution

Content creators, musicians, and authors can automatically split royalties among collaborators, publishers, and rights holders without complex accounting systems.

### Business Revenue Sharing

Companies can distribute revenue among partners, departments, or regional offices based on pre-agreed percentages, ensuring transparent and automatic profit sharing.

### Team Compensation

Organizations can create compensation structures where teams or individuals receive automatic payments based on their contribution percentages or roles.

### Investment Returns

Investment groups can automatically distribute returns among members based on their investment amounts or ownership percentages.

Benefits
--------

### Transparency

Every SplitXCH transaction is recorded on the blockchain, providing complete transparency and auditability for all participants.

### Automation

Once set up, payments distribute automatically without manual intervention, saving time and reducing administrative overhead.

### Trustless Operation

The smart contract nature of SplitXCH addresses eliminates the need for trusted intermediaries, reducing counterparty risk.

### Cost Efficiency

With only a 1.5% platform fee per split level, SplitXCH offers competitive pricing compared to traditional payment splitting services.

Getting Started
---------------

To use SplitXCH, simply describe your desired payment split in natural language, provide valid XCH addresses for all recipients, and the system will generate your custom split address along with a summary of the distribution structure.

Technical Implementation
------------------------

SplitXCH uses the Chia blockchain's smart contract capabilities to create puzzle addresses that enforce the specified distribution rules. The system handles all the complex calculations and blockchain interactions, making sophisticated payment splitting accessible to non-technical users.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/koba42corp/chia-splitxch/SKILL.md>