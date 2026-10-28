---
name: yandex-metrica-analytics-full
description: Analyze Yandex Metrica data for product decisions.
version: 1.0.0
author: Pavel Nasuta, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [yandex-metrica, web-analytics, seo, marketing, product]
    related_skills: []
---

# Yandex Metrica Analytics Full

Turn aggregate Yandex Metrica data into a decision that can be checked later. This public release is read-only: it retrieves counters, configured goals, and aggregate reports; it does not change Metrica or connect additional services.

## When to Use

- Diagnose a traffic, engagement, goal, SEO, campaign, or product-funnel signal.
- Prepare a decision-oriented weekly digest or a low-noise alert design.
- Explain what the available data supports, what remains a hypothesis, and what to check next.

Do not use this workflow for raw Logs API exports, session-level data, re-identification, credential collection, budget decisions without cost data, or Metrica configuration changes.

## Prerequisites

- An OAuth token with **only** `metrika:read` and an account that can view the required counter.
- Store the token as `YANDEX_METRICA_TOKEN` in the host's approved secret storage. Never paste it into chat, a skill file, a report, or a repository.
- A counter, time period, and decision question. If the KPI or goal meaning is unclear, use the brief before querying.

Do not request or connect Webmaster, advertising, CRM, or another data source unless the user explicitly asks. Those sources can be named as optional future extensions when they would materially improve a conclusion.

## Data boundaries

Metrica supports aggregate evidence about traffic, engagement, configured goals, sources, campaigns, devices, geography, and the whitelisted report dimensions in `scripts/metrica_read.py`.

Metrica alone does not prove search rankings or indexing, media cost, CAC, ROAS, ROI, profit, retention, or a product-funnel stage whose goal/event meaning was never defined. Never replace a missing cut with a plausible proxy.

## Procedure

1. **Write the decision brief.** Complete [the brief](templates/analytics-brief.md) from the request: counter, timezone, period, equal comparison, KPI, guardrail, goal map, decision owner, and review date. Completion: every conclusion has a defined metric and scope.
2. **Read configuration first.** Use the helper to read the accessible counter and its goals before interpreting a goal metric. Completion: the report uses the requested counter and a goal with a confirmed business meaning.
3. **Retrieve the smallest aggregate report.** Run the helper through the host terminal. Start with totals; add only the dimensions needed to explain a material movement. Completion: the API response matches the requested counter and exact period.
4. **Interpret with boundaries.** Follow [the operating model](references/analytics-operating-model.md) and [the role playbooks](references/role-playbooks.md). Compare equivalent periods, show absolute volume with rates, disclose sampling or response limitations, and separate facts from explanations. Completion: the output names the strongest supported interpretation and the material uncertainty.
5. **Recommend one next action.** State owner, success metric, guardrail, and review date. Completion: a reader can decide what to do without treating a correlation as proof of cause.

## Read-only helper

Run these from the installed skill directory through the host terminal:

```bash
python3 scripts/metrica_read.py counters
python3 scripts/metrica_read.py goals --counter COUNTER_ID
python3 scripts/metrica_read.py report --counter COUNTER_ID --date1 YYYY-MM-DD --date2 YYYY-MM-DD --metrics ym:s:visits,ym:s:users
```

The helper makes only GET requests and rejects report fields outside its aggregate-only allowlist. It never saves exports or mutates Metrica.

## Outputs

Write in the user's language. Include the counter and exact period; comparable values and segment contribution where relevant; available source and missing evidence; separate facts, hypotheses, and recommendation; one action with an owner and review date.

Use [the weekly digest template](templates/weekly-digest.md) for recurring reporting. Follow [the digest and alert rules](references/digests-and-alerts.md) before proposing automation.

## Verification

- Confirm that the counter, timezone, and period match the brief.
- Read current goals before interpreting a goal metric.
- Disclose sampling, limited disclosure, low volume, tracking changes, campaign changes, or an unequal comparison when material.
- Do not calculate CAC, ROAS, or ROI without cost data; do not infer search rankings from organic traffic.
- Confirm that the proposed action has a success metric, guardrail, owner, and review date.

## References

- [Analytics operating model](references/analytics-operating-model.md)
- [Role playbooks](references/role-playbooks.md)
- [Evidence and interpretation](references/interpreting-data.md)
- [Digests and alerts](references/digests-and-alerts.md)
- [Analytics brief](templates/analytics-brief.md)
- [Weekly digest](templates/weekly-digest.md)
