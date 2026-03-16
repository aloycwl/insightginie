---
layout: post
title: "DJ Set Ripper: Extract Tracklists and Download Individual Tracks"
date: 2026-03-08T01:45:54
categories: [24854]
original_url: https://insightginie.com/dj-set-ripper-extract-tracklists-and-download-individual-tracks
---

DJ Set Ripper: Extract Tracklists and Download Individual Tracks
================================================================

If you're a DJ or music enthusiast, you might often come across a fantastic DJ set on platforms like YouTube, SoundCloud, Mixcloud, or 1001Tracklists and wish you could download the individual tracks. The **DJ Set Ripper** skill from OpenClaw makes this possible. This article will explain how this skill works and how it can help you build your music library.

Understanding the DJ Set Ripper Skill
-------------------------------------

The DJ Set Ripper skill is designed to extract tracklists from DJ sets on various platforms and then download each track individually. This process involves several steps, including fetching the set URL, extracting the raw text, parsing the tracklist, downloading each track, and generating a log file to keep track of the status of each track.

### Fetching the Set URL and Extracting Raw Text

The first step involves fetching the set URL and extracting the relevant information. Depending on the platform, the method of extraction varies:

* **YouTube:** The skill uses `yt-dlp --dump-json` to fetch the description and metadata.
* **SoundCloud / Mixcloud:** The `web_fetch` command is used to grab the page content in markdown mode.
* **1001Tracklists:** Again, `web_fetch` is used, as this source provides the most structured data, making it the preferred choice when available.

### Parsing the Tracklist

Once the raw text is extracted, it is fed to the model with a specific prompt structure to identify the tracks. The model is instructed to return a JSON array of objects, each containing the track number, timestamp, artist, and title. The prompt includes several rules to ensure accurate parsing, such as preserving remix/mix names, handling unidentified tracks, and normalizing artist names.

If the parsing process returns zero tracks, the skill informs the user that the tracklist couldn't be extracted and suggests checking 1001Tracklists manually or pasting the tracklist directly.

### Downloading Each Track

After parsing the tracklist, the skill proceeds to download each track using the `dj-mp3-sourcer` workflow. This involves searching various sources in a priority order, preferring extended mixes, and either downloading the tracks or surfacing purchase links. The downloads are parallelized to avoid rate limits, and files are saved to `~/Downloads/{set-name}/`, where the set name is derived from the mix title.

Users are also given the option to download the full mix. If they choose to do so, the skill uses `yt-dlp` with specific options to embed the thumbnail and add metadata, saving the file in a sanitized format.

### Normalizing Filenames

After all downloads are complete, the skill runs a normalization script to ensure consistent filename formatting. This involves writing the parsed tracklist as JSON and then running a script to fuzzy-match each MP3 file to a tracklist entry, renaming the files accordingly. This step is crucial to maintaining a clean and organized music library.

### Generating the Log File

The skill generates a log file to provide a comprehensive overview of the downloaded tracks. The log file includes details such as the set title, URL, date, total tracks found, and the status of each track (downloaded, purchase link, not found, unidentified). This log file helps users keep track of their downloads and identify any missing tracks.

Edge Cases and Configuration
----------------------------

The DJ Set Ripper skill is designed to handle various edge cases, such as:

* **No tracklist in description:** The skill checks 1001Tracklists via web search if no tracklist is found in the description.
* **Unidentified tracks:** Tracks listed as “ID – ID” or “ID” are logged as unidentified and not downloaded.
* **Bootlegs / mashups:** The skill searches for these tracks but logs them as not found if they cannot be located.
* **B2B sets:** Multiple artists in the set title are handled gracefully.
* **Duplicate tracks:** These are deduplicated by artist and title before downloading.
* **Very long sets:** The skill batches these in groups of 5 and reports progress as batches complete.

The skill also offers several configuration options, including the output directory, format, download of the full mix, free-only mode, and the number of parallel downloads. These options can be customized to suit individual preferences.

Conclusion
----------

The DJ Set Ripper skill from OpenClaw is a powerful tool for extracting tracklists from DJ sets and downloading individual tracks. By following a structured workflow, the skill ensures accurate parsing, efficient downloading, and organized storage of tracks. Whether you are a DJ building a music library or a music enthusiast looking to expand your collection, the DJ Set Ripper skill simplifies the process and enhances your music experience.

Remember to respect copyright laws and use this skill responsibly to download music you have the right to access. Happy listening and downloading!

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/robinnnnn/dj-set-ripper/SKILL.md>