---
layout: post
title: "node-transfer: High-Speed File Transfer Between OpenClaw Nodes"
date: 2026-03-06T21:17:09
categories: [24854]
original_url: https://insightginie.com/node-transfer-high-speed-file-transfer-between-openclaw-nodes
---

Introduction
------------

The `node-transfer` skill solves critical performance and memory issues when transferring large files between OpenClaw nodes. Traditional methods using `nodes.invoke` with Base64 encoding create significant overhead, consume excessive memory, and result in painfully slow transfers.

This skill implements native HTTP streaming with Node.js streams, providing zero memory overhead, no Base64 encoding, and transfer speeds limited only by network bandwidth.

Problem Solved
--------------

Before `node-transfer`, transferring large files between OpenClaw nodes faced several critical issues:

| Issue | Impact |
| --- | --- |
| Base64 Encoding Overhead | 33% larger payload, slower transfers |
| Memory Exhaustion (OOM) | Loading multi-GB files into memory crashes the process |
| Transfer Latency | JSON serialization/deserialization adds significant delay |
| 9-Minute Deployments | Re-deploying scripts on every transfer |

`node-transfer` eliminates these issues through native HTTP streaming, achieving up to 200x faster transfers with 99% less memory usage.

Architecture
------------

The skill uses a simple yet effective architecture:

```
┌──────────────┐     HTTP Stream      ┌──────────────┐
│  send.js     │ ◄──────────────────► │ receive.js   │
│  (Source)    │   (Token-protected)  │ (Destination)│
└──────────────┘                      └──────────────┘
   │                                     │
   ▼                                     ▼
┌──────────────┐                      ┌──────────────┐
│  Read Stream │                      │ Write Stream │
│  (fs.create  │                      │ (fs.create   │
│   ReadStream)│                      │  WriteStream)│
└──────────────┘                      └──────────────┘
   │                                     │
   ▼                                     ▼
┌──────────────┐                      ┌──────────────┐
│  File on     │                      │  File on     │
│  Disk        │                      │  Disk        │
└──────────────┘                      └──────────────┘
```

### Security Model

* **One-time Token**: 256-bit cryptographically random token (64 hex chars)
* **Single Connection**: Only one download allowed per token
* **Auto-shutdown**: Server closes after transfer completes or disconnects
* **Token Validation**: Every request must include the correct token

Requirements
------------

* **Node.js**: 14.0.0 or higher
* **Network**: TCP connectivity between nodes (any port 1024-65535)
* **Firewall**: Must allow outbound connections and inbound on ephemeral ports
* **Disk Space**: Sufficient space on destination for received files

Installation
------------

The “Install Once” pattern ensures scripts are deployed once per node and persist for future use.

### Method 1: Using deploy.js (Recommended)

```
# Generate deployment script for a target node
node deploy.js E3V3

# This outputs a PowerShell script that you can execute via nodes.invoke()
```

### Method 2: Manual Deployment

```
# Create directory
mkdir C:/openclaw/skills/node-transfer/scripts -Force

# Copy these files (ensure UTF-8 without BOM encoding):
# - send.js
# - receive.js
# - ensure-installed.js
# - version.js
```

### Method 3: Via OpenClaw Agent

```
// 1. Check if already installed (< 100ms)
const check = await nodes.invoke({
  node: 'E3V3',
  command: ['node', 'C:/openclaw/skills/node-transfer/scripts/ensure-installed.js', 'C:/openclaw/skills/node-transfer/scripts']
});
const checkResult = JSON.parse(check.output);
if (!checkResult.installed) {
  // 2. Deploy if needed (one-time, ~30 seconds)
  console.log('Deploying node-transfer to E3V3...');
  // ... deployment code ...
}
```

Usage
-----

### Basic Transfer Workflow

```
const INSTALL_DIR = 'C:/openclaw/skills/node-transfer/scripts';
const SOURCE_NODE = 'E3V3';
const DEST_NODE = 'E3V3-Docker';

// Step 1: Check installation on both nodes (fast!)
const [sourceCheck, destCheck] = await Promise.all([
  nodes.invoke({
    node: SOURCE_NODE,
    command: ['node', `${INSTALL_DIR}/ensure-installed.js`, INSTALL_DIR]
  }),
  nodes.invoke({
    node: DEST_NODE,
    command: ['node', `${INSTALL_DIR}/ensure-installed.js`, INSTALL_DIR]
  })
]);

// Deploy if needed (usually only once per node ever)
// ... deployment code if not installed ...

// Step 2: Start sender on source node
const sendResult = await nodes.invoke({
  node: SOURCE_NODE,
  command: ['node', `${INSTALL_DIR}/send.js`, 'C:/data/large-file.zip']
});
const { url, token, fileSize, fileName } = JSON.parse(sendResult.output);

// Step 3: Start receiver on destination node
const receiveResult = await nodes.invoke({
  node: DEST_NODE,
  command: ['node', `${INSTALL_DIR}/receive.js`, url, token, '/incoming/file.zip']
});
const result = JSON.parse(receiveResult.output);

console.log(`Transferred ${result.bytesReceived} bytes in ${result.duration}s at ${result.speedMBps}MB/s`);
```

### Command Line Usage

#### Sender

```
node send.js /path/to/file.zip
```

Output:

```
{
  "url": "http://192.168.1.10:54321/transfer",
  "token": "a1b2c3d4e5f6789...",
  "fileSize": 1073741824,
  "fileName": "file.zip",
  "sourceIp": "192.168.1.10",
  "port": 54321,
  "version": "1.0.0"
}
```

Options:

```
node send.js /path/to/file.zip --port 8080 --timeout 10
node send.js --help
node send.js --version
```

#### Receiver

```
node receive.js "http://192.168.1.10:54321/transfer" "token-here..." /path/to/save.zip
```

Output:

```
{
  "success": true,
  "bytesReceived": 1073741824,
  "totalBytes": 1073741824,
  "duration": 8.42,
  "speedMBps": 121.5,
  "outputPath": "/path/to/save.zip"
}
```

Options:

```
node receive.js    --timeout 60 --no-progress
node receive.js --help
node receive.js --version
```

API Reference
-------------

### send.js

Starts an HTTP server to stream a file.

#### Usage:

```
node send.js  [options]
```

#### Arguments:

* `filePath` (required): Path to the file to send

#### Options:

* `--port <n>`: Use specific port (default: random ephemeral)
* `--timeout <n>`: Timeout in minutes (default: 5)

#### Output (JSON):

| Field | Type | Description |
| --- | --- | --- |
| url | string | HTTP URL for receiver to connect to |
| token | string | Security token (64 hex chars) |
| fileSize | number | File size in bytes |
| fileName | string | Original filename |
| sourceIp | string | IP address of sender |
| port | number | TCP port used |
| version | string | Version of send.js |

#### Exit Codes:

* `0`: Success (transfer completed or info displayed)
* `1`: Error (check stderr for JSON error details)

#### Error Output (JSON):

```
{
  "error": "ERROR_CODE",
  "message": "Human-readable error message"
}
```

### receive.js

Connects to a sender and streams the file to disk.

#### Usage:

```
node receive.js <url> <token> <output> [options]
```

#### Arguments:

* `url` (required): Sender URL from send.js output
* `token` (required): Security token from send.js output
* `output` (required): Path to save the received file

#### Options:

* `--timeout <n>`: Timeout in minutes (default: 5)
* `--no-progress`: Disable progress output

#### Output (JSON):

| Field | Type | Description |
| --- | --- | --- |
| success | boolean | Whether transfer completed successfully |
| bytesReceived | number | Number of bytes received |
| totalBytes | number | Total bytes expected (from sender) |
| duration | number | Transfer duration in seconds |
| speedMBps | number | Average transfer speed in MB/s |
| outputPath | string | Path where file was saved |

#### Exit Codes:

* `0`: Success (transfer completed)
* `1`: Error (check stderr for JSON error details)

#### Error Output (JSON):

```
{
  "error": "ERROR_CODE",
  "message": "Human-readable error message"
}
```

Troubleshooting
---------------

### Common Issues

1. **Connection Refused**: Check firewall settings and ensure TCP connectivity between nodes
2. **Timeout Errors**: Increase timeout value if transferring very large files
3. **Permission Denied**: Ensure the script has read access to source files and write access to destination directories
4. **Invalid Token**: Verify the token matches exactly between sender and receiver

### Performance Tips

1. Use wired connections instead of WiFi for faster transfers
2. Close unnecessary applications to free up system resources
3. For extremely large files (>10GB), consider increasing timeout values
4. Ensure both nodes have sufficient disk space for the transfer

Conclusion
----------

The `node-transfer` skill provides a robust, high-performance solution for file transfers between OpenClaw nodes. By leveraging native Node.js streams and HTTP streaming, it eliminates the memory and performance bottlenecks of traditional Base64 encoding methods.

With its simple API, secure token-based authentication, and impressive performance improvements (up to 200x faster with 99% less memory), `node-transfer` is the recommended approach for any file transfer needs in OpenClaw environments.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/eisonme/node-transfer/SKILL.md>