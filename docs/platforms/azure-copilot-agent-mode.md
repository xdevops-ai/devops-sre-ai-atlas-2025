---
layout: default
title: Azure Copilot Agent Mode
parent: Platform Directory
---

# Azure Copilot Agent Mode

**Activities**: Y/M | **Diagnostics**: P/M | **Provisioning**: Y/M  <br>
**Event ontology**: P/L | **Observability**: P/L | **Confidence**: High

**Build style / interface —** VS Code extension (Copilot for Azure) with chat ("Ask") and Agent Mode.  
**What it actually does —** Natural-language operations over Azure: decomposes requests into tasks, generates or modifies Bicep, runs Azure CLI/azd commands, checks resource health, and deploys under RBAC with confirmation gates.  
**Data / telemetry —** Azure Resource Graph, resource configurations, health APIs.  
**Interoperability —** Azure CLI/SDK and Azure Developer CLI; Azure RBAC.  
**Deployment model —** Client-side VS Code extension backed by your Azure subscription with a cloud backend.  
**Notes —** Enterprise-ready guardrails: explicit confirmation before changes, execution history logs, respect for tenant boundaries.

**UKM Snapshots:**
ingest P/L, index P/L, retrieval P/M, governance Y/M, overall medium-low  <br>
**Note:** Knowledge: consumes product-native and BYO sources.

**UAM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Activities: agent executes playbooks/workflows with policy

**UDM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Diagnostics: anomaly detection & triage

**UOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Observability: ingests platform telemetry

**UEOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Ontology: normalizes to standard schemas

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: SaaS-managed; limited direct apply; cloud-hosted service
**Links —** [Official Site](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode), [Docs](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=vs-2022), [Blog](https://code.visualstudio.com/blogs/)
