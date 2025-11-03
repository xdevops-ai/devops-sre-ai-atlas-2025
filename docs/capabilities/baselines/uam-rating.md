---
layout: default
title: UAM Rating Example (v2)
parent: UAM Baseline (v2)
grand_parent: Capability Framework
nav_order: 1
permalink: /capabilities/baselines/uam/rating-example/
last_updated: 2025-10-12T00:00:00Z
---

# ✅ UAM Rating Example (v2)

This page shows a **concrete, vendor‑neutral example** of how to rate a platform against the **Universal Activity Model (UAM) v2** and compute the **Overall Activity Maturity (0–4)**.

---

## How to use this
1. Review the **seven UAM phases** and their level definitions in the [UAM Baseline (v2)]({{ '/capabilities/baselines/uam/' | relative_url }}).
2. For your platform, assign a **0–4 level per phase** based on evidence (screenshots, exports, policies, logs).
3. Apply **gates** (if missing governed retrieval or exportable evidence packs, cap at ≤2; see baseline notes).
4. Compute **Overall Activity Maturity** = round(nearest) of the average across phases **after** applying any caps.
5. Save a machine‑readable record under `_data/ratings/uam/*.yaml` so pages can render tables/cards consistently.

> Tip: Use the YAML file in the **Download** section below as a template.

---

## Example: “AcmeOps Platform” — UAM v2 rating

**Overall Activity Maturity (0–4): `3 — Governed`**  
_Computed from per‑phase levels with no gating caps triggered._

### Per‑phase scoring (with evidence notes)

| UAM Phase | Level (0–4) | Evidence you should attach (examples) | Notes |
|---|:---:|---|---|
| **1. Capture & Sessionization** | **4** | Transcript export showing durable `base_id`, monotonic timestamps | Sessions persist across channels (chat + tool); correct `actor/channel/doc_type`. |
| **2. Evidence Policy & Verification** | **3** | Allow‑list config (domains/params), verify logs, TTL‑dedupe metrics | Implements allow‑lists + hashing; TTL dedupe partial (12h) → not full 4. |
| **3. Sanitization & Redaction** | **3** | Redaction test logs; commit/path normalization examples | Secrets/PII masked; path + commit normalization in place. |
| **4. Enrichment & Linking** | **3** | Hop graph export; manifests of links (commits/PRs/paths/tickets) | Hops & blast‑radius narrative generated for incidents. |
| **5. Indexing & Search** | **3** | Vector + metadata search traces; rerank proof | Combined search + rerank improves textual match quality. |
| **6. Replay & Summarization** | **4** | Replay Markdown + TL;DR with citations to **verified** evidence | Role‑labeled, noise‑pruned replay; TL;DR cites verified artifacts. |
| **7. Governance, Export & Operability** | **3** | RBAC/tenancy tests; Markdown/JSON exports; health/metrics dashboard | Governed retrieval enforced; exports present; SLOs tracked. |

**Average (unrounded)** = (4+3+3+3+3+4+3) / 7 = **3.29** → **rounded = 3**.

### Gates checked for this example
- **Exportable evidence packs?** ✅ Present → *no cap*  
- **Governed retrieval (tenant/user/visibility)?** ✅ Present → *no cap*  
- **Verification & dedupe discipline?** ⚠️ Partial → *kept level 3 for F2; still no global cap*

---

## JSON/YAML record (machine‑readable)

Use this structure under `_data/ratings/uam/` to drive badges/cards in pages.

```yaml
platform: "AcmeOps Platform"
version: "2025.10"
baseline: "UAM v2"
atlas_token_activities: "Y/M"   # Optional: if you also track Atlas token view
levels:
  capture_sessionization: 4
  evidence_policy_verification: 3
  sanitization_redaction: 3
  enrichment_linking: 3
  index_search: 3
  replay_summarization: 4
  governance_export_operability: 3
gates:
  evidence_packs_exportable: true
  governed_retrieval: true
  verification_dedupe: "partial"
composite:
  average_unrounded: 3.2857
  rounded: 3
  cap_applied: null
  overall: 3
evidence_links:
  transcript_export: "https://example.com/permalink/timeline/123"
  evidence_pack: "s3://acme-evidence/packs/2025-10-10/evidence.json"
  governance_tests: "https://example.com/run/ci/governance-tests-#9876"
notes: |
  TTL‑dedupe runs at 12h; move to 72h across sources to qualify for Level 4 on F2.
```

---

## Download

- **Example page (this file):** You can copy it to `docs/capabilities/baselines/uam/rating-example.md`.  
- **Example data record:** Place the YAML under `docs/_data/ratings/uam/acme_uam_rating_v2.yaml`.

**Files:**  
- [Download the rating example page](sandbox:/mnt/data/uam_rating_example.md)  
- [Download the YAML rating record](sandbox:/mnt/data/acme_uam_rating_v2.yaml)

---

## Update steps (copy/paste)

1. Drop the YAML into `_data/ratings/uam/` and change the values to your platform.  
2. Copy this Markdown into `docs/capabilities/baselines/uam/rating-example.md`.  
3. Link to the baseline: `[UAM Baseline (v2)]({{ '/capabilities/baselines/uam/' | relative_url }})`.  
4. Commit & push; your sidebar will show **UAM Rating Example (v2)** under UAM.  
5. For each vendor page, include a small badge or table that reads from `_data/ratings/uam/*.yaml`.
