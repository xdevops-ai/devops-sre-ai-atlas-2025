---
layout: default
title: "Robusta / HolmesGPT"
parent: Platform Directory
permalink: /platforms/robusta-holmesgpt/
---

# Robusta / HolmesGPT

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

documented installable product; OSS HolmesGPT plus commercial Robusta SaaS/self-hosted platform. Commercial and OSS feature scopes differ.

## Is it relevant to your team?

**Why shortlist it:** Investigate Kubernetes incidents using existing telemetry, with an OSS or commercial route to evaluate.

**Pilot question:** Which required features are available in HolmesGPT OSS versus Robusta commercial, and does the selected deployment respect your data boundary?

This is editorial evaluation guidance inferred from the documented scope, not a product guarantee. Confirm contract, region, deployment model and feature entitlement with the provider.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | investigation history and context |
| UAM — Activities | investigation tools; dangerous calls approval-gated |
| UDM — Diagnostics | incident investigation |
| UOM — Observability | integrated telemetry; not a full replacement backend |
| UEOM — Events / ontology | alert timelines; general ontology unverified |
| UPM — Provisioning | not verified |

## Scope and limitations

Robusta investigates incidents over existing telemetry using an in-cluster agent and outbound-only SaaS connectivity, with self-hosted options. Commercial REST/SSE APIs, approval-required interactions and production-context PR reviews must not be assumed to exist in open-source HolmesGPT. Legacy deterministic Robusta Classic playbooks are distinct from HolmesGPT. Performance has not been independently tested.

## Official links and evidence

1. [Architecture - Robusta documentation (docs.robusta.dev)](https://docs.robusta.dev/master/how-it-works/architecture.html)
2. [Holmes Chat API - Robusta documentation (docs.robusta.dev)](https://docs.robusta.dev/master/configuration/holmesgpt/holmes-chat-api.html)
3. [HolmesGPT PR Review - Robusta documentation (docs.robusta.dev)](https://docs.robusta.dev/master/configuration/github-actions/holmes-pr-review.html)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
