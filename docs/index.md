---
layout: default
title: Home
nav_order: 1
---

# DevOps & SRE AI Platforms Atlas 2025

**A vendor-neutral, community-driven wiki** -- **Last updated: {{ site.time | date: '%B %d, %Y' }}**

![GitHub](https://img.shields.io/badge/version-2025.10-blue) ![GitHub](https://img.shields.io/badge/platforms-25+-green) ![GitHub](https://img.shields.io/badge/status-active-brightgreen)

## What This Is

This atlas provides comprehensive, evidence-based analysis of AI agent platforms across the DevOps/SRE/ITOps ecosystem.

**Key Features:**

- Vendor-neutral analysis -- No hype, just capabilities
- Community-driven -- Contributions welcome
- Structured data -- Machine-readable platform information
- Actionable insights -- Real implementation guidance

## Quick Navigation

- **[Platform Archetypes]({{ '/archetypes/' | relative_url }})** -- Strengths/weaknesses by category
- **[Platform Overview]({{ '/platform-overview/' | relative_url }})** -- One-page summary of all platforms
- **[Platform Directory]({{ '/platforms/' | relative_url }})** -- Deep dives with capability scoring
- **[Capability Framework]({{ '/capabilities/' | relative_url }})** -- How we score vendors
- **[Community Resources]({{ '/community/' | relative_url }})** -- Contribute, discuss, roadmap

## Executive Summary -- DevOps & SRE AI Platforms (Oct 11, 2025)

**The headline:** AI agents for DevOps/SRE have progressed from "chat over dashboards" to actionable co‑workers spanning triage → RCA → guided remediation → post‑incident learning. No single vendor covers the full lifecycle; the 2025 winning pattern is composable adoption: anchor on an observability‑first triage brain, add a workflow orchestrator for approvals/audit, and layer in guardrailed provisioning for safe apply/rollback.

### Market map at a glance

| Archetype | Best fit | Representative platforms | Core strength | Typical limits |
| --- | --- | --- | --- | --- |
| Observability‑First | Fast triage, RCA, incident comms | Dynatrace Davis AI; Cisco (Splunk) AI Agents; Datadog Bits AI & Agents; Elastic AI Assistant; New Relic AI | Multi‑signal correlation, causal/hypothesis reasoning, narrative updates | Usually no direct apply beyond playbooks; relies on external approvals |
| Provisioning‑Focused | Safe, repeatable infra changes | Azure Copilot (Agent Mode); DuploCloud; Qovery; Kuberns | Generate/apply IaC with approvals and rollback | Lighter AIOps correlation; observability via integrations |
| Developer‑Centric & Frameworks | Code/PR changes; build your own agents | AWS Strands SDK; Atlassian Rovo Dev; GitHub Copilot Coding Agent; Zencoder; JFrog Fly; Azure AI Agent Service (Foundry) | Planning/tool orchestration, CI/CD fixes, AgentOps | Not a runtime ops console; direct infra apply limited |
| Enterprise Orchestrators | Cross‑team workflows, audit, CMDB | ServiceNow AI Agent Orchestrator; Salesforce Agentforce (OpsAI); PagerDuty AIOps | Ticket/change graph, approvals, runbooks | Deep telemetry depends on observability tools |
| Data & MLOps | AI quality, data pipelines | Databricks Agent Bricks; Snowflake Cortex Agents; Dataiku AI Agents | Evaluations/guardrails, lineage, model operations | Infra ops out of scope |
| Specialized Domain | Deep expertise for a niche | IBM AskIAM (IAM); Solo.io Kagent (K8s) | Accuracy within narrow scope | Limited breadth by design |

### Top 6 takeaways for 2025

1. From chat to action: leaders pair explanations with verifiable evidence (queries/logs/traces) and suggest the next safe step (runbook, PR, or controlled apply).
2. Human‑in‑the‑loop is default: approvals, RBAC and audit trails are table stakes for production change.
3. AgentOps matters: tracing, evaluations and policy hooks (data boundaries, PII controls, prompt safety) separate pilots from production.
4. Event ontology wins RCA: platforms with typed entities + change context consistently outperform generic LLMs on root cause.
5. IaC is the safety rail: even where agents can apply changes, diffs/Bicep/Terraform + approvals remain the safest path.
6. Compose the stack: the best outcomes pair one observability brain + one orchestrator + optional provisioning.

### Quick picks by job‑to‑be‑done

- Rapid triage & RCA with evidence: Dynatrace; Cisco (Splunk); Datadog Bits AI — complement with PagerDuty AIOps for comms/response.
- End‑to‑end incident coordination & comms: PagerDuty AIOps; ServiceNow; Salesforce — complement with your observability suite.
- Direct, approval‑gated infra changes: Azure Copilot (Agent Mode); DuploCloud — complement with Qovery for migration IaC.
- Build governed, bespoke ops agents: Azure AI Agent Service (Foundry); AWS Strands — complement with Dataiku/Databricks for evaluations.
- Repo/CI‑centric fixes (PRs/tests/docs): GitHub Copilot Coding Agent; Atlassian Rovo Dev; Zencoder — complement with JFrog Fly for release policy.
- Kubernetes deep‑dive fixes: Solo.io Kagent — complement with APM/logs.
- Identity requests & compliance: IBM AskIAM.
- Data & MLOps guardrails/evals: Databricks Agent Bricks; Dataiku; Snowflake Cortex Agents.

### Capability trends vs. last edition

- **Diagnostics:** more change‑aware correlation and hypothesis testing; observability tools add post‑mortem drafting and Slack/Teams updates by default.
- **Activities & history:** richer incident timelines and action replays (e.g., “apply last good remediation”), strongest in orchestrators.
- **Provisioning:** clear split—some stay advisory; others (Azure Copilot, DuploCloud) execute with diffs, approvals, rollbacks.
- **Event ontology:** convergence on OTel semantic conventions and CMDB/entity graphs; better joins across alerts, services and changes.
- **Agent observability:** first‑class traces, evaluations, safety scores (Foundry, Dataiku, Databricks, Salesforce Command Center).

### Reference architecture (what “good” looks like)

1. **Telemetry backbone:** OTel + your observability suite (Dynatrace/Splunk/Datadog/Elastic/New Relic).
2. **Orchestration & audit:** ServiceNow or Salesforce; add PagerDuty AIOps for real‑time response.
3. **Provisioning lane:** Azure Copilot (Agent Mode) or DuploCloud for controlled applies; Qovery for migration IaC.
4. **Developer loop:** GitHub Copilot Coding Agent / Atlassian Rovo Dev / Zencoder; JFrog Fly for release policy.
5. **AgentOps layer:** Azure AI Agent Service (Foundry), Dataiku, or Databricks for tracing, evaluations and safety.
6. **Guardrails:** RBAC, approval workflows, drift checks, read‑only dry‑runs by default and immutable audit logs.

### Risks & guardrails to enforce

- **False confidence / silent failures:** require evidence links for every diagnosis; block summary‑only outputs.
- **Unsafe changes:** enforce two‑person approval and automatic rollback plans; prefer IaC diffs over ad‑hoc commands.
- **Vendor lock‑in:** favour platforms with MCP/A2A, exportable traces and open schemas.
- **Cost surprises:** track agent run counts, tool invocations, LLM usage; set SLOs & budgets for agents.

### Bake‑off checklist (pair with Atlas KPIs)

- **TTFC/TTRC:** measure on a fixed incident set, with linked evidence and a verification plan per RCA.
- **Actionability rate:** percentage of cases with a safe next step (rollback/fix or runbook).
- **Closed‑loop rate:** percentage of incidents where the platform proposed and executed a remediation under approvals.
- **AgentOps quality:** presence of traces/evals/guardrails, red‑team tests, data‑boundary controls.
- **Interoperability:** MCP/OTel support; OTel‑CMDB mapping if you use an orchestrator.

---

## Join the Community

This is a living document! Help us keep it current:

- Contribute updates via [GitHub](https://github.com/xdevops-ai/devops-sre-ai-atlas-2025)
- **Join conversations via [GitHub Issues](https://github.com/xdevops-ai/devops-sre-ai-atlas-2025/issues)** (GitHub Discussions is not enabled)
- Report bugs or feature requests via the same Issues link above.
- Meet the team & community at our [Bucharest XDevOps Meetup](https://www.meetup.com/bucharest-xdevops-meetup-group/)

---

*This project is [open source](https://github.com/xdevops-ai/devops-sre-ai-atlas-2025/blob/main/LICENSE) and maintained by the xDevOps community.*
