---
layout: post
title: 'FOSMVVM ViewModel Generator: Automating SwiftUI Architecture'
date: '2026-03-10T16:16:14'
categories:
- ai
- openclaw
original_url: https://insightginie.com/fosmvvm-viewmodel-generator-automating-swiftui-architecture/
featured_image: /media/images/8142.jpg
---

<p>The FOSMVVM ViewModel Generator is a powerful tool that automates the creation of ViewModels for SwiftUI applications following the FOSMVVM architecture patterns. This skill generates ViewModels that serve as the bridge between your data models and SwiftUI views, handling everything from localization to error display patterns.</p>
<h2>Core Architecture</h2>
<p>At its heart, the ViewModel acts as a bridge in the Model-View-ViewModel architecture:</p>
<p>Model (Data) → ViewModel (The Bridge) → View (SwiftUI)</p>
<p>The generator handles two distinct hosting modes for ViewModels:</p>
<ul>
<li><strong>Server-Hosted</strong>: Data comes from server/database, uses hand-written factories</li>
<li><strong>Client-Hosted</strong>: Data is local to device, uses macro-generated factories</li>
</ul>
<h2>Key Features</h2>
<p>The generator automatically scaffolds:</p>
<ul>
<li><strong>RequestableViewModel</strong>: For full pages/screens with server requests</li>
<li><strong>Localization bindings</strong>: Handles @LocalizedString references automatically</li>
<li><strong>Stub factories</strong>: For testing and previews</li>
<li><strong>Error handling patterns</strong>: Client-hosted ViewModels for ResponseError scenarios</li>
</ul>
<h2>Best Practices</h2>
<p>The generator enforces FOSMVVM patterns:</p>
<ul>
<li>Views should only render, never compose or format data</li>
<li>Use @LocalizedCompoundString for composed text instead of string interpolation</li>
<li>Each error scenario gets its own specific ViewModel</li>
<li>Hybrid apps can mix both hosting modes seamlessly</li>
</ul>
<p>By automating ViewModel creation, the FOSMVVM ViewModel Generator ensures consistency, handles localization automatically, and enforces architectural best practices across your SwiftUI application.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/foscomputerservices/fosmvvm-viewmodel-generator/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/foscomputerservices/fosmvvm-viewmodel-generator/SKILL.md</a></p>
