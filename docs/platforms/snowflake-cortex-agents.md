---
layout: default
title: Snowflake Cortex Agents
parent: Platform Directory
---

# Snowflake Cortex Agents

**Activities**: Y/M | **Diagnostics**: P/L | **Provisioning**: P/L  <br>
**Event ontology**: Y/H | **Observability**: P/L | **Confidence**: Medium

**Build style / interface —** Low-code assistant builder embedded in the Snowflake Data Cloud, using Cortex Analyst and Cortex Search. Agents are authored via SQL, Python and declarative YAML and run inside your Snowflake account.  
**What it actually does —** Provides domain-specific AI assistants for data pipelines and MLOps. Cortex Analyst answers questions on your Snowflake data; Cortex Search builds chatbots on top of your schemas and UDFs. Agents can orchestrate workflows via built-in functions, call UDFs or external services, and return structured responses.  
**Data / telemetry —** Uses Snowflake tables and query history as both data and telemetry. Conversation logs and monitoring APIs record agent interactions; SQL/Python tasks provide observability signals.  
**Interoperability —** Integrates via Snowpark, UDFs/stored procedures and REST APIs. Agents can call external services via system-defined functions and return results into Snowflake.  
**Deployment model —** Runs as a managed service inside your Snowflake account. There is no separate runtime; agents deploy via SQL/Python and operate within Snowflake's security and governance controls.  
**Notes —** Designed for data and MLOps use cases; not general DevOps/SRE. Diagnostic and provisioning capabilities are limited; its strengths are knowledge and ontology (UEOM/UKM) and activities (UAM).

**UKM Snapshots:** 
ingest medium-high, index medium-high, retrieval medium-high, governance medium-high, overall medium-high  <br>
**Note:** Coverage — Ingest medium-high; Index medium-high; Retrieval medium-high; Governance medium-high; Overall medium-high


**UAM Snapshots:**   
ingest medium-high, index medium-high, retrieval medium-high, governance medium-high, overall medium-high  <br>
**Note:** Coverage — Ingest medium-high; Index medium-high; Retrieval medium-high; Governance medium-high; Overall medium-high


**UDM Snapshots:**   
ingest low-medium, index low-medium, retrieval low-medium, governance low-medium, overall low-medium  <br>
**Note:** Coverage — Ingest low-medium; Index low-medium; Retrieval low-medium; Governance low-medium; Overall low-medium


**UOM Snapshots:**   
ingest low-medium, index low-medium, retrieval low-medium, governance low-medium, overall low-medium  <br>
**Note:** Coverage — Ingest low-medium; Index low-medium; Retrieval low-medium; Governance low-medium; Overall low-medium


**UEOM Snapshots:**   
ingest high, index high, retrieval high, governance high, overall high  <br>
**Note:** Coverage — Ingest high; Index high; Retrieval high; Governance high; Overall high


**UPM Snapshots:**   
ingest low-medium, index low-medium, retrieval low-medium, governance low-medium, overall low-medium  <br>
**Note:** Coverage — Ingest low-medium; Index low-medium; Retrieval low-medium; Governance low-medium; Overall low-medium


**Latest updates —** Cortex Agents docs/guide expanded (2025).
**Links —** [Official Site](https://www.snowflake.com/en/product/features/cortex/), [Docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents), [Blog](https://docs.snowflake.com/en/user-guide/snowflake-cortex/snowflake-intelligence)
