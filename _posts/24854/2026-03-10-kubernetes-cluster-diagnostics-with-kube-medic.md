---
layout: post
title: "Kubernetes Cluster Diagnostics with kube-medic"
date: 2026-03-10T23:18:20
categories: [24854]
original_url: https://insightginie.com/kubernetes-cluster-diagnostics-with-kube-medic
---

Kubernetes Cluster Diagnostics with kube-medic
----------------------------------------------

Managing Kubernetes clusters effectively requires powerful diagnostic tools that can quickly identify and resolve issues across your infrastructure. kube-medic is a comprehensive Kubernetes diagnostics toolkit designed to provide instant AI-powered incident triage through kubectl commands. This tool enables cluster administrators, SREs, and DevOps engineers to perform full cluster health assessments, detailed pod investigations, deployment analysis, resource pressure detection, and event monitoring—all from a single interface.

### What is kube-medic?

kube-medic is a Kubernetes Cluster Triage & Diagnostics tool that provides instant AI-powered incident triage via kubectl. It’s designed to help you understand what’s happening in your cluster by correlating data from multiple sources and presenting actionable insights. The tool is developed by Anvil AI and is available under the MIT license, making it accessible for both personal and commercial use.

The primary goal of kube-medic is to transform raw Kubernetes data into meaningful diagnoses. Instead of just listing symptoms, it connects the dots between events, pod statuses, logs, and resource usage to identify root causes and recommend specific solutions.

### Your Role as a Cluster Diagnostician

When using kube-medic, you take on the role of an expert Kubernetes SRE. Your job isn’t just to run commands—it’s to analyze data across multiple dimensions and provide comprehensive diagnoses. Here’s how you should approach different scenarios:

#### Events + Pod Status:

When you see a pod with CrashLoopBackOff status and OOMKilled events, don’t just report the symptoms. Connect the dots: low memory limits combined with OOMKilled events indicate that the pod is running out of memory. The solution is to increase the memory limit in the pod specification.

#### Logs + Events:

If logs show connection refused errors and events indicate a service endpoint change, the root cause is likely a misconfigured service rather than the crashing pod itself. Understanding these correlations is crucial for effective troubleshooting.

#### Resources + Pod Count:

High memory usage on a node combined with many pods without resource limits indicates resource contention risk. Pods without proper resource constraints can consume excessive resources, leading to node instability and scheduling issues.

#### Deployment History + Current State:

If a deployment was updated 10 minutes ago and pods started crashing 10 minutes ago, the deployment is likely the cause. Understanding the timeline of changes helps identify when problems were introduced.

### Subcommands and Usage

kube-medic provides several subcommands for different diagnostic scenarios. Each subcommand serves a specific purpose and provides targeted insights into your cluster’s health.

#### sweep — Full Cluster Health Triage

Use this when you need to assess the overall health of your cluster or answer questions like “What’s wrong with my cluster?” or “Is everything healthy?”

```
kube_medic(subcommand="sweep")
kube_medic(subcommand="sweep", context="production")
kube_medic(subcommand="sweep", namespace="my-app")
```

The sweep command returns comprehensive information including node status, problem pods (non-Running), CrashLoopBackOff pods, ImagePullBackOff pods, recent warning events, and component health. Here’s how to interpret the results:

* **Start with nodes** — Are any NotReady or under pressure? Node health is foundational to cluster stability.
* **Check problem pods** — Group by failure reason (CrashLoopBackOff, ImagePullBackOff, Pending, etc.) to identify patterns.
* **Look at events** for patterns like repeated OOMKilled, FailedScheduling, or other warning events.
* **Cross-reference** — Are problem pods on a specific node? Is there resource pressure affecting multiple components?

#### pod <name> — Pod Autopsy

Use this when investigating specific pod issues or answering questions like “Why is pod X crashing?”

```
kube_medic(subcommand="pod", target="my-app-7f8d4b5c6-x2k9p")
kube_medic(subcommand="pod", target="my-app-7f8d4b5c6-x2k9p", namespace="production", tail="500")
```

The pod autopsy provides detailed information including full pod details, container statuses, current logs, previous container logs, events for this specific pod, and image version mismatch detection. Here’s how to present pod autopsy results:

```
## 🏥 Pod Autopsy: `my-app-7f8d4b5c6-x2k9p`
**Namespace:** production | **Node:** worker-node-1 | **Phase:** Running | **QoS:** Burstable

### Container Status
| Container | Image | Ready | Restarts | State |
|-----------|-------|-------|----------|-------|
| my-app | my-app:v1.2.3 | true | 0 | Running |
| sidecar | logging-agent:v2.1.0 | true | 0 | Running |

### ⚠️ Image Mismatches
- Container "my-app" is running image "my-app:v1.2.3" but spec shows "my-app:v1.2.4"

### Events Timeline
- 2024-01-15 10:30: Pod scheduled on worker-node-1
- 2024-01-15 10:31: Container started successfully
- 2024-01-15 10:35: Warning: Image version mismatch detected

### Diagnosis
The pod is running an older image version (v1.2.3) than specified in the deployment spec (v1.2.4). This could indicate a rollout issue or image pull problem.

### Recommended Actions
1. Check if the image "my-app:v1.2.4" is available in the registry
2. Verify image pull secrets and registry access
3. Consider rolling back to the previous stable version if the new image is broken
```

#### deploy <name> — Deployment Status

Use this when checking deployment health or answering questions like “Is the deployment stuck?” or “What version is deployed?”

```
kube_medic(subcommand="deploy", target="my-app", namespace="production")
```

The deployment analysis provides deployment details, replica counts, rollout status, rollout history, ReplicaSets with revisions, and deployment events. Key things to check:

* **observedGeneration < generation** — The controller hasn’t processed the latest spec yet.
* **unavailableReplicas > 0** — The rollout may be stuck or failing.
* **Rollout status says “waiting”** — Something is blocking the rollout.
* **Check ReplicaSet images across revisions** — Was there a recent image change that might be causing issues?

#### resources — CPU/Memory Pressure

Use this when investigating resource-related issues or answering questions like “Which pods use the most memory?” or “Are my nodes overloaded?”

```
kube_medic(subcommand="resources")
kube_medic(subcommand="resources", context="staging", namespace="default")
```

The resources command returns node resource usage (CPU/memory percentages), node pressure conditions, top 20 pods by CPU, top 20 pods by memory, and pods missing resource limits. Here’s how to interpret the results:

* **Nodes > 85% memory** = danger zone, risk of OOMKiller killing pods
* **Nodes > 90% CPU** = scheduling will be impacted, new pods may not be scheduled
* **Pods without limits** = unbounded resource consumption risk
* **Pods without requests** = scheduler can’t make informed decisions about pod placement

#### events [namespace] — Recent Events

Use this when investigating recent changes or answering questions like “What changed recently?” or “What happened in the last 15 minutes?”

```
kube_medic(subcommand="events")
kube_medic(subcommand="events", target="kube-system")
kube_medic(subcommand="events", since="1h")
```

The events command returns all recent events sorted newest first (capped at 100), with summary statistics and top event reasons. This is invaluable for understanding what’s been happening in your cluster over time.

### Write Operations (DANGER — Requires User Confirmation)

kube-medic is read-only by default to prevent accidental changes to your cluster. When you determine that a fix is needed, you must follow a strict approval process:

1. **Show the exact command** you want to run
2. **Explain what it will do** and any associated risks
3. **Wait for explicit confirmation** from the user (“yes”, “do it”, “go ahead”)
4. **Only then use confirm\_write** to execute the command

Here’s an example flow:

```
You: Based on the triage, deployment `my-app` revision 5 introduced a broken image.
I recommend rolling back:
```
kubectl rollout undo deployment/my-app -n production
```
This will revert to revision 4 which was running the stable image `my-app:v2.3.1`.
Shall I proceed?

User: Yes, do it.

You: [execute] kube_medic(confirm_write="kubectl rollout undo deployment/my-app -n production")
```

Allowed write commands include:

* `kubectl rollout undo ...` — Rollback a deployment
* `kubectl rollout restart ...` — Restart pods in a deployment
* `kubectl scale ...` — Scale a deployment up or down
* `kubectl delete pod ...` — Delete a specific pod to force restart
* `kubectl cordon ...` / `kubectl uncordon ...` — Drain management

**NEVER execute write commands without user approval.** **NEVER run kubectl exec** commands through kube-medic as they can be dangerous and unpredictable.

### Multi-Cluster Support

kube-medic supports multi-cluster environments. When managing multiple clusters, always ask which context to use or let users specify with `--context`. You can help users list available contexts with:

```
kube_medic(subcommand="sweep", context="production")
```

This allows you to target specific clusters for diagnostics, which is essential in complex environments with staging, production, and development clusters.

### Integration and Dependencies

kube-medic integrates seamlessly with standard Kubernetes tools and requires the following dependencies:

* **kubectl** — The primary Kubernetes command-line tool
* **jq** — For JSON processing and data manipulation

The tool uses these dependencies to gather data from your cluster and present it in a structured, actionable format. All commands are executed through kubectl, ensuring compatibility with standard Kubernetes authentication and authorization mechanisms.

### Conclusion

kube-medic is an essential tool for anyone responsible for Kubernetes cluster operations. By providing comprehensive diagnostics, intelligent correlation of cluster data, and actionable recommendations, it significantly reduces the time and effort required to identify and resolve cluster issues. Whether you’re performing routine health checks, investigating specific problems, or managing complex multi-cluster environments, kube-medic provides the insights and tools you need to maintain healthy, stable Kubernetes infrastructure.

The key to effective use of kube-medic is understanding how to interpret the data it provides and following the proper diagnostic workflow. Start with broad sweeps to understand cluster health, dive into specific pods or deployments when problems are identified, monitor resource usage to prevent issues before they occur, and always follow the approval process for any write operations. With practice, kube-medic becomes an indispensable part of your Kubernetes operations toolkit.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/tkuehnl/kube-medic/SKILL.md>