---
layout: default
title: "BMC Helix AIOps (ServiceOps)"
parent: Platform Directory
permalink: /platforms/bmc-helix-aiops/
---

# BMC Helix AIOps (ServiceOps)

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

BMC Helix AIOps; documented observability-cost and HelixGPT Log Analyzer use case. This does not validate availability of the entire agentic suite.

## Is it relevant to your team?

**Why shortlist it:** Evaluate source-side log analysis and observability-cost controls in an existing BMC Helix environment.

**Pilot question:** Can the documented log-analysis workflow operate on your sources with the required access and a measurable reduction in unnecessary ingestion? Confirm broader agentic capabilities separately.

This is editorial evaluation guidance inferred from the documented scope, not a product guarantee. Confirm contract, region, deployment model and feature entitlement with the provider.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | Not verified |
| UAM — Activities | integration automation documented |
| UDM — Diagnostics | HelixGPT source-side log analysis in reviewed use case |
| UOM — Observability | OpenTelemetry ingestion, filtering and usage dashboards |
| UEOM — Events / ontology | service-model and event context; broader ontology not verified |
| UPM — Provisioning | Not verified |

## Scope and limitations

The current official documentation describes OpenTelemetry ingestion/filtering, usage dashboards and HelixGPT Log Analyzer just-in-time analysis at the log source without ingesting those logs. This is a concrete observability-cost use case, not proof of the full suite's agentic maturity. Required configuration and entitlement need separate confirmation.

## Official links and evidence

1. [Managing the cost of observability (docs.helixops.ai)](https://docs.helixops.ai/bin/IT-Operations-Management/Operations-Management/BMC-Helix-AIOps/aiops262/Getting-started/Use-cases/Managing-the-cost-of-observability/)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
