---
layout: post
title: "Understanding SatGate CLI: The Server-Side API Access Manager"
date: 2026-03-07T07:17:19
categories: [24854]
original_url: https://insightginie.com/understanding-satgate-cli-the-server-side-api-access-manager
---

What is SatGate CLI?
--------------------

SatGate CLI is a command-line interface tool designed to manage API access, budgets, and monetization for the agent economy. Think of it as the server-side counterpart to client tools like lnget – they’re the wallet, and we’re the register. This tool allows operators to control what agents can access and how much they can spend, providing a comprehensive solution for API access management.

Core Purpose and Architecture
-----------------------------

SatGate CLI serves as the economic firewall for your APIs, enabling you to mint tokens, track spending, revoke agents, and enforce budgets. It’s specifically designed for the server side of agent commerce, handling enforcement, attribution, and governance of API access.

The tool operates in two primary deployment modes:

1. **Self-hosted gateway**: For organizations running their own SatGate instances locally
2. **SatGate Cloud**: For those using the managed cloud service

Installation and Setup
----------------------

Setting up SatGate CLI is straightforward. The tool automatically runs a configuration script if no configuration file exists at ~/.satgate/config.yaml. Alternatively, you can set environment variables to configure your connection:

```
# For self-hosted gateway
export SATGATE_GATEWAY=http://localhost:9090
export SATGATE_ADMIN_TOKEN=sgk_your_token

# For SatGate Cloud
export SATGATE_SURFACE=cloud
export SATGATE_GATEWAY=https://satgate-gateway.fly.dev
export SATGATE_BEARER_TOKEN=sg_your_api_key
export SATGATE_TENANT=your-tenant-slug
```

Always run `satgate status` first to confirm you’re targeting the right gateway before performing any operations.

Safety Rules and Best Practices
-------------------------------

SatGate CLI implements several safety rules to prevent accidental damage:

* Always check the target first with `satgate status` before any operation
* Use `--dry-run` on destructive operations like `revoke` or `mint` with large budgets
* Never use `--yes` without explicit user approval
* Remember that revocation is irreversible – always confirm token name before revoking

Core Commands and Functionality
-------------------------------

### Gateway Health Checks

Before performing any operations, you can check the gateway’s health:

```
satgate status        # Full status (version, surface, uptime)
satgate ping          # Quick liveness check (exit 0/1)
```

### Token Management

Creating tokens for agents is a fundamental operation:

```
# Interactive token creation
satgate mint

# Non-interactive token creation
satgate mint --agent "my-bot" --budget 500 --expiry 30d --routes "/api/openai/*"

# Creating child tokens with delegation
satgate mint --agent "child-bot" --budget 100 --parent "parent-token-id"

# Preview without executing
satgate mint --agent "my-bot" --budget 500 --dry-run
```

### Spending Analysis

Monitoring agent spending is crucial for budget management:

```
satgate spend                    # Org-wide cost center rollups
satgate spend --agent "cs-bot"   # Per-agent breakdown
satgate spend --period 7d        # Time-scoped analysis
```

### Token Inspection

Managing existing tokens requires visibility:

```
satgate tokens        # All tokens with status, spend, budget
satgate token <id>   # Detail: scope, delegation chain, spend
```

### Agent Revocation

When agents need to be removed:

```
satgate revoke <token-id>          # Interactive confirmation
satgate revoke <token-id> --dry-run  # Preview only
```

### Security Monitoring

Keeping track of security threats:

```
satgate report threats  # Blocked requests, anomalies
```

### Policy Management

Checking current policy modes:

```
satgate mode  # Current mode per route (read-only)
```

Common Workflows
----------------

Here are some typical scenarios you might encounter:

1. **New agent needs API access**: `satgate mint --agent "agent-name" --budget 500 --routes "/api/openai/*"`
2. **How much are agents spending?**: `satgate spend`
3. **Agent is misbehaving**: `satgate revoke <token-id>`
4. **Board wants AI spend report**: `satgate spend --json > report.json`
5. **Is the gateway healthy?**: `satgate ping`

Output Formats and Integration
------------------------------

All commands support JSON output for machine-readable integration:

```
satgate tokens --json | jq '.[] | select(.status == "active")'
satgate spend --json > monthly-report.json
```

Pairing with lnget
------------------

SatGate CLI works in conjunction with lnget to create a complete agent commerce stack:

+ **lnget**: Agents pay for L402-gated APIs automatically
+ **SatGate CLI**: Operators mint tokens, set budgets, revoke access, view spend

When an agent using lnget hits your SatGate-protected endpoint, SatGate enforces the budget and attributes the cost, which you can then view in `satgate spend`.

To install lnget, use: `claude plugin marketplace add lightninglabs/lightning-agent-tools`

Real-World Use Cases
--------------------

SatGate CLI enables several practical scenarios:

1. **API Monetization**: Charge agents for API access based on usage
2. **Budget Enforcement**: Prevent runaway costs by setting spending limits
3. **Access Control**: Granular control over which agents can access which endpoints
4. **Compliance**: Track and report on AI agent spending for regulatory purposes
5. **Security**: Quickly revoke access to compromised agents

Advanced Features
-----------------

Beyond basic functionality, SatGate CLI offers advanced capabilities:

+ **Delegation**: Create hierarchical token structures with parent-child relationships
+ **Route-based Policies**: Different policies for different API endpoints
+ **Time-based Expiry**: Automatic token expiration for temporary access
+ **JSON Output**: Programmatic integration with other tools and scripts
+ **Dry-run Mode**: Safe testing of operations before execution

Conclusion
----------

SatGate CLI is an essential tool for organizations managing API access in the agent economy. By providing comprehensive token management, budget enforcement, and spending analytics, it enables secure and controlled API monetization. Whether you’re running a self-hosted gateway or using SatGate Cloud, the CLI provides the command-line power needed to manage your API’s economic firewall effectively.

The combination of SatGate CLI with client-side tools like lnget creates a complete ecosystem for agent commerce, allowing organizations to securely monetize their APIs while providing agents with seamless payment experiences. As the agent economy continues to grow, tools like SatGate CLI will become increasingly important for managing the complex relationships between API providers and AI agents.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/matt-dean-git/satgate/SKILL.md>