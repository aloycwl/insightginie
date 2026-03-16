---
layout: post
title: "(2/50) Market Microstructure Basics &amp; Instruments"
date: 2025-09-22T13:24:31
categories: [11698]
original_url: https://insightginie.com/2-50-market-microstructure-basics-instruments
---

To understand how quantitative strategies operate in real markets, one must first understand **market microstructure**. Market microstructure is the study of how trading actually happens — the mechanics behind order execution, liquidity, and price formation.

Grasping these basics is essential for anyone building AI-driven or systematic trading strategies.

---

1. Orders and Order Types
-------------------------

Orders are the basic instructions traders give to exchanges or brokers.

* **Market Order:** Execute immediately at the best available price. Fast, but execution price is uncertain.
* **Limit Order:** Execute only at a specified price or better. Provides price control, but execution is not guaranteed.

👉 Together, these orders form the **limit order book (LOB)** — the engine of modern electronic markets.

---

2. Bid-Ask Spread
-----------------

* **Bid Price:** Highest price a buyer is willing to pay.
* **Ask Price:** Lowest price a seller is willing to accept.
* **Spread:** Difference between ask and bid.

The spread reflects **liquidity and transaction cost**. Tight spreads → high liquidity, wide spreads → low liquidity.

---

3. Latency
----------

Latency is the **time delay** between placing an order and seeing its effect in the market.

* Low latency = critical in high-frequency trading (HFT).
* Factors: network speed, matching engine performance, distance to exchange servers.

---

4. Venues
---------

Trading occurs across multiple venues:

* **Exchanges:** Centralized order books (e.g., NYSE, NASDAQ, Binance).
* **ECNs & Dark Pools:** Alternative trading systems with less transparency.
* **OTC (Over-the-Counter):** Direct deals between parties, common in FX.

---

5. Asset Types
--------------

Different asset classes trade with distinct microstructural features:

* **Equities:** Shares in companies, centralized exchanges dominate.
* **Futures:** Standardized contracts, leverage and expiry matter.
* **FX (Forex):** Decentralized market, OTC trading, extremely liquid.
* **Crypto:** 24/7 trading, highly fragmented across exchanges.

---

💻 Lab Exercise: Simulate a Limit Order Book Tick
------------------------------------------------

**Objective:** Understand how the order book updates with each trade.

### Steps:

1. Create a simple **limit order book (LOB)** with initial bid/ask prices and volumes.
2. Add incoming orders (market and limit).
3. Update the book after each tick (order event).
4. Visualize the **bid-ask spread changes** over time.

**Python Starter Code (simplified):**

```
import matplotlib.pyplot as plt

# Initial bid and ask prices
bid = 100.0
ask = 100.5
spread = ask - bid

bids, asks, spreads = [bid], [ask], [spread]

# Simulate 10 ticks
for i in range(10):
    if i % 2 == 0:  # buy pressure
        bid += 0.1
    else:  # sell pressure
        ask -= 0.1
    spread = max(0.01, ask - bid)  # spread can't be negative
    bids.append(bid)
    asks.append(ask)
    spreads.append(spread)

# Plot evolution
plt.plot(bids, label="Bid Price")
plt.plot(asks, label="Ask Price")
plt.plot(spreads, label="Spread")
plt.xlabel("Ticks")
plt.ylabel("Price")
plt.title("Limit Order Book Tick Simulation")
plt.legend()
plt.show()
```

### Expected Outcome:

* A visualization showing how **bid and ask prices** move as trades occur.
* The spread widening/narrowing depending on order flow.

---

Key Takeaways
-------------

* Market microstructure governs **execution quality, transaction cost, and slippage**.
* Understanding orders, spreads, latency, and venues is crucial for building realistic strategies.
* Simulating order book dynamics helps bridge theory with real market mechanics.