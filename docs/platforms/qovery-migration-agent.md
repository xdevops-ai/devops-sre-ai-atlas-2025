---
layout: default
title: "Qovery Migration Agent"
parent: Platform Directory
permalink: /platforms/qovery-migration-agent/
---

# Qovery Migration Agent

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

Qovery Migration AI Agent, OSS still-in-development per README

## Is it relevant to your team?

**Why shortlist it:** Experiment with generated migration artifacts for a supported app/provider combination.

**Pilot question:** Verify the repository's current supported source platform and manually validate generated Terraform and Dockerfiles before treating migration as successful.

This is editorial evaluation guidance inferred from the documented scope, not a product guarantee. Confirm contract, region, deployment model and feature entitlement with the provider.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | provider app context |
| UAM — Activities | file-generation workflow |
| UDM — Diagnostics | manifest validation |
| UOM — Observability | Not verified |
| UEOM — Events / ontology | Not verified |
| UPM — Provisioning | Terraform+Dockerfile generation |

## Scope and limitations

README scope inconsistent between intro and feature list; conservative Heroku-to-Qovery focus, not general migration success.

## Official links and evidence

1. [GitHub - Qovery/qovery-migration-ai-agent: Qovery Migration AI Agent to Automate and Ease the Migration From C (github.com)](https://github.com/Qovery/qovery-migration-ai-agent)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
