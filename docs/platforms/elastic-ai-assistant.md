---
layout: default
title: Elastic AI Assistant
parent: Platform Directory
---

# Elastic AI Assistant

**Activities**: P/M | **Diagnostics**: P/M | **Provisioning**: N/L  <br>
**Event ontology**: P/M | **Observability**: Y/M | **Confidence**: Medium

**Build style / interface —** Integrated into Elastic Observability (Kibana) with contextual prompts and chat.  
**What it actually does —** Explains errors and logs with actionable fixes, answers questions like "why is latency high?", recommends queries and visualizations, and surfaces runbooks with the option to execute them for known issues.  
**Data / telemetry —** Elastic full-stack data (metrics, logs, traces, APM profiles) grounded via ESRE; can include your organization’s knowledge base via connectors and RAG.  
**Interoperability —** Works with user-provided LLMs or Elastic Cloud LLM; supports content connectors and can trigger Elastic Actions or external workflows.  
**Deployment model —** Runs on the Elastic Stack (self-hosted) or Elastic Cloud.  
**Notes —** A human assistant that accelerates root-cause analysis and onboarding.

**UKM Snapshots:**
ingest Y/M, index Y/M, retrieval Y/M, governance P/M, overall medium  <br>
**Note:** Knowledge: BYO sources; governed ingestion & indexing.

**UAM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Activities: agent executes playbooks/workflows with policy

**UDM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Diagnostics: root-cause analysis with causal signals; correlates metrics/traces/logs

**UOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Observability: ingests metrics/traces/logs/events

**UEOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Ontology: product-native with adapters

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: SaaS-managed; limited direct apply; cloud-hosted service
**Links —** [Official Site](https://www.elastic.co/elasticsearch/ai-assistant), [Docs](https://www.elastic.co/docs/solutions/observability/observability-ai-assistant), [Blog](https://www.elastic.co/docs/solutions/security/ai/ai-assistant)
