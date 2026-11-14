---
layout: default
title: UKM — Ratings & Notes (Examples)
parent: UKM Baseline (v2)
grand_parent: Capability Framework
nav_order: 10
permalink: /capabilities/baselines/ukm/ratings/
---

> Historical assessment: scores below were not revalidated in the November 2026 review. See the [current evidence matrix]({{ "/capabilities/" | relative_url }}).


> This page is **illustrative** and may reference vendors for comparison. The baseline itself remains **vendor‑neutral**.


## 📊 Ratings — Current Platforms (UKM v2)

| Platform | **Overall UKM (0–4)** | Gating Notes |
| --- | --- | --- |
| **Salesforce – Agentforce (OpsAI)** | **4** | Typed corpora in Data Cloud; governed retrieval with citations; knowledge graph linking; profile‑aware surfacing. |
| **ServiceNow – AI Agent Orchestrator** | **4** | CSDM/Service Graph + KB; governed retrieval; citations; versioned ontology & query packs. |
| **Databricks – Agent “Bricks”** | **4** | Lakehouse tables + vector functions; lineage graph; governed RAG; profile/context aware. |
| **Dataiku – AI Agents** | **4** | Schema‑validated ingest; knowledge bank + vector; lineage/registry; governed retrieval with feedback. |
| **IBM – AskIAM** | **3** | Typed corpora (policies, roles, access); identity graph; governed retrieval; limited diagram/story composition. |
| **Opsera – Hummingbird** | **3** | Unified DevOps insights model; hybrid index + traceability graph; governed retrieval; citations on summaries. |
| **AWS – Strands SDK** | **2** | BYO storage/index; vector search optional; provenance via tool traces; no native graph/governance → **cap 2**. |
| **Google – Conversational Agents** | **1** | KB/FAQ index; minimal provenance; no vector/graph in base product → **L1**. |
| **GitHub – Copilot** | **1** | Ephemeral repo context; no persistent KB or graph; no citations → **L1**. |
| **Termius – Gloria** | **1** | Live host responses only; no ingest/index; no governance beyond auth → **L1**. |

> **Caps applied** per gates: lack of exportable citations, RDF/SHACL (or typed cross‑corpus retrieval), or enforceable visibility ⇒ **max L2**.

---

## 🧾 Platform Notes — Evidence‑Aligned (per UKM phase)

### Salesforce – Agentforce (OpsAI) — **UKM 4**
- **Ingestion & Validation:** Connectors into Data Cloud ingest KB, tickets, docs with schema validation; provenance captured (source, owner, revision).  
- **Normalization & Enrichment:** Topics ontology and entity tagging (service/team); PII redaction and version metadata; visibility by account/role.  
- **Indexing & Linking:** Hybrid keyword+vector index; links to CMDB/graph entities; shapes (schema) drive embeddings; cross‑record linking of cases/incidents/runbooks.  
- **Retrieval & Composition:** Typed retrieval (capability/knowledge/story); RAG with citations/snippets; composes “action plans” and Mermaid‑style diagrams for processes.  
- **Governance & Evolution:** Policy‑enforced visibility; per‑record provenance in answers; freshness monitoring; feedback loops refine results.

### ServiceNow – AI Agent Orchestrator — **UKM 4**
- **Ingestion & Validation:** Ingests KB articles, incidents, changes; validates against CSDM; dedupe via KB workflows; provenance/version retained.  
- **Normalization & Enrichment:** CSDM/Service Graph adds owner, service, env; PII masking; alias/version policy for KB.  
- **Indexing & Linking:** KB + semantic index; deep linking into CMDB/graph; query library mapped to service context.  
- **Retrieval & Composition:** Typed retrieval across KB/incidents/runbooks; citations on answers; diagram assembly for service runbooks.  
- **Governance & Evolution:** Strict RBAC by assignment groups/tenants; audit trails; feedback & recency windows; managed deprecation lifecycle.

### Databricks – Agent “Bricks” — **UKM 4**
- **Ingestion & Validation:** Structured ingest into Lakehouse tables; MLflow/Delta lineage; schema checks and dedupe.  
- **Normalization & Enrichment:** Unity Catalog entities, ownership, tags; PII policies; versioned docs and profiles.  
- **Indexing & Linking:** Vector functions + metadata in Delta; lineage graph links datasets↔models↔agents; shapes→vectors via table schemas.  
- **Retrieval & Composition:** Governed RAG on trusted data; profile‑aware answers; composes code/SQL/diagrams with citations.  
- **Governance & Evolution:** Central governance (ACLs, audits), quality dashboards; freshness SLOs; continuous evals & feedback.

### Dataiku – AI Agents — **UKM 4**
- **Ingestion & Validation:** Multi‑connector ingest with schema validation; DLQ and data quality checks; provenance fields on each item.  
- **Normalization & Enrichment:** Owner/visibility/entity tags; LLM Mesh enrichment; versions and aliasing.  
- **Indexing & Linking:** Knowledge bank with vector + metadata; lineage graph across datasets/flows/models; SHACL‑like shape checks where applicable.  
- **Retrieval & Composition:** Typed retrieval (capability/knowledge/story/profile); RAG with citations; agent can assemble Mermaid diagrams and narratives.  
- **Governance & Evolution:** Guardrails and permissions centrally enforced; feedback traces; freshness windows and dashboards.

### IBM – AskIAM — **UKM 3**
- **Ingestion & Validation:** Structured ingest from IAM/HR systems (roles, entitlements, policies); validation on identity schemas; full provenance.  
- **Normalization & Enrichment:** Unifies identities, roles, apps; adds owner/visibility; PII redaction by policy.  
- **Indexing & Linking:** Identity/entitlement graph with linkable nodes; hybrid search (attributes + text); query packs for audits.  
- **Retrieval & Composition:** Typed retrieval (policy/knowledge/profile); cites back to access logs/records; limited diagram/story assembly.  
- **Governance & Evolution:** Strong RBAC/SoD enforcement; query auditability; feedback into certification cycles; high governance pass rate.

### Opsera – Hummingbird — **UKM 3**
- **Ingestion & Validation:** Pulls CI/CD, repos, tickets; validates against a DevOps insights schema; dedupe of runs and issues.  
- **Normalization & Enrichment:** Normalizes entities (service/pipeline/env); tags DORA metrics; versions by run/build.  
- **Indexing & Linking:** Hybrid index + traceability graph linking commit→build→deploy→incident; query library.  
- **Retrieval & Composition:** Typed retrieval across insights and KB; summaries with citations; diagrams for pipelines available.  
- **Governance & Evolution:** RBAC by team/project; audit logs; feedback loops for recommendation quality.

### AWS – Strands SDK — **UKM 2**
- **Ingestion & Validation:** No managed KB ingest; developers bring sources; agent tool traces provide minimal provenance.  
- **Normalization & Enrichment:** Light normalization via standard tool contracts; optional entity tags.  
- **Indexing & Linking:** BYO vector/metadata store; no native RDF/SHACL or tenancy graph → **graph/governance gate caps at 2**.  
- **Retrieval & Composition:** On‑demand tool retrieval; basic snippet assembly; citations optional if implemented by developer.  
- **Governance & Evolution:** IAM‑scoped access; developer‑managed visibility; limited platform‑level governance metrics.

### Google – Conversational Agents — **UKM 1**
- **Ingestion & Validation:** Manual KB/FAQ uploads; minimal schema validation; limited dedupe.  
- **Normalization & Enrichment:** Basic tags/intents; little entity mapping; optional PII redaction.  
- **Indexing & Linking:** Keyword/FAQ index; no vector by default; no graph.  
- **Retrieval & Composition:** Template/LLM responses; no guaranteed citations; single‑corpus retrieval.  
- **Governance & Evolution:** Basic role separation; conversation analytics; limited visibility enforcement → **cap 1**.

### GitHub – Copilot — **UKM 1**
- **Ingestion & Validation:** Ephemeral repo/PR context only; no KB ingest.  
- **Normalization & Enrichment:** None beyond repo metadata.  
- **Indexing & Linking:** No persistent index/graph.  
- **Retrieval & Composition:** Generates code/snippets; no citations/provenance.  
- **Governance & Evolution:** Org policy for usage; no KB governance → **L1**.

### Termius – Gloria — **UKM 1**
- **Ingestion & Validation:** No KB ingest; operates on live SSH outputs.  
- **Normalization & Enrichment:** Minimal tagging; no ontology.  
- **Indexing & Linking:** No persistent index/graph.  
- **Retrieval & Composition:** On‑the‑fly Q&A; no citations.  
- **Governance & Evolution:** Key‑based auth; minimal retrieval governance → **L1**.

---

## 📌 Summary & Guidance

- **Leaders (UKM 4):** Salesforce Agentforce, ServiceNow AI Agent Orchestrator, Databricks Agent Bricks, Dataiku AI Agents — all demonstrate **typed corpora**, **hybrid vector+keyword search**, **governed retrieval with citations**, and **graph/lineage linking**, with feedback/freshness loops.  
- **Strong (UKM 3):** IBM AskIAM, Opsera Hummingbird — domain‑specific graphs and governed retrieval, but limited **story/diagram composition** or cross‑domain reasoning keep them at L3.  
- **Builders (UKM 2):** AWS Strands SDK — flexible but **BYO** for index/graph/governance, so gate‑capped at L2 absent formal exportable citations and tenancy controls.  
- **Foundational (UKM 1):** Google Conversational Agents, GitHub Copilot, Termius Gloria — keyword or ephemeral context only; no exportable citations or graphs.

**Common gating failures** that cap vendors at **≤ L2**:  
1) No exportable **citations/provenance** with results.  
2) No **RDF/SHACL graph** *or* lack of **typed cross‑corpus retrieval**.  
3) No demonstrable **visibility/tenant enforcement** under test.  

**Evidence to collect for bake‑offs:** retrieval logs with citations, schema/shape files, visibility test scripts (pass/fail), freshness dashboards, and any ontology/graph query packs.
