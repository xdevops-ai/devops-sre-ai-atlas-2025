---
layout: default
title: Microsoft Azure SRE Agent
parent: Platform Directory
---

# Microsoft Azure SRE Agent

**Activities**: Y/M | **Diagnostics**: Y/M | **Provisioning**: P/M  <br>
**Event ontology**: P/M | **Observability**: Y/M | **Confidence**: High

**Build style / interface —** Azure Portal; chat + action timeline.  
**What it actually does —** Diagnoses issues from Azure telemetry and can execute mitigations with approvals; billed via Azure Agent Units (AAU).  
**Data / telemetry —** Azure Monitor and Logs.  
**Interoperability —** Hooks into Azure services, GitHub/PagerDuty (via integrations).  
**Deployment model —** Azure managed service.  
**Notes —** Scoped to Azure; approval-gated actions.

**UKM Snapshots:**  
context learning P/M, overall medium

**UAM Snapshots:**  
timeline Y/M, approvals Y/M, overall medium

**UDM Snapshots:**  
diagnosis Y/M, suggestions Y/M, overall medium

**UOM Snapshots:**  
Azure signals Y/M

**UEOM Snapshots:**  
resource graph P/M

**UPM Snapshots:**  
mitigations P/M (approval-gated)

**Latest updates —** Preview billing started Sept 1, 2025 (AAU).  
**Links —** [Product](https://azure.microsoft.com/en-us/products/sre-agent), [Docs – Overview](https://learn.microsoft.com/en-us/azure/sre-agent/overview), [Docs – Billing](https://learn.microsoft.com/en-us/azure/sre-agent/billing)
