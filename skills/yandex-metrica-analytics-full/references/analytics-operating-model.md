# Analytics operating model

## Decision brief

Before querying, complete `templates/analytics-brief.md` in the conversation or use the information already supplied by the user. Confirm:

- counter and site timezone;
- business decision and accountable owner;
- primary KPI, guardrail, and the goal IDs that define them;
- date range, equal comparison period, and materiality threshold;
- required breakdowns and review date.

If the brief is incomplete, do not invent a business KPI or label a goal as activation, purchase, or retention. State the missing definition and either provide a traffic overview or ask the one question that changes the analysis.

## Source boundaries

The default data source is Yandex Metrica only. It can support aggregate evidence about traffic, engagement, configured goals, sources, campaigns, devices, geography, and landing URLs allowed by the aggregate-only policy.

Metrica alone does not establish:

- search positions, search queries, indexing, or snippet changes;
- media cost, CAC, ROAS, ROI, or profit;
- product retention, funnel stages, or user intent unless goals and their meanings are explicitly defined.

Do not calculate CAC, ROAS, or ROI without cost data. Do not infer rankings from organic traffic. Do not request or connect an additional source, token, browser session, or integration unless the user explicitly asks to add it. When a conclusion needs another source, name it as an optional future extension and give the strongest conclusion supported by Metrica alone.

## Interpretation rules

1. Read goals before using goal metrics; record each goal ID, type, and business meaning from the brief.
2. Compare equal periods and disclose calendar, campaign, release, tracking, attribution, or mix differences.
3. Show absolute volume alongside a percentage movement. Do not treat a low-base percentage as a material signal.
4. Check the API response for sampling or limited-disclosure indicators and state any material limitation.
5. Decompose a total movement before recommending action: source/campaign, landing URL, device, geography, and new/returning users only when relevant and sufficiently large.
6. Separate observed facts, competing explanations, and the next verification. A correlation is not a causal claim.
7. Finish with one decision-ready action: owner, success metric, guardrail, and review date.

## Role-specific instructions

### Web analytics

Start with the KPI and its guardrail, then find the smallest aggregate segment that materially explains the movement. If goals, filters, or tracking changed, prioritize an instrumentation check over a growth recommendation.

### SEO

Assess organic visits, engagement, goal rate, landing URLs, devices, and locations. Phrase rank, demand, snippet, and indexing explanations as hypotheses. Recommend a future Webmaster/Search Console check only when it would change the next action; never ask to connect it by default.

### Marketing and paid acquisition

Assess traffic quality and configured downstream goals by confirmed source, UTM, campaign, content, and landing URL. Without cost data, recommend only a traffic-quality or conversion test; do not call a channel efficient or recommend a budget change based on ROI.

### Product

Use the goal map to identify acquisition, activation, conversion, and friction only when each stage has a defined event/goal. If the map is absent, report the measurement-design gap rather than inventing a funnel or retention conclusion.

### Executive support

Lead with material movement, driver, risk, and one decision request. Keep unknowns visible and exclude channel or team rankings without comparable scope and baselines.

## Review checklist

Before delivery, verify that the counter and period are correct, the comparison is equivalent, goal definitions are fresh, absolute volume is shown, material response limitations are disclosed, and every recommendation has an owner and review date.
