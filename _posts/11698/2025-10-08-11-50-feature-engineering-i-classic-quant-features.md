---
layout: post
title: "(11/50) Feature engineering I — classic quant features"
date: 2025-10-08T13:27:11
categories: [11698]
original_url: https://insightginie.com/11-50-feature-engineering-i-classic-quant-features
---

In the high-stakes world of quantitative finance and algorithmic trading, the difference between profit and loss often hinges on the quality of your data and, more specifically, the features you extract from it. Raw financial data, while abundant, rarely provides direct actionable insights. This is where **feature engineering** steps in—the art and science of transforming raw data into features that better represent the underlying problem to predictive models, thereby improving their accuracy and performance. For anyone serious about building robust trading strategies, understanding and implementing classic quantitative features is not just an advantage; it’s a fundamental requirement.

This deep dive will explore a foundational set of classic quant features—returns, log returns, moving averages, volatility, RSI, and MACD. We’ll discuss their theoretical underpinnings, practical applications, and touch upon their implementation, culminating in a conceptual lab where we’ll outline how to implement and backtest a simple momentum signal.

What is Feature Engineering in Quantitative Finance?
----------------------------------------------------

At its core, feature engineering in quantitative finance involves creating new variables from existing financial data that are more informative for a specific task, such as predicting price movements, identifying trends, or assessing risk. Imagine trying to predict stock prices using just the closing price. It’s difficult. But what if you knew the \*change\* in price, the \*average\* price over a week, or how \*volatile\* it has been? These derived metrics are features, and they provide a richer context for any predictive model, be it a simple rule-based system or a complex machine learning algorithm.

Effective feature engineering can:

* **Improve model performance:** By highlighting patterns that raw data obscures.
* **Reduce dimensionality:** Sometimes, well-engineered features can condense information from many raw data points into a few powerful ones.
* **Provide domain expertise:** Incorporating financial theory and market intuition into your data.
* **Increase interpretability:** Making it easier to understand why a model makes certain predictions.

The Building Blocks: Returns and Log Returns
--------------------------------------------

Before diving into more complex indicators, we must first understand the most fundamental measure of performance: returns.

### Returns (Simple Returns)

Simple returns measure the percentage change in an asset’s price over a period. They are intuitive and easy to calculate:

`R_t = (P_t - P_{t-1}) / P_{t-1}`

Where `P_t` is the price at time `t` and `P_{t-1}` is the price at time `t-1`. Simple returns are additive across assets in a portfolio (e.g., if you have 60% in Asset A and 40% in Asset B, your portfolio return is 0.6 \* R\_A + 0.4 \* R\_B).

### Log Returns (Continuously Compounded Returns)

Log returns are the natural logarithm of the price ratio:

`r_t = ln(P_t / P_{t-1})`

Log returns are particularly useful in quantitative finance for several reasons: they are additive across time (`ln(P_t / P_0) = ln(P_1 / P_0) + ln(P_2 / P_1) + ... + ln(P_t / P_{t-1})`), which simplifies calculations for multi-period returns and makes them suitable for statistical analysis where assumptions of normal distribution are often made (though financial returns are rarely truly normal). For short periods, simple and log returns are very similar, but they diverge for larger price changes.

Smoothing the Noise: Moving Averages (MAs)
------------------------------------------

Moving averages are among the most widely used technical indicators. They smooth out price data over a specified period, helping to identify trends and reduce the impact of random short-term fluctuations.

### Simple Moving Average (SMA)

The SMA is the unweighted average of a security’s price over a specified number of periods. For example, a 10-day SMA sums the closing prices of the past 10 days and divides by 10. SMAs are lagging indicators, meaning they reflect past price action and are best used to confirm trends rather than predict them.

### Exponential Moving Average (EMA)

The EMA gives more weight to recent prices, making it more responsive to new information than the SMA. Because of its responsiveness, the EMA is often preferred by traders looking for quicker signals. The calculation involves a smoothing factor that decreases exponentially for older data points.

Both SMAs and EMAs are invaluable for identifying support and resistance levels, as well as generating crossover signals (e.g., a short-term MA crossing above a long-term MA often signals an uptrend).

Measuring Risk: Volatility
--------------------------

Volatility is a measure of the dispersion of returns for a given security or market index. It quantifies the degree of variation of a trading price series over time. High volatility means prices can change dramatically over a short period, while low volatility suggests prices are relatively stable.

The most common way to calculate volatility is by taking the standard deviation of returns over a specific period (e.g., daily, weekly, monthly). Annualized volatility is often used for comparison purposes. Volatility is a critical input for risk management, option pricing (e.g., Black-Scholes model), and understanding the risk-adjusted returns of an asset.

Oscillators for Momentum and Reversal: RSI and MACD
---------------------------------------------------

Oscillators are technical analysis tools that fluctuate between a minimum and maximum value, typically plotted above or below a price chart. They are used to identify overbought or oversold conditions and potential trend reversals.

### Relative Strength Index (RSI)

The RSI is a momentum oscillator that measures the speed and change of price movements. It oscillates between 0 and 100. Traditionally, an asset is considered overbought when the RSI is above 70 and oversold when it is below 30. Divergences between price and RSI can also signal potential trend reversals.

The basic calculation involves averaging gains and losses over a period (commonly 14 periods) to create an initial RSI, then smoothing it. The formula is: `RSI = 100 - [100 / (1 + RS)]`, where RS is the average gain / average loss.

### Moving Average Convergence Divergence (MACD)

The MACD is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. It is calculated by subtracting the 26-period EMA from the 12-period EMA. The result is the MACD line. A nine-period EMA of the MACD line, known as the ‘signal line,’ is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals. The MACD histogram, which plots the difference between the MACD line and its signal line, provides further insight into momentum.

Traders look for crossovers of the MACD line and the signal line, as well as divergences between the MACD and price, to identify potential trading opportunities.

Bringing It All Together: A Simple Momentum Strategy
----------------------------------------------------

Now that we’ve covered these classic features, let’s consider how they might be combined into a simple trading strategy. A common approach in quantitative finance is to exploit *momentum*, the tendency for assets that have performed well recently to continue performing well, and vice-versa.

Consider a basic momentum strategy:

* **Entry Signal:** Buy (go long) an asset if its current price is above its 200-day Simple Moving Average (SMA), \*and\* its 14-day Relative Strength Index (RSI) is above 50 (indicating bullish momentum).
* **Exit Signal:** Sell (close position) if the price falls below the 200-day SMA, \*or\* the RSI drops below 30 (indicating oversold conditions or loss of momentum).

This simple strategy combines a long-term trend filter (200-day SMA) with a short-term momentum confirmation (RSI). The use of both helps filter out false signals that might arise from using a single indicator.

Lab: Implement and Backtest Simple Momentum Signal
--------------------------------------------------

Implementing and backtesting such a strategy is crucial to assess its viability. This practical lab would typically involve the following steps using a programming language like Python:

1. **Data Acquisition:** Obtain historical price data (e.g., daily closing prices) for your chosen asset(s) from a reliable source (e.g., Yahoo Finance, Quandl, proprietary data feeds).
2. **Feature Calculation:**
   * Calculate daily returns and log returns.
   * Compute 200-day SMA.
   * Compute 14-day RSI.
   * (Optional: calculate MACD for further exploration).
3. **Strategy Logic Implementation:** Write code to apply the entry and exit rules described above. This involves iterating through your historical data, checking the conditions for each day, and recording simulated trades.
4. **Backtesting Framework:** Develop or use an existing backtesting library (e.g., `backtrader`, `zipline` in Python, or a custom script) to simulate trades based on your signals.
   * Track portfolio value, cash, and positions over time.
   * Account for transaction costs (commissions, slippage).
5. **Performance Evaluation:** Analyze key metrics from your backtest:
   * Total Return
   * Annualized Return
   * Maximum Drawdown
   * Sharpe Ratio (risk-adjusted return)
   * Win Rate, Profit Factor
6. **Optimization & Robustness Testing:** Experiment with different parameter values (e.g., 150-day SMA, RSI 60/40) and test the strategy across various assets and market conditions to check its robustness.

This iterative process of implementation and backtesting allows you to refine your strategy, understand its strengths and weaknesses, and build confidence before considering live deployment.

Why These Features Matter for Machine Learning
----------------------------------------------

While we’ve discussed these features in the context of rule-based strategies, their true power extends to machine learning. Instead of explicitly defining ‘buy’ or ‘sell’ rules, you can feed these engineered features (returns, MAs, volatility, RSI, MACD values) into a machine learning model (e.g., a Random Forest, Gradient Boosting Machine, or even a Neural Network). The model can then learn complex, non-linear relationships between these features and future price movements or labels (e.g., ‘price goes up tomorrow’, ‘price goes down tomorrow’).

These classic quant features serve as excellent inputs because they already capture crucial aspects of market behavior—trend, momentum, and risk—in a way that raw price data cannot. They provide the necessary context for algorithms to identify patterns and make more informed predictions.

Conclusion
----------

Feature engineering is an indispensable skill for anyone aspiring to excel in quantitative finance and algorithmic trading. By mastering classic quant features like returns, log returns, moving averages, volatility, RSI, and MACD, you equip yourself with the fundamental tools to transform raw financial data into meaningful insights. These features not only form the backbone of many successful rule-based trading strategies but also serve as powerful inputs for advanced machine learning models. The journey from understanding these concepts to implementing and rigorously backtesting them is where theoretical knowledge truly translates into practical edge in the financial markets. Continue to explore, experiment, and refine your feature engineering prowess—it’s a continuous process of learning and adaptation in the ever-evolving world of finance.