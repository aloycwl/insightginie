---
layout: post
title: "Equity Valuation Framework: A Professional Playbook for Investment Analysis"
date: 2026-03-12T21:46:00
categories: [24854]
original_url: https://insightginie.com/equity-valuation-framework-a-professional-playbook-for-investment-analysis
---

**Equity Valuation Framework: A Professional Playbook for Investment Analysis**

The [*Equity Valuation Framework*](https://github.com/openclaw/skills/blob/main/sbulb/current./media/images//media/images//media/images/jpg) skill on [*GitHub*](https://github.com/openclaw/skills/tree/main/skills/ndtchan/equity-valuation-framework) provides a comprehensive, decision-grade playbook for professional equity valuation. This skill, maintained under the [*OpenClaw repository*](https://github.com/openclaw/skills), transforms structured market and financial inputs into a standardized, high-quality report.

Understanding the Equity Valuation Framework
--------------------------------------------

![Equity Valuation Framework](https://github.com/openclaw/skills/blob/main/sbulb/current./media/images//media/images//media/images/jpg)The primary goal of the Equity Valuation Framework is to analyze already-fetched data, providing a consistent, professional view of a company's value. It does not fetch data directly but requires structured inputs from other workflows, such as `vnstock-free-expert` for company, price, and ratio inputs, and `nso-macro-monitor`, `us-macro-news-monitor`, or `vn-market-news-monitor` for contextual macro and news data.

When to Trigger the Equity Valuation Framework
----------------------------------------------

Use this skill in the following scenarios:

* When you need to “value this stock.”
* When you want to determine if a stock is “cheap/expensive.”
* When comparing stocks, such as in “best stock between A/B/C.”
* When asking for a “bull/base/bear” analysis.
* When you need a structured “investment memo.”

The Equity Valuation Framework is designed for decision-ready reports, not just raw metrics.

Required Input Contract
-----------------------

The skill accepts an input bundle with various sections. Although missing fields are allowed, they must be flagged for transparency. Here is a sample input contract:

```
{  
	"ticker": "HPG",  
	"as_of_date": "YYYY-MM-DD",  
	"currency": "VND",  
	"financials": {  
		"income_statement": {},  
		"balance_sheet": {},  
		"cash_flow": {},  
		"ratios": {}  
	},  
	"price_history": {  
		"daily": [],  
		"returns": {  
			"1m": null,  
			"3m": null,  
			"6m": null,  
			"12m": null  
		}  
	},  
	"peer_set": ["AAA", "BBB"],  
	"macro_snapshot": {},  
	"news_digest": {},  
	"metadata": {  
		"source": "kbs|vci",  
		"data_quality_notes": []  
	}  
}
```

Data Quality Gate
-----------------

The framework begins with a critical step: the Data Quality Gate, which assesses the completeness, freshness, and consistency of the input data. This step assigns an initial confidence level:

* **High**: Data is complete, recent, and internally consistent.
* **Medium**: Minor gaps exist, but the valuation remains usable.
* **Low**: Major gaps require caution, and only a directional view is possible.

Valuation Modules
-----------------

The Equity Valuation Framework employs several modules, chosen based on the available data and the type of analysis needed:

### 1. Multiples (Relative Valuation)

This module compares the company's performance to its peers using key ratios like P/E, P/B, and EV/EBITDA. It helps determine if the stock is under or overvalued relative to its industry.

### 2. Discounted Cash Flow (DCF) Valuation

DCF analysis estimates a company's intrinsic value by discounting expected future cash flows back to the present. The framework uses revenue growth paths, margin paths, reinvestment assumptions, and weighted average cost of capital (WACC) for a comprehensive valuation.

### 3. Sector-Specific Adaptation

Different sectors require tailored analysis. For example:

* **Banks/Insurance/Financials**: Focus on P/B, ROE, asset quality, and capital adequacy.
* **Cyclicals**: Use cycle-aware assumptions for commodities, chemicals, and other cyclical industries.

Scenario Framework
------------------

The framework generates three scenarios based on different macroeconomic and industry conditions:

* **Bull**: Optimistic outlook with better macroeconomic conditions and execution upside.
* **Base**: Most likely path under current conditions.
* **Bear**: Pessimistic scenario with macroeconomic or industry shocks and execution shortfalls.

Each scenario includes key assumptions, expected fundamental trajectories, implied fair value ranges, and optional probability weights.

Margin of Safety Rule
---------------------

The framework defines a “Fair Value” range using module triangulation and a “Safety Zone” below fair value, typically ranging from 15-30% depending on confidence and cyclicality. It avoids absolute buy/sell commands, instead using language like “appears undervalued / fairly valued / stretched” and emphasizing “margin-of-safety discipline.”

Decision Policy
---------------

The framework provides an integrated view by combining valuation outputs, business quality checklists, and macro/news constraints. It offers conditional action framing for portfolio risk management, with labels such as:

* **Attractive**: Valuation discount + acceptable quality/risk.
* **Watchlist**: Mixed signals; wait for triggers.
* **Caution**: Valuation unsupported or risk too high.

Required Report Output Template
-------------------------------

Finally, the framework generates a detailed report with the following sections, ensuring clarity and comprehensive analysis:

* **Executive Summary**: One paragraph outlining the current valuation stance and why.
* **What Data Was Used**: Source, as-of date, statement periods, peer set.
* **Core Thesis (Bull / Base / Bear)**: Key drivers by scenario.
* **Valuation Work**: Multiples table, DCF summary, sensitivity table.
* **Business Quality Assessment**: Checklist table with evidence lines.
* **Risk Register**: Ranked risks with impact, probability, and monitoring trigger.
* **Fair Value and Safety Zone**: Fair value range and margin-of-safety zone with rationale.
* **Confidence and Gaps**: Confidence level and missing data that could change the view.
* **Disclaimer**: Educational analysis only, not personalized investment advice.

Formatting Standards
--------------------

The framework adheres to strict formatting standards, ensuring clarity and consistency:

* Use simple language and explain terms briefly.
* State all critical assumptions explicitly.
* Distinguish facts vs. assumptions vs. inference.
* Do not hide data gaps; surface them early.
* Keep numbers auditable and unit-consistent (VND bn/trn, %, x).

Conclusion
----------

The [*Equity Valuation Framework*](https://github.com/openclaw/skills/blob/main/sbulb/current./media/images//media/images//media/images/jpg) skill on GitHub is a comprehensive tool designed to standardize the equity valuation process. Whether you are a seasoned analyst or just starting out, this framework provides a clear and structured method for analyzing stocks, making it an invaluable resource for professionals and investors alike.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/ndtchan/equity-valuation-framework/SKILL.md>