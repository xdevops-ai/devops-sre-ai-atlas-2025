---
layout: default
title: UEOM Baseline (v2)
parent: Capability Framework
nav_order: 9
has_children: true
permalink: /capabilities/baselines/ueom/
last_updated: 2025-10-12T12:56:12Z
---

# 🧠 Universal Event Ontology Model (UEOM) — v2 (0–4 scale)
*A vendor‑neutral baseline describing how platforms **model, validate, materialize, retrieve, and govern** event & topology knowledge as a graph.*

**Last updated:** 2025-10-12T12:56:12Z

---

## What changed in v2
- Normalized maturity scale to **0–4** with clear **acceptance gates** per phase.
- **Evidence discipline**: if a vendor cannot provide **OWL/Turtle**, **mapping specs/code**, and **SHACL validation artifacts**, scoring is capped (see gates).
- Added **quality KPIs** (shape coverage, insert throughput, query latency, dedupe accuracy, provenance completeness, named‑graph tenancy) for fair bake‑offs.
- **Atlas alignment**: token→numeric mapping for the Atlas **🧠 Event Ontology** capability.

---

## ⚙️ Five Ontology Phases  

| # | Phase | Definition | Typical Evidence |
|:--:|------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **1** | **Concept & Modeling** | Define classes, properties, and identifiers with a consistent naming policy. | OWL/RDF Turtle, prefixes, examples, change logs |
| **2** | **Mapping & Normalization** | Deterministically map raw events or resources to ontology instances. | Source→URI rules, identity/dedupe keys, unit normalization, JSON-LD envelopes |
| **3** | **Validation & Conformance** | Enforce shapes and constraints during ingest. | SHACL shapes (strict/relaxed), violation reports, coverage metrics |
| **4** | **Materialization & Linking** | Insert and link triples in a graph store with resilience. | SPARQL updates, batch/idempotent inserts, link discovery, provenance stamps |
| **5** | **Retrieval, Reasoning & Governance** | Query, reason or derive, embed for RAG; govern evolution and access. | SPARQL library, reasoning/rules, embeddings keyed by URIs, versioning, named graphs & RBAC |

---

## 🧩 UEOM Maturity Scale (0–4)  

| Level | Label | Acceptance (must satisfy all lower levels) |
|:--:|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **0** | **None** | No ontology deliverables; ad-hoc documents only. |
| **1** | **Schema-only** | Versioned OWL/Turtle exists with labels and examples; **no enforced mapping or validation in pipeline**. |
| **2** | **Validated graph** | Deterministic **mapping** runs in ingest; **SHACL** validates instances; violation reports and coverage % exported. |
| **3** | **Governed graph** | **Named graphs** per tenant/env; **provenance** (PROV) on inserts; **versioning** and deprecation policy; **RBAC** on the data plane; query pack published. |
| **4** | **Semantic/Reasoned** | Reasoning/rules or inference; **cross-domain joins** with latency SLOs; **embeddings** bound to URIs (RAG-ready); governance metrics and evolution workflows. |
> **Evidence gates (caps):**
> - **No shapes (SHACL)** → cap at **L1** even if mapping exists.
> - **No deterministic identity/URI strategy** → cap at **L2**.
> - **No named‑graph tenancy/RBAC** → cap at **L2**.
> - **No shareable query pack (SPARQL) or provenance** → cap at **L3**.

> **Overall rule:** UEOM level = **highest level where all acceptance clauses for that level and below hold**.

---

## 🔎 Per‑phase expectations by level (condensed)

### 1) Concept & Modeling
- **L0:** None.  
- **L1:** OWL/Turtle with classes, properties, `rdfs:label`, alias policy; version tag & change log.  
- **L2:** Modeling referenced by mapping specs; identifiers policy for entities/events.  
- **L3:** Deprecation policy; compatibility notes; migration guidance.  
- **L4:** Cross‑domain vocabulary alignment (e.g., OTel/CIM/CSDM); reasoning targets documented.

### 2) Mapping & Normalization
- **L0:** None.  
- **L1:** Narrative mapping doc only.  
- **L2:** Deterministic rules → URIs; JSON‑LD envelopes; unit/time normalization; id/dedupe keys.  
- **L3:** Mapping coverage metrics (% event types, % fields); backfill/replay jobs; schema drift detectors.  
- **L4:** Multi‑source federation; conflict resolution; incremental materialization strategies.

### 3) Validation & Conformance
- **L0:** None.  
- **L1:** Shapes drafted but not enforced.  
- **L2:** SHACL (strict/relaxed) enforced in pipeline; violations exported with counts & examples.  
- **L3:** Coverage KPIs by class/property; conformance SLOs; test fixtures & CI checks.  
- **L4:** Rule‑based/derived assertions validated; regression/upgrade suites.

### 4) Materialization & Linking
- **L0:** Manual inserts.  
- **L1:** Unbatched scripts.  
- **L2:** SPARQL Update with idempotency; batch/retry; link discovery (e.g., change→incident).  
- **L3:** Named graphs per tenant/env; provenance (`prov:wasDerivedFrom`, `prov:wasGeneratedBy`); throughput SLOs.  
- **L4:** Streaming & CDC pipelines; backpressure metrics; historical snapshots/time‑travel graphs.

### 5) Retrieval, Reasoning & Governance
- **L0:** Ad‑hoc selects only.  
- **L1:** A few hand‑written queries.  
- **L2:** Published **query pack**; parameterized SPARQL; pagination; perf hints.  
- **L3:** RBAC by named graph; versioned endpoints; governance dashboards (shape coverage, inserts/s, violations).  
- **L4:** Reasoning or rule engine; **RAG embeddings** keyed by URIs; cross‑domain joins with P95 latency SLO; lineage/explainability UI.

---

## 🧠 Neutral Ontology Event (examples)

**A) Turtle (TTL) instance**
```turtle
@prefix xdev: <http://xdevops.ai/iac-ontology#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

<urn:svc:api-gateway>
  a xdev:Service ;
  rdfs:label "API Gateway" ;
  xdev:owns <urn:team:platform> ;
  xdev:dependsOn <urn:cloud:subnet:prod-east-1> .

<urn:inc:INC-4431>
  a xdev:Incident ;
  xdev:affects <urn:svc:api-gateway> ;
  xdev:startedAt "2025-10-11T12:00:00Z"^^xsd:dateTime ;
  prov:wasGeneratedBy <urn:event:alert:abcdef> .
```

**B) JSON‑LD envelope (ingest → normalize)**
```json
{
  "@context": {
    "xdev": "http://xdevops.ai/iac-ontology#",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "urn:inc:INC-4431",
  "@type": "xdev:Incident",
  "xdev:affects": "urn:svc:api-gateway",
  "xdev:startedAt": "2025-10-11T12:00:00Z",
  "prov:wasGeneratedBy": "urn:event:alert:abcdef"
}
```

---

## ✅ Feature Requirements (FR) & Acceptance Criteria (AC)

**F1. Modeling** — Versioned OWL/Turtle with naming & alias policy.  
**AC:** Published file with prefix table, class/property definitions, labels, examples, and CHANGELOG.

**F2. Mapping** — Deterministic source→URI rules; JSON‑LD outputs; unit/time normalization.  
**AC:** For a sample source set, mapping yields stable URIs; duplicates deduped by keys; outputs validate against schema.

**F3. Validation** — SHACL (strict/relaxed) in pipeline.  
**AC:** Violations reported with paths & counts; coverage % per class; CI fails on threshold breach.

**F4. Materialization** — SPARQL batch/idempotent inserts; link discovery; provenance.  
**AC:** Insert logs show retries/backoff; provenance fields present; named graphs created per tenant/env.

**F5. Retrieval/Reasoning/Governance** — Query pack; RBAC; reasoning/rules; embeddings for RAG.  
**AC:** Query pack documented; RBAC enforced; cross‑domain query P95 within SLO; embeddings index keyed by URIs exists.

---

## 📈 Quality KPIs & Target Bands

- **Shape coverage** (required classes with shapes): ≥ **80%** (L3), ≥ **95%** (L4).  
- **Insert throughput**: ≥ **5k triples/s** sustained (L3), ≥ **20k triples/s** (L4) *or env‑appropriate*.  
- **Query latency P95 (cross‑domain)**: ≤ **1200 ms** (L3), ≤ **600 ms** (L4).  
- **Dedupe FP rate**: ≤ **1%** (L3), ≤ **0.2%** (L4).  
- **Provenance completeness** (inserts with PROV): ≥ **90%** (L3), ≥ **99%** (L4).  
- **Tenancy isolation** (named‑graph policy tests): 100% pass for L3–L4.  
- **RAG coverage** (nodes/edges embedded): ≥ **60%** (L3), ≥ **85%** (L4).

> Use the **same dataset & query pack** across vendors to compare fairly.

---

## 🔁 Atlas alignment (🧠 Event Ontology token → UEOM level)

| Atlas token | UEOM level |
|---|---:|
| **N/L** | **0** |
| **P/L** | **1** |
| **P/M** | **2** |
| **Y/M** | **3** |
| **Y/H** | **4** |

---

## 🔍 Comparison Template (vs. UEOM)

| Platform | Modeling (0–4) | Mapping (0–4) | Validation (0–4) | Materialization (0–4) | Retrieval/Reasoning/Gov. (0–4) | **Overall UEOM (0–4)** | ShapeCoverage_% | InsertThroughput_triples_s | QueryP95_ms | Dedupe_FP_% | Provenance_% | NamedGraphs_count | RAG_Coverage_% | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **Your Stack** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Competitor A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Competitor B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

> Attach artifacts for every ✓: OWL/Turtle, shapes, mapping specs/code, violation reports, insert logs, SPARQL queries, governance screenshots.

---

## 📝 Conformance Checklist

- Versioned **OWL/Turtle** with labels, alias policy, and CHANGELOG.  
- Deterministic **identity/URI** strategy; JSON‑LD envelopes; unit/time normalization; dedupe keys.  
- **SHACL** strict/relaxed validation in pipeline; coverage metrics & CI gates.  
- **SPARQL** batch/idempotent inserts; **named graphs** per tenant/env; **provenance** stamps.  
- **Query pack** (parameterized SPARQL) with examples; **RBAC** & tenancy isolation tests.  
- **Reasoning/rules** or inference configured; **embeddings** index bound to URIs for RAG; cross‑domain SLOs.

---

## 📦 Appendix — Example SPARQL

```sparql
# Change→Incident candidates within ±2h for affected service
PREFIX xdev: <http://xdevops.ai/iac-ontology#>
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?change ?when
WHERE {
  GRAPH ?g {
    ?inc a xdev:Incident ;
         xdev:affects <urn:svc:api-gateway> ;
         xdev:startedAt ?t .
    ?change a xdev:Change ;
            xdev:affects <urn:svc:api-gateway> ;
            xdev:at ?when .
    FILTER ( ABS(?when - ?t) < "PT2H"^^xsd:duration )
  }
}
ORDER BY ?when
```

---

# ✅ Ratings (UEOM v2) — Platforms

> **Note:** Scores reflect publicly evidenced capabilities against **UEOM gates**. Where OWL/Turtle, **SHACL**, **named‑graph tenancy**, or **SPARQL query packs** are missing, levels are **capped** per gates. Use the **Platform Notes** to see what evidence would lift a cap.

| Platform | Modeling | Mapping | Validation | Materialization | Retrieval/Gov. | **Overall UEOM** | Gate Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| **Atlassian – Rovo Dev** | 1 | 1 | 0 | 1 | 1 | **1 — Schema‑only** | No OWL/SHACL; internal graph only; no SPARQL pack (cap L1). |
| **AWS – Strands SDK** | 0 | 0 | 0 | 0 | 0 | **0 — None** | Framework; ontology optional; no native graph/SHACL. |
| **Cisco – Splunk AI Agents (AgenticOps)** | 2 | 2 | 1 | 2 | 2 | **1 — Schema‑only (cap)** | CIM schema & data models; no SHACL → cap L1. |
| **Databricks – Agent Bricks** | 1 | 1 | 0 | 1 | 1 | **1 — Schema‑only** | Tables/lineage not RDF; no SHACL/SPARQL pack. |
| **Datadog – Bits AI** | 1 | 1 | 0 | 1 | 1 | **1 — Schema‑only** | Tags/service map; no OWL/SHACL; no SPARQL. |
| **Dataiku – AI Agents** | 2 | 2 | 1 | 2 | 2 | **1 — Schema‑only (cap)** | Strong governance; lacks SHACL/named‑graph RDF → cap L1. |
| **DuploCloud – AI Help Desk** | 1 | 1 | 0 | 1 | 1 | **1 — Schema‑only** | Config graph; no OWL/SHACL artifacts. |
| **Dynatrace – Davis AI** | 2 | 2 | 1 | 2 | 2 | **1 — Schema‑only (cap)** | Smartscape topology; no SHACL/SPARQL pack → cap L1. |
| **Elastic – AI Assistant for Observability** | 1 | 1 | 0 | 1 | 1 | **1 — Schema‑only** | ECS schema; not RDF/SHACL. |
| **GitHub – Copilot** | 0 | 0 | 0 | 0 | 0 | **0 — None** | No ontology features. |
| **Google – Vertex AI Agent Builder** | 1 | 1 | 0 | 0 | 1 | **1 — Schema‑only** | Intents/entities; no RDF/SHACL/SPARQL. |
| **IBM – AskIAM** | 2 | 2 | 1 | 2 | 2 | **1 — Schema‑only (cap)** | Identity graph & governance; no SHACL/OWL evidence. |
| **JFrog – Project “Fly”** | 0 | 0 | 0 | 0 | 0 | **0 — None** | Pipeline‑focused; no ontology deliverables. |
| **Solo.io – Kagent** | 1 | 1 | 0 | 1 | 1 | **1 — Schema‑only** | K8s object graph; no RDF/SHACL. |

---

## 🗒️ Platform Notes (phase‑by‑phase)

### Atlassian – Rovo Dev — **UEOM 1 (Schema‑only)**
- **Modeling:** Uses Atlassian Teamwork Graph concepts (issues, PRs, pages) but no **OWL/Turtle** export.  
- **Mapping & Normalization:** Relies on built‑in IDs (Jira keys, PR numbers); no published **JSON‑LD URI policy**.  
- **Validation & Conformance:** No **SHACL** enforcement evidence; validation limited to product schemas.  
- **Materialization & Linking:** Internal graph only; no SPARQL updates; linking via native relationships.  
- **Retrieval/Reasoning/Governance:** Search & link traversal; no **query pack** (SPARQL); governance via Atlassian RBAC.  
- **To reach L2/L3:** Publish OWL/Turtle; add SHACL shapes; expose SPARQL endpoint with named‑graph tenancy and query pack.

### AWS – Strands SDK — **UEOM 0 (None)**
- **Modeling:** No default ontology; developers may bring one.  
- **Mapping/Validation/Materialization:** BYO; SDK offers tool hooks but not RDF/SHACL pipelines.  
- **Retrieval/Governance:** No graph store; no RBAC at ontology layer (IAM applies to tools).  
- **Upgrade path:** Provide sample OWL/SHACL starter kit and Neptune/TDB loader with SPARQL queries.

### Cisco – Splunk AI Agents (AgenticOps) — **UEOM 1 (cap by SHACL gate)**
- **Modeling:** Splunk **CIM** & knowledge objects act as schemas (not OWL).  
- **Mapping:** Data model acceleration & field aliases (not JSON‑LD URIs).  
- **Validation:** CIM conformity checks exist but not **SHACL**; → **cap L1**.  
- **Materialization:** Splunk indexes, not triple store; no SPARQL; linking via CIM/ITSI episodes.  
- **Retrieval/Gov.:** SPL queries; RBAC strong at index level; no named‑graph tenancy.  
- **Next steps:** Export CIM as OWL; SHACL shapes; SPARQL view over CIM with provenance.

### Databricks – Agent Bricks — **UEOM 1 (Schema‑only)**
- **Modeling:** Unity Catalog schemas/lineage; no RDF/OWL.  
- **Mapping:** Delta/SQL transformations; no URI/JSON‑LD guarantees.  
- **Validation:** Constraints/expectations but no **SHACL**.  
- **Materialization:** Tables not triples; no SPARQL.  
- **Retrieval/Gov.:** SQL + vector search; strong governance at data plane; not graph‑native.  
- **Path to L3:** Provide RDF/SHACL exports + SPARQL views; named‑graph tenancy via per‑workspace graphs.

### Datadog – Bits AI — **UEOM 1 (Schema‑only)**
- **Modeling:** Tag schema and service/entity taxonomy (non‑RDF).  
- **Mapping:** Tags unify signals; no JSON‑LD URIs.  
- **Validation:** Parser rules; no **SHACL**.  
- **Materialization:** Proprietary stores; no SPARQL.  
- **Retrieval/Gov.:** UI & API filters; RBAC strong; no graph query pack.  
- **Lift:** Publish ontology (OWL), shapes, and SPARQL library over entity graph.

### Dataiku – AI Agents — **UEOM 1 (cap)**
- **Modeling:** Project/asset registry; potential RDF export via plugins not standard.  
- **Mapping:** Recipes for normalization; URI policy optional.  
- **Validation:** Quality/guardrails exist; not **SHACL**; → cap L1.  
- **Materialization:** Tables/lineage; optional graph connectors.  
- **Retrieval/Gov.:** Strong governance; not graph‑native querying.  
- **Lift:** Provide first‑class RDF/SHACL pipeline and SPARQL pack.

### DuploCloud – AI Help Desk — **UEOM 1**
- **Modeling:** Internal config model; no OWL.  
- **Mapping/Validation:** Deterministic but proprietary; no SHACL.  
- **Materialization:** No triple store; links via resource IDs.  
- **Retrieval/Gov.:** Ticketed retrieval; RBAC enforced; no SPARQL.

### Dynatrace – Davis AI — **UEOM 1 (cap)**
- **Modeling:** Smartscape entity model; not OWL.  
- **Mapping:** Deterministic entity IDs; not JSON‑LD URIs.  
- **Validation:** Platform constraints; not **SHACL**.  
- **Materialization:** Proprietary graph; no SPARQL endpoint.  
- **Retrieval/Gov.:** DQL & UI; strong governance; no named‑graph tenancy.  
- **Lift:** Export OWL/TTL for Smartscape; SHACL; SPARQL with provenance (PROV).

### Elastic – AI Assistant for Observability — **UEOM 1**
- **Modeling:** ECS field schema; not RDF.  
- **Mapping:** Ingest pipelines normalize fields; no URI policy.  
- **Validation:** Pipelines & index templates; no **SHACL**.  
- **Materialization:** Elasticsearch indices; no triples/SPARQL.  
- **Retrieval/Gov.:** DSL queries; RBAC; no graph governance layer.

### GitHub – Copilot — **UEOM 0 (None)**
- No ontology components; focus is code completions.

### Google – Vertex AI Agent Builder — **UEOM 1**
- **Modeling:** Intents/entities for dialog; not OWL.  
- **Mapping/Validation:** None beyond intent schemas; no SHACL.  
- **Materialization:** No triple store.  
- **Retrieval/Gov.:** KB retrieval only; no SPARQL or named graphs.

### IBM – AskIAM — **UEOM 1 (cap)**
- **Modeling:** Identity/role schemas; possible graph under the hood; no public OWL.  
- **Mapping:** Deterministic IDs (users, roles); no JSON‑LD URIs.  
- **Validation:** Strong policy checks; no SHACL; → cap L1.  
- **Materialization:** Directory/relational/graph mix; no SPARQL.  
- **Retrieval/Gov.:** Rich RBAC; not RDF‑native retrieval.  
- **Lift:** Publish ontology, shapes, and SPARQL pack across identity graph.

### JFrog – Project “Fly” — **UEOM 0 (None)**
- Pipeline helper; no ontology deliverables or graph APIs.

### Solo.io – Kagent — **UEOM 1**
- **Modeling:** Kubernetes object schema; not OWL.  
- **Mapping:** OwnerRefs/labels as links; no URI policy.  
- **Validation:** K8s admission/CRD schemas; no **SHACL**.  
- **Materialization:** API server & logs; no triple store.  
- **Retrieval/Gov.:** kubectl/Prom/Loki queries; no SPARQL.

---

## 📌 Summary & Guidance
- **Reality check:** Most platforms evaluated **do not expose RDF/OWL, SHACL, SPARQL, or named‑graph tenancy**, so they legitimately score **L0–L1** under **UEOM v2** gates. Many *do* maintain rich proprietary graphs (topology, identity, CMDB) — but **without ontology artifacts they cannot pass the gates**.
- **Levers to reach L2–L3 quickly:**
  1) Publish a **minimal OWL/Turtle** for your domain entities + **URI/identity policy**.  
  2) Enforce **SHACL** during ingest (strict/relaxed); export **violation reports**.  
  3) Stand up a **SPARQL endpoint** (or views) with a **query pack** and **PROV** provenance.  
  4) Add **named‑graph tenancy** (per tenant/env) and wire RBAC to graph endpoints.
- **L4 roadmap:** Add **reasoning/rules**, **embedding index keyed by URIs** for RAG, and **cross‑domain latency SLOs**.
