---
layout: default
title: AWS Strands SDK
parent: Platform Directory
---

# AWS Strands SDK

**Activities**: P/L | **Diagnostics**: P/M | **Provisioning**: Y/M  <br>
**Event ontology**: P/L | **Observability**: P/M | **Confidence**: High

**Build style / interface —** Code-first SDK for Python and Node.  
**What it actually does —** A model-driven agent framework that plans and acts via tools, with deployments on AWS Lambda, Fargate, EKS, and EC2.  
**Data / telemetry —** Agent plans and tool calls traced via OpenTelemetry.  
**Interoperability —** Supports the MCP standard and agent-to-agent communication; integrates AWS services and community toolpacks.  
**Deployment model —** Runs in your own AWS account.  
**Notes —** Bring your own memory and knowledge base; strong tracing and governance hooks.

**UKM Snapshots:**
ingest P/L, index N/L, retrieval P/M, governance P/M, overall medium-low  <br>
**Note:** Knowledge: BYO sources; governed ingestion & indexing.

**UAM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Activities: guided actions with approvals

**UDM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Diagnostics: anomaly detection & triage; correlates metrics/traces/logs

**UOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Observability: ingests metrics/traces/logs/events

**UEOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Ontology: normalizes to standard schemas; CMDB/service-aware entities

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: SaaS-managed; limited direct apply
**Links —** [Official Site](https://strandsagents.com/latest/), [Docs](https://strandsagents.com/latest/documentation/docs/), [Blog](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/)
