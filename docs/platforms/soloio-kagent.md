---
layout: default
title: Kagent (Solo.io)
parent: Platform Directory
---

# Kagent (Solo.io)

Activities: Y/M | Diagnostics: Y/H | Provisioning: Y/M  <br>
Event ontology: P/M | Observability: Y/H | Confidence: High

**Build style / interface —** Kubernetes-native AI agent framework that orchestrates tools via an open Agent Gateway and MCP servers, with CRDs and the Gateway API.  
**What it actually does —** Orchestrates Prometheus, Grafana, Helm, Argo and other tools for cluster diagnostics, root cause analysis and safe changes. Collects agent and LLM traces along with Kubernetes and Prometheus data.  
**Data / telemetry —** Collects agent and LLM traces plus Kubernetes and Prometheus telemetry for diagnostics and analysis.  
**Interoperability —** Interfaces via MCP servers, custom resource definitions (CRDs) and the Gateway API; integrates with open-source and enterprise Kubernetes clusters and popular observability tools.  
**Deployment model —** Runs inside Kubernetes clusters; the open Agent Gateway is donated to the Linux Foundation with enterprise support available.  
**Notes —** Strong Kubernetes workflows, deep observability integrations and policy hooks; brings extensibility via CRDs and a pluggable gateway.

**UKM Snapshots:**
ingest medium-high, index medium-high, retrieval medium-high, governance medium-high, overall medium-high  <br>
Note: See analysis/baselines/knowledge.md (doc-platform.tar) for definitions and evaluation criteria.







**UAM Snapshots:**
ingest medium-high, index medium-high, retrieval medium-high, governance medium-high, overall medium-high  <br>
Note: See analysis/baselines/activity.md (doc-platform.tar) for definitions and evaluation criteria.






**UDM Snapshots:**
ingest high, index high, retrieval high, governance high, overall high  <br>
Note: See analysis/baselines/diagnostic.md (doc-platform.tar) for definitions and evaluation criteria.






**UOM Snapshots:**
ingest high, index high, retrieval high, governance high, overall high  <br>
**Note:** Instrumentation & Ingest: Y/M; Kagent hooks into a Kubernetes cluster’s observability endpoints; Normalization & Enrichment: Y/M; Data coming from Kubernetes already carries labels (namespace, pod nam
