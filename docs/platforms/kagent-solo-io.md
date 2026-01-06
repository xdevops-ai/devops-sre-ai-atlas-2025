---
layout: default
title: Kagent (Solo.io)
parent: Platform Directory
---

# Kagent — Kubernetes Agent Framework (Solo.io)

**Activities**: Y/M | **Diagnostics**: Y/H | **Provisioning**: Y/M  
**Event ontology**: P/M | **Observability**: Y/H | **Confidence**: High

**Build style / interface —** Kubernetes-native, open-source agent framework deployed in-cluster using CRDs and controllers; optional UI and CLI for agent management.  
**What it actually does —** Runs AI-powered agents inside Kubernetes clusters to diagnose issues, inspect live state, execute remediation actions, and orchestrate operational workflows using tools such as kubectl, Helm, Argo, and Prometheus queries.  
**Data / telemetry —** Live Kubernetes API objects, cluster events, pod logs, and metrics retrieved on demand from Prometheus/Grafana and other in-cluster observability tools.  
**Interoperability —** Strong cloud-native integration via Kubernetes APIs; supports MCP (Model Context Protocol) for tool access and A2A patterns for agent-to-agent communication; integrates with Prometheus, Grafana, Istio, Argo CD, Helm, and external LLM providers.  
**Deployment model —** Self-hosted, runs entirely inside Kubernetes clusters; open-source (CNCF Sandbox project).  
**Notes —** Focused on Kubernetes and platform engineering use cases; governance, approvals, and RBAC rely on Kubernetes-native controls and external policy engines rather than a built-in ITSM layer.

---

## 🧠 UKM Snapshots
ingest Y/M, index P/M, retrieval Y/M, governance P/L, overall medium  

**Note:** Knowledge derived from live cluster state, configuration, and retrieved documentation; no centralized long-term enterprise knowledge base by default.

---

## ⚙️ UAM Snapshots
ingest Y/M, index Y/M, retrieval Y/M, governance P/M, overall medium-high  

**Note:** Captures agent actions, tool invocations, and remediation steps as structured activity flows; replay and approval depend on surrounding platform controls.

---

## 🔍 UDM Snapshots
ingest Y/H, index Y/M, retrieval Y/M, governance Y/M, overall high  

**Note:** Strong Kubernetes-centric diagnostics using live queries, logs, events, and dependency inspection; RCA is evidence-driven but scoped to cluster context.

---

## 👁️ UOM Snapshots
ingest Y/H, index Y/M, retrieval Y/H, governance Y/M, overall high  

**Note:** Leverages existing observability stacks (Prometheus, Grafana, logs) with deep contextual navigation rather than storing telemetry itself.

---

## 🧬 UEOM Snapshots
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium  

**Note:** Entity model centers on Kubernetes primitives (clusters, namespaces, pods, services, workloads) and their relationships.

---

## 🚀 UPM Snapshots
ingest Y/M, index Y/M, retrieval Y/M, governance P/M, overall medium-high  

**Note:** Supports controlled execution of kubectl, Helm, and Argo-based changes; rollback and safety depend on underlying Kubernetes and GitOps tooling.

---

**Latest updates —** Accepted into CNCF Sandbox; rapid community growth and expanded MCP-based tool integrations (2024–2025).  
**Links —**  
- https://kagent.dev  
- https://docs.kagent.dev  
- https://github.com/kagent-dev/kagent
