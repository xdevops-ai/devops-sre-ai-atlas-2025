---
layout: default
title: Platform Overview
nav_order: 3
permalink: /platform-overview/
---

# 📋 DevOps & SRE AI Platforms — 2025 Atlas (Updated October 11, 2025)

> **What this is:** A vendor‑neutral overview of AI agent platforms across DevOps/SRE/ITOps and data/MLOps.  

---
# 🧭 Legend — DevOps Agent Atlas 2025

| Symbol | Meaning |
|:-------|:---------|
| **Y/H** | Yes / High — mature, advanced capability |
| **Y/M** | Yes / Medium — strong but not complete |
| **Y/L** | Yes / Low — basic implementation |
| **P/H** | Partial / High — advanced but limited scope |
| **P/M** | Partial / Medium — moderate capability |
| **P/L** | Partial / Low — early or narrow capability |
| **N/L** | None / Low — minimal or no implementation |

---

## 🧩 Emoji Key

| Emoji | Section | Description |
|:------|:--------|:------------|
| 🧩 | **Platform header** | Platform / product name |
| ⚙️ | **Activities** *(UAM)* | Task automation & history |
| 🔍 | **Diagnostics** *(UDM)* | Detection, correlation, RCA |
| 🚀 | **Provisioning** *(UPM)* | Safe infra/apply (plan/approve/apply/rollback) |
| 🧬 | **Event Ontology** *(UEOM)* | Data model & relationships |
| 👁️ | **Observability** *(UOM)* | Telemetry depth (metrics/logs/traces) |
| 🧠 | **Knowledge layer (UKM)** | Ingest / Normalize / Index / Retrieve / Govern |
| 📈 | **Confidence** | Maturity & evidence |
| 🏗️ | **Build style / interface** | Code-first vs. low-code |
| 💡 | **What it actually does** | Core value |
| 📊 | **Data / telemetry** | Key signals used |
| 🔗 | **Interoperability** | Ecosystem & protocols |
| 🏢 | **Deployment model** | SaaS / self-hosted / cloud |
| 🗒️ | **Notes** | Caveats |

> **Note:** We reserve **🧠** for the **Knowledge layer (UKM)** and **🧬** for **Event Ontology (UEOM)**. The document title uses 📋 to avoid emoji conflicts.

---

💡 **Usage:**  
Every platform section follows the same schema so you can compare capabilities at a glance.  
The combination of emoji + short labels ensures quick scanning for SREs, analysts, and engineers reviewing the Atlas.

---

# 🧩 Capability Explanations — Exhaustive Guide

This section defines each Atlas capability with **clear boundaries**, **what counts / does not count**, **evidence you should collect**, and a **scoring rubric** for Y / P / N with maturity (Low/Medium/High). Use it to evaluate vendors consistently and to avoid ambiguity during bake‑offs.

> **How to use:** For each capability, validate with artifacts (screenshots, API outputs, logs, PRs, dashboards) and mark the **highest level that is fully satisfied**. When in doubt, choose the **lower** level and add a note.

---
## 🧩 Capability Explanations — Knowledge & Contextual Intelligence Layer

This section defines how an AI system can **represent, ingest, and use organizational knowledge** — from infrastructure topology and DevOps workflows to individual engineer expertise and contextual storytelling.  
It allows retrieval-augmented agents (diag, activity, etc.) to adapt their reasoning, tone, and outputs to the specific company or environment.

---

### 🧠 Knowledge — Organizational Memory & Semantic Context

**What it is:**  
A structured repository of all *explicit and tacit* company knowledge: architecture diagrams, policies, conventions, incident retrospectives, KB articles, and internal best practices.

**Counts as capability**
- Indexed across multiple modalities (text, diagrams, configs, wiki pages).  
- Linked to ontology entities (services, clusters, teams, roles).  
- Versioned and queryable through embeddings and metadata filters.  
- Governed by visibility/ownership (team/org/global).  

**Does NOT count**
- Unstructured file dumps without metadata or embeddings.  
- Outdated or unvalidated documentation with no provenance.

**Evidence checklist**
- Knowledge graphs, Milvus collections, or RDF triples representing internal sources.  
- API for semantic + keyword retrieval with metadata (owner, timestamp, tags).  
- Periodic validation and feedback loops.

**Scoring**
- **N/L:** Ad-hoc or external wiki only.  
- **P/M:** Some internal KB indexed but no entity linkage.  
- **Y/M:** Multi-source KB with embeddings + metadata; used in prompting.  
- **Y/H:** Fully governed, ontology-linked knowledge layer with reasoning hooks.

---

### 💪 Capability — Skills, Tools, and Procedural Know-How

**What it is:**  
A registry of *what the organization and its engineers can do* — DevOps playbooks, deployment methods, automation scripts, observability patterns, and integrations.

**Counts as capability**
- Taxonomy of internal tools, scripts, services, and their APIs.  
- Linkage between people (or teams) and the systems they operate.  
- Stored as structured “capability cards” (name, purpose, API, maturity, owner).  
- Referenced dynamically by agents to decide which tool or process to use.  

**Does NOT count**
- Static list of tools without API metadata or context.  
- Human-only descriptions not usable for orchestration or planning.

**Evidence checklist**
- YAML/JSON “capability registry” or vector index describing actions/functions.  
- Mappings to workloads, environments, and ownership.  
- Retrieval and ranking via intent classifiers or embeddings.

**Scoring**
- **N/L:** Tribal knowledge only.  
- **P/M:** Tools listed manually; partial metadata.  
- **Y/M:** Structured capability index; referenced by agents.  
- **Y/H:** Dynamic capability graph with discovery, usage tracking, and confidence metrics.

---

### 📖 Storytelling — Narratives, Incidents, and Institutional Memory

**What it is:**  
Curated *narratives* capturing how the organization learned, failed, and evolved — incident timelines, project retrospectives, and engineering “stories” that teach context and culture.

**Counts as capability**
- Chronological or thematic story records linked to systems, incidents, and outcomes.  
- Embedded narratives used for prompt adaptation (e.g., tone, lessons learned).  
- Governed by confidentiality and relevance tags.  
- Indexed for retrieval and reasoning (semantic embeddings).  

**Does NOT count**
- Free-form incident logs with no summary, tags, or structure.  
- Public case studies unlinked to internal systems.

**Evidence checklist**
- Vectorized retrospectives, “stories” collections in Milvus.  
- Temporal relationships (before/after incidents).  
- Summaries and moral/lesson fields for generative prompting.

**Scoring**
- **N/L:** No structured retrospectives.  
- **P/M:** Informal retros or blog posts.  
- **Y/M:** Indexed story corpus; retrievable and summarized.  
- **Y/H:** Semantic narrative graph integrated into prompt adaptation.

---

### 🏗️ Workload Deployed — Ontology Instances (Runtime Context)

**What it is:**  
The **live topology** and **state** of the company’s deployed workloads — environments, namespaces, services, pods, metrics, and relationships.

**Counts as capability**
- Modeled as ontology instances (e.g., RDF/OWL classes → running resources).  
- Continuously synchronized with runtime telemetry (Prometheus/K8s APIs).  
- Serves as contextual substrate for diagnostics and recommendations.  
- Queryable via SPARQL, vector search, or graph traversal.  

**Does NOT count**
- Static inventory CSVs or unmaintained CMDB.  
- Runtime metrics with no semantic linkage to entities.

**Evidence checklist**
- Ontology instance data (Service, Deployment, Pod, Config, etc.).  
- Relationships: dependsOn, monitoredBy, ownedBy, runsIn.  
- Regular updates and validation.

**Scoring**
- **N/L:** Static CMDB; no live state.  
- **P/M:** Partial synchronization; some ontology coverage.  
- **Y/M:** Live state mapping to ontology instances; used for diagnostics.  
- **Y/H:** Fully dynamic knowledge graph fed by observability + infra data streams.

---

### 👤 Profiles — Human and Team Context

**What it is:**  
Representation of **engineer/SRE/DevOps profiles**, expertise, and operational responsibilities to personalize diagnostics and knowledge retrieval.

**Counts as capability**
- Metadata: roles, experience areas, systems owned, on-call history, skills.  
- Integrated into authorization and reasoning layers (e.g., route query to expert).  
- Optional embeddings for semantic matching (e.g., “find engineer experienced with Kafka”).  

**Does NOT count**
- HR database dump or generic user list.  
- Missing skills, ownership, or expertise linkages.

**Evidence checklist**
- Structured “EngineerProfile” dataset or graph nodes linked to capabilities/workloads.  
- Skill taxonomies and ownership relationships.  
- Governance for PII and access control.

**Scoring**
- **N/L:** Flat user list, no metadata.  
- **P/M:** Basic roles + system ownership.  
- **Y/M:** Skills/ownership mapped and retrievable.  
- **Y/H:** Full semantic profile graph with confidence, feedback, and usage tracking.

---

### 🧮 Integration Scenarios

| Agent | Uses these categories for… |
|--------|-----------------------------|
| **diag** | Tailor hypotheses using KB + ontology (Workload Deployed); cite prior stories for reasoning context. |
| **activity** | Enrich timelines with org knowledge (link KB entries, engineers, workloads). |
| **knowledge service** | Central ingestion and governance layer (retrieval, versioning, embedding). |
| **UI/Chat agents** | Context-aware prompting and story-based responses. |

---

## 🧠 Unified Models — Snapshot Guide (UKM, UAM, UDM, UOM, UEOM, UPM)

> **How to read these lines:** Each platform card includes snapshot lines like  
> `**🧠 UKM — Snapshot:** Ingest **…**, Index **…**, Retrieval **…**, Governance **…**, Overall **…**.`  
> The four facets are interpreted **per model** as defined below. Scores use the same rubric as above (N/L, P/L, P/M, Y/M, Y/H → Overall Low → High).

**Mapping from top‑line badges → U‑models**
- **UKM** ⇢ derives from the **Knowledge & Contextual Intelligence Layer** maturity (RAG/KB governance).  
- **UAM** ⇢ derives from **⚙️ Activities** maturity.  
- **UDM** ⇢ derives from **🔍 Diagnostics** maturity.  
- **UOM** ⇢ derives from **👁️ Observability** maturity.  
- **UEOM** ⇢ derives from **🧬 Event Ontology** maturity.  
- **UPM** ⇢ derives from **🚀 Provisioning** maturity.

---

### 🧠 UKM — Unified Knowledge Model (Ingest → Index → Retrieve → Govern)

**Facet definitions**
- **Ingest:** Connectors/pipelines for docs, incidents, runbooks, configs; dedupe and provenance.  
- **Index:** Hybrid search (keyword + vector) with metadata (owner, service, env); update cadence.  
- **Retrieval:** RAG quality; citations; query routing to the right corpus; multi‑doc synthesis.  
- **Governance:** RBAC, PII policy, source visibility, versioning, feedback loops, eval sets.

**Counts as capability**
- Multi‑source knowledge with embeddings and metadata; citations in answers; corpus scoping by role/team.  
- Measurable retrieval quality (evaluations); provenance stored and exportable.

**Scoring**
- **N/L:** Ad‑hoc or external wiki only.  
- **P/M:** Some internal KB indexed; limited metadata; weak governance.  
- **Y/M:** Multi‑source hybrid index; RAG used in prompting; role‑aware visibility.  
- **Y/H:** Fully governed, ontology‑linked corpus with evals, citations, and continuous feedback.

---

### ⚙️ UAM — Unified Activity Model (Log → Learn → Automate)

**Facet definitions**
- **Ingest:** Durable capture of actions/events (sessions, tickets, PRs, pipeline runs, change sets).  
- **Index:** Correlated, searchable timeline linked to incidents/entities; de‑dupe & normalization.  
- **Retrieval:** Fast queries, filters, and **replay** of parametrized actions/runbooks.  
- **Governance:** Audit trail, RBAC, approvals, retention/SOX controls, signed artifacts.

**Counts as capability**
- End‑to‑end activity timeline with owners, inputs, outputs, outcomes; exportable history/API; parameterized replays.

**Scoring**
- **N/L**, **P/M**, **Y/M**, **Y/H** — as defined above.

---

### 🔍 UDM — Unified Diagnostics Model (Detect → Correlate → RCA → Verify)

**Facet definitions**
- **Ingest:** Alerts + telemetry + change/events streams.  
- **Index:** Problem/incidence structures (grouped signals, similarity clusters, causal/episode graphs).  
- **Retrieval:** Evidence‑backed narratives; queries, tests, hypotheses reconstruction.  
- **Governance:** Evaluation sets, confidence & FP/FN tracking, human‑in‑the‑loop and override rules.

**Counts as capability**
- Multi‑signal correlation; change‑aware hints; hypothesis lists with confidence; verification steps.

**Scoring**
- **N/L**, **P/M**, **Y/M**, **Y/H** — as defined above.

---

### 👁️ UOM — Unified Observability Model (MELT)

**Facet definitions**
- **Ingest:** Multi‑signal collection (APM/Infra/RUM/profiles), ideally **OpenTelemetry‑compliant**.  
- **Index:** Time‑series, log, and trace stores with join keys; service maps/topology.  
- **Retrieval:** SLOs, drill‑downs, cross‑modal hops (alert → trace → span → logs), time‑travel comparisons.  
- **Governance:** RBAC, data classification/PII filtering, retention & cost controls, sampling policy.

**Counts as capability**
- Unified dashboards; entity pages with linked telemetry; alert → evidence hops; SLO burn rates; topology views.

**Scoring**
- **N/L**, **P/M**, **Y/M**, **Y/H** — as defined above.

---

### 🧬 UEOM — Unified Event Ontology Model (Entities & Relationships)

**Facet definitions**
- **Ingest:** Mapping raw signals into **typed entities** with stable IDs.  
- **Index:** Graph/relational store for **relationships** (depends_on, runs_on, caused_by) and versions.  
- **Retrieval:** Graph traversal/queries (SPARQL/DSL); cross‑joins across telemetry & tickets.  
- **Governance:** Schema versioning, lineage/provenance, ownership, quality checks & federation rules.

**Counts as capability**
- Documented schemas; cross‑domain joins; exportable graph; semantic query API.

**Scoring**
- **N/L**, **P/M**, **Y/M**, **Y/H** — as defined above.

---

### 🚀 UPM — Unified Provisioning Model (Plan → Approve → Apply → Verify → Rollback)

**Facet definitions**
- **Ingest:** Desired state (IaC templates), change sets, drift & preflight/policy results.  
- **Index:** Per‑env state, plan/diff history, dependency graph, rollback points.  
- **Retrieval:** Human‑readable diffs, impact/risk summaries, prior “known‑good” run selection.  
- **Governance:** RBAC, **policy‑as‑code**, approvals/freeze windows, **automatic rollback**, break‑glass audit.

**Counts as capability**
- Generate/apply IaC with diffs, approvals, rollback; drift detection; execution logs; policy gates.

**Scoring**
- **N/L**, **P/M**, **Y/M**, **Y/H** — as defined above.

---

## ⚙️ Activities — Activity Footprint (Log → Learn → Automate)

**What it is:** The platform’s ability to **record what happened**, **make that history actionable**, and **replay or automate** activity patterns.

**Counts as capability**
- **Logging:** durable records of actions/events (e.g., sessions, tickets, PRs, pipeline runs, change sets).
- **Search & awareness:** query, filter, and correlate the activity timeline; link to incidents or entities.
- **Repro/automation:** re‑run past fixes/runbooks; trigger actions from history (e.g., “apply last good remediation”).

**Does NOT count**
- Ephemeral console output without storage or search.
- Vendor says “we log everything” with **no user‑visible history** or export.

**Evidence checklist**
- Export/API for activity history; correlation to incidents/CMDB/owners.
- Ability to **replay** or **schedule** a past action; audit trail of who/when/what.

**Scoring**
- **N/L:** Little/no persisted history; no search.  
- **P/M:** Persisted history + basic search; limited correlation; manual replay only.  
- **Y/M:** Rich timeline + correlation to entities/incidents + API export; some templated replays.  
- **Y/H:** Full audit + programmatic replay, **policy guardrails**, approvals, and **closed‑loop** automation.

**Edge cases**: Git/CI logs alone → **P/M** unless the agent **uses** them for replay/decisions.

---

## 🔍 Diagnostics — Detection → Correlation → RCA → Verification

**What it is:** How the platform **detects anomalies**, **groups signals**, **identifies root cause**, and **verifies** hypotheses with evidence.

**Counts as capability**
- **Detection:** thresholds, anomalies (stat/ML), pattern mining.  
- **Correlation:** multi‑signal grouping across metrics/logs/traces/changes.  
- **RCA:** causal graphs or structured hypotheses explaining *why*.  
- **Verification:** counter‑tests, confidence scoring, and falsification steps; links to evidence.

**Does NOT count**
- LLM summary of dashboards with no evidence or tests.  
- “RCA” that is just the **first alert** restated.

**Evidence checklist**
- An incident record with **grouped signals**, a **root‑cause narrative**, **queries/logs** linked, and a **confidence** or **verdict**.  
- If ML is claimed: show **model/feature** descriptions or docs; show **examples** of correct/incorrect RCA.

**Scoring**
- **N/L:** Alerts only; no grouping; no cause.  
- **P/M:** Some correlation or heuristic RCA; limited verification; links to raw data.  
- **Y/M:** Structured RCA (entities/changes) + repeatable verification plan + confidence.  
- **Y/H:** Causal/graph‑based RCA + automated counter‑tests + **early finalize** on high confidence; low false‑positive rate tracked.

**Edge cases**: If evidence is not linkable/exportable → cap at **P/M**.

---

## 🚀 Provisioning — Control Plane for Infra & Services

**What it is:** Ability to **create/modify** infrastructure/services directly, with **safety** (approvals, drift detection, rollback).

**Counts as capability**
- Executing **Terraform/Cloud/K8s** changes (apply/rollback), with approvals and diffs.  
- Generating IaC **and** applying it through the platform’s control path.  
- Recording change sets and status to history.

**Does NOT count**
- Only opening a **PR** with IaC (no execution) → this is **indirect**.  
- Clicking a third‑party runbook manually with no platform control or audit.

**Evidence checklist**
- Change plan/diff, execution logs, approval trail, **rollback outcome**.  
- Policy checks (preflight, drift detection), dry-run/simulator proof.

**Scoring**
- **N/L:** Recommendations or PRs only; no apply.  
- **P/M:** Limited apply via integrations; no rollback/approvals.  
- **Y/M:** Managed apply with approvals/policies; rollback supported; drift checks.  
- **Y/H:** Safe multi‑env orchestration, canary/blue‑green, policy-as-code, and **automatic rollback** on failure.

**Edge cases**: “We trigger Jenkins/Terraform” without visibility → **P/M** at best.

---

## 🧬 Event Ontology — Semantic Model & Relationships

**What it is:** A **domain model** for events/entities (services, pods, hosts, alerts, changes) with **typed relationships** and **schemas**.

**Counts as capability**
- Entities with stable IDs (service, workload, ticket, user, dataset).  
- Relationships (depends_on, runs_on, caused_by), time windows, and schemas.  
- Standards: **OTel semantic conventions**, **CIM**, **CSDM**, **DQL entities**.

**Does NOT count**
- Free‑text or flat tables without entity linkage.

**Evidence checklist**
- Schema docs; example queries that traverse relationships; export of typed entities.  
- Mapping docs showing how vendor ingests → normalized ontology.

**Scoring**
- **N/L:** Flat metrics/logs; no linkage.  
- **P/M:** Partial mapping (e.g., alerts → service); limited joins.  
- **Y/M:** Cohesive graph across domains (infra/app/change/ticket); queryable.  
- **Y/H:** Versioned ontology with lineage, enrichment pipelines, and cross-product federation.

**Edge cases**: If only *one* domain (e.g., CI) is modeled → **P/M** unless cross-domain mapping exists.

---

## 👁️ Observability — Telemetry Breadth & Depth

**What it is:** How comprehensively the platform **collects, visualizes, and links** telemetry (metrics, logs, traces, events) to entities and incidents.

**Counts as capability**
- Multi‑signal ingest (**metrics/logs/traces/events**), SLO/SLA views, drill-downs to entity timelines.  
- First‑class dashboards and APIs; alerting with runbooks.

**Does NOT count**
- Static screenshots or one‑off charts without live data.  
- “Bring your own Grafana” with zero native linkage.

**Evidence checklist**
- Live dashboards; entity page with linked telemetry; alert → trace/log/metric hops.  
- SLO burn‑rates; topology view tied to telemetry.

**Scoring**
- **N/L:** No native or live telemetry; static screenshots/CSVs only; no queries or alerting.  
- **P/M:** One major signal only or siloed collectors; basic dashboards; limited linking; minimal alerting; no cross‑modal hops.  
- **Y/M:** Multiple sources unified; entity/incident link‑outs; SLOs.  
- **Y/H:** Full‑stack + topology + cross‑modal hops (alert → trace → span → logs) + **time travel** and comparative baselines.

**Edge cases**: If traces absent but logs/metrics proxy spans adequately, cap at **Y/M**.

---

## 📈 Confidence — Maturity, Stability & Evidence Quality

**What it is:** Our rating of how **reliable and production‑ready** the platform’s claims are, based on **documentation, evidence, and references**.

**What drives confidence**
- **Enterprise references/GA** vs. beta/claims.  
- **Repeatable demos** with exported artifacts (not marketing screenshots).  
- **Operational hygiene:** SLAs, rate limits, circuit breakers, RBAC, auditability.

**Scoring**
- **Low:** early/beta; sparse docs; limited third‑party validation.  
- **Med:** documented features, consistent results in scope, some references.  
- **High:** GA + references + audits; strong artifacts; mature guardrails.

**Edge cases**: Missing artifacts → drop one level.

---

## 📊 Suggested KPIs for Bake‑offs

- **TTFC / TTRC:** Time‑to‑first‑clue / time‑to‑root‑cause.  
- **Verified RCA rate** and **false‑positive rate** across a fixed incident set.  
- **Actionability:** % of cases with a clear, safe next step (rollback/fix).  
- **Evidence quality:** % of outputs with linked queries/logs/traces.  
- **Operator effort:** Clicks/commands to resolution; handoff count.  
- **Resilience:** Behavior under partial outages (API down, timeouts, throttling).

---
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

# 🗂️ Platform Archetypes Overview

Keep the original overview, plus add the clarifications below to reflect new platforms.

### 🔭 Observability‑First Agents
These agents spring from APM, monitoring, and logging platforms. **Dynatrace’s Davis AI** and **Cisco’s (Splunk) AI Agents** are prime examples. They have **high diagnostic capabilities** – ingesting huge volumes of telemetry, detecting anomalies, performing root cause analysis (often with causal AI), and even initiating automated remediation of known issues. They boast strong event ontologies (Dynatrace’s unified entity model, Splunk’s CIM with OpenTelemetry data) and rich observability dashboards. However, they intentionally do not focus on provisioning or large-scale changes – any fixes applied are usually within the existing infrastructure (restarting services, adjusting thresholds, etc.), not deploying new servers or altering network architecture. The value here is in proactive incident detection and resolution guidance, not infrastructure as code.

**Additions (Oct 2025):** **Datadog Bits AI & AI Agents** (SRE/Dev/Sec agents, hypothesis‑driven RCA, incident comms, post‑mortems), **Elastic AI Assistant for Observability** (ESRE‑grounded answers, runbook proposals), **New Relic AI** (plain‑English NRQL, change‑aware analysis).

### ⚙️ Provisioning‑Focused Agents
These platforms excel at automating environment setup and resource management. **DuploCloud’s AI DevOps Suite** and **Qovery’s AI Migration Agent** fall in this bucket. They typically integrate with cloud APIs or use Infrastructure-as-Code (Terraform, Docker, Kubernetes) under the hood to provision and configure systems on demand. For example, DuploCloud’s agent can create cloud resources and pipelines based on high-level requests (backed by Terraform), and Qovery’s open-source agent can generate Terraform files or Dockerfiles to help migrate applications to cloud platforms. **Kuberns Platform**, a managed PaaS with an AI assistant, also emphasizes one-click deployment and AI-driven scaling/cost optimization. These agents handle provisioning as a core strength, automating tasks like spinning up VMs, containers, or cloud services. On the flip side, their observability and diagnostics features are limited – they might perform basic health checks or cost analyses, but they don’t have full AIOps event correlation. In short, they’ll launch or fix your infrastructure components, but they rely on other tools to deeply monitor them.

**Additions (Oct 2025):** **Microsoft Azure Copilot (Agent Mode)**—VS Code operator that decomposes requests, generates/modifies Bicep, runs `az`/`azd`, checks resource health, deploys under RBAC with confirmation gates.

### 👨‍💻 Developer‑Centric (Code‑First) Agents
This category targets software engineers and integrates into the development lifecycle. **AWS Strands SDK**, **Atlassian’s Rovo Dev Agent**, **GitHub Copilot**, **Zencoder AI Agents**, and **JFrog’s Fly** all exemplify a developer-first approach. They often run as part of the coding process or CI/CD pipeline. For instance, Atlassian’s Rovo Dev is a CLI tool that can generate code, write tests, and even create pull requests autonomously to accelerate development. GitHub’s evolving AI agent can propose code changes via pull requests while respecting branch protections (acting as an asynchronous coding assistant). Zencoder’s agents embed in CI to fix failing tests, update documentation, and suggest code refactors automatically when pipelines fail. JFrog Fly introduces an “agentic” repository that works with AI agents to manage artifact releases and security compliance in the dev workflow. These tools usually require some configuration or code (they might be SDKs or CLI commands), and they operate by producing code or config changes rather than by controlling running infrastructure directly. Their “activities” logging is often via source control history or CI logs, and their observability is minimal outside developer metrics (like code quality or build status). In essence, they act as AI co-developers more than traditional ops bots.

**Additions (Oct 2025):** **Microsoft Azure AI Agent Service (Foundry)**—enterprise framework for building and observing multi‑agent systems; MCP/OpenAPI tools; AgentOps/OTel tracing; open‑source Agent Framework SDK.

### 🏢 Enterprise Workflow Orchestrators
These are the heavyweights leveraging existing enterprise platforms. **ServiceNow AI Agent Orchestrator** and **Salesforce OpsAI/Agentforce** are key examples, and even **IBM’s AskIAM** (built on Watsonx) fits here for a specialized domain. They provide a low-code interface to orchestrate complex workflows across IT and business operations. ServiceNow’s platform can ingest activity records from across the enterprise (tickets, configuration database, monitoring alerts) and use AI agents to triage incidents, correlate events, and even execute runbook actions via its workflow engine. Salesforce’s Agentforce (also branded as OpsAI for IT ops use-case) integrates with its Data Cloud and Atlas AI to monitor events (like incidents, cases) and can trigger actions through Salesforce Flow or external integrations. These platforms tend to have a high event ontology – for example, Salesforce defines an incident object model and topics for events, and ServiceNow has its Common Service Data Model – which helps their agents understand context at a high level. They can perform diagnostics (e.g., identifying an alert’s likely root cause, using knowledge base or past incidents) and even some provisioning or remediation by invoking other tools (resetting a server via integration, creating a Jira ticket, running an Apex script, etc.). However, their direct observability into infrastructure is partial; they often rely on integrations with monitoring tools for deep metrics. The strength here is coordination and breadth: an agent orchestrator can call on many specialized agents or workflows to resolve an incident end-to-end. These systems are poised to be the “brain” that delegates tasks out to more focused tools.

**Additions (Oct 2025):** **PagerDuty AIOps**—noise reduction & correlation, AI agent suite drafting comms and next steps, change‑aware hints; safe diagnostics/remediations via Automation Actions/Rundeck.

### 📊 Data and MLOps Agents
A subset of platforms concentrate on data pipelines, ML model lifecycle, and AI quality management. **Databricks’ Agent Bricks**, **Snowflake’s AI Agents**, and **Dataiku AI Agents** represent this group. They are not traditional IT ops tools but bring agentic AI to data science and analytics operations. For example, Databricks Agent Bricks can simulate agents in notebooks to evaluate LLM behaviors or automatically judge the quality of model outputs (it focuses on AI evaluation and guardrails, using synthetic data and MLflow tracking). Snowflake’s approach involves using its Data Cloud to let agents automate parts of the data science workflow – e.g. preparing datasets, scheduling training runs, or detecting data drift – all within the Snowflake ecosystem (with a strong event model of pipeline steps and metrics). Dataiku’s AI Agents feature allows creation of governed agents that can orchestrate data projects, with a “trace explorer” to debug agent decisions and built-in guardrails. These data-focused agents have rich domain-specific ontologies (for pipelines, models, datasets) and good observability into model performance and costs. They typically don’t provision infrastructure outside their platform – for instance, they won’t create new Kubernetes clusters for you, but they might allocate resources in Databricks or trigger a cloud function as part of a data workflow. Their diagnostics are about data and model issues (accuracy, drift, etc.) rather than IT incidents.

### 🎯 Specialized Domain Agents
Some AI agents zero in on a narrow yet critical domain of IT. **IBM’s AskIAM** is a prime example, concentrating on Identity and Access Management tasks. Built with Watsonx Assistant, AskIAM can handle requests like provisioning or deprovisioning user access, checking compliance with access policies, and answering audit queries. It maintains activity records of access changes and can diagnose potential identity risks (like toxic permission combinations) using AI. Another example is **JFrog’s security and compliance agents** (part of JFrog Fly’s ecosystem), which automatically scan for vulnerabilities and even initiate remediation by suggesting or applying artifact updates. **Kagent by Solo.io** targets Kubernetes operations specifically – it runs AI agents inside K8s clusters to troubleshoot and fix issues at the cluster level (e.g., analyzing pod logs, adjusting deployments) and uses an open standard (MCP, or Model Context Protocol) to interface with various tools. These domain-specific agents leverage AI to handle repetitive, domain-specific chores with high accuracy, but by design they are limited in scope – they won’t manage anything outside their niche.

---
### Recap — quick list
- **🔭 Observability‑First:** Dynatrace Davis AI; Cisco (Splunk) AI Agents; **Datadog Bits AI & AI Agents**; **Elastic AI Assistant for Observability**; **New Relic AI**.  
- **⚙️ Provisioning‑Focused:** DuploCloud AI Help Desk; Qovery AI Migration Agent; Kuberns Platform; **Microsoft Azure Copilot (Agent Mode)**.  
- **👨‍💻 Developer‑Centric (Code‑first & Frameworks):** AWS Strands SDK; Atlassian Rovo Dev; GitHub Copilot Coding Agent; Zencoder; JFrog Fly (agentic repo); **Microsoft Azure AI Agent Service (Foundry)**.  
- **🏢 Enterprise Workflow Orchestrators:** ServiceNow AI Agent Orchestrator; Salesforce Agentforce (OpsAI); **PagerDuty AIOps**.  
- **📊 Data & MLOps Agents:** Databricks Agent Bricks; Snowflake Cortex Agents; Dataiku AI Agents.  
- **🎯 Specialized Domain:** IBM AskIAM (IAM); Solo.io Kagent (K8s).

---

# PLATFORM SECTIONS (A–Z)

> **Notation:** Each card includes a short **UKM snapshot** (knowledge layer maturity) **and** U‑model snapshots (UAM/UDM/UOM/UEOM/UPM). “Latest updates” link to primary sources.

---

## 🧩 Atlassian Rovo Dev
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/M  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** P/L  · 👁️ **Observability:** P/L  · 📈 **Confidence:** High

**🏗️ Build style / interface** — CLI + cloud; integrates across Jira/Confluence/Bitbucket/GitHub.  
**💡 What it actually does** — Context‑aware coding agent for planning, coding, tests, docs, and PR automation.  
**📊 Data / telemetry** — Work items + docs + repo/PR history.  
**🔗 Interoperability** — Atlassian Graph, CLI; works with Bitbucket/GitHub.  
**🏢 Deployment model** — Atlassian cloud + local CLI.  
**🗒️ Notes** — Developer‑centric; infra ops out of scope.

**🧠 UKM — Snapshot:** Ingest **P/M** (work items/repos), Index **P/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**🔍 UDM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🧬 UEOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 AWS Strands SDK
⚙️ **Activities:** P/L  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** Y/M  
🧬 **Event ontology:** P/L  · 👁️ **Observability:** P/M  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Code‑first SDK (Python/Node).  
**💡 What it actually does** — Model‑driven agent framework; plan/act via tools; deploy on AWS (Lambda/Fargate/EKS/EC2).  
**📊 Data / telemetry** — Agent plans/tool calls via OpenTelemetry.  
**🔗 Interoperability** — MCP + A2A; AWS services; community toolpacks.  
**🏢 Deployment model** — Your AWS account.  
**🗒️ Notes** — BYO memory/KB; strong tracing & governance hooks.

**🧠 UKM — Snapshot:** Ingest **P/L**, Index **N/L**, Retrieval **P/M**, Governance **P/M**, Overall **Medium‑Low**.

**⚙️ UAM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🧬 UEOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🚀 UPM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**Latest updates:** SDK OSS release; OTel tracing; MCP integration patterns and prescriptive guidance.  
Links: aws.amazon.com/blogs/opensource • aws.amazon.com/blogs/machine-learning • docs.aws.amazon.com/prescriptive-guidance • github.com/strands-agents

---

## 🧩 Cisco Splunk AI Agents
⚙️ **Activities:** Y/H  · 🔍 **Diagnostics:** Y/H  · 🚀 **Provisioning:** N/L  
🧬 **Event ontology:** Y/H  · 👁️ **Observability:** Y/H  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Low‑code actions in Splunk Observability/Security.  
**💡 What it actually does** — AI agents for telemetry collection, alert config, anomaly/RCA, and fix recommendations.  
**📊 Data / telemetry** — OpenTelemetry signals; Splunk CIM.  
**🔗 Interoperability** — Broad ecosystem; Cisco + Splunk.  
**🏢 Deployment model** — Splunk Cloud/Observability Cloud.  
**🗒️ Notes** — Remediation via playbooks/integrations more than direct infra apply.

**🧠 UKM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/M**, Overall **High**.

**⚙️ UAM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🔍 UDM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**👁️ UOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🧬 UEOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🚀 UPM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

**Latest updates:** “Agentic AI‑powered Observability” unveiled at .conf25; AI Troubleshooting Agents across portfolio.  
Links: splunk.com/newsroom • investor.cisco.com • siliconangle.com

---

## 🧩 Databricks Agent Bricks
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** P/L  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** Y/M  · 👁️ **Observability:** P/M  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Workspace UI + APIs; Mosaic AI + MLflow.  
**💡 What it actually does** — **Auto‑optimize agents** on enterprise data; eval/guardrails; traces in Lakehouse/MLflow.  
**📊 Data / telemetry** — Traces, eval datasets, cost/quality.  
**🔗 Interoperability** — Connectors; runs in Databricks.  
**🏢 Deployment model** — Databricks workspace.  
**🗒️ Notes** — Evaluation/quality focus; not infra ops.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**👁️ UOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🧬 UEOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 Datadog Bits AI & AI Agents
⚙️ **Activities:** Y/H  · 🔍 **Diagnostics:** Y/H  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** Y/M  · 👁️ **Observability:** Y/H  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Integrated into Datadog SaaS platform (no‑code UX in dashboards/incident console).  
**💡 What it actually does** — Generative AIOps assistant + role‑specific agents (SRE/Dev/Sec). Investigates alerts/incidents with parallel, hypothesis‑driven RCA; groups related alerts; produces real‑time incident summaries & suggested next steps; drafts post‑mortems; Dev agent can open PRs.  
**📊 Data / telemetry** — Datadog’s unified telemetry (metrics, logs, traces, events) + service topology & runbooks.  
**🔗 Interoperability** — Slack/Teams, PagerDuty/On‑Call, Jira/ServiceNow; GitHub for PR‑based fixes.  
**🏢 Deployment model** — Datadog SaaS (some agents LA/preview in 2025).  
**🗒️ Notes** — Human‑in‑the‑loop with optional auto‑run of safe remediations; approvals for complex actions.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**⚙️ UAM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🔍 UDM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**👁️ UOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🧬 UEOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 Dataiku AI Agents
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** Y/M  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** High

**🏗️ Build style / interface** — No/low‑code + Python; LLM Mesh; **Trace Explorer**.  
**💡 What it actually does** — Build/trace/evaluate governed agents; orchestrate data workflows.  
**📊 Data / telemetry** — Structured agent traces & metrics.  
**🔗 Interoperability** — LLM Mesh; plugins; LangChain‑style patterns.  
**🏢 Deployment model** — Dataiku DSS.  
**🗒️ Notes** — Strong guardrails/tracing; infra provisioning out of scope.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/H**, Overall **Medium‑High**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 DuploCloud AI Help Desk
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/H  · 🚀 **Provisioning:** Y/H  
🧬 **Event ontology:** P/M  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — No/low‑code ticket‑driven agents.  
**💡 What it actually does** — K8s troubleshooting & cloud ops; can apply fixes via **DuploCloud Terraform Provider**.  
**📊 Data / telemetry** — Tickets/action logs + cloud account metadata.  
**🔗 Interoperability** — Terraform provider + integrations.  
**🏢 Deployment model** — SaaS + Terraform.  
**🗒️ Notes** — Strong on apply/rollback in DuploCloud context.

**🧠 UKM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🚀 UPM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

---

## 🧩 Dynatrace Davis AI
⚙️ **Activities:** Y/H  · 🔍 **Diagnostics:** Y/H  · 🚀 **Provisioning:** N/L  
🧬 **Event ontology:** Y/H  · 👁️ **Observability:** Y/H  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Low‑code workflows + Davis apps.  
**💡 What it actually does** — Automatic anomaly detection & **causal RCA**; correlates into **Davis problems** with evidence.  
**📊 Data / telemetry** — Full‑stack APM/Infra/Logs/RUM in **Grail**; DQL.  
**🔗 Interoperability** — Integrations & workflows.  
**🏢 Deployment model** — Dynatrace SaaS.  
**🗒️ Notes** — Remediation guided or via workflows; direct infra apply is limited.

**🧠 UKM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/M**, Overall **High**.

**⚙️ UAM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🔍 UDM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**👁️ UOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🧬 UEOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🚀 UPM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.


## 🧩 Elastic AI Assistant for Observability
⚙️ **Activities:** P/M  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** N/L (↗ runbooks)  
🧬 **Event ontology:** P/M  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — Built into Elastic Observability (Kibana) with contextual prompts + chat.  
**💡 What it actually does** — Explains errors/logs with actionable fixes, answers “why is latency high?”, recommends queries/visualizations, and surfaces relevant runbooks (can propose executing them for known issues).  
**📊 Data / telemetry** — Elastic full‑stack data (metrics/logs/traces/APM profiles) grounded via ESRE; optional org KB via connectors (RAG).  
**🔗 Interoperability** — Works with user‑provided LLMs or Elastic Cloud LLM; content connectors; triggers Elastic Actions/external workflows.  
**🏢 Deployment model** — Elastic Stack (self‑hosted or Elastic Cloud).  
**🗒️ Notes** — Human assistant first; accelerates RCA and onboarding.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **P/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🚀 UPM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

---

## 🧩 GitHub Copilot Coding Agent
⚙️ **Activities:** P/M  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** N/L  · 👁️ **Observability:** P/M  · 📈 **Confidence:** High

**🏗️ Build style / interface** — PR/CLI; async cloud agent; Agents panel.  
**💡 What it actually does** — Launches ephemeral VM, clones repo, runs tests/fixes, opens PRs, responds to review.  
**📊 Data / telemetry** — PRs/commits/CI logs; agent status.  
**🔗 Interoperability** — GitHub Actions/CLI; MCP extension in docs.  
**🏢 Deployment model** — GitHub SaaS.  
**🗒️ Notes** — Infra provisioning via IaC PRs only.

**🧠 UKM — Snapshot:** Ingest **P/L**, Index **N/L**, Retrieval **P/M**, Governance **Y/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🧬 UEOM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 Google Vertex AI Agent Builder
⚙️ **Activities:** P/L  · 🔍 **Diagnostics:** P/L  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** P/L  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — No‑code console (Dialogflow CX lineage) + ADK.  
**💡 What it actually does** — Multi‑agent conversational experiences; analytics; actions via webhooks/GCP services.  
**📊 Data / telemetry** — Conversation analytics, evals.  
**🔗 Interoperability** — Webhooks; Vertex AI Search; **Agent Garden** samples.  
**🏢 Deployment model** — Google Cloud.  
**🗒️ Notes** — Infra changes require external services; Jules (coding agent) is separate.

**🧠 UKM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/M**, Governance **P/M**, Overall **Medium‑Low**.

**⚙️ UAM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🔍 UDM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 IBM AskIAM
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/M  · 🚀 **Provisioning:** Y/H  
🧬 **Event ontology:** P/M  · 👁️ **Observability:** P/L  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — Low‑code assistant workflows delivered via IBM Consulting.  
**💡 What it actually does** — IAM requests/approvals; onboarding; posture insights; cross‑system provisioning.  
**📊 Data / telemetry** — IAM requests, audit trails.  
**🔗 Interoperability** — IAM APIs (Entra, SailPoint, etc.).  
**🏢 Deployment model** — IBM‑managed for clients.  
**🗒️ Notes** — Deep infra telemetry not in scope.

**🧠 UKM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**👁️ UOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🧬 UEOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🚀 UPM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

---

## 🧩 JFrog Fly (Agentic Repository)
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** Y/M  · 👁️ **Observability:** P/M  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — Low‑config repo + agent workflows.  
**💡 What it actually does** — Agent‑aware artifact/evidence flows; policy & compliance events; MCP connections to tools.  
**📊 Data / telemetry** — Semantic metadata; evidence & policy events.  
**🔗 Interoperability** — JFrog platform; GitHub; MCP.  
**🏢 Deployment model** — SaaS (beta).  
**🗒️ Notes** — Release governance focus; not direct infra apply.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🧬 UEOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 Kagent (Solo.io)
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/H  · 🚀 **Provisioning:** Y/M  
🧬 **Event ontology:** P/M  · 👁️ **Observability:** Y/H  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Kubernetes‑native framework; **Agent Gateway** (OSS) for A2A/MCP; kmcp.  
**💡 What it actually does** — Cluster diagnostics and tool orchestration (K8s/Prom/Grafana/Helm/Argo).  
**📊 Data / telemetry** — Agent & LLM traces; K8s/Prom via tools.  
**🔗 Interoperability** — MCP servers/tools; K8s CRDs, Gateway API.  
**🏢 Deployment model** — K8s runtime (OSS/Enterprise).  
**🗒️ Notes** — Deep K8s workflows; strong observability and policy hooks.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **P/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**👁️ UOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🧬 UEOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🚀 UPM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

---

## 🧩 Kuberns Platform
⚙️ **Activities:** P/M  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** Y/H  
🧬 **Event ontology:** P/L  · 👁️ **Observability:** P/M  · 📈 **Confidence:** Low

**🏗️ Build style / interface** — Low‑code PaaS UI; “one‑click deploy”.  
**💡 What it actually does** — Deploy/scale apps; AI‑assisted cost/perf optimization (claims).  
**📊 Data / telemetry** — Basic platform metrics.  
**🔗 Interoperability** — Not well‑documented.  
**🏢 Deployment model** — Managed PaaS.  
**🗒️ Notes** — Limited third‑party validation; treat as **tentative**.

**🧠 UKM — Snapshot:** Ingest **P/L**, Index **N/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low**.

**⚙️ UAM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🧬 UEOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🚀 UPM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

---

## 🧩 Microsoft Azure AI Agent Service (Foundry)

> **Note:** Microsoft Copilot and Azure/Foundry are separate offerings; they appear as distinct entries to reflect different product positioning and capabilities.

⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** N/L  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** P/M  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Azure AI Foundry service + **open‑source Agent Framework** SDK; visual workflow editor & CLI.  
**💡 What it actually does** — Build/deploy/manage multi‑agent systems with enterprise guardrails; orchestrates stateful agent workflows; integrates tools via OpenAPI & **MCP**; evaluation & **AgentOps** monitoring.  
**📊 Data / telemetry** — Agent conversation logs, tool invocations, **OpenTelemetry** traces; governance events & metrics.  
**🔗 Interoperability** — 1,400+ **Azure Logic Apps** as tools; supports external frameworks (LangChain/LangGraph); connectors; integrates with Microsoft 365 Copilot & external APIs.  
**🏢 Deployment model** — Azure AI Foundry (cloud) with containerized agent runtime; SDK open‑source for local dev + cloud deploy.  
**🗒️ Notes** — Focused on agent workflow orchestration/governance rather than direct human‑facing ops.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **P/M**, Retrieval **Y/M**, Governance **Y/H**, Overall **Medium‑High**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 Microsoft Azure Copilot (Agent Mode)

> **Note:** Microsoft Copilot and Azure/Foundry are separate offerings; they appear as distinct entries to reflect different product positioning and capabilities.

⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** Y/M  
🧬 **Event ontology:** P/L  · 👁️ **Observability:** P/L  · 📈 **Confidence:** High

**🏗️ Build style / interface** — VS Code extension (**Copilot for Azure**) with chat (“Ask”) + **Agent Mode**.  
**💡 What it actually does** — Natural‑language ops over Azure: decomposes prompts into tasks, **generates/modifies Bicep**, runs **Azure CLI/azd**, checks resource health, and deploys with confirmations under RBAC.  
**📊 Data / telemetry** — Azure Resource Graph, resource configs, and health APIs.  
**🔗 Interoperability** — Azure CLI/SDK + Azure Developer CLI; **Azure RBAC**.  
**🏢 Deployment model** — Client‑side VS Code extension backed by your Azure subscription (cloud backend).  
**🗒️ Notes** — Enterprise‑ready guardrails: explicit confirmation before changes; logs execution history; respects tenant boundaries.

**🧠 UKM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/M**, Governance **Y/M**, Overall **Medium‑Low**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🧬 UEOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🚀 UPM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

---

## 🧩 New Relic AI (formerly “Grok”)
⚙️ **Activities:** P/L  · 🔍 **Diagnostics:** Y/M  · 🚀 **Provisioning:** N/L  
🧬 **Event ontology:** Y/M  · 👁️ **Observability:** Y/H  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Web chatbot in New Relic One; IDE via **CodeStream**; mobile app.  
**💡 What it actually does** — Lets anyone query telemetry in plain English, summarize health, explain anomalies, **generate NRQL/dashboards**, and recommend fixes; guides instrumentation and alerting; analyzes deploy impact pre/post.  
**📊 Data / telemetry** — Unified MELT data + deploy/change events and UX data.  
**🔗 Interoperability** — OpenAI GPT with New Relic data context; CodeStream integration; alerting tie‑ins.  
**🏢 Deployment model** — New Relic SaaS.  
**🗒️ Notes** — Advisory only (no direct apply); RBAC enforced; some regulated accounts unsupported (2025).

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**⚙️ UAM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🔍 UDM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**👁️ UOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🧬 UEOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🚀 UPM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

---

## 🧩 Opsera Hummingbird (Unified Insights)
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/M  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** P/M  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — Low‑code dashboards & insights.  
**💡 What it actually does** — Aggregates CI/CD + SCM; DORA/DevEx metrics; AI insights & recommendations.  
**📊 Data / telemetry** — CI, SCM, release events; AI code assistant adoption analytics.  
**🔗 Interoperability** — Connectors; actions via integrations.  
**🏢 Deployment model** — SaaS.  
**🗒️ Notes** — Infra provisioning via integrations only.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **P/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 PagerDuty AIOps (Event Intelligence & AI Agent Suite)
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/M  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** P/M  · 👁️ **Observability:** P/L  · 📈 **Confidence:** High

**🏗️ Build style / interface** — SaaS with low‑code incident workflows, **Automation Actions**, AI‑driven Command Console.  
**💡 What it actually does** — Incident intelligence & response automation: suppress/dedupe noise, correlate related alerts into incidents, surface change context and similar incidents, draft status updates/post‑mortems, and recommend next steps. SRE, Insights, and Shift agents assist during response.  
**📊 Data / telemetry** — Ingests events from monitoring tools + change feeds; maintains incident timelines/human response history; change tracking.  
**🔗 Interoperability** — Datadog/New Relic/CloudWatch, Jira/ServiceNow, Slack/Teams; remediation via Automation Actions or **Rundeck**.  
**🏢 Deployment model** — PagerDuty Operations Cloud (SaaS).  
**🗒️ Notes** — Human‑centric: can auto‑execute safe diagnostics/remediations when confidence high; escalates if uncertain.

**🧠 UKM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**👁️ UOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🧬 UEOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 Qovery AI Migration Agent
⚙️ **Activities:** P/L  · 🔍 **Diagnostics:** P/L  · 🚀 **Provisioning:** Y/H (via IaC output)  
🧬 **Event ontology:** N/L  · 👁️ **Observability:** P/L  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Code‑first; OSS repo + web.  
**💡 What it actually does** — Scans apps and **generates Terraform/Dockerfiles** for PaaS→cloud migration; effort estimates.  
**📊 Data / telemetry** — One‑time analysis & config output.  
**🔗 Interoperability** — Terraform/Docker ecosystems; Qovery platform.  
**🏢 Deployment model** — OSS + Qovery cloud.  
**🗒️ Notes** — Produces artifacts; doesn’t run live observability.

**🧠 UKM — Snapshot:** Ingest **P/L**, Index **N/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**⚙️ UAM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🔍 UDM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**👁️ UOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🧬 UEOM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

**🚀 UPM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

---

## 🧩 Salesforce Agentforce (OpsAI)
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/H  · 🚀 **Provisioning:** Y/M  
🧬 **Event ontology:** Y/H  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** High

**🏗️ Build style / interface** — Low‑code **Agent Studio** + Apex; **Command Center**; MCP support.  
**💡 What it actually does** — Ingest/search via **Data Cloud**; incident/ops flows; trigger actions and integrations.  
**📊 Data / telemetry** — Data Cloud topics/events; agent metrics in Command Center.  
**🔗 Interoperability** — MCP, MuleSoft, Flows, partner tools.  
**🏢 Deployment model** — Salesforce Cloud.  
**🗒️ Notes** — OpsAI positioned as Agentforce use‑case.

**🧠 UKM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🚀 UPM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

---

## 🧩 ServiceNow AI Agent Orchestrator
⚙️ **Activities:** Y/H  · 🔍 **Diagnostics:** Y/H  · 🚀 **Provisioning:** Y/M  
🧬 **Event ontology:** Y/H  · 👁️ **Observability:** Y/M  · 📈 **Confidence:** High

**🏗️ Build style / interface** — No/low‑code **Agent Studio**; orchestrates across ITSM/ITOM.  
**💡 What it actually does** — Multi‑agent coordination, incident workflows, runbooks; **OTel → CMDB** via Service Graph.  
**📊 Data / telemetry** — ITSM/CMDB/CSDM; OpenTelemetry via Service Graph.  
**🔗 Interoperability** — Integrations, scripts, OTel.  
**🏢 Deployment model** — ServiceNow Cloud.  
**🗒️ Notes** — Provisioning via integrations/runbooks.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/H**, Overall **High**.

**⚙️ UAM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🔍 UDM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**👁️ UOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🧬 UEOM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🚀 UPM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

---

## 🧩 Snowflake Cortex Agents
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** P/L  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** Y/H  · 👁️ **Observability:** P/L  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — Low‑code + SQL/Python inside Snowflake.  
**💡 What it actually does** — Agents orchestrate **Cortex Analyst** (structured) + **Cortex Search** (unstructured) with tools/LLMs.  
**📊 Data / telemetry** — Agent conversation logs; monitoring APIs.  
**🔗 Interoperability** — Custom tools via UDFs/SPs; REST API.  
**🏢 Deployment model** — Snowflake SaaS.  
**🗒️ Notes** — Data‑centric scope; not infra AIOps.

**🧠 UKM — Snapshot:** Ingest **Y/M**, Index **Y/H**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**👁️ UOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🧬 UEOM — Snapshot:** Ingest **Y/H**, Index **Y/H**, Retrieval **Y/H**, Governance **Y/H**, Overall **High**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

---

## 🧩 Termius — Gloria
⚙️ **Activities:** P/M  · 🔍 **Diagnostics:** P/M  · 🚀 **Provisioning:** P/M  
🧬 **Event ontology:** N/L  · 👁️ **Observability:** P/M  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — In‑app assistant in Termius; no‑code UX.  
**💡 What it actually does** — Runs services/commands over SSH; pull/configure/run Docker containers; log/VM plans emerging.  
**📊 Data / telemetry** — Session/command outcomes; light history.  
**🔗 Interoperability** — SSH‑first.  
**🏢 Deployment model** — Termius Cloud + your hosts over SSH.  
**🗒️ Notes** — Not a full AIOps suite; roadmap evolving.

**🧠 UKM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **P/M**, Governance **P/M**, Overall **Low**.

**⚙️ UAM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🔍 UDM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**👁️ UOM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

**🧬 UEOM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

**🚀 UPM — Snapshot:** Ingest **P/M**, Index **P/M**, Retrieval **P/M**, Governance **P/M**, Overall **Medium**.

---

## 🧩 Zencoder AI Agents
⚙️ **Activities:** Y/M  · 🔍 **Diagnostics:** Y/M  · 🚀 **Provisioning:** P/L  
🧬 **Event ontology:** N/L  · 👁️ **Observability:** P/L  · 📈 **Confidence:** Med

**🏗️ Build style / interface** — Code‑first; CI webhook/CLI.  
**💡 What it actually does** — Autonomous coding agents to fix failing tests, patch vulns, add docs/tests, open PRs.  
**📊 Data / telemetry** — CI runs/issues/PRs dashboards.  
**🔗 Interoperability** — GitHub/Jira/Sentry, etc.  
**🏢 Deployment model** — SaaS + CLI.  
**🗒️ Notes** — PR‑centric; not runtime infra ops.

**🧠 UKM — Snapshot:** Ingest **P/L**, Index **N/L**, Retrieval **P/M**, Governance **P/M**, Overall **Medium‑Low**.

**⚙️ UAM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**🔍 UDM — Snapshot:** Ingest **Y/M**, Index **Y/M**, Retrieval **Y/M**, Governance **Y/M**, Overall **Medium‑High**.

**👁️ UOM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.

**🧬 UEOM — Snapshot:** Ingest **N/L**, Index **N/L**, Retrieval **N/L**, Governance **N/L**, Overall **Low**.

**🚀 UPM — Snapshot:** Ingest **P/L**, Index **P/L**, Retrieval **P/L**, Governance **P/L**, Overall **Low‑Medium**.


---

# Appendix — Verification Notes (Oct 2025)

This edition incorporates source‑verified changes across all vendors (see “Latest updates” links in each card). Highlights:
- **Agentforce 3** adds **Command Center** & **MCP**; enterprise observability for agents (Salesforce press + landing).  
- **Strands SDK** open‑sourced with **OTel** and **MCP**; prescriptive guidance and GitHub activity.  
- **Splunk/Cisco** unveils **agentic AI** across Observability (.conf25).  
- **Databricks Agent Bricks** launched; subsequent enterprise partnerships reported.  
- **Snowflake Cortex Agents** document multi‑tool orchestration (Analyst + Search) and monitoring.  
- **ServiceNow** details **AI Agent Orchestrator/Studio** and **OTel → CMDB** connector.  
- **JFrog Fly** (agentic repo) announced with MCP integrations; beta.  
- **Qovery** OSS migration agent generates Terraform/Dockerfiles for PaaS→cloud.  
- **Rovo Dev** now GA across CLI/Bitbucket/GitHub.  
- **Termius Gloria** blog confirms SSH/Docker scope.  

**Additions (Oct 2025):**
- **Datadog Bits AI & Agents** launched/expanded at DASH 2025 (SRE/Dev/Sec agents; post‑mortems).  
- **Elastic AI Assistant** iterated 2024–2025 with ESRE grounding, multi‑step chat, runbook proposals.  
- **Microsoft Azure Copilot (Agent Mode)** GA June 2025 with Bicep generation, `az`/`azd` orchestration, confirmation‑gated changes under RBAC.  
- **Microsoft Azure AI Agent Service (Foundry)** GA mid‑2025 (Logic Apps as tools, AgentOps, OTel traces); **Oct 2025** open‑source Agent Framework SDK.  
- **New Relic AI** (Grok → AI) adds NRQL generation, guided instrumentation, change‑aware analysis.  
- **PagerDuty AIOps** introduces AI Agent Suite (Oct 2025) for incident response & insights.

---

# Appendix — Verified Sources (Oct 2025)

- **Salesforce Agentforce 3 (Command Center, MCP):** https://www.salesforce.com/partners/solutions/technology-partner/agentforce-3/  
- **AWS agents observability with OpenTelemetry (AgentCore/Strands):** https://aws.amazon.com/blogs/mt/observability-patterns-for-ai-agents-on-aws-with-amazon-bedrock-agentcore/  
- **Cisco / Splunk AI Assistant for IT Operations:** https://www.splunk.com/en_us/blog/it/ai-assistant-for-it-operations.html  
- **Dynatrace Davis AI causal correlation docs:** https://docs.dynatrace.com/docs/shortlink/ai-correlation#how-it-works  
- **ServiceNow Service Graph Connector for OpenTelemetry (OTel → CMDB):** https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/solution-brief/service-graph-connector-for-opentelemetry.pdf  
- **Snowflake Cortex Agents (Run API):** https://docs.snowflake.com/en/developer-guide/snowflake-cortex/agents/command/run  
- **Dataiku Trace Explorer (product blog):** https://www.dataiku.com/blog/trace-explorer-in-dataiku-13-2/  
- **Databricks Agent Bricks (news):** https://www.reuters.com/business/finance/databricks-buy-sequoia-backed-tecton-ai-agent-push-2025-08-22/  
- **JFrog Fly (agentic repository) press:** https://jfrog.com/press/introducing-jfrog-fly-the-industrys-first-agentic-repository/  
- **DuploCloud Terraform Provider:** https://registry.terraform.io/providers/duplocloud/duplocloud/latest  
- **Termius — Gloria (DevOps AI Agent):** https://termius.com/blog/devops-ai-agent-gloria  
- **Qovery Migration AI Agent:** https://medium.com/qovery/introducing-the-qovery-migration-ai-agent-3fe3892616b6  

**Newly added sources (Oct 2025):**
- **Microsoft Azure Copilot (Agent Mode) GA coverage:** https://visualstudiomagazine.com *(search: “Copilot for Azure Agent Mode GA June 2025”)*  
- **Microsoft Azure AI Agent Service / Foundry (overview & GA):** https://azure.microsoft.com *(Agent Service/Foundry)* • https://www.infoq.com/news/ *(search: “Azure AI Agent Service GA Logic Apps tools”)*  
- **Datadog Bits AI & Agents launch:** https://www.datadoghq.com  
- **Elastic AI Assistant for Observability:** https://www.elastic.co • https://www.digitalisationworld.com  
- **New Relic AI (Grok → AI):** https://newrelic.com  
- **PagerDuty AIOps AI Agent Suite recap:** https://www.aimmediahouse.com *(search: “PagerDuty AI Agent Suite 2025”)*


## Neutral one-line summaries (A–Z)

- **[Atlassian Rovo Dev]({{ '/platforms/atlassian-rovo-dev' | relative_url }})** — Developer-centric coding/PR automation that links Jira↔Docs↔Code; infrastructure ops are out of scope.
- **[AWS Strands SDK]({{ '/platforms/aws-strands-sdk' | relative_url }})** — Code-first agent framework to plan/act with tools on AWS with OTel traces; bring your own knowledge layer.
- **[Cisco Splunk AI Agents]({{ '/platforms/cisco-splunk-ai-agents' | relative_url }})** — Agents embedded in Splunk for telemetry, anomaly/RCA, and playbook-driven remediation across Cisco/Splunk ecosystem.
- **[Databricks Agent Bricks]({{ '/platforms/databricks-agent-bricks' | relative_url }})** — Lakehouse-native agent evaluation and guardrails with MLflow traces; not intended for infra ops.
- **[Datadog Bits AI & Agents]({{ '/platforms/datadog-bits-ai' | relative_url }})** — Hypothesis-driven triage/RCA and incident comms over unified Datadog telemetry; can suggest runbooks/PRs.
- **[Dataiku AI Agents]({{ '/platforms/dataiku-ai-agents' | relative_url }})** — Governed agents for data workflows with Trace Explorer; strong tracing/guardrails, limited direct provisioning.
- **[DuploCloud AI Help Desk]({{ '/platforms/duplocloud-ai-help-desk' | relative_url }})** — Ticket-driven DevOps agents with Terraform-backed provisioning and rollback in the DuploCloud context.
- **[Dynatrace Davis AI]({{ '/platforms/dynatrace-davis-ai' | relative_url }})** — Causal correlation/RCA over full-stack telemetry, producing “Davis problems” with evidence; remediation via workflows.
- **[Elastic AI Assistant]({{ '/platforms/elastic-ai-assistant' | relative_url }})** — ESRE-grounded explanations and query suggestions inside Elastic Observability with runbook proposals.
- **[GitHub Copilot Coding Agent]({{ '/platforms/github-copilot-coding-agent' | relative_url }})** — Async cloud agent that fixes code/tests and opens PRs; infrastructure changes are PR-only.
- **[Google Vertex AI Agent Builder]({{ '/platforms/google-vertex-agent-builder' | relative_url }})** — No-code/ADK for conversational and multi-agent apps with webhooks/GCP actions; ops via external services.
- **[IBM AskIAM]({{ '/platforms/ibm-askiam' | relative_url }})** — IAM-focused assistant for requests/approvals and cross-system provisioning; limited deep infra observability.
- **[JFrog Fly (Agentic Repository)]({{ '/platforms/jfrog-fly-agentic-repo' | relative_url }})** — Agent-aware artifact/release governance with policy/evidence events; not a runtime ops console.
- **[Kagent (Solo.io)]({{ '/platforms/soloio-kagent' | relative_url }})** — Kubernetes-native agents orchestrating K8s/Prom/Grafana/Helm/Argo for diagnostics and guarded actions.
- **[Kuberns Platform]({{ '/platforms/kuberns-platform' | relative_url }})** — Managed PaaS with AI-assisted deployment/ops; third-party validation is currently limited.
- **[Microsoft Azure AI Agent Service (Foundry)]({{ '/platforms/azure-ai-agent-service-foundry' | relative_url }})** — Enterprise service to build/orchestrate multi-agent workflows with AgentOps and Logic Apps tools.
- **[Microsoft Azure Copilot (Agent Mode)]({{ '/platforms/azure-copilot-agent-mode' | relative_url }})** — VS Code operator that generates/edits Bicep and runs Azure CLI under RBAC with explicit confirmations.
- **[New Relic AI]({{ '/platforms/new-relic-ai' | relative_url }})** — Natural-language telemetry queries, NRQL generation, and change-aware analysis; advisory only (no direct apply).
- **[Opsera Hummingbird (Unified Insights)]({{ '/platforms/opsera-hummingbird' | relative_url }})** — Unified DevOps insights/DORA metrics with recommendations; actions routed via integrations.
- **[PagerDuty AIOps]({{ '/platforms/pagerduty-aiops' | relative_url }})** — Incident intelligence for noise reduction, correlation, comms drafts, and safe diagnostics/remediations via Automation Actions/Rundeck.
- **[Qovery AI Migration Agent]({{ '/platforms/qovery-migration-agent' | relative_url }})** — Scans apps and outputs Terraform/Dockerfiles for cloud migration; produces artifacts, not live changes.
- **[Salesforce Agentforce (OpsAI)]({{ '/platforms/salesforce-agentforce-opsai' | relative_url }})** — Data Cloud-backed agents for ops flows with actions via Flows/MuleSoft and Command Center observability.
- **[ServiceNow AI Agent Orchestrator]({{ '/platforms/servicenow-ai-agent-orchestrator' | relative_url }})** — Multi-agent workflows across ITSM/ITOM with CMDB/OTel mapping; provisioning through runbooks/integrations.
- **[Snowflake Cortex Agents]({{ '/platforms/snowflake-cortex-agents' | relative_url }})** — Data-centric agents orchestrating Analyst/Search with tools/LLMs; infrastructure AIOps out of scope.
- **[Termius — Gloria]({{ '/platforms/termius-gloria' | relative_url }})** — SSH-native assistant to run services/commands and manage Docker on hosts; early provisioning features.
- **[Zencoder AI Agents]({{ '/platforms/zencoder-ai-agents' | relative_url }})** — CI-centric autonomous code fixers that diagnose failing pipelines and open PRs.
