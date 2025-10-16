---
layout: default
title: AWS Strands SDK
parent: Platform Directory
---

# AWS Strands SDK

**Activities**: P/L | **Diagnostics**: P/M | **Provisioning**: Y/M  <br>
**Event ontology**: P/L | **Observability**: P/M | **Confidence**: High

**Build style / interface —** Code-first SDK for Python and Node.  
**What it actually does —** A model-driven agent framework that plans and acts via tools, with deployments on AWS Lambda, Fargate, EKS, and EC2.  
**Data / telemetry —** Agent plans and tool calls traced via OpenTelemetry.  
**Interoperability —** Supports the MCP standard and agent-to-agent communication; integrates AWS services and community toolpacks.  
**Deployment model —** Runs in your own AWS account.  
**Notes —** Bring your own memory and knowledge base; strong tracing and governance hooks.

**UKM Snapshots:** 
ingest P/L, index N/L, retrieval P/M, governance P/M, overall medium-low  <br>
**Note:** Ingestion & Validation: P/L; Normalization & Enrichment: P/M; Strands emphasizes a model-agnostic, tool-based architecture brightdata


**UAM Snapshots:**   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium  <br>
**Note:** Capture & Sessionization: P/M; Evidence Policy & Verification: P/L


**UDM Snapshots:**   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium  <br>
**Note:** Detection & Triggering: N/L; Analysis & Correlation: N/L; Any correlation of data or root cause reasoning must be programmed by the solution builder


**UOM Snapshots:**   
ingest P/M, index P/M, retrieval P/M, governance P/M, overall medium  <br>
**Note:** Instrumentation & Ingest: P/L; The Strands SDK itself doesn’t come with monitoring agents for applications, but it does instrument the AI agent’s own operations; Normalization & Enrichment: P/L; Any telemetry the agent u


**UEOM Snapshots:**   
ingest P/L, index P/L, retrieval P/L, governance P/L, overall low-medium  <br>
**Note:** Coverage — Ingest P/L; Index P/L; Retrieval P/L; Governance P/L; Overall low-medium


**UPM Snapshots:**   
ingest Y/M, index Y/M, retrieval Y/M, governance Y/M, overall medium-high  <br>
**Note:** Coverage — Ingest Y/M; Index Y/M; Retrieval Y/M; Governance Y/M; Overall medium-high


**Latest updates —** Strands Agents SDK deep dive on architectures & observability (Jul 31, 2025).
**Links —** [Official Site](https://strandsagents.com/latest/), [Docs](https://strandsagents.com/latest/documentation/docs/), [Blog](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/)
