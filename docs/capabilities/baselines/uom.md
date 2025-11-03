---
layout: default
title: UOM Baseline (v2)
parent: Capability Framework
nav_order: 5
has_children: true
permalink: /capabilities/baselines/uom/
last_updated: 2025-10-12T12:46:23Z
---

# 👁️ Universal Observability Model (UOM) — v2 (0–4 scale)
*A vendor-neutral baseline describing how platforms **collect, normalize, store, explore, alert, correlate, and govern** observability data (metrics, logs, traces, events, profiles).*

**Last updated:** 2025-10-12T12:46:23Z

---

## What changed in v2

- **Maturity scale normalized to 0–4** with explicit **acceptance gates** per phase.
- **Evidence discipline:** To claim Level ≥ 3, platforms must provide **shareable evidence** (permalinks/exports) that reproduce the charts/queries used.
- **Cross-signal gate:** Without **cross-signal drill-downs** (e.g., metrics → logs/traces on the same entity/time window), overall level is **capped at 2 (Unified)**.
- **Governance gate:** Level 4 requires **RBAC, PII controls, cost guardrails**, and **ingest/query SLOs**.
- **Atlas alignment:** token→numeric mapping for the Atlas **👁️ Observability** capability.

---

## ⚙️ Eight Observability Phases

| #   | Phase                        | Definition                                   | Typical Data                              | Expected Capability                                                   |
|:---:|-----------------------------|----------------------------------------------|-------------------------------------------|-----------------------------------------------------------------------|
| **1** | **Instrumentation & Ingest**   | Capture signals from apps/infra safely        | Metrics, logs, traces, K8s events, profiles | SDKs/agents/collectors; scrape/push; secure endpoints; backpressure   |
| **2** | **Normalization & Enrichment** | Apply schemas; add rich context               | OTel semantic conv., env/service/version/team | Tagging; parsing; K8s enrichment; time sync                          |
| **3** | **Storage, Sampling & Indexing** | Persist/index efficiently by signal           | TSDB/log store/trace store; retention tiers | Tiered retention; sampling; cardinality control                       |
| **4** | **Visualization & Exploration** | Explore across signals & entities             | Dashboards; *QL (Prom/Log/Trace); entity pages | Cross-signal drill-downs; templating                                 |
| **5** | **Alerting, SLOs & Detection**  | Notify on symptoms/outcomes                   | Rules, SLI/SLO burn, anomalies            | Multi-signal alerts; dedupe; escalation; runbooks                     |
| **6** | **Topology & Context**          | Understand relationships & changes            | Service maps; K8s; CMDB/ownership         | Dependency graphs; change awareness                                   |
| **7** | **Incident Evidence & Handoffs** | Package findings for action                   | Links, snapshots, exports                 | Evidence packs; permalinks; ticket/chat exports                       |
| **8** | **Governance, Cost & Reliability** | Keep it safe, fast, affordable               | RBAC, PII, quotas, cost; SLOs             | Quotas, rate limits, usage & cost reports; ingest/query SLOs          |

---

## 🧩 UOM Maturity Scale (0–4)

| Level | Label                | Acceptance (must satisfy all lower levels)                                                                 |
|:----:|----------------------|--------------------------------------------------------------------------------------------------------------|
| **0** | **None**             | No systematic signals; ad-hoc SSH/logs only.                                                                |
| **1** | **Single-signal**    | One signal (e.g., metrics **or** logs) with manual dashboards; minimal schema.                              |
| **2** | **Unified**          | At least **two signals** (metrics + logs and/or traces) in one UX; basic enrichment and search; **exportable queries**. |
| **3** | **Contextual**       | Cross-signal drill-downs; SLOs; entity/topology pages; **evidence packs** for incidents.                     |
| **4** | **Governed/Optimized** | Anomaly detection or tail-based sampling, dedupe/correlation; RBAC/PII; ingest/query SLOs; cost guardrails; tenancy. |

> **Gating rules**
> - **Evidence gate:** No shareable permalinks/exports → **cap at 2**.  
> - **Cross-signal gate:** No metrics↔logs/traces drill-down on entities → **cap at 2**.  
> - **Governance gate:** No RBAC/PII/cost & SLOs → **cap at 3**.

---

## 🔎 Per‑phase expectations by level (condensed)

### 1) Instrumentation & Ingest
- **L0:** No collectors/SDKs.  
- **L1:** One signal via agent/scrape; best‑effort endpoints.  
- **L2:** Two signals; authenticated endpoints; basic backpressure.  
- **L3:** Multi‑signal with HA collectors; buffering; drop metrics; ingest lag tracked.  
- **L4:** Fleet management; auto‑instrumentation; SLOs on ingest lag/loss.

### 2) Normalization & Enrichment
- **L0:** Raw payloads.  
- **L1:** Minimal labels; ad‑hoc parsing.  
- **L2:** OTel semantic conventions; env/service/version/team labels; K8s enrichment.  
- **L3:** Consistent parsing rules; time sync; owner mapping.  
- **L4:** Policy‑validated schemas; schema evolution; PII redaction on ingest.

### 3) Storage, Sampling & Indexing
- **L0:** Ephemeral storage.  
- **L1:** Single‑tier retention; no sampling/cardinality control.  
- **L2:** Retention per signal; basic sampling; index strategy.  
- **L3:** Tiered retention; tail‑based trace sampling; hot/cold moves; compaction.  
- **L4:** Adaptive sampling/cardinality budgets; cost/SLO‑aware retention.

### 4) Visualization & Exploration
- **L0:** None.  
- **L1:** Basic dashboards per signal.  
- **L2:** Unified UI; saved queries; ad‑hoc *QL.  
- **L3:** Cross‑signal drill‑downs; entity pages; panel templating.  
- **L4:** Time travel/compare; guided queries; shareable permalinks with provenance.

### 5) Alerting, SLOs & Detection
- **L0:** None.  
- **L1:** Static threshold alerts per signal.  
- **L2:** Multi‑signal alerts; maintenance windows; runbook links.  
- **L3:** SLI/SLO burn‑rates; dedupe; escalation & routing.  
- **L4:** Anomaly detection with quality tracking; noise budgets; change‑aware hints.

### 6) Topology & Context
- **L0:** None.  
- **L1:** Manual lists.  
- **L2:** Basic service map/K8s topology.  
- **L3:** Ownership links; change awareness; blast‑radius.  
- **L4:** Versioned topology with time travel; CMDB/graph joins.

### 7) Incident Evidence & Handoffs
- **L0:** None.  
- **L1:** Screenshots only.  
- **L2:** Query permalinks; export PNG/CSV/Markdown.  
- **L3:** One‑click **evidence packs** (query links, snapshots, context); ticket/chat exporters.  
- **L4:** Immutable evidence with provenance; retention guarantees.

### 8) Governance, Cost & Reliability
- **L0:** None.  
- **L1:** Shared admin; best‑effort availability.  
- **L2:** Basic RBAC; usage reports.  
- **L3:** Quotas/rate limiters; PII redaction; tenancy.  
- **L4:** Ingest/query SLOs; cost guardrails & budgets; per‑tenant named‑graph or index isolation.

---

## 🧠 Neutral Observability Signal (JSON example)

```json
{
  "observability_signal": {
    "id": "uuid",
    "ts": "2025-10-11T12:00:00Z",
    "signal_type": "metric",
    "resource": {
      "service.name": "api-gateway",
      "service.version": "1.42.0",
      "k8s.namespace": "payments",
      "k8s.pod": "api-gw-7b4d7",
      "cloud.region": "eu-west-1"
    },
    "attributes": {
      "http.method": "GET",
      "http.route": "/checkout",
      "deployment.sha": "0f3a1c2"
    },
    "metric": {
      "name": "http.server.duration",
      "type": "histogram",
      "unit": "ms",
      "p95": 560
    },
    "links": {
      "trace_id": "6f1c2…",
      "commit": "0f3a1c2",
      "runbook": "kb://checkout-latency"
    },
    "slo_context": {
      "sli": "latency_p95",
      "slo_target": 300,
      "window": "1h",
      "burn_rate": 2.1
    }
  }
}
```

---

## ✅ Feature Requirements (FR) & Acceptance Criteria (AC)

**F1. Instrumentation & Ingest** — SDKs/collectors; secure endpoints; buffering/backpressure.  
**AC:** Ingest health exposes lag/loss; auth on endpoints; HA collector config exists.

**F2. Normalization & Enrichment** — OTel conventions; env/service/version/team; parsers.  
**AC:** Sample records show normalized labels and K8s enrichment; parsing rules under version control.

**F3. Storage, Sampling & Indexing** — tiered retention; sampling; cardinality control.  
**AC:** Policy file shows per‑signal retention; trace sampling configured; label cardinality dashboard available.

**F4. Visualization & Exploration** — cross‑signal drills; entity pages.  
**AC:** From an alert panel, user can hop metrics→logs/traces on the same entity/time; saved permalinks exist.

**F5. Alerting, SLOs & Detection** — multi‑signal alerts; SLO burn; dedupe.  
**AC:** Alert definition references SLI/SLO; dedupe/noise metrics are visible; maintenance windows defined.

**F6. Topology & Context** — service map; ownership; change awareness.  
**AC:** Entity page shows owner/team and recent deploys/config changes.

**F7. Evidence & Handoffs** — exports & packs.  
**AC:** Evidence pack export (Markdown/JSON) contains query links, snapshots, and context; ticket/chat exporters configured.

**F8. Governance, Cost & Reliability** — RBAC; PII; quotas; SLOs.  
**AC:** RBAC policy applied; PII rules; usage & cost reports; ingest/query SLO dashboards.

---

## 📈 Quality KPIs & Target Bands (guide)

- **Ingest lag (P95)**: ≤ **6 s** (L3), ≤ **2 s** (L4).  
- **Query latency — dashboard (P95)**: ≤ **3 s** (L3), ≤ **1.5 s** (L4).  
- **Query latency — ad-hoc (P95)**: ≤ **7 s** (L3), ≤ **3 s** (L4).  
- **SLO coverage**: ≥ **50%** of services (L3), ≥ **80%** (L4).  
- **Alert dedupe ratio**: ≥ **30%** (L3), ≥ **50%** (L4).  
- **Tail trace sampling coverage**: ≥ **30%** (L3), ≥ **60%** (L4).  
- **Evidence coverage**: ≥ **90%** of incidents have evidence packs (L3–L4).

> Tune bands per stack/scale; use the same dataset across vendors.

---

## 🔁 Atlas alignment (👁️ Observability token → UOM level)

| Atlas token | UOM level |
|---|---:|
| **N/L** | **0** |
| **P/L** | **1** |
| **P/M** | **2** |
| **Y/M** | **3** |
| **Y/H** | **4** |

---

## 🔍 Comparison Template (vs. UOM)

| Platform | Ingest (0–4) | Normalize (0–4) | Storage/Index (0–4) | Visualization (0–4) | Alerting/SLO (0–4) | Topology (0–4) | Evidence/Handoff (0–4) | Gov/Cost/Rel (0–4) | **Overall UOM (0–4)** | IngestLag_P50_ms | IngestLag_P95_ms | QueryDash_P95_ms | QueryAdhoc_P95_ms | SLO_Coverage_% | Alert_Dedupe_Ratio | TailTraceSampling_% | Evidence_Export (Y/N) | CrossSignal (Y/N) | Retention_Metrics_d | Retention_Logs_d | Retention_Traces_d | CostPerGB_USD | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|---:|---:|---|
| **Your Stack** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## 📝 Conformance Checklist

- **Instrumentation:** OTel SDK/auto‑inst; K8s & infra collectors; HA + backpressure.  
- **Enrichment:** Consistent `service.*`, version, env, team tags; parsing rules; K8s resource attrs.  
- **Storage:** Per‑signal retention policy; sampling/tiering; index compaction; cardinality dashboards.  
- **Queries:** PromQL/LogQL/TraceQL; entity pages; cross‑signal hops; shareable permalinks.  
- **Alerting/SLO:** SLO burn‑rates; dedupe; maintenance windows; runbook links.  
- **Topology:** Service map & K8s topology; ownership; change awareness.  
- **Evidence:** One‑click export to Markdown/JSON; ticket/chat exporters.  
- **Gov/Cost/Rel:** RBAC, PII masking, quotas; ingest/query **SLOs**; cost/usage reports.

---

## 📦 Appendix — Example Evidence Pack (Markdown)

```md
### Incident Evidence Pack — API Latency
- **Panel (PromQL)**: https://grafana/…
- **Logs (Loki)**: https://loki/…
- **Trace (Tempo)**: https://tempo/…
- **Entity page**: https://observability/services/api-gateway
- **SLO burn**: 2.1× / 1h window
- **Topology snapshot**: attached PNG
```

---

## Ratings (UOM v2)

| Platform | **Overall UOM Level (0–4)** |
|---|---:|
| Atlassian – Rovo Dev | **1 — Single‑signal** |
| AWS – Strands SDK (Agent Development Framework) | **2 — Unified** |
| Cisco – Splunk AI Agents (Agentic Observability) | **4 — Governed/Optimized** |
| Databricks – “Agent Bricks” (Lakehouse AI Agents) | **2 — Unified** |
| Datadog – “Bits” AI Agents (SRE & DevOps) | **4 — Governed/Optimized** |
| Dataiku – AI Agents (DSS Platform) | **2 — Unified** |
| DuploCloud – AI CloudOps Help Desk | **3 — Contextual** |
| Dynatrace – Davis AI (Autonomous Observability) | **4 — Governed/Optimized** |
| Elastic – AI Assistant for Observability | **3 — Contextual** |
| GitHub – Copilot (Coding & DevOps Assistant) | **0 — None** |
| Google – Vertex AI Conversational Agent (Gen App Builder) | **1 — Single‑signal** |
| IBM – AskIAM (Identity Assistant) | **2 — Unified** |
| JFrog – “Fly” CI/CD Agent | **2 — Unified** |
| Solo.io – Kagent (Kubernetes Assistant) | **3 — Contextual** |

---

## Platform Notes (evidence‑mapped to the 8 phases)

*(Platform notes unchanged from your source; ensure they render as lists and paragraphs.)*

---

## Summary & Guidance

- **Leaders (Level 4):** Cisco/Splunk, Datadog, Dynatrace — meet evidence, cross-signal, and governance gates with mature anomaly/correlation and exportable incident evidence.  
- **Strong Context (Level 3):** Elastic, DuploCloud, Solo.io — solid cross-signal pivots and entity/topology context; add ingest/query SLOs and stronger auto-correlation to approach L4.  
- **Unified but Limited (Level 2):** AWS Strands, Databricks, Dataiku, IBM AskIAM, JFrog — can unify or analyze specific domains but miss cross-signal UX and/or evidence exports.  
- **Basic/None (≤1):** Atlassian Rovo, Google Vertex, GitHub Copilot — not observability platforms; treat them as adjunct assistants, not signal sources.

**Next steps for bake-off:** use a fixed dataset and attach **permalinks/exports** for all queries, cross-signal pivots, alert definitions, and evidence packs to validate the assigned levels against the UOM gates.
