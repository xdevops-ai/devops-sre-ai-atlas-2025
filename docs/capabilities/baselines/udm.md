# 🧭 Universal Diagnostic Model (UDM) — v2 (0–4 scale)
*A vendor‑neutral baseline describing how intelligent Ops/Observability systems **detect, enrich, correlate, explain (RCA), and recommend/remediate** incidents — with verifiable evidence.*

**Last updated:** 2025-10-12T12:28:58Z

---

## What changed in v2
- **Maturity scale normalized to 0–4** (was 0–4/0–5 across sources). Clear **acceptance gates** per level.
- **Precise phase names**: Signal Detection · Context Enrichment · Event Correlation & Classification · Root Cause Analysis · Recommendation/Remediation.
- **Atlas alignment**: Token→numeric mapping for the Atlas **🔍 Diagnostics** capability.
- **Operational metrics**: TTFC/TTRC, Verified‑RCA rate, false‑positive rate added as non‑functional targets.
- **Exports**: Scorecard CSV and machine‑readable rubric JSON.

---

## ⚙️ Five Diagnostic Phases
| # | Phase | Definition | Typical Data | Expected Capability |
|---:|---|---|---|---|
| **1** | **Signal Detection** | Identify anomalies or deviations from expected behavior | Metrics (CPU/latency/errors), logs, traces, alerts | Thresholds, anomaly detectors, drift‑aware baselines; capture detection reason & thresholds |
| **2** | **Context Enrichment** | Link signals with entities, ownership, deploy/change context | Service maps, k8s/CMDB, deploy metadata | Stable IDs, dependency graph, change/owner joins, SLO context |
| **3** | **Event Correlation & Classification** | Group related signals and classify the probable domain/cause family | Multi‑signal events across time windows | Correlation windows, clustering/causal hints, change‑aware grouping |
| **4** | **Root Cause Analysis (RCA)** | Produce a **testable hypothesis** explaining *why* with evidence | Enriched telemetry + historical baselines + change diffs | Structured hypothesis + verification plan; confidence; negative evidence considered |
| **5** | **Recommendation / Remediation** | Propose (or execute under guardrails) a mitigation with verification | Runbooks, IaC diffs, workflows | Risk‑aware plan, preflight checks, approvals; rollback & post‑verify steps |

---

## 🧩 UDM Maturity Scale (0–4)

| Level | Label | Acceptance (must satisfy this level **and** all lower levels) |
|---:|---|---|
| **0** | **None** | No diagnostics beyond raw alerts/logs; no context; no evidence export. |
| **1** | **Reactive** | L1 detection: manual/threshold alerts; minimal labeling; ad‑hoc triage notes. |
| **2** | **Correlated** | L2 detection + **multi‑signal correlation or rule‑based classification**; entity/service mapping; links to evidence (queries/logs/traces). |
| **3** | **Intelligent** | L3 adds **structured RCA** with **verification steps** (counter‑tests), confidence scoring, change awareness, and **explainable evidence** (permalinks/queries included). |
| **4** | **Autonomous** | L4 adds **causal reasoning/graphs**, **automated counter‑tests**, early‑finalize on high confidence, and **guardrailed remediation** (approvals/rollback), with tracked quality metrics (Verified‑RCA rate, FP rate). |

> **Gating rule:** A product’s **UDM level** is the **highest level** whose acceptance gates (and all below) are met. Any missing gate caps the level.

---

## 🔎 Per‑phase expectations by level (condensed)

### 1) Signal Detection
- **L0:** Raw alerts or manual observation only.  
- **L1:** Static thresholds; alert definitions exist; detection reason/threshold captured.  
- **L2:** **Anomaly detection** or pattern mining; cross‑signal awareness.  
- **L3:** Baselines per entity/SLO; change‑aware detectors reduce noise.  
- **L4:** Drift detection, adaptive thresholds; quality metrics (precision/recall) tracked.

### 2) Context Enrichment
- **L0:** No stable IDs; no owners.  
- **L1:** Basic labels (service/env).  
- **L2:** **Entity/owner mapping**; dependency edges; deploy metadata attached.  
- **L3:** SLO context + recent **change** joins; impact radius estimated.  
- **L4:** Versioned topology; out‑of‑date context flagged; lineage kept.

### 3) Event Correlation & Classification
- **L0:** Each alert stands alone.  
- **L1:** Manual grouping.  
- **L2:** **Time‑window correlation**; domain tagging (network/db/app).  
- **L3:** Multi‑signal clustering + **change‑aware grouping**; duplicate suppression.  
- **L4:** Causal graph with scored edges; near‑duplicate incidents merged automatically.

### 4) Root Cause Analysis (RCA)
- **L0:** No causal statement.  
- **L1:** Free‑text guess; no tests.  
- **L2:** Heuristic RCA with links to **raw evidence**.  
- **L3:** **Structured hypothesis** (entity/change), **verification plan** with counter‑tests, confidence value, and negative evidence.  
- **L4:** **Causal/graph‑based** RCA; automated counter‑tests; **early finalize** on high confidence; false‑positive rate tracked.

### 5) Recommendation / Remediation
- **L0:** None.  
- **L1:** Human advice only.  
- **L2:** Runbook suggestions with evidence links.  
- **L3:** **Structured plan**: preflight checks, risk notes, post‑verify steps.  
- **L4:** **Guardrailed automation**: approvals, drift checks, **rollback plan**, closed‑loop verification and audit.

---

## ✅ Feature Requirements (FR) & Acceptance Criteria (AC)

**F1. Detection** — Ingest metrics/logs/traces; configurable thresholds and anomaly detectors; store **detection reason** (rule, threshold, model).  
**AC:** A sample incident shows detection metadata (why/where), reproducible by re‑running the query or rule.

**F2. Context** — Maintain entity IDs, owners, dependency/impact edges, deploy/change metadata, SLO context.  
**AC:** Given an incident, the system lists affected entity, owner, last deploy/change, and SLO window.

**F3. Correlation** — Group events across a window; label domain; suppress duplicates; link correlation evidence.  
**AC:** Incident record shows the grouped alerts with grouping rationale and time bounds.

**F4. RCA** — Emit **hypotheses[]** with fields: `entity`, `suspected_change`, `evidence_refs[]`, `counter_tests[]`, `confidence` (0–1).  
**AC:** At least one counter‑test runs and is linkable; negative evidence reduces confidence.

**F5. Recommendation/Remediation** — Produce a plan with steps, **preflight checks**, required approvals, and **post‑verify**.  
**AC:** Plan lists commands/runbooks or PRs; on execution, verification results are attached; rollback path is present.

---

## 📈 Non‑functional Targets (diagnostic quality & speed)

- **TTFC** (time‑to‑first‑clue) P50 ≤ **60 s**, P95 ≤ **3 min** on standard incident set.  
- **TTRC** (time‑to‑root‑cause) P50 ≤ **10 min**, P95 ≤ **30 min** (for contained scope).  
- **Verified‑RCA rate** ≥ **80%** on curated set; **false‑positive rate** tracked and trending down.  
- **Explainability**: each RCA contains **evidence permalinks**; queries are re‑runnable.  
- **Stability**: detectors tolerant to data gaps; safeguards against alert storms.

---

## 🔁 Atlas alignment (🔍 Diagnostics token → UDM level)

| Atlas token | UDM level |
|---|---:|
| **N/L** | **0** |
| **P/L** | **1** |
| **P/M** | **2** |
| **Y/M** | **3** |
| **Y/H** | **4** |

> Use this to convert Atlas table entries into UDM’s 0–4 for composite scoring.

---

## 🧠 Neutral Diagnostic Event (JSON example)

```json
{
  "diagnostic_event": {
    "id": "uuid",
    "timestamp": "2025-10-08T15:00:00Z",
    "phase": "root_cause",
    "signal": { "metric": "latency_p95", "value": 560, "threshold": 200 },
    "context": { "service": "api-gateway", "node": "node-12", "region": "eu-west" },
    "correlation_group": "incident-4431",
    "root_cause": { "hypothesis": "deployment rollback failed", "confidence": 0.87 },
    "evidence_refs": ["grafana://...","loki://...","change://deploy/abc123"],
    "counter_tests": ["promql://increase(errors_total,5m)","logql://kubernetes.container.name=api-gateway"],
    "recommendation": { "action": "redeploy previous version", "automatable": true, "requires_approval": true }
  }
}
```

---

## 🔍 Comparison Template (vs. UDM)

| Platform | Signal Detection | Context Enrichment | Event Correlation | Root Cause Analysis | Recommendation/Remediation | **Overall UDM Level (0–4)** |
|---|---|---|---|---|---|---|
| **Your Platform** |  |  |  |  |  |  |
| Competitor A |  |  |  |  |  |  |
| Competitor B |  |  |  |  |  |  |

> Keep evidence links (alert rules, queries, grouped incident records, RCA plans, runbooks) for every ✓.

---

## 📝 Conformance Checklist

- Detection records include **why** (rule/model/threshold) and are reproducible.  
- Entity/owner/deploy/change context resolvable for each incident.  
- Correlation shows window/rationale and suppresses duplicates.  
- RCA includes **structured hypothesis**, **counter‑tests**, **confidence**, and **negative evidence** handling.  
- Recommendations include **preflight**, **approvals**, **post‑verify**, and **rollback**.  
- Evidence links are permalinks; raw queries/logs are accessible.  
- Quality metrics (Verified‑RCA rate, FP rate) are tracked and reported.

---

## 📊 Suggested KPIs for bake‑offs (diagnostics)

- **TTFC/TTRC** distribution on a fixed incident corpus.  
- **Verified‑RCA rate** and **false‑positive rate**.  
- **Correlation quality**: % incidents with correct grouping; duplicate suppression ratio.  
- **Explainability**: % RCAs with runnable queries/logs attached.  
- **Actionability**: % incidents with a safe, approved next step.

---

## 📊 Ratings — Current Platforms (UDM v2)

| Platform | UDM Level |
|---|---:|
| Atlassian – Rovo Dev | 2 |
| AWS – Strands SDK | 1 |
| Cisco – Splunk AI Agents (AgenticOps) | 4 |
| Databricks – Agent Bricks | 3 |
| Datadog – Bits AI SRE | 4 |
| Dataiku – AI Agents | 4 |
| DuploCloud – AI Help Desk | 4 |
| Dynatrace – Davis AI | 4 |
| Elastic – AI Assistant for Observability | 2 |
| GitHub – Copilot | 1 |
| Google – Vertex AI Agent Builder | 1 |
| IBM – AskIAM | 3 |
| JFrog – Project Fly | 2 |
| Solo.io – Kagent | 3 |

> Levels reflect the strict UDM v2 gating rules (evidence‑backed RCA, counter‑tests, change awareness, and governed remediation).

---

## 🧾 Platform Notes — Evidence‑backed summaries

### Atlassian – Rovo Dev — **UDM 2**
- **Signal Detection:** Reactive; relies on Atlassian alerts (Opsgenie/Compass); no native anomaly detection.  
- **Context Enrichment:** Uses Teamwork Graph to pull commits, issues, docs for a target service.  
- **Event Correlation & Classification:** Light correlation via graph lookups; no multi‑signal causation.  
- **Root Cause Analysis:** Smart search across Atlassian data; identifies likely causes from history, not raw telemetry.  
- **Recommendation/Remediation:** Suggests runbooks/docs; can open PRs/tickets; no autonomous fixes.

### AWS – Strands SDK — **UDM 1**
- **Signal Detection:** None by default; developers must wire to CloudWatch or alerts.  
- **Context Enrichment:** Tooling available, but correlation logic is custom to each agent.  
- **Event Correlation & Classification:** No built‑in engine; depends on prompts/code.  
- **Root Cause Analysis:** LLM‑driven heuristics only as implemented; accuracy varies.  
- **Recommendation/Remediation:** Actions possible via tools; suggestions are unverified unless you add checks.

### Cisco – Splunk AI Agents (AgenticOps) — **UDM 4**
- **Signal Detection:** Continuous multi‑domain telemetry with dynamic baselines; predictive alerting; Event iQ noise reduction.  
- **Context Enrichment:** Cross‑domain enrichment (network ↔ app ↔ infra) with ITSI episodes.  
- **Event Correlation & Classification:** Automatic episode correlation & dedup; prioritized incidents.  
- **Root Cause Analysis:** Causal algorithms pinpoint probable root cause with evidence & timeline.  
- **Recommendation/Remediation:** Actionable recommendations & optional automation via runbooks/integrations.

### Databricks – Agent Bricks — **UDM 3**
- **Signal Detection:** Triggered by jobs/model drift; no general prod monitoring out‑of‑box.  
- **Context Enrichment:** Rich context from Lakehouse (lineage, MLflow), strong data joins.  
- **Event Correlation & Classification:** Good in data/ML domain; relies on implementation for breadth.  
- **Root Cause Analysis:** Multi‑step SQL/ML analyses across curated data when coded.  
- **Recommendation/Remediation:** Can run notebooks/workflows; typically human‑approved.

### Datadog – Bits AI SRE — **UDM 4**
- **Signal Detection:** Launches investigations on monitor alerts; groups related alerts to reduce noise.  
- **Context Enrichment:** Pulls APM, infra, logs, deploys, runbooks; builds incident timeline.  
- **Event Correlation & Classification:** Multi‑hypothesis testing & consolidation into one incident.  
- **Root Cause Analysis:** Rapid, evidence‑linked RCA with charts, logs, traces.  
- **Recommendation/Remediation:** Prescriptive steps & comms; human‑in‑the‑loop for execution.

### Dataiku – AI Agents — **UDM 4**
- **Signal Detection:** Anomaly triggers in pipelines/metrics; jobs & KPI thresholds.  
- **Context Enrichment:** Business context, curated datasets, model metadata.  
- **Event Correlation & Classification:** Cross‑dataset analyses; topic‑driven classification.  
- **Root Cause Analysis:** Explains drivers (e.g., churn/revenue) with traceable data.  
- **Recommendation/Remediation:** Suggests actions; can trigger pipelines under governance.

### DuploCloud – AI Help Desk — **UDM 4**
- **Signal Detection:** User‑driven & system‑driven ticketing; ties to platform monitors.  
- **Context Enrichment:** Deep context of cloud config & live state via embedded terminal.  
- **Event Correlation & Classification:** Recognizes known patterns across k8s/network/permissions.  
- **Root Cause Analysis:** Interactive verification by running safe commands; fast isolation.  
- **Recommendation/Remediation:** AI‑suggested commands; one‑click approved fixes with guardrails.

### Dynatrace – Davis AI — **UDM 4**
- **Signal Detection:** Real‑time anomalies with seasonal baselines; single Problem event.  
- **Context Enrichment:** Smartscape topology; business impact (RUM/SLO).  
- **Event Correlation & Classification:** Automatic causation across stack; deduped problem context.  
- **Root Cause Analysis:** Causal AI pinpoints root process/service; explains evidence.  
- **Recommendation/Remediation:** Runbook suggestions & automation engine integrations.

### Elastic – AI Assistant for Observability — **UDM 2**
- **Signal Detection:** Assistive; piggybacks on Elastic alerts/ML jobs.  
- **Context Enrichment:** Fast log/trace explanations within Kibana context.  
- **Event Correlation & Classification:** User‑steered queries across logs/metrics/traces.  
- **Root Cause Analysis:** Great for log triage; limited multi‑system causation.  
- **Recommendation/Remediation:** Light guidance; no autonomous actions.

### GitHub – Copilot — **UDM 1**
- **Signal Detection:** None in prod; focused on code/tests in dev.  
- **Context Enrichment:** Understands repo/test context; no ops telemetry.  
- **Event Correlation & Classification:** N/A for ops; helps interpret build logs.  
- **Root Cause Analysis:** Explains code/test failures; not system incidents.  
- **Recommendation/Remediation:** Generates code/config fixes after human diagnosis.

### Google – Vertex AI Agent Builder — **UDM 1**
- **Signal Detection:** None out‑of‑box; flows trigger via intents/webhooks.  
- **Context Enrichment:** Developer‑defined; can fetch metrics via tools.  
- **Event Correlation & Classification:** Scripted logic; no generic engine.  
- **Root Cause Analysis:** Decision‑tree style unless extended.  
- **Recommendation/Remediation:** Can call tools; governed by custom flows.

### IBM – AskIAM — **UDM 3**
- **Signal Detection:** Detects IAM issues (missing roles/SOD conflicts) on queries.  
- **Context Enrichment:** Unifies users↔roles↔apps; pulls login/audit traces.  
- **Event Correlation & Classification:** Deterministic policy reasoning across identity graph.  
- **Root Cause Analysis:** Explains ‘why/why not’ access with full chain of evidence.  
- **Recommendation/Remediation:** Initiates revoke/grant with approvals; governed changes.

### JFrog – Project Fly — **UDM 2**
- **Signal Detection:** CI/CD failure events; artifact policy blocks.  
- **Context Enrichment:** Artifact metadata, Xray findings, repo context.  
- **Event Correlation & Classification:** Maps build failures to deps/repos.  
- **Root Cause Analysis:** Pinpoints failing step/dependency; limited beyond pipeline.  
- **Recommendation/Remediation:** Suggests fixes; automates routine CI tasks.

### Solo.io – Kagent — **UDM 3**
- **Signal Detection:** K8s/service‑mesh events (crashloops, 5xx, policy blocks).  
- **Context Enrichment:** K8s objects, YAML, mesh telemetry, network policies.  
- **Event Correlation & Classification:** Links config ↔ runtime failures.  
- **Root Cause Analysis:** K8s expert checks (deploys, policies, routing).  
- **Recommendation/Remediation:** Proposes YAML patches/commands; optional apply with RBAC.

---

## 🧩 Summary (what the ratings say)
- **Level 4 (Autonomous):** Cisco/Splunk, Datadog, Dataiku, DuploCloud, Dynatrace — deliver multi‑signal detection, explainable RCA with evidence, and **guardrailed remediation**.  
- **Level 3 (Intelligent):** Databricks, Solo.io, IBM AskIAM — strong structured RCA in their domains; remediation is governed but not fully automated across all use‑cases.  
- **Level 2 (Correlated):** Atlassian, Elastic, JFrog — correlate and guide investigations; RCA is heuristic; remediation remains manual.  
- **Level 1 (Reactive):** AWS Strands, GitHub Copilot, Google Vertex — frameworks/assistants that require custom wiring for diagnostics.  
- **Key gates failing at lower levels:** lack of **evidence‑linked RCA** and **counter‑tests**, limited **change awareness**, and absence of **guardrailed remediation with rollback**.
