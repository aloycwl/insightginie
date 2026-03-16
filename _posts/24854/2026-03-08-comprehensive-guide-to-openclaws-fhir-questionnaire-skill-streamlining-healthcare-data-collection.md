---
layout: post
title: "Comprehensive Guide to OpenClaw&#8217;s FHIR Questionnaire Skill: Streamlining Healthcare Data Collection"
date: 2026-03-08T23:46:22
categories: [24854]
original_url: https://insightginie.com/comprehensive-guide-to-openclaws-fhir-questionnaire-skill-streamlining-healthcare-data-collection
---

Comprehensive Guide to OpenClaw’s FHIR Questionnaire Skill: Streamlining Healthcare Data Collection
===================================================================================================

OpenClaw’s FHIR Questionnaire Skill is a powerful tool designed to simplify and standardize the process of creating and managing healthcare questionnaires. This skill leverages the Fast Healthcare Interoperability Resources (FHIR) standard, ensuring interoperability and facilitating seamless data exchange across different healthcare systems. In this guide, we’ll delve into the functionalities of this skill, exploring how it aids in creating FHIR-conforming questionnaire definitions and integrates with clinical coding systems like LOINC and SNOMED CT.

Understanding the FHIR Questionnaire Skill
------------------------------------------

The FHIR Questionnaire Skill is meticulously crafted to transform plain requirement ideation documents into fully compliant FHIR questionnaires. It includes a suite of scripts that enable users to look up LOINC (Logical Observation Identifiers Names and Codes) and SNOMED CT (Systematized Nomenclature of Medicine–Clinical Terms) codes, two of the most widely used clinical coding systems globally. What sets this skill apart is that it eliminates the need for API keys, streamlining the process and making it more accessible.

Key Features and Functionalities
--------------------------------

### Dependency Requirements

To utilize the FHIR Questionnaire Skill, users need to have the following dependencies installed:

* Python 3.8 or higher
* JSONSchema 4.0.0 or higher

### Network Access Requirements

The skill requires whitelisted network access to the following resources:

* [clinicaltables.nlm.nih.gov](https://clinicaltables.nlm.nih.gov/) (for LOINC search)
* [tx.fhir.org](https://tx.fhir.org/) (for LOINC answer lists and SNOMED CT search via FHIR terminology server)

If network access fails, the skill will halt operations to prevent the use of incorrect or unreliable clinical codes.

### Critical Rules and Guidelines

To ensure the accuracy and reliability of clinical coding, the FHIR Questionnaire Skill enforces several critical rules:

* **Never suggest LOINC or SNOMED CT codes from memory or training data:** Always use the provided search and query scripts to retrieve clinical codes.
* **Use LOINC for clinical questions/observations:** Before suggesting any LOINC code, users must run the `search_loinc.py` script with appropriate search terms.
* **Use SNOMED CT for clinical concepts/conditions:** Similarly, users must always run the `search_snomed.py` script before suggesting any SNOMED CT code.
* **Only use codes returned by the scripts:** If a search fails or returns no results, users should not attempt to make up codes or suggest codes from memory.
* **Network access failures:** If the network access fails during a code search or query, users should stop the process immediately and not proceed with suggesting codes.

### Essential Scripts for Clinical Coding

The FHIR Questionnaire Skill provides a set of essential scripts that users must utilize to ensure accurate and reliable clinical coding:

#### 1. Searching LOINC Codes

To search for LOINC codes, users should run the `search_loinc.py` script with relevant clinical questions or observations. This script queries the clinicaltables.nlm.nih.gov server and returns matching LOINC codes. For example:

```
python scripts/search_loinc.py "depression screening"
python scripts/search_loinc.py "blood pressure" --format fhir
```

#### 2. Searching SNOMED CT Codes

To search for SNOMED CT codes, users should run the `search_snomed.py` script with relevant clinical concepts or conditions. This script queries the tx.fhir.org terminology server and returns matching SNOMED CT codes. For example:

```
python scripts/search_snomed.py "diabetes"
python scripts/search_snomed.py "hypertension" --format fhir
python scripts/search_snomed.py "diabetes mellitus" --semantic-tag "disorder"
```

Note that the `--semantic-tag` filter works best when the semantic tag appears in the display name (e.g., “Diabetes mellitus (disorder)”).

#### 3. Finding Answer Options

For questions with standardized answers, users can use the `query_valueset.py` script to find answer options. This script queries the tx.fhir.org terminology server and returns matching answer lists. For example:

```
python scripts/query_valueset.py --loinc-code "72166-2"
python scripts/query_valueset.py --loinc-code "72166-2" --format fhir
```

#### 4. Validating Questionnaires

Before finalizing a questionnaire, users should validate its structure using the `validate_questionnaire.py` script. This script checks the questionnaire definition against the FHIR specifications. For example:

```
python scripts/validate_questionnaire.py questionnaire.json
python scripts/validate_questionnaire.py questionnaire.json --verbose
```

Templates and Workflows
-----------------------

The FHIR Questionnaire Skill provides a variety of templates to help users get started with creating FHIR questionnaires. These templates range from minimal JSON structures to advanced questionnaires with conditional logic. Users can find these templates in the `assets/templates/` directory:

* `minimal.json`: A bare-bones structure to get started
* `basic.json`: A simple questionnaire with basic elements
* `advanced.json`: A complex questionnaire with conditional logic

The skill also outlines several workflows to guide users through the process of creating different types of FHIR questionnaires:

### Standardized Clinical Instruments (PHQ-9, GAD-7, etc.)

To create questionnaires for standardized clinical instruments like the PHQ-9 (Patient Health Questionnaire-9) or GAD-7 (Generalized Anxiety Disorder-7), users should follow these steps:

1. Find the panel code for the clinical instrument using the `search_loinc.py` script. This step is critical and should never be skipped.
2. Find the answer options for the clinical instrument using the `query_valueset.py` script with the found LOINC code.
3. Refer to the examples and templates provided in the `references/examples.md` file for complete implementations.

### Custom Organizational Questionnaires

To create custom questionnaires specific to an organization’s needs, users should follow these steps:

1. Start with a template from the `assets/templates/` directory.
2. For any clinical questions, search for LOINC codes using the `search_loinc.py` script.
3. Add answer options if available using the `query_valueset.py` script with the found LOINC code.
4. For custom questions without LOINC results, use inline `answerOptions` without a coding system.
5. Validate the questionnaire using the `validate_questionnaire.py` script.

Common Patterns and Best Practices
----------------------------------

Users of the FHIR Questionnaire Skill should be familiar with the following common patterns and best practices:

### Conditional Display

To create questionnaires with conditional display, users can utilize the `enableWhen` property. This allows for showing or hiding questions based on previous answers.

### Repeating Groups

To create repeating groups within a questionnaire, users should set the `"repeats": true` property. This is particularly useful for sections like medications or allergies.

### Standardized Answers

To use standardized answers for questions, users should utilise the `query_valueset.py` script with the appropriate LOINC code. This ensures that the answers are backed by LOINC and facilitates interoperability.

### Custom Answers

For questions without standardized answers, users should use inline `answerOption` with `valueCoding` (and no coding system). This is the simplest and most spec-compliant approach for custom answer lists.

Advanced Features and Custom Coding Systems
-------------------------------------------

### Opt-in: Reusable Welshare Coding System

For users who require reusable codes that can be shared across multiple questionnaires, the FHIR Questionnaire Skill offers the Welshare coding system. This namespace (`http://codes.welshare.app`) can be utilized to create CodeSystem and ValueSet pairs. To convert an inline answer list to the reusable format, users should add the appropriate system URI to each `valueCoding` and optionally reference the ValueSet via `answerValueSet`.

To create reusable custom codes, users can run the following command:

```
python scripts/create_custom_codesystem.py --interactive
```

Troubleshooting and Support
---------------------------

While using the FHIR Questionnaire Skill, users might encounter various issues and errors. Here are some common problems and their solutions:

### No LOINC Results

If a LOINC search returns no suitable results, users should try using broader search terms. For example, searching for “depression” instead of “PHQ-9 question 1”.

### Network Errors

If network errors occur during a code search or query, users can try using alternative servers with the `--server` flag. For instance:

```
python scripts/search_loinc.py "blood pressure" --server https://hapi.fhir.org/baseR4
python scripts/search_loinc.py "blood pressure" --server https://r4.ontoserver.csiro.au/fhir
```

### Validation Errors

If validation errors occur during the questionnaire validation process, users should refer to the FHIR Questionnaire specifications in the `references/fhir_questionnaire_spec.md` file for guidance.

### No Answer List Found

If no answer list is found for a particular LOINC code, users should use inline `answerOption` with system-less `valueCoding` (code + display only). This approach is the simplest and most spec-compliant for custom answer lists. Users should not attempt to fall back to a custom coding system unless explicitly requested by the user.

Conclusion
----------

The FHIR Questionnaire Skill by OpenClaw is a comprehensive and powerful tool for creating and managing FHIR-conforming questionnaires. By leveraging standardized clinical coding systems like LOINC and SNOMED CT, this skill ensures interoperability, accuracy, and efficiency in healthcare data collection. With its user-friendly scripts, extensive templates, and robust validation mechanisms, the FHIR Questionnaire Skill empowers healthcare professionals to create tailored, reliable, and standardized questionnaires that meet the unique needs of their organizations and patients.

Whether you are looking to implement standardized clinical instruments or create custom questionnaires, the FHIR Questionnaire Skill offers the flexibility and support needed to streamline the process and enhance healthcare data management.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/elmariachi111/fhir-questionnaire/SKILL.md>