---
layout: default
title: Kagent (Solo.io)
parent: Platform Directory
---

# Kagent (Solo.io)

**Activities**: Y/M | **Diagnostics**: Y/H | **Provisioning**: Y/M  <br>
**Event ontology**: P/M | **Observability**: Y/H | **Confidence**: High

**Build style / interface —** Kubernetes-native AI agent framework that orchestrates tools via an open Agent Gateway and MCP servers, with CRDs and the Gateway API.  
**What it actually does —** Orchestrates Prometheus, Grafana, Helm, Argo and other tools for cluster diagnostics, root cause analysis and safe changes. Collects agent and LLM traces along with Kubernetes and Prometheus data.  
**Data / telemetry —** Collects agent and LLM traces plus Kubernetes and Prometheus telemetry for diagnostics and analysis.  
**Interoperability —** Interfaces via MCP servers, custom resource definitions (CRDs) and the Gateway API; integrates with open-source and enterprise Kubernetes clusters and popular observability tools.  
**Deployment model —** Runs inside Kubernetes clusters; the open Agent Gateway is donated to the Linux Foundation with enterprise support available.  
**Notes —** Strong Kubernetes workflows, deep observability integrations and policy hooks; brings extensibility via CRDs and a pluggable gateway.

**UKM Snapshots:**
ingest medium-high, index medium-high, retrieval medium-high, governance medium-high, overall medium-high  <br>
**Note:** Knowledge: consumes product-native and BYO sources.

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
**Note:** Ontology: normalizes to standard schemas

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: integrates with IaC/tools for apply; Kubernetes aware
**Links —** [Official Site](https://www.solo.io/products/kagent-enterprise), [Docs](https://www.solo.io/blog/bringing-agentic-ai-to-kubernetes-contributing-kagent-to-cncf), [Blog](https://www.globenewswire.com/news-release/2025/09/15/3150169/0/en/Solo-io-Announces-Kagent-Enterprise-to-Bridge-the-Agentic-Infrastructure-Gap-Between-Kubernetes-and-AI.html)
