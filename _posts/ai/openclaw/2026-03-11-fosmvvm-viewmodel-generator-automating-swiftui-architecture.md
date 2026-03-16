---
layout: post
title: "FOSMVVM ViewModel Generator: Automating SwiftUI Architecture"
date: 2026-03-11T00:16:14
categories: [24854]
original_url: https://insightginie.com/fosmvvm-viewmodel-generator-automating-swiftui-architecture
---

The FOSMVVM ViewModel Generator is a powerful tool that automates the creation of ViewModels for SwiftUI applications following the FOSMVVM architecture patterns. This skill generates ViewModels that serve as the bridge between your data models and SwiftUI views, handling everything from localization to error display patterns.

Core Architecture
-----------------

At its heart, the ViewModel acts as a bridge in the Model-View-ViewModel architecture:

Model (Data) → ViewModel (The Bridge) → View (SwiftUI)

The generator handles two distinct hosting modes for ViewModels:

* **Server-Hosted**: Data comes from server/database, uses hand-written factories
* **Client-Hosted**: Data is local to device, uses macro-generated factories

Key Features
------------

The generator automatically scaffolds:

* **RequestableViewModel**: For full pages/screens with server requests
* **Localization bindings**: Handles @LocalizedString references automatically
* **Stub factories**: For testing and previews
* **Error handling patterns**: Client-hosted ViewModels for ResponseError scenarios

Best Practices
--------------

The generator enforces FOSMVVM patterns:

* Views should only render, never compose or format data
* Use @LocalizedCompoundString for composed text instead of string interpolation
* Each error scenario gets its own specific ViewModel
* Hybrid apps can mix both hosting modes seamlessly

By automating ViewModel creation, the FOSMVVM ViewModel Generator ensures consistency, handles localization automatically, and enforces architectural best practices across your SwiftUI application.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/foscomputerservices/fosmvvm-viewmodel-generator/SKILL.md>