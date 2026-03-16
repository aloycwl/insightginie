---
layout: post
title: "OpenServ Agent SDK: Complete Guide to Building Autonomous AI Agents for the OpenServ Platform"
date: 2026-03-05T15:40:26
categories: [24854]
original_url: https://insightginie.com/openserv-agent-sdk-complete-guide-to-building-autonomous-ai-agents-for-the-openserv-platform
---

OpenServ Agent SDK: Complete Guide to Building Autonomous AI Agents for the OpenServ Platform
=============================================================================================

In the rapidly evolving world of artificial intelligence, developers need tools that simplify the creation, deployment, and management of autonomous agents. The **OpenServ Agent SDK** (available as `@openserv-labs/sdk`) does exactly that. It provides a TypeScript‑first framework for building custom AI agents that run on the OpenServ platform, interact with other agents, and can be triggered by a variety of payment‑based or webhook mechanisms.

What Does the OpenServ Agent SDK Skill Do?
------------------------------------------

The OpenServ Agent SDK skill is a *developer‑oriented package* that abstracts away the low‑level plumbing required to turn a piece of code into a fully fledged, on‑chain‑compatible AI service. In plain language, it lets you:

* **Define an agent** with a system prompt and a set of capabilities (functions the agent can execute).
* **Register the agent** on the OpenServ network using a wallet‑based identity, automatically handling API keys and authentication tokens.
* **Run the agent** so it can listen for incoming tasks, execute capabilities, and return results to the platform.
* **Integrate with multi‑agent workflows** and ERC‑8004 on‑chain identity, enabling complex, composable AI pipelines.

All of this is achieved without the need to manage your own LLM API keys when you use *runless capabilities* or the built‑in `generate()` method. The platform handles the actual language‑model call, records usage, and bills the appropriate workspace.

How the SDK Works – Step‑by‑Step Flow
-------------------------------------

The SDK follows a clear, four‑stage workflow that mirrors the lifecycle of a typical AI service:

1. **Define Your Agent**
   * Provide a *system prompt* that sets the agent’s personality, goals, and constraints.
   * Add *capabilities* – either *runless* (no code, platform‑handled LLM call) or *runnable* (custom JavaScript/TypeScript logic).
2. **Register with the Platform**
   * Call `provision()` from `@openserv-labs/client`. This creates or re‑uses a blockchain wallet, registers the agent, and writes `OPENSERV_API_KEY` and `OPENSERV_AUTH_TOKEN` to `.env` (or you can bind them directly via `agent.instance`).
   * During development you can skip a custom endpoint URL; the SDK automatically opens a secure tunnel to the platform.
3. **Start the Agent**
   * Execute `run(agent)`. The agent opens a WebSocket (or HTTP) listener, receives tasks, runs the appropriate capability, and streams the response back.
   * Inside runnable capabilities you have access to `this.generate()`, `this.addLogToTask()`, `this.uploadFile()`, and other helper methods.
4. **Interact with the Platform**
   * Use the `agent` object to create or update tasks, manage files, and query workspace metadata.
   * Combine multiple agents in a workflow using the `openserv-client` skill, which offers the full Platform API for orchestrating complex pipelines.

Capability Types – Runless vs. Runnable
---------------------------------------

Capabilities are the core building blocks of an agent. They tell the platform \*what\* the agent can do and \*how\* it does it.

### Runless Capabilities (Recommended for Most Scenarios)

Runless capabilities are essentially declarative. You only provide a `name`, `description`, and optionally `inputSchema` and `outputSchema`. The OpenServ platform automatically performs the LLM call, validates the schema, and returns the result. Benefits include:

* No need to store or manage an LLM API key.
* Reduced code complexity – you write no `run()` function.
* Built‑in usage tracking and billing.

Example:

```
agent.addCapability({
  name: 'generate_haiku',
  description: 'Generate a traditional 5‑7‑5 haiku about the supplied topic.',
  inputSchema: z.object({ topic: z.string() }),
  outputSchema: z.object({ haiku: z.string() })
});
```

### Runnable Capabilities (Custom Logic & External APIs)

When you need to call external services, perform data transformations, or embed proprietary business logic, you create a runnable capability. It requires a `run` function that receives the parsed arguments and an `action` context.

```
agent.addCapability({
  name: 'translate',
  description: 'Translate text to a target language using a third‑party translation API.',
  inputSchema: z.object({ text: z.string(), targetLanguage: z.string() }),
  async run({ args, action }) {
    const response = await fetch('https://api.translate.com/v2', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ q: args.text, target: args.targetLanguage })
    });
    const data = await response.json();
    return data.translatedText;
  }
});
```

Inside `run` you can also call `this.generate()` to delegate a sub‑LLM request, attach logs, or upload files to the current task.

Agent Helper Methods – What You Can Do Inside Capabilities
----------------------------------------------------------

The SDK injects a set of helper methods into the `this` context of every runnable capability. These methods make it easy to interact with the OpenServ platform without writing low‑level HTTP calls.

* **generate()** – Perform a platform‑delegated LLM call. Supports plain text prompts, structured output via a Zod schema, and multi‑turn conversation history.
* **addLogToTask()** – Append a log entry (info, warning, error) to the current task for debugging or audit trails.
* **uploadFile()** – Attach a file to one or more tasks, useful for delivering PDFs, images, or data dumps.
* **createTask(), updateTaskStatus(), getTaskDetail()** – Full CRUD operations for task management, enabling agents to orchestrate their own sub‑tasks.
* **getFiles(), deleteFile()** – Manage the file store associated with a workspace.

All helper methods automatically include the `workspaceId` and `auth token` from the `action` context, ensuring secure and correctly billed operations.

Action Context – Understanding the `action` Parameter
-----------------------------------------------------

Every runnable capability receives an `action` object that describes the origin of the request. The type is a union, where the `task` property only exists for the `'do-task'` variant. A typical guard looks like this:

```
async run({ args, action }) {
  if (action?.type === 'do-task' && action.task) {
    const { workspace, task } = action;
    // workspace.id, task.id, task.description, etc.
  }
}
```

Never destructure `action.task` before the guard; TypeScript will raise a type error.

Trigger Types – How Agents Are Invoked
--------------------------------------

OpenServ supports several trigger mechanisms that determine how external callers start an agent:

* **Webhook** – HTTP POST to a generated URL. Ideal for integrating with SaaS platforms.
* **x402** – Paid, on‑chain request that includes a price, timeout, and optional metadata. Perfect for monetizing AI services.
* **Cron** – Scheduled execution using standard cron syntax (e.g., `0 9 * * *` for daily 9 AM runs).
* **Manual** – Direct UI invocation from the OpenServ dashboard.

For webhook and x402 triggers, always set `timeout` to at least `600` seconds (10 minutes) to give the agent enough time for research, generation, or external API calls.

Real‑World Use Cases
--------------------

Below are five concrete scenarios where the OpenServ Agent SDK shines:

### 1. Content Generation Marketplace

Build a “Haiku Poetry Generator” that accepts a theme via an x402 trigger, uses a runless capability to produce a haiku, and returns the poem with a title and tags. Monetize each poem with a tiny fee, and let the platform handle billing and usage tracking.

### 2. Data Enrichment Service

A runnable capability calls a third‑party API (e.g., Clearbit) to enrich a list of email addresses. The agent can then use `this.generate()` to summarize each contact’s profile into a concise paragraph, attaching the result as a CSV file to the task.

### 3. Automated Customer Support Bot

Combine runless capabilities for FAQ answering with a runnable capability that creates tickets in a ticketing system. The agent can log each interaction, upload conversation transcripts, and close the task once the issue is resolved.

### 4. Financial Report Summarizer

Upload a PDF of a quarterly earnings report, use `this.uploadFile()` to store it, then invoke a runnable capability that extracts tables, runs calculations, and finally calls `this.generate()` to produce an executive summary.

### 5. Multi‑Agent Workflow Orchestration

Leverage the `openserv-client` skill to chain several agents: a data‑scraper agent gathers raw data, a transformer agent cleans it, and a final analytics agent produces visual insights. Each step runs as a separate task, with logs and files passed along the pipeline.

Benefits of Using the OpenServ Agent SDK
----------------------------------------

* **Zero‑API‑Key LLM Calls** – Runless capabilities and `generate()` let you use powerful language models without storing secrets.
* **On‑Chain Identity & Billing** – Agents are tied to a wallet, enabling transparent, trustless payment via x402.
* **Scalable Architecture** – The platform automatically tunnels development agents and can be run behind a custom HTTP server for production, supporting horizontal scaling.
* **Rich Ecosystem** – Seamless integration with the `openserv-client` skill provides full workflow orchestration, task management, and ERC‑8004 compliance.
* **Developer Friendly** – TypeScript, Zod schemas for validation, and a concise API reduce boilerplate and improve reliability.

Getting Started – Quick Installation Guide
------------------------------------------

```
# Initialize a new Node project
npm init -y
npm pkg set type=module

# Install the SDK, client, and Zod for schema validation
npm i @openserv-labs/sdk @openserv-labs/client zod dotenv

# Optional dev dependencies for TypeScript
npm i -D typescript tsx @types/node

# Add a dev script to package.json
# "dev": "tsx src/agent.ts"
```

Copy the `examples/basic-agent.ts` file into `src/agent.ts`, adjust the system prompt, add your desired capabilities, and run `npm run dev`. The SDK will spin up a tunnel, provision a wallet, and start listening for tasks.

Production Considerations
-------------------------

When moving to production, you should:

* Set `DISABLE_TUNNEL=true` and expose a stable HTTP endpoint.
* Store `WALLET_PRIVATE_KEY`, `OPENSERV_API_KEY`, and `OPENSERV_AUTH_TOKEN` securely (e.g., using a secret manager).
* Implement proper error handling and use `markTaskAsErrored()` to surface failures to end‑users.
* Monitor usage via the OpenServ dashboard to avoid unexpected costs.

Conclusion
----------

The OpenServ Agent SDK empowers developers to turn simple TypeScript functions into fully fledged, on‑chain‑compatible AI services. By abstracting wallet provisioning, task routing, and LLM billing, the SDK lets you focus on the core value proposition of your agent—whether that’s generating creative content, enriching data, or orchestrating complex multi‑agent workflows. With runless capabilities, the `generate()` helper, and seamless integration with the broader OpenServ ecosystem, you can launch scalable, monetizable AI agents in minutes rather than weeks.

Start building today, experiment with the provided examples, and explore the limitless possibilities of autonomous AI agents on the OpenServ platform.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/issa-me-sush/openserv-agent-sdk/SKILL.md>