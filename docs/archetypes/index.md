---
layout: default
title: Platform Archetypes
nav_order: 2
permalink: /archetypes/
---

# Understand what kind of product you are evaluating

**Updated November 2026.** Archetypes describe a starting point, not a maturity score. One vendor can span categories; a platform portfolio may require several separately licensed products.

| Archetype | Useful when | Integration / ownership to expect | Boundary to verify |
| --- | --- | --- | --- |
| Observability-native assistant | Your useful production signals already live in that platform | Telemetry coverage, entity mapping, retention and account entitlements | Whether it only explains or can also execute changes |
| Cross-tool AI SRE | Investigation crosses several monitoring, cloud and code systems | Connector scopes, production context, data residency and investigation ownership | Evidence quality, inconclusive cases and supported write actions |
| Incident coordination | On-call routing, communication and repeatable incident process are the bottleneck | Chat, alerting, escalation policies and incident records | Workflow automation is not automatically root-cause diagnosis |
| Governed operational automation | Repeated requests or changes need a controlled execution path | Runners, scoped identities, approval policies and recovery procedures | Artifact generation is not verified apply or rollback |
| Developer / delivery agent | The desired output is a code change, test, pipeline fix or PR | Repository access, CI environments, branch protection and review ownership | Repository success is not a production service-health guarantee |
| Agent framework / managed runtime | You need custom behavior and can own its engineering | Tools, prompts, evaluations, hosting, security and on-call support | Extensibility is not an already-shipped SRE workflow |
| Data / business / identity specialist | The task belongs to a specific data platform or business domain | Domain permissions, enterprise systems and product-specific licensing | Do not infer general infrastructure capability from a domain-specific example |

## Build a shortlist, not a shopping list

1. State the result you want a person to achieve faster or more reliably.
2. Check products already in your stack before adding integration and governance work.
3. Exclude options that cannot meet your data, identity or availability constraints.
4. Compare two or three plausible candidates on the same workload; the number is a practical suggestion, not a research finding.
5. Expand the scope only after the initial workflow has a verified outcome and an owner.

[Browse the classified Platform Directory]({{ "/platforms/" | relative_url }}) · [Plan a pilot with the Buyer Guide]({{ "/platform-overview/" | relative_url }})

The [historical archetype analysis]({{ "/history/2025-archetypes/" | relative_url }}) is preserved separately; its older capability rankings are not revalidated here.
