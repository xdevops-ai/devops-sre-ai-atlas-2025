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

UKM Snapshot: ingest P/L, index N/L, retrieval P/M, governance Y/M, overall medium.
UAM Snapshot: ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium.
UDM Snapshot: ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium.
UOM Snapshot: ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium.
UEOM Snapshot: ingest N/L, index N/L, retrieval N/L, governance N/L, overall low.
UPM Snapshot: ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium.

Latest updates — Public preview and GA announcements; docs on creating PRs and review loop; industry press coverage.
Links — github.blog • docs.github.com • The Verge
