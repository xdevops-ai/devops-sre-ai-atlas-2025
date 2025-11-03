---
layout: default
title: Rating Example (UOM v2)
parent: UOM Baseline (v2)
nav_order: 1
permalink: /capabilities/baselines/uom/rating-example/
last_updated: 2025-10-12T12:46:23Z
---

# 📊 UOM Rating Example (v2)

Use this page as a template to score a platform against **UOM v2**.  
**Gating recap:**  
- No shareable **evidence exports/permalinks** → **cap at 2**.  
- No **cross-signal drill-downs** (metrics↔logs/traces) → **cap at 2**.  
- No **RBAC/PII/cost guardrails with ingest/query SLOs** → **cap at 3**.

---

## Example — *Acme Observability*

### Scores (per phase)

| Ingest | Normalize | Storage/Index | Visualization | Alerting/SLO | Topology | Evidence/Handoff | Gov/Cost/Rel |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **3** | **3** | **3** | **3** | **3** | **3** | **3** | **2** |

**Gates:** `evidence_export=Y`, `cross_signal=Y`, `governance_slos=N` → **Overall UOM = 3 (Contextual)**.

### KPI snapshot

- **IngestLag P50/P95 (ms):** 450 / 1900  
- **Query P95 (dash/adhoc):** 2200 / 5800  
- **SLO Coverage:** 65% of services  
- **Alert Dedupe Ratio:** 36%  
- **Tail Trace Sampling:** 40%  
- **Retention (days):** metrics=180, logs=30, traces=14  
- **Cost per GB (USD):** 0.12

### Comparison row

| Platform | Ingest (0–4) | Normalize (0–4) | Storage/Index (0–4) | Visualization (0–4) | Alerting/SLO (0–4) | Topology (0–4) | Evidence/Handoff (0–4) | Gov/Cost/Rel (0–4) | **Overall UOM (0–4)** | IngestLag_P50_ms | IngestLag_P95_ms | QueryDash_P95_ms | QueryAdhoc_P95_ms | SLO_Coverage_% | Alert_Dedupe_Ratio | TailTraceSampling_% | Evidence_Export (Y/N) | CrossSignal (Y/N) | Retention_Metrics_d | Retention_Logs_d | Retention_Traces_d | CostPerGB_USD | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|---:|---:|---|
| **Acme Observability** | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | **3** | 450 | 1900 | 2200 | 5800 | 65 | 0.36 | 40 | Y | Y | 180 | 30 | 14 | 0.12 | Evidence bundles exported as Markdown + permalinks; no ingest/query SLOs yet. |

---

## Copy‑paste YAML (optional data record)

Save under `docs/_data/ratings/uom/acme_uom_rating_v2.yaml`:

```yaml
vendor: Acme Co.
product: Acme Observability
model: UOM v2
last_updated: 2025-10-12T12:46:23Z
gating:
  evidence_export: true
  cross_signal: true
  governance_slos: false
scores:
  ingest: 3
  normalize: 3
  storage_index: 3
  visualization: 3
  alerting_slo: 3
  topology: 3
  evidence_handoff: 3
  governance_cost_reliability: 2
overall_uom_level: 3
kpis:
  ingest_lag_p50_ms: 450
  ingest_lag_p95_ms: 1900
  query_dash_p95_ms: 2200
  query_adhoc_p95_ms: 5800
  slo_coverage_pct: 65
  alert_dedupe_ratio: 0.36
  tail_trace_sampling_pct: 40
retention_days:
  metrics: 180
  logs: 30
  traces: 14
cost:
  per_gb_usd: 0.12
evidence:
  exports: ["markdown", "png", "csv"]
  permalinks: true
  examples:
    - "grafana://dashboard/panels/latency"
    - "loki://query/error-rate"
    - "tempo://trace/abc123"
notes: >
  Governance/SLO gate prevents Level 4 until ingest/query SLO dashboards and cost guardrails are in place.
```
