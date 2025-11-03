---
layout: default
title: UAM Baseline (v2)
parent: Capability Framework
nav_order: 6
has_children: true
permalink: /capabilities/baselines/uam/
last_updated: 2025-10-12T00:00:00Z
---

# 🧭 Universal Activity Model (UAM) — Baseline Framework v2 (0–4 scale)
*A vendor-neutral framework describing how intelligent platforms **capture, sanitize, enrich, index, retrieve, replay, summarize, and govern** human/tool activity.*  
This version aligns the **Activities** capability in the Atlas with a **0–4 maturity scale** and tightens acceptance criteria, KPIs, and lint rules.

**Last updated:** 2025-10-12T00:00:00Z

---

## 🔄 What changed in v2
- **Maturity scale normalized to 0–4** (was 0–5).  
- Clear **token→level mapping** for Atlas scores (`N/L, P/L, P/M, Y/M, Y/H`).  
- Tightened **Feature Requirements & Acceptance Criteria** for each phase.  
- Added **lint checks** and **comparison template** that output an **Overall Activity Maturity (0–4)**.

---

## ⚙️ The Seven Activity Phases

| Phase | Definition | Typical Data | Expected Capability |
|---|---|---|---|
| **1. Capture & Sessionization** | Start/continue a durable activity session and record turns | Chat/tool/system messages, tags, endpoint IDs | Durable `base_id`, monotonic timestamps, `actor/channel/doc_type` normalization |
| **2. Evidence Policy & Verification** | Ingest artifacts under policy, verify, dedupe | URLs, files, metrics/logs/alerts, code/PRs | Allow-lists (domains/params/schemes), canonicalization, hashing, async verification, TTL-based dedupe |
| **3. Sanitization & Redaction** | Normalize and scrub sensitive info | Text, query strings, paths, tokens | Secret/PII masking, path/commit normalization, governance scope injection |
| **4. Enrichment & Linking** | Build relationships and hop graphs | Commits, PRs, paths, tickets, services | Link extraction, manifests/edges, impact hops & blast-radius narrative |
| **5. Indexing & Search** | Persist rows and enable retrieval | Embeddings + scalar metadata | Vector, metadata-only, combined, faceted search with rerank & governance filters |
| **6. Replay & Summarization** | Reconstruct clear timelines; TL;DR | Activity rows + evidence clusters | Role-labeled replay with noise pruning; concise summaries with top evidence |
| **7. Governance, Export & Operability** | Enforce visibility; export evidence; observe SLOs | Tenant/user/visibility, metrics | RBAC/scope, Markdown/JSON exports, health/metrics, retries/backoff/circuit-breakers |

---

## 🧩 UAM Maturity Scale (0–4)

| Level | Label | Description |
|---|---|---|
| **0 — None** | No capability | Unstructured logs; no sessions, policy, or search |
| **1 — Basic** | Capture only | Sessionized transcripts with minimal export; weak/no policy |
| **2 — Indexed** | Searchable | Vector/keyword search + basic metadata; partial governance |
| **3 — Governed** | Policy-enforced | Evidence policy, sanitization, scoped retrieval, replay & summary |
| **4 — Operational** | SLO-backed | Hop graphs; verification & dedupe; rerank; exports; metrics/SLOs; resilient at scale |

### Token → Level mapping (Atlas **Activities** → UAM 0–4)

- `N/L` → **0**  
- `P/L` → **1**  
- `P/M` → **2**  
- `Y/M` → **3**  
- `Y/H` → **4**  

> Use this mapping to compute a single **Overall Activity Maturity (0–4)** from Atlas tokens.

---

## 🧠 Neutral Activity Event (JSON envelope)

```json
{
  "activity_event": {
    "id": "uuid",
    "timestamp": "2025-10-09T12:00:00Z",
    "phase": "capture",
    "base_id": "uuid-base",
    "section": "default",
    "status": "active",
    "doc_type": "message",
    "actor": "user",
    "channel": "chat",
    "text": "Show P95 latency for checkout over the last 45m",
    "text_sha256": "sha256:...",
    "endpoint_id": "prod-east",
    "tool_name": null,
    "tags_arr_csv": "checkout,latency",
    "links_repo_commits_csv": "0f3a1c2,1a2b3c4d",
    "links_repo_prs_csv": "#1342",
    "links_repo_paths_csv": "services/checkout/limiters.py",
    "visibility": "team",
    "tenant_id": "acme",
    "user_id": "user-123",
    "evidence": [
      { "kind": "metric", "title": "P95 latency - checkout", "uri": "https://grafana/acme/p95?panel=12", "hash": "sha256:...", "status": "verified" },
      { "kind": "log",    "title": "gateway 5xx errors",     "uri": "https://loki/acme?q=severity%3Derror", "hash": "sha256:...", "status": "verified" }
    ],
    "correlation_group": "uuid-base",
    "governance": { "pii_redacted": true }
  }
}
```

---

## 🧱 Canonical Data Model (row fields)

`id`, `base_id`, `section`, `ts`, `status (active|closed)`, `doc_type (message|summary|transcript)`,  
`actor (user|assistant|tool|system)`, `channel (chat|oc|task|shell|endpoint)`, `text`, `text_sha256`,  
`embedding_vector`, `endpoint_id`, `tool_name`, `tags_arr_csv`, `metadata_json`,  
`links_repo_commits_csv`, `links_repo_prs_csv`, `links_repo_paths_csv`,  
`visibility (team|org|private)`, `tenant_id`, `user_id`.

**Evidence kinds:** `web`, `metric`, `log`, `code`, `ticket`, `image`, `k8s_event`, `alert`, `change`.

---

## 🎯 Use-case Catalog

- **UC-A1 — Sessionized capture across channels:** durable `base_id`, correct `actor/channel/doc_type`.  
- **UC-A2 — Evidence ingestion & verification:** canonicalize → allow-list → verify → dedupe.  
- **UC-A3 — Replay timeline (handoff-ready):** chronological, role-labeled, noise-pruned.  
- **UC-A4 — TL;DR summary:** concise narrative + links to top evidence clusters.  
- **UC-A5 — Combined semantic + faceted search:** vector + filters + rerank under governance.  
- **UC-A6 — Impact hops (code/change correlation):** commits/PRs/paths graph + blast-radius note.  
- **UC-A7 — Governance-enforced retrieval:** tenant/user/visibility constraints + masking.  
- **UC-A8 — Close & export:** status→`closed`; export summary/replay/evidence/hops (Markdown/JSON).

---

## ✅ Feature Requirements (FR) & Acceptance Criteria (AC)

### F1. Capture & Sessionization
- **FR:** Durable `base_id`, normalized turn fields, monotonic timestamps.  
- **AC:** First turn yields non-empty `base_id`; subsequent turns append until closed.

### F2. Evidence Policy & Verification
- **FR:** URI canonicalization, allow-lists (domains/params/schemes), hashing, TTL-dedupe, async verification.  
- **AC:** Disallowed items rejected with reason; allowed → `status=verified|reason`.

### F3. Sanitization & Redaction
- **FR:** Normalize commits/PRs/paths; mask secrets/PII; inject governance filters.  
- **AC:** Secret-like substrings masked; artifacts canonicalized and deduped.

### F4. Enrichment & Linking
- **FR:** Extract links; maintain manifests/edges; build hop graphs and narrative.  
- **AC:** `retrieve_hops` returns stable nodes/edges; duplicates deduped.

### F5. Indexing & Search
- **FR:** Persist to vector store with scalar metadata; support vector/metadata/combined/faceted; rerank.  
- **AC:** Correct ranking per mode; rerank improves textual match quality.

### F6. Replay & Summarization
- **FR:** Role-aware replay with noise pruning; concise TL;DR with evidence references.  
- **AC:** Renderers output non-empty Markdown; highlights link to verified evidence.

### F7. Governance, Export & Operability
- **FR:** Enforce tenant/user/visibility; Markdown/JSON exports; health/metrics; retries/backoff/circuit-breakers.  
- **AC:** Out-of-scope queries return empty + governance note; healthcheck stable under load.

---

## 📈 Non-functional Targets

- **Latency:** P50 search ≤ **800 ms**, P95 replay ≤ **1.5 s** (typical sessions).  
- **Scale:** ≥ **millions of rows**, sharded vectors; configurable verify concurrency.  
- **Resilience:** retries with jitter, timeouts, circuit-breakers; idempotent writes.  
- **Security:** strict allow-lists; TLS to backends; PII redaction on ingest & render.

---

## 🔍 Comparison Template (vs. UAM v2)

| Platform | Capture & Session | Evidence Policy | Sanitization | Enrichment/Links | Index & Search | Replay & Summary | Governance & Ops | **Overall Activity Maturity (0–4)** |
|---|---|---|---|---|---|---|---|---|
| **Your Platform** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **4 — Operational** |
| Competitor A |  |  |  |  |  |  |  |  |
| Competitor B |  |  |  |  |  |  |  |  |

> Keep evidence links (screenshots, API outputs, exports) for every ✓.

---

## 🧪 Minimal Acceptance Examples

- **Schema rejection** — malformed activity JSON rejected with JSON-pointer to failing field.  
- **Evidence verify** — non-allow-listed domain is blocked with reason; allow-listed is marked `verified`.  
- **Replay quality** — renderer outputs a timeline with roles and links to **verified** evidence.  
- **Governance filter** — team-scoped query cannot see `visibility=org|private` rows.  

---

## 🧪 Lint checks (regex-style)

- **Slash notation only:** reject `\b([YMNPLH])\s*[–—-]\s*([YMNPLH])\b`.  
- **No hybrid tokens:** reject `\bN/P/L\b` (choose `N/L` or `P/L`).  
- **Confidence tokens:** restrict to `Low|Med|High`.  
- **Activity maturity tokens:** allow only `N/L|P/L|P/M|Y/M|Y/H` → map via table above.

---

## 📦 Appendix — Combined Search (pseudo-request)

```json
{
  "command": "combined_search",
  "text": "checkout p95 latency",
  "filters": {
    "endpoint_id": "prod-east",
    "actor_in": ["tool","assistant"],
    "ts_gte": "2025-10-08T00:00:00Z"
  },
  "limit": 20
}
```

---

## 📊 Platform Ratings (UAM v2)

| Platform | Atlas Token (Activities) | **Overall UAM (0–4)** | Evidence Highlights / Gating Note |
|---|---|---:|---|
| **Atlassian – Rovo Dev** | **Y/M** | **3** | Durable in-app sessions (Jira/Confluence), permission-aware answers, chat transcripts; limited formal evidence verification/dedupe keeps it below 4. |
| **AWS – Strands SDK** | **P/M** | **2** | Strong agent tracing via OTel; BYO policy/index; no turnkey evidence packs or governed retrieval. |
| **Cisco – Splunk AI Agents (AgenticOps)** | **Y/H** | **4** | Incident-scoped sessions, auto evidence packs, dedupe/correlation, exportable timelines under enterprise RBAC. |
| **Databricks – Agent Bricks** | **Y/M** | **3** | MLflow/Delta capture, lineage, governed access; evidence/verification patterns exist but are implementation-driven (not one-click). |
| **Datadog – Bits AI** | **Y/H** | **4** | End-to-end incident timelines, TL;DR with citations, cross-signal evidence, team-scoped RBAC, shareable permalinks. |
| **Dataiku – AI Agents** | **Y/H** | **4** | Trace Explorer, guardrails & registry, auditable runs, exportable artifacts; mature replay/summarization. |
| **DuploCloud – AI Help Desk** | **Y/H** | **4** | Ticketed sessions tied to actions, approvals, full audit of AI suggestions/execution within cloud guardrails. |
| **Dynatrace – Davis AI** | **Y/H** | **4** | Problem cards with causal timelines, evidence links, exports; governed access & privacy controls. |
| **Elastic – AI Assistant for Observability** | **P/M** | **2** | Ephemeral chat context; relies on Kibana audit & saved objects; limited native evidence packs or replay automation. |
| **GitHub – Copilot** | **N/L** | **0** | Stateless completions; no durable sessions, evidence policy, or retrieval across activity. |
| **Google – Vertex AI Agent Builder** | **P/L** | **1** | Session IDs and logs per dialog; minimal policy/verification; limited retrieval & replay beyond transcripts. |
| **IBM – AskIAM** | **Y/M** | **3** | Sessionized IAM actions & dialogs, strict policy/SoD gates, strong audit; narrower multi-signal capture keeps it at 3. |
| **JFrog – Project “Fly”** | **P/M** | **2** | Session per pipeline run with annotated logs; limited policy enforcement, replay beyond CI context. |
| **Solo.io – Kagent** | **Y/M** | **3** | Chat-based K8s ops sessions, RBAC-scoped evidence (metrics/logs/events), good replay in chat; light formal verification/evidence packs. |

---

## 📝 Executive Summary (Activities)

- **Distribution (14 platforms):**  
  **Level 4 (Y/H):** Cisco, Datadog, Dataiku, DuploCloud, Dynatrace (5)  
  **Level 3 (Y/M):** Atlassian Rovo, Databricks, IBM AskIAM, Solo.io Kagent (4)  
  **Level 2 (P/M):** AWS Strands, Elastic, JFrog (3)  
  **Level 1 (P/L):** Google Vertex (1)  
  **Level 0 (N/L):** GitHub Copilot (1)

- **Common gating gaps from 3→4:**  
  1) Missing **exportable evidence packs** (permalinks/exports that reproduce queries/charts).  
  2) Lack of **verification/dedupe** discipline (allow-lists, hashing, TTL dedupe).  
  3) Incomplete **replay & TL;DR** (noise-pruned timelines with evidence citations).  
  4) Weak **governed retrieval** (tenant/user/visibility filtering).

- **What Level 4 vendors do well:**  
  - Treat every interaction as a **durable session** with monotonic timestamps & actor attribution.  
  - Provide **evidence packs** and **one-click handoffs** for review/audit.  
  - Enforce **RBAC/tenancy**, redact PII, and expose **SLOs** for ingest/query.  
  - Offer **replayable timelines** and **summaries** citing verified evidence.

- **Fast-track improvements for Level 2–3:**  
  - Introduce **policy-enforced evidence pipelines** (allow-lists, hashing, dedupe).  
  - Implement **evidence pack exports** (Markdown/JSON).  
  - Add **role-labeled replay renderers** with TL;DR and verified links.  
  - Enforce **governed retrieval** with visibility filters in all search interfaces.
