---
layout: post
title: "Basename Agent: Onchain Identity + Æmail for AI Explained"
date: 2026-03-11T02:16:53
categories: [24854]
original_url: https://insightginie.com/basename-agent-onchain-identity-aemail-for-ai-explained
---

What is the Basename Agent Skill?
---------------------------------

The Basename Agent skill provides AI agents with a complete onchain identity solution, combining a .base.eth domain name with a dedicated agentic email address at basemail.ai. This skill enables autonomous agents to establish verifiable digital identities without requiring human intervention in the registration process.

The skill is designed specifically for AI agents who need professional identities for communication, reputation building, and onchain interactions. By integrating with the Base blockchain and BaseMail infrastructure, it offers a seamless way for agents to obtain both a memorable domain name and functional email address in a single transaction.

Core Functionality
------------------

The Basename Agent skill performs several key functions:

* Checks availability and price for desired .base.eth domain names
* Facilitates registration of the domain on the Base blockchain
* Creates and configures a corresponding agentic email address
* Handles ERC-8004 registration for agent identity verification
* Manages Attention Bonds for secure message delivery
* Integrates with BaseMail's authentication and email systems

Three Registration Methods
--------------------------

### 1. Donate Buy (Recommended)

The Donate Buy method is the primary and recommended approach for registering a Basename. This method requires the agent to have its own wallet and pay for the registration directly.

Key features of Donate Buy:

* Agent pays for the registration using its own wallet
* 15% donation goes to support the BaseMail infrastructure
* Trustless and atomic on-chain transaction
* No external dependencies required
* Agent receives both the Basename and email address
* ERC-8004 registration and Attention Bonds are automatically configured

The cost structure is transparent and economical. For a typical 0.0001 ETH name, the agent pays 0.000115 ETH total (including the 15% donation), which translates to approximately $0.04 at current rates.

### 2. Auto Register (Free)

The Auto Register method is designed for agents with limited budgets. In this approach, BaseMail's worker pays for the gas and registration fees on behalf of the agent.

Characteristics of Auto Register:

* No cost to the agent
* No donation required
* BaseMail worker covers all expenses
* Agent receives both Basename and email address
* Less trustless than Donate Buy since someone else is paying

While this method is free for the agent, it's worth considering that someone else is funding your identity. The documentation suggests considering Donate Buy for future registrations to support the ecosystem.

### 3. WalletConnect v2 (Advanced)

The WalletConnect v2 method provides the most advanced and self-custodial approach. It allows agents to interact directly with base.org through headless browser integration.

Features of WalletConnect v2:

* Direct interaction with Base blockchain
* Headless browser automation
* Full self-custody of the registration process
* Requires additional dependencies like Puppeteer
* More complex implementation

Technical Implementation
------------------------

### API Integration

The skill integrates with several APIs to provide its functionality:

* BaseMail API for authentication and email services
* DonateBuy contract on Base Mainnet for domain registration
* ERC-8004 contract for agent identity verification
* ENS resolution services for domain management

### Smart Contract Interaction

The core registration happens through the DonateBuy contract at address 0x8b10c4D29C99Eac19Edc59C4fac790518b815DE7 on Base Mainnet. This contract handles the atomic registration of both the Basename and the donation in a single transaction.

The contract uses the L2 Resolver at 0x426fA03fB86E510d0Dd9F70335Cf102a98b10875 to configure the ENS records for the newly registered domain.

Benefits for AI Agents
----------------------

### Professional Identity

Having a .base.eth domain and agentic email address provides AI agents with a professional identity that can be used for:

* Communication with other agents and services
* Reputation building and trust establishment
* Authentication and verification purposes
* Integration with web3 services and protocols

### Sybil Resistance

The Basename Agent system includes features that help prevent Sybil attacks:

* ERC-8004 registration creates verifiable agent identities
* Attention Bonds require USDC-backed messages
* CO-QAF reputation system provides Sybil-resistant trust scores

### Seamless Integration

The skill provides comprehensive integration capabilities:

* REST API endpoints for easy integration
* JavaScript and Python code examples
* Support for both modern and traditional web3 libraries
* Flexible deployment options for different use cases

Security Considerations
-----------------------

The skill implements several security measures:

* SIWE (Sign-In with Ethereum) authentication for secure access
* Proper key management and signing procedures
* Atomic transactions to prevent partial registrations
* Verification of ENS records and ownership

Use Cases
---------

### Autonomous Agent Communication

AI agents can use their Basename and email address to communicate with other agents, services, and humans in a professional manner.

### Service Integration

Services can integrate with agents using their verifiable onchain identities for authentication and authorization.

### Reputation Systems

The onchain identity enables participation in reputation systems and trust networks within the AI agent ecosystem.

Getting Started
---------------

To use the Basename Agent skill, developers can:

1. Choose the appropriate registration method based on their needs
2. Follow the provided code examples for their preferred language
3. Integrate the skill into their agent's workflow
4. Test the functionality with sample names before production use

Conclusion
----------

The Basename Agent skill represents a significant advancement in AI agent infrastructure by providing verifiable onchain identities and functional email addresses. With multiple registration options, comprehensive API integration, and strong security measures, it offers a robust solution for agents seeking professional digital identities in the web3 ecosystem.

Whether you're building autonomous agents for DeFi, social platforms, or enterprise applications, the Basename Agent skill provides the foundational identity infrastructure needed for secure and professional agent interactions.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/daaab/basename-agent/SKILL.md>