---
layout: default
title: Qovery Migration Agent
parent: Platform Directory
---

# Qovery Migration Agent

**Activities**: P/L | **Diagnostics**: P/L | **Provisioning**: Y/H  <br>
**Event ontology**: N/L | **Observability**: P/L | **Confidence**: High

**Build style / interface —** Code-first; open-source repo plus web UI.  
**What it actually does —** Scans applications and generates Terraform and Dockerfiles to migrate PaaS workloads to cloud, providing effort estimates.  
**Data / telemetry —** One-time analysis and configuration output.  
**Interoperability —** Supports Terraform/Docker ecosystems and integrates with the Qovery platform.  
**Deployment model —** Open-source agent with a Qovery cloud service.  
**Notes —** Produces artifacts but does not run live observability.

**UKM Snapshots:**
ingest P/L, index N/L, retrieval P/L, governance P/L, overall Low-Medium  <br>
**Note:** Knowledge: consumes product-native and BYO sources.

**UAM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Activities: guided actions with approvals

**UDM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Diagnostics: anomaly detection & triage

**UOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Observability: ingests platform telemetry

**UEOM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Ontology: product-native with adapters

**UPM Snapshots:**
ingest —, index —, retrieval —, governance —, overall —  <br>
**Note:** Provisioning: integrates with IaC/tools for apply; cloud-hosted service
**Links —** [Official Site](https://migrate.qovery.com/), [Docs](https://github.com/Qovery/qovery-migration-ai-agent), [Blog](https://www.qovery.com/blog/open-source-devops-ai-agent--effortless-migration-from-heroku-to-aws)
