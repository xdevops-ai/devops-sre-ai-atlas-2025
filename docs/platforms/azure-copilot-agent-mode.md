---
layout: default
title: Azure Copilot Agent Mode
parent: Platform Directory
---

# Azure Copilot Agent Mode

Activities: Y/M | Diagnostics: P/M | Provisioning: Y/M  
Event ontology: P/L | Observability: P/L | Confidence: High

Build style / interface — VS Code extension (Copilot for Azure) with chat ("Ask") and Agent Mode.  
What it actually does — Natural-language operations over Azure: decomposes requests into tasks, generates or modifies Bicep, runs Azure CLI/azd commands, checks resource health, and deploys under RBAC with confirmation gates.  
Data / telemetry — Azure Resource Graph, resource configurations, health APIs.  
Interoperability — Azure CLI/SDK and Azure Developer CLI; Azure RBAC.  
Deployment model — Client-side VS Code extension backed by your Azure subscription with a cloud backend.  
Notes — Enterprise-ready guardrails: explicit confirmation before changes, execution history logs, respect for tenant boundaries.

UKM Snapshots: 
ingest P/L, index P/L, retrieval P/M, governance Y/M, overall medium-low
Note:   See analysis/baselines/knowledge.md (doc-platform.tar) for definitions and evaluation criteria.

UAM Snapshots:   
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high
Note:   See analysis/baselines/activity.md (doc-platform.tar) for definitions and evaluation criteria.
UDM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/diagnostic.md (doc-platform.tar) for definitions and evaluation criteria.
UOM Snapshots:   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium
Note:   See analysis/baselines/observability.md (doc-platform.tar) for definitions and evaluation criteria.
UEOM Snapshots:   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium
Note:   See analysis/baselines/ontology.md (doc-platform.tar) for definitions and evaluation criteria.
UPM Snapshots:   
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high
Note:   See analysis/baselines/provisioning.md (doc-platform.tar) for definitions and evaluation criteria.

Latest updates — Agent Mode docs refreshed for Visual Studio 2022 (Sep 22, 2025).
Links — [Official Site](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode), [Docs](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=vs-2022), [Blog](https://code.visualstudio.com/blogs/)
