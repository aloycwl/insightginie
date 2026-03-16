---
layout: post
title: "OpenClaw Camino Places Skill: Flexible Geocoding and Place Lookup"
date: 2026-03-09T01:19:26
categories: [24854]
original_url: https://insightginie.com/openclaw-camino-places-skill-flexible-geocoding-and-place-lookup
---

Introduction to Camino Places Skill
-----------------------------------

The Camino Places skill is a powerful tool within the OpenClaw ecosystem that enables flexible place lookup and geocoding capabilities. Whether you need to find the coordinates of a famous landmark, geocode an address, or discover places within a specific area, this skill provides comprehensive location intelligence through both free-form queries and structured address components.

Core Functionality
------------------

The Places skill serves as a flexible place lookup system that can handle multiple input formats. You can search for locations using natural language queries like “Eiffel Tower” or provide structured address components such as street name, city, state, and country. This dual approach makes the skill versatile for various use cases, from finding tourist attractions to geocoding business addresses.

The skill returns essential information including geographic coordinates (latitude and longitude), formatted addresses, place types, and importantly, can optionally provide street-level photos to give visual context to the locations found.

Installation and Setup
----------------------

Installing the Camino Places skill is straightforward through multiple methods. You can install it as part of the complete Camino AI location intelligence suite using the command `npx skills add https://github.com/barneyjm/camino-skills`, or install it individually with `npx skills add https://github.com/barneyjm/camino-skills --skill places`.

For those using clawhub, installation is even simpler with `npx clawhub@latest install places`. Once installed, you'll need to configure your API key. You can start with a free trial that provides 25 calls without signup, or sign up at <https://app.getcamino.ai/skills/activate> for 1,000 free calls per month.

Key Features and Capabilities
-----------------------------

The Places skill offers several powerful features that make it stand out. Unlike the Query skill which uses AI ranking for natural language searches, Places focuses on precise geocoding and location lookup. It can return coordinates for any address or place name, making it ideal for applications that need exact geographic positioning.

One of the most valuable features is the optional street-level photo capability. When enabled, the skill can provide imagery from around the searched location, giving users visual confirmation and context. This is particularly useful for real estate applications, travel planning, or any scenario where seeing the actual location matters.

Usage Examples
--------------

The skill supports various usage patterns through both shell scripts and direct API calls. For simple landmark searches, you can use commands like `./scripts/places.sh '{"query": "Eiffel Tower"}'`. For more complex searches with photos, try `./scripts/places.sh '{"query": "Empire State Building", "include_photos": true}'`.

Structured address searches work equally well: `./scripts/places.sh '{"street": "1600 Pennsylvania Avenue", "city": "Washington", "state": "DC", "country": "USA"}'`. You can also search by city alone or combine multiple address components for more accurate results.

Parameters and Configuration
----------------------------

The skill offers extensive configuration options through its parameters. You can specify the query type, address components (street, city, state, country, postal code), and control the number of results with the limit parameter. The include\_photos parameter enables or disables street-level imagery, while photo\_radius controls the search area for photos in meters.

For more comprehensive searches, the mode parameter allows switching between “basic” and “advanced” search depths. The advanced mode provides richer data by leveraging web-enriched place information, making it ideal for applications that need detailed location intelligence.

Response Format and Data Structure
----------------------------------

Responses from the Places skill are well-structured JSON objects containing multiple useful fields. Each result includes the display\_name (formatted address), geographic coordinates (lat and lon), place type, importance score, and a detailed address breakdown. When photos are included, they appear in a photos array with URLs, coordinates, and camera heading information.

The response also indicates whether street imagery is available for the location, helping users understand the completeness of the visual data provided. This structured format makes it easy to integrate the skill's output into various applications and workflows.

Best Practices and Use Cases
----------------------------

For optimal results, use the query parameter for landmarks, points of interest, and well-known places. When you need precise geocoding for addresses, use structured address fields instead. Enable include\_photos when visual context is important, such as in real estate applications or travel planning tools.

The advanced mode is particularly useful when you need comprehensive place data beyond basic coordinates and addresses. Combining multiple address components improves accuracy, especially for locations in areas with similar names or when searching internationally.

Integration and Workflow
------------------------

The Places skill integrates seamlessly into larger workflows through its API endpoints and shell script interfaces. Whether you're building a real estate application that needs property location data, a travel app that shows landmarks with photos, or a logistics system that requires accurate address geocoding, this skill provides the foundation.

Its companion skills in the Camino suite, including Query, Route, Journey, and others, allow for building comprehensive location-based applications. The Places skill serves as a fundamental building block for any system that needs to understand and work with geographic locations.

Conclusion
----------

The Camino Places skill represents a robust solution for flexible place lookup and geocoding within the OpenClaw ecosystem. Its combination of free-form query support, structured address handling, optional street-level photos, and comprehensive response data makes it an invaluable tool for developers building location-aware applications.

With easy installation, generous free tier, and extensive configuration options, the Places skill provides everything needed to add sophisticated location intelligence to your projects. Whether you're building a simple address lookup tool or a complex location-based service, this skill offers the reliability and features required for professional-grade applications.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-places/SKILL.md>