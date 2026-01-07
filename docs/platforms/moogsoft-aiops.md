---
layout: default
title: Moogsoft — AIOps & Incident Correlation
parent: Platform Directory
---

# Moogsoft — AIOps & Incident Correlation

**Activities**: P/M | **Diagnostics**: Y/M | **Provisioning**: N/L  
**Event ontology**: P/M | **Observability**: P/M | **Confidence**: Medium

**Build style / interface —** SaaS incident intelligence platform with a web UI, Situation Room, and collaboration timelines; integrates with chat and ITSM tools.  
**What it actually does —** Applies ML-based noise reduction and correlation to group alerts into incidents, highlights probable root-cause alerts, and surfaces similar historical incidents to accelerate triage and response.  
**Data / telemetry —** Alert and event streams from monitoring and observability tools; optional metric ingestion for anomaly detection; change and context metadata from external systems.  
**Interoperability —** Wide integration ecosystem including Datadog, Dynatrace, New Relic, Splunk, Prometheus-based tools, ServiceNow, Jira, PagerDuty, Slack, and Microsoft Teams.  
**Deployment model —** SaaS (cloud-hosted; now part of Dell APEX AIOps Incident Management).  
**Notes —** Focused on alert correlation and incident intelligence; remediation and provisioning actions are executed via external automation or ITSM integrations.

---

## 🧠 UKM Snapshots
ingest P/M, index P/M, retrieval P/M, governance P/L, overall low-medium  

**Note:** Stores incident context, alert history, and resolution notes; limited enterprise knowledge management beyond incidents.

---

## ⚙️ UAM Snapshots
ingest P/M, index P/M, retrieval P/M, governance P/L, overall medium  

**Note:** Maintains incident timelines, ownership, and status changes; deeper activity replay depends on integrated tools.

---

## 🔍 UDM Snapshots
ingest Y/M, index Y/M, retrieval Y/M, governance P/M, overall medium  

**Note:** Strong alert correlation and anomaly detection; RCA is probabilistic and evidence-backed rather than causal-graph based.

---

## 👁️ UOM Snapshots
ingest P/M, index P/L, retrieval P/M, governance P/L, overall low-medium  

**Note:** Consumes telemetry from upstream observability platforms; users pivot to source dashboards for deep analysis.

---

## 🧬 UEOM Snapshots
ingest P/M, index P/M, retrieval P/M, governance P/L, overall medium  

**Note:** Incident-centric ontology linking alerts, services, and changes; limited full-stack workload topology.

---

## 🚀 UPM Snapshots
ingest N/L, index N/L, retrieval N/L, governance N/L, overall low  

**Note:** No native provisioning or rollback; actions are delegated to automation platforms and runbooks.

---

**Latest updates —** Integrated into Dell APEX AIOps portfolio with continued enhancements to correlation rules, workflows, and UI (2024–2025).  
**Links —**  
- [Official](https://www.moogsoft.com)  
- [Dell] (https://www.dell.com/en-us/dt/apex/aiops.htm ) 
- [Docs](https://docs.moogsoft.com)
