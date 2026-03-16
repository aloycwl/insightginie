---
layout: post
title: 'Equity Valuation Framework: A Professional Playbook for Investment Analysis'
date: '2026-03-12T21:46:00'
categories:
- ai
- openclaw
original_url: https://insightginie.com/equity-valuation-framework-a-professional-playbook-for-investment-analysis/
featured_image: /media/images/8147.jpg
---

<p><strong>Equity Valuation Framework: A Professional Playbook for Investment Analysis</strong></p>
<p>The <a href="https://github.com/openclaw/skills/blob/main/sbulb/current.jpg"><em>Equity Valuation Framework</em></a> skill on <a href="https://github.com/openclaw/skills/tree/main/skills/ndtchan/equity-valuation-framework"><em>GitHub</em></a> provides a comprehensive, decision-grade playbook for professional equity valuation. This skill, maintained under the <a href="https://github.com/openclaw/skills"><em>OpenClaw repository</em></a>, transforms structured market and financial inputs into a standardized, high-quality report.</p>
<h2>Understanding the Equity Valuation Framework</h2>
<p><img decoding="async" src="https://github.com/openclaw/skills/blob/main/sbulb/current.jpg" alt="Equity Valuation Framework" style="float: right; margin: 10px;">The primary goal of the Equity Valuation Framework is to analyze already-fetched data, providing a consistent, professional view of a company&#8217;s value. It does not fetch data directly but requires structured inputs from other workflows, such as <code>vnstock-free-expert</code> for company, price, and ratio inputs, and <code>nso-macro-monitor</code>, <code>us-macro-news-monitor</code>, or <code>vn-market-news-monitor</code> for contextual macro and news data.</p>
<h2>When to Trigger the Equity Valuation Framework</h2>
<p>Use this skill in the following scenarios:</p>
<ul>
<li>When you need to &#8220;value this stock.&#8221;</li>
<li>When you want to determine if a stock is &#8220;cheap/expensive.&#8221;</li>
<li>When comparing stocks, such as in &#8220;best stock between A/B/C.&#8221;</li>
<li>When asking for a &#8220;bull/base/bear&#8221; analysis.</li>
<li>When you need a structured &#8220;investment memo.&#8221;</li>
</ul>
<p>The Equity Valuation Framework is designed for decision-ready reports, not just raw metrics.</p>
<h2>Required Input Contract</h2>
<p>The skill accepts an input bundle with various sections. Although missing fields are allowed, they must be flagged for transparency. Here is a sample input contract:</p>
<pre>{<br>	"ticker": "HPG",<br>	"as_of_date": "YYYY-MM-DD",<br>	"currency": "VND",<br>	"financials": {<br>		"income_statement": {},<br>		"balance_sheet": {},<br>		"cash_flow": {},<br>		"ratios": {}<br>	},<br>	"price_history": {<br>		"daily": [],<br>		"returns": {<br>			"1m": null,<br>			"3m": null,<br>			"6m": null,<br>			"12m": null<br>		}<br>	},<br>	"peer_set": ["AAA", "BBB"],<br>	"macro_snapshot": {},<br>	"news_digest": {},<br>	"metadata": {<br>		"source": "kbs|vci",<br>		"data_quality_notes": []<br>	}<br>}</pre>
<h2>Data Quality Gate</h2>
<p>The framework begins with a critical step: the Data Quality Gate, which assesses the completeness, freshness, and consistency of the input data. This step assigns an initial confidence level:</p>
<ul>
<li><strong>High</strong>: Data is complete, recent, and internally consistent.</li>
<li><strong>Medium</strong>: Minor gaps exist, but the valuation remains usable.</li>
<li><strong>Low</strong>: Major gaps require caution, and only a directional view is possible.</li>
</ul>
<h2>Valuation Modules</h2>
<p>The Equity Valuation Framework employs several modules, chosen based on the available data and the type of analysis needed:</p>
<h3>1. Multiples (Relative Valuation)</h3>
<p>This module compares the company&#8217;s performance to its peers using key ratios like P/E, P/B, and EV/EBITDA. It helps determine if the stock is under or overvalued relative to its industry.</p>
<h3>2. Discounted Cash Flow (DCF) Valuation</h3>
<p>DCF analysis estimates a company&#8217;s intrinsic value by discounting expected future cash flows back to the present. The framework uses revenue growth paths, margin paths, reinvestment assumptions, and weighted average cost of capital (WACC) for a comprehensive valuation.</p>
<h3>3. Sector-Specific Adaptation</h3>
<p>Different sectors require tailored analysis. For example:</p>
<ul>
<li><strong>Banks/Insurance/Financials</strong>: Focus on P/B, ROE, asset quality, and capital adequacy.</li>
<li><strong>Cyclicals</strong>: Use cycle-aware assumptions for commodities, chemicals, and other cyclical industries.</li>
</ul>
<h2>Scenario Framework</h2>
<p>The framework generates three scenarios based on different macroeconomic and industry conditions:</p>
<ul>
<li><strong>Bull</strong>: Optimistic outlook with better macroeconomic conditions and execution upside.</li>
<li><strong>Base</strong>: Most likely path under current conditions.</li>
<li><strong>Bear</strong>: Pessimistic scenario with macroeconomic or industry shocks and execution shortfalls.</li>
</ul>
<p>Each scenario includes key assumptions, expected fundamental trajectories, implied fair value ranges, and optional probability weights.</p>
<h2>Margin of Safety Rule</h2>
<p>The framework defines a &#8220;Fair Value&#8221; range using module triangulation and a &#8220;Safety Zone&#8221; below fair value, typically ranging from 15-30% depending on confidence and cyclicality. It avoids absolute buy/sell commands, instead using language like &#8220;appears undervalued / fairly valued / stretched&#8221; and emphasizing &#8220;margin-of-safety discipline.&#8221;</p>
<h2>Decision Policy</h2>
<p>The framework provides an integrated view by combining valuation outputs, business quality checklists, and macro/news constraints. It offers conditional action framing for portfolio risk management, with labels such as:</p>
<ul>
<li><strong>Attractive</strong>: Valuation discount + acceptable quality/risk.</li>
<li><strong>Watchlist</strong>: Mixed signals; wait for triggers.</li>
<li><strong>Caution</strong>: Valuation unsupported or risk too high.</li>
</ul>
<h2>Required Report Output Template</h2>
<p>Finally, the framework generates a detailed report with the following sections, ensuring clarity and comprehensive analysis:</p>
<ul>
<li><strong>Executive Summary</strong>: One paragraph outlining the current valuation stance and why.</li>
<li><strong>What Data Was Used</strong>: Source, as-of date, statement periods, peer set.</li>
<li><strong>Core Thesis (Bull / Base / Bear)</strong>: Key drivers by scenario.</li>
<li><strong>Valuation Work</strong>: Multiples table, DCF summary, sensitivity table.</li>
<li><strong>Business Quality Assessment</strong>: Checklist table with evidence lines.</li>
<li><strong>Risk Register</strong>: Ranked risks with impact, probability, and monitoring trigger.</li>
<li><strong>Fair Value and Safety Zone</strong>: Fair value range and margin-of-safety zone with rationale.</li>
<li><strong>Confidence and Gaps</strong>: Confidence level and missing data that could change the view.</li>
<li><strong>Disclaimer</strong>: Educational analysis only, not personalized investment advice.</li>
</ul>
<h2>Formatting Standards</h2>
<p>The framework adheres to strict formatting standards, ensuring clarity and consistency:</p>
<ul>
<li>Use simple language and explain terms briefly.</li>
<li>State all critical assumptions explicitly.</li>
<li>Distinguish facts vs. assumptions vs. inference.</li>
<li>Do not hide data gaps; surface them early.</li>
<li>Keep numbers auditable and unit-consistent (VND bn/trn, %, x).</li>
</ul>
<h2>Conclusion</h2>
<p>The <a href="https://github.com/openclaw/skills/blob/main/sbulb/current.jpg"><em>Equity Valuation Framework</em></a> skill on GitHub is a comprehensive tool designed to standardize the equity valuation process. Whether you are a seasoned analyst or just starting out, this framework provides a clear and structured method for analyzing stocks, making it an invaluable resource for professionals and investors alike.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/ndtchan/equity-valuation-framework/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/ndtchan/equity-valuation-framework/SKILL.md</a></p>
