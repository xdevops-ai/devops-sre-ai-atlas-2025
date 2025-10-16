---
layout: default
title: AWS Strands SDK
parent: Platform Directory
---

# AWS Strands SDK

Activities: P/L | Diagnostics: P/M | Provisioning: Y/M  <br>
Event ontology: P/L | Observability: P/M | Confidence: High

**Build style / interface —** Code-first SDK for Python and Node.  
**What it actually does —** A model-driven agent framework that plans and acts via tools, with deployments on AWS Lambda, Fargate, EKS, and EC2.  
**Data / telemetry —** Agent plans and tool calls traced via OpenTelemetry.  
**Interoperability —** Supports the MCP standard and agent-to-agent communication; integrates AWS services and community toolpacks.  
**Deployment model —** Runs in your own AWS account.  
**Notes —** Bring your own memory and knowledge base; strong tracing and governance hooks.

**UKM Snapshots:**
ingest P/L, index N/L, retrieval P/M, governance P/M, overall medium-low  <br>
**Note:** Ingestion & Validation: P/L; The Strands SDK itself doesn’t ingest domain knowledge for you; Normalization & Enrichment: P/M; Strands emphasizes a model-agnostic, tool-based architecture brightdata
