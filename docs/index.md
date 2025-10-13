---
layout: default
title: Home
nav_order: 1
---

# 🚀 DevOps & SRE AI Platforms Atlas 2025

> **A vendor-neutral, community-driven wiki** · **Last updated: {{ site.time | date: '%B %d, %Y' }}**

![GitHub](https://img.shields.io/badge/version-2025.10-blue)
![GitHub](https://img.shields.io/badge/platforms-25+-green)
![GitHub](https://img.shields.io/badge/status-active-brightgreen)

## 🌟 What This Is

This atlas provides comprehensive, evidence-based analysis of AI agent platforms across the DevOps/SRE/ITOps ecosystem. 

**Key Features:**
- 🔍 **Vendor-neutral analysis** - No hype, just capabilities
- 🤝 **Community-driven** - Contributions welcome
- 📊 **Structured data** - Machine-readable platform information
- 🎯 **Actionable insights** - Real implementation guidance

## 📒 Quick Navigation

### [Platform Archetypes](/docs/archetypes.md)
Understand the different categories of AI platforms and their strengths/weaknesses.

### [Platform Directory](/docs/platforms/)
Detailed analysis of individual AI platforms with capability scoring.

### [Capability Framework](/docs/capabilities.md)
Our methodology for evaluating and comparing platforms.

### [Community Resources](/docs/community.md)
Contribution guidelines, discussion forums, and use cases.

## 🧭 Executive Summary — DevOps & SRE AI Platforms (Oct 11, 2025)

**The headline:** AI agents for DevOps/SRE have progressed from “chat over dashboards” to **actionable co‑workers** spanning **triage → RCA → guided remediation → post‑incident learning**. No single vendor covers the full lifecycle; the 2025 winning pattern is **composable adoption**: anchor on an **observability‑first triage brain**, add a **workflow orchestrator** for approvals/audit, and layer in **guardrailed provisioning** for safe apply/rollback.

### Market map at a glance
| Archetype | Best fit | Representative platforms | Core strength | Typical limits |
|---|---|---|---|---|
| **🔭 Observability‑First** | Fast triage, RCA, incident comms | Dynatrace Davis AI; Cisco (Splunk) AI Agents; **Datadog Bits AI & Agents**; **Elastic AI Assistant**; **New Relic AI** | Multi‑signal correlation, causal/hypothesis reasoning, narrative updates | Usually **no direct apply** beyond playbooks; relies on external approvals |
| **⚙️ Provisioning‑Focused** | Safe, repeatable infra changes | **Azure Copilot (Agent Mode)**; DuploCloud; Qovery; Kuberns | Generate/apply IaC with approvals and rollback | Lighter AIOps correlation; observability via integrations |
| **👨‍💻 Developer‑Centric & Frameworks** | Code/PR changes; build your own agents | AWS Strands SDK; Atlassian Rovo Dev; GitHub Copilot Coding Agent; Zencoder; JFrog Fly; **Azure AI Agent Service (Foundry)** | Planning/tool orchestration, CI/CD fixes, AgentOps | Not a runtime ops console; direct infra apply limited |
| **🏢 Enterprise Orchestrators** | Cross‑team workflows, audit, CMDB | ServiceNow AI Agent Orchestrator; Salesforce Agentforce (OpsAI); **PagerDuty AIOps** | Ticket/change graph, approvals, runbooks | Deep telemetry depends on observability tools |
| **📊 Data & MLOps** | AI quality, data pipelines | Databricks Agent Bricks; Snowflake Cortex Agents; Dataiku AI Agents | Evals/guardrails, lineage, model ops | Infra ops out of scope |
| **🎯 Specialized Domain** | Deep expertise for a niche | IBM AskIAM (IAM); Solo.io Kagent (K8s) | Accuracy within narrow scope | Limited breadth by design |

### Top 6 takeaways for 2025
1. **From chat to action:** Leaders pair **explanations with verifiable evidence** (queries/logs/traces) and **suggest the next safe step** (runbook, PR, or controlled apply).  
2. **Human‑in‑the‑loop is default:** Approvals, RBAC, and audit trails are table stakes for production change.  
3. **AgentOps matters:** Tracing, evaluations, and policy hooks (data boundaries, PII controls, prompt safety) separate pilots from production.  
4. **Event ontology wins RCA:** Platforms with **typed entities + change context** consistently outperform generic LLMs on root cause.  
5. **IaC is the safety rail:** Even where agents can apply changes, **diffs/Bicep/Terraform + approvals** remain the safest path.  
6. **Compose the stack:** The best outcomes pair **one observability brain + one orchestrator + optional provisioning**.

### Quick picks by job‑to‑be‑done
- **Rapid triage & RCA with evidence:** Dynatrace; Cisco (Splunk); **Datadog Bits AI** · *(complement: PagerDuty AIOps for comms/response)*.  
- **End‑to‑end incident coordination & comms:** **PagerDuty AIOps**; ServiceNow; Salesforce · *(complement: your observability suite)*.  
- **Direct, approval‑gated infra changes:** **Azure Copilot (Agent Mode)**; DuploCloud · *(complement: Qovery for migration IaC)*.  
- **Build governed, bespoke ops agents:** **Azure AI Agent Service (Foundry)**; AWS Strands · *(complement: Dataiku/Databricks for evals)*.  
- **Repo/CI‑centric fixes (PRs/tests/docs):** GitHub Copilot Coding Agent; Atlassian Rovo Dev; Zencoder · *(complement: JFrog Fly for release policy)*.  
- **Kubernetes deep‑dive fixes:** Solo.io Kagent · *(complement: APM/logs)*.  
- **Identity requests & compliance:** IBM AskIAM.  
- **Data & MLOps guardrails/evals:** Databricks Agent Bricks; Dataiku; Snowflake Cortex Agents.

### Capability trends vs. last edition
- **Diagnostics:** More **change‑aware correlation** and **hypothesis testing**; observability tools add **post‑mortem drafting** and **Slack/Teams updates** by default.  
- **Activities & history:** Richer **incident timelines** and **action replays** (e.g., “apply last good remediation”), strongest in orchestrators.  
- **Provisioning:** Clear split—some stay advisory; others (Azure Copilot, DuploCloud) execute with **diffs, approvals, rollbacks**.  
- **Event ontology:** Convergence on **OTel semantic conventions** and CMDB/entity graphs; better joins across **alerts ↔ services ↔ changes**.  
- **Agent observability:** First‑class **traces, evaluations, safety scores** (Foundry, Dataiku, Databricks, Salesforce Command Center).

### Reference architecture (what “good” looks like)
1. **Telemetry backbone:** OTel + your observability suite (Dynatrace/Splunk/Datadog/Elastic/New Relic).  
2. **Orchestration & audit:** ServiceNow or Salesforce; add **PagerDuty AIOps** for real‑time response.  
3. **Provisioning lane:** **Azure Copilot (Agent Mode)** or DuploCloud for controlled applies; Qovery for migration IaC.  
4. **Developer loop:** GitHub Copilot Coding Agent / Atlassian Rovo Dev / Zencoder; JFrog Fly for release policy.  
5. **AgentOps layer:** Azure AI Agent Service (Foundry), Dataiku, or Databricks for **tracing, evals, safety**.  
6. **Guardrails:** RBAC, approval workflows, drift checks, **read‑only dry‑runs by default**, and **immutable audit logs**.

### Risks & guardrails to enforce
- **False confidence / silent failures:** Require **evidence links** for every diagnosis; block “summary‑only” outputs.  
- **Unsafe changes:** Enforce **two‑person approval** and **automatic rollback plans**; prefer **IaC diffs** over ad‑hoc commands.  
- **Vendor lock‑in:** Favor platforms with **MCP/A2A**, exportable traces, and **open schemas**.  
- **Cost surprises:** Track **agent run counts, tool invocations, LLM usage**; set SLOs & budgets for agents.

### Bake‑off checklist (pair with Atlas KPIs)
- **TTFC/TTRC** on a fixed incident set, with **linked evidence** and a **verification plan** per RCA.  
- **Actionability rate:** % of cases with a safe next step (rollback/fix or runbook).  
- **Closed‑loop rate:** % of incidents where the platform **proposed and executed** a remediation under approvals.  
- **AgentOps quality:** Presence of **traces/evals/guardrails**, red‑team tests, **data boundary controls**.  
- **Interoperability:** MCP/OTel support; **OTel→CMDB** mapping if you use an orchestrator.
---

## 🤝 Join the Community

This is a living document! Help us keep it current:

- 📝 **Contribute updates** via [GitHub](https://github.com/xdevops.ai/devops-sre-ai-atlas-2025)
- 🔎 **Join discussions** in [GitHub Discussions](https://github.com/xdevops.ai/devops-sre-ai-atlas-2025/discussions)
- 🐛 **Report issues** via [GitHub Issues](https://github.com/xdevops.ai/devops-sre-ai-atlas-2025/issues)
- 🎟️ **Meet the team & community** at our [Bucharest XDevOps Meetup](https://www.meetup.com/bucharest-xdevops-meetup-group/)

---

*This project is [open source](MIT) and maintained by the xDevOps community.*
