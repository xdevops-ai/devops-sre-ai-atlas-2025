---
layout: default
title: Kubiya — ChatOps + Workflow Execution
parent: Platform Directory
---

# Kubiya — ChatOps + Workflow Execution

**Activities**: Y/H | **Diagnostics**: P/M | **Provisioning**: Y/M  
**Event ontology**: P/L | **Observability**: P/L | **Confidence**: Medium

**Build style / interface —** Chat-first platform (Slack and Microsoft Teams) with a web console and CLI; combines conversational AI with a workflow engine and YAML-based automation definitions.  
**What it actually does —** Acts as an AI-powered DevOps and SRE assistant that executes real operational workflows from chat. It provisions infrastructure, runs CI/CD tasks, deploys to Kubernetes, answers operational questions from internal documentation, and orchestrates multi-step remediation workflows with human-in-the-loop approvals.  
**Data / telemetry —** Contextual and operational data from connected systems: chat commands, workflow state, infrastructure metadata, CI/CD events, alert notifications, and internal knowledge bases. Raw metrics and logs remain in external observability platforms and are queried on demand.  
**Interoperability —** Broad integration across the DevOps toolchain: AWS, GCP, Azure, Kubernetes, Terraform, Helm, Argo CD, GitHub/GitLab, CI/CD systems, Jira, ServiceNow, and observability tools. Provides APIs, SDKs, and an open-source runner/CLI for extending workflows.  
**Deployment model —** SaaS control plane with optional self-hosted runners deployed in customer environments; hybrid and enterprise deployments supported.  
**Notes —** Strong focus on self-service operations and delegation via ChatOps; emphasizes execution and workflow orchestration rather than deep diagnostics or native observability.

---

## 🧠 UKM Snapshots
ingest Y/M, index Y/M, retrieval Y/M, governance P/M, overall medium  

**Note:** Leverages internal documentation and runbooks to answer questions and guide workflows; not a general-purpose enterprise knowledge graph.

---

## ⚙️ UAM Snapshots
ingest Y/H, index Y/M, retrieval Y/M, governance Y/M, overall high  

**Note:** Core strength of the platform; supports multi-step automation, approvals, RBAC, and full audit trails for executed actions.

---

## 🔍 UDM Snapshots
ingest P/M, index P/M, retrieval P/M, governance P/L, overall medium  

**Note:** Diagnostics are assisted through queries and context gathering; relies on external tools for detection and RCA.

---

## 👁️ UOM Snapshots
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low  

**Note:** Observability signals are consumed via integrations; Kubiya does not store or analyze telemetry itself.

---

## 🧬 UEOM Snapshots
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low  

**Note:** Event handling is workflow-driven rather than based on a unified event ontology.

---

## 🚀 UPM Snapshots
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high  

**Note:** Supports controlled provisioning and change execution through infrastructure-as-code, cloud APIs, and GitOps tooling.

---

**Latest updates —** Expanded multi-agent capabilities, improved workflow generation from natural language, and broader enterprise integrations (2024–2025).  
**Links —**  
- [Official](https://www.kubiya.ai)  
- [Docs](https://docs.kubiya.ai)  
- [GitHub](https://github.com/kubiya-ai)
