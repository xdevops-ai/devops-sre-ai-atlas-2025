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

UKM Snapshot: ingest P/L, index P/L, retrieval P/M, governance Y/M, overall medium-low.  
UAM Snapshot: ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high.  
UDM Snapshot: ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium.  
UOM Snapshot: ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium.  
UEOM Snapshot: ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium.  
UPM Snapshot: ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high.

Latest updates — GA June 2025 with Agent Mode transforms Copilot for Azure from chat helper to autonomous operator for cloud DevOps; can auto-resolve deployment errors.  
Links — visualstudiomagazine.com (GA coverage), learn.microsoft.com, azure.microsoft.com.
