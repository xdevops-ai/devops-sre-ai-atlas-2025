---
layout: default
title: Azure AI Agent Service Foundry
parent: Platform Directory
---

# Azure AI Agent Service Foundry

**Activities**: Y/M | **Diagnostics**: N/L | **Provisioning**: P/L  <br>
**Event ontology**: P/M | **Observability**: Y/M | **Confidence**: Medium‑High

**Build style / interface —** Azure AI Foundry service and open‑source Agent Framework SDK, with a visual workflow editor and CLI.  
**What it actually does —** Provides an enterprise framework to build, deploy and manage multi‑agent systems with guardrails; orchestrates stateful agent workflows; integrates tools via OpenAPI and the Model Context Protocol (MCP); supports evaluation and AgentOps monitoring.  
**Data / telemetry —** Agent conversation logs, tool invocations, OpenTelemetry traces, governance events and metrics.  
**Interoperability —** Over 1 400 Azure Logic Apps as tools; supports external frameworks such as LangChain and LangGraph; connectors to Microsoft 365 Copilot and other APIs.  
**Deployment model —** Runs as Azure AI Foundry in the cloud with a containerised agent runtime; the SDK is open‑source for local development and cloud deployment.  
**Notes —** Focused on agent workflow orchestration and governance rather than direct human‑facing operations.

**UKM Snapshots:**
ingest Y/M, index P/M, retrieval Y/M, governance Y/H, overall medium  <br>
**Note:** Knowledge: consumes product-native and BYO sources.

**UAM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Activities: agent executes playbooks/workflows with policy; sessionized context

**UDM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Diagnostics: anomaly detection & triage; correlates metrics/traces/logs

**UOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Observability: ingests metrics/traces/logs/events

**UEOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Ontology: product-native with adapters

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: integrates with IaC/tools for apply; cloud-hosted service
**Links —** [Official Site](https://azure.microsoft.com/en-us/products/ai-foundry/agent-service), [Docs](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview), [Blog](https://azure.microsoft.com/en-us/blog/)
