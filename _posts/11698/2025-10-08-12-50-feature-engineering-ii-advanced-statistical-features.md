---
layout: post
title: "(12/50) Feature engineering II — advanced statistical features"
date: 2025-10-08T13:27:17
categories: [11698]
original_url: https://insightginie.com/12-50-feature-engineering-ii-advanced-statistical-features
---

In the rapidly evolving landscape of machine learning, the quality of your features often dictates the performance ceiling of your models. While basic feature engineering might suffice for tabular data, time series data presents a unique set of challenges and opportunities. Its inherent temporal dependence requires a more sophisticated approach. This article, “Feature Engineering II,” delves into advanced statistical techniques that transform raw time series into powerful predictive signals, moving beyond simple lags to uncover deeper, more meaningful relationships.

If you’re looking to build high-performing models for forecasting, anomaly detection, or quantitative finance, understanding concepts like autocorrelation, stationarity, cointegration, and pairs features isn’t just beneficial—it’s essential. These advanced statistical tools empower data scientists and machine learning engineers to extract nuanced information that standard methods often miss, leading to more robust and accurate predictions.

Understanding Time Series Dependence: Autocorrelation and Partial Autocorrelation
---------------------------------------------------------------------------------

Time series data is characterized by its sequential nature, meaning that observations are not independent. The value at any given time point is often correlated with past values. This temporal dependence is precisely what advanced statistical features aim to capture.

### Autocorrelation Function (ACF)

The **Autocorrelation Function (ACF)** measures the linear relationship between an observation at time *t* and observations at previous time steps (*t-1, t-2, …*). In simpler terms, it tells you how much a series is correlated with its own past values at different lags. An ACF plot displays these correlation coefficients against the lag number. A significant spike at a particular lag indicates a strong correlation with values from that past period, often revealing seasonality or trends.

* **Interpretation:** If the ACF decays slowly, it often suggests a trend. Significant spikes at specific lags (e.g., 12 for monthly data) indicate seasonality.
* **Feature Use:** Lags with high ACF values can be directly used as features in predictive models, capturing the persistence or cyclical patterns in the data.

### Partial Autocorrelation Function (PACF)

While ACF measures the total correlation, the **Partial Autocorrelation Function (PACF)** measures the linear relationship between an observation at time *t* and an observation at a previous time step (*t-k*), *after removing the effects of all intermediate observations (t-1, t-2, …, t-k+1)*. It isolates the direct correlation between two points, stripping away indirect correlations that pass through intermediate lags.

* **Interpretation:** A significant spike at lag *k* in the PACF plot, followed by insignificant values, suggests a direct relationship at lag *k*.
* **Feature Use:** PACF helps identify the “true” lag dependencies, which are crucial for building autoregressive (AR) components in models or for selecting direct lag features.

Both ACF and PACF plots are indispensable tools for understanding the internal structure of a time series, guiding the selection of appropriate lag features, and informing model choices like ARIMA parameters.

Stationarity: The Cornerstone of Reliable Time Series Analysis
--------------------------------------------------------------

One of the most critical concepts in time series analysis is **stationarity**. A time series is considered stationary if its statistical properties—mean, variance, and autocorrelation structure—do not change over time. In essence, a stationary series looks the same regardless of when you observe it.

Why is stationarity so important? Many statistical models, particularly those based on regression, assume that the underlying data generating process is constant. Non-stationary series can lead to spurious regressions, where two unrelated series appear to be correlated simply because they share a common trend. For machine learning models, non-stationarity can make it difficult for algorithms to learn stable patterns, often leading to poor generalization on unseen data.

### Stationarity Tests: Proving Constancy

Visual inspection of a time series plot can give hints about stationarity (e.g., a clear trend or changing variance). However, formal statistical tests are required for robust confirmation. Here are two widely used tests:

#### Augmented Dickey-Fuller (ADF) Test

The **Augmented Dickey-Fuller (ADF) test** is a popular statistical test used to determine if a unit root is present in a time series, which would indicate non-stationarity. The null hypothesis (H₀) of the ADF test is that the time series has a unit root (i.e., it is non-stationary). The alternative hypothesis (H₁) is that the series is stationary.

* **Interpretation:** If the p-value is less than a chosen significance level (e.g., 0.05), we reject the null hypothesis and conclude that the series is likely stationary. A higher test statistic (more negative) compared to critical values also suggests stationarity.

#### KPSS Test (Kwiatkowski–Phillips–Schmidt–Shin Test)

The **KPSS test** offers a complementary perspective to the ADF test. Unlike ADF, the null hypothesis (H₀) of the KPSS test is that the time series is stationary around a deterministic trend (or mean). The alternative hypothesis (H₁) is that the series is non-stationary due to the presence of a unit root.

* **Interpretation:** If the p-value is less than the significance level, we reject the null hypothesis and conclude that the series is non-stationary. If the p-value is greater, we fail to reject the null, suggesting stationarity.

Using both ADF and KPSS tests together provides a more robust assessment. For instance, if ADF rejects non-stationarity and KPSS fails to reject stationarity, you have strong evidence of stationarity. If both tests contradict, further investigation or transformation might be needed.

### Making a Series Stationary: Transformations

If a series is found to be non-stationary, it can often be transformed into a stationary one. Common techniques include:

* **Differencing:** Subtracting the observation at the previous time step from the current observation (e.g., `Y_t = X_t - X_{t-1}`). This removes trends. Seasonal differencing removes seasonal components.
* **Log Transformation:** Applying a logarithm to the series can stabilize variance when the variance increases with the mean.
* **Detrending:** Subtracting a fitted trend line (e.g., from a linear regression) from the series.

The resulting stationary series or its differenced values can then be used as powerful features in your models.

Cointegration: The Long-Term Dance of Non-Stationary Series
-----------------------------------------------------------

While differencing helps achieve stationarity, it can sometimes lead to a loss of long-term information. This is where **cointegration** comes into play. Cointegration describes a scenario where two or more non-stationary time series have a long-term, stable linear relationship, even though each series individually is non-stationary.

Imagine two random walks. Individually, they wander aimlessly. But if they are cointegrated, the difference (or “spread”) between them will be stationary. This implies that they cannot drift too far apart from each other over extended periods; they are “bound” together in some equilibrium.

For data scientists, cointegration is a powerful concept because it allows us to leverage relationships between non-stationary series without losing the long-term information that differencing might discard. It’s particularly valuable in financial applications.

Tests like the Engle-Granger two-step procedure or the Johansen test can formally assess cointegration between series. If a set of series is cointegrated, the stationary linear combination (the spread) can be a highly informative feature.

Pairs Features: Capitalizing on Cointegration for Predictive Power
------------------------------------------------------------------

Building directly on the concept of cointegration, **pairs features** involve creating new features by combining two or more related time series, especially those found to be cointegrated. The most common form of a pair feature is the *spread* between two series.

Consider two stock prices that are cointegrated. While each stock price might be non-stationary, their difference (Stock A Price – Stock B Price) will be stationary. This stationary spread can be an incredibly powerful feature for several reasons:

* **Mean Reversion:** A stationary spread tends to revert to its mean. When the spread deviates significantly from its historical average, it suggests one asset is temporarily overvalued or undervalued relative to the other.
* **Relative Value:** It captures the relative performance and relationship between the two assets, rather than their absolute price movements.
* **Signal Generation:** Deviations from the mean of the spread can act as strong signals for trading strategies (e.g., “pairs trading”) or for predicting future relative movements.

Beyond simple differences, pairs features can also involve ratios or more complex linear combinations. The key is that the resulting feature captures a stable, long-term relationship that is often hidden when analyzing individual series in isolation. These features can significantly enhance models predicting relative performance, risk, or arbitrage opportunities.

Integrating Advanced Features into Machine Learning Models
----------------------------------------------------------

The ultimate goal of feature engineering is to create variables that improve your machine learning model’s performance. Here’s how these advanced statistical features can be integrated:

* **Autocorrelation/PACF Lags:** Identify significant lags from ACF/PACF plots and create new features representing the series’ values at those specific lags. For example, `series_t-1`, `series_t-12`.
* **Stationary Transformations:** Instead of using the raw non-stationary series, input its differenced or log-transformed stationary version into your model. This helps models like linear regressions or neural networks assume stable statistical properties.
* **Cointegrated Spreads:** If you have two cointegrated series (e.g., `Asset A` and `Asset B`), create a new feature `Spread = Asset A - Asset B`. This stationary spread provides a direct measure of their long-term equilibrium and deviations from it.
* **Rolling Statistics on Features:** Apply rolling means, standard deviations, or other statistics to these newly created features to capture their short-term dynamics.

By providing models with features that explicitly capture temporal dependencies, stationarity, and long-term relationships, you equip them with a deeper understanding of the underlying data generation process. This leads to more accurate predictions, more robust models, and often, better interpretability.

Practical Considerations and Best Practices
-------------------------------------------

While powerful, applying these advanced techniques requires careful consideration:

* **Domain Knowledge:** Always combine statistical insights with domain expertise. Understanding the real-world processes generating your time series data can guide your feature engineering choices.
* **Feature Selection:** Not all statistically significant features will be useful for your model. Use techniques like feature importance, recursive feature elimination, or permutation importance to select the most impactful features.
* **Avoiding Look-Ahead Bias:** When creating lag features or performing transformations, ensure you are only using past data. Never use future information that wouldn’t be available at the time of prediction. This is critical for time series forecasting.
* **Computational Cost:** Some tests (e.g., Johansen cointegration) can be computationally intensive for very large datasets.

Conclusion
----------

Advanced statistical feature engineering is not merely an enhancement; it’s a fundamental shift in how we approach time series data for machine learning. By mastering autocorrelation, stationarity tests, cointegration, and pairs features, you gain the ability to extract nuanced, stable, and highly predictive signals from even the most complex temporal datasets.

These techniques move beyond superficial analysis, allowing your models to capture the true underlying dynamics and long-term relationships that govern time series. Incorporating these features will undoubtedly elevate your predictive models, leading to more accurate forecasts, insightful analyses, and ultimately, a significant competitive edge in fields ranging from finance to energy and beyond. Start experimenting with these powerful tools today and unlock the full potential of your time series data!