---
layout: post
title: "OGT Docs &#8211; Create Task: Complete Guide for Managing Tasks in Docs-First Workflow"
date: 2026-03-05T12:03:20
categories: [24854]
original_url: https://insightginie.com/ogt-docs-create-task-complete-guide-for-managing-tasks-in-docs-first-workflow
---

What is OGT Docs – Create Task?
-------------------------------

OGT Docs – Create Task is a comprehensive system for creating and managing tasks in a docs-first workflow. It provides a structured approach to task lifecycle management where each task is represented as a folder that moves through various workflow stages, accumulating documentation and signals as it progresses.

The system is designed to bring clarity, traceability, and organization to task management by treating documentation as the primary artifact of work. Instead of scattered notes or ephemeral conversations, every task maintains a complete history of its evolution from conception to completion.

How OGT Docs – Create Task Works
--------------------------------

The system operates on a simple yet powerful principle: each task is a folder that moves through defined stages. This folder-based approach ensures that all related documentation stays together and can be easily tracked throughout the task's lifecycle.

### Core Workflow Stages

Tasks move through six primary stages:

1. **pending** – Tasks that are defined but not yet started
2. **in\_progress** – Tasks being actively worked on
3. **review** – Tasks completed and awaiting review
4. **blocked** – Tasks that cannot proceed due to dependencies
5. **done** – Completed and verified tasks
6. **rejected** – Tasks that were declined

Each stage has specific requirements and signals that indicate the task's current state. The system uses empty files as signals – their presence indicates a particular state without requiring content.

### Folder Structure

The complete folder structure looks like this:

```
docs/todo/
├── pending/                    # Tasks not yet started
│   └── {task_slug}/
│       ├── task.md             # Primary task definition
│       ├── context.md          # Background information (optional)
│       ├── .version            # Schema version
│       └── .priority           # Priority level
├── in_progress/                # Tasks being actively worked on
│   └── {task_slug}/
│       ├── task.md
│       ├── progress.md         # Work log and updates
│       ├── .version
│       ├── .priority
│       ├── .assigned_to_{agent}  # Who's working on it
│       └── .started_at         # Timestamp when started
├── review/                     # Tasks awaiting review
│   └── {task_slug}/
│       ├── task.md
│       ├── progress.md
│       ├── implementation.md   # What was done
│       ├── .version
│       ├── .ready_for_review   # Empty signal
│       ├── .pr_link            # PR URL if applicable
│       └── .review_requested_at
├── blocked/                    # Tasks that cannot proceed
│   └── {task_slug}/
│       ├── task.md
│       ├── progress.md
│       ├── .version
│       ├── .blocked            # Empty signal
│       ├── .blocked_reason     # Why blocked (content)
│       ├── .blocked_at         # When blocked
│       └── .depends_on         # What it's waiting for
├── done/                       # Completed and verified tasks
│   └── {task_slug}/
│       ├── task.md
│       ├── progress.md
│       ├── implementation.md
│       ├── verification.md     # How it was verified
│       ├── .version
│       ├── .verified           # Empty signal - REQUIRED
│       ├── .completed_at       # Completion timestamp
│       └── .verified_by_{agent}  # Who verified
├── rejected/                   # Tasks that were declined
│   └── {task_slug}/
│       ├── task.md
│       ├── .version
│       ├── .rejected           # Empty signal
│       ├── .rejected_reason    # Why rejected (content)
│       └── .rejected_at        # When rejected
└── implemented/                # Done tasks that are deployed/released
    └── {task_slug}/
        ├── task.md
        ├── implementation.md
        ├── verification.md
        ├── .version
        ├── .verified
        ├── .completed_at
        ├── .implemented_at     # When deployed
        └── .release_version    # Which release included it
```

Key Components of Each Task
---------------------------

### task.md – The Primary Definition

Every task starts with a task.md file that contains:

* **Task Title** – Clear, descriptive name
* **Summary** – Brief overview of what the task accomplishes
* **Objectives** – Specific, actionable goals
* **Acceptance Criteria** – Measurable outcomes that define completion
* **Dependencies** – Other tasks or resources required
* **Estimated Effort** – Time or complexity assessment
* **References** – Links to related documentation or resources

### progress.md – The Work Log

As tasks move through the in\_progress stage, progress.md serves as a chronological log of work performed. This includes:

* Start timestamps and initial analysis
* Major milestones and accomplishments
* Current status updates
* Blocks encountered and how they were resolved

### implementation.md – The Technical Record

Once work is complete, implementation.md documents:

* Files changed and their purposes
* Technical decisions made
* Testing performed
* Any special considerations or trade-offs

### verification.md – The Quality Assurance

For completed tasks, verification.md provides:

* Verification date and tester
* Tests performed and their results
* Evidence that acceptance criteria were met
* Final verification status

Use Cases and Benefits
----------------------

### Individual Contributor Benefits

For developers, designers, and other individual contributors, OGT Docs – Create Task provides:

* **Clear Starting Point** – No ambiguity about what needs to be done
* **Progress Tracking** – Visual indication of how much work remains
* **Context Preservation** – All relevant information stays with the task
* **Knowledge Transfer** – Others can understand work without asking
* **Quality Assurance** – Built-in verification ensures completeness

### Team Benefits

For teams, the system enables:

* **Transparency** – Everyone can see what's being worked on
* **Workload Management** – Clear view of who's busy and who's available
* **Dependency Tracking** – Blocks are visible and can be addressed
* **Knowledge Sharing** – Learning is captured and preserved
* **Process Improvement** – Bottlenecks and inefficiencies become visible

### Organizational Benefits

At the organizational level, OGT Docs – Create Task delivers:

* **Auditability** – Complete history of all work performed
* **Onboarding Efficiency** – New team members can understand context quickly
* **Process Standardization** – Consistent approach across all tasks
* **Quality Improvement** – Verification requirements ensure standards
* **Risk Management** – Blocks and dependencies are surfaced early

Getting Started with OGT Docs – Create Task
-------------------------------------------

### Creating Your First Task

Follow these steps to create your first task:

1. Create a new folder in the appropriate stage (usually pending/)
2. Name the folder using a clear, descriptive slug (e.g., fuzzy\_search)
3. Create task.md with all required sections
4. Add context.md if background information is needed
5. Create .version and .priority files

### Moving Tasks Through Workflow

As work progresses, move tasks through stages:

1. When starting work, move from pending/ to in\_progress/
2. Update progress.md with your work log
3. Create .assigned\_to\_{agent} and .started\_at files
4. When complete, move to review/ and create implementation.md
5. Add .ready\_for\_review, .pr\_link, and .review\_requested\_at
6. After review, move to done/ and create verification.md
7. Add .verified, .completed\_at, and .verified\_by\_{agent}

Best Practices
--------------

### Task Definition

* Keep tasks focused and achievable
* Write clear, specific objectives
* Define measurable acceptance criteria
* Identify dependencies early

### Documentation Quality

* Write for future readers, not just yourself
* Use clear, concise language
* Include links to relevant resources
* Update documentation as work progresses

### Workflow Management

* Move tasks promptly when stages change
* Keep progress.md updated regularly
* Don't skip verification – it's essential for quality
* Communicate blocks early and clearly

Common Scenarios
----------------

### Handling Blocks

When a task cannot proceed due to dependencies:

1. Move the task to blocked/
2. Create .blocked and .blocked\_reason files
3. Document what it's waiting for in .depends\_on
4. Add .blocked\_at timestamp

### Managing Reviews

For tasks awaiting review:

1. Move to review/ after completion
2. Update implementation.md with technical details
3. Create .ready\_for\_review signal
4. Add .pr\_link if applicable
5. Include .review\_requested\_at timestamp

### Verification Process

For completed tasks:

1. Move to done/ after review approval
2. Create verification.md with test results
3. Add .verified signal (REQUIRED)
4. Include .completed\_at timestamp
5. Add .verified\_by\_{agent} to indicate who verified

Advanced Features
-----------------

### Priority System

Each task includes a .priority file that can contain: critical, high, medium, or low. This helps teams focus on the most important work.

### Version Control

The .version file tracks schema versions, allowing for evolution of the task structure over time without breaking existing tasks.

### Integration with Development Tools

The system integrates well with:

* Git for version control
* CI/CD pipelines for automated verification
* Project management tools for visualization
* Communication platforms for notifications

Conclusion
----------

OGT Docs – Create Task provides a comprehensive, structured approach to task management that emphasizes documentation, transparency, and quality. By treating each task as a folder that moves through defined stages, teams can achieve better organization, clearer communication, and higher quality outcomes.

The system's emphasis on documentation as the primary artifact of work ensures that knowledge is preserved, context is maintained, and processes are repeatable. Whether you're an individual contributor looking for better organization or a team leader seeking to improve workflow management, OGT Docs – Create Task offers a proven framework for success.

Start implementing OGT Docs – Create Task today to transform how your team manages work, communicates progress, and delivers results.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/eduardou24/ogt-docs-create-task/SKILL.md>