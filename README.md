# Yandex Metrica Analytics Full Skill

A read-only workflow for turning aggregate Yandex Metrica reports into decisions for web analytics, SEO, marketing, and product work.

## What it does

- Reads accessible counters, current goals, and aggregate reports through the Yandex Metrica API.
- Uses a decision brief, an explicit goal map, equivalent-period comparison, and a clear separation between facts, hypotheses, and recommendations.
- Produces weekly-digest and alert-design inputs without exporting raw sessions or changing Metrica.

## Install in Hermes

```bash
hermes skills tap add pavelnasuta/yandex-metrica-analytics-full-full-skill
hermes skills install pavelnasuta/yandex-metrica-analytics-full-full-skill/skills/yandex-metrica-analytics-full
```

The canonical workflow is `skills/yandex-metrica-analytics-full/SKILL.md`. Thin adapters for Claude Code, Codex, and generic `AGENTS.md` users point to the same workflow.

## Configuration

Use an OAuth token with `metrika:read` only. Store it in the host's approved secret storage as `YANDEX_METRICA_TOKEN`; never commit it or paste it into an agent conversation.

The token owner must have view access to the requested Metrica counter. This release does not require or configure tokens for Yandex Webmaster, advertising platforms, CRM, or other services.

## Limitations

The workflow does not change Metrica, read raw Logs API data, or retrieve session-level data. It does not calculate CAC, ROAS, ROI, profit, search rankings, or indexing from Metrica alone. When another source would materially improve a decision, the workflow names it as an optional future extension and does not request or connect it by default.

## Verification

The package includes offline tests for its public contract and report-field safety:

```bash
python3 -m unittest discover -s tests -v
```

The helper itself is read-only:

```bash
python3 skills/yandex-metrica-analytics-full/scripts/metrica_read.py --help
```

## Support

Report bugs or request improvements through [GitHub Issues](https://github.com/pavelnasuta/yandex-metrica-analytics-full-full-skill/issues).

## Release notes

### v1.0.0

- First public release.
- Read-only Metrica reports, goal-aware decision briefs, role playbooks, digest template, and explicit source boundaries.
