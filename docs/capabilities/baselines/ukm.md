---
layout: default
title: UKM Baseline (v2)
parent: Capability Framework
nav_order: 5
has_children: true
permalink: /capabilities/baselines/ukm/
last_updated: 2025-10-12T13:16:15Z
---


# 🧠 Universal Knowledge Model (UKM) — v2 (0–4 scale)
*A vendor‑neutral baseline describing how platforms **ingest, normalize, index, retrieve, and govern** organizational knowledge.*

**Last updated:** 2025-10-12T13:16:15Z

---

## What changed in v2
- **Maturity scale normalized to 0–4** with explicit acceptance gates per phase.
- **Typed corpora** clarified: `capability`, `knowledge`, `story`, `ontology`, `profile`.
- **Evidence discipline**: exportable **citations/provenance**, **schemas/shapes**, **retrieval traces**, and **visibility tests** are required for higher levels.
- **Gating rules** added so keyword‑only search or undocumented RAG can’t be scored like ontology‑linked, governed systems.
- **Quality KPIs** added (Precision@k, citation rate, freshness, latency, SHACL violations, governance pass rate).
- **Atlas alignment**: token→numeric mapping for the Atlas **UKM snapshot** components.

---

## ⚙️ The Five Knowledge Phases
| # | Phase | Definition | Typical Data | Expected Capability |
|---:|---|---|---|---|
| **1** | **Ingestion & Validation** | Bring knowledge into the system and ensure it conforms to schema | KB JSON, runbooks, retros, capability cards, profiles, ontology events | Source adapters, schema validation, dedupe, provenance capture |
| **2** | **Normalization & Enrichment** | Add structure and context | Owner/visibility, tags, entities (service/team/env), versions | Metadata normalization, ontology tagging, PII redaction, versioning |
| **3** | **Indexing & Linking** | Make it searchable and connected | Embeddings, scalar metadata, RDF triples, shapes | Vector index (Milvus‑class), metadata filters/expr, graph links (RDF/SHACL), shapes→vectors |
| **4** | **Retrieval & Composition** | Answer questions and assemble context | RAG queries, typed retrieval (capability/knowledge/story), profile hints | Similarity + filters + routing, snippet assembly, Mermaid diagrams, profile‑aware results |
| **5** | **Governance & Evolution** | Control access, explain results, and improve quality | Visibility scopes, citations, feedback, freshness | Enforced visibility, citations/provenance, feedback loops, recency windows, deprecation lifecycle |

---

## 🧩 UKM Maturity Scale (0–4)
| Level | Label | Acceptance (must satisfy all lower levels) |
|---:|---|---|
| **0** | **None** | Ad‑hoc docs/wikis; no embeddings or schema; no provenance. |
| **1** | **Indexed** | Keyword search across files/pages; basic metadata (owner or tags); no vector index; no graph. |
| **2** | **Semantic** | Vector index + metadata filters; basic provenance (source, owner, updated_at); recency windows; no graph requirements. |
| **3** | **Ontology‑linked** | Typed corpora + RDF/SHACL graph; schema‑validated ingest; **governed retrieval** (visibility enforcement); cross‑domain joins; diagram assembly supported. |
| **4** | **Contextual Intelligence** | Profile‑aware retrieval & story composition; citations on every answer; continuous freshness & feedback; explainable snippet assembly with diagrams; versioned ontology & query packs. |

> **Exportability gate:** If **citations/provenance** cannot be exported with retrieval results, **cap at Level 2 (Semantic)**.

> **Graph gate:** If there is **no RDF/SHACL graph with mappings** (or no typed retrieval across corpora), **cap at Level 2 (Semantic)**.

> **Governance gate:** If **visibility/tenant enforcement** cannot be proven with tests (no cross‑tenant bleed), **cap at Level 2 (Semantic)**.

> **Overall rule:** Overall **UKM level = highest level where all acceptance clauses for that level and below hold**.

---

## 🔎 Per‑phase expectations by level (condensed)

### 1) Ingestion & Validation
- **L0:** Manual uploads; no validation.  
- **L1:** Keyword ingestors; minimal metadata; no schema errors surfaced.  
- **L2:** Schema validation with actionable errors; dedupe; provenance recorded.  
- **L3:** Validated multi‑corpus ingest; SHACL validation for ontology items; DLQ/Bloom dedupe.  
- **L4:** Event‑driven re‑ingest; freshness SLOs; backfill/migrations with change logs.

### 2) Normalization & Enrichment
- **L0:** None.  
- **L1:** Owner or tag only.  
- **L2:** Owner/visibility/tags; entity hints (service/team/env); PII redaction.  
- **L3:** Ontology tagging; versions; alias policy; normalization of units/formats.  
- **L4:** Auto‑enrichment from telemetry/ontology; confidence scores.

### 3) Indexing & Linking
- **L0:** Flat files only.  
- **L1:** Keyword index only.  
- **L2:** Vector + metadata index; hybrid search (vector ∪ keyword).  
- **L3:** RDF graph; SHACL shapes; shapes→vectors; linkable nodes/edges; query library.  
- **L4:** RAG‑ready embeddings keyed by URIs; cross‑domain joins at SLO.

### 4) Retrieval & Composition
- **L0:** Manual browsing.  
- **L1:** Keyword only; no citations.  
- **L2:** Similarity + filters; snippet assembly; optional citations.  
- **L3:** **Typed retrieval** (capability/knowledge/story/profile/ontology), cite‑back; diagram (Mermaid) support.  
- **L4:** Profile‑aware retrieval (skills/ownership), scenario/story composition; answer plans with citations & diagrams.

### 5) Governance & Evolution
- **L0:** None.  
- **L1:** Best‑effort RBAC.  
- **L2:** Enforced visibility/tenant scopes; audit of queries.  
- **L3:** Provenance on every item; redaction; per‑tenant graphs; feedback loops.  
- **L4:** Quality dashboards; deprecation lifecycle; continuous evals; SLA/SLO for search.

---

## 🧠 Neutral Knowledge Event (JSON Example)

```json
{
  "knowledge_event": {
    "id": "2f8f6e9b-0b09-4c3e-8d0a-1209bb0a75f1",
    "timestamp": "2025-10-09T12:00:00Z",
    "phase": "ingest",
    "corpus": "capability",
    "item": {
      "key": "oncall_handoff_slack_v1",
      "title": "On-call Handoff via Slack",
      "text": "Standard handoff format and Slack workflow steps…",
      "entities": ["slack","incident","runbook"],
      "tags": ["oncall","handoff"]
    },
    "metadata": {
      "owner": "platform",
      "visibility": "team",
      "source": "repo://kb/capabilities/oncall.json",
      "revision": "a1b2c3"
    },
    "provenance": {
      "created_at": "2025-09-01T10:00:00Z",
      "updated_at": "2025-10-01T09:30:00Z"
    },
    "embedding_ref": "milvus://collections/devops_capabilities/ids/…",
    "graph_refs": ["graphdb://iac#Capability/oncall_handoff"],
    "governance": { "pii_redacted": true, "scopes": ["team"] }
  }
}
```

---

## ✅ Feature Requirements (FR) & Acceptance Criteria (AC)

**F1. Schema discipline & ingest logs** — Validates and rejects invalid rows with actionable errors.  
**AC:** 100% of ingestors produce structured error records with JSON pointers.

**F2. Normalization & enrichment** — Owner/visibility/tags; entity mapping; PII redaction.  
**AC:** All items carry owner, visibility and entity metadata; PII masked where applicable.

**F3. Indexing & linking** — Vector + metadata index; RDF/SHACL graph; shapes→vectors.  
**AC:** Items resolvable by URI; SHACL violations logged; embeddings retrievable by node URI.

**F4. Retrieval & composition** — Typed retrieval with routing; snippet assembly; diagrams.  
**AC:** Queries route to the correct corpus; results include citations; Mermaid render succeeds or returns diagnostics.

**F5. Governance & evolution** — Visibility enforced; citations/provenance included; freshness windows; feedback loop.  
**AC:** Cross‑tenant/visibility bleed tests pass; answers carry citations; freshness metrics available; feedback captured.

---

## 📈 Quality KPIs & Target Bands (guide)

- **Precision@5:** ≥ **0.60** (L3), ≥ **0.75** (L4).  
- **Citation_Rate% (answers with citations):** ≥ **95%** (L3), ≥ **99%** (L4).  
- **Search_Latency_P50/P95 (ms):** ≤ **800/1500** (L3), ≤ **500/900** (L4).  
- **Freshness_P95_Age_days (capability corpus):** ≤ **14** (L3), ≤ **7** (L4).  
- **Governance_Pass_Rate% (visibility tests):** ≥ **99.0%** (L3), ≥ **99.9%** (L4).  
- **SHACL_Violation_Rate per 1k inserts:** ≤ **5** (L3), ≤ **1** (L4).  
- **Index_Coverage% (required corpora present):** ≥ **60%** (L3, ≥3/5), ≥ **80%** (L4, ≥4/5).  
- **Broken_Link_Rate% (evidence/citations):** ≤ **1.0%** (L3), ≤ **0.2%** (L4).

> Use the **same query set** and capture retrieval logs + citations across vendors for fair bake‑offs.

---

## 🔁 Atlas alignment (UKM token → UKM level)

| Atlas token | UKM level |
|---|---:|
| **N/L** | **0** |
| **P/L** | **1** |
| **P/M** | **2** |
| **Y/M** | **3** |
| **Y/H** | **4** |

---

## 🔍 Comparison Template (vs. UKM)

| Platform | Ingest&Validate (0–4) | Normalize&Enrich (0–4) | Index&Link (0–4) | Retrieve&Compose (0–4) | Govern&Evolve (0–4) | **Overall UKM (0–4)** | Precision@5 | Citation_Rate_% | Search_P50_ms | Search_P95_ms | Freshness_P95_days | Governance_Pass_% | SHACL_Viol/1k | Index_Coverage_% | Broken_Link_% | Evidence Links |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **Your Stack** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Competitor A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Competitor B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

> Attach retrieval logs, citations, schema/shape files, and governance test scripts as evidence.

---

## 📝 Conformance Checklist

- **Schema‑validated ingest** with actionable errors; DLQ/Dedupe.  
- **Normalization** adds owner, visibility, entities, versions; PII masking applied.  
- **Vector + metadata index** and **RDF/SHACL** graph with shapes→vectors.  
- **Typed retrieval** (capability/knowledge/story/profile/ontology) with **citations** and diagram assembly.  
- **Governance & freshness** enforced; query audit; feedback loops; deprecation lifecycle.

---

## 📦 Appendix — Minimal Acceptance Examples

- **Schema rejection** — malformed `capability` JSON rejected; error returns JSON‑pointer to failing field.  
- **Typed routing** — `corpus=story` query returns only stories; score threshold applied.  
- **SHACL validation** — invalid resource violates a shape; violation logged and routed to DLQ.  
- **Mermaid rendering** — valid code produces PNG/SVG; errors return a diagnostic message.  
- **Governance filter** — team‑scoped query does not return org/private items; tests included.  
- **Precision@k** — for a standard query set, Precision@5 ≥ target with citations present.

---

## 🗂️ Field Canonicals (Knowledge)

- **phase** ∈ `{ingest, normalize, index, retrieve, govern}`  
- **corpus** ∈ `{capability, knowledge, story, ontology, profile}`  
- **visibility** ∈ `{team, org, private}`  
- **provenance**: `{source, owner, created_at, updated_at, revision}`  
- **links**: `graph_refs[]`, `embedding_ref`


---
