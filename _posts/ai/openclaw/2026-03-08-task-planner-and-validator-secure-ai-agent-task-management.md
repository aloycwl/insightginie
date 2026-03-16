---
layout: post
title: "Task Planner and Validator &#8211; Secure AI Agent Task Management"
date: 2026-03-08T10:18:19
categories: [24854]
original_url: https://insightginie.com/task-planner-and-validator-secure-ai-agent-task-management
---

Introduction to Task Planner and Validator
------------------------------------------

The Task Planner and Validator is a comprehensive skill that provides a secure, step-by-step task management system specifically designed for AI Agents. This tool ensures that automated processes execute safely, with proper validation, rollback capabilities, and execution control.

Core Features
-------------

### Safety Validation

The system automatically detects potentially dangerous operations before execution. Each step can be configured with safety checks that trigger warnings for operations like file deletion, system modifications, or access to sensitive paths. This proactive approach prevents accidental damage during automated workflows.

### Step-by-Step Execution Control

Tasks are broken down into individual steps, each with its own description, action identifier, parameters, and expected output. The planner validates the entire workflow before execution, ensuring logical consistency and safety compliance.

### Rollback Capabilities

For steps that support rollback, the system maintains checkpoints that can be used to revert changes if something goes wrong. This feature is crucial for operations like database migrations or system updates where reversibility is important.

Basic Usage
-----------

Getting started with the Task Planner is straightforward. First, you import and initialize the planner:

```
from task_planner import TaskPlanner
# Create planner
planner = TaskPlanner(auto_approve=False)
```

Then define your executor function that contains the actual logic for each action:

```
def my_executor(action: str, parameters: dict):
    """Your custom execution logic"""
    if action == "fetch_data":
        # Fetch data from API, database, etc.
        return {"data": [1, 2, 3]}
    elif action == "process_data":
        # Process the data
        return {"processed": True}
    else:
        return {"status": "completed"}
```

Create a plan by defining steps with descriptions, actions, parameters, and expected outputs:

```
steps = [
    {
        "description": "Fetch user data",
        "action": "fetch_data",
        "parameters": {"source": "database"},
        "expected_output": "List of users"
    },
    {
        "description": "Process users",
        "action": "process_data",
        "parameters": {"validation": True},
        "expected_output": "Processed data"
    }
]
plan = planner.create_plan(
    title="Data Processing Pipeline",
    description="Fetch and process user data",
    steps=steps
)
```

Validation and Execution
------------------------

Before executing any plan, validation is crucial:

```
# Validate
is_valid, warnings = planner.validate_plan(plan)
if warnings:
    print("Warnings:", warnings)

# Approve
planner.approve_plan(plan, approved_by="admin")

# Execute
success, results = planner.execute_plan(plan, my_executor)

# Get summary
summary = planner.get_execution_summary(plan)
print(f"Progress: {summary['progress_percentage']}%")
```

Advanced Features
-----------------

### Dry Run Mode

Test your plan without actually executing any actions:

```
success, results = planner.execute_plan(plan, my_executor, dry_run=True)
# Simulate only, no actual execution
```

### Persistence

Save and load plans for reuse:

```
# Save
planner.save_plan(plan, "my_plan.json")
# Load later
loaded_plan = planner.load_plan("my_plan.json")
# Verify integrity
if loaded_plan.verify_integrity():
    planner.execute_plan(loaded_plan, my_executor)
```

### Error Handling

Control how the system handles errors during execution:

```
success, results = planner.execute_plan(plan, my_executor, stop_on_error=False)
# Continue on failures

# Check results
for result in results:
    if not result['success']:
        print(f"Step {result['order']} failed: {result['error']}")
```

Step Configuration
------------------

Each step supports comprehensive configuration:

```
{
    "description": str,
    "action": str,
    "parameters": dict,
    "expected_output": str,
    "safety_check": bool,
    "rollback_possible": bool,
    "max_retries": int
}
```

Common Use Cases
----------------

### API Orchestration

Chain multiple API calls together with proper validation:

```
steps = [
    {
        "description": "Authenticate",
        "action": "api_auth",
        "parameters": {"service": "github"},
        "expected_output": "Auth token"
    },
    {
        "description": "Fetch data",
        "action": "api_fetch",
        "parameters": {"endpoint": "/repos"},
        "expected_output": "Repository list"
    }
]
```

### Data Pipeline

Build ETL processes with validation at each stage:

```
steps = [
    {
        "description": "Extract data",
        "action": "extract",
        "parameters": {"source": "database"},
        "expected_output": "Raw data"
    },
    {
        "description": "Transform data",
        "action": "transform",
        "parameters": {"rules": ["normalize", "validate"]},
        "expected_output": "Clean data"
    },
    {
        "description": "Load data",
        "action": "load",
        "parameters": {"destination": "warehouse"},
        "expected_output": "Success confirmation"
    }
]
```

### System Automation

Automate system administration tasks with safety checks:

```
steps = [
    {
        "description": "Backup database",
        "action": "backup",
        "parameters": {"target": "postgres"},
        "expected_output": "Backup file path",
        "rollback_possible": True
    },
    {
        "description": "Update schema",
        "action": "migrate",
        "parameters": {"version": "2.0"},
        "expected_output": "Migration complete",
        "rollback_possible": True
    },
    {
        "description": "Verify integrity",
        "action": "verify",
        "parameters": {"checks": ["all"]},
        "expected_output": "All checks passed"
    }
]
```

Best Practices
--------------

### Always Validate First

Never skip validation. Even if you plan to auto-approve, running validation helps catch configuration errors early:

```
is_valid, warnings = planner.validate_plan(plan)
if not is_valid:
    print("Plan validation failed!")
    for warning in warnings:
        print(f"  - {warning}")
    exit(1)
```

### Use Descriptive Names

Clear, descriptive step names prevent confusion and make debugging easier:

```
# Good ✅
{
    "description": "Fetch active users from PostgreSQL production database",
    "action": "fetch_active_users_postgres_prod",
    ...
}

# Bad ❌
{
    "description": "Get data",
    "action": "get",
    ...
}
```

### Mark Dangerous Operations

Explicitly mark potentially dangerous operations and consider whether rollback is possible:

```
{
    "description": "Delete temporary files older than 30 days",
    "action": "cleanup_temp_files",
    "parameters": {
        "age_days": 30,
        "path": "/tmp"
    },
    "safety_check": True,
    "rollback_possible": False
}
```

### Test with Dry Run

Always test your plan in dry run mode before actual execution:

```
success, results = planner.execute_plan(plan, my_executor, dry_run=True)
if success:
    # Now run for real
    success, results = planner.execute_plan(plan, my_executor, dry_run=False)
```

### Handle Errors Gracefully

Implement robust error handling in your executor:

```
def safe_executor(action: str, parameters: dict):
    try:
        result = execute_action(action, parameters)
        return result
    except Exception as e:
        logging.error(f"Failed to execute {action}: {e}")
        raise  # Re-raise to let planner handle it
```

Advanced Configuration
----------------------

### Auto-Approve for Automation

For fully automated workflows, enable auto-approval:

```
planner = TaskPlanner(auto_approve=True)
```

### Checkpoint System

The system automatically creates checkpoints for rollback-capable steps. You can access checkpoint history through the executor:

```
checkpoints = planner.executor.checkpoint_stack
```

### Execution History

Track all execution attempts:

```
history = planner.executor.execution_history
for entry in history:
    print(f"{entry['timestamp']}: {entry['step_id']} - {entry['status']}")
```

### Custom Validation Rules

Add custom validation rules to the safety validator:

```
planner.safety_validator.dangerous_operations.append('my_dangerous_op')
planner.safety_validator.sensitive_paths.append('/my/sensitive/path')
```

Troubleshooting
---------------

### “Plan must be approved before execution”

Solution: Approve the plan first or use auto-approve mode:

```
planner.approve_plan(plan, approved_by="admin")
# Or use auto-approve mode
planner = TaskPlanner(auto_approve=True)
```

### Safety validation warnings

Review warnings and ensure operations are intentional. If operations are safe, you can approve anyway:

```
is_valid, warnings = planner.validate_plan(plan)
for warning in warnings:
    print(warning)
if is_valid:
    # Still valid, just warnings
    planner.approve_plan(plan)
```

### Steps executing out of order

Ensure order values are sequential and properly configured:

```
steps[0]['order'] = 1
steps[1]['order'] = 2
steps[2]['order'] = 3
```

Conclusion
----------

The Task Planner and Validator provides a robust foundation for building safe, reliable AI Agent workflows. By combining safety validation, rollback capabilities, and comprehensive execution control, it ensures that automated processes execute predictably and can recover from failures when they occur.

Whether you're building data pipelines, API orchestrations, or system automation workflows, this skill provides the tools needed to manage complexity while maintaining safety and reliability.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/cerbug45/task-panner-validator/SKILL.md>