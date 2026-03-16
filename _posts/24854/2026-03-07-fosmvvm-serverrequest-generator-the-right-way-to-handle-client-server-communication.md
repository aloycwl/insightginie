---
layout: post
title: "FOSMVVM ServerRequest Generator: The Right Way to Handle Client-Server Communication"
date: 2026-03-07T11:17:30
categories: [24854]
original_url: https://insightginie.com/fosmvvm-serverrequest-generator-the-right-way-to-handle-client-server-communication
---

Building client-server communication in Swift applications can be surprisingly error-prone. Hardcoded URLs, manual JSON encoding, and inconsistent error handling create technical debt that compounds over time. The FOSMVVM ServerRequest Generator solves these problems by providing a type-safe, architecture-consistent approach to all client-server interactions.

What is FOSMVVM ServerRequest Generator?
----------------------------------------

The FOSMVVM ServerRequest Generator is a skill that automatically generates ServerRequest types for CRUD operations and client-server communication. It scaffolds requests, response bodies, and typed error handling, ensuring every client uses the same pattern for communicating with FOSMVVM servers.

### The Architecture Context

ServerRequest is THE way to communicate with an FOSMVVM server. No exceptions. Whether you’re building an iOS app, macOS app, web app, CLI tool, data collector, or background job, all clients use ServerRequest via the processRequest(mvvmEnv:) method.

The MVVMEnvironment holds configuration like baseURL, headers, version, and error handling. You configure it ONCE at startup and use it EVERYWHERE via processRequest().

What You Must NEVER Do
----------------------

Before we dive into the right approach, let’s look at what you should avoid:

* ❌ Wrong – hardcoded URL: `let url = URL(string: "http://server/api/users/123")!`
* ❌ Wrong – string path: `try await client.get("/api/users/\(id)")`
* ❌ Wrong – manual JSON encoding: `let json = try JSONEncoder().encode(body)`
* ❌ Wrong – hardcoded fetch path: `fetch('/api/users/123')`
* ❌ Wrong – constructing URLs manually: `` fetch(`/api/ideas/${ideaId}/move`) ``

What You Must ALWAYS Do
-----------------------

### Step 1: Configure MVVMEnvironment Once at Startup

For CLI tools, background jobs, or data collectors, configure at startup:

```
import ViewModels  // Your shared module
let mvvmEnv = await MVVMEnvironment(
    currentVersion: .currentApplicationVersion,
    appBundle: Bundle.module,
    deploymentURLs: [
        .debug: URL(string: "http://localhost:8080")!
    ]
)
```

Your shared module contains SystemVersion+App.swift:

```
public extension SystemVersion {
    static var currentApplicationVersion: Self {
        .v1_0
    }
    static var v1_0: Self {
        .init(major: 1, minor: 0, patch: 0)
    }
}
```

### Step 2: Use processRequest(mvvmEnv:) Everywhere

```
// ✅ RIGHT - ServerRequest with MVVMEnvironment
let request = UserShowRequest(query: .init(userId: id))
try await request.processRequest(mvvmEnv: mvvmEnv)
let user = request.responseBody

// ✅ RIGHT - Create operation
let createRequest = CreateIdeaRequest(requestBody: .init(content: content))
try await createRequest.processRequest(mvvmEnv: mvvmEnv)
let newId = createRequest.responseBody?.id

// ✅ RIGHT - Update operation
let updateRequest = MoveIdeaRequest(requestBody: .init(ideaId: id, newStatus: status))
try await updateRequest.processRequest(mvvmEnv: mvvmEnv)
```

When to Use This Skill
----------------------

Use the FOSMVVM ServerRequest Generator when:

* Implementing any client-server communication
* Adding CRUD operations (Create, Read, Update, Delete)
* Building data collectors or sync tools
* Any Swift code that needs to talk to the server

If you’re about to write URLRequest or a hardcoded path string, STOP and use this skill instead.

What ServerRequest Provides
---------------------------

The ServerRequest pattern handles several concerns automatically:

| Concern | How ServerRequest Handles It |
| --- | --- |
| URL Path | Derived from type name via Self.path (e.g., MoveIdeaRequest → /move\_idea) |
| HTTP Method | Determined by action.httpMethod (ShowRequest=GET, CreateRequest=POST, etc.) |
| Request Body | RequestBody type, automatically JSON encoded via requestBody?.toJSONData() |
| Response Body | ResponseBody type, automatically JSON decoded into responseBody |
| Error Response | ResponseError type, automatically decoded when response can’t decode as ResponseBody |
| Validation | RequestBody: ValidatableModel for write operations |
| Body Size Limits | RequestBody.maxBodySize for large uploads (files, images) |
| Type Safety | Compiler enforces correct types throughout |

### Request Protocol Selection

Choose based on the operation:

| Operation | Protocol | HTTP Method | RequestBody Required? |
| --- | --- | --- | --- |
| Read data | ShowRequest | GET | No |
| Read ViewModel | ViewModelRequest | GET | No |
| Create entity | CreateRequest | POST | Yes (ValidatableModel) |
| Update entity | UpdateRequest | PATCH | Yes (ValidatableModel) |
| Replace entity | (use .replace action) | PUT | Yes |
| Soft delete | DeleteRequest | DELETE | No |
| Hard delete | DestroyRequest | DELETE | No |

What This Skill Generates
-------------------------

### Core Files (Always)

| File | Location | Purpose |
| --- | --- | --- |
| {Action}Request.swift | {ViewModelsTarget}/Requests/ | The ServerRequest type |
| {Action}Controller.swift | {WebServerTarget}/Controllers/ | Server-side handler |

### Optional: WebApp Bridge (for web clients)

| File | Purpose |
| --- | --- |
| WebApp route | Bridges JS fetch to ServerRequest.fetch() |
| JS handler guidance | How to invoke from browser |

How to Use This Skill
---------------------

Invocation: /fosmvvm-serverrequest-generator

Prerequisites:

* Operation requirements understood from conversation context
* RequestBody and ResponseBody structures discussed or documented
* Client type identified (iOS app, WebApp, CLI tool, background job, etc.)

Workflow integration: This skill is typically used when implementing client-server communication. The skill references conversation context automatically—no file paths or Q&A needed. Often follows fosmvvm-viewmodel-generator (for ResponseBody ViewModels) and fosmvvm-fields-generator (for RequestBody validation).

Pattern Implementation
----------------------

This skill references conversation context to determine ServerRequest structure:

### Operation Type Detection

From conversation context, the skill identifies:

* CRUD operation (create, read, update, delete)
* HTTP semantics (GET for read, POST for create, PATCH/PUT for update, DELETE for delete)
* Protocol choice (ShowRequest, ViewModelRequest, CreateRequest, UpdateRequest, DeleteRequest)

### Request Structure Design

From requirements already in context:

* RequestBody fields (what data the client sends)
* Query parameters (URL query string data)
* Fragment parameters (URL fragment/anchor data)
* Validation requirements (ValidatableModel for write operations)

### Response Structure Design

From requirements already in context:

* ResponseBody type (often a ViewModel, sometimes just an ID)
* ResponseError type (custom error structure or EmptyError)
* Success scenarios (what indicates success)

Benefits of Using FOSMVVM ServerRequest Generator
-------------------------------------------------

By using this skill, you get:

* **Consistency**: All clients use the same pattern
* **Type Safety**: Compiler catches errors at compile time
* **Maintainability**: Changes to API structure are localized
* **Reduced Bugs**: No more hardcoded URLs or manual JSON handling
* **Better Testing**: ServerRequest types are easy to mock and test

The FOSMVVM ServerRequest Generator is an essential tool for any Swift project that needs reliable, maintainable client-server communication. By following the patterns it establishes, you’ll save time, reduce bugs, and create a more robust architecture for your application.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/foscomputerservices/fosmvvm-serverrequest-generator/SKILL.md>