---
layout: default
title: "PagerDuty AIOps / Paige (SRE Agent)"
parent: Platform Directory
permalink: /platforms/pagerduty-aiops/
---

# PagerDuty AIOps / Paige (SRE Agent)

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

Paige (SRE Agent), documented; access and AIOps console entitlements differ. Individual feature availability must be checked separately.

## Is it relevant to your team?

**Why shortlist it:** Connect AI investigation to an established on-call and incident-response process.

**Pilot question:** Can an incident move from alert through a scoped investigation and approved workflow, and which skills require early-access entitlement?

This is editorial evaluation guidance inferred from the documented scope, not a product guarantee. Confirm contract, region, deployment model and feature entitlement with the provider.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | connector/skill context |
| UAM — Activities | workflows |
| UDM — Diagnostics | investigation |
| UOM — Observability | integrated logs+metrics |
| UEOM — Events / ontology | event correlation |
| UPM — Provisioning | Not verified |

## Scope and limitations

Paige, previously described as SRE Agent, provides an investigation surface within PagerDuty. Current documentation distinguishes PagerDuty AI access from the AIOps-plus-AI console requirements. Historical GA announcements do not make every skill or newer feature generally available.

## Official links and evidence

1. [Paige overview, requirements and availability (docs.pagerduty.com)](https://docs.pagerduty.com/ai-automation/advance/sre-agent)
2. [PagerDuty release notes (docs.pagerduty.com)](https://docs.pagerduty.com/get-started/release-notes)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
