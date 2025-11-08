---
layout: default
title: HashiCorp Terraform MCP + Project Infragraph
parent: Platform Directory
---

# HashiCorp Terraform MCP + Project Infragraph

**Activities**: P/M | **Diagnostics**: N/L | **Provisioning**: Y/M  <br>
**Event ontology**: Y/M | **Observability**: N/L | **Confidence**: Medium

**Build style / interface —** MCP servers exposing safe IaC actions to agents; Terraform Cloud/CLI.  
**What it actually does —** Lets AI agents plan/apply Terraform with policy/audit via MCP; Infragraph unifies resource graph context for safer changes.  
**Data / telemetry —** Terraform state/plan; resource graph.  
**Interoperability —** MCP standard; Terraform Registry and providers.  
**Deployment model —** Open-source MCP server + HCP/Terraform Cloud.  
**Notes —** Pair with an observability brain for diagnostics.

**UKM Snapshots:**  
run history P/M

**UAM Snapshots:**  
audit trail Y/M (VCS/TF Cloud)

**UDM Snapshots:**  
N/L

**UOM Snapshots:**  
N/L

**UEOM Snapshots:**  
resource graph Y/M

**UPM Snapshots:**  
plan/apply Y/M, rollback via IaC patterns

**Latest updates —** Terraform MCP Server released (May–Jul 2025).  
**Links —** [Blog](https://www.hashicorp.com/en/blog/build-secure-ai-driven-workflows-with-new-terraform-and-vault-mcp-servers), [GitHub](https://github.com/hashicorp/terraform-mcp-server)
