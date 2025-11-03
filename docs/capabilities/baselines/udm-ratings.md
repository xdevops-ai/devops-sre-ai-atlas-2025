---
layout: default
title: UDM Rating Example (v2)
parent: UDM Baseline (v2)
grand_parent: Capability Framework
nav_order: 1
permalink: /capabilities/baselines/udm/rating-example/
last_updated: 2025-10-12T12:28:58Z
---

# ✅ UDM Rating Example (v2)

This page shows a **concrete, vendor‑neutral example** of how to rate a platform against the **Universal Diagnostic Model (UDM) v2** and compute the **Overall UDM Level (0–4)**.

---

## How to use this
1. Review the **five UDM phases** and their level definitions in the [UDM Baseline (v2)]({{ '/capabilities/baselines/udm/' | relative_url }}).
2. For your platform, assign a **0–4 level per phase** based on evidence (queries, permalinks, grouped incidents, RCA plans).
3. Apply **gates** (e.g., missing evidence‑linked RCA or guardrailed remediation prevents Level 3–4).
4. Compute **Overall UDM Level** = round(nearest) of the average across phases **after** applying caps.
5. Save a machine‑readable record under `_data/ratings/udm/*.yaml` so pages can render tables/cards consistently.

> Tip: Use the YAML file in the **Download** section below as a template.

---

## Example: “AcmeOps Platform” — UDM v2 rating

**Overall UDM Level (0–4): `3 — Intelligent`**  
_Computed from per‑phase levels with no global cap triggered._

### Per‑phase scoring (with evidence notes)

| UDM Phase | Level (0–4) | Evidence you should attach (examples) | Notes |
|---|:---:|---|---|
| **1. Signal Detection** | **3** | Detector configs, anomaly screenshots; detection reason (rule/model) | Baselines per service; change‑aware noise reduction. |
| **2. Context Enrichment** | **3** | Incident page showing entity/owner, last deploy & SLO | Stable IDs + deploy/change join + SLO context. |
| **3. Event Correlation & Classification** | **3** | Grouped incident record; window & rationale | Multi‑signal clustering; duplicate suppression. |
| **4. Root Cause Analysis (RCA)** | **3** | Structured hypothesis with counter‑tests & confidence | Evidence permalinks; at least one counter‑test executed. |
| **5. Recommendation / Remediation** | **2** | Plan with preflight/rollback; approval screenshot | No fully automated close‑loop; guarded, human approval. |

**Average (unrounded)** = (3+3+3+3+2) / 5 = **2.80** → **rounded = 3**.

### Gates checked for this example
- **Evidence‑linked RCA present?** ✅ Yes (permalinks + counter‑test) → *no cap*.  
- **Guardrailed remediation?** ⚠️ Partial → Level 2 for phase 5; overall still 3.  
- **Causal graph/automated counter‑tests?** ❌ Not yet → prevents Level 4.

---

## JSON/YAML record (machine‑readable)

Use this structure under `_data/ratings/udm/` to drive badges/cards in pages.

```yaml
platform: "AcmeOps Platform"
version: "2025.10"
baseline: "UDM v2"
atlas_token_diagnostics: "Y/M"   # Optional: Atlas token if you mirror the table view
levels:
  detection: 3
  context_enrichment: 3
  event_correlation_classification: 3
  rca: 3
  recommendation_remediation: 2
gates:
  evidence_linked_rca: true
  guardrailed_remediation: "partial"  # true|partial|false
  causal_graph: false
kpis:
  ttfc_p50_s: 45
  ttfc_p95_s: 160
  ttrc_p50_min: 9
  ttrc_p95_min: 28
  verified_rca_rate: 0.82
  false_positive_rate: 0.08
composite:
  average_unrounded: 2.8
  rounded: 3
  cap_applied: null
  overall: 3
evidence_links:
  detector_config: "https://example.com/monitors/latency-p95"
  grouped_incident: "https://example.com/incidents/INC-4431"
  rca_permalink: "https://example.com/rca/INC-4431#hypothesis-1"
  remediation_plan: "https://example.com/runbooks/redeploy-previous"
notes: |
  Automate counter‑tests and enable closed‑loop remediation with approvals+rollback to qualify for Level 4.
```

---

## Download

- **Example page (this file):** You can copy it to `docs/capabilities/baselines/udm/rating-example.md`.  
- **Example data record:** Place the YAML under `docs/_data/ratings/udm/acme_udm_rating_v2.yaml`.

**Files:**  
- [Download the rating example page](sandbox:/mnt/data/udm_rating_example.md)  
- [Download the YAML rating record](sandbox:/mnt/data/acme_udm_rating_v2.yaml)

---

## Update steps (copy/paste)

1. Drop the YAML into `_data/ratings/udm/` and change the values to your platform.  
2. Copy this Markdown into `docs/capabilities/baselines/udm/rating-example.md`.  
3. Link to the baseline: `[UDM Baseline (v2)]({{ '/capabilities/baselines/udm/' | relative_url }})`.  
4. Commit & push; your sidebar will show **UDM Rating Example (v2)** under UDM.  
5. For each vendor page, include a small badge/table that reads from `_data/ratings/udm/*.yaml`.
