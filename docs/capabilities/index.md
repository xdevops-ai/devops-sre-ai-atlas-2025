---
layout: default
title: Capability Framework
nav_order: 5
permalink: /capabilities/
---

# Capability Framework

**Reviewed 14 November 2026.** The six existing Atlas axes are retained. Current descriptions replace unsupported precision: no numerical score or composite ranking is assigned from a vendor page alone.

## Six complementary questions

| Axis | What to establish |
| --- | --- |
| UKM — Knowledge | What context is retained, retrieved and governed? |
| UAM — Activities | What tasks can be executed, with whose authority and audit trail? |
| UDM — Diagnostics | What evidence supports investigation, diagnosis and verification? |
| UOM — Observability | Is telemetry native, integrated, or only agent tracing? |
| UEOM — Events / ontology | Are there event relationships and topology, or a documented governed ontology? |
| UPM — Provisioning | Can it plan, validate, apply and verify infrastructure changes, or only generate artifacts? |

## Evidence rules

- Documented product surface, availability announcement, preview and vendor claim are different evidence classes.
- **Not verified** is not a zero or a claim of absence.
- Framework extensibility is not a shipped operational capability.
- Telemetry integration is not a native observability backend; agent tracing is not infrastructure monitoring.
- An incident relationship graph is not proof of a general governed ontology.
- Suggested fixes, a PR, and autonomous production writes are distinct. Licensing, approvals and deployment scope matter.
- No customer savings, correctness or speed claim is treated as independently tested.

## Use the matrix in a buying decision

Choose the two or three axes that matter for your actual task. Read the linked record for its deployment, availability and pilot question before interpreting a cell. A wider row is not necessarily a better fit. The [Buyer Guide]({{ "/platform-overview/" | relative_url }}) includes a downloadable scorecard and comparable outcome/cost measures.

## Current evidence matrix

Each linked record contains its official sources, feature availability and limits. Descriptions are editorial mappings, not implementation equivalence with XDevOps.

| Platform | UKM | UAM | UDM | UOM | UEOM | UPM |
| --- | --- | --- | --- | --- | --- | --- |
| [Atlassian Rovo Dev]({{ "/platforms/atlassian-rovo-dev/" | relative_url }}) | Teamwork Graph | code+PR tasks | build/code troubleshooting | Not verified | work-item context | Not verified |
| [AWS DevOps Agent]({{ "/platforms/aws-devops-agent/" | relative_url }}) | runbooks, history and app relationships | SRE tasks through configured integrations and skills | operational investigations | observability integrations | cross-signal and deployment correlation | general provisioning not verified |
| [AWS Strands SDK]({{ "/platforms/aws-strands-sdk/" | relative_url }}) | memory framework | tool execution framework | custom | agent tracing | custom | deployment of agents only |
| [BigPanda AI Incident Assistant]({{ "/platforms/bigpanda-ai-incident-assistant/" | relative_url }}) | knowledge+post-incident analysis | collaboration workflows | investigation | integrated infrastructure signals | ADR correlation context | Not verified |
| [BMC Helix AIOps (ServiceOps)]({{ "/platforms/bmc-helix-aiops/" | relative_url }}) | Not verified | integration automation documented | HelixGPT source-side log analysis in reviewed use case | OpenTelemetry ingestion, filtering and usage dashboards | service-model and event context; broader ontology not verified | Not verified |
| [Ciroos]({{ "/platforms/ciroos/" | relative_url }}) | persistent graph memory | collaboration; actuator scope unverified | cross-domain investigation | connected signals | signal normalization, correlation and temporal topology graph | not verified |
| [Cisco Splunk AI Agents]({{ "/platforms/cisco-splunk-ai-agents/" | relative_url }}) | service context | query+chart tools | natural-language diagnosis | native APM/infra/logs | alert context | Not verified |
| [Cleric]({{ "/platforms/cleric/" | relative_url }}) | retained infrastructure context | fix PRs and issues; writes opt-in | alert investigation and change verification | integrations and production verification | alert grouping; general ontology unverified | not verified |
| [Databricks Agent Bricks]({{ "/platforms/databricks-agent-bricks/" | relative_url }}) | search+memory | durable runtime+sandbox | custom | MLflow agent tracing | custom | agent runtime hosting |
| [Datadog Bits Investigation]({{ "/platforms/datadog-bits-ai/" | relative_url }}) | investigation context | investigation execution | production investigation | native telemetry | monitor+incident context | Not verified |
| [Dataiku AI Agents]({{ "/platforms/dataiku-ai-agents/" | relative_url }}) | data+tools | custom tools | custom | agent evaluation, not infra monitoring | custom | agent deployment only |
| [Dell APEX AIOps (Moogsoft)]({{ "/platforms/dell-apex-aiops/" | relative_url }}) | Not verified | incident management | incident analysis scope | application observability module | incident correlation lineage | Not verified |
| [DuploCloud AI Help Desk]({{ "/platforms/duplocloud-ai-help-desk/" | relative_url }}) | ticket context/history | supervised production commands | task investigation | Not verified | ticket relationships only | platform tasks, scope-dependent |
| [Dynatrace Intelligence and Assist]({{ "/platforms/dynatrace-davis-ai/" | relative_url }}) | shared guides | agentic queries+workflow integration | troubleshooting | native telemetry | contextual topology | Not verified |
| [Elastic Agent Builder and legacy AI Assistant]({{ "/platforms/elastic-ai-assistant/" | relative_url }}) | legacy knowledge base, successor gaps | workflow integration | investigation skills preview | native telemetry | service map context | Not verified |
| [Firefly (Agentic Cloud Automation)]({{ "/platforms/firefly-agentic-cloud-automation/" | relative_url }}) | cloud system-of-record | drift+recovery workflows | misconfiguration investigation | inventory+drift, not full APM | dependency graph | IaC generation+recovery |
| [Gemini Cloud Assist (formerly Duet)]({{ "/platforms/google-duet-ai-ops/" | relative_url }}) | operational memory/context | guided tools | investigations with access restrictions | GCP signals | topology+alert clustering | IaC generation |
| [Gemini Enterprise Agent Platform (formerly Vertex Agent Builder)]({{ "/platforms/google-vertex-agent-builder/" | relative_url }}) | grounded data | agent framework | custom | model+agent monitoring | custom | agent deployment only |
| [GitHub Copilot Coding Agent]({{ "/platforms/github-copilot-coding-agent/" | relative_url }}) | repo context | code+PR automation | code debugging | Not verified | issue+PR context | code output, not managed infra |
| [GitHub Copilot in VS Code (legacy Azure label)]({{ "/platforms/azure-copilot-agent-mode/" | relative_url }}) | repo memory | tools+terminal | code assistance | Not verified | Not verified | custom tools only |
| [GitLab Duo]({{ "/platforms/gitlab-duo/" | relative_url }}) | repo context | SDLC agents | code/pipeline assistance | Not verified | SDLC context | CI-driven, not generic |
| [Grafana Assistant]({{ "/platforms/grafana-assistant/" | relative_url }}) | skills and runbook context | triggered investigations; code-fix sandboxes preview | multi-step investigations | native Grafana Cloud telemetry and visualization | Watchers and incident triggers; generic ontology unverified | not verified |
| [Harness AI (incl. Harness MCP Server)]({{ "/platforms/harness-ai/" | relative_url }}) | SDLC graph+memory | delivery worker agents | failure investigation | delivery+cost signals | pipeline/deployment graph | IaC/deployments |
| [HashiCorp Terraform MCP + Project Infragraph]({{ "/platforms/hashicorp-terraform-mcp-infragraph/" | relative_url }}) | registry context | MCP tool interface | Not verified | Not verified | Infragraph unverified | Terraform workflow assistance |
| [HPE OpsRamp]({{ "/platforms/hpe-opsramp/" | relative_url }}) | conversation context | alert policy management+automation | operational troubleshooting | native monitoring+logs | service maps+alerts | Not verified |
| [IBM AskIAM]({{ "/platforms/ibm-askiam/" | relative_url }}) | IAM knowledge | access requests+approvals | identity intelligence | Not verified | identity relationships | user provisioning only |
| [IBM Instana + Turbonomic + watsonx]({{ "/platforms/ibm-instana-turbonomic-watsonx/" | relative_url }}) | contextual insights | optimization actions | intelligent investigation | native Instana telemetry | application entities | resource optimization, not general provisioning |
| [incident.io (AI SRE)]({{ "/platforms/incident-io/" | relative_url }}) | operational context | response coordination | parallel evidence-backed investigations | integrated telemetry | incident relationships | Not verified |
| [JFrog Fly transition to JFrog Platform]({{ "/platforms/jfrog-fly-agentic-repo/" | relative_url }}) | package context | release workflows | Not verified | Not verified | artifact metadata | artifact delivery, not infra provisioning |
| [Kagent (Solo.io)]({{ "/platforms/soloio-kagent/" | relative_url }}) | custom | Kubernetes agent orchestration | tool-dependent | agent/runtime context | custom | agent deployment |
| [Komodor / Klaudia]({{ "/platforms/komodor-klaudia/" | relative_url }}) | persistent memory and knowledge graphs | built-in and custom governed workflows | Kubernetes investigations | operational integrations and optimization | Alert Intelligence and context | broad infrastructure provisioning not verified |
| [Kuberns Platform]({{ "/platforms/kuberns-platform/" | relative_url }}) | Not verified | deployment automation claimed | Not verified | monitoring claimed | Not verified | deployment+scaling claimed |
| [Kubiya — ChatOps + Workflow Execution]({{ "/platforms/kubiya/" | relative_url }}) | Context Graph | governed workflows | tool-dependent | integrated | graph, ontology scope unproven | infrastructure workflows |
| [LogicMonitor Edwin AI]({{ "/platforms/logicmonitor-aiops/" | relative_url }}) | private/public knowledge agents | action groups | AI investigations | native+integrated telemetry | normalized events+correlation | Not verified |
| [Microsoft Azure SRE Agent]({{ "/platforms/microsoft-azure-sre-agent/" | relative_url }}) | retained context | schedules+governed automation | investigations | Azure+partner signals | deployment correlation | permitted CLI scope, not universal |
| [Microsoft Foundry Agent Service]({{ "/platforms/azure-ai-agent-service-foundry/" | relative_url }}) | search+tools | managed agent runtime | custom | agent tracing/evals | custom | agent hosting only |
| [NeuBird AI]({{ "/platforms/neubird-ai/" | relative_url }}) | project instructions and history | investigation initiation and status; infrastructure writes unverified | incident investigation | cloud and monitoring integrations | incident history; generic ontology unverified | not verified |
| [New Relic Autopilot]({{ "/platforms/new-relic-ai/" | relative_url }}) | runbooks+retrospectives | investigation tasks | RCA+recommendations | native telemetry | incident context | Not verified |
| [Opsera Hummingbird]({{ "/platforms/opsera-hummingbird/" | relative_url }}) | toolchain context | pipeline automation | pipeline failure explanation | SDLC metrics, not APM | toolchain relationships | workflows/integrations |
| [PagerDuty AIOps / Paige (SRE Agent)]({{ "/platforms/pagerduty-aiops/" | relative_url }}) | connector/skill context | workflows | investigation | integrated logs+metrics | event correlation | Not verified |
| [Qovery Migration Agent]({{ "/platforms/qovery-migration-agent/" | relative_url }}) | provider app context | file-generation workflow | manifest validation | Not verified | Not verified | Terraform+Dockerfile generation |
| [Resolve AI]({{ "/platforms/resolve-ai/" | relative_url }}) | production memory | governed operational tasks | multi-agent production investigation | integrated evidence | triage and contextual relationships; generic ontology unverified | generic provisioning not verified |
| [Robusta / HolmesGPT]({{ "/platforms/robusta-holmesgpt/" | relative_url }}) | investigation history and context | investigation tools; dangerous calls approval-gated | incident investigation | integrated telemetry; not a full replacement backend | alert timelines; general ontology unverified | not verified |
| [Rootly — Incident Response Automation]({{ "/platforms/Rootly/" | relative_url }}) | incident evidence/history | incident workflows | AI investigation | integrated telemetry | alerts+incident context | Not verified |
| [Salesforce Agentforce]({{ "/platforms/salesforce-agentforce-opsai/" | relative_url }}) | Salesforce context | business+IT service actions | ticket support | agent optimization not infra APM | customer/workflow context | Not verified |
| [Servicenow AI Agent Orchestrator]({{ "/platforms/servicenow-ai-agent-orchestrator/" | relative_url }}) | enterprise context | workflow automation | IT-specific agents scope-dependent | ITOM separate module | CMDB context separate | workflow-dependent |
| [Snowflake Cortex Agents]({{ "/platforms/snowflake-cortex-agents/" | relative_url }}) | enterprise data/retrieval | tool+code execution | custom | agent monitoring | custom | agent runtime only |
| [Snyk — DevSecOps Automation]({{ "/platforms/snyk/" | relative_url }}) | vulnerability knowledge | fix PR workflows | security analysis | security findings not APM | dependency relationships | IaC scanning not provisioning |
| [GloriaOps (early access; Termius link lineage)]({{ "/platforms/termius-gloria/" | relative_url }}) | vendor-described infrastructure context | structured operations and approval plans, early-access claim | alert-triggered read-only investigation, vendor-described | connected infrastructure signals; backend coverage unverified | live infrastructure model described; generic ontology unverified | general provisioning not verified |
| [Traversal]({{ "/platforms/traversal/" | relative_url }}) | Knowledge Bank | remediation execution unverified: source conflict | causal investigation positioning | integrated observability | live entities, dependencies and alert correlation | not verified |
| [xMatters — Operations Automation]({{ "/platforms/xMatters/" | relative_url }}) | workflow context | deterministic incident automation | Not verified | integrations | alert-triggered flows | custom integration-dependent |
| [Zencoder AI Agents]({{ "/platforms/zencoder-ai-agents/" | relative_url }}) | codebase context | code/test/review agents | code verification | Not verified | Not verified | Not verified |

## Baselines and history

The existing baselines remain useful acceptance checklists. They are not proof that any vendor currently meets each criterion.

- [UKM baseline]({{ "/capabilities/baselines/ukm/" | relative_url }})
- [UAM baseline]({{ "/capabilities/baselines/uam/" | relative_url }})
- [UDM baseline]({{ "/capabilities/baselines/udm/" | relative_url }})
- [UOM baseline]({{ "/capabilities/baselines/uom/" | relative_url }})
- [UEOM baseline]({{ "/capabilities/baselines/ueom/" | relative_url }})
- [UPM baseline]({{ "/capabilities/baselines/upm/" | relative_url }})

[Historical scores]({{ "/capabilities/historical-scores/" | relative_url }}) are preserved for traceability but have not been revalidated. Legacy ratings pages and long-form comparisons are historical background, not the current evidence layer.
