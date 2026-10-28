# Digests and alerts

## Recurring digests

A digest is a decision artifact, not a daily data dump. Define before scheduling:

1. Counter(s), timezone, and period.
2. Reader and business decision it supports.
3. Primary KPI, segment breakdown, and guardrail.
4. Comparison baseline and materiality threshold.
5. Destination and cadence.

Use `templates/weekly-digest.md`. Keep facts separate from hypotheses and recommendations. Do not create a recurring job until the user explicitly approves all five choices above.

## Alert design

- Alert on a material change relative to a stated baseline, not any normal day-to-day variance.
- Require both a relative and an absolute threshold, for example a conversion decline plus a minimum loss of goal completions.
- Prefer a two-stage alert: inexpensive read-only sentinel detects the signal; an agent interprets it with counter context before notifying.
- Deduplicate alerts by counter, metric, period, and threshold crossing.
- Do not create alert noise from a first-run baseline. Record baseline silently unless the user asks to surface current risks.
- Each alert must state metric, period, baseline, actual value, affected segment, confidence/caveat, and next check.

## Safe scheduling

Load `scheduled-agent-jobs` before creating a job. Pin its model/provider, preserve the explicit delivery target, run a low-risk representative check, and verify the completed delivery record. Never schedule raw Logs API exports by default.
