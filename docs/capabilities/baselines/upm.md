
---
layout: default
title: UPM Baseline (v2)
parent: Capability Framework
nav_order: 5
has_children: true
permalink: /capabilities/baselines/upm/
last_updated: 2025-10-12T13:02:58Z
---

# 🚀 Universal Provisioning Model (UPM) — v2 (0–4 scale)
*A vendor-neutral baseline describing how platforms **plan, validate, execute, verify, and audit** provisioning & change operations.*

**Last updated:** 2025-10-12T13:02:58Z

---

## What changed in v2

- **Maturity scale** normalized to 0–4 with explicit acceptance gates for each phase.
- **Evidence discipline:** plan diffs, approval trails, execution logs, verification read-backs, and rollback evidence must be exportable; otherwise scoring is **capped** (see Evidence gates below).
- **Quality KPIs** added (plan determinism, approval coverage, change success rate, rollback success, MTTR after failed change, verification latency, drift coverage, evidence completeness).
- **Atlas alignment:** token→numeric mapping for the **🚀 Provisioning** capability.

---

## ⚙️ The Five Provisioning Phases

| #   | Phase                              | Definition                                               | Typical Data                                     | Expected Capability                                                                      |
|:---:|------------------------------------|----------------------------------------------------------|--------------------------------------------------|------------------------------------------------------------------------------------------|
| **1** | **Intent & Planning**                | Turn a human/API request into a deterministic plan         | NL prompts, tickets, IaC templates (Bicep/Terraform/Helm) | Ordered resource graph; explicit commands/templates; idempotency; dependency resolution   |
| **2** | **Pre-flight & Approvals**          | Validate prerequisites and policies **before** mutation    | Cloud/K8s reads, quotas/limits, OPA/policies, RBAC scope, cost est. | Existence checks; dry-run/simulation; policy evaluation; approvals/gates                  |
| **3** | **Safe Execution**                  | Execute the plan with **guard-rails**                     | Version-pinned CLIs, mTLS endpoints, ephemeral creds | Meta blocking; pipe allow-list; timeouts/retries; progressive rollout; secret redaction  |
| **4** | **Post-Execution Verification & Drift** | Prove intended state and detect drift                      | Read-backs, health probes, rollout status, baselines | Rollout/health checks; config/state diffs vs baseline; drift alarms; rollback trigger     |
| **5** | **Audit, Governance & Rollback**    | Record, attribute, and remediate                           | Change log, approvals, evidence, ownership       | Immutable audit trail; evidence packs; visibility enforcement; **automated rollback**     |

---

## 🧩 UPM Maturity Scale (0–4)

| Level | Label           | Acceptance (must satisfy all lower levels)                                                                 |
|:----:|------------------|-------------------------------------------------------------------------------------------------------------|
| **0** | **None**         | Manual clicks/scripts; no deterministic plan; no audit.                                                    |
| **1** | **Scripted**     | Imperative scripts; basic logs; long-lived creds; best-effort read-backs.                                  |
| **2** | **Guarded**      | Deterministic plans; pre-flight checks; mTLS/secret redaction; timeouts; partial drift checks.             |
| **3** | **Policy-aware** | OPA/policy evaluation; approvals; ephemeral creds; version-pinned CLIs; streaming telemetry; drift checks; **documented rollback plan**. |
| **4** | **Autonomous**   | NL→plan + simulation; guarded auto-execution with progressive delivery; **continuous drift reconciliation**; **executed rollback** evidence; change SLOs. |

> **Evidence gates**  
> • If **plan diff + approval trail + execution logs** are not exportable, **cap at Level 2 (Guarded)**.  
> • If **rollback evidence** (successful rollback in test/prod) is missing, **cap at Level 3 (Policy-aware)**.

> **Gating rule:** Platform **UPM level = highest level where all acceptance clauses for that level and below hold**.

---

## 🔎 Per‑phase expectations by level (condensed)

### 1) Intent & Planning
- **L0:** Ad-hoc commands; no ordering/idempotency.  
- **L1:** Scripted commands; minimal templating; plan varies run-to-run.  
- **L2:** Deterministic plan with explicit resources/commands; idempotent steps; reproducible outputs.  
- **L3:** Policy-annotated plan (who/why/when); change windows; impact notes; cost est. optional.  
- **L4:** NL→plan compiler; simulation report; dependency graph; canary/blue‑green plan variants.

### 2) Pre‑flight Validation & Approvals
- **L0:** None.  
- **L1:** Manual checks; informal peer review.  
- **L2:** Automated existence/quota checks; dry-run; halt on missing prereqs.  
- **L3:** OPA/policy packs; two-person approvals; SoD; maintenance windows enforced.  
- **L4:** Auto-approval within guardrails (low‑risk lanes); budget/risk scoring; pre-flight SLOs.

### 3) Safe Execution
- **L0:** Direct shell; long‑lived tokens; no guard‑rails.  
- **L1:** Scripts with some retries; no isolation; no meta blocking.  
- **L2:** Version‑pinned CLIs; mTLS; timeouts/retries; **meta blocking**; **pipe allow‑list**.  
- **L3:** Progressive rollout; rate limiting; backoff; masked secret egress; blast‑radius constraints.  
- **L4:** Automated promotion gates; health-gated progression; self‑pause on anomalies.

### 4) Post‑Execution Verification & Drift
- **L0:** None or manual spot checks.  
- **L1:** Minimal read‑backs (success messages).  
- **L2:** Read‑backs for key resources; basic health checks.  
- **L3:** Verified rollout status; baseline diffs; drift monitors; auto‑open rollback plan.  
- **L4:** Continuous drift reconciliation; post‑change SLO checks; auto‑rollback on failure.

### 5) Audit, Governance & Rollback
- **L0:** Ad‑hoc logs; missing attribution.  
- **L1:** Text logs; no immutability; shared creds.  
- **L2:** Conversation/run logs; redactions; per‑endpoint scopes.  
- **L3:** **Immutable** audit (hash/append‑only); evidence pack (plan/approvals/logs/verify); RBAC; tenant scoping.  
- **L4:** Executed rollback recorded with evidence; change SLOs; exportable evidence pack with permalinks.

---

## 🧠 Neutral Provisioning Event (JSON Example)

```json
{
  "provisioning_event": {
    "id": "e5f2a4a2-86d1-41b6-a6f3-7a7e2b1c7f10",
    "timestamp": "2025-10-09T12:00:00Z",
    "phase": "execute",
    "intent": {
      "request": "Create AKS cluster aks-demo in eastus and namespace team-alpha",
      "source": "chatops",
      "initiator": "user-123",
      "tenant": "acme"
    },
    "target": {
      "cloud": "azure",
      "cluster_endpoint_id": "prod-east",
      "resources": [
        {"type":"az_resource_group","name":"rg-demo","location":"eastus"},
        {"type":"az_aks","name":"aks-demo","resource_group":"rg-demo"},
        {"type":"k8s_namespace","name":"team-alpha"}
      ]
    },
    "plan": {
      "commands": [
        "az group create --name rg-demo --location eastus",
        "az aks create --name aks-demo --resource-group rg-demo --node-count 2 --ssh-key-value \"ssh-rsa AAAA...\"",
        "kubectl-1.29 create namespace team-alpha"
      ],
      "resources_needed": [],
      "approvals": ["platform-owners"]
    },
    "execution": {
      "agent": "agent-session",
      "mTLS": true,
      "pipe_allow_list": ["jq","grep","wc","head","tail","cut","sort","uniq"],
      "steps": [
        {"cmd":"az group create ...","rc":0,"stdout_ref":"obs://logs/rg","stderr_trunc":false},
        {"cmd":"az aks create ...","rc":0,"stdout_ref":"obs://logs/aks","stderr_trunc":true},
        {"cmd":"kubectl-1.29 create namespace team-alpha","rc":0,"stdout":"namespace/team-alpha created"}
      ]
    },
    "verification": {
      "checks": [
        {"type":"k8s_rollout_status","target":"deployment/coredns","namespace":"kube-system","ok":true},
        {"type":"aks_connectivity","cluster":"aks-demo","ok":true}
      ],
      "drift": {"baseline_hash":"sha256:...","current_hash":"sha256:...","diff": []}
    },
    "governance": {
      "visibility": "team",
      "owner": "platform",
      "redactions": ["--token=***","Authorization: Bearer ***"]
    },
    "audit_trace": [
      {"ts":"2025-10-09T12:00:01Z","msg":"preflight complete"},
      {"ts":"2025-10-09T12:00:12Z","msg":"execute step 1 OK"},
      {"ts":"2025-10-09T12:03:34Z","msg":"verify OK"}
    ],
    "rollback": {
      "available": true,
      "plan": ["kubectl-1.29 delete ns team-alpha","az aks delete --name aks-demo --resource-group rg-demo"]
    }
  }
}
```

---

## ✅ Feature Requirements (FR) & Acceptance Criteria (AC)

**F1. Deterministic planning** — NL/API → explicit plan with ordered commands/resources and idempotency.  
**AC:** Same inputs produce the **same plan**; dependency graph exported.

**F2. Pre‑flight validation** — Existence/quotas/policy checks; dry-run; halt on failure.  
**AC:** Missing prereq fails the plan with an actionable message; policy violations listed.

**F3. Safe execution** — Version‑pinned CLIs; mTLS; meta blocking; pipe allow‑list; timeouts/retries.  
**AC:** Blocked metas reported; only `jq|grep|wc|head|tail|cut|sort|uniq` allowed post‑pipe; secrets redacted.

**F4. Verification & drift** — Read-backs, rollout/health checks; diffs vs baseline; drift alarms.  
**AC:** Verify report includes resource health and diff summary; failing checks trigger rollback plan emission.

**F5. Audit & rollback** — Immutable audit, evidence pack; RBAC; tenant scopes; executed rollback evidence.  
**AC:** Evidence pack (plan/approvals/logs/verify/rollback) downloadable; queryable by change ID.

---

## 📈 Quality KPIs & Target Bands (guide)

- **Plan determinism (% identical plans same input):** ≥ **95%** (L3), ≥ **99%** (L4)  
- **Approval coverage (% changes with approvals as required):** ≥ **90%** (L3), **100%** (L4)  
- **Policy pass rate (pre‑flight):** ≥ **85%** (L3), ≥ **95%** (L4)  
- **Change success rate:** ≥ **95%** (L3), ≥ **98%** (L4)  
- **Rollback success rate:** ≥ **90%** (L3), ≥ **97%** (L4)  
- **MTTR after failed change (minutes):** ≤ **30** (L3), ≤ **15** (L4)  
- **Plan compile P95 (ms):** ≤ **1500** (L3), ≤ **800** (L4)  
- **Verification P95 (ms):** ≤ **2000** (L3), ≤ **1200** (L4)  
- **Drift detection coverage (% resources monitored):** ≥ **70%** (L3), ≥ **90%** (L4)  
- **Evidence pack completeness (% changes with full pack):** ≥ **85%** (L3), **100%** (L4)

> Use a **fixed, shared change set** across vendors; attach permalinks to plans, logs, and verify/rollback reports.

---

## 🔁 Atlas alignment (🚀 Provisioning token → UPM level)

| Atlas token | UPM level |
|---|---:|
| **N/L** | **0** |
| **P/L** | **1** |
| **P/M** | **2** |
| **Y/M** | **3** |
| **Y/H** | **4** |

---

## 🔍 Comparison Template (vs. UPM)

| Platform               | Intent&Plan (0–4) | Pre-flight&Approvals (0–4) | Safe Exec (0–4) | Verify&Drift (0–4) | Audit&Rollback (0–4) | **Overall UPM (0–4)** | PlanDeterminism_% | ApprovalsCoverage_% | PolicyPass_% | ChangeSuccess_% | RollbackSuccess_% | MTTR_failed_change_min | Plan_P95_ms | Verify_P95_ms | DriftCoverage_% | EvidenceCompleteness_% | Evidence Links |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **Your Stack**         |                    |                           |                 |                    |                      |                       |                   |                     |              |                 |                   |                        |               |               |                 |                        |               |

> Attach evidence: plan diffs, approvals, logs, verify/diff reports, rollback outputs (or recordings).

---

## 📝 Conformance Checklist

- **Deterministic plan** with dependency ordering and idempotency.  
- **Pre-flight first**: existence/policy checks and dry-run gates.  
- **Guard-rails on by default**: meta blocking; pipe allow-list; timeouts; retries; output truncation; secret redaction.  
- **Secure execution**: mTLS, ephemeral creds, endpoint scoping.  
- **Verification & drift**: health checks; diffs vs baseline; alarms; rollback plan.  
- **Auditability**: immutable logs; evidence packs; tenant-scoped RBAC; exportable permalinks.  
- **Rollback**: executed rollback evidence for Level 4.

---

## 🧪 Minimal Acceptance Examples

- **Meta blocking** — commands containing shell metas (`; && || \ $() < > >> \n`) are rejected with a clear error.  
- **Pipe allow-list** — only `grep|jq|wc|head|tail|cut|sort|uniq` permitted post-pipe; others rejected.  
- **TLS fallback** — certificate error triggers one retry with `--insecure-skip-tls-verify` (logged).  
- **Missing prerequisite** — plan halts when `resources_needed` check fails; explicit message returned.  
- **Secret redaction** — tokens/Authorization headers masked in echoes/logs.  
- **Rollback dry-run** — simulated rollback produces a valid, executable plan; Level 4 requires at least one executed rollback with evidence.

---

## 🗂️ Field Canonicals (Provisioning)

- **phase** ∈ `{plan, preflight, execute, verify, audit}`  
- **source** ∈ `{chatops, api, ticket}`  
- **visibility** ∈ `{team, org, private}`  
- **agent** ∈ `{agent-session}`  
- **pipe_allow_list** default: `grep,jq,wc,head,tail,cut,sort,uniq`
