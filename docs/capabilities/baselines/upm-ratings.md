---
layout: default
title: UPM Rating Example (v2)
parent: UPM Baseline (v2)
nav_order: 10
permalink: /capabilities/baselines/upm/rating-example/
last_updated: 2025-11-03T00:00:00Z
---

> Historical assessment: scores below were not revalidated in the November 2026 review. See the [current evidence matrix]({{ "/capabilities/" | relative_url }}).


# 🧪 UPM Rating Example — *AbcCorp Cloud Platform*

This worked example shows how to score a platform against **UPM v2** using the five phases, **evidence gates**, and KPIs.

---

## 1) Phase Scores (0–4)

| Phase                      | Score | Notes |
|:--------------------------|:-----:|:------|
| **Intent & Planning**     | **3** | Deterministic NL→plan compiler with dependency graph and idempotent steps. |
| **Pre-flight & Approvals**| **3** | OPA policy packs; two-person approvals (SoD); maintenance windows enforced. |
| **Safe Execution**        | **3** | Version-pinned CLIs, mTLS; **meta blocking** + **pipe allow-list**; progressive rollout. |
| **Verification & Drift**  | **3** | Read-backs + rollout checks; baseline diffs; drift monitors create tickets. |
| **Audit & Rollback**      | **3** | Immutable audit; evidence packs (plan/approvals/logs/verify). Rollback **plan** present, but no executed rollback evidence yet. |

**Evidence gates:**  
- Exportable **plan diff + approvals + logs**: **Yes** → passes first gate.  
- **Executed rollback evidence**: **No** → **caps Overall at Level 3**.

**➡ Overall UPM Level: `3 — Policy-aware`**

---

## 2) KPI Snapshot

| KPI                          | Value  |
|-----------------------------:|:-------|
| **PlanDeterminism_%**        | **97.2** |
| **ApprovalsCoverage_%**      | **96.4** |
| **PolicyPass_%**             | **90.7** |
| **ChangeSuccess_%**          | **97.9** |
| **RollbackSuccess_%**        | **92.1** (simulated in prod) |
| **MTTR_failed_change_min**   | **22**  |
| **Plan_P95_ms**              | **1200** |
| **Verify_P95_ms**            | **1700** |
| **DriftCoverage_%**          | **78**  |
| **EvidenceCompleteness_%**   | **92**  |

> To reach **Level 4**, execute at least one rollback **in each environment tier** (test/staging/prod) and attach evidence.

---

## 3) Evidence Links (examples)

- Plan diff permalink: `https://ops.example.com/changes/CHG-4421/plan`  
- Approvals: `https://ops.example.com/changes/CHG-4421/approvals`  
- Execution logs: `https://logs.example.com/kibana/app/discover#...`  
- Verify report: `https://ops.example.com/changes/CHG-4421/verify`  
- Drift dashboard: `https://grafana.example.com/d/drift/overview`

> Replace with real permalinks in your environment. Evidence must be re-runnable or immutable snapshots.

---

## 4) Comparison Row (copy/paste)

| Platform               | Intent&Plan (0–4) | Pre-flight&Approvals (0–4) | Safe Exec (0–4) | Verify&Drift (0–4) | Audit&Rollback (0–4) | **Overall UPM (0–4)** | PlanDeterminism_% | ApprovalsCoverage_% | PolicyPass_% | ChangeSuccess_% | RollbackSuccess_% | MTTR_failed_change_min | Plan_P95_ms | Verify_P95_ms | DriftCoverage_% | EvidenceCompleteness_% | Evidence Links |
|------------------------|:-----------------:|:---------------------------:|:---------------:|:------------------:|:--------------------:|:---------------------:|:-----------------:|:-------------------:|:------------:|:---------------:|:-----------------:|:----------------------:|:------------:|:-------------:|:---------------:|:----------------------:|:-------------:|
| **AbcCorp Platform**   | **3**             | **3**                       | **3**           | **3**              | **3**                | **3**                 | **97.2**          | **96.4**            | **90.7**     | **97.9**        | **92.1**          | **22**                 | **1200**     | **1700**      | **78**          | **92**                 | plan:… · approvals:… · logs:… · verify:… · drift:… |

---

## 5) Gaps & Next Steps

1. **Executed rollback evidence** in prod; attach logs and verification read-back.  
2. Increase **DriftCoverage** to ≥ **90%** and add auto-reconcile for low-risk drifts.  
3. Raise **PolicyPass** to ≥ **95%** via pre-flight remediation.  
4. Reduce **Verify_P95** below **1200 ms** (optimize health checks, retries, parallelization).
