---
layout: default
title: GitHub Copilot Coding Agent
parent: Platform Directory
---

# GitHub Copilot Coding Agent

Activities: P/M | Diagnostics: P/M | Provisioning: P/L  
Event ontology: N/L | Observability: P/M | Confidence: High

Build style / interface — PR/CLI; asynchronous cloud agent; Agents panel.  
What it actually does — Launches an isolated VM, clones your repository, runs tests and fixes, opens pull requests, and responds to reviews.  
Data / telemetry — Pull requests, commits, and CI logs plus agent status.  
Interoperability — GitHub Actions and CLI; managed connectors via MCP extension in docs.  
Deployment model — Runs as part of GitHub SaaS.  
Notes — Only applies infrastructure changes via IaC PRs; does not directly mutate runtime resources.

UKM Snapshots: 
ingest P/L, index N/L, retrieval P/M, governance Y/M, overall medium
Note:   See analysis/baselines/knowledge.md (doc-platform.tar) for definitions and evaluation criteria.

UAM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/activity.md (doc-platform.tar) for definitions and evaluation criteria.
UDM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/diagnostic.md (doc-platform.tar) for definitions and evaluation criteria.
UOM Snapshots:   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium
Note:   See analysis/baselines/observability.md (doc-platform.tar) for definitions and evaluation criteria.
UEOM Snapshots:   
ingest N/L, index N/L, retrieval N/L, governance N/L, overall low
Note:   See analysis/baselines/ontology.md (doc-platform.tar) for definitions and evaluation criteria.
UPM Snapshots:   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium
Note:   See analysis/baselines/provisioning.md (doc-platform.tar) for definitions and evaluation criteria.

Latest updates — Copilot coding agent GA (Sep 25, 2025).
Links — [Official Site](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent), [Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent), [Blog](https://www.theverge.com/news/669339/github-ai-coding-agent-fix-bugs)
