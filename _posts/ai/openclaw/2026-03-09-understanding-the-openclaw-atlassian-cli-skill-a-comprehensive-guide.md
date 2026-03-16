---
layout: post
title: "Understanding the OpenClaw Atlassian CLI Skill: A Comprehensive Guide"
date: 2026-03-09T14:46:19
categories: [24854]
original_url: https://insightginie.com/understanding-the-openclaw-atlassian-cli-skill-a-comprehensive-guide
---

Understanding the OpenClaw Atlassian CLI Skill: A Comprehensive Guide
=====================================================================

Last updated: March 2024

Introduction to the OpenClaw Atlassian CLI Skill
------------------------------------------------

The OpenClaw Atlassian CLI skill is a powerful tool designed to interact with Jira Cloud and perform Atlassian organization administration tasks directly from the command line. This skill is particularly useful for developers, project managers, and system administrators who need to automate workflows, manage projects, and handle various Jira operations efficiently.

What the OpenClaw Atlassian CLI Skill Does
------------------------------------------

The OpenClaw Atlassian CLI skill leverages the Atlassian CLI (acli) to perform a wide range of operations, including:

* **Jira Work Item Management:** Create, edit, search, assign, transition, comment, clone, link, archive, attach files, and manage watchers for work items.
* **Project Management:** Create, list, update, and archive projects. Manage project settings, custom fields, and schemes.
* **Board and Sprint Management:** Search and manage boards, list and manage sprints, and view work items within sprints.
* **Filter and Dashboard Management:** Create, edit, and manage filters and dashboards.
* **Organization Administration:** Manage user accounts, authentication, and organization settings.
* **Automation and Integration:** Automate workflows and integrate with other tools and systems.
* **AI Agent Interaction:** Interact with the Rovo Dev AI agent for advanced coding and development tasks.

Prerequisites and Authentication
--------------------------------

Before using the OpenClaw Atlassian CLI skill, ensure that the Atlassian CLI (acli) is installed and authenticated on your system. The binary is not bundled with this skill, so you will need to install it separately.

To verify the availability of acli, run the following command in your terminal:

```
acli --help
```

Authentication is crucial for performing operations with the Atlassian CLI. You can check your authentication status with the following commands:

```
acli jira auth status
acli admin auth status
```

If you are not authenticated, you can use one of the following methods:

* **OAuth (Interactive):** Recommended for users as it is interactive and secure.

+ ```
  acli jira auth login --web
  ```

* **API Token (Non-Interactive):** Recommended for CI/automation as it is non-interactive and secure.

+ ```
  echo "$API_TOKEN" | acli jira auth login --site "mysite.atlassian.net" --email "user@atlassian.com" --token
  ```

* **Admin API Key:** Required for admin commands only.

+ ```
  echo "$API_KEY" | acli admin auth login --email "admin@atlassian.com" --token
  ```

* **Switching Between Accounts:** Manage multiple accounts efficiently.

+ ```
  acli jira auth switch --site mysite.atlassian.net --email user@atlassian.com
  acli admin auth switch --org myorgname
  ```

Security Best Practices
-----------------------

When using the OpenClaw Atlassian CLI skill, it is essential to follow security best practices to protect sensitive information and prevent unauthorized access.

### Secret Handling

Never hardcode tokens or API keys in commands. Always use environment variables or file-based input to ensure the security of sensitive information.

* ```
  acli jira workitem create --summary "Fix login bug" --project "TEAM" --type "Bug" --from-json template.json
  ```

Never log, echo, or display tokens in the output. Avoid piping secrets through intermediate files that persist on disk.

Prefer OAuth for interactive use and only use token-based auth for CI/automation where OAuth is not feasible. Do not store tokens in shell history.

If using environment variables, ensure they are set in the environment rather than inlined as literal values.

### Destructive Operations

Some commands are destructive or irreversible. Always confirm with the user before executing these commands:

* ```
  acli jira workitem delete
  acli jira project delete
  acli admin user delete
  acli admin user deactivate
  acli jira field delete
  ```

These commands are impactful but reversible:

* ```
  acli jira workitem archive / unarchive
  acli jira project archive / restore
  acli admin user cancel-delete
  acli jira field cancel-delete
  ```

Agent safety rules:

* Never run destructive commands without explicit user confirmation, even if –yes is available.
* When bulk-targeting via –jql or –filter, first run a search with the same query to show the user what will be affected.
* Prefer –json output to verify targets before applying destructive changes.
* Do not combine –yes with destructive bulk operations unless the user explicitly requests unattended execution.

Command Structure and Common Patterns
-------------------------------------

The command structure for acli follows the pattern:

```
acli <command> [<subcommand> ...] {MANDATORY FLAGS} [OPTIONAL FLAGS]
```

There are four top-level command groups:

* **acli jira:** Jira Cloud operations (work items, projects, boards, sprints, filters, dashboards, fields).
* **acli admin:** Organization administration (user management, auth).
* **acli rovodev:** Rovo Dev AI coding agent (Beta).
* **acli feedback:** Submit feedback and bug reports.

### Output Formats

Most list/search commands support –json, –csv, and default table output for flexible data handling.

### Bulk Operations

Target multiple items via:

* ```
  --key "KEY-1,KEY-2,KEY-3":
  ```

  Comma-separated keys.
* ```
  --jql "project = TEAM AND status = 'To Do'":
  ```

  JQL query.
* ```
  --filter 10001:
  ```

  Saved filter ID.
* ```
  --from-file "items.txt":
  ```

  File with keys/IDs (comma/whitespace/newline separated).

Use –ignore-errors to continue past failures in bulk operations and –yes or -y to skip confirmation prompts, which is useful for automation.

### Pagination

Manage result sets with:

* ```
  --limit N:
  ```

  Maximum items to return (defaults vary: 30-50).
* ```
  --paginate:
  ```

  Fetch all pages automatically (overrides –limit).

### JSON Templates

Many create/edit commands support –generate-json to produce a template and –from-json to consume it:

```
acli jira workitem create --generate-json > template.json
# edit template.json
acli jira workitem create --from-json template.json
```

Quick Reference: Most Common Operations
---------------------------------------

### Work Items

Create, search, view, edit, transition, assign, comment, and bulk create work items with these common operations:

```
# Create
acli jira workitem create --summary "Fix login bug" --project "TEAM" --type "Bug"
acli jira workitem create --summary "New feature" --project "TEAM" --type "Story" --assignee "@me" --label "frontend,p1"

# Search
acli jira workitem search --jql "project = TEAM AND assignee = currentUser()" --json
acli jira workitem search --jql "project = TEAM AND status = 'In Progress'" --fields "key,summary,assignee" --csv

# View
acli jira workitem view KEY-123
acli jira workitem view KEY-123 --json --fields "*all"

# Edit
acli jira workitem edit --key "KEY-123" --summary "Updated title" --assignee "user@atlassian.com"

# Transition
acli jira workitem transition --key "KEY-123" --status "Done"
acli jira workitem transition --jql "project = TEAM AND sprint in openSprints()" --status "In Progress"

# Assign
acli jira workitem assign --key "KEY-123" --assignee "@me"

# Comment
acli jira workitem comment create --key "KEY-123" --body "Work completed"

# Bulk Create
acli jira workitem create-bulk --from-csv issues.csv
```

### Projects

List, view, and create projects with these commands:

```
acli jira project list --paginate --json
acli jira project view --key "TEAM" --json
acli jira project create --from-project "TEAM" --key "NEW" --name "New Project"
```

### Boards & Sprints

Search, list, and manage boards and sprints with these operations:

```
acli jira board search --project "TEAM"
acli jira board list-sprints --id 123 --state active
acli jira sprint list-workitems --sprint 1 --board 6
```

Detailed Command Reference
--------------------------

For complete details on every command, including flag parameters and examples, refer to the detailed reference guides:

* [Jira Work Item Commands](https://github.com/openclaw/skills/blob/main/references/jira-workitem-commands.md): Create, edit, search, assign, transition, comment, clone, link, archive, attach files, manage watchers.
* [Other Commands](https://github.com/openclaw/skills/blob/main/references/other-commands.md): Jira project, board, sprint, filter, dashboard, field. Admin, rovodev, feedback.

These references provide comprehensive information to help you maximize the potential of the OpenClaw Atlassian CLI skill.

Conclusion
----------

The OpenClaw Atlassian CLI skill is an invaluable tool for anyone working with Jira Cloud and Atlassian organizations. By leveraging the power of the Atlassian CLI, you can streamline workflows, automate tasks, and enhance productivity. Always follow security best practices and confirm with users before executing destructive operations to ensure a safe and efficient working environment.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/peetzweg/atlassian-cli/SKILL.md>