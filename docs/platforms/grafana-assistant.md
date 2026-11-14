---
layout: default
title: "Grafana Assistant"
parent: Platform Directory
permalink: /platforms/grafana-assistant/
---

# Grafana Assistant

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

Assistant Investigations GA since late July 2026; Watchers GA 2026-10-19; Managed Sandboxes public preview as of 2026-10-20. Availability differs by feature.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | skills and runbook context |
| UAM — Activities | triggered investigations; code-fix sandboxes preview |
| UDM — Diagnostics | multi-step investigations |
| UOM — Observability | native Grafana Cloud telemetry and visualization |
| UEOM — Events / ontology | Watchers and incident triggers; generic ontology unverified |
| UPM — Provisioning | not verified |

## Scope and limitations

Grafana Assistant combines observability-native investigations with natural-language monitoring and skills. Investigations and Watchers have GA milestones, while Managed Sandboxes for code-fix work remain public preview in the October announcement. Skills and tool approvals have their own configuration. Access from self-managed Grafana still connects to Grafana Cloud and does not establish wholly offline or on-premises inference.

## Official sources

1. [Official source 1](https://grafana.com/blog/observabilitycon-2026-announcements/)
2. [Official source 2](https://grafana.com/whats-new/page/2/)
3. [Official source 3](https://grafana.com/blog/grafana-assistant-everywhere/)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
