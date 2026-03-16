---
layout: post
title: "Otterline Sports Predictions Skill: Free NBA and NHL Betting Picks"
date: 2026-03-09T14:18:42
categories: [24854]
original_url: https://insightginie.com/otterline-sports-predictions-skill-free-nba-and-nhl-betting-picks
---

What is the Otterline Sports Predictions Skill?
-----------------------------------------------

The Otterline skill is a specialized OpenClaw skill that provides free daily sports betting predictions and picks for NBA and NHL games. This skill leverages Otterline's AI consensus model to deliver confidence-tiered betting recommendations without requiring any API key or authentication.

### Key Features of the Otterline Skill

The Otterline skill offers several valuable features for sports betting enthusiasts:

* **Free Daily Predictions**: Access to free NBA and NHL moneyline winners every day
* **Confidence Tiers**: Picks are categorized by confidence levels from Elite to Lean
* **No Authentication Required**: Simply call the endpoints without API keys
* **Live Data**: Real-time predictions updated daily
* **Entertainment Focus**: Designed for entertainment purposes with responsible gambling messaging

How to Access Otterline Predictions
-----------------------------------

The Otterline skill provides two main endpoints for accessing free sports betting picks:

### NBA Predictions Endpoint

Fetch free NBA sample picks using:

```
curl -s "https://gvwawacjgghesljfzbph.supabase.co/functions/v1/free-nba-picks"
```

You can also specify a particular date:

```
curl -s "https://gvwawacjgghesljfzbph.supabase.co/functions/v1/free-nba-picks?date=2026-02-05"
```

### NHL Predictions Endpoint

Fetch free NHL sample picks using:

```
curl -s "https://gvwawacjgghesljfzbph.supabase.co/functions/v1/free-nhl-picks"
```

With optional date parameter:

```
curl -s "https://gvwawacjgghesljfzbph.supabase.co/functions/v1/free-nhl-picks?date=2026-02-05"
```

Understanding the Prediction Data Structure
-------------------------------------------

Both NBA and NHL endpoints return JSON data with consistent structure. Here's what you'll receive:

### Top-Level Response Fields

* `type`: Always “FREE SAMPLE”
* `notice`: Information about how many picks are shown
* `league`: “NBA” or “NHL”
* `date`: The date for the predictions (YYYY-MM-DD)
* `model`: Information about the prediction model
* `picks`: Array of individual game predictions
* `no_games`: Boolean indicating if there are games that day
* `upgrade_url`: Link to premium picks
* `upgrade_message`: Promotional message for premium service
* `full_picks_url`: URL for complete picks
* `generated_at`: Timestamp when predictions were generated

### Pick Object Structure

Each pick contains specific fields depending on the league:

#### NBA Pick Fields

* `matchup`: Game matchup description
* `pick`: Selected team to win
* `tier`: Confidence level (elite, verified, strong, pass)
* `consensus_count`: Number of models agreeing (typically 1-3)
* `combo_win_rate`: Combined win rate percentage
* `start_time`: Game start time (may be null)

#### NHL Pick Fields

* `matchup`: Game matchup description
* `pick`: Selected team to win
* `tier`: Confidence level (elite, verified, strong, lean)
* `score`: Numerical score value
* `moneyPuckWinProb`: Moneyline win probability percentage
* `models`: Internal model data (never shown to users)

Confidence Tier System
----------------------

Otterline uses a tiered confidence system to categorize predictions:

### NBA Tiers

* **Elite**: Highest confidence picks with strong consensus
* **Verified**: Well-supported predictions with good model agreement
* **Strong**: Solid picks with moderate confidence
* **Pass**: No recommended bet for this game

### NHL Tiers

* **Elite**: Top confidence predictions
* **Verified**: Reliable picks with good support
* **Strong**: Confident recommendations
* **Lean**: Slight edge picks with lower confidence

How to Present Predictions to Users
-----------------------------------

When using the Otterline skill to display predictions, follow these guidelines:

### Display Format

Always fetch fresh data from the endpoints rather than caching predictions. Present the information with clear headers, proper tier categorization, and include the Otterline branding and disclaimer.

### Sample Output Structure

A typical presentation would include:

* Header with league, date, and “free sample” designation
* Notice about how many picks are shown
* Tier-organized picks with appropriate confidence indicators
* Win rate or probability statistics where available
* Premium upgrade offer
* Otterline attribution and responsible gambling disclaimer

Common User Queries and Responses
---------------------------------

The Otterline skill can handle various user requests:

### Today's Picks

When users ask for today's picks, fetch both NBA and NHL predictions and present both leagues with clear labeling.

### Elite Picks Only

For users seeking only the highest confidence picks, filter the predictions to show only elite tier selections.

### Future Date Requests

Users can request picks for specific dates using the date parameter in the API call.

### League-Specific Requests

Handle requests for “Just NBA” or “Just NHL” by fetching only the requested league's predictions.

### Premium Information

When users ask about getting more picks or full analysis, direct them to the premium service at otterline.club/premium.

Important Considerations
------------------------

Several key points should be noted when using the Otterline skill:

* The endpoints return free samples and may show fewer than 4 picks
* If no games are scheduled, display the appropriate message
* Always include the responsible gambling disclaimer
* Never show internal model data to users
* Convert game times to the user's local timezone when displaying
* The service is for entertainment purposes only

Premium Features
----------------

While the skill provides free daily samples, full daily pick slates with complete analysis are available through Otterline's premium service at [otterline.club/premium](https://otterline.club/premium).

Responsible Gambling
--------------------

Always include the disclaimer: “For entertainment only; bet responsibly.” The Otterline skill is designed for informational and entertainment purposes, not as financial advice.

Conclusion
----------

The Otterline skill provides a valuable service for sports betting enthusiasts by offering free, AI-powered predictions for NBA and NHL games. With its confidence-tiered system, real-time data, and user-friendly presentation, it serves as an excellent tool for those interested in sports betting while emphasizing responsible gambling practices.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/chrislyonshfx/otterline/SKILL.md>