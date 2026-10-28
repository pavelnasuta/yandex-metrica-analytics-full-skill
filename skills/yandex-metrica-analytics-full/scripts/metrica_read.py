#!/usr/bin/env python3
"""Read-only helper for the Yandex Metrica Management and Reporting APIs."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_URL = 'https://api-metrika.yandex.net'

SAFE_DIMENSIONS = {
    'ym:s:trafficSource', 'ym:s:lastTrafficSource', 'ym:s:sourceEngine',
    'ym:s:searchEngine', 'ym:s:socialNetwork', 'ym:s:referalSource',
    'ym:s:advEngine', 'ym:s:lastUTMSource', 'ym:s:lastUTMMedium',
    'ym:s:lastUTMCampaign', 'ym:s:lastUTMContent', 'ym:s:lastUTMTerm',
    'ym:s:firstUTMSource', 'ym:s:firstUTMMedium', 'ym:s:firstUTMCampaign',
    'ym:s:regionCountry', 'ym:s:regionCountryName', 'ym:s:regionCity',
    'ym:s:regionCityName', 'ym:s:startURL', 'ym:s:browser', 'ym:s:operatingSystem',
    'ym:s:deviceCategory', 'ym:s:datePeriodday', 'ym:s:datePeriodweek',
    'ym:s:datePeriodmonth',
}
SAFE_METRICS = {
    'ym:s:visits', 'ym:s:users', 'ym:s:pageviews', 'ym:s:bounceRate',
    'ym:s:pageDepth', 'ym:s:avgVisitDurationSeconds', 'ym:s:newUsers',
    'ym:s:newUsersShare', 'ym:s:ecommercePurchases', 'ym:s:ecommerceRevenue',
}
GOAL_METRIC = re.compile(r'^ym:s:goal\d+(?:visits|users|conversionRate|reaches|revenue)$')
FILTER_FIELD = re.compile(r'ym:[a-z]+:[A-Za-z0-9]+')


def is_safe_metric(field: str) -> bool:
    return field in SAFE_METRICS or bool(GOAL_METRIC.fullmatch(field))


def validate_report(args: argparse.Namespace) -> str | None:
    metrics = [field.strip() for field in args.metrics.split(',') if field.strip()]
    dimensions = [field.strip() for field in args.dimensions.split(',') if field.strip()]
    unsafe_metrics = [field for field in metrics if not is_safe_metric(field)]
    unsafe_dimensions = [field for field in dimensions if field not in SAFE_DIMENSIONS]
    filter_fields = FILTER_FIELD.findall(args.filters)
    unsafe_filters = [field for field in filter_fields if field not in SAFE_DIMENSIONS and not is_safe_metric(field)]
    sort_field = args.sort.lstrip('-')
    unsafe_sort = [sort_field] if sort_field and sort_field not in SAFE_DIMENSIONS and not is_safe_metric(sort_field) else []
    if unsafe_metrics or unsafe_dimensions or unsafe_filters or unsafe_sort:
        rejected = unsafe_metrics + unsafe_dimensions + unsafe_filters + unsafe_sort
        return 'Unsafe report field(s) rejected by the aggregate-only policy: ' + ', '.join(sorted(set(rejected)))
    return None


def token() -> str:
    value = os.environ.get('YANDEX_METRICA_TOKEN', '')
    if not value:
        env_file = Path(os.environ.get('HERMES_HOME', str(Path.home() / '.hermes'))) / '.env'
        try:
            for line in env_file.read_text(encoding='utf-8').splitlines():
                match = re.match(r'^\s*YANDEX_METRICA_TOKEN\s*=\s*(.*?)\s*$', line)
                if match:
                    value = match.group(1).strip().strip('"\'')
                    break
        except OSError:
            pass
    if not value:
        raise RuntimeError('YANDEX_METRICA_TOKEN is not available in approved secret storage.')
    return value


def get(path: str, params: dict[str, str]) -> dict:
    query = urlencode({key: value for key, value in params.items() if value not in ('', None)})
    url = f'{BASE_URL}{path}' + (f'?{query}' if query else '')
    request = Request(url, headers={'Authorization': f'OAuth {token()}', 'Accept': 'application/json'})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def output(payload: dict) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description='Read-only Yandex Metrica helper. Token is read from YANDEX_METRICA_TOKEN.')
    commands = root.add_subparsers(dest='command', required=True)

    counters = commands.add_parser('counters', help='List accessible counters')
    counters.add_argument('--search', default='', help='Optional name or site filter')
    counters.add_argument('--limit', default='100')

    goals = commands.add_parser('goals', help='List goals for one counter')
    goals.add_argument('--counter', required=True)

    report = commands.add_parser('report', help='Run an aggregate Reporting API query')
    report.add_argument('--counter', required=True)
    report.add_argument('--metrics', default='ym:s:visits,ym:s:users,ym:s:pageviews')
    report.add_argument('--dimensions', default='')
    report.add_argument('--date1', default='')
    report.add_argument('--date2', default='')
    report.add_argument('--filters', default='')
    report.add_argument('--sort', default='')
    report.add_argument('--limit', default='100')
    report.add_argument('--accuracy', default='full', choices=('full', 'medium', 'low'))
    report.add_argument('--type', default='data', choices=('data', 'bytime', 'drilldown', 'comparison'))
    return root


def main() -> int:
    args = parser().parse_args()
    if args.command == 'report':
        unsafe = validate_report(args)
        if unsafe:
            print(unsafe, file=sys.stderr)
            return 2
    try:
        if args.command == 'counters':
            output(get('/management/v1/counters', {'per_page': args.limit, 'search_string': args.search}))
        elif args.command == 'goals':
            output(get(f'/management/v1/counter/{args.counter}/goals', {}))
        else:
            output(get(f'/stat/v1/{args.type}', {
                'ids': args.counter, 'metrics': args.metrics, 'dimensions': args.dimensions,
                'date1': args.date1, 'date2': args.date2, 'filters': args.filters,
                'sort': args.sort, 'limit': args.limit, 'accuracy': args.accuracy,
            }))
    except (HTTPError, URLError, RuntimeError) as error:
        print(f'Read-only Metrica request failed: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
