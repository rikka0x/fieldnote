#!/usr/bin/env python3
"""Tiny public-safe helper: fetch a page title without storing cookies or secrets."""

from __future__ import annotations

import html
import re
import sys
import urllib.request


TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: link-title-check.py <https-url>", file=sys.stderr)
        return 2

    url = sys.argv[1]
    if not url.startswith(("https://", "http://")):
        print("error: expected http(s) url", file=sys.stderr)
        return 2

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "fieldnote-link-title-check/0.1"},
    )
    with urllib.request.urlopen(req, timeout=10) as res:
        body = res.read(512_000).decode("utf-8", "replace")
        final_url = res.geturl()

    match = TITLE_RE.search(body)
    title = html.unescape(match.group(1)).strip() if match else "(no title found)"
    title = re.sub(r"\s+", " ", title)

    print(f"url: {final_url}")
    print(f"title: {title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
