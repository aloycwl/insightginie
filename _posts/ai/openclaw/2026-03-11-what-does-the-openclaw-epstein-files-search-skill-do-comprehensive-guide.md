---
layout: post
title: "What Does the OpenClaw Epstein Files Search Skill Do? | Comprehensive Guide"
date: 2026-03-11T23:46:13
categories: [24854]
original_url: https://insightginie.com/what-does-the-openclaw-epstein-files-search-skill-do-comprehensive-guide
---

Understanding the OpenClaw Epstein Files Search Skill
=====================================================

The OpenClaw Epstein Files Search skill is a powerful tool designed for individuals and researchers who need easy access to the declassified Jeffrey Epstein documents released by the U.S. Department of Justice (DOJ). Here, we break down how this skill operates and what it can do for users.

Introduction to the Epstein Files
---------------------------------

On January 30, 2026, the DOJ released over 44,886 documents related to Jeffrey Epstein, offering unprecedented insight into the case. This vast collection includes court filings, depositions, flight logs, financial records, communications, evidence inventories, and more.

Getting Started with the Epstein Files Search Skill
---------------------------------------------------

### Prerequisites

To use this skill, you need:

* Node.js and npm installed on your system
* Access to the internet for fetching search results
* Basic familiarity with command-line interfaces (CLI)

### Installation

First, clone the [OpenClaw skills repository](https://github.com/openclaw/skills). Navigate to the directory containing the Epstein Files Search skill and install the required dependencies using npm.

If you're already using [Project Einstein](https://emc2ai.io), this skill is pre-installed.

### Available Commands

#### Search

The primary command allows users to search across the indexed Epstein documents. The skill supports searching by name, topic, location, and keyword.

##### Command Syntax

```
node scripts/epstein.mjs search --query <terms> [--limit N]
```

##### Flags

* `--query <terms>`: Mandatory flag specifying the search terms.
* `--limit <N>`: Optional flag setting the maximum number of results (1-500), with a default of 10.

##### Examples

* Search for a person: `node scripts/epstein.mjs search --query "Ghislaine Maxwell" --limit 10`
* Search for a topic: `node scripts/epstein.mjs search --query "flight logs" --limit 20`
* Search by location: `node scripts/epstein.mjs search --query "Little St James"`

#### Stats

Retrieves indexed data statistics, including the number of documents, database size, and last update.

```
node scripts/epstein.mjs stats
```

Understanding the Output Format
-------------------------------

Search results are returned in JSON format, which makes it easy to parse programmatically. The output structure includes:

* `query`: The search terms entered.
* `totalHits`: The total number of documents matching the search criteria.
* `hits`: An array of individual search results, each containing:

* `id`: Unique identifier for the document.
* `efta_id`: The official EFTA identifier from the DOJ.
* `content_preview`: A preview of the document content.
* `doc_type`: Type of document (legal\_document, evidence, etc.).
* `dataset`: The dataset from which the document is sourced.
* `pages`: Number of pages in the document.
* `people`: List of individuals mentioned in the document.
* `locations`: Locations referenced in the document.
* `aircraft`: Aircraft identifiers mentioned.
* `evidence_types`: Types of evidence included in the document.
* `source`: Source of the document, typically the DOJ release.
* `indexed_at`: When the document was indexed.
* `doj_url`: Direct link to the PDF file on the DOJ website.
* `doj_listing_url`: Link to the overview page for that data set.

### Quick Links

Each result includes direct PDF links and data set overview links, making it easy to access the source documents directly from the DOJ's website.

Statistics
----------

The stats command provides:

* `totalDocuments`: Total number of indexed documents (44,886+).
* `databaseSize`: Size of the database (2.1 GB).
* `lastUpdate`: When the index was last updated.
* `isIndexing`: Whether the database is currently being indexed.

Data Sources
------------

The OpenClaw Epstein Files Search skill is powered by:

* The U.S. Department of Justice release of Epstein-related records.
* The DugganUSA API, which indexes and makes these documents searchable.

These sources cover over 44,886 document files with more than 3 million pages across various types of content.

Practical Examples
------------------

The skill offers practical features for advanced users looking to integrate the results with other tools or workflows:

### Piping Outputs

* Filter results with `jq`: `node scripts/epstein.mjs search --query "Maxwell" --limit 100 | jq ".hits[] | .people"`
* Save results to a file: `node scripts/epstein.mjs search --query "flight logs" --limit 500 > flight-logs.json`
* Count hits: `node scripts/epstein.mjs search --query "Palm Beach" | jq ".totalHits"`
* Extract mentioned people: `node scripts/epstein.mjs search --query "2005" --limit 100 | jq "[.hits[].people[]?] | unique"`

Troubleshooting Common Issues
-----------------------------

* **Cannot Reach API:** Check your internet connection or temporary DugganUSA API downtimes.
* **No Results Found:** Broaden your search terms; the search is keyword-based.
* **Slow Responses:** The API typically responds in 100-900ms. Larger result sets may take slightly longer.

Conclusion
----------

The OpenClaw Epstein Files Search skill is a comprehensive, freely accessible tool that enables detailed exploration of the DOJ's Jeffrey Epstein document releases. With its ability to search by name, topic, location, and keyword, it serves as an invaluable resource for legal researchers, journalists, and anyone seeking deeper insights into the Epstein case.

References
----------

* [DOJ Epstein Records](https://www.justice.gov/epstein) — Official release page
* [DugganUSA API](https://dugganusa.com) — Search index provider
* [Project Einstein](https://project-einstein.org) — AI agent with built-in Epstein files search

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/chuxo/epstein/SKILL.md>