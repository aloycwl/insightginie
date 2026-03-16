---
layout: post
title: "Understanding the Teneo SDK: Connecting to AI Agents with WebSocket and Blockchain Payments"
date: 2026-03-09T00:21:38
categories: [24854]
original_url: https://insightginie.com/understanding-the-teneo-sdk-connecting-to-ai-agents-with-websocket-and-blockchain-payments
---

What is the Teneo SDK?
----------------------

The Teneo SDK is a powerful tool that enables developers to connect to AI agents on the Teneo Protocol platform. It provides a comprehensive set of features for real-time communication, authentication, and payment processing, making it easier than ever to integrate AI agents into your applications.

At its core, the Teneo SDK uses WebSocket-based communication to establish a persistent connection with AI agents. This allows for real-time, bidirectional communication between your application and the AI agents, enabling seamless interactions and instant responses.

Key Features of the Teneo SDK
-----------------------------

The Teneo SDK offers a range of features that make it a versatile and powerful tool for developers:

### WebSocket-based Real-time Communication

The SDK uses WebSocket technology to establish a persistent connection with AI agents. This enables real-time, bidirectional communication, allowing for instant responses and seamless interactions.

### Wallet-based Authentication using Ethereum Private Keys

Authentication is handled through Ethereum private keys, providing a secure and decentralized way to verify user identity. This approach leverages the security and trust of the Ethereum blockchain.

### Room Management

The SDK includes features for managing communication rooms, which can be either private or public. Private rooms are automatically available after authentication, while public rooms require explicit subscription.

### x402 Micropayment Protocol

The SDK supports the x402 micropayment protocol, which allows for small, instant payments to AI agents. This is particularly useful for paid agent interactions, where users pay a small fee for each request.

### Multi-chain Payment Support

The SDK supports multiple blockchain networks, including Base, Peaq, and Avalanche. This flexibility allows developers to choose the network that best suits their needs in terms of cost, speed, and availability.

Installation and Setup
----------------------

Getting started with the Teneo SDK is straightforward. You can install it using npm or pnpm:

```
npm install @teneo-protocol/sdk
# or
pnpm add @teneo-protocol/sdk
```

Core Concepts
-------------

Before diving into the implementation details, it’s important to understand some key concepts:

### Rooms

Rooms are communication channels where users interact with AI agents. There are two types of rooms:

* **Private rooms**: These are automatically available after authentication and do not require any subscription.
* **Public rooms**: These require explicit subscription via the `subscribeToRoom()` method.

Room ownership determines who can invite agents to the room, adding an extra layer of control and security.

### Agents

AI agents are identified by their @handle (e.g., @x-agent-enterprise-v2). They can be discovered through the `listAgents()` or `searchAgents()` methods, and invited to private rooms by room owners.

Some agents require x402 payments for each interaction, so it’s important to check the agent’s pricing before use.

### x402 Payment Protocol

The x402 payment protocol is a micropayment system that uses USDC (a stablecoin) on supported blockchain networks. This allows for small, instant payments to AI agents, typically ranging from $0.01 to $0.10 per request.

Authentication and Connection
-----------------------------

Connecting to the Teneo platform requires authentication using an Ethereum private key. Here’s a basic example of how to set up the SDK:

```
import { TeneoSDK } from "@teneo-protocol/sdk";

const sdk = new TeneoSDK({
  wsUrl: "wss://backend.developer.chatroom.teneo-protocol.ai/ws",
  privateKey: "0x...",
  logLevel: "silent",
  maxReconnectAttempts: 30,
  paymentNetwork: "eip155:8453",
  paymentAsset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
});

await sdk.connect();
```

This code initializes the SDK with the necessary configuration, including the WebSocket URL, Ethereum private key, and payment settings. The `connect()` method establishes the connection and handles both WebSocket and wallet signature authentication.

### Payment Network Configuration

The SDK supports multiple blockchain networks for payments. Here’s a table of the supported networks and their configurations:

| Network | CAIP-2 ID | Chain ID | USDC Contract |
| --- | --- | --- | --- |
| Base | eip155:8453 | 8453 | 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 |
| Peaq | eip155:3338 | 3338 | 0xbbA60da06c2c5424f03f7434542280FCAd453d10 |
| Avalanche | eip155:43114 | 43114 | 0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E |

Base is recommended for low fees, but you can choose the network that best fits your needs.

Room Management
---------------

Managing rooms is a crucial part of using the Teneo SDK. Here’s how you can work with rooms:

### Discovering Rooms

After connecting, you can get a list of all rooms available to your wallet:

```
const rooms = sdk.getRooms();
for (const room of rooms) {
  console.log(`Room: ${room.name} [${room.id}]`);
  console.log(`  Public: ${room.is_public}`);
  console.log(`  Owner: ${room.is_owner}`);
}
```

This will give you information about each room, including whether it’s public, who owns it, and its unique ID.

### Subscribing to Rooms

Private rooms are automatically available after authentication, but public rooms require explicit subscription:

```
const publicRoom = rooms.find(r => r.is_public);
if (publicRoom) {
  await sdk.subscribeToRoom(publicRoom.id);
}
```

You can then check which rooms you’re subscribed to:

```
const subscribedRooms = sdk.getSubscribedRooms();
console.log(`Subscribed to: ${subscribedRooms.join(", ")}`);
```

Agent Discovery and Invitation
------------------------------

Finding and inviting agents to your rooms is a key part of using the Teneo SDK:

### Finding Available Agents

You can list all available agents on the platform:

```
const agents = await sdk.listAgents();
for (const agent of agents) {
  console.log(`Agent: ${agent.name} (@${agent.handle})`);
  console.log(`  ID: ${agent.agent_id}`);
  console.log(`  Description: ${agent.description}`);
  console.log(`  Price: $${agent.price_per_request || 0}`);
}
```

You can also search for agents by name or keyword:

```
const results = await sdk.searchAgents("twitter");
console.log(`Found ${results.length} agents matching "twitter"`);
```

### Inviting Agents to Rooms

Only room owners can invite agents to rooms. Here’s how you can invite an agent:

```
const xAgent = agents.find(a => a.handle === "x-agent-enterprise-v2");
if (xAgent) {
  await sdk.addAgentToRoom(roomId, xAgent.agent_id);
  console.log(`Invited ${xAgent.name} to room`);
}
```

You can also invite agents directly by their known agent ID:

```
await sdk.addAgentToRoom(roomId, "x-agent-enterprise-v2");
```

### Ensuring Required Agents Are in Room

If you need to ensure that specific agents are in a room, you can use the following function:

```
async function ensureAgentsInRoom(sdk, roomId, requiredAgentIds) {
  const roomAgents = await sdk.listRoomAgents(roomId);
  const existingIds = new Set(roomAgents.map(a => a.agent_id?.toLowerCase()));
  
  const missing = requiredAgentIds.filter(id => !existingIds.has(id.toLowerCase()));
  
  for (const agentId of missing) {
    try {
      await sdk.addAgentToRoom(roomId, agentId);
      console.log(`Invited agent "${agentId}" to room`);
    } catch (err) {
      console.warn(`Failed to invite "${agentId}": ${err.message}`);
    }
  }
}
```

Sending Messages to Agents
--------------------------

Once you have agents in your room, you can start sending messages to them:

```
const response = await sdk.sendMessage("@x-agent-enterprise-v2 user @elonmusk", {
  waitForResponse: true,
  timeout: 60000,
  format: "both"
});
console.log(response.humanized || response.content);
```

You can also specify a target room for the message:

```
const response = await sdk.sendMessage("@x-agent-enterprise-v2 post_stats 123456", {
  waitForResponse: true,
  timeout: 60000,
  format: "both",
  room: "room-id-here"
});
```

### Common Agent Commands

Here are some common commands you can use with agents:

* **X/Twitter agent – Get user profile stats**: “@x-agent-enterprise-v2 user @username”
* **X/Twitter agent – Get post/tweet stats**: “@x-agent-enterprise-v2 post\_stats 1234567890123456789”

Event Handling
--------------

The SDK provides event handling for agent responses and payment detection:

### Agent Responses

You can listen for agent responses using the following code:

```
sdk.on("agent:response", (data) => {
  console.log(`Agent: ${data.agentName || data.agentId}`);
  console.log(`Success: ${data.success}`);
  console.log(`Content: ${data.humanized || data.content}`);
  if (data.error) {
    console.error(`Error: ${data.error}`);
  }
});
```

### Payment Detection

You can detect payments in agent responses by parsing the content for common payment patterns:

```
sdk.on("agent:response", (data) => {
  const content = data.humanized || data.content || "";
  const patterns = [
    /x402Payment\$(\d+\.\d+)/i,
    /Payment[:\s]+\$(\d+\.\d+)/i,
    /charged\$(\d+\.\d+)/i,
    /\$(\d+\.\d+)\s*(?:USDC|usdc)/i,
  ];
  
  for (const pattern of patterns) {
    const match = content.match(pattern);
    if (match) {
      const usdAmount = parseFloat(match[1]);
      console.log(`Payment detected: $${usdAmount}`);
    }
  }
});
```

Conclusion
----------

The Teneo SDK provides a powerful and flexible way to integrate AI agents into your applications. With its WebSocket-based communication, Ethereum wallet authentication, and x402 micropayment protocol, it offers a comprehensive solution for building AI-powered applications.

Whether you’re building a chatbot, a social media analytics tool, or any other application that could benefit from AI agents, the Teneo SDK provides the tools you need to get started. Its support for multiple blockchain networks and its robust event handling make it a versatile choice for developers looking to leverage the power of AI agents.

By following the guidelines in this article, you should be well-equipped to start using the Teneo SDK in your own projects. Happy coding!

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/hunterdrop22/tyt/SKILL.md>