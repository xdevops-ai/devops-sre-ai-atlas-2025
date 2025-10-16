---
layout: default
title: Azure Copilot Agent Mode
parent: Platform Directory
---

# Azure Copilot Agent Mode

Activities: Y/M | Diagnostics: P/M | Provisioning: Y/M  <br>
Event ontology: P/L | Observability: P/L | Confidence: High

**Build style / interface —** VS Code extension (Copilot for Azure) with chat ("Ask") and Agent Mode.  
**What it actually does —** Natural-language operations over Azure: decomposes requests into tasks, generates or modifies Bicep, runs Azure CLI/azd commands, checks resource health, and deploys under RBAC with confirmation gates.  
**Data / telemetry —** Azure Resource Graph, resource configurations, health APIs.  
**Interoperability —** Azure CLI/SDK and Azure Developer CLI; Azure RBAC.  
**Deployment model —** Client-side VS Code extension backed by your Azure subscription with a cloud backend.  
**Notes —** Enterprise-ready guardrails: explicit confirmation before changes, execution history logs, respect for tenant boundaries.

**UKM Snapshots:**
ingest P/L, index P/L, retrieval P/M, governance Y/M, overall medium-low  <br>
Note: See analysis/baselines/knowledge.md (doc-platform.tar) for definitions and evaluation criteria.







**UAM Snapshots:**
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high  <br>
Note: See analysis/baselines/activity.md (doc-platform.tar) for definitions and evaluation criteria.






**UDM Snapshots:**
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium  <br>
Note: See analysis/baselines/diagnostic.md (doc-platform.tar) for definitions and evaluation criteria.






**UOM Snapshots:**
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium  <br>
Note: See analysis/baselines/observability.md (doc-platform.tar) for definitions and evaluation criteria.






**UEOM Snapshots:**
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium  <br>
Note: See analysis/baselines/ontology.md (doc-platform.tar) for definitions and evaluation criteria.






**UPM Snapshots:**
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high  <br>
Note: See analysis/baselines/provisioning.md (doc-platform.tar) for definitions and evaluation criteria.







**Latest updates —** — 
**Links —** [Official Site](https://...), [Docs](https://...), [Blog](https://...)