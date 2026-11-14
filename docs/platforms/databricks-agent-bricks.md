---
layout: default
title: "Databricks Agent Bricks"
parent: Platform Directory
permalink: /platforms/databricks-agent-bricks/
---

# Databricks Agent Bricks

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

Agent Bricks developer platform; docs updated 2026-11-12

## Is it relevant to your team?

**Why shortlist it:** Build governed data-grounded agents where the team already works in Databricks.

**Pilot question:** Can a representative agent retrieve the correct governed data and pass your evaluation set? Agent traces alone do not prove infrastructure monitoring.

This is editorial evaluation guidance inferred from the documented scope, not a product guarantee. Confirm contract, region, deployment model and feature entitlement with the provider.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | search+memory |
| UAM — Activities | durable runtime+sandbox |
| UDM — Diagnostics | custom |
| UOM — Observability | MLflow agent tracing |
| UEOM — Events / ontology | custom |
| UPM — Provisioning | agent runtime hosting |

## Scope and limitations

Current documentation points to Databricks agent development and runtime capabilities. Agent traces, sandboxing and evaluations do not by themselves establish an out-of-the-box infrastructure SRE workflow.

## Official links and evidence

1. [Develop agents on Databricks | Databricks on AWS (docs.databricks.com)](https://docs.databricks.com/aws/en/agents)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
