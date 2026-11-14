---
layout: default
title: "Kubiya — ChatOps + Workflow Execution"
parent: Platform Directory
permalink: /platforms/kubiya/
---

# Kubiya — ChatOps + Workflow Execution

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

Kubiya control plane/workflows, documented hosted+self-hosted

## Is it relevant to your team?

**Why shortlist it:** Offer governed operational workflows through a shared execution control plane.

**Pilot question:** Where will runners and the control plane operate, and can the workflow enforce the requesting user's permissions and approval boundaries?

This is editorial evaluation guidance inferred from the documented scope, not a product guarantee. Confirm contract, region, deployment model and feature entitlement with the provider.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | Context Graph |
| UAM — Activities | governed workflows |
| UDM — Diagnostics | tool-dependent |
| UOM — Observability | integrated |
| UEOM — Events / ontology | graph, ontology scope unproven |
| UPM — Provisioning | infrastructure workflows |

## Scope and limitations

Kubiya documents hosted and self-hosted control-plane options and governed workflows. The MCP interface exposes selected operations, not proof of every infrastructure capability. Diagnosis depends on connected tools; validate the execution identity and audit trail in your own workflow.

## Official links and evidence

1. [Kubiya MCP server repository and setup (github.com)](https://github.com/kubiyabot/kubiya-mcp-server)
2. [MCP interface overview (docs.kubiya.ai)](https://docs.kubiya.ai/mcp/overview) — automated access check inconclusive
3. [Control-plane deployment overview (docs.kubiya.ai)](https://docs.kubiya.ai/core-concepts/control-plane/overview) — automated access check inconclusive
4. [Workflow API overview (docs.kubiya.ai)](https://docs.kubiya.ai/api-reference/workflows/overview) — automated access check inconclusive

Some official pages returned an access error or an unavailable-page response during the automated link check. This is not evidence that the product or link is unavailable to every reader. The capability review and link availability are separate checks.

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
