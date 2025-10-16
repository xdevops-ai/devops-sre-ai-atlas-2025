---
layout: default
title: PagerDuty AIOps
parent: Platform Directory
---

# PagerDuty AIOps

**Activities**: Y/M | **Diagnostics**: Y/M | **Provisioning**: P/L  <br>
**Event ontology**: P/M | **Observability**: P/L | **Confidence**: High

**Build style / interface —** SaaS incident management with low-code incident workflows, Automation Actions, and an AI-driven Command Console.  
**What it actually does —** Provides incident intelligence and response automation: suppresses and deduplicates alerts, correlates related events into incidents, surfaces change context and similar past incidents, drafts status updates and post-mortems, and recommends next steps. Includes SRE, Insights and Shift agents to assist during response.  
**Data / telemetry —** Ingests events from monitoring tools and change feeds, and maintains incident timelines and human response history.  
**Interoperability —** Integrates with Datadog, New Relic, CloudWatch, Jira, ServiceNow, Slack and Teams; remediation can run via Automation Actions or Rundeck.  
**Deployment model —** PagerDuty Operations Cloud (SaaS).  
**Notes —** Human-centric: can auto-execute safe diagnostics and remediations when confidence is high, but escalates to humans if uncertain.

**UKM Snapshots:**
ingest P/M, index P/M, retrieval Y/M, governance Y/M, overall medium  <br>
**Note:** Knowledge: consumes product-native and BYO sources.

**UAM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Activities: agent executes playbooks/workflows with policy; sessionized context

**UDM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Diagnostics: anomaly detection & triage; correlates metrics/traces/logs; SOC detections supported

**UOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Observability: ingests metrics/traces/logs/events

**UEOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Ontology: normalizes to standard schemas; CMDB/service-aware entities

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: SaaS-managed; limited direct apply; cloud-hosted service
**Links —** [Official Site](https://www.pagerduty.com/platform/aiops/), [Docs](https://support.pagerduty.com/main/docs/aiops), [Blog](https://www.pagerduty.com/resources/aiops/learn/what-is-aiops/)
