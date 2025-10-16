---
layout: default
title: GitHub Copilot Coding Agent
parent: Platform Directory
---

# GitHub Copilot Coding Agent

**Activities**: P/M | **Diagnostics**: P/M | **Provisioning**: P/L  <br>
**Event ontology**: N/L | **Observability**: P/M | **Confidence**: High

**Build style / interface —** PR/CLI; asynchronous cloud agent; Agents panel.  
**What it actually does —** Launches an isolated VM, clones your repository, runs tests and fixes, opens pull requests, and responds to reviews.  
**Data / telemetry —** Pull requests, commits, and CI logs plus agent status.  
**Interoperability —** GitHub Actions and CLI; managed connectors via MCP extension in docs.  
**Deployment model —** Runs as part of GitHub SaaS.  
**Notes —** Only applies infrastructure changes via IaC PRs; does not directly mutate runtime resources.

**UKM Snapshots:**
ingest P/L, index N/L, retrieval P/M, governance Y/M, overall medium  <br>
**Note:** Knowledge: BYO sources; governed ingestion & indexing.

**UAM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Activities: agent executes playbooks/workflows with policy

**UDM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Diagnostics: anomaly detection & triage; correlates metrics/traces/logs

**UOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Observability: ingests metrics/traces/logs/events

**UEOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Ontology: normalizes to standard schemas

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: SaaS-managed; limited direct apply; cloud-hosted service
**Links —** [Official Site](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent), [Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent), [Blog](https://www.theverge.com/news/669339/github-ai-coding-agent-fix-bugs)
