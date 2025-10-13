---
layout: default
title: Community Resources
nav_order: 90
---

# 🤝 Community Resources

Welcome! This page consolidates ways to contribute, ask questions, and track work for the **DevOps & SRE AI Platforms Atlas**.

## Contribute
- 📝 Update or add a platform card via GitHub Issues: {% if site.github and site.github.repository_url %}{{ site.github.repository_url }}/issues{% else %}https://github.com/<ORG>/<REPO>/issues{% endif %}.
- 🔧 Open a pull request: {% if site.github and site.github.repository_url %}{{ site.github.repository_url }}/pulls{% else %}https://github.com/<ORG>/<REPO>/pulls{% endif %}.
- 📄 Read the contribution guide: {% if site.github and site.github.repository_url %}{{ site.github.repository_url }}/blob/main/CONTRIBUTING.md{% else %}CONTRIBUTING.md{% endif %}.

## Discuss
- 💬 Join discussions: {% if site.github and site.github.repository_url %}{{ site.github.repository_url }}/discussions{% else %}https://github.com/<ORG>/<REPO>/discussions{% endif %}.
- 🗓️ Community meetups: [Bucharest XDevOps Meetup](https://www.meetup.com/bucharest-xdevops-meetup-group/).

## Governance & Policies
- 🛡️ Code of Conduct: {% if site.github and site.github.repository_url %}{{ site.github.repository_url }}/blob/main/CODE_OF_CONDUCT.md{% else %}CODE_OF_CONDUCT.md{% endif %}.
- 📜 License: {{ '/LICENSE' | relative_url }}

## Roadmap
- 🗺️ Track milestones: {% if site.github and site.github.repository_url %}{{ site.github.repository_url }}/milestones{% else %}https://github.com/<ORG>/<REPO>/milestones{% endif %}.
- 📌 Backlog: {% if site.github and site.github.repository_url %}{{ site.github.repository_url }}/projects{% else %}https://github.com/<ORG>/<REPO>/projects{% endif %}.

*Tip:* If any link above 404s, replace `<ORG>/<REPO>` with your repository path or enable the `jekyll-github-metadata` plugin.
