# Interpreting Metrica data

## Evidence before recommendations

- Define the decision before choosing metrics; vanity traffic is not a business outcome.
- Compare equivalent periods and disclose material differences in traffic mix, campaign activity, release dates, or calendar effects.
- Check counter status, goals, filters, attribution model, and report sampling before interpreting a conversion movement.
- Treat a correlation as a hypothesis unless an experiment, reliable causal design, or an independently verified mechanism supports it.
- Prefer contribution analysis: a channel can rise while total performance falls, and a rate can rise while absolute conversions fall.

## Diagnostic sequence

1. Verify the total signal: visits, users, target action, conversion rate, and relevant guardrail.
2. Decompose by source/campaign, landing page, device, geography, and new/returning user when the decision needs it.
3. Identify the smallest segment that explains material change.
4. Check whether tracking or a goal definition changed.
5. Write competing explanations and the cheapest next check or experiment.

## Decision format

**Signal:** what moved, for which counter and period.

**Evidence:** the compared values and the segment contribution.

**Caveat:** sampling, small volume, changing definitions, or another boundary.

**Interpretation:** a bounded hypothesis, not a claim of cause.

**Action:** one owner, one action, and a success/guardrail metric with a review date.

## Quality thresholds

- Do not alert on a percentage change without showing absolute volume.
- Do not interpret a goal before a fresh goals read confirms its type and status.
- Do not compare campaigns with different attribution or cost coverage as if they are equivalent.
- If the requested conclusion cannot be supported by Metrica, say which additional source is needed.
- Do not replace an unavailable page, event, or funnel cut with a nearby aggregate; disclose the limitation because a plausible proxy can produce a wrong decision.
