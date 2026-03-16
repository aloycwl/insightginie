---
layout: post
title: "Birdfolio Skill: Comprehensive Guide to Bird Identification, Life List Tracking, and Trading Card Generation with OpenClaw"
date: 2026-03-05T22:40:30
categories: [24854]
original_url: https://insightginie.com/birdfolio-skill-comprehensive-guide-to-bird-identification-life-list-tracking-and-trading-card-generation-with-openclaw
---

Birdfolio Skill: Comprehensive Guide to Bird Identification, Life List Tracking, and Trading Card Generation with OpenClaw
==========================================================================================================================

For birdwatchers, naturalists, educators, and anyone who loves spotting feathered friends, the **Birdfolio skill**—a component of the [OpenClaw](https://github.com/openclaw/skills) ecosystem—offers a seamless, tech‑driven experience. It turns a simple bird photo into a full‑blown personal life list, assigns a rarity tier inspired by Pokémon, and even produces a custom trading‑card‑style visual that can be shared on Telegram or saved for later. This article dives deep into what the skill does, how it works under the hood, real‑world use cases, and the tangible benefits you'll gain by adding Birdfolio to your bird‑watching toolkit.

What Is the Birdfolio Skill?
----------------------------

Birdfolio is a *complete workflow* that bridges three core activities:

1. **Bird Identification:** Using Vision (OpenClaw's image‑analysis engine) and You.com search results, the skill determines the species, scientific name, confidence level, and key visual features of any bird photo you submit.
2. **Life List Tracking:** Each confirmed sighting is logged to a personal `lifeList.json` file, stored locally and mirrored to a Railway‑hosted PostgreSQL API. The list is organized by rarity tiers—`common`, `rare`, and `superRare`—so you can instantly see how many “big finds” you've collected.
3. **Trading Card Generation:** A two‑column HTML card is generated on‑the‑fly, embedding your original photo (base64‑encoded) alongside species details, rarity badge, fun fact, and a running count of total species observed. The card is rendered to a 600×400 PNG, uploaded to Cloudflare R2, and sent back to you via Telegram.

All of this happens automatically after a brief one‑time setup, making Birdfolio a truly *hands‑free* companion for fieldwork.

Step‑by‑Step: How Birdfolio Works
---------------------------------

Below is a detailed walk‑through of the skill's internal flow, from first‑time setup to the moment you receive a polished trading card.

### 1️⃣ One‑Time Setup Flow

* **Trigger:** You say “Set up my Birdfolio,” “set my region,” or you send a photo before any configuration exists.
* **Region Prompt:** The skill asks, “What's your home region? (e.g., California, Texas, United Kingdom).”
* **Workspace Creation:** It runs `init_birdfolio.py` with your Telegram ID, chosen region, and the Railway API URL. This creates the `birdfolio/` folder hierarchy, registers you in the remote API, and writes a `config.json` file for future reference.
* **Checklist Generation:** Three You.com searches pull the most common, uncommon, and rare/vagrant birds for your region. The skill builds a starter checklist containing 10 common, 5 rare, and 1 super‑rare species, stored in `birdfolio/checklist.json`.
* **Welcome Message:** You receive a friendly preview of your checklist, e.g.,

  ```
  🦅 Birdfolio is set up for California!
  Your checklist:
  Common (10): American Robin, House Sparrow, …
  Rare (5): Great Blue Heron, …
  Super Rare: California Condor
  Send me a bird photo to start collecting!
  ```

### 2️⃣ Bird Identification Flow (When You Send a Photo)

1. **Photo Retrieval:** OpenClaw downloads the image to a temporary media folder. The skill copies it to `birdfolio/birds/{slug}-{timestamp}.jpg` for permanent storage.
2. **Vision Identification:** Using the `image` tool, the skill returns JSON with `commonName`, `scientificName`, `confidence` (high/medium/low), and a list of visible features.
3. **Confidence Handling:**
   * *High:* Proceed automatically.
   * *Medium:* The skill asks for confirmation: “I think this might be a *species* — based on *features*. Does that look right to you?”
   * *Low:* It politely requests a clearer shot and stops the flow.
4. **Rarity Lookup:** A You.com query (e.g., “*American Robin California eBird frequency how common rare*“) returns textual signals. The skill maps these to the tier values `common`, `rare`, or `superRare`. If the species isn't on the checklist, it's marked as a “bonus” find.
5. **Fun Fact Extraction:** Another You.com search pulls a punchy 1‑2 sentence fact about the bird's behavior, habitat, or unique trait.
6. **Log the Sighting:** `log_sighting.py` records the event in the remote API and returns useful metrics: `isLifer` (first‑time ever), `totalSightings`, and `totalSpecies`.
7. **Checklist Update:** `update_checklist.py` flips the `found` flag for that species, ensuring future progress reports are accurate.
8. **Card Generation:**
   * Vision determines the bird's horizontal position (percentage from left edge) to set `--object-position` for optimal cropping.
   * `generate_card.py` builds an HTML card embedding the photo as base64, the rarity badge, fun fact, region, date, and a running life‑count.
   * `screenshot_card.js` renders the HTML to a 600×400 PNG.
   * `upload_card.py` pushes the PNG to Cloudflare R2, returning a public URL.
   * The skill PATCHes the sighting record with the card URL and finally sends the PNG back to you via Telegram.
9. **Final Reply:** Depending on the metrics, the skill crafts a personalized message:
   * If `isLifer` is true: “🎉 New lifer! That's your first ever *species*! Bird #[totalSpecies] in your Birdfolio.”* If this is the very first bird ever (`totalSpecies == 1`): it also shares a PWA link: `https://birdfolio.tonbistudio.com/app/[telegram_id]`* Otherwise: “[Common Name] spotted! You've now seen [N] species in your Birdfolio.” The reply includes the rarity emoji, the fun fact, and a note about checklist status.

### 3️⃣ Checklist & Stats Queries

When you ask, “How's my checklist?” or “Birdfolio progress,” the skill runs `get_stats.py`. The output is formatted as a concise visual progress bar:

```
📋 California Checklist
Common   ✅✅✅⬜⬜⬜⬜⬜⬜⬜  3/10
Rare     ✅⬜⬜⬜⬜              1/5
Super Rare ⬜                0/1
🐦 4 species | 5 total sightings
📍 Last spotted: American Robin on 2024‑09‑12
🏆 Rarest find: California Condor (superRare)
```

Optionally, the skill can generate a graphical checklist card (HTML → PNG) for a richer visual experience.

### 4️⃣ Life List View

Commands like “Show my Birdfolio” or “Show my life list” read `birdfolio/lifeList.json`, group entries by rarity (Super Rare → Rare → Common), and either render a plain‑text list or an HTML gallery saved as `my-birdfolio.html`. The resulting PNG can be sent to you, giving a quick snapshot of every bird you've logged.

### 5️⃣ Species Lookup (No Logging)

If you ask, “Tell me about *species*,” the skill performs two You.com searches—one for general facts and another for regional eBird frequency. It returns a conversational summary without touching your life list or generating a card.

### 6️⃣ Rarest Bird Query

“What's my rarest bird?” triggers `get_stats.py` again, extracts the `rarestBird` object, and replies with the species name, rarity tier, date spotted, and region.

Real‑World Use Cases
--------------------

* **Field Birdwatching:** While out on a hike, snap a quick photo, send it to the bot, and instantly know the species, its rarity, and add it to your life list—all without pulling out a notebook.
* **Citizen Science Projects:** Researchers can ask participants to submit sightings; the automated logging and rarity classification streamline data collection for regional bird surveys.
* **Education & Classroom:** Teachers can use Birdfolio to turn a lesson on local fauna into an interactive activity—students upload photos, receive facts, and compete for the most “Super Rare” finds.
* **Social Sharing:** The generated trading cards are perfect for Telegram groups, Instagram stories, or personal blogs, turning each sighting into a shareable badge of achievement.
* **Personal Motivation:** The gamified rarity system (Common, Rare, Super Rare) encourages users to explore new habitats and chase elusive species, fostering deeper engagement with nature.

Key Benefits of Using Birdfolio
-------------------------------

1. **Instant, Accurate Identification:** Vision combined with curated You.com searches delivers high‑confidence results in seconds.
2. **Automated Life‑List Management:** No spreadsheets or manual entry—every sighting is recorded, timestamped, and categorized automatically.
3. **Gamified Rarity Tiers:** The Pokémon‑style badges add a fun, competitive layer that motivates continued birding.
4. **Personalized Trading Cards:** Each card is a visual souvenir, embedding your exact photo and a fun fact, ready to share or print.
5. **Cross‑Platform Integration:** Works within Telegram, but the underlying JSON files and API can be accessed by any front‑end (web, mobile, PWA).
6. **Scalable Architecture:** Data lives both locally and in a Railway‑hosted PostgreSQL instance, ensuring durability and easy backup.
7. **Educational Value:** Fun facts and species summaries turn casual sightings into learning moments.

SEO‑Friendly Summary (For Quick Reference)
------------------------------------------

If you're searching for a tool that *identifies birds from photos*, *tracks a personal life list*, and *creates custom trading cards*, look no further than the **Birdfolio skill for OpenClaw**. By combining AI‑driven image analysis, real‑time eBird data, and automated card generation, Birdfolio delivers a seamless, gamified bird‑watching experience that's perfect for hobbyists, educators, and citizen‑science projects alike.

Getting Started
---------------

To launch Birdfolio:

1. Open a Telegram chat with your OpenClaw bot.
2. Send the command `Set up my Birdfolio` and follow the region prompt.
3. Once setup is complete, simply send a bird photo. The bot will handle the rest—from identification to card delivery.

That's it! You now have a living, breathing digital bird collection that grows with every adventure.

Conclusion
----------

The Birdfolio skill transforms the traditional bird‑watching checklist into an interactive, data‑rich, and visually rewarding experience. By automating identification, logging, and card creation, it frees you to focus on what matters most—enjoying the birds themselves. Whether you're a seasoned birder chasing that elusive super‑rare vagrant or a beginner eager to learn the names of common backyard visitors, Birdfolio scales to your skill level and keeps you motivated every step of the way.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/tonbistudio/birdfolio/SKILL.md>