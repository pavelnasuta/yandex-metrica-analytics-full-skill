# Role playbooks

## Capability gate

Before selecting a playbook, match the requested decision to the approved data surface. The current aggregate helper supports high-level traffic, source/UTM, geography, device, browser, and goal-metric cuts. It does not support page URLs, custom-event parameters, or a defined multi-step funnel. Do not substitute a nearby aggregate for the requested cut: state the gap and name the approved extension or external source required.

For any page-level output, use a separately reviewed URL-normalization workflow that strips query parameters, bounds the result to a ranked aggregate, and enforces a minimum-volume threshold. For product funnels, require an agreed goal-to-stage map before interpreting a leak.

## Web analytics

1. Start with traffic, users, engagement, and goal completion for the selected counter.
2. Compare the period with an equal preceding period and identify the biggest contribution to change by source, landing page, device, and geography.
3. Check tracking configuration and goal definitions before declaring a funnel shift.
4. End with one operational decision: investigate instrumentation, fix a leak, scale a source, or run a test.

## SEO

1. Use organic traffic, search-engine/source dimensions, landing pages, device, and location where appropriate.
2. Separate demand change from rank/snippet/indexing hypotheses; Metrica alone does not prove rankings.
3. Prioritize pages by organic visits, engagement, goal rate, and business relevance rather than pageviews alone.
4. Recommend a controlled content/technical change or identify Webmaster/Search Console as an optional future verification; never request credentials or connect it by default.

## Marketing and paid acquisition

1. Split results by source, medium, campaign, content, and landing page only when UTMs and attribution are confirmed.
2. Inspect volume, conversion rate, and a quality guardrail such as bounce rate or downstream goal rate. Without cost data, do not calculate or claim CAC, ROAS, ROI, or budget efficiency.
3. Do not call a channel successful because it bought cheap visits; connect it to activation or conversion.
4. Without cost data, return a traffic-quality or conversion-test recommendation, not a budget recommendation.

## Product

1. Define the activation or product event before looking at traffic.
2. Use only the stages in the approved goal map. If activation, conversion, or retention proxy is not defined by a goal/event, report the measurement gap instead of inventing a funnel.
3. Compare cohorts/segments only when their definitions are stable and data volume is sufficient.
4. Translate a detected leak into one product hypothesis, expected mechanism, owner, and success metric.

## Executive decision support

1. State the business question and one primary KPI.
2. Keep the narrative to material movement, drivers, risks, and a decision request.
3. Do not rank teams or channels without comparable baselines and scope.
4. Include only actions that have an owner and review date.
