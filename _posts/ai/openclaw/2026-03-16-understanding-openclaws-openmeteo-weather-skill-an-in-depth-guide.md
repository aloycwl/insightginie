---
layout: post
title: "Understanding OpenClaw&#8217;s OpenMeteo Weather Skill: An In-Depth Guide"
date: 2026-03-16T08:46:14
categories: [24854]
original_url: https://insightginie.com/understanding-openclaws-openmeteo-weather-skill-an-in-depth-guide
---

Understanding OpenClaw's OpenMeteo Weather Skill: An In-Depth Guide

Understanding OpenClaw's OpenMeteo Weather Skill: An In-Depth Guide
===================================================================

Introduction
------------

Welcome to the comprehensive guide on OpenClaw's OpenMeteo Weather skill! This skill is a powerful tool designed for fetching current weather, hourly forecasts, and daily forecasts for any city or coordinates around the world. It leverages the free Open-Meteo API, making it an excellent choice for developers and users who need reliable weather data without the hassle of API keys.

This article will dive deep into the functionalities, usage, and practical examples of the OpenMeteo Weather skill. Whether you're a developer, a tech enthusiast, or just someone curious about how to integrate weather data into your projects, this guide is for you.

What is OpenMeteo Weather Skill?
--------------------------------

The OpenMeteo Weather skill is a part of the OpenClaw project, which is hosted on GitHub. This skill allows users to get detailed weather information for any location worldwide using the Open-Meteo API. The best part? It doesn't require an API key, making it hassle-free to use.

Here's a quick overview of what you can do with this skill:

* Fetch current weather conditions for any city or coordinates.
* Get hourly weather forecasts.
* Obtain daily weather forecasts.
* Check specific weather parameters like temperature, rain, snow, wind, sunrise/sunset, UV, humidity, pressure, etc.
* Determine if you need an umbrella based on precipitation data.

Prerequisites and Requirements
------------------------------

Before you can start using the OpenMeteo Weather skill, ensure you have the following:

* Access to a terminal or command-line interface.
* Bash installed on your system.
* The required bins: curl and jq (for JSON processing).
* The OpenClaw skill repository cloned on your machine.

You can install the required bins using the following commands:

```
sudo apt-get update
```

```
sudo apt-get install curl jq
```

Using the OpenMeteo Weather Skill
---------------------------------

The OpenMeteo Weather skill can be used via the command-line interface (CLI). Here's the basic syntax:

```
bash {baseDir}/scripts/weather.sh [options]
```

replace `{baseDir}` with the directory where the OpenClaw skills repository is cloned.

Quick Reference
---------------

Here are some quick examples to help you get started:

* **Current Weather:**
* `bash {baseDir}/scripts/weather.sh --current --city=Berlin`
* `bash {baseDir}/scripts/weather.sh --current --city=London`
* `bash {baseDir}/scripts/weather.sh --current --lat=48.8566 --lon=2.3522`
* **Disambiguate with –country:**
* `bash {baseDir}/scripts/weather.sh --current --city=Portland --country=US`
* **Forecast:**
* `bash {baseDir}/scripts/weather.sh --forecast-days=3 --city=Paris`
* **Both Current + Forecast:**
* `bash {baseDir}/scripts/weather.sh --current --forecast-days=2 --city=Rome`
* **Custom Params:**
* `bash {baseDir}/scripts/weather.sh --forecast-days=2 --city=Vienna  
  --hourly-params=precipitation,precipitation_probability,weather_code`

Options
-------

The OpenMeteo Weather skill offers a variety of options to customize your weather data requests. Here's a detailed breakdown of the available options:

### Location Options

**–city=NAME** — Specify the city name for which you want to fetch weather data. The city name is auto-geocoded, so it's usually sufficient on its own.

**–country=…** — An optional country hint to disambiguate city names. This can be any format (e.g., GB, France, Ger). It's only needed when the city name is ambiguous (e.g., Portland, US vs. Portland, UK).

**–lat=FLOAT –lon=FLOAT** — Direct coordinates for precision. If you have the exact latitude and longitude, you can bypass the geocoding process by using these options.

### Mode Options

**–current** — Fetch current weather conditions.

**–forecast** — Fetch hourly and daily forecasts.

**–forecast-days=N** — Specify the forecast length in days (1–16 days, default: 7; implies –forecast).

### Param Overrides

**–current-params=…** — Override current weather variables. Use comma-separated variable names.

**–hourly-params=…** — Override hourly forecast variables. Use comma-separated variable names.

**–daily-params=…** — Override daily forecast variables. Use comma-separated variable names.

### Output Options

**–human** — Emoji-rich formatted output for humans (default is porcelain, optimized for agents).

Available API Variables
-----------------------

The OpenMeteo Weather skill supports a wide range of weather variables. Here's a list of available variables that you can override using the param override options:

### Current & Hourly Variables

* **temperature\_2m** (default) — Air temperature at 2m, °C.
* **apparent\_temperature** (default) — Feels-like temperature, °C.
* **relative\_humidity\_2m** (default) — Relative humidity at 2m, %.
* **precipitation** (default) — Total precipitation (rain + showers + snow), mm.
* **precipitation\_probability** (default, hourly only) — Probability of precipitation, %.
* **weather\_code** (default) — Weather condition, auto-resolved to text in output.
* **wind\_speed\_10m** (default) — Wind speed at 10m, km/h.
* **wind\_gusts\_10m** — Wind gust speed at 10m, km/h.
* **wind\_direction\_10m** — Wind direction, °.
* **cloud\_cover** (default, current only) — Total cloud cover, %.
* **is\_day** (default, current only) — Daytime flag, 0/1.
* **pressure\_msl** — Sea-level atmospheric pressure, hPa.
* **surface\_pressure** — Surface pressure, hPa.
* **visibility** — Visibility distance, m.
* **rain** — Rain only (no showers/snow), mm.
* **showers** — Shower rain only, mm.
* **snowfall** — Snowfall amount, cm.
* **snow\_depth** — Snow depth on the ground, m.
* **dew\_point\_2m** — Dew point temperature at 2m, °C.
* **uv\_index** (hourly only) — UV index.

### Daily Variables

* **temperature\_2m\_max** (default) — Daily max temperature, °C.
* **temperature\_2m\_min** (default) — Daily min temperature, °C.
* **precipitation\_sum** (default) — Total daily precipitation, mm.
* **precipitation\_probability\_max** (default) — Max precipitation probability, %.
* **weather\_code** (default) — Dominant weather condition for the day.
* **wind\_speed\_10m\_max** (default) — Max wind speed, km/h.
* **wind\_gusts\_10m\_max** — Max wind gust speed, km/h.
* **wind\_direction\_10m\_dominant** — Dominant wind direction, °.
* **sunrise** — Sunrise time, ISO 8601.
* **sunset** — Sunset time, ISO 8601.
* **daylight\_duration** — Daylight duration, seconds.
* **sunshine\_duration** — Sunshine duration, seconds.
* **precipitation\_hours** — Hours with precipitation.
* **rain\_sum** — Total daily rain, mm.
* **showers\_sum** — Total daily showers, mm.
* **snowfall\_sum** — Total daily snowfall, cm.
* **uv\_index\_max** — Max UV index.
* **apparent\_temperature\_max** — Daily max feels-like, °C.
* **apparent\_temperature\_min** — Daily min feels-like, °C.

Conversational Examples
-----------------------

Here are some practical examples of how you can use the OpenMeteo Weather skill in a conversational context:

### Example 1: General Weather Overview

**User:**

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/lstpsche/openmeteo-weather/SKILL.md>