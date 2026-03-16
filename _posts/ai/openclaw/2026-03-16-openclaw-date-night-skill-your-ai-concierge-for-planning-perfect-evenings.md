---
layout: post
title: "OpenClaw Date Night Skill: Your AI Concierge for Planning Perfect Evenings"
date: 2026-03-16T05:16:17
categories: [24854]
original_url: https://insightginie.com/openclaw-date-night-skill-your-ai-concierge-for-planning-perfect-evenings
---

What the Date Night Skill Does
------------------------------

The Date Night skill is your personal AI concierge that handles every aspect of planning an evening out. This skill transforms casual requests like “plan a date night” into complete, coordinated experiences using browser automation. It manages restaurant reservations through OpenTable and Resy, books movie tickets via Fandango, Megaplex, and AMC, finds and compares event tickets across SeatGeek, Ticketmaster, and StubHub, checks weather conditions, estimates drive times, calculates total budgets including babysitter rates, creates calendar events, and even notifies your partner about plans.

Getting Started: First-Time Onboarding
--------------------------------------

The first time you use the Date Night skill, it runs a friendly onboarding process to personalize your experience. When you invoke the skill initially, it asks about your name, email, and phone number for reservation forms, whether you're planning with a partner (and their name), preferred notification channels for partner updates, dietary restrictions, childcare needs, location, favorite movie theaters, babysitter rates, and calendar management tools. This information is stored locally in `~/.openclaw/skills/date-night/config.json` and never transmitted except during actual booking form submissions.

Core Features and Capabilities
------------------------------

The skill excels at end-to-end planning through several key capabilities. For dining, it searches nearby restaurants based on your location and dietary preferences, handles reservation requests, and can modify or cancel bookings when needed. For entertainment, it finds current movie showtimes at your preferred theaters, books tickets across major chains, and searches for concerts, sports events, and local activities with price comparisons across multiple ticketing platforms.

Beyond bookings, the skill manages logistics by checking weather forecasts for your planned date, estimating drive times between locations, calculating total costs including your specified babysitter rate, and adding events to your calendar using your preferred tool (Google, iCal, or other). It also handles partner communication by drafting notifications for approval before sending, ensuring you maintain control over what gets shared.

Privacy and Data Handling
-------------------------

Your personal information stays local and secure. The skill stores your name, email, phone number, and preferences only in the configuration file on your machine. These details are used solely for auto-filling booking forms and are never transmitted except directly to the booking websites during form submission. For SMS verification during reservations, the skill can read only the most recent relevant messages from known booking service short codes, and only when actively processing a reservation.

Configuration and Customization
-------------------------------

The skill offers extensive customization options. You can specify dietary preferences like vegetarian, no alcohol, or gluten-free, which filter restaurant recommendations. If you have children, you can set the number of kids, their ages, and your babysitter rate for accurate budget calculations. Your location and zip code help find nearby venues, while your preferred theater chain ensures movie searches default to your favorite spots. The calendar integration supports multiple tools, and notification preferences include iMessage, Telegram, Discord, Signal, or SMS.

Technical Implementation
------------------------

Built on playwright-cli browser automation, the skill interacts with real booking websites just as a human would, navigating forms, selecting options, and completing transactions. It maintains local browser session cookies for services like Resy (with opt-in storage) and keeps a history log of past date nights. The skill uses various tools including web search, web fetch, Google Places API for location data, and messaging integrations for partner notifications.

Available Commands and Triggers
-------------------------------

You can invoke the skill with natural language requests like “plan a date night,” “find us a restaurant,” “get us movie tickets,” “book a table at [restaurant],” “what's playing near me,” “find concert tickets,” or “cancel our reservation.” The skill understands context and can modify existing plans or reconfigure preferences as needed. It also supports autonomous operation for partner notifications when configured, always drafting messages for your approval before sending.

Why Use the Date Night Skill
----------------------------

This skill eliminates the hassle of coordinating multiple booking platforms, comparing prices across ticketing sites, and managing logistics for a night out. It transforms what could be hours of research and form-filling into a simple conversation, letting you focus on enjoying your evening rather than planning it. Whether you're organizing a romantic dinner, a movie night, or a full evening of activities, the Date Night skill handles the details while keeping your personal information private and secure.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/tdavis009/date-night/SKILL.md>