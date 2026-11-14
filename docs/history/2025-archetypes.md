---
layout: default
title: Historical archetypes (October 2025)
nav_exclude: true
search_exclude: true
permalink: /history/2025-archetypes/
---

> Historical material, not a current purchasing recommendation. See the [buyer guide]({{ "/platform-overview/" | relative_url }}).

# Platform Archetypes Overview

# 🧭 Platform Archetypes — DevOps & SRE AI Platforms (2025 Atlas)
*Understand the major categories of AI platforms and when to use them. This file condenses the Atlas “Platform Archetypes Overview” into a standalone guide.*

**Last updated:** 2025-10-11

---

## Why archetypes?
No single product spans triage → RCA → remediation → post‑incident learning at a “best‑in‑class” level. Teams succeed by **composing** 2–3 archetypes that complement each other. Use this guide to choose the **brain** (triage/RCA), the **hands** (provisioning/change), and the **orchestrator** (workflows/approvals/audit).

---

## 🔎 Quick comparison matrix

| Archetype | Best fit | Representative platforms | Core strength | Typical limits | Typical U‑model highs |
|---|---|---|---|---|---|
| **🔭 Observability‑First** | Rapid triage, RCA, incident comms | Dynatrace Davis AI; Cisco (Splunk) AI Agents; **Datadog Bits AI & Agents**; **Elastic AI Assistant**; **New Relic AI** | Multi‑signal correlation; causal/hypothesis reasoning; live dashboards; post‑mortems | Usually **no direct apply** beyond playbooks; change control via integrations | **UDM**, **UOM** (high); **UAM**/**UEOM** (med‑high); **UPM** (low) |
| **⚙️ Provisioning‑Focused** | Safe infra/app changes with guardrails | **Azure Copilot (Agent Mode)**; DuploCloud; Qovery; Kuberns | IaC diff/plan → approve → apply → verify → rollback | Lighter AIOps; limited evidence for RCA; relies on external obs | **UPM** (high); **UAM** (med); **UOM/UDM** (low‑med) |
| **👨‍💻 Developer‑Centric & Frameworks** | Code/PR changes; build bespoke agents | AWS Strands SDK; Atlassian Rovo Dev; GitHub Copilot Coding Agent; Zencoder; JFrog Fly; **Azure AI Agent Service (Foundry)** | Planning/orchestration, CI fixes, AgentOps (traces/evals) | Not a runtime ops console; limited direct infra apply | **UAM** (med‑high); **UKM/UEOM** (varies); **UPM** (low‑med) |
| **🏢 Enterprise Orchestrators** | Cross‑team workflows, approvals, CMDB | ServiceNow Agent Orchestrator; Salesforce Agentforce (OpsAI); **PagerDuty AIOps** | Ticket/change graph; HIL approvals; runbooks; comms | Deep telemetry depends on obs stack; limited native apply | **UAM/UDM** (high); **UKM/UEOM** (med‑high); **UPM** (med) |
| **📊 Data & MLOps** | AI quality, lineage, pipeline ops | Databricks Agent Bricks; Snowflake Cortex Agents; Dataiku AI Agents | Evals/guardrails, lineage, cost/quality governance | Infra AIOps out of scope; limited live ops | **UKM/UEOM/UAM** (med‑high); **UOM/UDM/UPM** (low‑med) |
| **🎯 Specialized Domain** | Deep accuracy for a niche | IBM AskIAM (IAM); Solo.io **Kagent** (K8s) | Precision in a narrow domain; strong playbooks | Intentional breadth limits | High in one model (e.g., **UPM** for IAM; **UDM/UOM** for K8s) |

> **Reading “U‑model highs”** — which baseline models a given archetype tends to score highest on: **UOM** (Observability), **UDM** (Diagnostics), **UAM** (Activities), **UPM** (Provisioning), **UEOM** (Ontology), **UKM** (Knowledge).

---

## Decision helper — pick by job‑to‑be‑done

- **“We need faster triage with evidence.”** → Start **🔭 Observability‑First**; add **🏢 Orchestrator** for comms/approvals.  
- **“We want safe, auditable changes.”** → Start **⚙️ Provisioning‑Focused**; add **🔭 Observability‑First** for verify & SLO checks.  
- **“We’ll build custom agents with governance.”** → Start **👨‍💻 Developer‑Centric & Frameworks**; add **🏢 Orchestrator** for enterprise routing.  
- **“We live inside tickets/CMDB across many teams.”** → Start **🏢 Orchestrator**; integrate **🔭 Observability‑First** and **⚙️ Provisioning‑Focused** lanes.  
- **“We must measure AI quality & data lineage.”** → Start **📊 Data & MLOps**; integrate with your agent runtime.  
- **“We need accuracy in a narrow domain (IAM/K8s).”** → Add a **🎯 Specialized** agent alongside your main brain/hands.

---

## Evidence to request per archetype
Ask vendors to provide **exportable artifacts** (permalinks/JSON/Markdown) so you can reproduce claims.

- **🔭 Observability‑First:** Alert rule(s), grouped incident record, causal/hypothesis graph, cross‑signal drill‑down links, post‑mortem export.  
- **⚙️ Provisioning‑Focused:** Plan diff, approval trail, execution logs, verification read‑backs, **rollback** evidence.  
- **👨‍💻 Developer‑Centric & Frameworks:** Agent traces (OTel), evaluation suites/metrics, tool registry, reproducible runs.  
- **🏢 Orchestrators:** Workflow definitions, CMDB/graph joins (OTel→CMDB), governance tests (RBAC, tenancy), audit exports.  
- **📊 Data & MLOps:** Eval datasets, guardrail policies, lineage graph, agent run telemetry.  
- **🎯 Specialized:** Domain‑specific test corpus + success criteria; safety/guardrail proofs.

---

## Detailed archetype notes

### 🔭 Observability‑First Agents
**Definition.** Born from APM/monitoring/logging. Excel at anomaly detection, correlation, and causal/hypothesis‑driven RCA with **cross‑signal drill‑downs**.  
**Strengths.** Fast TTFC/TTRC; entity pages; SLO burn; incident narratives & post‑mortems.  
**Limits.** Usually **no direct apply** beyond playbooks; change gates via external systems.  
**Examples.** Dynatrace Davis AI; Cisco (Splunk) AI Agents; **Datadog Bits AI & Agents**; **Elastic AI Assistant**; **New Relic AI**.  
**Typical U‑profile.** **UDM/UOM** high; **UAM/UEOM** med‑high; **UPM** low.

### ⚙️ Provisioning‑Focused Agents
**Definition.** IaC‑driven control planes for plan→approve→apply→verify→rollback under guardrails.  
**Strengths.** Deterministic plans, policy gates, drift checks, **rollback**; direct cloud/K8s changes.  
**Limits.** Limited RCA/correlation; relies on your observability for evidence.  
**Examples.** **Azure Copilot (Agent Mode)**; DuploCloud; Qovery; Kuberns.  
**Typical U‑profile.** **UPM** high; **UAM** med; others low‑med.

### 👨‍💻 Developer‑Centric & Frameworks
**Definition.** Code/PR agents and agent frameworks with strong **AgentOps** (traces/evals/safety).  
**Strengths.** Planning/orchestration; CI fixes; reproducibility; SDK & tool integration (MCP/OpenAPI).  
**Limits.** Not a production ops console; changes often land as PRs rather than live apply.  
**Examples.** AWS Strands SDK; Atlassian Rovo Dev; GitHub Copilot Coding Agent; Zencoder; JFrog Fly; **Azure AI Agent Service (Foundry)**.  
**Typical U‑profile.** **UAM** med‑high; **UKM/UEOM** variable; **UPM** low‑med (PR‑first).

### 🏢 Enterprise Workflow Orchestrators
**Definition.** Low‑code multi‑agent coordinators across ITSM/ITOM with CMDB and approvals.  
**Strengths.** Incident workflows; comms; RBAC/tenancy; **OTel→CMDB** mappings; runbooks.  
**Limits.** Deep telemetry via integrations; limited direct apply.  
**Examples.** ServiceNow AI Agent Orchestrator; Salesforce Agentforce (OpsAI); **PagerDuty AIOps**.  
**Typical U‑profile.** **UAM/UDM** high; **UKM/UEOM** med‑high; **UPM** med (via actions).

### 📊 Data & MLOps Agents
**Definition.** Agentic governance for data/ML: evals, guardrails, lineage, cost/quality.  
**Strengths.** Evaluation harnesses; experiment tracking; trace observability for agents.  
**Limits.** Infra AIOps out of scope; provisioning limited to platform tasks.  
**Examples.** Databricks Agent Bricks; Snowflake Cortex Agents; Dataiku AI Agents.  
**Typical U‑profile.** **UKM/UEOM/UAM** med‑high; others low‑med.

### 🎯 Specialized Domain Agents
**Definition.** High accuracy within a narrow scope (e.g., **IAM** or **Kubernetes**).  
**Strengths.** Deep playbooks; domain primitives; safer auto‑actions in‑scope.  
**Limits.** Limited breadth by design; must be composed with other archetypes.  
**Examples.** IBM AskIAM (IAM); Solo.io **Kagent** (K8s).  
**Typical U‑profile.** One or two models high (e.g., **UPM** in IAM; **UDM/UOM** in K8s).

---

## Integration patterns (compose your stack)

1) **Observability brain + Orchestrator + Provisioning hands**  
- **Use when:** You want fast RCA with evidence, human‑in‑the‑loop approvals, and safe changes.  
- **Shape:** 🔭 + 🏢 + ⚙️

2) **Framework + Orchestrator (enterprise guardrails)**  
- **Use when:** You’ll build tailored agents and need governance and routing.  
- **Shape:** 👨‍💻 + 🏢 (+ 🔭 for evidence)

3) **Specialist + Observability brain (targeted wins)**  
- **Use when:** K8s/IAM pain dominates; add focused automation next to generic triage.  
- **Shape:** 🎯 + 🔭 (+ ⚙️ if changes are frequent)

---

## Evaluation checklist (per archetype)

- **Evidence exportability:** permalinks/JSON/Markdown to reproduce claims.  
- **Cross‑signal drill‑down:** mandatory for 🔭 at Level ≥ 3 (see UOM).  
- **Change safety:** diffs, approvals, rollback proof for ⚙️ at Level ≥ 3 (see UPM).  
- **AgentOps:** traces, evals, safety guards for 👨‍💻 and 🏢.  
- **Ontology:** typed entities & joins for 🏢/🔭 at Level ≥ 3 (see UEOM).  
- **Governance:** RBAC/PII/tenancy tests for any archetype deployed at scale.

---

## Recap — quick list
- **🔭 Observability‑First:** Dynatrace Davis AI; Cisco (Splunk) AI Agents; **Datadog Bits AI & Agents**; **Elastic AI Assistant for Observability**; **New Relic AI**.  
- **⚙️ Provisioning‑Focused:** DuploCloud AI Help Desk; Qovery AI Migration Agent; Kuberns Platform; **Microsoft Azure Copilot (Agent Mode)**.  
- **👨‍💻 Developer‑Centric & Frameworks:** AWS Strands SDK; Atlassian Rovo Dev; GitHub Copilot Coding Agent; Zencoder; JFrog Fly (agentic repo); **Microsoft Azure AI Agent Service (Foundry)**.  
- **🏢 Enterprise Workflow Orchestrators:** ServiceNow AI Agent Orchestrator; Salesforce Agentforce (OpsAI); **PagerDuty AIOps**.  
- **📊 Data & MLOps Agents:** Databricks Agent Bricks; Snowflake Cortex Agents; Dataiku AI Agents.  
- **🎯 Specialized Domain:** IBM AskIAM (IAM); Solo.io Kagent (K8s).

---

### Notes
- Scoring shorthand (**Y/H, Y/M, P/M**…) maps to 0–4 levels per the baseline models.  
- Use the same incident corpus and change sets across vendors for fair comparisons.
