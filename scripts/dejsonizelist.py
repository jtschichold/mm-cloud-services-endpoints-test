#!/usr/bin/env python3

import sys
import json
import ipaddress
import argparse
import re

from typing import Dict, Callable, Any, List, Set


VERSION = "0.0.0alpha" # you got the point, right?

INVALID_TOKEN_RE = re.compile(r'(?:[^\./+=\?&]+\*[^\./+=\?&]*)|(?:[^\./+=\?&]*\*[^\./+=\?&]+)')
BROAD_PATTERN = re.compile(r'^(?:\*\.)+[a-zA-Z]+(?::[0-9]+)?$')


def ip_handler(e: str) -> List[str]:
    try:
        ipaddress.ip_network(e)
    except ValueError as _:
        return []

    return [e]


def panosurl_handler(e: str) -> List[str]:
    if not isinstance(e, str):
        return []

    xe = INVALID_TOKEN_RE.sub('*', e)
    if xe != e:
        # url changed, invalid tokens detected
        # check if the pattern is now too broad
        hostname = e
        if '/' in hostname:
            hostname, _ = hostname.split('/', 1)
        if BROAD_PATTERN.match(hostname) is not None:
            return []

    if xe.startswith('*'):
        return [xe[2:], xe]

    return [xe]


ITYPES: Dict[str,Dict[str,Callable[[str],List[str]]]] = {
    'ip': {'handler': ip_handler},
    'pan-os-url': {'handler': panosurl_handler}
}


def parse_args() -> Any:
    parser = argparse.ArgumentParser(description='Process a JSON list from stdin and produces a plain text version of it.')
    parser.add_argument('--type', '-t', action='store',
                        choices=['ip', 'pan-os-url'],
                        required=True,
                        help='type of the entries (choices: ip, pan-os-url)')
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    inlist = json.load(sys.stdin)
    if not isinstance(inlist, list):
        raise ValueError("Input is not a list")

    handler = ITYPES[args.type]['handler']
    result: Set[str] = set()
    for e in inlist:
        result = result.union(handler(e))

    for r in sorted(result):
        print(r)


if __name__ == "__main__":
    main()
