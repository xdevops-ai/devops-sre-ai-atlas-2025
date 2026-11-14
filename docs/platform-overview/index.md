---
layout: default
title: Buyer Guide
nav_order: 3
permalink: /platform-overview/
---

# Choose an AI operations platform for a real job

**Evidence edition: November 2026.** Start with the operational outcome, not a universal vendor ranking. This guide helps you make a shortlist, define a fair pilot and identify what must be verified before buying. Product evidence is linked from each [platform record]({{ "/platforms/" | relative_url }}).

## 1. Pick the problem you will measure

| Your team's problem | Start with | Illustrative records, not a ranking | What a useful pilot must show |
| --- | --- | --- | --- |
| Engineers spend too long assembling incident evidence | AI SRE investigation or an assistant in your existing observability stack | [AWS DevOps Agent]({{ "/platforms/aws-devops-agent/" | relative_url }}), [Robusta / HolmesGPT]({{ "/platforms/robusta-holmesgpt/" | relative_url }}), [Datadog]({{ "/platforms/datadog-bits-ai/" | relative_url }}), [Grafana]({{ "/platforms/grafana-assistant/" | relative_url }}) | Correctly scoped evidence, explainable hypotheses, a clear inconclusive state and a human-verifiable outcome |
| On-call coordination is fragmented across tools and people | Incident-response workflow plus investigation | [Rootly]({{ "/platforms/Rootly/" | relative_url }}), [incident.io]({{ "/platforms/incident-io/" | relative_url }}), [PagerDuty]({{ "/platforms/pagerduty-aiops/" | relative_url }}) | Less manual coordination without missed notifications, unsafe actions or duplicated incidents |
| Routine operational requests wait on a specialist | Governed workflow / infrastructure automation | [Kubiya]({{ "/platforms/kubiya/" | relative_url }}), [DuploCloud]({{ "/platforms/duplocloud-ai-help-desk/" | relative_url }}), [Komodor]({{ "/platforms/komodor-klaudia/" | relative_url }}) | A scoped request, required approval, execution evidence, verification and a recovery path |
| CI failures and code changes consume engineering time | Repository / delivery agents | [GitHub Copilot]({{ "/platforms/github-copilot-coding-agent/" | relative_url }}), [GitLab Duo]({{ "/platforms/gitlab-duo/" | relative_url }}), [Harness]({{ "/platforms/harness-ai/" | relative_url }}) | A reviewable change with relevant tests; a green agent response is not proof that a PR is safe |
| You need a custom agent over your own tools and data | Agent-building framework or managed runtime | [Strands]({{ "/platforms/aws-strands-sdk/" | relative_url }}), [Foundry]({{ "/platforms/azure-ai-agent-service-foundry/" | relative_url }}), [kagent]({{ "/platforms/soloio-kagent/" | relative_url }}) | Feasible integration, governance and operating effort, not merely a successful demo prompt |

A product may span multiple rows. Existing integrations, data boundaries and permissions usually matter more than feature counts. Do not buy multiple tools merely because an archetype diagram has several boxes.

## 2. Apply hard constraints before a demo

- **Availability:** verify the exact feature, plan, region and release. A usable product may still contain preview or early-access features.
- **Deployment and data:** identify what runs locally, what leaves your network, where inference happens and what is retained. A local runner is not proof of offline inference.
- **Authority:** separate read access, suggested actions, PR creation and production mutation. Test tenant, project, user and service boundaries.
- **Integration:** list the actual telemetry, repository, cloud and chat systems required. Check connector scope, rate limits and unsupported versions.
- **Operational ownership:** agree who maintains connectors, runbooks, prompts, custom agents and incident escalation when the assistant fails.
- **Commercial scope:** get written clarification of required modules, add-ons, usage units, support and exit/export terms. This Atlas does not provide verified current quotes.

## 3. Run one reproducible pilot

Choose a small, agreed set of historical incidents and representative safe tasks. Include incomplete telemetry, a misleading alert, an unavailable tool, a permission denial and an incident the system should not resolve confidently. Keep data and expected outcomes consistent across candidates.

[Download the pilot scorecard (CSV)]({{ "/assets/evaluation-scorecard.csv" | relative_url }}). Fill in targets before testing; the blank thresholds are intentional.

| Measure | How to calculate / observe | Why it matters |
| --- | --- | --- |
| Successful task rate | Tasks whose agreed outcome a human or independent check verified ÷ attempted tasks | Avoids counting plausible narratives as success |
| Evidence quality | Check whether claims link to the right time, resource, source and supporting observation | Makes the conclusion inspectable |
| Human effort | Operator minutes for setup, investigation, correction, approvals and cleanup | Captures transferred work, not only response speed |
| Time to useful evidence | Time until the first correct, actionable, cited finding | Measures assistance without promising automatic resolution |
| False-confidence rate | Incorrect confident answers or false “fixed” states ÷ evaluated cases | Exposes harmful overclaiming |
| Authorization failures | Attempts or successful actions beyond the intended user/project/tool scope | Safety gate, not a score to average away |
| Recovery behavior | What happens after timeout, partial execution, duplicate event or connector failure | Shows whether the workflow can be operated safely |
| Fully allocated cost per successful task | Subscription + usage + infrastructure + allocated integration/operations effort, divided by verified successful tasks | Allows a more useful comparison than token prices alone |

Keep sample size, excluded cases and limitations with the result. A small pilot is not a statistical guarantee. Re-test after material connector, model, permission or workflow changes.

## 4. Compare like with like

The [six-axis evidence matrix]({{ "/capabilities/" | relative_url }}) is a navigation aid, not a league table. Compare candidates within the same job and deployment constraints.

- Native telemetry storage and querying external telemetry are different architectures, not automatic good/bad scores.
- Building a custom agent and buying a packaged investigation product have different engineering costs.
- A proposed fix, an approved PR and a verified production repair are different outcomes.
- Identity provisioning is not general infrastructure provisioning. Agent tracing is not full-stack infrastructure monitoring.
- Vendor case studies and internal benchmarks can motivate a pilot; they do not establish your savings or superiority over another vendor.

## Review limitations and history

This edition reviews public official material, not customer installations. Access-limited or inconclusive evidence is identified in the individual records. [Historical overview]({{ "/history/2026-01-overview/" | relative_url }}) and [historical scores]({{ "/capabilities/historical-scores/" | relative_url }}) are retained for traceability, not current purchasing recommendations.
