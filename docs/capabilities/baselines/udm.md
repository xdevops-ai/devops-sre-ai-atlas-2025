# 🧭 Universal Diagnostic Model (UDM) — v2 (0–4 scale)

*A vendor-neutral baseline describing how intelligent Ops/Observability systems **detect, enrich, correlate, explain (RCA), and recommend/remediate** incidents — with verifiable evidence.*

**Last updated:** 2025-10-12T12:28:58Z

---

## What changed in v2

- **Maturity scale normalized to 0–4** (was 0–4/0–5 across sources). Clear **acceptance gates** per level.
- **Precise phase names**: Signal Detection · Context Enrichment · Event Correlation & Classification · Root Cause Analysis · Recommendation/Remediation.
- **Atlas alignment**: Token→numeric mapping for the Atlas **🔍 Diagnostics** capability.
- **Operational metrics**: TTFC/TTRC, Verified-RCA rate, false-positive rate added as non-functional targets.
- **Exports**: Scorecard CSV and machine-readable rubric JSON.

---

## ⚙️ Five Diagnostic Phases

| # | Phase | Definition | Typical Data | Expected Capability |
|---:|---|---|---|---|
| **1** | **Signal Detection** | Identify anomalies or deviations from expected behavior | Metrics (CPU/latency/errors), logs, traces, alerts | Thresholds, anomaly detectors, drift-aware baselines; capture detection reason & thresholds |
| **2** | **Context Enrichment** | Link signals with entities, ownership, deploy/change context | Service maps, k8s/CMDB, deploy metadata | Stable IDs, dependency graph, change/owner joins, SLO context |
| **3** | **Event Correlation & Classification** | Group related signals and classify the probable domain/cause family | Multi-signal events across time windows | Correlation windows, clustering/causal hints, change-aware grouping |
| **4** | **Root Cause Analysis (RCA)** | Produce a **testable hypothesis** explaining *why* with evidence | Enriched telemetry + historical baselines + change diffs | Structured hypothesis + verification plan; confidence; negative evidence considered |
| **5** | **Recommendation / Remediation** | Propose (or execute under guardrails) a mitigation with verification | Runbooks, IaC diffs, workflows | Risk-aware plan, preflight checks, approvals; rollback & post-verify steps |

---

## 🧩 UDM Maturity Scale (0–4)

| Level | Label | Acceptance (must satisfy this level **and** all lower levels) |
|---:|---|---|
| **0** | **None** | No diagnostics beyond raw alerts/logs; no context; no evidence export. |
| **1** | **Reactive** | L1 detection: manual/threshold alerts; minimal labeling; ad-hoc triage notes. |
| **2** | **Correlated** | L2 detection + **multi-signal correlation or rule-based classification**; entity/service mapping; links to evidence (queries/logs/traces). |
| **3** | **Intelligent** | L3 adds **structured RCA** with **verification steps** (counter-tests), confidence scoring, change awareness, and **explainable evidence** (permalinks/queries included). |
| **4** | **Autonomous** | L4 adds **causal reasoning/graphs**, **automated counter-tests**, early-finalize on high confidence, and **guardrailed remediation** (approvals/rollback), with tracked quality metrics (Verified-RCA rate, FP rate). |

> **Gating rule:** A product’s **UDM level** is the **highest level** whose acceptance gates (and all below) are met. Any missing gate caps the level.

---

*(Content continues as formatted in prior step...)*
