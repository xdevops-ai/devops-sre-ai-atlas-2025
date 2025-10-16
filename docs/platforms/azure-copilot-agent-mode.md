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
**Note:** Coverage — Ingest P/L; Index P/L; Retrieval P/M; Governance Y/M; Overall medium-low


**UAM Snapshots:**   
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high  <br>
**Note:** Coverage — Ingest Y/M; Index Y/M; Retrieval Y/M; Governance Y/M; Overall medium-high


**UDM Snapshots:**   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium  <br>
**Note:** Coverage — Ingest P/M; Index P/M; Retrieval P/M; Governance P/M; Overall medium


**UOM Snapshots:**   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium  <br>
**Note:** Coverage — Ingest P/L; Index P/L; Retrieval P/L; Governance P/L; Overall low-medium


**UEOM Snapshots:**   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium  <br>
**Note:** Coverage — Ingest P/L; Index P/L; Retrieval P/L; Governance P/L; Overall low-medium


**UPM Snapshots:**   
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high  <br>
**Note:** Coverage — Ingest Y/M; Index Y/M; Retrieval Y/M; Governance Y/M; Overall medium-high


**Latest updates —** Agent Mode docs refreshed for Visual Studio 2022 (Sep 22, 2025).
**Links —** [Official Site](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode), [Docs](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=vs-2022), [Blog](https://code.visualstudio.com/blogs/)
