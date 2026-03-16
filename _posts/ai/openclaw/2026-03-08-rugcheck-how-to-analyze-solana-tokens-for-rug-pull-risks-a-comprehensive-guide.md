---
layout: post
title: "RugCheck: How to Analyze Solana Tokens for Rug Pull Risks &#8211; A Comprehensive Guide"
date: 2026-03-08T21:45:58
categories: [24854]
original_url: https://insightginie.com/rugcheck-how-to-analyze-solana-tokens-for-rug-pull-risks-a-comprehensive-guide
---

Understanding RugCheck: Your Solana Token Safety Analyzer
=========================================================

In the fast-paced world of cryptocurrencies, especially in ecosystems like Solana, the need for reliable token analysis tools is paramount to avoid potential rug pulls and scams. RugCheck has emerged as a popular solution for Solana token safety analysis. This article will explore what RugCheck does and how you can use it to evaluate Solana tokens effectively.

What is RugCheck?
-----------------

RugCheck is a free API service that allows users to analyze Solana tokens by their mint addresses for potential rug pull risks. It provides a comprehensive report that includes risk scores, risk flags, liquidity provider information, token metadata, holder distribution, and more.

Key Features of RugCheck
------------------------

### Risk Score and Flags

RugCheck assigns a risk score to each token on a scale from 0 to 100, with higher scores indicating higher risk. The scores are accompanied by risk flags that highlight specific concerns, such as mutable metadata, low liquidity, or a single holder owning a large percentage of the token supply.

* **0-30:** Low risk (Good)
* **30-60:** Medium risk (Caution)
* **60-100:** High risk (Danger)

### Liquidity Provider Information

One of the critical aspects RugCheck analyzes is the percentage of liquidity provider (LP) tokens that are locked. If the LP tokens are not locked, it indicates that the creator can pull the liquidity anytime, which is a significant red flag for potential rug pulls.

### Token Metadata Analysis

RugCheck examines token metadata to determine if it is mutable, meaning the creator can change the token's name, image, or other metadata. This is another critical red flag, as it can be used to deceive holders.

### Holder Distribution

The tool also provides detailed information about the distribution of token holders. Highly concentrated holder distributions, where a few wallets hold a large percentage of the token supply, can indicate potential risks.

How to Use RugCheck
-------------------

### Getting Started

The easiest way to use RugCheck is through its command-line script. Below are some basic commands to help you get started:

#### 1. Get Risk Summary

To get a quick summary of a token's risk, use the following command:

```
bash scripts/rugcheck.sh summary <MINT_ADDRESS>
```

This will provide you with a risk score, risk flags, and the percentage of LP tokens locked.

#### 2. Get Full Detailed Report

For a more comprehensive report, use this command:

```
bash scripts/rugcheck.sh report <MINT_ADDRESS>
```

This will give you detailed information about the token's metadata, holders, markets, creator information, and more.

### Interpreting the Results

Here are the key fields and their meanings:

* **score\_normalised:** Risk score from 0 to 100.
* **risks[]:** An array of risk flags with details including risk type, level, description, and raw risk contribution.
* **lpLockedPct:** Percentage of LP tokens locked.
* **tokenProgram:** SPL token program used.
* **tokenType:** Token type classification.
* **tokenMeta:** Information about the token's name, symbol, URI, mutable flag, and update authority.
* **token:** Details about the token's supply, decimals, mint authority, and freeze authority.
* **creator/creatorBalance:** Information about the token creator and their current balance.
* **topHolders[]:** Top holders with their addresses, owner information, percentage of supply, and UI amount.
* **markets[]:** DEX markets/pools with liquidity data.
* **insiderNetworks:** Connected insider wallet clusters.

Red Flag Checklist
------------------

When analyzing a token with RugCheck, it's essential to look out for the following red flags:

* **Mutable Metadata:** If token metadata is mutable, the creator can change the token's name or image, which is a significant risk.
* **Low Liquidity:** Tokens with low liquidity are easier to manipulate.
* **High Holder Concentration:** If the top 10 holders own more than 50% of the supply, it indicates high risk.
* **Single Holder Dominance:** If one wallet holds more than 20% of the supply, it's a red flag.
* **LP Not Locked:** If the LP tokens are not locked, the creator can pull liquidity anytime.
* **Mint Authority Exists:** The creator can mint an infinite number of tokens if the mint authority exists.
* **Freeze Authority Exists:** If the freeze authority exists, the creator can freeze wallets.
* **Few LP Providers:** If only 1-2 wallets are providing liquidity, it's a risk.
* **Low/Zero Trade Volume:** No real market activity is a red flag.
* **Creator Holds Large Balance:** If the creator still holds a significant portion of the supply, it indicates potential risk.

presenting Findings
-------------------

To present the analysis findings clearly, you can format the results like this example:

```
🔍 RugCheck Analysis: CLWDN (ClawdNation)  
Mint: 3zvSRWfjPvcnt8wfTrKhgCtQVwVSrYfBY6g1jPwzfHJG  
⚠️ Risk Score: 59/100 (Medium-High Risk)  
  
🚩 Risk Flags:  
🔴 Low Liquidity — $102.55  
⚠️ Single holder ownership — 40.00%  
⚠️ High holder concentration — Top 10 hold >50%  
⚠️ Low amount of holders  
⚠️ Low LP providers  
⚠️ Mutable metadata  
  
🔓 LP Locked: 0% (NOT LOCKED)  
📊 Top Holders:  
1. 40.0% — 3Y3g...p7rk  
2. 15.0% — 5bNH...4VGj  
3. 15.0% — 4dkX...Ncg6  
4. 10.0% — 8yY2...CKn8  
5. 10.0% — 2MT5...eB3h  
  
Verdict: HIGH RISK — Multiple red flags. No locked liquidity, concentrated holdings, mutable metadata. Exercise extreme caution.
```

API Details
-----------

The RugCheck API allows you to access its functionality programmatically. Here are some essential details about the API:

### Base URL

<https://api.rugcheck.xyz>

### Auth

Auth is not required for read endpoints such as viewing token summaries or detailed reports.

### Rate Limits

Respect 429 responses and add delays of 2-3 seconds between bulk queries to avoid rate limiting.

### Bulk Queries

For larger-scale analyses, RugCheck offers bulk query endpoints that require a JWT from Solana wallet auth:

* **POST /v1/bulk/tokens/summary:** Check multiple tokens at once.
* **POST /v1/bulk/tokens/report:** Get full reports for multiple tokens.

Please note that these bulk query endpoints may not be accessible to most agents without proper authentication.

RugCheck Web Interface
----------------------

In addition to the API, RugCheck also offers a web interface where users can easily check tokens by entering the mint address:

<https://rugcheck.xyz/tokens/<mint>>

This user-friendly interface makes it easy for non-technical users to analyze token safety.

Conclusion
----------

RugCheck is an invaluable tool for anyone looking to analyze Solana tokens and avoid potential rug pulls. By providing comprehensive risk scores, detailed reports, and an easy-to-use interface, it empowers users to make informed decisions about token safety. Whether you're an investor, developer, or just curious about the Solana ecosystem, RugCheck is a resource you shouldn't overlook.

To explore RugCheck in depth, visit the [OpenClaw skills repository on GitHub](https://github.com/openclaw/skills/tree/main/skills/skills/psychotechv4/rugcheck) for more information and usage examples.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/psychotechv4/rugcheck/SKILL.md>