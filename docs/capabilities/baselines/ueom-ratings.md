---
layout: default
title: Rating Example — UEOM (Acme Events Graph)
parent: UEOM Baseline (v2)
nav_order: 1
permalink: /capabilities/baselines/ueom/rating-example/
last_updated: 2025-11-03T00:00:00Z
---

# UEOM Rating Example — “Acme Events Graph”

A worked example showing how to score a platform against **UEOM v2** using real evidence.

---

## 🔮 Assessment summary
- **Overall UEOM level:** **3 — Governed graph**  
- **Gate checks:** SHACL **enforced**, deterministic **URI/identity** policy **present**, **named‑graph tenancy + RBAC** **present**, **SPARQL query pack + provenance** **present**.  
- **Why not Level 4?** No reasoning engine/inference configured and **no embeddings keyed by URIs** for RAG; cross‑domain query SLOs not yet met.

---

## ✅ Phase scores & evidence

| Phase | Score (0–4) | Evidence highlights |
|---|---:|---|
| **Modeling** | **3** | `acme.owl.ttl` with classes/properties/labels; alias & deprecation policy; CHANGELOG. |
| **Mapping & Normalization** | **3** | Deterministic source→URI rules (`uri_policy.md`); JSON‑LD envelopes; units/time normalized; replay job for backfill. |
| **Validation & Conformance** | **3** | SHACL strict/relaxed in ingest; violation report with counts by class; CI gate at 2% max violations. |
| **Materialization & Linking** | **3** | SPARQL Update with batch/idempotent inserts; link discovery for change↔incident; **named graphs** per tenant/env; PROV stamps. |
| **Retrieval / Reasoning / Governance** | **3** | Versioned **SPARQL query pack**; RBAC by named graph; governance dashboard (shape coverage, inserts/s, violations). No inference/embeddings yet. |

> **Overall = 3** (all gates for 1–3 satisfied; L4 gates not met).

---

## 📊 KPI snapshot

| Metric | Value |
|---|---:|
| **ShapeCoverage_%** | **88** |
| **InsertThroughput_triples_s** | **7500** |
| **QueryP95_ms** | **820** |
| **Dedupe_FP_%** | **0.6** |
| **Provenance_%** | **94** |
| **NamedGraphs_count** | **12** |
| **RAG_Coverage_%** | **0** |

---

## 📋 Comparison row (copy‑paste into the UEOM table)

```
| Acme Events Graph | 3 | 3 | 3 | 3 | 3 | **3** | 88 | 7500 | 820 | 0.6 | 94 | 12 | 0 | Query pack v1; no inference/embeddings yet |
```

---

## 🔗 Evidence links (placeholders)

- OWL/Turtle: `repo://ontology/acme.owl.ttl`  
- SHACL shapes: `repo://ontology/shapes/strict-and-relaxed.ttl`  
- Mapping specs & URI policy: `repo://ontology/mapping/uri_policy.md`  
- Validation report: `s3://evidence/ueom/validation-2025-10-28.json`  
- Insert logs: `s3://evidence/ueom/ingest-2025-10-28.log.gz`  
- SPARQL query pack: `repo://ontology/queries/`  
- Governance dashboard: `https://internal.acme/ontology/governance`

---

## ⏭️ What to add to reach **Level 4**
1) Enable **reasoning/rules** (e.g., SHACL‑AF/SWRL or store‑native inference) with regression tests.  
2) Build **URI‑keyed embeddings** and an **entity RAG index** with coverage ≥ 85%.  
3) Establish **cross‑domain query P95 ≤ 600 ms** SLO and meet it on the standard query set.  
4) Extend mapping coverage to ≥ 95% of required classes and publish an evolution workflow.
