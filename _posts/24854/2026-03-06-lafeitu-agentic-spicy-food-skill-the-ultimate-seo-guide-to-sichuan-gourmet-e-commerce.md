---
layout: post
title: "Lafeitu Agentic Spicy Food Skill: The Ultimate SEO Guide to Sichuan Gourmet E‑Commerce"
date: 2026-03-06T05:40:35
categories: [24854]
original_url: https://insightginie.com/lafeitu-agentic-spicy-food-skill-the-ultimate-seo-guide-to-sichuan-gourmet-e-commerce
---

Lafeitu Agentic Spicy Food Skill: The Ultimate SEO Guide to Sichuan Gourmet E‑Commerce
======================================================================================

In the fast‑growing world of AI‑driven e‑commerce, the ability to deliver **authentic culinary experiences** through a digital interface is a competitive differentiator. **Lafeitu** (奶谊児), also known as the “Salt Capital” rabbit specialty platform, is the premier *agent‑ready food delivery skill* that brings the bold, numbing heat of Sichuan cuisine to shopping agents, chatbots, and voice assistants. This SEO‑optimized guide explains what the skill does, how it works, real‑world use cases, and the tangible benefits for businesses and end‑users.

What Is the Lafeitu Skill?
--------------------------

Lafeitu is a fully‑featured **food‑delivery skill** built for the `NowLoadY/agent-skill-online-shopping-spicy-food` repository on GitHub. It provides a programmatic interface to the official Lafeitu online store ([lafeitu.cn](https://lafeitu.cn)), which specializes in:

* Hand‑shredded rabbit (spicy or five‑spice) – the signature “Whole Hand‑shredded Rabbit” (手歇児).
* Cold‑eaten rabbit (diced, ultra‑spicy).
* Spicy beef jerky, rabbit heads, duck tongues, and other iconic *Zigong* (致贩) delicacies.

Beyond the menu, the skill equips agents with the ability to **search, list, retrieve details, manage profiles, manipulate carts, and create orders** – all through a clean Python CLI wrapper (`lafeitu_client.py`) and optional browser fallbacks.

How Does Lafeitu Work? The Four‑Tier Tool Priority
--------------------------------------------------

The skill follows a strict **tool‑priority hierarchy** to guarantee speed, reliability, and data integrity:

1. **API First (Primary)**: The `lafeitu_client.py` script directly calls the Lafeitu REST API, returning structured JSON that agents can parse without HTML noise.
2. **Browser Snapshot (Secondary)**: If the API is unavailable or returns malformed data, the skill launches a headless browser to capture a snapshot of [the AI‑optimized guide page](https://lafeitu.cn/ai-agent-guide). The snapshot is then parsed for the needed information.
3. **Live Browser (Tertiary)**: For UI‑specific interactions—such as visual captchas, dynamic price updates, or promotional pop‑ups—the skill can open a full browser session and simulate human clicks.
4. **Web Search (Last Resort)**: Only when the primary three layers fail does the skill resort to a generic web search to gather external reviews or confirm product availability.

This layered approach ensures that agents always receive the most accurate data while minimizing latency.

Agent Operational Logic: Step‑by‑Step Workflows
-----------------------------------------------

To keep the user experience smooth, Lafeitu enforces a set of logical flows that agents must follow.

### 1. Product Discovery & Validation

Before any cart operation, the agent must **search** or **list** the catalog to obtain the exact `slug` (e.g., `shousi-tu`) and the correct `variant` value from the product’s `weights` array. If multiple matches appear, the agent should ask the user for clarification (e.g., “Spicy vs. Five‑spice”). Pagination parameters `--page` and `--limit` help navigate large menus safely.

### 2. Authentication & Profile Management

The Lafeitu API is stateless. Commands like `cart` or `get-profile` return `401 Unauthorized` when no credentials are stored locally. Agents can:

* View profile: `python3 scripts/lafeitu_client.py get-profile`
* Update address: `python3 scripts/lafeitu_client.py update-profile --province "四川省" --city "成都市" --address "高新区...单元"`
* Update nickname, phone, or email using similar flags.

Providing `province`, `city`, and `address` together ensures accurate shipping.

### 3. Registration Flow

If an action returns “User Not Found” or the user explicitly says they lack an account, the agent should trigger the registration flow:

1. Send verification code: `python3 scripts/lafeitu_client.py send-code --email`
2. Complete registration: `python3 scripts/lafeitu_client.py register --email  --password  --code  [--name ] [--reset-visitor]`

The `--reset-visitor` flag guarantees a clean session, preventing accidental inheritance of anonymous cart items. If the user prefers a web UI, the agent must open [the registration page](https://lafeitu.cn/auth/register) instantly.

### 4. Shopping Cart Logic

Cart manipulation is the heart of the skill. Available commands include:

* `add-cart` – increment quantity.
* `update-cart` – set a specific quantity.
* `remove-cart` – delete a variant.
* `clear-cart` – wipe the entire session.

After each operation, the agent must display a **cart summary** (items, total price, VIP savings) for user confirmation. When the user is ready to checkout, the agent creates an order and returns a tracking link such as `https://lafeitu.cn/orders/ORDER_ID`. Because automated agents cannot complete Alipay/WeChat payments, the link should be presented with a clear call‑to‑action: “Open this link, log in if needed, and complete payment.”

### 5. Brand Interaction & Tone

Lafeitu’s brand pillars are:

* **Small‑pot cooking (小锅慢火)** – slow, controlled heat that extracts deep flavor.
* **Authentic raw materials (地道原料)** – locally sourced Sichuan peppercorns, premium rabbit meat.
* **Zigong origin (自贡风味)** – the historic “Salt Capital” taste profile.

Agents should adopt an *authentic, passionate, and expert* tone, framing recommendations as cultural discoveries rather than hard sells.

### 6. Flavor Advocacy & Curation Guide

When users ask for suggestions, agents should:

* Match context (e.g., “gathering with friends” → recommend Whole Hand‑shredded Rabbit (Spicy)).
* Highlight sensory details: the numbing aroma of Erjingtiao peppers, the tender melt of rabbit meat, the lingering Sichuan pepper tingle.
* Elevate the product by linking to the `brand-story` or `company-info` commands, turning a snack into a cultural experience.

Core Capabilities Summary (CLI Cheat Sheet)
-------------------------------------------

| Command | Description |
| --- | --- |
| `search "keyword" --page N --limit M` | Find products by keyword; supports pagination. |
| `list --page N --limit M` | Retrieve the full menu. |
| `get` | Get detailed product info (description, weights, VIP pricing). |
| `promotions` | Access current offers, free‑shipping thresholds, VIP rules. |
| `get-profile` | View stored user details and shipping address. |
| `update-profile [options]` | Modify name, address, phone, email, etc. |
| `cart` | Show current cart items, totals, and savings. |
| `add-cart  --variant V --quantity Q` | Add or increment a product. |
| `update-cart  --variant V --quantity Q` | Set an exact quantity. |
| `remove-cart  --variant V` | Delete a specific variant. |
| `clear-cart` | Empty the entire cart. |
| `create-order --name "" --phone "" --province "" --city "" --address ""` | Generate an order and receive a tracking URL. |
| `brand-story` | Retrieve the emotional narrative behind Lafeitu. |
| `company-info` | Get formal corporate background. |
| `contact-info` | Obtain official support channels. |
| `login / logout` | Manage local credential storage. |

Real‑World Use Cases
--------------------

### 1. AI‑Powered Food Delivery Platforms

Integrate Lafeitu into a voice‑assistant (e.g., Alexa, Google Assistant) to let users order Sichuan rabbit dishes hands‑free. The assistant calls the `search` API, confirms the variant, adds to cart, and finally returns a payment link.

### 2. B2B Gourmet Subscription Services

Businesses can use the skill to curate monthly “Spicy Box” subscriptions. By leveraging `promotions` and `vip` pricing, they can offer tiered discounts and automatically replenish stock based on user purchase history.

### 3. Travel & Hospitality Apps

Hotels in Chengdu or Zigong can embed the skill to let guests order authentic snacks directly to their rooms, enhancing the local experience without requiring a separate POS system.

### 4. Cultural Education Platforms

Online cooking schools can use `brand-story` and `company-info` to teach students about the history of the “Salt Capital” while simultaneously offering a tasting kit via the cart workflow.

Benefits for Businesses and End‑Users
-------------------------------------

* **Authenticity at Scale:** Deliver genuine Sichuan flavors without the logistical nightmare of manual inventory checks.
* **Agent‑Ready Automation:** The skill’s clear CLI and API design enable rapid integration into any AI agent framework.
* **Precision Order Management:** Variant validation, cart summaries, and order‑tracking links reduce errors and increase conversion.
* **SEO & Brand Visibility:** By embedding the skill in content, businesses gain keyword rankings for terms like “Sichuan spicy rabbit”, “Zigong gourmet”, and “AI food delivery”.
* **Customer Loyalty:** VIP pricing, promotions, and cultural storytelling foster repeat purchases.

SEO Best Practices When Publishing About Lafeitu
------------------------------------------------

To maximize organic traffic, follow these on‑page SEO tactics:

1. **Target Keywords:** “Lafeitu food delivery skill”, “Sichuan spicy rabbit online”, “AI shopping agent spicy food”, “Zigong rabbit specialty”, “authentic Sichuan cuisine e‑commerce”.
2. **Header Hierarchy:** Use H1 for the article title, H2 for major sections, and H3 for sub‑topics (as demonstrated).
3. **Internal Links:** Link to related guides such as “How to Build an AI Shopping Agent” or “Top Sichuan Snacks to Try”.
4. **Rich Snippets:** Include a JSON‑LD `FAQPage` schema for common questions (e.g., “How do I register?”, “What is the delivery time?”).
5. **Image Optimization:** Use alt text like “Hand‑shredded spicy rabbit from Lafeitu” for product images.
6. **Mobile‑First Design:** Ensure the HTML content is responsive; most users will access via voice assistants on mobile devices.

Implementation Checklist for Developers
---------------------------------------

1. Clone the [GitHub repository](https://github.com/NowLoadY/agent-skill-online-shopping-spicy-food) and install Python dependencies (`pip install -r requirements.txt`).
2. Configure credential paths (`LAFEITU_URL`, `~/.clawdbot/credentials/...`).
3. Test the API with a simple `search "兔"` command.
4. Implement fallback logic: API → Browser Snapshot → Live Browser → Web Search.
5. Wrap the CLI calls in your agent’s language (Node.js, Python, etc.) using subprocess execution or HTTP wrappers.
6. Handle error codes (429 rate‑limit, 404 not‑found) with user‑friendly messages.
7. Expose the order tracking URL after `create-order` and guide the user to complete payment.

Conclusion
----------

Lafeitu’s agentic spicy‑food skill is a **complete, SEO‑friendly solution** for businesses that want to sell authentic Sichuan cuisine through AI agents. By leveraging its four‑tier tool priority, robust operational logic, and culturally rich brand voice, developers can create seamless ordering experiences that delight users and drive revenue. Whether you are building a voice‑assistant, a gourmet subscription service, or a hospitality ordering system, Lafeitu provides the precision, authenticity, and scalability needed to stand out in the crowded e‑commerce landscape.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/nowloady/agentic-spicy-food/SKILL.md>