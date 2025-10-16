---
layout: default
title: Elastic AI Assistant
parent: Platform Directory
---

# Elastic AI Assistant

Activities: P/M | Diagnostics: P/M | Provisioning: N/L  
Event ontology: P/M | Observability: Y/M | Confidence: Medium

Build style / interface — Integrated into Elastic Observability (Kibana) with contextual prompts and chat.  
What it actually does — Explains errors and logs with actionable fixes, answers questions like "why is latency high?", recommends queries and visualizations, and surfaces runbooks with the option to execute them for known issues.  
Data / telemetry — Elastic full-stack data (metrics, logs, traces, APM profiles) grounded via ESRE; can include your organization’s knowledge base via connectors and RAG.  
Interoperability — Works with user-provided LLMs or Elastic Cloud LLM; supports content connectors and can trigger Elastic Actions or external workflows.  
Deployment model — Runs on the Elastic Stack (self-hosted) or Elastic Cloud.  
Notes — A human assistant that accelerates root-cause analysis and onboarding.

UKM Snapshots: 
ingest Y/M, index Y/M, retrieval Y/M, governance P/M, overall medium
Note:   See analysis/baselines/knowledge.md (doc-platform.tar) for definitions and evaluation criteria.

UAM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/activity.md (doc-platform.tar) for definitions and evaluation criteria.
UDM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/diagnostic.md (doc-platform.tar) for definitions and evaluation criteria.
UOM Snapshots:   
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high
Note:   See analysis/baselines/observability.md (doc-platform.tar) for definitions and evaluation criteria.
UEOM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/ontology.md (doc-platform.tar) for definitions and evaluation criteria.
UPM Snapshots:   
ingest N/L, index N/L, retrieval N/L, governance N/L, overall low
Note:   See analysis/baselines/provisioning.md (doc-platform.tar) for definitions and evaluation criteria.

Latest updates — Elastic expands AI Assistant docs for Observability & Security (2025).
Links — [Official Site](https://www.elastic.co/elasticsearch/ai-assistant), [Docs](https://www.elastic.co/docs/solutions/observability/observability-ai-assistant), [Blog](https://www.elastic.co/docs/solutions/security/ai/ai-assistant)
