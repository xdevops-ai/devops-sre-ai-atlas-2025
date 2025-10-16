---
layout: default
title: AWS Strands SDK
parent: Platform Directory
---

# AWS Strands SDK

Activities: P/L | Diagnostics: P/M | Provisioning: Y/M  
Event ontology: P/L | Observability: P/M | Confidence: High

Build style / interface — Code-first SDK for Python and Node.  
What it actually does — A model-driven agent framework that plans and acts via tools, with deployments on AWS Lambda, Fargate, EKS, and EC2.  
Data / telemetry — Agent plans and tool calls traced via OpenTelemetry.  
Interoperability — Supports the MCP standard and agent-to-agent communication; integrates AWS services and community toolpacks.  
Deployment model — Runs in your own AWS account.  
Notes — Bring your own memory and knowledge base; strong tracing and governance hooks.

UKM Snapshots: 
ingest P/L, index N/L, retrieval P/M, governance P/M, overall medium-low
Note:   See analysis/baselines/knowledge.md (doc-platform.tar) for definitions and evaluation criteria.

UAM Snapshots:   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium
Note:   See analysis/baselines/activity.md (doc-platform.tar) for definitions and evaluation criteria.
UDM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/diagnostic.md (doc-platform.tar) for definitions and evaluation criteria.
UOM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/observability.md (doc-platform.tar) for definitions and evaluation criteria.
UEOM Snapshots:   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium
Note:   See analysis/baselines/ontology.md (doc-platform.tar) for definitions and evaluation criteria.
UPM Snapshots:   
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high
Note:   See analysis/baselines/provisioning.md (doc-platform.tar) for definitions and evaluation criteria.

Latest updates — Strands Agents SDK deep dive on architectures & observability (Jul 31, 2025).
Links — [Official Site](https://strandsagents.com/latest/), [Docs](https://strandsagents.com/latest/documentation/docs/), [Blog](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/)
