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

## Official sources

1. [Official source 1](https://github.com/Qovery/qovery-migration-ai-agent)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
