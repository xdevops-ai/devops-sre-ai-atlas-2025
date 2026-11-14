---
layout: default
title: "AWS DevOps Agent"
parent: Platform Directory
permalink: /platforms/aws-devops-agent/
---

# AWS DevOps Agent

**Evidence reviewed: 14 November 2026.** Official documentation/announcements; no independent runtime test.

## Identity and availability

GA explicitly announced 2026-03-31. Distinct operational product from AWS Strands SDK already in Atlas.

## Capability mapping

Descriptions map product evidence to the Atlas framework, not numerical maturity scores. **Not verified does not mean absent.** Integration with telemetry is not equivalent to a native observability backend; correlation is not proof of a generic ontology.

| Atlas capability | Reviewed evidence |
| --- | --- |
| UKM — Knowledge | runbooks, history and app relationships |
| UAM — Activities | SRE tasks through configured integrations and skills |
| UDM — Diagnostics | operational investigations |
| UOM — Observability | observability integrations |
| UEOM — Events / ontology | cross-signal and deployment correlation |
| UPM — Provisioning | general provisioning not verified |

## Scope and limitations

AWS DevOps Agent is an operational investigation product, distinct from the Strands agent-building toolkit. Its GA announcement covers AWS, multicloud and on-premises operations through configured integrations and context. Current documentation and CLI describe investigation, readiness and testing surfaces, but do not establish equivalence to a general-purpose provisioning platform. Vendor MTTR statements are not an independently measured comparison.

## Official sources

1. [Official source 1](https://aws.amazon.com/about-aws/whats-new/2026/03/aws-devops-agent-generally-available/)
2. [Official source 2](https://docs.aws.amazon.com/devopsagent/latest/userguide/)
3. [Official source 3](https://docs.aws.amazon.com/cli/latest/reference/devops-agent/)

Undated source pages use the review date above, not an inferred release date. Vendor performance claims are not independent benchmarks.

[Platform Directory]({{ "/platforms/" | relative_url }}) · [Capability Framework]({{ "/capabilities/" | relative_url }})
